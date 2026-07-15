#!/usr/bin/env python3
"""Summarize exact S7 saturation and completion first-use ledgers."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (2 * value.denominator)
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def serialize_mass(value: Fraction) -> dict[str, str]:
    text = fraction_text(value)
    return {
        "fraction": text,
        "decimal": decimal_text(value),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_s7() -> set[int]:
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    scales = (64, 256, 2048, 8192, 32768, 262144, 1048576)
    separations = (61, 303, 1597, 8195, 93476, 230164)
    state = {scales[0] + value for value in base}
    for index, separation in enumerate(separations):
        anchor = {0} | state
        raw = {
            value + layer * separation
            for value in anchor
            for layer in range(3)
        }
        state = {scales[index + 1] + value for value in raw}
    if (len(state), min(state), max(state)) != (9840, 1048576, 2021668):
        raise AssertionError("certified S7 reconstruction mismatch")
    return state


def read_classification(path: Path) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            if completion in result:
                raise AssertionError("duplicate completion classification")
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing_index": int(row["missing_index"]),
            }
    return result


def aspect_band(witness_step: int, target_gap: int) -> str:
    if witness_step <= target_gap:
        return "h_le_D"
    if witness_step <= 2 * target_gap:
        return "D_lt_h_le_2D"
    if witness_step <= 4 * target_gap:
        return "2D_lt_h_le_4D"
    if witness_step <= 8 * target_gap:
        return "4D_lt_h_le_8D"
    return "h_gt_8D"


def serialize_aspect_profile(
    profile: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    order = (
        "h_le_D",
        "D_lt_h_le_2D",
        "2D_lt_h_le_4D",
        "4D_lt_h_le_8D",
        "h_gt_8D",
    )
    rows = []
    for band in order:
        row = profile.get(band, {"count": 0, "mass": Fraction()})
        rows.append(
            {
                "band": band,
                "count": int(row["count"]),
                "target_mass": serialize_mass(row["mass"]),
            }
        )
    return rows


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: summarize_s7_terminal_completion_saturation.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    classifications = read_classification(classification_path)
    s7 = build_s7()

    status_counts = Counter()
    witness_steps: dict[int, int] = {}
    for completion, record in classifications.items():
        status = str(record["status"])
        status_counts[status] += 1
        witness = record["witness"]
        missing_index = int(record["missing_index"])
        if status == "certified_S7_hole":
            if witness[missing_index] != completion:
                raise AssertionError("witness missing coordinate mismatch")
            step = witness[1] - witness[0]
            if step <= 0 or any(
                witness[index + 1] - witness[index] != step for index in range(3)
            ):
                raise AssertionError("classification witness is not a four-AP")
            if any(
                value not in s7
                for index, value in enumerate(witness)
                if index != missing_index
            ):
                raise AssertionError("classification witness leaves S7")
            if completion in s7:
                raise AssertionError("certified hole already belongs to S7")
            witness_steps[completion] = step
        elif status == "S7_admissible_extension":
            if missing_index != -1 or witness != (0, 0, 0, 0):
                raise AssertionError("admissible extension carries a fake witness")
        else:
            raise AssertionError(f"unknown classification status: {status}")

    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    target_aggregate: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "targets": 0,
            "source_occurrences": 0,
            "target_union": Fraction(),
            "source_collision": Fraction(),
            "terminal_collision": Fraction(),
            "amplification": Fraction(),
        }
    )
    target_class_profile: dict[str, Counter[str]] = defaultdict(Counter)
    completion_targets: dict[tuple[str, int], list[dict[str, object]]] = defaultdict(list)
    assignment_rows: list[tuple[object, ...]] = []

    unresolved_targets = 0
    unresolved_target_union = Fraction()
    unresolved_source_collision = Fraction()
    unresolved_terminal_collision = Fraction()
    unresolved_amplification = Fraction()

    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        unresolved_targets += 1
        unresolved_target_union += Fraction(row["target_weight"])
        unresolved_source_collision += Fraction(row["source_collision_weight"])
        unresolved_terminal_collision += Fraction(row["terminal_collision_weight"])
        unresolved_amplification += Fraction(row["transport_amplification_slack"])
        completions = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completions) != 1:
            raise AssertionError("one unresolved target has multiple completion requests")
        completion = next(iter(completions))
        classification = classifications.get(completion)
        if classification is None:
            raise AssertionError("unclassified completion request")
        status = str(classification["status"])
        aggregate = target_aggregate[status]
        aggregate["targets"] += 1
        aggregate["source_occurrences"] += int(row["source_count"])
        aggregate["target_union"] += Fraction(row["target_weight"])
        aggregate["source_collision"] += Fraction(row["source_collision_weight"])
        aggregate["terminal_collision"] += Fraction(row["terminal_collision_weight"])
        aggregate["amplification"] += Fraction(row["transport_amplification_slack"])
        terminal_class = ",".join(row["terminal_classes"])
        target_class_profile[status][terminal_class] += 1
        completion_targets[(status, completion)].append(row)
        assignment_rows.append(
            (
                row["target"],
                completion,
                status,
                row["source_count"],
                row["target_weight"],
                row["source_collision_weight"],
            )
        )

    source_aggregate: dict[str, dict[str, object]] = defaultdict(
        lambda: {"sources": 0, "initial": Fraction(), "target_occurrence": Fraction()}
    )
    unresolved_sources = 0
    unresolved_initial = Fraction()
    unresolved_target_occurrence = Fraction()
    for row in source_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        unresolved_sources += 1
        unresolved_initial += Fraction(row["initial_weight"])
        unresolved_target_occurrence += Fraction(row["target_weight"])
        completion = int(row["natural_completion"])
        classification = classifications.get(completion)
        if classification is None:
            raise AssertionError("source row uses an unclassified completion")
        status = str(classification["status"])
        aggregate = source_aggregate[status]
        aggregate["sources"] += 1
        aggregate["initial"] += Fraction(row["initial_weight"])
        aggregate["target_occurrence"] += Fraction(row["target_weight"])

    if sum(int(row["targets"]) for row in target_aggregate.values()) != unresolved_targets:
        raise AssertionError("target classification count partition failed")
    if sum((row["target_union"] for row in target_aggregate.values()), Fraction()) != unresolved_target_union:
        raise AssertionError("target union mass partition failed")
    if sum((row["source_collision"] for row in target_aggregate.values()), Fraction()) != unresolved_source_collision:
        raise AssertionError("source collision partition failed")
    if sum((row["terminal_collision"] for row in target_aggregate.values()), Fraction()) != unresolved_terminal_collision:
        raise AssertionError("terminal collision partition failed")
    if sum((row["amplification"] for row in target_aggregate.values()), Fraction()) != unresolved_amplification:
        raise AssertionError("amplification partition failed")
    if sum(int(row["sources"]) for row in source_aggregate.values()) != unresolved_sources:
        raise AssertionError("source count partition failed")
    if sum((row["initial"] for row in source_aggregate.values()), Fraction()) != unresolved_initial:
        raise AssertionError("source initial mass partition failed")
    if sum((row["target_occurrence"] for row in source_aggregate.values()), Fraction()) != unresolved_target_occurrence:
        raise AssertionError("source target occurrence partition failed")

    completion_profile: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "first": Fraction(),
            "reuse": Fraction(),
            "singletons": 0,
            "reused": 0,
            "maximum": 0,
        }
    )
    first_aspect: dict[str, dict[str, object]] = defaultdict(
        lambda: {"count": 0, "mass": Fraction()}
    )
    all_aspect: dict[str, dict[str, object]] = defaultdict(
        lambda: {"count": 0, "mass": Fraction()}
    )
    completion_rows: list[tuple[object, ...]] = []

    for (status, completion), members in sorted(completion_targets.items()):
        ordered = sorted(
            members,
            key=lambda row: (
                -Fraction(row["target_weight"]),
                tuple(int(value) for value in row["target"]),
            ),
        )
        first = ordered[0]
        first_weight = Fraction(first["target_weight"])
        total_weight = sum((Fraction(row["target_weight"]) for row in ordered), Fraction())
        profile = completion_profile[status]
        profile["first"] += first_weight
        profile["reuse"] += total_weight - first_weight
        profile["singletons"] += len(ordered) == 1
        profile["reused"] += len(ordered) > 1
        profile["maximum"] = max(int(profile["maximum"]), len(ordered))

        first_band = None
        if status == "certified_S7_hole":
            witness_step = witness_steps[completion]
            first_target = tuple(int(value) for value in first["target"])
            first_gap = first_target[1] - first_target[0]
            first_band = aspect_band(witness_step, first_gap)
            first_aspect[first_band]["count"] += 1
            first_aspect[first_band]["mass"] += first_weight
            for row in ordered:
                target = tuple(int(value) for value in row["target"])
                gap = target[1] - target[0]
                band = aspect_band(witness_step, gap)
                all_aspect[band]["count"] += 1
                all_aspect[band]["mass"] += Fraction(row["target_weight"])

        completion_rows.append(
            (
                status,
                completion,
                len(ordered),
                fraction_text(total_weight),
                tuple(first["target"]),
                fraction_text(first_weight),
                first_band,
            )
        )

    target_profile = []
    for status, row in target_aggregate.items():
        completion_row = completion_profile[status]
        if completion_row["first"] + completion_row["reuse"] != row["target_union"]:
            raise AssertionError("completion first-use/reuse partition failed")
        target_profile.append(
            {
                "status": status,
                "targets": row["targets"],
                "source_occurrences": row["source_occurrences"],
                "distinct_completion_integers": status_counts[status],
                "singleton_completion_integers": completion_row["singletons"],
                "completion_integers_reused_by_targets": completion_row["reused"],
                "maximum_targets_per_completion_integer": completion_row["maximum"],
                "target_union_mass": serialize_mass(row["target_union"]),
                "completion_first_target_mass": serialize_mass(completion_row["first"]),
                "completion_target_reuse_mass": serialize_mass(completion_row["reuse"]),
                "source_collision_mass": serialize_mass(row["source_collision"]),
                "terminal_collision_mass": serialize_mass(row["terminal_collision"]),
                "transport_amplification_slack": serialize_mass(row["amplification"]),
                "terminal_class_counts": dict(sorted(target_class_profile[status].items())),
            }
        )
    target_profile.sort(key=lambda row: -Fraction(row["target_union_mass"]["fraction"]))

    source_profile = []
    for status, row in source_aggregate.items():
        source_profile.append(
            {
                "status": status,
                "sources": row["sources"],
                "initial_mass": serialize_mass(row["initial"]),
                "target_occurrence_mass": serialize_mass(row["target_occurrence"]),
            }
        )
    source_profile.sort(key=lambda row: -Fraction(row["initial_mass"]["fraction"]))

    hole_first_mass = completion_profile["certified_S7_hole"]["first"]
    hole_union_mass = target_aggregate["certified_S7_hole"]["target_union"]
    if sum((row["mass"] for row in first_aspect.values()), Fraction()) != hole_first_mass:
        raise AssertionError("first-target aspect mass partition failed")
    if sum(int(row["count"]) for row in first_aspect.values()) != status_counts["certified_S7_hole"]:
        raise AssertionError("first-target aspect count partition failed")
    if sum((row["mass"] for row in all_aspect.values()), Fraction()) != hole_union_mass:
        raise AssertionError("all-target aspect mass partition failed")
    if sum(int(row["count"]) for row in all_aspect.values()) != target_aggregate["certified_S7_hole"]["targets"]:
        raise AssertionError("all-target aspect count partition failed")

    classification_bytes = classification_path.read_bytes()
    output = {
        "schema": "s7_terminal_completion_saturation_summary_v2",
        "scope": "ambient_unresolved terminal completions on certified residual-sponsor R4_to_F5 frontier",
        "generation_six_propagated": False,
        "s7": {
            "points": len(s7),
            "minimum": min(s7),
            "maximum": max(s7),
        },
        "completion_counts": dict(sorted(status_counts.items())),
        "unresolved_parent_totals": {
            "targets": unresolved_targets,
            "sources": unresolved_sources,
            "target_union_mass": serialize_mass(unresolved_target_union),
            "source_initial_mass": serialize_mass(unresolved_initial),
            "source_target_occurrence_mass": serialize_mass(unresolved_target_occurrence),
            "source_collision_mass": serialize_mass(unresolved_source_collision),
            "terminal_collision_mass": serialize_mass(unresolved_terminal_collision),
            "transport_amplification_slack": serialize_mass(unresolved_amplification),
        },
        "target_profile": target_profile,
        "source_profile": source_profile,
        "certified_hole_witness_aspect": {
            "identity": "target_weight=(witness_step/target_gap)*witness_step_weight",
            "first_target_profile": serialize_aspect_profile(first_aspect),
            "all_target_profile": serialize_aspect_profile(all_aspect),
        },
        "hashes": {
            "classification_tsv_sha256": hashlib.sha256(classification_bytes).hexdigest(),
            "target_assignments_sha256": canonical_hash(sorted(assignment_rows)),
            "completion_first_use_rows_sha256": canonical_hash(completion_rows),
        },
        "checks": {
            "every_completion_classified": len(classifications) == sum(status_counts.values()),
            "target_count_partition": sum(int(row["targets"]) for row in target_profile) == unresolved_targets,
            "target_union_partition": sum((Fraction(row["target_union_mass"]["fraction"]) for row in target_profile), Fraction()) == unresolved_target_union,
            "completion_first_use_reuse_partition": all(
                Fraction(row["completion_first_target_mass"]["fraction"])
                + Fraction(row["completion_target_reuse_mass"]["fraction"])
                == Fraction(row["target_union_mass"]["fraction"])
                for row in target_profile
            ),
            "source_count_partition": sum(int(row["sources"]) for row in source_profile) == unresolved_sources,
            "source_initial_partition": sum((Fraction(row["initial_mass"]["fraction"]) for row in source_profile), Fraction()) == unresolved_initial,
            "first_target_aspect_partition": sum((Fraction(row["target_mass"]["fraction"]) for row in serialize_aspect_profile(first_aspect)), Fraction()) == hole_first_mass,
            "all_target_aspect_partition": sum((Fraction(row["target_mass"]["fraction"]) for row in serialize_aspect_profile(all_aspect)), Fraction()) == hole_union_mass,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["summary_payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
