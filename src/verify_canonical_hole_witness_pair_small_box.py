#!/usr/bin/env python3
"""Exhaust canonical four-AP hole-witness pair reuse on a small interval."""
from __future__ import annotations

from collections import Counter, defaultdict


def four_aps(lower: int, upper: int) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for left in range(lower, upper + 1):
        for step in range(1, (upper - left) // 3 + 1):
            rows.append(tuple(left + index * step for index in range(4)))
    return tuple(rows)


def contains_four_ap(values: set[int], progressions: tuple[tuple[int, ...], ...]) -> bool:
    return any(set(row) <= values for row in progressions)


def canonical_pair(witness: tuple[int, int, int, int], missing: int) -> tuple[int, int]:
    for index in range(3):
        if index != missing and index + 1 != missing:
            return witness[index], witness[index + 1]
    raise AssertionError("hole witness has no adjacent present pair")


def verify_pair_fiber(
    pair: tuple[int, int],
    holes: list[tuple[int, tuple[int, ...], int]],
) -> None:
    left, right = pair
    step = right - left
    if step <= 0:
        raise AssertionError("invalid canonical support pair")
    possible = {left - step, left + 2 * step, left + 3 * step}
    if any(hole not in possible for hole, _witness, _missing in holes):
        raise AssertionError("canonical hole left the three-value fiber")
    if len({hole for hole, _witness, _missing in holes}) > 2:
        raise AssertionError("canonical support pair serves more than two holes")


def main() -> int:
    parent_universe = tuple(range(1, 13))
    lower, upper = 0, 13
    progressions = four_aps(lower, upper)
    parent_progressions = tuple(
        row for row in progressions if set(row) <= set(parent_universe)
    )

    parent_count = 0
    parents_with_holes = 0
    hole_count = 0
    support_pair_fibers = 0
    reused_pair_fibers = 0
    maximum_multiplicity = 0
    multiplicities: Counter[int] = Counter()

    for mask in range(1 << len(parent_universe)):
        parent = {
            parent_universe[index]
            for index in range(len(parent_universe))
            if (mask >> index) & 1
        }
        if contains_four_ap(parent, parent_progressions):
            continue
        parent_count += 1

        witness_by_hole: dict[int, tuple[tuple[int, int, int, int], int]] = {}
        for witness in progressions:
            missing = [
                index for index, value in enumerate(witness) if value not in parent
            ]
            if len(missing) != 1:
                continue
            missing_index = missing[0]
            hole = witness[missing_index]
            candidate = (witness, missing_index)
            previous = witness_by_hole.get(hole)
            if previous is None or candidate < previous:
                witness_by_hole[hole] = candidate

        if not witness_by_hole:
            continue
        parents_with_holes += 1
        hole_count += len(witness_by_hole)
        fibers: dict[
            tuple[int, int], list[tuple[int, tuple[int, ...], int]]
        ] = defaultdict(list)
        for hole, (witness, missing_index) in witness_by_hole.items():
            pair = canonical_pair(witness, missing_index)
            if pair[0] not in parent or pair[1] not in parent:
                raise AssertionError("canonical support pair is not present")
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            fibers[pair].append((hole, witness, missing_index))

        for pair, holes in fibers.items():
            verify_pair_fiber(pair, holes)
            multiplicity = len({hole for hole, _witness, _missing in holes})
            support_pair_fibers += 1
            reused_pair_fibers += multiplicity > 1
            maximum_multiplicity = max(maximum_multiplicity, multiplicity)
            multiplicities[multiplicity] += 1

    if maximum_multiplicity != 2:
        raise AssertionError("small box did not attain sharp multiplicity two")

    print("canonical_hole_witness_pair_small_box_v1")
    print("parent_universe=[1,12]")
    print("witness_universe=[0,13]")
    print(f"four_ap_free_parents={parent_count}")
    print(f"parents_with_certified_holes={parents_with_holes}")
    print(f"certified_hole_checks={hole_count}")
    print(f"support_pair_fibers={support_pair_fibers}")
    print(f"reused_support_pair_fibers={reused_pair_fibers}")
    print(f"multiplicity_one_fibers={multiplicities[1]}")
    print(f"multiplicity_two_fibers={multiplicities[2]}")
    print(f"maximum_support_pair_multiplicity={maximum_multiplicity}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
