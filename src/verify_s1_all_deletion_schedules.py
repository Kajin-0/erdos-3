#!/usr/bin/env python3
"""Exhaust every coordinated side-anchor deletion schedule on S1.

A schedule is progression-labeled: when two selected three-term progressions
delete the same sponsor and lead to the same next vertex set, they remain two
distinct schedules because their middle-step outputs differ.

For each current set, every available three-term progression is permitted. The
coordinated sponsor is the left endpoint when v2(step) is even and the right
endpoint when v2(step) is odd. Enumeration stops at a three-term-progression-
free residual.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterator
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from verify_s1_deletion_dag_adapter import (
    SelectedProgression,
    all_three_aps,
    coordinated_sponsor,
    harmonic,
    middle_resolution,
)


State = tuple[int, ...]
Schedule = tuple[SelectedProgression, ...]


@dataclass(frozen=True)
class Transition:
    progression: SelectedProgression
    child: State


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


@lru_cache(maxsize=None)
def transitions(state: State) -> tuple[Transition, ...]:
    result: list[Transition] = []
    for step, left, middle, right in all_three_aps(state):
        sponsor, opposite = coordinated_sponsor(step, left, right)
        child = tuple(value for value in state if value != sponsor)
        result.append(
            Transition(
                progression=SelectedProgression(
                    time=0,
                    sponsor=sponsor,
                    middle=middle,
                    opposite=opposite,
                    step=step,
                    left=left,
                    right=right,
                ),
                child=child,
            )
        )
    return tuple(result)


def enumerate_schedules(
    state: State,
    prefix: Schedule = (),
) -> Iterator[tuple[Schedule, State]]:
    available = transitions(state)
    if not available:
        yield prefix, state
        return
    for transition in available:
        progression = transition.progression
        timed = SelectedProgression(
            time=len(prefix) + 1,
            sponsor=progression.sponsor,
            middle=progression.middle,
            opposite=progression.opposite,
            step=progression.step,
            left=progression.left,
            right=progression.right,
        )
        yield from enumerate_schedules(
            transition.child,
            prefix + (timed,),
        )


def collect_reachable_states(root: State) -> frozenset[State]:
    seen: set[State] = set()

    def visit(state: State) -> None:
        if state in seen:
            return
        seen.add(state)
        for transition in transitions(state):
            visit(transition.child)

    visit(root)
    return frozenset(seen)


def canonical_schedule_hash(
    schedules: list[tuple[Schedule, State]],
) -> str:
    records = []
    for schedule, residual in schedules:
        records.append(
            {
                "selected": [
                    [
                        progression.sponsor,
                        progression.middle,
                        progression.opposite,
                        progression.step,
                    ]
                    for progression in schedule
                ],
                "residual": list(residual),
            }
        )
    records.sort(key=lambda record: (record["selected"], record["residual"]))
    payload = "\n".join(
        json.dumps(record, sort_keys=True, separators=(",", ":"))
        for record in records
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonical_state_hash(states: frozenset[State]) -> str:
    payload = "\n".join(
        ",".join(str(value) for value in state)
        for state in sorted(states)
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def profile_key(values: frozenset[int]) -> str:
    return ",".join(str(value) for value in sorted(values)) or "empty"


def build_certificate() -> str:
    parent = state_by_depth(1)
    root = tuple(sorted(parent.values))
    backbone = frozenset(
        value - min(parent.values)
        for value in parent.values
        if value > min(parent.values)
    )

    reachable = collect_reachable_states(root)
    schedules = list(enumerate_schedules(root))

    schedule_lengths: Counter[int] = Counter()
    residual_profiles: Counter[frozenset[int]] = Counter()
    terminal_profiles: Counter[frozenset[int]] = Counter()
    fiber_union_profiles: Counter[frozenset[int]] = Counter()
    sponsor_sequences: Counter[tuple[int, ...]] = Counter()

    all_fibers_pairwise_disjoint = True
    all_fiber_unions_in_backbone = True
    maximum_novel_fiber_mass = Fraction(0)

    for schedule, residual_state in schedules:
        residual = frozenset(residual_state)
        if all_three_aps(residual):
            raise AssertionError("terminal residual still contains a 3-AP")

        schedule_lengths[len(schedule)] += 1
        residual_profiles[residual] += 1
        sponsor_sequences[
            tuple(progression.sponsor for progression in schedule)
        ] += 1

        terminal_steps, fibers, _, _ = middle_resolution(schedule)
        terminal_profiles[terminal_steps] += 1

        fiber_union: set[int] = set()
        for step in sorted(fibers):
            fiber = set(fibers[step])
            if fiber_union & fiber:
                all_fibers_pairwise_disjoint = False
            fiber_union.update(fiber)
        frozen_union = frozenset(fiber_union)
        fiber_union_profiles[frozen_union] += 1

        novel = frozen_union - backbone
        novel_mass = harmonic(novel)
        maximum_novel_fiber_mass = max(
            maximum_novel_fiber_mass,
            novel_mass,
        )
        if novel:
            all_fiber_unions_in_backbone = False

    sponsor_multiplicity = Counter(sponsor_sequences.values())

    expected_schedule_lengths = Counter({5: 240, 6: 1320})
    expected_terminal_profiles = Counter(
        {
            frozenset({1, 5}): 480,
            frozenset({1, 4, 5}): 240,
            frozenset({1, 5, 6}): 420,
            frozenset({1, 4, 5, 6}): 420,
        }
    )
    expected_fiber_unions = Counter(
        {
            frozenset({21}): 120,
            frozenset({1, 21}): 180,
            frozenset({16, 21}): 60,
            frozenset({21, 26}): 180,
            frozenset({1, 2, 21}): 30,
            frozenset({1, 21, 26}): 390,
            frozenset({16, 21, 26}): 120,
            frozenset({1, 2, 21, 26}): 240,
            frozenset({1, 16, 21, 26}): 240,
        }
    )
    expected_residuals = Counter(
        {
            frozenset({65, 66, 86, 87, 90, 91}): 210,
            frozenset({65, 66, 82, 86, 87, 91}): 30,
            frozenset({65, 66, 80, 86, 87, 90, 91}): 180,
            frozenset({65, 66, 86, 87, 91, 92}): 720,
            frozenset({65, 66, 80, 86, 87, 91}): 360,
            frozenset({65, 66, 80, 82, 86, 87, 91}): 60,
        }
    )

    if len(reachable) != 120:
        raise AssertionError("reachable-state count mismatch")
    if len(schedules) != 1_560:
        raise AssertionError("schedule count mismatch")
    if len(sponsor_sequences) != 930:
        raise AssertionError("sponsor-sequence count mismatch")
    if sponsor_multiplicity != Counter({1: 444, 2: 414, 4: 72}):
        raise AssertionError("sponsor-sequence multiplicity mismatch")
    if schedule_lengths != expected_schedule_lengths:
        raise AssertionError("schedule-length distribution mismatch")
    if residual_profiles != expected_residuals:
        raise AssertionError("residual profile mismatch")
    if terminal_profiles != expected_terminal_profiles:
        raise AssertionError("terminal-step profile mismatch")
    if fiber_union_profiles != expected_fiber_unions:
        raise AssertionError("fiber-union profile mismatch")
    if not all_fibers_pairwise_disjoint:
        raise AssertionError("some middle fibers overlap each other")
    if not all_fiber_unions_in_backbone:
        raise AssertionError("some middle fiber leaves the backbone")
    if maximum_novel_fiber_mass != 0:
        raise AssertionError("novel middle-fiber mass is nonzero")

    state_hash = canonical_state_hash(reachable)
    schedule_hash = canonical_schedule_hash(schedules)
    if state_hash != "7c96b7e498353a08899a62e4c6a977b604934ae0a08b6deb0f771f4eafb77ec5":
        raise AssertionError("reachable-state catalog hash mismatch")
    if schedule_hash != "bbdc46cbe4d2bae61cc942c139beab4fe2872e66ce7e97cd0072241a66c6c05d":
        raise AssertionError("schedule catalog hash mismatch")

    lines = [
        "S1 ALL COORDINATED DELETION SCHEDULES",
        "",
        "schedule_semantics=progression_labeled",
        "coordinated_rule=left_if_v2_even_right_if_v2_odd",
        f"reachable_states={len(reachable)}",
        f"terminal_residuals={len(residual_profiles)}",
        f"progression_labeled_schedules={len(schedules)}",
        f"distinct_sponsor_sequences={len(sponsor_sequences)}",
        "sponsor_sequence_multiplicity_1=444",
        "sponsor_sequence_multiplicity_2=414",
        "sponsor_sequence_multiplicity_4=72",
        "schedule_length_5=240",
        "schedule_length_6=1320",
        "all_middle_fibers_pairwise_disjoint=true",
        "all_middle_fiber_unions_contained_in_backbone=true",
        "maximum_novel_fiber_mass=0",
        "backbone=" + profile_key(backbone),
        f"reachable_state_catalog_sha256={state_hash}",
        f"schedule_catalog_sha256={schedule_hash}",
        "",
        "terminal_step_profiles:",
    ]
    for profile, count in sorted(
        terminal_profiles.items(),
        key=lambda item: (len(item[0]), sorted(item[0])),
    ):
        lines.append(f"  {count} {profile_key(profile)}")

    lines.append("fiber_union_profiles:")
    for profile, count in sorted(
        fiber_union_profiles.items(),
        key=lambda item: (len(item[0]), sorted(item[0])),
    ):
        lines.append(
            f"  {count} {profile_key(profile)} "
            f"H={fraction_text(harmonic(profile))}"
        )

    lines.append("residual_profiles:")
    for profile, count in sorted(
        residual_profiles.items(),
        key=lambda item: (len(item[0]), sorted(item[0])),
    ):
        lines.append(f"  {count} {profile_key(profile)}")

    lines.extend(
        [
            "",
            (
                "conclusion: every coordinated deletion schedule on S1 "
                "has zero middle-fiber support outside the "
                "minimum-translation backbone."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_s1_all_deletion_schedules.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: all coordinated S1 deletion schedules")
    print("reachable_states=120")
    print("progression_labeled_schedules=1560")
    print("distinct_sponsor_sequences=930")
    print("all_middle_fiber_unions_contained_in_backbone=true")
    print("maximum_novel_fiber_mass=0")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
