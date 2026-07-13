#!/usr/bin/env python3
"""Classify complete cheap replay candidates on small S7 cyclic-output children.

For each exact shell-resolved child of size at most MAX_STATE_SIZE, this verifier
forms every admissible factor-two and factor-four three-translate extension and
checks four-term-progression-freeness by exact membership. This is a complete
finite obstruction test for those states, equivalent to testing every layer
word rather than only the local collision/completion subset.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from export_simultaneous_deletion_transition import build_payload
from verify_three_translate_obstruction_classes import class_rows, normalize
from verify_s7_scc_local_completion_credit import (
    COMPONENT,
    canonical_set_hash,
    parity_ok,
    support_sets,
)

MAX_STATE_SIZE = 50
EXPECTED_OCCURRENCES = 63
EXPECTED_EXACT_STATES = 62
EXPECTED_SMALL_STATES = 33
EXPECTED_CATALOG_SHA256 = (
    "55a148e8eb49994881ee97b4df45bb9138dbd0a6b7577256968a01b4f139e6ca"
)
EXPECTED = {
    2: {
        "domain": 21_724,
        "local_invalid": 2_128,
        "additional_affine_invalid": 4_436,
        "exact_invalid": 6_564,
        "valid": 15_160,
        "overlap": 1_424,
        "four_ap": 5_140,
        "nonempty_states": 30,
        "fully_excluded_states": 1,
        "surviving_states": 29,
        "active_first_witness_classes": 33,
        "base_only_first_witnesses": 0,
    },
    4: {
        "domain": 87_829,
        "local_invalid": 4_538,
        "additional_affine_invalid": 7_568,
        "exact_invalid": 12_106,
        "valid": 75_723,
        "overlap": 2_548,
        "four_ap": 9_558,
        "nonempty_states": 33,
        "fully_excluded_states": 1,
        "surviving_states": 32,
        "active_first_witness_classes": 33,
        "base_only_first_witnesses": 0,
    },
}
EXPECTED_FIRST = {
    2: ((5,), 4, 1, (16, 21, 26), 16, 1),
    4: ((5,), 4, 1, (16, 21, 26), 16, 1),
}
EXPECTED_CLASS_HISTOGRAM_SHA256 = {
    2: "270349594a150e57a23388aa80da8dfb2581b0dafd462f911578b645e99438af",
    4: "5da0d0cbd4934eabd3ba0a492288c871a424990f59d9c16a86b22b2204ae4339",
}
CERTIFICATE_SHA256 = (
    "6a1073d6fd485c0a99526c59c32b5a0985220632e32e67fc8fed9d5b8c5234e0"
)

CLASS_ID = {}
for class_id, representative, reverse, *_ in class_rows():
    CLASS_ID[representative] = class_id
    CLASS_ID[reverse] = class_id


def first_four_ap(values: Iterable[int]) -> tuple[int, int] | None:
    """Return one nontrivial four-term AP using exact membership checks."""
    ordered = sorted(set(values))
    present = set(ordered)
    maximum = ordered[-1]
    for left_index, first in enumerate(ordered):
        for second in ordered[left_index + 1 :]:
            step = second - first
            if first + 3 * step > maximum:
                break
            if first + 2 * step in present and first + 3 * step in present:
                return first, step
    return None


def grouped_states() -> list[tuple[tuple[int, ...], int, tuple[int, ...]]]:
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
        scale = int(occurrence["shell_scale"])
        row = grouped.setdefault(values, {"scale": scale, "sources": []})
        if row["scale"] != scale:
            raise AssertionError("exact state appeared at two shell scales")
        row["sources"].append(source)

    if occurrence_count != EXPECTED_OCCURRENCES:
        raise AssertionError(f"occurrence count mismatch: {occurrence_count}")
    if len(grouped) != EXPECTED_EXACT_STATES:
        raise AssertionError(f"exact state count mismatch: {len(grouped)}")

    small: list[tuple[tuple[int, ...], int, tuple[int, ...]]] = []
    for values, row in grouped.items():
        if len(values) > MAX_STATE_SIZE:
            continue
        imported = set(values) & backbone
        if imported:
            raise AssertionError(
                "small-state frontier unexpectedly contains imported labels: "
                f"{values!r}"
            )
        small.append(
            (
                values,
                int(row["scale"]),
                tuple(sorted(int(source) for source in row["sources"])),
            )
        )

    small.sort(
        key=lambda item: (
            item[1],
            min(item[0]),
            max(item[0]),
            canonical_set_hash(item[0]),
        )
    )
    if len(small) != EXPECTED_SMALL_STATES:
        raise AssertionError(f"small-state count mismatch: {len(small)}")
    return small


def classify(values: tuple[int, ...], scale: int, factor: int) -> dict[str, object]:
    upper = (factor * scale - 1 - max(values)) // 2
    domain = {
        separation
        for separation in range(1, upper + 1)
        if parity_ok(separation)
    }
    anchor = {0, *values}

    local_overlap, local_completion, _ = support_sets(anchor, upper)
    local_invalid = domain & (local_overlap | local_completion)

    exact_invalid: set[int] = set()
    overlap: set[int] = set()
    four_ap: set[int] = set()
    first_witness_classes: dict[int, int] = {}
    valid: list[int] = []

    for separation in sorted(domain):
        generated_layers = {
            value + layer * separation: layer
            for value in anchor
            for layer in range(3)
        }
        generated = set(generated_layers)
        if len(generated) != 3 * len(anchor):
            overlap.add(separation)
            exact_invalid.add(separation)
            continue
        if max(generated) >= factor * scale:
            raise AssertionError("candidate fit bound failed")
        witness = first_four_ap(generated)
        if witness is not None:
            first, step = witness
            word = tuple(
                generated_layers[first + index * step]
                for index in range(4)
            )
            normalized = normalize(word)
            if normalized == (0, 0, 0, 0):
                class_id = 0
            else:
                class_id = CLASS_ID[normalized]
            first_witness_classes[class_id] = (
                first_witness_classes.get(class_id, 0) + 1
            )
            four_ap.add(separation)
            exact_invalid.add(separation)
        else:
            valid.append(separation)

    if not local_invalid <= exact_invalid:
        raise AssertionError("local support is not a subset of exact invalidity")
    if exact_invalid != overlap | four_ap:
        raise AssertionError("exact invalidity partition mismatch")

    return {
        "upper": upper,
        "domain": len(domain),
        "local_invalid": len(local_invalid),
        "additional_affine_invalid": len(exact_invalid - local_invalid),
        "exact_invalid": len(exact_invalid),
        "valid": len(valid),
        "first_valid": valid[0] if valid else None,
        "last_valid": valid[-1] if valid else None,
        "overlap": len(overlap),
        "four_ap": len(four_ap),
        "first_witness_class_counts": {
            str(class_id): first_witness_classes[class_id]
            for class_id in sorted(first_witness_classes)
        },
    }


def build_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for values, scale, sources in grouped_states():
        records.append(
            {
                "values": list(values),
                "state_sha256": canonical_set_hash(values),
                "sources": list(sources),
                "scale": scale,
                "size": len(values),
                "minimum": min(values),
                "maximum": max(values),
                "factors": {
                    str(factor): classify(values, scale, factor)
                    for factor in (2, 4)
                },
            }
        )
    return records


def aggregate(records: list[dict[str, object]], factor: int) -> dict[str, int]:
    rows = [record["factors"][str(factor)] for record in records]
    fields = (
        "domain",
        "local_invalid",
        "additional_affine_invalid",
        "exact_invalid",
        "valid",
        "overlap",
        "four_ap",
    )
    result = {
        field: sum(int(row[field]) for row in rows)
        for field in fields
    }
    result["nonempty_states"] = sum(int(row["domain"]) > 0 for row in rows)
    result["fully_excluded_states"] = sum(
        int(row["domain"]) > 0 and int(row["valid"]) == 0
        for row in rows
    )
    result["surviving_states"] = sum(int(row["valid"]) > 0 for row in rows)
    class_counts: dict[int, int] = {}
    for row in rows:
        for class_id, count in row["first_witness_class_counts"].items():
            key = int(class_id)
            class_counts[key] = class_counts.get(key, 0) + int(count)
    result["active_first_witness_classes"] = len(class_counts)
    result["base_only_first_witnesses"] = class_counts.get(0, 0)
    return result


def class_histogram(
    records: list[dict[str, object]],
    factor: int,
) -> dict[int, int]:
    counts: dict[int, int] = {}
    for record in records:
        row = record["factors"][str(factor)]
        for class_id, count in row["first_witness_class_counts"].items():
            key = int(class_id)
            counts[key] = counts.get(key, 0) + int(count)
    return counts


def class_histogram_hash(counts: dict[int, int]) -> str:
    payload = "".join(
        f"{class_id},{counts[class_id]}\n"
        for class_id in sorted(counts)
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def first_survivors(
    records: list[dict[str, object]],
    factor: int,
) -> tuple[tuple[int, ...], int, int, tuple[int, ...], int, int]:
    first: tuple[tuple[int, ...], int, int] | None = None
    first_nontrivial: tuple[tuple[int, ...], int, int] | None = None

    for record in records:
        row = record["factors"][str(factor)]
        if int(row["valid"]) == 0:
            continue
        candidate = (
            tuple(int(value) for value in record["values"]),
            int(record["scale"]),
            int(row["first_valid"]),
        )
        if first is None:
            first = candidate
        if int(record["size"]) >= 3 and first_nontrivial is None:
            first_nontrivial = candidate

    if first is None or first_nontrivial is None:
        raise AssertionError("expected surviving states")
    result = (*first, *first_nontrivial)
    if result != EXPECTED_FIRST[factor]:
        raise AssertionError(
            f"first survivor mismatch for factor {factor}: {result!r}"
        )
    return result


def build_certificate() -> str:
    records = build_records()
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

    histograms = {
        factor: class_histogram(records, factor)
        for factor in (2, 4)
    }
    for factor, counts in histograms.items():
        missing = sorted(set(range(1, 35)) - set(counts))
        if missing != [22] or 0 in counts:
            raise AssertionError(
                f"unexpected first-witness class support for factor {factor}: "
                f"missing={missing}, base={counts.get(0, 0)}"
            )
        digest = class_histogram_hash(counts)
        if digest != EXPECTED_CLASS_HISTOGRAM_SHA256[factor]:
            raise AssertionError(
                f"class histogram hash mismatch for factor {factor}: {digest}"
            )

    lines = [
        "S7 CYCLIC SCC SMALL-STATE COMPLETE AFFINE FRONTIER",
        "",
        f"maximum_state_size={MAX_STATE_SIZE}",
        f"exact_states={len(records)}",
        f"state_catalog_sha256={catalog_hash}",
        "",
        (
            "classification: exact three-translate generation and complete "
            "four-AP membership test"
        ),
        "local_baseline: layer collision plus same-layer completion",
        "all_selected_states_have_imported_labels=0",
        "",
    ]

    for factor in (2, 4):
        row = observed[factor]
        lines.extend(
            [
                f"factor{factor}_domain={row['domain']}",
                f"factor{factor}_local_invalid={row['local_invalid']}",
                (
                    f"factor{factor}_additional_affine_invalid="
                    f"{row['additional_affine_invalid']}"
                ),
                f"factor{factor}_exact_invalid={row['exact_invalid']}",
                f"factor{factor}_valid={row['valid']}",
                f"factor{factor}_overlap={row['overlap']}",
                f"factor{factor}_four_ap={row['four_ap']}",
                f"factor{factor}_nonempty_states={row['nonempty_states']}",
                (
                    f"factor{factor}_fully_excluded_states="
                    f"{row['fully_excluded_states']}"
                ),
                f"factor{factor}_surviving_states={row['surviving_states']}",
                (
                    f"factor{factor}_active_first_witness_classes="
                    f"{row['active_first_witness_classes']}"
                ),
                (
                    f"factor{factor}_base_only_first_witnesses="
                    f"{row['base_only_first_witnesses']}"
                ),
                f"factor{factor}_missing_first_witness_class=22",
                (
                    f"factor{factor}_first_witness_class_histogram_sha256="
                    f"{EXPECTED_CLASS_HISTOGRAM_SHA256[factor]}"
                ),
                "",
            ]
        )
        (
            first_values,
            first_scale,
            first_r,
            nontrivial_values,
            nontrivial_scale,
            nontrivial_r,
        ) = first_survivors(records, factor)
        lines.extend(
            [
                f"factor{factor}_first_survivor_scale={first_scale}",
                (
                    f"factor{factor}_first_survivor_state="
                    + ",".join(map(str, first_values))
                ),
                f"factor{factor}_first_survivor_R={first_r}",
                (
                    f"factor{factor}_first_size_ge_3_survivor_scale="
                    f"{nontrivial_scale}"
                ),
                (
                    f"factor{factor}_first_size_ge_3_survivor_state="
                    + ",".join(map(str, nontrivial_values))
                ),
                f"factor{factor}_first_size_ge_3_survivor_R={nontrivial_r}",
                "",
            ]
        )

    lines.extend(
        [
            "factor2_exact_invalid_fraction=1641/5431",
            "factor2_valid_fraction=3790/5431",
            "factor4_exact_invalid_fraction=12106/87829",
            "factor4_valid_fraction=75723/87829",
            "",
            (
                "conclusion: complete affine testing strengthens local "
                "completion coverage but leaves most candidates valid"
            ),
            (
                "on the exact size-at-most-50 child frontier. The smallest "
                "surviving state is {5} at scale 4 with R=1;"
            ),
            (
                "the first surviving state of size at least three is "
                "{16,21,26} at scale 16 with R=1."
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
            "usage: verify_s7_scc_small_state_affine_frontier.py [OUTPUT]"
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
