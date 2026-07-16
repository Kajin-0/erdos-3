#!/usr/bin/env python3
"""Exhaustively verify the completion-step light/heavy transfer on small boxes."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json


def four_ap_witness(values: set[int]) -> tuple[int, int, int, int] | None:
    if not values:
        return None
    lower, upper = min(values), max(values)
    for first in sorted(values):
        for step in range(1, (upper - first) // 3 + 1):
            progression = (
                first,
                first + step,
                first + 2 * step,
                first + 3 * step,
            )
            if all(value in values for value in progression):
                return progression
    return None


def is_four_ap_free(values: set[int]) -> bool:
    return four_ap_witness(values) is None


def hole_witnesses(
    parent: set[int], completion: int
) -> list[tuple[tuple[int, int, int, int], int]]:
    radius = max((abs(value - completion) for value in parent), default=0)
    result: list[tuple[tuple[int, int, int, int], int]] = []
    for missing in range(4):
        for step in range(1, radius + 1):
            first = completion - missing * step
            progression = tuple(first + index * step for index in range(4))
            if all(
                progression[index] in parent
                for index in range(4)
                if index != missing
            ):
                result.append((progression, missing))
    return sorted(result)


def canonical_support(
    witness: tuple[tuple[int, int, int, int], int]
) -> tuple[int, int]:
    progression, missing = witness
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = progression[index], progression[index + 1]
            if pair[1] - pair[0] != progression[1] - progression[0]:
                raise AssertionError("canonical support changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support")


def oriented_fiber(
    parent: set[int], completion: int, orientation: int
) -> set[int]:
    if orientation not in (-1, 1):
        raise ValueError("orientation must be -1 or +1")
    result: set[int] = set()
    if not parent:
        return result
    radius = max(abs(value - completion) for value in parent)
    for step in range(1, radius + 1):
        if (
            completion + orientation * step in parent
            and completion + 2 * orientation * step in parent
        ):
            result.add(step)
    return result


def harmonic_mass(values: set[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def verify_box(lower: int, upper: int) -> dict[str, object]:
    universe = tuple(range(lower, upper + 1))
    stats = Counter()
    maximum_holes_per_support = 0
    maximum_fibers_per_support = 0
    profile_rows: list[tuple[object, ...]] = []

    for mask in range(1 << len(universe)):
        parent = {
            universe[index]
            for index in range(len(universe))
            if (mask >> index) & 1
        }
        if not is_four_ap_free(parent):
            continue
        stats["four_ap_free_parents"] += 1

        holes_by_support: dict[tuple[int, int], list[int]] = defaultdict(list)
        for completion in universe:
            if completion in parent:
                continue
            witnesses = hole_witnesses(parent, completion)
            if not witnesses:
                continue
            stats["certified_same_box_holes"] += 1
            support = canonical_support(witnesses[0])
            holes_by_support[support].append(completion)

        for support, completions in sorted(holes_by_support.items()):
            maximum_holes_per_support = max(
                maximum_holes_per_support, len(completions)
            )
            if len(completions) > 2:
                raise AssertionError("canonical support has more than two holes")

            fibers: list[tuple[int, int, set[int]]] = []
            for completion in sorted(completions):
                for orientation in (-1, 1):
                    steps = oriented_fiber(parent, completion, orientation)
                    if not steps:
                        continue
                    stats["nonempty_oriented_fibers"] += 1
                    if not is_four_ap_free(steps):
                        raise AssertionError(
                            "completion-step fiber contains a four-AP"
                        )
                    for step in steps:
                        target = {
                            completion + orientation * step,
                            completion + 2 * orientation * step,
                        }
                        if not target <= parent:
                            raise AssertionError("fiber target left parent")
                    fibers.append((completion, orientation, steps))

            fiber_count = len(fibers)
            maximum_fibers_per_support = max(
                maximum_fibers_per_support, fiber_count
            )
            if fiber_count > 4:
                raise AssertionError("one support has more than four fibers")
            if not fibers:
                continue

            gap = support[1] - support[0]
            threshold = Fraction(1, fiber_count * gap)
            light_mass = Fraction()
            heavy_mass = Fraction()
            for completion, orientation, steps in fibers:
                mass = harmonic_mass(steps)
                if mass <= threshold:
                    stats["light_fibers"] += 1
                    light_mass += mass
                    kind = "light"
                else:
                    stats["heavy_fibers"] += 1
                    heavy_mass += mass
                    kind = "heavy"
                    if mass <= Fraction(1, 4 * gap):
                        raise AssertionError(
                            "heavy fiber lacks the universal quarter-share bound"
                        )
                profile_rows.append(
                    (
                        tuple(sorted(parent)),
                        support,
                        completion,
                        orientation,
                        tuple(sorted(steps)),
                        kind,
                        f"{mass.numerator}/{mass.denominator}",
                        f"{threshold.numerator}/{threshold.denominator}",
                    )
                )

            if light_mass > Fraction(1, gap):
                raise AssertionError("light fibers exceed support-pair capacity")
            if light_mass:
                stats["supports_with_light_load"] += 1
            if heavy_mass:
                stats["supports_with_heavy_load"] += 1

    payload = {
        "box": [lower, upper],
        "counts": dict(sorted(stats.items())),
        "maximum_holes_per_support": maximum_holes_per_support,
        "maximum_oriented_fibers_per_support": maximum_fibers_per_support,
        "profile_sha256": hashlib.sha256(
            json.dumps(
                profile_rows,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
    }
    return payload


def verify_dyadic_scale() -> dict[str, int]:
    lower, upper = 8, 15
    universe = tuple(range(lower, upper + 1))
    parents = 0
    fibers = 0
    for mask in range(1 << len(universe)):
        parent = {
            universe[index]
            for index in range(len(universe))
            if (mask >> index) & 1
        }
        if not is_four_ap_free(parent):
            continue
        parents += 1
        for completion in universe:
            if completion in parent or not hole_witnesses(parent, completion):
                continue
            for orientation in (-1, 1):
                steps = oriented_fiber(parent, completion, orientation)
                if not steps:
                    continue
                fibers += 1
                if max(steps) >= lower // 2:
                    raise AssertionError("same-shell fiber failed strict scale descent")
                for step in steps:
                    shell_base = 1 << (step.bit_length() - 1)
                    if shell_base > lower // 4:
                        raise AssertionError(
                            "resolved fiber shell did not descend by two levels"
                        )
    return {"dyadic_parents": parents, "dyadic_fibers": fibers}


def main() -> int:
    payload = verify_box(1, 12)
    scale = verify_dyadic_scale()
    payload.update(scale)

    expected_counts = {
        "certified_same_box_holes": 4632,
        "four_ap_free_parents": 2233,
        "heavy_fibers": 3852,
        "light_fibers": 1848,
        "nonempty_oriented_fibers": 5700,
        "supports_with_heavy_load": 2243,
        "supports_with_light_load": 1848,
    }
    if payload["counts"] != expected_counts:
        raise AssertionError(
            f"completion-step count profile changed: {payload['counts']}"
        )
    if payload["maximum_holes_per_support"] != 2:
        raise AssertionError("maximum hole multiplicity changed")
    if payload["maximum_oriented_fibers_per_support"] != 4:
        raise AssertionError("maximum fiber multiplicity changed")
    if scale != {"dyadic_parents": 192, "dyadic_fibers": 234}:
        raise AssertionError(f"dyadic scale profile changed: {scale}")

    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: completion-step fiber light/heavy transfer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
