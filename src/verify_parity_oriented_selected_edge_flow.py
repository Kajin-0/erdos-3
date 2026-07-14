#!/usr/bin/env python3
"""Exhaustively verify parity-oriented selected-edge flow on [1,14]."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

from verify_full_edge_coordinated_branching import contains_four_ap, pair_weight, valuation

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 14


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def fraction_record(value: Fraction) -> dict[str, str]:
    text = f"{value.numerator}/{value.denominator}"
    return {
        "fraction": text,
        "decimal": f"{float(value):.12f}",
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def three_aps(values: set[int]) -> list[tuple[int, int]]:
    rows = []
    for left in sorted(values):
        for middle in sorted(value for value in values if value > left):
            step = middle - left
            if middle + step in values:
                rows.append((left, step))
    return rows


def run_schedule(initial: frozenset[int]) -> dict[str, object]:
    current = set(initial)
    direct_pairs: dict[tuple[int, int], int] = {}
    survivor_pairs: dict[tuple[int, int], int] = {}
    actions = []

    while True:
        aps = three_aps(current)
        if not aps:
            break
        left, step = min(aps, key=lambda row: (row[1], row[0]))
        points = (left, left + step, left + 2 * step)
        if valuation(step, 2) % 2 == 0:
            sponsor = points[0]
            survivors = (points[1], points[2])
            orientation = "left"
        else:
            sponsor = points[2]
            survivors = (points[0], points[1])
            orientation = "right"
        middle = points[1]
        opposite = points[2] if sponsor == points[0] else points[0]
        direct = tuple(sorted(((sponsor, middle), (sponsor, opposite))))
        survivor = tuple(sorted(survivors))
        index = len(actions)

        for pair in direct:
            if pair in direct_pairs:
                raise AssertionError("sponsor edge repeated")
            direct_pairs[pair] = index
        if survivor in survivor_pairs:
            raise AssertionError("survivor edge repeated")
        survivor_pairs[survivor] = index

        actions.append(
            {
                "index": index,
                "left": left,
                "step": step,
                "orientation": orientation,
                "sponsor": sponsor,
                "survivors": list(survivors),
                "direct_pairs": [list(pair) for pair in direct],
                "survivor_pair": list(survivor),
            }
        )
        current.remove(sponsor)

    if three_aps(current):
        raise AssertionError("schedule did not terminate at a three-AP-free residual")

    overlap = set(direct_pairs) & set(survivor_pairs)
    for pair in overlap:
        if not survivor_pairs[pair] < direct_pairs[pair]:
            raise AssertionError("overlap pair was not created before release")

    selected_load = sum((Fraction(1, row["step"]) for row in actions), Fraction())
    direct_mass = sum((pair_weight(pair) for pair in direct_pairs), Fraction())
    survivor_mass = sum((pair_weight(pair) for pair in survivor_pairs), Fraction())
    union = set(direct_pairs) | set(survivor_pairs)
    union_mass = sum((pair_weight(pair) for pair in union), Fraction())
    overlap_mass = sum((pair_weight(pair) for pair in overlap), Fraction())

    if direct_mass != Fraction(3, 2) * selected_load:
        raise AssertionError("direct edge mass identity failed")
    if survivor_mass != selected_load:
        raise AssertionError("survivor edge mass identity failed")
    if direct_mass + survivor_mass != union_mass + overlap_mass:
        raise AssertionError("creation/release union identity failed")
    if direct_mass + survivor_mass != Fraction(5, 2) * selected_load:
        raise AssertionError("complete edge energy identity failed")

    return {
        "initial": sorted(initial),
        "initial_size": len(initial),
        "actions": len(actions),
        "residual": sorted(current),
        "residual_size": len(current),
        "direct_pairs": len(direct_pairs),
        "survivor_pairs": len(survivor_pairs),
        "union_pairs": len(union),
        "overlap_pairs": len(overlap),
        "selected_load": fraction_record(selected_load),
        "direct_mass": fraction_record(direct_mass),
        "survivor_mass": fraction_record(survivor_mass),
        "union_mass": fraction_record(union_mass),
        "overlap_mass": fraction_record(overlap_mass),
        "actions_sha256": canonical_hash(actions),
    }


def main() -> int:
    metrics = Counter()
    records_hash = hashlib.sha256()
    maximum_actions = None
    maximum_overlap = None
    aggregate_selected = Fraction()
    aggregate_union = Fraction()
    aggregate_overlap = Fraction()

    for mask in range(1 << LIMIT):
        values = frozenset(index + 1 for index in range(LIMIT) if mask & (1 << index))
        if contains_four_ap(values):
            continue
        row = run_schedule(values)
        records_hash.update(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        )
        metrics["four_ap_free_subsets"] += 1
        for name in (
            "actions",
            "direct_pairs",
            "survivor_pairs",
            "union_pairs",
            "overlap_pairs",
        ):
            metrics[name] += int(row[name])
        if maximum_actions is None or row["actions"] > maximum_actions["actions"]:
            maximum_actions = row
        if maximum_overlap is None or row["overlap_pairs"] > maximum_overlap["overlap_pairs"]:
            maximum_overlap = row
        aggregate_selected += Fraction(row["selected_load"]["fraction"])
        aggregate_union += Fraction(row["union_mass"]["fraction"])
        aggregate_overlap += Fraction(row["overlap_mass"]["fraction"])

    output = {
        "schema": "parity_oriented_selected_edge_flow_certificate_v1",
        "interval": [1, LIMIT],
        "metrics": dict(metrics),
        "aggregate": {
            "selected_load": fraction_record(aggregate_selected),
            "union_mass": fraction_record(aggregate_union),
            "overlap_release_mass": fraction_record(aggregate_overlap),
        },
        "maximum_action_witness": maximum_actions,
        "maximum_overlap_witness": maximum_overlap,
        "verified": {
            "all_schedules_terminate_at_three_ap_free_residual": True,
            "all_sponsor_edges_distinct": True,
            "all_survivor_edges_distinct": True,
            "all_overlap_created_before_release": True,
            "direct_mass_equals_three_halves_selected_load": True,
            "survivor_mass_equals_selected_load": True,
            "union_plus_release_equals_five_halves_selected_load": True,
        },
        "records_sha256": records_hash.hexdigest(),
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
