#!/usr/bin/env python3
"""Verify the AP occurrence-family light/heavy transfer on exact benchmarks."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
import hashlib
import json
import sys

from verify_full_edge_coordinated_branching import contains_four_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXHAUSTIVE_LIMIT = 14
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


def three_ap_occurrences(values: frozenset[int]) -> tuple[tuple[int, int], ...]:
    ordered = sorted(values)
    lookup = values
    rows = []
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            if middle + step in lookup:
                rows.append((left, step))
    return tuple(rows)


def harmonic(values: set[int] | frozenset[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def profile(values: frozenset[int], occurrences: tuple[tuple[int, int], ...] | None = None) -> dict[str, object]:
    if contains_four_ap(values):
        raise AssertionError("profile input contains a four-AP")
    rows = occurrences if occurrences is not None else three_ap_occurrences(values)
    if len(rows) != len(set(rows)):
        raise AssertionError("occurrence family contains duplicates")
    by_step: dict[int, list[int]] = defaultdict(list)
    for start, step in rows:
        if not {start, start + step, start + 2 * step}.issubset(values):
            raise AssertionError("selected occurrence is not contained in parent")
        by_step[step].append(start)

    fibers: dict[tuple[int, int], set[int]] = defaultdict(set)
    step_edges = set()
    first_mass = Fraction()
    for step, starts in by_step.items():
        base = min(starts)
        step_edges.add((base, base + step))
        first_mass += Fraction(1, step)
        for start in starts:
            if start == base:
                continue
            fibers[(base, start)].add(step)

    if len(step_edges) != len(by_step):
        raise AssertionError("distinct steps produced duplicate base edges")

    occurrence_mass = sum((Fraction(1, step) for _start, step in rows), Fraction())
    fiber_mass = sum((harmonic(steps) for steps in fibers.values()), Fraction())
    if occurrence_mass != first_mass + fiber_mass:
        raise AssertionError("transpose identity failed")

    light_mass = Fraction()
    heavy_mass = Fraction()
    light_pair_mass = Fraction()
    light_count = 0
    heavy_count = 0
    far_fiber_count = 0
    heavy_without_far_count = 0
    heavy_shell_count = 0
    records = []

    for pair, steps in sorted(fibers.items()):
        left, right = pair
        delta = right - left
        mass = harmonic(steps)
        if contains_four_ap(frozenset(steps)):
            raise AssertionError("step fiber contains a four-AP")
        if any(step >= (max(values) - min(values) + 1) for step in steps):
            raise AssertionError("step fiber failed scale descent")
        has_far = any(step < delta for step in steps)
        is_light = mass <= Fraction(1, delta)
        if is_light and has_far:
            raise AssertionError("light fiber contains a far incidence")
        shell_exponents = {step.bit_length() - 1 for step in steps}
        if is_light:
            light_count += 1
            light_mass += mass
            light_pair_mass += Fraction(1, delta)
        else:
            heavy_count += 1
            heavy_mass += mass
            heavy_shell_count += len(shell_exponents)
            far_fiber_count += int(has_far)
            heavy_without_far_count += int(not has_far)
        records.append(
            {
                "pair": [left, right],
                "delta": delta,
                "steps": sorted(steps),
                "mass": fraction_record(mass),
                "light": is_light,
                "has_far_step": has_far,
                "shell_exponents": sorted(shell_exponents),
            }
        )

    if light_mass > light_pair_mass:
        raise AssertionError("light fibers exceed activated pair capacity")
    if occurrence_mass != first_mass + light_mass + heavy_mass:
        raise AssertionError("light/heavy mass decomposition failed")

    return {
        "parent_size": len(values),
        "parent_min": min(values) if values else None,
        "parent_max": max(values) if values else None,
        "occurrences": len(rows),
        "used_steps": len(by_step),
        "fibers": len(fibers),
        "light_fibers": light_count,
        "heavy_fibers": heavy_count,
        "far_heavy_fibers": far_fiber_count,
        "near_only_heavy_fibers": heavy_without_far_count,
        "heavy_shells": heavy_shell_count,
        "occurrence_mass": fraction_record(occurrence_mass),
        "first_step_mass": fraction_record(first_mass),
        "fiber_mass": fraction_record(fiber_mass),
        "light_fiber_mass": fraction_record(light_mass),
        "light_pair_capacity": fraction_record(light_pair_mass),
        "heavy_fiber_mass": fraction_record(heavy_mass),
        "fiber_records_sha256": canonical_hash(records),
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


def small_reuse_support() -> frozenset[int]:
    return frozenset({0, 2, 19, 23, 25, 27, 36, 44, 46, 50, 52, 54})


def main() -> int:
    exhaustive_metrics = defaultdict(int)
    exhaustive_hash = hashlib.sha256()
    for mask in range(1 << EXHAUSTIVE_LIMIT):
        values = frozenset(
            index + 1 for index in range(EXHAUSTIVE_LIMIT) if mask & (1 << index)
        )
        if contains_four_ap(values):
            continue
        row = profile(values)
        exhaustive_hash.update(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        )
        exhaustive_metrics["four_ap_free_subsets"] += 1
        exhaustive_metrics["occurrences"] += int(row["occurrences"])
        exhaustive_metrics["fibers"] += int(row["fibers"])
        exhaustive_metrics["light_fibers"] += int(row["light_fibers"])
        exhaustive_metrics["heavy_fibers"] += int(row["heavy_fibers"])
        exhaustive_metrics["far_heavy_fibers"] += int(row["far_heavy_fibers"])
        exhaustive_metrics["near_only_heavy_fibers"] += int(row["near_only_heavy_fibers"])

    base_six = []
    for n in range(1, BASE_SIX_MAX_N + 1):
        row = profile(digit_set(n))
        row["n"] = n
        row["unit_step_expected_collisions"] = 3 ** (n - 1) - 1
        base_six.append(row)

    small = profile(small_reuse_support())
    mult4 = profile(multiplicity_four_support())

    output = {
        "schema": "ap_occurrence_light_heavy_transfer_probe_v1",
        "exhaustive_interval": [1, EXHAUSTIVE_LIMIT],
        "exhaustive_metrics": dict(exhaustive_metrics),
        "exhaustive_records_sha256": exhaustive_hash.hexdigest(),
        "base_six": base_six,
        "small_reuse_gadget": small,
        "multiplicity_four_gadget": mult4,
        "verified": {
            "exact_occurrence_transpose_identity": True,
            "all_step_fibers_four_ap_free": True,
            "all_light_fibers_near_only": True,
            "light_mass_bounded_by_pair_capacity": True,
            "heavy_fibers_strictly_lower_scale": True,
        },
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
