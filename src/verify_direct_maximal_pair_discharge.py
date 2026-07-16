#!/usr/bin/env python3
"""Exhaust the finite relative-maximal analogue of direct pair discharge."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json


Pair = tuple[int, int]
Progression = tuple[int, int, int, int]


def four_aps(lower: int, upper: int) -> tuple[Progression, ...]:
    rows: list[Progression] = []
    for left in range(lower, upper + 1):
        for step in range(1, (upper - left) // 3 + 1):
            rows.append(tuple(left + index * step for index in range(4)))
    return tuple(rows)


def contains_four_ap(values: set[int], rows: tuple[Progression, ...]) -> bool:
    return any(set(row) <= values for row in rows)


def three_aps(values: set[int]) -> tuple[tuple[int, int, int], ...]:
    if not values:
        return ()
    upper = max(values)
    rows: list[tuple[int, int, int]] = []
    for left in sorted(values):
        for step in range(1, (upper - left) // 2 + 1):
            middle = left + step
            right = left + 2 * step
            if middle in values and right in values:
                rows.append((left, middle, right))
    return tuple(rows)


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def canonical_pair(witness: Progression, missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            return witness[index], witness[index + 1]
    raise AssertionError("hole witness has no adjacent support")


def is_relative_maximal(
    parent: set[int], universe: set[int], progressions: tuple[Progression, ...]
) -> bool:
    if contains_four_ap(parent, progressions):
        return False
    return all(
        contains_four_ap(parent | {value}, progressions)
        for value in universe - parent
    )


def hole_witness(
    parent: set[int], completion: int, progressions: tuple[Progression, ...]
) -> tuple[Progression, int]:
    candidates: list[tuple[Progression, int]] = []
    for row in progressions:
        if completion not in row:
            continue
        missing = row.index(completion)
        if all(row[index] in parent for index in range(4) if index != missing):
            candidates.append((row, missing))
    if not candidates:
        raise AssertionError("relative maximality completion lacks a witness")
    return min(candidates)


def completion_candidates(
    pair: Pair, universe: set[int]
) -> list[tuple[int, str, int, Fraction]]:
    left, right = pair
    gap = right - left
    rows = [
        (left - gap, "right_adjacent", gap, Fraction(1)),
        (right + gap, "left_adjacent", gap, Fraction(1)),
    ]
    if gap % 2 == 0:
        rows.append((left + gap // 2, "outer", gap // 2, Fraction(1, 2)))
    return sorted(row for row in rows if row[0] in universe)


def classify_pair(
    parent: set[int],
    shell: set[int],
    pair: Pair,
    universe: set[int],
    progressions: tuple[Progression, ...],
) -> tuple[str, int, str, int, Fraction, Pair | None]:
    candidates = completion_candidates(pair, universe)
    if not candidates:
        raise AssertionError("eligible pair has no relative-universe completion")

    local = [row for row in candidates if row[0] in shell]
    if local:
        completion, role, step, coefficient = min(local)
        return "local", completion, role, step, coefficient, None

    cross = [row for row in candidates if row[0] in parent]
    if cross:
        completion, role, step, coefficient = min(cross)
        if role == "outer":
            raise AssertionError("outer completion left its dyadic shell")
        left, right = pair
        image = (completion, left) if completion < left else (right, completion)
        return "cross", completion, role, step, coefficient, image

    completion, role, step, coefficient = min(candidates)
    witness, missing = hole_witness(parent, completion, progressions)
    support = canonical_pair(witness, missing)
    return "hole", completion, role, step, coefficient, support


def harmonic(values: set[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def main() -> int:
    universe = set(range(1, 13))
    progressions = four_aps(1, 12)
    maximal_parents = [
        {value for value in universe if (mask >> (value - 1)) & 1}
        for mask in range(1 << len(universe))
    ]
    maximal_parents = [
        parent
        for parent in maximal_parents
        if is_relative_maximal(parent, universe, progressions)
    ]
    if len(maximal_parents) != 58:
        raise AssertionError("relative-maximal parent count changed")

    counts = Counter()
    profile_rows: list[object] = []
    maximum_roles_per_support = 0

    for parent in maximal_parents:
        for base in (1, 2, 4, 8):
            shell = {value for value in parent if base <= value < 2 * base}
            eligible_pairs = [
                pair
                for pair in combinations(sorted(shell), 2)
                if completion_candidates(pair, universe)
            ]

            for mask in range(1 << len(eligible_pairs)):
                activated = {
                    eligible_pairs[index]
                    for index in range(len(eligible_pairs))
                    if (mask >> index) & 1
                }
                counts["activated_families"] += 1
                counts["activated_pair_occurrences"] += len(activated)

                local: set[Pair] = set()
                cross_images: dict[Pair, Pair] = {}
                hole_rows: list[tuple[Pair, int, str, int, Fraction, Pair]] = []

                for pair in activated:
                    kind, completion, role, step, coefficient, output = classify_pair(
                        parent, shell, pair, universe, progressions
                    )
                    if kind == "local":
                        local.add(pair)
                    elif kind == "cross":
                        assert output is not None
                        previous = cross_images.get(output)
                        if previous is not None and previous != pair:
                            raise AssertionError("cross-shell edge swap is not injective")
                        cross_images[output] = pair
                    else:
                        assert output is not None
                        hole_rows.append(
                            (pair, completion, role, step, coefficient, output)
                        )

                counts["local_pairs"] += len(local)
                counts["cross_pairs"] += len(cross_images)
                counts["hole_pairs"] += len(hole_rows)

                local_mass = sum((pair_weight(pair) for pair in local), Fraction())
                local_capacity = Fraction(5, 2) * sum(
                    (
                        Fraction(1, middle - left)
                        for left, middle, _right in three_aps(shell)
                    ),
                    Fraction(),
                )
                if local_mass > local_capacity:
                    raise AssertionError("local pair union exceeds full-edge capacity")

                cross_mass = sum(
                    (pair_weight(pair) for pair in cross_images), Fraction()
                )
                cross_target_mass = sum(
                    (pair_weight(pair) for pair in cross_images.values()), Fraction()
                )
                if cross_mass != cross_target_mass:
                    raise AssertionError("cross-shell edge swap changed pair weight")
                if set(cross_images) & activated:
                    raise AssertionError("cross-shell output overlaps entering pair set")

                groups: dict[
                    tuple[Pair, int, str, Fraction], set[int]
                ] = defaultdict(set)
                roles_by_support: dict[
                    Pair, set[tuple[int, str, Fraction]]
                ] = defaultdict(set)
                for _pair, completion, role, step, coefficient, support in hole_rows:
                    groups[(support, completion, role, coefficient)].add(step)
                    roles_by_support[support].add((completion, role, coefficient))

                reserve = set(activated) | set(cross_images)
                light_supports: set[Pair] = set()
                light_load = Fraction()
                heavy_load = Fraction()
                heavy_role_count = 0

                for support, roles in roles_by_support.items():
                    multiplicity = len(roles)
                    maximum_roles_per_support = max(
                        maximum_roles_per_support, multiplicity
                    )
                    if multiplicity > 6:
                        raise AssertionError("canonical support exceeds six roles")
                    threshold = (
                        Fraction()
                        if support in reserve
                        else pair_weight(support) / multiplicity
                    )
                    for completion, role, coefficient in roles:
                        steps = groups[(support, completion, role, coefficient)]
                        load = coefficient * harmonic(steps)
                        if load <= threshold:
                            light_supports.add(support)
                            light_load += load
                        else:
                            heavy_load += load
                            heavy_role_count += 1

                if light_supports & reserve:
                    raise AssertionError("light support overlaps reserved pair capacity")
                light_capacity = sum(
                    (pair_weight(pair) for pair in light_supports), Fraction()
                )
                if light_load > light_capacity:
                    raise AssertionError("light load exceeds support-pair capacity")

                grouped_hole_mass = sum(
                    (
                        coefficient * harmonic(steps)
                        for (_support, _completion, _role, coefficient), steps
                        in groups.items()
                    ),
                    Fraction(),
                )
                hole_target_mass = sum(
                    (pair_weight(row[0]) for row in hole_rows), Fraction()
                )
                if grouped_hole_mass != hole_target_mass:
                    raise AssertionError("weighted hole-fiber identity failed")

                entering_mass = sum(
                    (pair_weight(pair) for pair in activated), Fraction()
                )
                outgoing_mass = cross_mass + light_capacity
                if entering_mass > local_capacity + outgoing_mass + heavy_load:
                    raise AssertionError("direct maximal pair discharge failed")

                counts["light_support_activations"] += len(light_supports)
                counts["heavy_role_fibers"] += heavy_role_count
                profile_rows.append(
                    (
                        tuple(sorted(parent)),
                        base,
                        tuple(sorted(activated)),
                        tuple(sorted(local)),
                        tuple(sorted(cross_images)),
                        tuple(sorted(light_supports)),
                        str(heavy_load),
                    )
                )

    expected_counts = {
        "activated_families": 1769,
        "activated_pair_occurrences": 4025,
        "cross_pairs": 833,
        "heavy_role_fibers": 573,
        "hole_pairs": 1280,
        "light_support_activations": 633,
        "local_pairs": 1912,
    }
    if dict(sorted(counts.items())) != expected_counts:
        raise AssertionError(f"direct discharge profile changed: {dict(counts)}")

    payload = {
        "schema": "direct_maximal_pair_discharge_small_box_v1",
        "relative_universe": [1, 12],
        "relative_maximal_parents": len(maximal_parents),
        "counts": expected_counts,
        "maximum_roles_per_support_observed": maximum_roles_per_support,
        "profile_sha256": hashlib.sha256(
            json.dumps(profile_rows, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: direct relative-maximal activated-pair discharge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
