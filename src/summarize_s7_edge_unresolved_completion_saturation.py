#!/usr/bin/env python3
"""Summarize S7-edge-unresolved terminal completion saturation exactly."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, digits = divmod(rounded, scale)
    return f"{sign}{whole}.{digits:0{places}d}"


def serialize_mass(value: Fraction) -> dict[str, str]:
    value_text = fraction_text(value)
    return {
        "fraction": value_text,
        "decimal": decimal_text(value),
        "sha256": hashlib.sha256(value_text.encode("utf-8")).hexdigest(),
    }


def canonical_hash(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def build_s7() -> set[int]:
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    scales = (64, 256, 2048, 8192, 32768, 262144, 1048576)
    separations = (61, 303, 1597, 8195, 93476, 230164)
    state = {scales[0] + value for value in base}
    for index, separation in enumerate(separations):
        state = {
            scales[index + 1] + value + layer * separation
            for value in ({0} | state)
            for layer in range(3)
        }
    if (len(state), min(state), max(state)) != (9840, 1048576, 2021668):
        raise AssertionError("certified S7 reconstruction mismatch")
    return state


def completion_roots(pair: tuple[int, int], roots: set[int]) -> set[int]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return candidates & roots


def read_classification(path: Path) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            if completion in result:
                raise AssertionError("duplicate saturation classification")
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing": int(row["missing_index"]),
            }
    return result


def support_pair(
    witness: tuple[int, ...], missing: int
) -> tuple[int, int]:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def aspect_band(step: int, gap: int) -> str:
    if step <= gap:
        return "h_le_D"
    if step <= 2 * gap:
        return "D_lt_h_le_2D"
    if step <= 4 * gap:
        return "2D_lt_h_le_4D"
    if step <= 8 * gap:
        return "4D_lt_h_le_8D"
    return "h_gt_8D"


def serialize_aspect_profile(
    profile: dict[str, list[object]],
) -> list[dict[str, object]]:
    order = (
        "h_le_D",
        "D_lt_h_le_2D",
        "2D_lt_h_le_4D",
        "4D_lt_h_le_8D",
        "h_gt_8D",
    )
    return [
        {
            "band": band,
            "count": int(profile.get(band, [0, Fraction()])[0]),
            "target_mass": serialize_mass(
                profile.get(band, [0, Fraction()])[1]
            ),
        }
        for band in order
    ]


def pair_profile(
    pair_holes: dict[tuple[int, int], list[Fraction]],
) -> dict[str, object]:
    union = sum(
        (Fraction(1, right - left) for left, right in pair_holes),
        Fraction(),
    )
    occurrence = sum(
        (
            Fraction(len(weights), right - left)
            for (left, right), weights in pair_holes.items()
        ),
        Fraction(),
    )
    targets = sum(
        (weight for weights in pair_holes.values() for weight in weights),
        Fraction(),
    )
    first = sum((max(weights) for weights in pair_holes.values()), Fraction())
    return {
        "distinct_pairs": len(pair_holes),
        "reused_pairs": sum(len(weights) > 1 for weights in pair_holes.values()),
        "maximum_multiplicity": max(
            (len(weights) for weights in pair_holes.values()), default=0
        ),
        "pair_union_mass": serialize_mass(union),
        "pair_occurrence_mass": serialize_mass(occurrence),
        "pair_reuse_mass": serialize_mass(occurrence - union),
        "target_mass": serialize_mass(targets),
        "support_pair_first_target_mass": serialize_mass(first),
        "support_pair_target_reuse_mass": serialize_mass(targets - first),
    }


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: summarize_s7_edge_unresolved_completion_saturation.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path, classification_path, output_path = map(Path, sys.argv[1:])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    classifications = read_classification(classification_path)
    s7 = build_s7()
    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    edge_supported_targets = 0
    edge_supported_mass = Fraction()
    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        pair = tuple(int(value) for value in row["target"])
        if completion_roots(pair, s7):
            edge_supported_targets += 1
            edge_supported_mass += Fraction(row["target_weight"])
            continue
        completion_values = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completion_values) != 1:
            raise AssertionError(
                "one edge-unresolved target requests multiple completions"
            )
        completion = next(iter(completion_values))
        if completion not in classifications:
            raise AssertionError(
                "edge-unresolved completion lacks saturation classification"
            )
        targets_by_completion[completion].append(row)

    if set(targets_by_completion) != set(classifications):
        raise AssertionError("classification contains unused completion integers")

    source_totals: dict[str, list[object]] = defaultdict(
        lambda: [0, Fraction(), Fraction()]
    )
    for row in source_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        pair = tuple(int(value) for value in row["target"])
        if completion_roots(pair, s7):
            continue
        completion = int(row["natural_completion"])
        status = str(classifications[completion]["status"])
        source_totals[status][0] += 1
        source_totals[status][1] += Fraction(row["initial_weight"])
        source_totals[status][2] += Fraction(row["target_weight"])

    status_rows: dict[str, list[dict[str, object]]] = defaultdict(list)
    first_aspect: dict[str, list[object]] = defaultdict(
        lambda: [0, Fraction()]
    )
    all_aspect: dict[str, list[object]] = defaultdict(
        lambda: [0, Fraction()]
    )
    support_pairs: dict[tuple[int, int], list[Fraction]] = defaultdict(list)
    near_support_pairs: dict[tuple[int, int], list[Fraction]] = defaultdict(list)
    assignment_rows = []

    for completion, members in sorted(targets_by_completion.items()):
        record = classifications[completion]
        status = str(record["status"])
        ordered = sorted(
            members,
            key=lambda row: (
                -Fraction(row["target_weight"]),
                tuple(row["target"]),
            ),
        )
        first = ordered[0]
        status_rows[status].extend(ordered)
        assignment_rows.append(
            (
                completion,
                status,
                tuple(first["target"]),
                first["target_weight"],
                len(ordered),
            )
        )
        if status != "certified_S7_hole":
            continue

        witness = tuple(int(value) for value in record["witness"])
        missing = int(record["missing"])
        step = witness[1] - witness[0]
        pair = support_pair(witness, missing)
        gap = int(first["target"][1]) - int(first["target"][0])
        first_weight = Fraction(first["target_weight"])
        band = aspect_band(step, gap)
        first_aspect[band][0] += 1
        first_aspect[band][1] += first_weight
        support_pairs[pair].append(first_weight)
        if step <= gap:
            near_support_pairs[pair].append(first_weight)

        for row in ordered:
            target_gap = int(row["target"][1]) - int(row["target"][0])
            target_band = aspect_band(step, target_gap)
            all_aspect[target_band][0] += 1
            all_aspect[target_band][1] += Fraction(row["target_weight"])

    target_profile = []
    for status, rows in status_rows.items():
        by_completion = {
            completion: members
            for completion, members in targets_by_completion.items()
            if classifications[completion]["status"] == status
        }
        target_union = sum(
            (Fraction(row["target_weight"]) for row in rows), Fraction()
        )
        first_mass = sum(
            (
                max(Fraction(row["target_weight"]) for row in members)
                for members in by_completion.values()
            ),
            Fraction(),
        )
        source_collision = sum(
            (Fraction(row["source_collision_weight"]) for row in rows),
            Fraction(),
        )
        terminal_collision = sum(
            (Fraction(row["terminal_collision_weight"]) for row in rows),
            Fraction(),
        )
        amplification = sum(
            (Fraction(row["transport_amplification_slack"]) for row in rows),
            Fraction(),
        )
        target_profile.append(
            {
                "status": status,
                "distinct_completion_integers": len(by_completion),
                "targets": len(rows),
                "source_occurrences": sum(
                    int(row["source_count"]) for row in rows
                ),
                "singleton_completion_integers": sum(
                    len(members) == 1 for members in by_completion.values()
                ),
                "reused_completion_integers": sum(
                    len(members) > 1 for members in by_completion.values()
                ),
                "maximum_targets_per_completion": max(
                    map(len, by_completion.values()), default=0
                ),
                "target_union_mass": serialize_mass(target_union),
                "completion_first_target_mass": serialize_mass(first_mass),
                "completion_target_reuse_mass": serialize_mass(
                    target_union - first_mass
                ),
                "source_collision_mass": serialize_mass(source_collision),
                "terminal_collision_mass": serialize_mass(terminal_collision),
                "transport_amplification_slack": serialize_mass(amplification),
                "terminal_class_counts": dict(
                    sorted(
                        Counter(
                            ",".join(row["terminal_classes"])
                            for row in rows
                        ).items()
                    )
                ),
            }
        )
    target_profile.sort(
        key=lambda row: -Fraction(row["target_union_mass"]["fraction"])
    )

    source_profile = [
        {
            "status": status,
            "sources": int(values[0]),
            "initial_mass": serialize_mass(values[1]),
            "target_occurrence_mass": serialize_mass(values[2]),
        }
        for status, values in source_totals.items()
    ]
    source_profile.sort(
        key=lambda row: -Fraction(row["initial_mass"]["fraction"])
    )

    total_target_union = sum(
        (
            Fraction(row["target_union_mass"]["fraction"])
            for row in target_profile
        ),
        Fraction(),
    )
    total_initial = sum(
        (Fraction(row["initial_mass"]["fraction"]) for row in source_profile),
        Fraction(),
    )
    total_target_occurrence = sum(
        (
            Fraction(row["target_occurrence_mass"]["fraction"])
            for row in source_profile
        ),
        Fraction(),
    )
    total_source_collision = sum(
        (
            Fraction(row["source_collision_mass"]["fraction"])
            for row in target_profile
        ),
        Fraction(),
    )
    total_terminal_collision = sum(
        (
            Fraction(row["terminal_collision_mass"]["fraction"])
            for row in target_profile
        ),
        Fraction(),
    )

    all_support = pair_profile(support_pairs)
    near_support = pair_profile(near_support_pairs)
    if (
        int(all_support["maximum_multiplicity"]) > 2
        or int(near_support["maximum_multiplicity"]) > 2
    ):
        raise AssertionError("canonical support-pair multiplicity exceeds two")

    output = {
        "schema": "s7_edge_unresolved_completion_saturation_summary_v1",
        "scope": "terminal targets with no supporting S7 three-AP edge",
        "generation_six_propagated": False,
        "S7_edge_supported_natural_unresolved": {
            "targets": edge_supported_targets,
            "target_union_mass": serialize_mass(edge_supported_mass),
        },
        "completion_counts": dict(
            sorted(
                Counter(
                    str(record["status"])
                    for record in classifications.values()
                ).items()
            )
        ),
        "edge_unresolved_totals": {
            "targets": sum(int(row["targets"]) for row in target_profile),
            "sources": sum(int(row["sources"]) for row in source_profile),
            "target_union_mass": serialize_mass(total_target_union),
            "source_initial_mass": serialize_mass(total_initial),
            "source_target_occurrence_mass": serialize_mass(
                total_target_occurrence
            ),
            "source_collision_mass": serialize_mass(total_source_collision),
            "terminal_collision_mass": serialize_mass(
                total_terminal_collision
            ),
            "transport_amplification_slack": serialize_mass(
                total_terminal_collision - total_source_collision
            ),
        },
        "target_profile": target_profile,
        "source_profile": source_profile,
        "certified_hole_witness_aspect": {
            "identity": (
                "target_weight=(witness_step/target_gap)*witness_step_weight"
            ),
            "first_target_profile": serialize_aspect_profile(first_aspect),
            "all_target_profile": serialize_aspect_profile(all_aspect),
        },
        "canonical_hole_support_pairs": {
            "all": all_support,
            "near_h_le_D": near_support,
        },
        "hashes": {
            "classification_tsv_sha256": hashlib.sha256(
                classification_path.read_bytes()
            ).hexdigest(),
            "assignment_rows_sha256": canonical_hash(assignment_rows),
        },
        "checks": {
            "all_classifications_used": (
                set(targets_by_completion) == set(classifications)
            ),
            "target_mass_partition": (
                total_target_union + edge_supported_mass
                == Fraction(
                    payment["masses"]["ambient_unresolved_target_union"][
                        "fraction"
                    ]
                )
            ),
            "source_collision_refines_terminal_collision": (
                total_source_collision <= total_terminal_collision
            ),
            "support_pair_multiplicity_at_most_two": (
                int(all_support["maximum_multiplicity"]) <= 2
            ),
            "near_support_pair_multiplicity_at_most_two": (
                int(near_support["maximum_multiplicity"]) <= 2
            ),
        },
    }
    raw = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["summary_payload_sha256"] = hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()
    output_path.write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
