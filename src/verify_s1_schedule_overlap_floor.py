#!/usr/bin/env python3
"""Verify the schedule-independent imported-overlap floor on S1.

For each progression-labeled coordinated deletion schedule, form the exact
middle multiplicity fibers Xi_q and the minimum-translation backbone B(S1).
The recursive overlap charge is

    H(B) + sum_q H(Xi_q) - H(B union union_q Xi_q).

The verifier exhausts all schedules and proves that every schedule has charge
at least 1/21.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterator
import hashlib
import sys

from certified_contaminated_states import state_by_depth, v2


State = tuple[int, ...]
Progression = tuple[int, int, int, int, int]
Schedule = tuple[Progression, ...]


EXPECTED_DISTRIBUTION = Counter(
    {
        Fraction(1, 21): 120,
        Fraction(22, 21): 180,
        Fraction(37, 336): 60,
        Fraction(47, 546): 180,
        Fraction(65, 42): 30,
        Fraction(593, 546): 390,
        Fraction(649, 4368): 120,
        Fraction(433, 273): 240,
        Fraction(5017, 4368): 240,
    }
)

EXPECTED_MINIMUM = Fraction(1, 21)
EXPECTED_MAXIMUM = Fraction(433, 273)
EXPECTED_MINIMIZER_COUNT = 120
EXPECTED_MAXIMIZER_COUNT = 240


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def harmonic(values: set[int] | frozenset[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction(0))


def all_three_aps(state: State) -> tuple[tuple[int, int, int, int], ...]:
    values = set(state)
    result: list[tuple[int, int, int, int]] = []
    maximum = state[-1]
    for index, left in enumerate(state):
        for middle in state[index + 1 :]:
            step = middle - left
            right = middle + step
            if right > maximum:
                break
            if right in values:
                result.append((step, left, middle, right))
    return tuple(result)


@lru_cache(maxsize=None)
def transitions(state: State) -> tuple[tuple[Progression, State], ...]:
    result: list[tuple[Progression, State]] = []
    for step, left, middle, right in all_three_aps(state):
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        child = tuple(value for value in state if value != sponsor)
        result.append(
            ((sponsor, middle, opposite, step, left), child)
        )
    return tuple(result)


def enumerate_schedules(
    state: State,
    prefix: Schedule = (),
) -> Iterator[Schedule]:
    available = transitions(state)
    if not available:
        yield prefix
        return
    for progression, child in available:
        yield from enumerate_schedules(child, prefix + (progression,))


def middle_fibers(schedule: Schedule) -> dict[int, frozenset[int]]:
    centers: dict[int, list[int]] = defaultdict(list)
    for _sponsor, middle, _opposite, step, _left in schedule:
        centers[step].append(middle)

    result: dict[int, frozenset[int]] = {}
    for step, values in centers.items():
        minimum = min(values)
        result[step] = frozenset(
            value - minimum
            for value in values
            if value > minimum
        )
    return result


def canonical_schedule_record(schedule: Schedule) -> str:
    return ";".join(
        f"{sponsor},{middle},{opposite},{step}"
        for sponsor, middle, opposite, step, _left in schedule
    )


def build_certificate() -> str:
    parent = state_by_depth(1)
    root = tuple(sorted(parent.values))
    minimum = min(parent.values)
    backbone = frozenset(
        value - minimum
        for value in parent.values
        if value > minimum
    )

    schedules = list(enumerate_schedules(root))
    distribution: Counter[Fraction] = Counter()
    minimizer_records: list[str] = []

    for schedule in schedules:
        fibers = middle_fibers(schedule)
        fiber_sets = [fibers[step] for step in sorted(fibers)]
        fiber_union = (
            frozenset().union(*fiber_sets)
            if fiber_sets
            else frozenset()
        )

        if not fiber_union <= backbone:
            raise AssertionError("fiber union leaves the backbone")

        seen: set[int] = set()
        for fiber in fiber_sets:
            if seen & set(fiber):
                raise AssertionError("middle fibers overlap each other")
            seen.update(fiber)

        occurrence_mass = sum(
            (harmonic(fiber) for fiber in fiber_sets),
            Fraction(0),
        )
        overlap_charge = (
            harmonic(backbone)
            + occurrence_mass
            - harmonic(backbone | fiber_union)
        )

        if overlap_charge != occurrence_mass:
            raise AssertionError("backbone-containment overlap identity failed")

        distribution[overlap_charge] += 1
        if overlap_charge == EXPECTED_MINIMUM:
            minimizer_records.append(canonical_schedule_record(schedule))

    if len(schedules) != 1_560:
        raise AssertionError("schedule count mismatch")
    if distribution != EXPECTED_DISTRIBUTION:
        raise AssertionError("overlap-charge distribution mismatch")

    minimum_charge = min(distribution)
    maximum_charge = max(distribution)
    if minimum_charge != EXPECTED_MINIMUM:
        raise AssertionError("minimum overlap charge mismatch")
    if maximum_charge != EXPECTED_MAXIMUM:
        raise AssertionError("maximum overlap charge mismatch")
    if distribution[minimum_charge] != EXPECTED_MINIMIZER_COUNT:
        raise AssertionError("minimum multiplicity mismatch")
    if distribution[maximum_charge] != EXPECTED_MAXIMIZER_COUNT:
        raise AssertionError("maximum multiplicity mismatch")

    minimizer_payload = "\n".join(sorted(minimizer_records)) + "\n"
    minimizer_sha256 = hashlib.sha256(
        minimizer_payload.encode("utf-8")
    ).hexdigest()

    lines = [
        "verified: exact imported-overlap charge on every coordinated S1 schedule",
        "verified: overlap charge equals middle-fiber occurrence mass",
        f"progression_labeled_schedules={len(schedules)}",
        f"minimum_overlap_charge={fraction_text(minimum_charge)}",
        f"minimum_schedule_count={distribution[minimum_charge]}",
        f"maximum_overlap_charge={fraction_text(maximum_charge)}",
        f"maximum_schedule_count={distribution[maximum_charge]}",
        f"minimum_schedule_catalog_sha256={minimizer_sha256}",
        "overlap_charge_distribution:",
    ]
    for charge, count in sorted(distribution.items()):
        lines.append(f"  {count} {fraction_text(charge)}")
    lines.extend(
        [
            (
                "conclusion: every coordinated deletion schedule on S1 "
                "has imported recursive overlap charge at least 1/21."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_s1_schedule_overlap_floor.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: S1 schedule-independent imported-overlap floor")
    print("minimum_overlap_charge=1/21")
    print("maximum_overlap_charge=433/273")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
