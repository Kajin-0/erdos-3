#!/usr/bin/env python3
"""Exhaustively verify the exact activated-pair union transfer row."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
import hashlib
import json
import sys

from verify_full_edge_coordinated_branching import contains_four_ap, pair_weight

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXHAUSTIVE_LIMIT = 16
BASE_SIX_MAX_N = 6


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


def harmonic(values: set[int] | frozenset[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def occurrences(values: frozenset[int]) -> tuple[tuple[int, int], ...]:
    ordered = sorted(values)
    lookup = values
    rows = []
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            if middle + step in lookup:
                rows.append((left, step))
    return tuple(rows)


def profile(values: frozenset[int]) -> dict[str, object]:
    if contains_four_ap(values):
        raise AssertionError("profile input contains a four-AP")
    rows = occurrences(values)
    by_step: dict[int, list[int]] = defaultdict(list)
    for start, step in rows:
        by_step[step].append(start)

    step_edges: set[tuple[int, int]] = set()
    near_targets: dict[tuple[int, int], set[int]] = defaultdict(set)
    far_fibers: dict[tuple[int, int], set[int]] = defaultdict(set)
    near_incidence_count = 0
    far_incidence_count = 0

    for step, starts in by_step.items():
        base = min(starts)
        step_edge = (base, base + step)
        if step_edge in step_edges:
            raise AssertionError("duplicate base-step edge")
        step_edges.add(step_edge)
        for start in starts:
            if start == base:
                continue
            delta = start - base
            if delta <= step:
                target = (base + step, start + step)
                if step in near_targets[target]:
                    raise AssertionError("duplicate near target incidence")
                near_targets[target].add(step)
                near_incidence_count += 1
            else:
                pair = (base, start)
                if step in far_fibers[pair]:
                    raise AssertionError("duplicate far fiber incidence")
                far_fibers[pair].add(step)
                far_incidence_count += 1

    activated = step_edges | set(near_targets)
    activated_mass = sum((pair_weight(pair) for pair in activated), Fraction())
    step_mass = sum((pair_weight(pair) for pair in step_edges), Fraction())
    occurrence_mass = sum((Fraction(1, step) for _start, step in rows), Fraction())

    recursive_new_mass = Fraction()
    recursive_reused_mass = Fraction()
    recursive_far_mass = Fraction()
    pair_payment_slack = Fraction()
    reused_target_count = 0
    new_target_count = 0
    fiber_rows = []

    for target, steps in sorted(near_targets.items()):
        if contains_four_ap(frozenset(steps)):
            raise AssertionError("near target preimage steps contain a four-AP")
        if any(step < target[1] - target[0] for step in steps):
            raise AssertionError("near target contains a far step")
        base_step = min(steps)
        if target in step_edges:
            residual = set(steps)
            recursive_reused_mass += harmonic(residual)
            reused_target_count += 1
            classification = "reused_step_edge"
            paid_step = None
        else:
            residual = set(steps)
            residual.remove(base_step)
            recursive_new_mass += harmonic(residual)
            pair_payment_slack += pair_weight(target) - Fraction(1, base_step)
            if pair_payment_slack < 0:
                raise AssertionError("new translated pair has negative payment slack")
            new_target_count += 1
            classification = "new_pair"
            paid_step = base_step
        fiber_rows.append(
            {
                "kind": "near",
                "target": list(target),
                "steps": sorted(steps),
                "classification": classification,
                "paid_step": paid_step,
                "residual_steps": sorted(residual),
            }
        )

    for pair, steps in sorted(far_fibers.items()):
        if contains_four_ap(frozenset(steps)):
            raise AssertionError("far step fiber contains a four-AP")
        delta = pair[1] - pair[0]
        if any(step >= delta for step in steps):
            raise AssertionError("far fiber contains a near step")
        recursive_far_mass += harmonic(steps)
        fiber_rows.append(
            {
                "kind": "far",
                "pair": list(pair),
                "steps": sorted(steps),
            }
        )

    recursive_mass = recursive_new_mass + recursive_reused_mass + recursive_far_mass
    rhs = activated_mass + recursive_mass
    if occurrence_mass > rhs:
        raise AssertionError("activated-pair union transfer inequality failed")

    base_occurrences = len(by_step)
    collision_occurrences = len(rows) - base_occurrences
    if collision_occurrences != near_incidence_count + far_incidence_count:
        raise AssertionError("collision incidence partition failed")

    return {
        "parent_size": len(values),
        "parent_min": min(values) if values else None,
        "parent_max": max(values) if values else None,
        "occurrences": len(rows),
        "used_steps": len(by_step),
        "collision_occurrences": collision_occurrences,
        "near_incidence_count": near_incidence_count,
        "far_incidence_count": far_incidence_count,
        "step_edges": len(step_edges),
        "near_targets": len(near_targets),
        "new_near_targets": new_target_count,
        "reused_step_edge_targets": reused_target_count,
        "activated_pairs": len(activated),
        "occurrence_mass": fraction_record(occurrence_mass),
        "step_edge_mass": fraction_record(step_mass),
        "activated_pair_union_mass": fraction_record(activated_mass),
        "recursive_new_target_mass": fraction_record(recursive_new_mass),
        "recursive_reused_target_mass": fraction_record(recursive_reused_mass),
        "recursive_far_mass": fraction_record(recursive_far_mass),
        "recursive_total_mass": fraction_record(recursive_mass),
        "pair_payment_slack": fraction_record(pair_payment_slack),
        "row_rhs": fraction_record(rhs),
        "row_surplus": fraction_record(rhs - occurrence_mass),
        "fiber_rows_sha256": canonical_hash(fiber_rows),
    }


def digit_set(n: int) -> frozenset[int]:
    powers = [6**index for index in range(n)]
    return frozenset(
        sum(digit * power for digit, power in zip(digits, powers, strict=True))
        for digits in product(range(3), repeat=n)
    )


def multiplicity_four_support() -> frozenset[int]:
    refs = frozenset({2, 6, 18, 54})
    step = 64
    base = 1024
    center = 55
    roots = frozenset({base + center, base + center + step, base + center + 2 * step})
    return frozenset(refs | roots | {2 * root - ref for root in roots for ref in refs})


def main() -> int:
    metrics = defaultdict(int)
    aggregate_occurrence = Fraction()
    aggregate_activated = Fraction()
    aggregate_recursive = Fraction()
    aggregate_surplus = Fraction()
    records_hash = hashlib.sha256()
    maximum_recursive_ratio = Fraction()
    maximum_recursive_witness = None
    maximum_pair_overlap = 0
    overlap_witness = None

    for mask in range(1 << EXHAUSTIVE_LIMIT):
        values = frozenset(
            index + 1 for index in range(EXHAUSTIVE_LIMIT) if mask & (1 << index)
        )
        if contains_four_ap(values):
            continue
        row = profile(values)
        records_hash.update(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        )
        metrics["four_ap_free_subsets"] += 1
        for name in (
            "occurrences",
            "used_steps",
            "collision_occurrences",
            "near_incidence_count",
            "far_incidence_count",
            "step_edges",
            "near_targets",
            "new_near_targets",
            "reused_step_edge_targets",
            "activated_pairs",
        ):
            metrics[name] += int(row[name])
        maximum_pair_overlap = max(maximum_pair_overlap, int(row["reused_step_edge_targets"]))
        if int(row["reused_step_edge_targets"]) == maximum_pair_overlap:
            overlap_witness = row
        occurrence_mass = Fraction(row["occurrence_mass"]["fraction"])
        activated_mass = Fraction(row["activated_pair_union_mass"]["fraction"])
        recursive_mass = Fraction(row["recursive_total_mass"]["fraction"])
        surplus = Fraction(row["row_surplus"]["fraction"])
        aggregate_occurrence += occurrence_mass
        aggregate_activated += activated_mass
        aggregate_recursive += recursive_mass
        aggregate_surplus += surplus
        if occurrence_mass:
            ratio = recursive_mass / occurrence_mass
            if ratio > maximum_recursive_ratio:
                maximum_recursive_ratio = ratio
                maximum_recursive_witness = row

    base_six = []
    for n in range(1, BASE_SIX_MAX_N + 1):
        row = profile(digit_set(n))
        row["n"] = n
        base_six.append(row)

    mult4 = profile(multiplicity_four_support())

    output = {
        "schema": "exact_activated_pair_union_transfer_probe_v1",
        "exhaustive_interval": [1, EXHAUSTIVE_LIMIT],
        "exhaustive_metrics": dict(metrics),
        "exhaustive_masses": {
            "occurrence": fraction_record(aggregate_occurrence),
            "activated_pair_union": fraction_record(aggregate_activated),
            "recursive": fraction_record(aggregate_recursive),
            "surplus": fraction_record(aggregate_surplus),
        },
        "maximum_recursive_over_occurrence": {
            "ratio": fraction_record(maximum_recursive_ratio),
            "witness": maximum_recursive_witness,
        },
        "maximum_reused_step_edge_targets": maximum_pair_overlap,
        "maximum_pair_overlap_witness": overlap_witness,
        "base_six": base_six,
        "multiplicity_four_gadget": mult4,
        "verified": {
            "all_activated_pairs_paid_once": True,
            "all_near_preimage_sets_four_ap_free": True,
            "all_far_fibers_four_ap_free": True,
            "all_recursive_fibers_strictly_lower_scale": True,
            "activated_pair_union_transfer_row": True,
        },
        "records_sha256": records_hash.hexdigest(),
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
