#!/usr/bin/env python3
"""Exhaustively verify the full-color coordinated branching identity.

For every four-AP-free subset of [1,12], construct:

- the parity-selected side child of every three-AP;
- the unique middle child indexed by chi(d)=v2(d)-v3(d) mod 3.

Verify exactly two child memberships per three-AP, exact harmonic identity
sum H(children)=2 L_3(B), four-AP-freeness of every child, and pairwise
disjoint first three dilates inside every child.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 12


def valuation(value: int, prime: int) -> int:
    if value <= 0:
        raise ValueError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def contains_four_ap(values: set[int] | frozenset[int]) -> bool:
    ordered = sorted(values)
    present = set(ordered)
    for left in ordered:
        for step in range(1, (ordered[-1] - left) // 3 + 1 if ordered else 0):
            if {left + step, left + 2 * step, left + 3 * step} <= present:
                return True
    return False


def three_aps(values: set[int] | frozenset[int]) -> tuple[tuple[int, int, int, int], ...]:
    ordered = sorted(values)
    present = set(ordered)
    rows: list[tuple[int, int, int, int]] = []
    for left in ordered:
        for middle in ordered:
            if middle <= left:
                continue
            step = middle - left
            right = middle + step
            if right in present:
                rows.append((left, middle, right, step))
    return tuple(rows)


def harmonic(values: set[int] | frozenset[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def child_family(
    values: frozenset[int],
) -> tuple[
    dict[tuple[str, int, int | None], frozenset[int]],
    dict[tuple[int, int, int, int], tuple[tuple[str, int, int | None], ...]],
]:
    children: dict[tuple[str, int, int | None], set[int]] = defaultdict(set)
    memberships: dict[
        tuple[int, int, int, int], list[tuple[str, int, int | None]]
    ] = defaultdict(list)

    for left, middle, right, step in three_aps(values):
        if valuation(step, 2) % 2 == 0:
            side_key = ("side_first", left, None)
        else:
            side_key = ("side_last", right, None)
        color = (valuation(step, 2) - valuation(step, 3)) % 3
        middle_key = ("middle", middle, color)

        children[side_key].add(step)
        children[middle_key].add(step)
        memberships[(left, middle, right, step)].extend((side_key, middle_key))

    return (
        {key: frozenset(steps) for key, steps in children.items()},
        {row: tuple(keys) for row, keys in memberships.items()},
    )


def verify_child(key: tuple[str, int, int | None], steps: frozenset[int]) -> None:
    if not steps:
        raise AssertionError(f"empty child {key}")
    if contains_four_ap(steps):
        raise AssertionError(f"child {key} contains a four-AP: {sorted(steps)}")
    first = set(steps)
    second = {2 * step for step in steps}
    third = {3 * step for step in steps}
    if first & second:
        raise AssertionError(f"child {key} has S/2S overlap")
    if first & third:
        raise AssertionError(f"child {key} has S/3S overlap")
    if second & third:
        raise AssertionError(f"child {key} has 2S/3S overlap")


def main() -> int:
    interval = tuple(range(1, LIMIT + 1))
    tested = 0
    ap_bearing = 0
    total_three_aps = 0
    total_child_states = 0
    total_child_memberships = 0
    maximum_three_aps = 0
    maximum_children = 0
    records: list[dict[str, object]] = []

    for mask in range(1 << LIMIT):
        values = frozenset(
            interval[index]
            for index in range(LIMIT)
            if mask & (1 << index)
        )
        if contains_four_ap(values):
            continue
        tested += 1
        aps = three_aps(values)
        children, memberships = child_family(values)

        if aps:
            ap_bearing += 1
        total_three_aps += len(aps)
        total_child_states += len(children)
        total_child_memberships += sum(len(keys) for keys in memberships.values())
        maximum_three_aps = max(maximum_three_aps, len(aps))
        maximum_children = max(maximum_children, len(children))

        if set(memberships) != set(aps):
            raise AssertionError("three-AP membership domain mismatch")
        for progression in aps:
            keys = memberships[progression]
            if len(keys) != 2 or len(set(keys)) != 2:
                raise AssertionError(
                    f"progression {progression} has memberships {keys}"
                )
            if {keys[0][0], keys[1][0]} != {
                "middle",
                "side_first" if keys[0][0] == "side_first" or keys[1][0] == "side_first" else "side_last",
            }:
                roles = {key[0] for key in keys}
                if "middle" not in roles or not roles & {"side_first", "side_last"}:
                    raise AssertionError(
                        f"progression {progression} has invalid roles {roles}"
                    )
            step = progression[3]
            if any(step not in children[key] for key in keys):
                raise AssertionError("membership step absent from child")

        for key, steps in children.items():
            verify_child(key, steps)

        load = sum((Fraction(1, row[3]) for row in aps), Fraction())
        child_mass = sum((harmonic(steps) for steps in children.values()), Fraction())
        if child_mass != 2 * load:
            raise AssertionError(
                f"mass identity failed for {sorted(values)}: "
                f"{child_mass} != 2*{load}"
            )

        records.append(
            {
                "values": list(values),
                "three_aps": len(aps),
                "children": len(children),
                "memberships": sum(len(keys) for keys in memberships.values()),
                "load": fraction_text(load),
                "child_mass": fraction_text(child_mass),
                "child_hash": canonical_hash(
                    [
                        [list(key), sorted(steps)]
                        for key, steps in sorted(children.items())
                    ]
                ),
            }
        )

    if total_child_memberships != 2 * total_three_aps:
        raise AssertionError("aggregate two-membership identity failed")

    output = {
        "schema": "full_color_coordinated_branching_exhaustive_v1",
        "interval": [1, LIMIT],
        "four_ap_free_subsets_tested": tested,
        "subsets_with_three_aps": ap_bearing,
        "total_three_ap_occurrences": total_three_aps,
        "total_child_states": total_child_states,
        "total_child_memberships": total_child_memberships,
        "maximum_three_aps_in_one_subset": maximum_three_aps,
        "maximum_children_in_one_subset": maximum_children,
        "exact_two_memberships_per_progression": True,
        "all_children_four_ap_free": True,
        "all_children_have_disjoint_first_three_dilates": True,
        "exact_harmonic_identity": "sum_children_H=2*weighted_three_AP_load",
        "records_sha256": canonical_hash(records),
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
