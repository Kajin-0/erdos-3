#!/usr/bin/env python3
"""Verify novel same-layer completion credit from the cyclic S7 output."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from export_simultaneous_deletion_transition import build_payload

COMPONENT = (1, 5, 61, 303, 1597, 8195, 323640)
EXPECTED_EXACT_STATES = 62
EXPECTED_OCCURRENCES = 63
EXPECTED_DUPLICATE = (61,)
EXPECTED_CATALOG_SHA256 = (
    "edbc0b27f56ce5a5cb5fbd4aa7a3818c093d34cd587ede906edcced1dce7b4b9"
)
EXPECTED = {
    2: {
        "domain": 950202,
        "full_invalid": 140722,
        "imported_invalid": 370,
        "novel_incremental": 140352,
        "novel_overlap": 46467,
        "novel_completion": 135943,
        "novel_completion_exclusive": 93885,
        "remaining": 809480,
        "positive_states": 54,
        "nonempty_states": 59,
        "fully_excluded_states": 1,
    },
    4: {
        "domain": 4986696,
        "full_invalid": 399445,
        "imported_invalid": 700,
        "novel_incremental": 398745,
        "novel_overlap": 121755,
        "novel_completion": 385457,
        "novel_completion_exclusive": 276994,
        "remaining": 4587251,
        "positive_states": 61,
        "nonempty_states": 62,
        "fully_excluded_states": 1,
    },
}
CERTIFICATE_SHA256 = (
    "0419cdeab12c1a8ab2f55e041a0259ffde77f90df7031be0736137502e6ff737"
)


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def parity_ok(value: int) -> bool:
    return value > 0 and v2(value) % 2 == 0


def canonical_set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def completion_coordinates(values: Iterable[int]) -> frozenset[int]:
    """Return missing coordinates of four-APs with exactly three points present."""
    present = set(values)
    ordered = sorted(present)
    completions: set[int] = set()
    for left_index, left in enumerate(ordered):
        for second in ordered[left_index + 1 :]:
            third = 2 * second - left
            if third in present:
                completions.add(3 * second - 2 * left)
                completions.add(2 * left - second)

            fourth = 3 * second - 2 * left
            if fourth in present:
                completions.add(2 * second - left)

            first = 3 * left - 2 * second
            if first in present:
                completions.add(2 * left - second)
    return frozenset(completions - present)


def brute_completion_coordinates(values: Iterable[int]) -> frozenset[int]:
    present = set(values)
    if len(present) < 3:
        return frozenset()
    span = max(present) - min(present)
    completions: set[int] = set()
    for step in range(1, span + 1):
        for first in range(min(present) - 3 * span, max(present) + 1):
            progression = [first + index * step for index in range(4)]
            mask = [value in present for value in progression]
            if sum(mask) == 3:
                completions.add(progression[mask.index(False)])
    return frozenset(completions)


def verify_completion_enumerator() -> None:
    ground = tuple(range(7))
    for mask in range(1 << len(ground)):
        values = {
            ground[index]
            for index in range(len(ground))
            if mask >> index & 1
        }
        if completion_coordinates(values) != brute_completion_coordinates(values):
            raise AssertionError(
                f"completion enumerator mismatch for {sorted(values)}"
            )


def support_sets(
    values: Iterable[int],
    upper: int,
) -> tuple[set[int], set[int], int]:
    """Return layer-collision and same-layer-completion separation support."""
    ordered = sorted(set(values))
    overlap: set[int] = set()
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            difference = right - left
            if difference <= upper and parity_ok(difference):
                overlap.add(difference)
            if difference % 2 == 0:
                separation = difference // 2
                if separation <= upper and parity_ok(separation):
                    overlap.add(separation)

    completions = completion_coordinates(ordered)
    completion_support: set[int] = set()
    for completion in completions:
        for value in ordered:
            difference = abs(completion - value)
            if difference <= upper and parity_ok(difference):
                completion_support.add(difference)
            if difference % 2 == 0:
                separation = difference // 2
                if separation <= upper and parity_ok(separation):
                    completion_support.add(separation)
    return overlap, completion_support, len(completions)


def build_state_records() -> tuple[list[dict[str, object]], int]:
    payload = build_payload(7)
    backbone = set(payload["backbone"]["values"])
    grouped: dict[tuple[int, ...], dict[str, object]] = {}
    occurrence_count = 0

    for occurrence in payload["recursive_shell_occurrences"]:
        if occurrence["source"] != "middle_fiber":
            continue
        source = occurrence["source_step"]
        if source not in COMPONENT:
            continue
        occurrence_count += 1
        values = tuple(occurrence["values"])
        scale = occurrence["shell_scale"]
        record = grouped.setdefault(
            values,
            {"scale": scale, "sources": []},
        )
        if record["scale"] != scale:
            raise AssertionError("exact state appeared at two shell scales")
        record["sources"].append(source)

    if occurrence_count != EXPECTED_OCCURRENCES:
        raise AssertionError(f"occurrence count mismatch: {occurrence_count}")
    if len(grouped) != EXPECTED_EXACT_STATES:
        raise AssertionError(f"exact state count mismatch: {len(grouped)}")
    duplicates = [
        values
        for values, record in grouped.items()
        if len(record["sources"]) > 1
    ]
    if duplicates != [EXPECTED_DUPLICATE]:
        raise AssertionError(f"unexpected exact duplicates: {duplicates!r}")

    records: list[dict[str, object]] = []
    for values, grouped_record in grouped.items():
        scale = int(grouped_record["scale"])
        imported = tuple(sorted(set(values) & backbone))
        novel = tuple(sorted(set(values) - backbone))
        record: dict[str, object] = {
            "state_sha256": canonical_set_hash(values),
            "sources": sorted(grouped_record["sources"]),
            "scale": scale,
            "size": len(values),
            "imported_size": len(imported),
            "novel_size": len(novel),
            "minimum": min(values),
            "maximum": max(values),
            "factors": {},
        }

        for factor in (2, 4):
            upper = (factor * scale - 1 - max(values)) // 2
            domain = {
                value
                for value in range(1, upper + 1)
                if parity_ok(value)
            }
            full_overlap, full_completion, full_coordinates = support_sets(
                {0, *values}, upper
            )
            (
                imported_overlap,
                imported_completion,
                imported_coordinates,
            ) = support_sets({0, *imported}, upper)
            full_invalid = domain & (full_overlap | full_completion)
            imported_invalid = domain & (
                imported_overlap | imported_completion
            )
            incremental = full_invalid - imported_invalid
            novel_overlap = (domain & full_overlap) - (
                domain & imported_overlap
            )
            novel_completion = (domain & full_completion) - (
                domain & imported_completion
            )
            novel_completion_exclusive = novel_completion - (
                domain & full_overlap
            )

            record["factors"][str(factor)] = {
                "upper": upper,
                "domain": len(domain),
                "full_invalid": len(full_invalid),
                "imported_invalid": len(imported_invalid),
                "novel_incremental": len(incremental),
                "novel_overlap": len(novel_overlap),
                "novel_completion": len(novel_completion),
                "novel_completion_exclusive": len(
                    novel_completion_exclusive
                ),
                "remaining": len(domain - full_invalid),
                "completion_coordinates": full_coordinates,
                "imported_completion_coordinates": imported_coordinates,
            }
        records.append(record)

    records.sort(
        key=lambda record: (
            record["scale"],
            record["minimum"],
            record["maximum"],
            record["state_sha256"],
        )
    )
    return records, occurrence_count


def aggregate(
    records: list[dict[str, object]],
    factor: int,
) -> dict[str, int]:
    fields = (
        "domain",
        "full_invalid",
        "imported_invalid",
        "novel_incremental",
        "novel_overlap",
        "novel_completion",
        "novel_completion_exclusive",
        "remaining",
    )
    rows = [record["factors"][str(factor)] for record in records]
    result = {
        field: sum(int(row[field]) for row in rows)
        for field in fields
    }
    result["positive_states"] = sum(
        int(row["novel_incremental"]) > 0 for row in rows
    )
    result["nonempty_states"] = sum(
        int(row["domain"]) > 0 for row in rows
    )
    result["fully_excluded_states"] = sum(
        int(row["domain"]) > 0 and int(row["remaining"]) == 0
        for row in rows
    )
    return result


def build_certificate() -> str:
    verify_completion_enumerator()
    records, occurrence_count = build_state_records()
    catalog = "\n".join(
        json.dumps(record, sort_keys=True, separators=(",", ":"))
        for record in records
    ) + "\n"
    catalog_hash = hashlib.sha256(catalog.encode("utf-8")).hexdigest()
    if catalog_hash != EXPECTED_CATALOG_SHA256:
        raise AssertionError(f"state catalog hash mismatch: {catalog_hash}")

    observed = {factor: aggregate(records, factor) for factor in (2, 4)}
    if observed != EXPECTED:
        raise AssertionError(f"aggregate mismatch: {observed!r}")

    lines = [
        "S7 CYCLIC SCC LOCAL COMPLETION CREDIT",
        "",
        "component=1,5,61,303,1597,8195,323640",
        f"raw_shell_occurrences={occurrence_count}",
        f"exact_numerical_states={len(records)}",
        "duplicate_exact_state=61",
        f"state_catalog_sha256={catalog_hash}",
        "",
        (
            "candidate_domain: 1 <= R <= "
            "floor((factor*L-1-max(X))/2), v2(R) even"
        ),
        (
            "imported_baseline: X intersect S7 minimum-translation "
            "backbone"
        ),
        "local_support: layer collision or same-layer 4-AP completion",
        (
            "novel_incremental: full local support minus imported-only "
            "local support"
        ),
        "",
    ]
    for factor in (2, 4):
        row = observed[factor]
        lines.extend(
            [
                f"factor{factor}_domain={row['domain']}",
                f"factor{factor}_full_invalid={row['full_invalid']}",
                (
                    f"factor{factor}_imported_invalid="
                    f"{row['imported_invalid']}"
                ),
                (
                    f"factor{factor}_novel_incremental="
                    f"{row['novel_incremental']}"
                ),
                f"factor{factor}_novel_overlap={row['novel_overlap']}",
                (
                    f"factor{factor}_novel_completion="
                    f"{row['novel_completion']}"
                ),
                (
                    f"factor{factor}_novel_completion_exclusive="
                    f"{row['novel_completion_exclusive']}"
                ),
                f"factor{factor}_remaining={row['remaining']}",
                (
                    f"factor{factor}_positive_states="
                    f"{row['positive_states']}"
                ),
                (
                    f"factor{factor}_nonempty_states="
                    f"{row['nonempty_states']}"
                ),
                (
                    f"factor{factor}_fully_excluded_states="
                    f"{row['fully_excluded_states']}"
                ),
                "",
            ]
        )
    lines.extend(
        [
            "factor2_novel_incremental_fraction=23392/158367",
            "factor4_novel_incremental_fraction=132915/1662232",
            "",
            (
                "conclusion: novel S7 cyclic-output labels create exact "
                "local collision/completion credit on most shell children,"
            ),
            (
                "but this certified subset excludes only 140352 of 950202 "
                "factor-two candidates and 398745 of 4986696"
            ),
            (
                "factor-four candidates after exact-state deduplication. "
                "It is genuine obstruction export, not a closing reserve."
            ),
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_s7_scc_local_completion_credit.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print(
        "certificate_sha256="
        + hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
