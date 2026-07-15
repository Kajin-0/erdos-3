#!/usr/bin/env python3
"""Summarize exact S7 saturation status of terminal completion requests."""
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
    completion_target_multiplicity: Counter[tuple[str, int]] = Counter()
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
        completion_target_multiplicity[(status, completion)] += 1
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

    target_profile = []
    for status, row in target_aggregate.items():
        multiplicities = [
            count
            for (candidate_status, _completion), count in completion_target_multiplicity.items()
            if candidate_status == status
        ]
        target_profile.append(
            {
                "status": status,
                "targets": row["targets"],
                "source_occurrences": row["source_occurrences"],
                "distinct_completion_integers": status_counts[status],
                "completion_integers_reused_by_targets": sum(value > 1 for value in multiplicities),
                "maximum_targets_per_completion_integer": max(multiplicities, default=0),
                "target_union_mass": serialize_mass(row["target_union"]),
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

    classification_bytes = classification_path.read_bytes()
    output = {
        "schema": "s7_terminal_completion_saturation_summary_v1",
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
        "hashes": {
            "classification_tsv_sha256": hashlib.sha256(classification_bytes).hexdigest(),
            "target_assignments_sha256": canonical_hash(sorted(assignment_rows)),
        },
        "checks": {
            "every_completion_classified": len(classifications) == sum(status_counts.values()),
            "target_count_partition": sum(int(row["targets"]) for row in target_profile) == unresolved_targets,
            "target_union_partition": sum((Fraction(row["target_union_mass"]["fraction"]) for row in target_profile), Fraction()) == unresolved_target_union,
            "source_count_partition": sum(int(row["sources"]) for row in source_profile) == unresolved_sources,
            "source_initial_partition": sum((Fraction(row["initial_mass"]["fraction"]) for row in source_profile), Fraction()) == unresolved_initial,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["summary_payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
