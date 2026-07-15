#!/usr/bin/env python3
"""Summarize canonical support-pair reuse for certified S7 completion holes."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, places: int = 12) -> str:
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (2 * value.denominator)
    whole, fractional = divmod(rounded, scale)
    return f"{whole}.{fractional:0{places}d}"


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


def canonical_pair(
    witness: tuple[int, int, int, int], missing: int
) -> tuple[int, int]:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def read_holes(
    path: Path,
) -> dict[int, tuple[tuple[int, int, int, int], int]]:
    holes = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["status"] != "certified_S7_hole":
                continue
            completion = int(row["completion"])
            witness = tuple(int(row[f"p{index}"]) for index in range(4))
            missing = int(row["missing_index"])
            holes[completion] = (witness, missing)
    return holes


def profile_rows(
    pair_holes: dict[tuple[int, int], list[tuple[int, Fraction]]],
) -> dict[str, object]:
    union_mass = sum(
        (Fraction(1, pair[1] - pair[0]) for pair in pair_holes), Fraction()
    )
    occurrence_mass = sum(
        (
            Fraction(len(holes), pair[1] - pair[0])
            for pair, holes in pair_holes.items()
        ),
        Fraction(),
    )
    target_mass = sum(
        (weight for holes in pair_holes.values() for _completion, weight in holes),
        Fraction(),
    )
    first_target_mass = sum(
        (
            max(weight for _completion, weight in holes)
            for holes in pair_holes.values()
        ),
        Fraction(),
    )
    maximum = max((len(holes) for holes in pair_holes.values()), default=0)
    return {
        "distinct_pairs": len(pair_holes),
        "reused_pairs": sum(len(holes) > 1 for holes in pair_holes.values()),
        "maximum_multiplicity": maximum,
        "pair_union_mass": serialize_mass(union_mass),
        "pair_occurrence_mass": serialize_mass(occurrence_mass),
        "pair_reuse_mass": serialize_mass(occurrence_mass - union_mass),
        "target_mass": serialize_mass(target_mass),
        "support_pair_first_target_mass": serialize_mass(first_target_mass),
        "support_pair_target_reuse_mass": serialize_mass(
            target_mass - first_target_mass
        ),
    }


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: summarize_canonical_hole_support_pairs.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    holes = read_holes(classification_path)
    target_rows = payment.get("target_rows")
    if not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks target_rows")

    targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        completions = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completions) != 1:
            raise AssertionError("one target requests multiple unresolved completions")
        completion = next(iter(completions))
        if completion in holes:
            targets_by_completion[completion].append(row)

    if set(targets_by_completion) != set(holes):
        raise AssertionError("certified-hole target family is incomplete")

    pair_holes: dict[tuple[int, int], list[tuple[int, Fraction]]] = defaultdict(list)
    near_pair_holes: dict[tuple[int, int], list[tuple[int, Fraction]]] = defaultdict(list)
    rows = []
    for completion, members in sorted(targets_by_completion.items()):
        witness, missing = holes[completion]
        step = witness[1] - witness[0]
        pair = canonical_pair(witness, missing)
        first = min(
            members,
            key=lambda row: (
                -Fraction(row["target_weight"]),
                tuple(int(value) for value in row["target"]),
            ),
        )
        target = tuple(int(value) for value in first["target"])
        gap = target[1] - target[0]
        weight = Fraction(first["target_weight"])
        near = step <= gap
        pair_holes[pair].append((completion, weight))
        if near:
            near_pair_holes[pair].append((completion, weight))
        rows.append(
            (
                completion,
                witness,
                missing,
                pair,
                target,
                fraction_text(weight),
                step,
                gap,
                near,
            )
        )

    all_profile = profile_rows(pair_holes)
    near_profile = profile_rows(near_pair_holes)
    if int(all_profile["maximum_multiplicity"]) > 2:
        raise AssertionError("canonical support-pair multiplicity exceeds two")
    if int(near_profile["maximum_multiplicity"]) > 2:
        raise AssertionError("near support-pair multiplicity exceeds two")

    output = {
        "schema": "canonical_hole_support_pair_profile_v1",
        "scope": "certified_S7_holes_on_terminal_pair_payment_frontier",
        "generation_six_propagated": False,
        "certified_holes": len(holes),
        "all": all_profile,
        "near_h_le_D": near_profile,
        "hashes": {
            "assignment_rows_sha256": canonical_hash(rows),
        },
        "checks": {
            "all_holes_assigned": len(rows) == len(holes),
            "support_pair_multiplicity_at_most_two": (
                int(all_profile["maximum_multiplicity"]) <= 2
            ),
            "near_support_pair_multiplicity_at_most_two": (
                int(near_profile["maximum_multiplicity"]) <= 2
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["profile_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output_path.write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
