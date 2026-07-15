#!/usr/bin/env python3
"""Transport only canonical hole-support pairs new to the activated source union."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    pair_weight,
    parent_schedule,
    reconstruct_fourth_recursive,
    serialize_mass,
    transport,
)

Pair = tuple[int, int]


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


def completion_roots(pair: Pair, roots: set[int]) -> set[int]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return candidates & roots


def read_holes(path: Path) -> dict[int, tuple[tuple[int, ...], int]]:
    holes: dict[int, tuple[tuple[int, ...], int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["status"] != "certified_S7_hole":
                continue
            completion = int(row["completion"])
            witness = tuple(int(row[f"p{index}"]) for index in range(4))
            missing = int(row["missing_index"])
            holes[completion] = witness, missing
    return holes


def canonical_pair(witness: tuple[int, ...], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def profile_pairs(pairs: set[Pair]) -> dict[str, object]:
    return {
        "pairs": len(pairs),
        "pair_union_mass": serialize_mass(
            sum((pair_weight(pair) for pair in pairs), Fraction())
        ),
    }


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: summarize_s7_new_hole_support_transport.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path, classification_path, output_path = map(Path, sys.argv[1:])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    holes = read_holes(classification_path)
    s7 = build_s7()
    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        target = tuple(int(value) for value in row["target"])
        if completion_roots(target, s7):
            continue
        completions = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completions) != 1:
            raise AssertionError("one edge-unresolved target has several completions")
        completion = next(iter(completions))
        if completion in holes:
            targets_by_completion[completion].append(row)
    if set(targets_by_completion) != set(holes):
        raise AssertionError("certified-hole target family is incomplete")

    support_pairs = {
        canonical_pair(*holes[completion]) for completion in sorted(holes)
    }
    original_source_pairs = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    existing_supports = support_pairs & original_source_pairs
    new_supports = support_pairs - original_source_pairs

    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}
    owned_activated: dict[Pair, int] = {}
    owned_residual: set[Pair] = set()
    cross_parent: set[Pair] = set()

    for pair in sorted(new_supports):
        owners = [
            parent_class
            for parent_class, schedule in schedules.items()
            if set(pair) <= schedule["roots"]
        ]
        if len(owners) > 1:
            raise AssertionError("new support pair belongs to several parent classes")
        if not owners:
            cross_parent.add(pair)
            continue
        parent_class = owners[0]
        schedule = schedules[parent_class]
        sponsors: set[int] = schedule["sponsors"]  # type: ignore[assignment]
        residual: set[int] = schedule["residual"]  # type: ignore[assignment]
        if set(pair) & sponsors:
            owned_activated[pair] = parent_class
        else:
            if not set(pair) <= residual:
                raise AssertionError("owned support pair is neither activated nor residual")
            owned_residual.add(pair)

    if set(owned_activated) | owned_residual | cross_parent != new_supports:
        raise AssertionError("new support ownership partition failed")

    transport_rows: list[dict[str, object]] = []
    for pair, parent_class in sorted(owned_activated.items()):
        result = transport(pair, schedules[parent_class])
        target: Pair = result["target"]  # type: ignore[assignment]
        path = result["path"]
        transport_rows.append(
            {
                "pair": pair,
                "parent_class": parent_class,
                "initial_weight": pair_weight(pair),
                "target": target,
                "target_weight": pair_weight(target),
                "terminal_class": result["terminal_class"],
                "path_length": len(path),
            }
        )

    new_by_target: dict[Pair, list[dict[str, object]]] = defaultdict(list)
    for row in transport_rows:
        new_by_target[row["target"]].append(row)  # type: ignore[index]

    existing_by_target: dict[Pair, list[Fraction]] = {}
    for row in target_rows:
        target = tuple(int(value) for value in row["target"])
        weights = [Fraction(record[2]) for record in row["source_pairs"]]
        if not weights:
            raise AssertionError("existing terminal target has no source weights")
        existing_by_target[target] = weights

    old_source_collision = sum(
        (Fraction(row["source_collision_weight"]) for row in target_rows),
        Fraction(),
    )
    combined_source_collision = Fraction()
    combined_target_union = Fraction()
    all_targets = set(existing_by_target) | set(new_by_target)
    for target in all_targets:
        weights = list(existing_by_target.get(target, ()))
        weights.extend(
            row["initial_weight"] for row in new_by_target.get(target, ())
        )
        combined_target_union += pair_weight(target)
        combined_source_collision += sum(weights, Fraction()) - max(weights)

    existing_target_union = sum(
        (pair_weight(target) for target in existing_by_target), Fraction()
    )
    new_initial_mass = sum(
        (row["initial_weight"] for row in transport_rows), Fraction()
    )
    new_target_occurrence_mass = sum(
        (row["target_weight"] for row in transport_rows), Fraction()
    )
    new_target_union_mass = sum(
        (pair_weight(target) for target in new_by_target), Fraction()
    )
    new_terminal_collision = (
        new_target_occurrence_mass - new_target_union_mass
    )
    new_target_overlap = set(new_by_target) & set(existing_by_target)
    new_target_overlap_mass = sum(
        (pair_weight(target) for target in new_target_overlap), Fraction()
    )
    incremental_collision = combined_source_collision - old_source_collision
    incremental_target_union = combined_target_union - existing_target_union
    old_initial_mass = Fraction(
        payment["masses"]["activated_initial_union"]["fraction"]
    )
    extended_initial_mass = old_initial_mass + new_initial_mass
    extended_rhs = combined_target_union + combined_source_collision
    if extended_initial_mass > extended_rhs:
        raise AssertionError("extended source-weighted transport inequality failed")

    terminal_classes = Counter(
        str(row["terminal_class"]) for row in transport_rows
    )
    path_lengths = Counter(int(row["path_length"]) for row in transport_rows)
    parent_counts = Counter(int(row["parent_class"]) for row in transport_rows)

    serial_rows = [
        {
            key: (
                f"{value.numerator}/{value.denominator}"
                if isinstance(value, Fraction)
                else list(value)
                if isinstance(value, tuple)
                else value
            )
            for key, value in row.items()
        }
        for row in transport_rows
    ]
    output = {
        "schema": "s7_new_hole_support_transport_profile_v1",
        "scope": "canonical certified-hole supports new to the activated source union",
        "generation_six_propagated": False,
        "support_identity": {
            "all": profile_pairs(support_pairs),
            "already_in_source_union": profile_pairs(existing_supports),
            "new_to_source_union": profile_pairs(new_supports),
        },
        "new_support_ownership": {
            "owned_activated": profile_pairs(set(owned_activated)),
            "owned_residual": profile_pairs(owned_residual),
            "cross_parent": profile_pairs(cross_parent),
        },
        "transport": {
            "source_pairs": len(transport_rows),
            "terminal_targets": len(new_by_target),
            "targets_already_in_existing_terminal_union": len(new_target_overlap),
            "initial_mass": serialize_mass(new_initial_mass),
            "target_occurrence_mass": serialize_mass(new_target_occurrence_mass),
            "target_union_mass": serialize_mass(new_target_union_mass),
            "terminal_collision_mass": serialize_mass(new_terminal_collision),
            "existing_target_overlap_mass": serialize_mass(new_target_overlap_mass),
            "incremental_target_union_mass": serialize_mass(
                incremental_target_union
            ),
            "incremental_source_collision_mass": serialize_mass(
                incremental_collision
            ),
            "terminal_class_counts": dict(sorted(terminal_classes.items())),
            "path_length_counts": {
                str(key): value for key, value in sorted(path_lengths.items())
            },
            "parent_counts": {
                str(key): value for key, value in sorted(parent_counts.items())
            },
        },
        "extended_ledger": {
            "old_activated_initial_mass": serialize_mass(old_initial_mass),
            "extended_activated_initial_mass": serialize_mass(
                extended_initial_mass
            ),
            "combined_terminal_target_union_mass": serialize_mass(
                combined_target_union
            ),
            "old_source_collision_mass": serialize_mass(old_source_collision),
            "combined_source_collision_mass": serialize_mass(
                combined_source_collision
            ),
            "combined_rhs": serialize_mass(extended_rhs),
            "combined_slack": serialize_mass(extended_rhs - extended_initial_mass),
        },
        "hashes": {
            "transport_rows_sha256": canonical_hash(serial_rows),
            "new_support_pairs_sha256": canonical_hash(sorted(new_supports)),
        },
        "checks": {
            "support_identity_partition": (
                existing_supports | new_supports == support_pairs
                and not (existing_supports & new_supports)
            ),
            "new_support_ownership_partition": (
                set(owned_activated) | owned_residual | cross_parent
                == new_supports
            ),
            "transport_monotonicity": all(
                row["initial_weight"] <= row["target_weight"]
                for row in transport_rows
            ),
            "extended_source_weighted_transport_inequality": (
                extended_initial_mass <= extended_rhs
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
