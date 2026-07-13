#!/usr/bin/env python3
"""Verify the canonical lexicographic coordinated policy on S1 through S5.

At each state, all three-term progressions are ordered by
(step, left, middle, right). The smallest currently available progression is
selected, and the coordinated side sponsor is deleted. The verifier computes
exact middle fibers, their imported/novel split relative to the fixed
minimum-translation backbone, and compact exact lower bounds for novel
harmonic mass.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import heapq
import sys

from certified_contaminated_states import state_by_depth, v2


EXPECTED = {
    1: {
        "state_size": 12,
        "deletions": 6,
        "residual_size": 6,
        "step_count": 2,
        "fiber_occurrence_cardinality": 4,
        "fiber_union_cardinality": 4,
        "imported_cardinality": 4,
        "novel_cardinality": 0,
        "schedule_sha256": "92a818934083b57e8533e2f84f9d0f62c0babc7c5be78dbf49eac6989750d842",
        "fiber_union_sha256": "15d5b8ff4fe4432b75ba1d5205abbc2ba6bc733729c0a41aa7b8226074a27c76",
        "novel_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "residual_sha256": "d85b4f105baec900f176d4a1d7d0779defd27cd40eb7ca26f8353681f45aa671",
        "novel_lower_bound": Fraction(0),
    },
    2: {
        "state_size": 39,
        "deletions": 26,
        "residual_size": 13,
        "step_count": 5,
        "fiber_occurrence_cardinality": 21,
        "fiber_union_cardinality": 18,
        "imported_cardinality": 10,
        "novel_cardinality": 8,
        "schedule_sha256": "82213485f7b2bd8167e69a9b184b9459ccb151d2b0cba6ba2a9ece8f336aae9c",
        "fiber_union_sha256": "4320283a5a1eeccda038baacdcec627b39237b34bd7d1780961994ae5599e42e",
        "novel_sha256": "50a278a066daaa2e53c4a8b0c11ce265d044d8297b13844d9c43baa709814e4e",
        "residual_sha256": "c429c7eb852865d4039283776cfb8619bbaa92c60b38636ea16e75ff5bd86dbb",
        "novel_lower_bound": Fraction(1193, 1000),
    },
    3: {
        "state_size": 120,
        "deletions": 92,
        "residual_size": 28,
        "step_count": 10,
        "fiber_occurrence_cardinality": 82,
        "fiber_union_cardinality": 59,
        "imported_cardinality": 2,
        "novel_cardinality": 57,
        "schedule_sha256": "05f1b062a2d2be6b76d979b302162b7bb1b19081139fa7ebf4429784254c18b6",
        "fiber_union_sha256": "5b82d2fd2a9550b5cc1cff1af7c4883157f78d764d4fd9bb0adc5706ccf9418f",
        "novel_sha256": "4367b775eec92f8cbabe8102d2954b6d9fed66d663b19eb7957309ed3114e226",
        "residual_sha256": "afa8287fb1d3e82704515692cc2e66dd0219ac7be5dc6ef66ab2d52df8958a96",
        "novel_lower_bound": Fraction(7, 5),
    },
    4: {
        "state_size": 363,
        "deletions": 305,
        "residual_size": 58,
        "step_count": 11,
        "fiber_occurrence_cardinality": 294,
        "fiber_union_cardinality": 206,
        "imported_cardinality": 33,
        "novel_cardinality": 173,
        "schedule_sha256": "03676957d8761f10afd4f65c038b48cd91bd24873c6d1d647ef04612753e22a1",
        "fiber_union_sha256": "9fc0367cdd910a6ed8ce39e0c378a46eaa836aa311f5a5ba88274232f729139c",
        "novel_sha256": "1eb2bf37bdedfc02c87d5a67d234389e8db6c3fe768f7e6514e592373f073524",
        "residual_sha256": "31d49b012e19a7fef09cff858d6f7a1a15c0bc0a00ce783f374030acd493c6ce",
        "novel_lower_bound": Fraction(29, 20),
    },
    5: {
        "state_size": 1092,
        "deletions": 974,
        "residual_size": 118,
        "step_count": 12,
        "fiber_occurrence_cardinality": 962,
        "fiber_union_cardinality": 678,
        "imported_cardinality": 76,
        "novel_cardinality": 602,
        "schedule_sha256": "b88a5f339950492202de02bc3f0c55ecb16378301a7e2aee0e72821b68d8e694",
        "fiber_union_sha256": "749a6cf59176c73be3bdaad9c9a094d83a7ed4f664d8b3e4fb308800d2b802af",
        "novel_sha256": "624f801abcef4310b206057a830dc90c63551f1b8f7b5137b49c0d23ff64121f",
        "residual_sha256": "5eac6b861fd28a3cc6903bcc666c6568730cf89c3d74a7918ec54b25cbd4ab2e",
        "novel_lower_bound": Fraction(149, 100),
    },
}


def canonical_set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonical_schedule_hash(
    schedule: Iterable[tuple[int, int, int, int, int]],
) -> str:
    payload = "\n".join(
        f"{left},{middle},{right},{step},{sponsor}"
        for left, middle, right, step, sponsor in schedule
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def initial_progressions(values: set[int]) -> list[tuple[int, int, int, int]]:
    ordered = sorted(values)
    maximum = ordered[-1]
    result: list[tuple[int, int, int, int]] = []
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            right = middle + step
            if right > maximum:
                break
            if right in values:
                result.append((step, left, middle, right))
    return result


def contains_three_ap(values: set[int]) -> bool:
    return bool(initial_progressions(values))


def harmonic_mass(values: Iterable[int]) -> Fraction:
    return sum((Fraction(1, value) for value in set(values)), Fraction(0))


def run_policy(depth: int) -> dict[str, object]:
    state = state_by_depth(depth)
    working = set(state.values)
    queue = initial_progressions(working)
    heapq.heapify(queue)

    schedule: list[tuple[int, int, int, int, int]] = []
    centers: dict[int, list[int]] = defaultdict(list)

    while queue:
        step, left, middle, right = heapq.heappop(queue)
        if not {left, middle, right} <= working:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        centers[step].append(middle)
        schedule.append((left, middle, right, step, sponsor))
        working.remove(sponsor)

    if contains_three_ap(working):
        raise AssertionError(f"S{depth}: nonterminal residual")

    fibers: dict[int, set[int]] = {}
    for step, values in centers.items():
        minimum = min(values)
        fibers[step] = {
            value - minimum
            for value in values
            if value > minimum
        }

    fiber_union = {
        value
        for fiber in fibers.values()
        for value in fiber
    }
    minimum_state = min(state.values)
    backbone = {
        value - minimum_state
        for value in state.values
        if value > minimum_state
    }
    imported = fiber_union & backbone
    novel = fiber_union - backbone
    occurrence_cardinality = sum(len(fiber) for fiber in fibers.values())

    if len(centers) + occurrence_cardinality != len(schedule):
        raise AssertionError(f"S{depth}: multiplicity identity failed")

    return {
        "state_size": state.size,
        "deletions": len(schedule),
        "residual_size": len(working),
        "step_count": len(centers),
        "fiber_occurrence_cardinality": occurrence_cardinality,
        "fiber_union_cardinality": len(fiber_union),
        "imported_cardinality": len(imported),
        "novel_cardinality": len(novel),
        "novel_harmonic_mass": harmonic_mass(novel),
        "schedule_sha256": canonical_schedule_hash(schedule),
        "fiber_union_sha256": canonical_set_hash(fiber_union),
        "novel_sha256": canonical_set_hash(novel),
        "residual_sha256": canonical_set_hash(working),
    }


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def verify() -> str:
    lines = [
        "verified: canonical lexicographic coordinated policy on S1 through S5",
        "verified: exact middle multiplicity identities",
        "verified: positive novel support on S2 through S5",
    ]

    for depth in range(1, 6):
        actual = run_policy(depth)
        expected = EXPECTED[depth]
        for field, expected_value in expected.items():
            if field == "novel_lower_bound":
                continue
            if actual[field] != expected_value:
                raise AssertionError(
                    f"S{depth}: {field} mismatch: "
                    f"{actual[field]!r} != {expected_value!r}"
                )

        mass = actual["novel_harmonic_mass"]
        lower = expected["novel_lower_bound"]
        if depth == 1:
            if mass != 0:
                raise AssertionError("S1: expected zero novel mass")
        elif not mass > lower:
            raise AssertionError(
                f"S{depth}: novel mass does not exceed {lower}"
            )

        lines.append(
            "S{depth}:state_size={state_size},deletions={deletions},"
            "residual={residual_size},steps={step_count},"
            "fiber_occ={fiber_occurrence_cardinality},"
            "fiber_union={fiber_union_cardinality},"
            "imported={imported_cardinality},novel={novel_cardinality},"
            "novel_mass_lower={lower},schedule_sha256={schedule_sha256},"
            "novel_sha256={novel_sha256}".format(
                depth=depth,
                lower=fraction_text(lower),
                **actual,
            )
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    certificate = verify()
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_lexicographic_novelty_s1_s5.py [certificate-path]"
        )
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")


if __name__ == "__main__":
    main()
