#!/usr/bin/env python3
"""Verify one complete simultaneous deletion-DAG resolution of S1.

The schedule is deterministic:

1. enumerate every three-term progression in the current set;
2. choose the lexicographically smallest tuple (step,left,middle,right);
3. delete the left endpoint when v2(step) is even and the right endpoint
   when v2(step) is odd;
4. continue until the residual is three-term-progression-free.

The script exports the exact middle multiplicity fibers, minimum-translation
backbone, standard dyadic shell occurrences, provenance, duplicate groups, and
strict containment relations. It is a finite adapter certificate, not a claim
that this schedule is canonical or extremal.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth, v2


@dataclass(frozen=True)
class SelectedProgression:
    time: int
    sponsor: int
    middle: int
    opposite: int
    step: int
    left: int
    right: int


@dataclass(frozen=True)
class ShellOccurrence:
    index: int
    source: str
    source_step: int | None
    exponent: int
    values: tuple[int, ...]
    provenance: tuple[int, ...]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def harmonic(values: Iterable[int]) -> Fraction:
    return sum(
        (Fraction(1, value) for value in set(values)),
        Fraction(0),
    )


def all_three_aps(values: Iterable[int]) -> list[tuple[int, int, int, int]]:
    ordered = sorted(set(values))
    present = set(ordered)
    progressions: list[tuple[int, int, int, int]] = []
    for left_index, left in enumerate(ordered):
        for middle in ordered[left_index + 1 :]:
            step = middle - left
            right = middle + step
            if right in present:
                progressions.append((step, left, middle, right))
    return sorted(progressions)


def coordinated_sponsor(
    step: int,
    left: int,
    right: int,
) -> tuple[int, int]:
    if v2(step) % 2 == 0:
        return left, right
    return right, left


def resolve_schedule(
    values: Iterable[int],
) -> tuple[tuple[SelectedProgression, ...], frozenset[int]]:
    current = set(values)
    selected: list[SelectedProgression] = []
    while True:
        progressions = all_three_aps(current)
        if not progressions:
            break
        step, left, middle, right = progressions[0]
        sponsor, opposite = coordinated_sponsor(step, left, right)
        if {sponsor, middle, opposite} != {left, middle, right}:
            raise AssertionError("coordinated role did not preserve progression")
        selected.append(
            SelectedProgression(
                time=len(selected) + 1,
                sponsor=sponsor,
                middle=middle,
                opposite=opposite,
                step=step,
                left=left,
                right=right,
            )
        )
        current.remove(sponsor)
    return tuple(selected), frozenset(current)


def verify_dag(
    parent: frozenset[int],
    selected: tuple[SelectedProgression, ...],
    residual: frozenset[int],
) -> None:
    deletion_time = {
        progression.sponsor: progression.time
        for progression in selected
    }
    if len(deletion_time) != len(selected):
        raise AssertionError("a sponsor was deleted more than once")
    if set(deletion_time) | set(residual) != set(parent):
        raise AssertionError("deleted and residual vertices do not partition parent")
    if set(deletion_time) & set(residual):
        raise AssertionError("deleted and residual vertices overlap")

    infinity = len(selected) + 1
    for progression in selected:
        source_time = deletion_time[progression.sponsor]
        for target in (progression.middle, progression.opposite):
            target_time = deletion_time.get(target, infinity)
            if source_time >= target_time:
                raise AssertionError("deletion-DAG edge is not time increasing")


def middle_resolution(
    selected: tuple[SelectedProgression, ...],
) -> tuple[
    frozenset[int],
    dict[int, frozenset[int]],
    dict[int, int],
    dict[tuple[int, int], int],
]:
    centers: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for progression in selected:
        centers[progression.step].append(
            (progression.middle, progression.sponsor)
        )

    terminal_steps: set[int] = set()
    fibers: dict[int, frozenset[int]] = {}
    terminal_sponsor: dict[int, int] = {}
    fiber_provenance: dict[tuple[int, int], int] = {}

    for step in sorted(centers):
        occurrences = sorted(centers[step])
        minimum_center, representative_sponsor = occurrences[0]
        terminal_steps.add(step)
        terminal_sponsor[step] = representative_sponsor
        differences: set[int] = set()
        for center, sponsor in occurrences[1:]:
            difference = center - minimum_center
            if difference <= 0:
                raise AssertionError("middle-fiber difference is not positive")
            if difference in differences:
                raise AssertionError("duplicate middle-fiber difference")
            differences.add(difference)
            fiber_provenance[(step, difference)] = sponsor
        fibers[step] = frozenset(differences)

    if len(terminal_steps) + sum(len(fiber) for fiber in fibers.values()) != len(selected):
        raise AssertionError("middle multiplicity identity failed")
    return (
        frozenset(terminal_steps),
        fibers,
        terminal_sponsor,
        fiber_provenance,
    )


def dyadic_exponent(value: int) -> int:
    if value <= 0:
        raise ValueError("dyadic shell labels must be positive")
    return value.bit_length() - 1


def shell_partition(values: Iterable[int]) -> dict[int, tuple[int, ...]]:
    shells: dict[int, list[int]] = defaultdict(list)
    for value in sorted(set(values)):
        shells[dyadic_exponent(value)].append(value)
    return {
        exponent: tuple(shells[exponent])
        for exponent in sorted(shells)
    }


def build_shell_occurrences(
    parent: frozenset[int],
    fibers: dict[int, frozenset[int]],
    fiber_provenance: dict[tuple[int, int], int],
) -> tuple[ShellOccurrence, ...]:
    minimum = min(parent)
    backbone = {
        value - minimum
        for value in parent
        if value > minimum
    }
    occurrences: list[ShellOccurrence] = []

    for exponent, values in shell_partition(backbone).items():
        provenance = tuple(minimum + value for value in values)
        occurrences.append(
            ShellOccurrence(
                index=len(occurrences),
                source="backbone",
                source_step=None,
                exponent=exponent,
                values=values,
                provenance=provenance,
            )
        )

    for step in sorted(fibers):
        for exponent, values in shell_partition(fibers[step]).items():
            provenance = tuple(
                fiber_provenance[(step, value)]
                for value in values
            )
            occurrences.append(
                ShellOccurrence(
                    index=len(occurrences),
                    source="middle_fiber",
                    source_step=step,
                    exponent=exponent,
                    values=values,
                    provenance=provenance,
                )
            )
    return tuple(occurrences)


def duplicate_groups(
    occurrences: tuple[ShellOccurrence, ...],
) -> tuple[tuple[int, ...], ...]:
    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for occurrence in occurrences:
        groups[occurrence.values].append(occurrence.index)
    return tuple(
        tuple(indices)
        for _, indices in sorted(groups.items())
        if len(indices) > 1
    )


def strict_containments(
    occurrences: tuple[ShellOccurrence, ...],
) -> tuple[tuple[int, int], ...]:
    containments: list[tuple[int, int]] = []
    sets = [set(occurrence.values) for occurrence in occurrences]
    for inner in range(len(occurrences)):
        for outer in range(len(occurrences)):
            if inner == outer:
                continue
            if sets[inner] < sets[outer]:
                containments.append((inner, outer))
    return tuple(sorted(containments))


def occurrence_record(occurrence: ShellOccurrence) -> dict[str, object]:
    return {
        "index": occurrence.index,
        "source": occurrence.source,
        "source_step": occurrence.source_step,
        "shell_exponent": occurrence.exponent,
        "shell_interval": [1 << occurrence.exponent, 1 << (occurrence.exponent + 1)],
        "values": list(occurrence.values),
        "provenance_sponsors_or_parents": list(occurrence.provenance),
        "harmonic_mass": fraction_text(harmonic(occurrence.values)),
    }


def build_payload() -> dict[str, object]:
    state = state_by_depth(1)
    parent = state.values
    selected, residual = resolve_schedule(parent)
    verify_dag(parent, selected, residual)
    if all_three_aps(residual):
        raise AssertionError("residual is not three-term-progression-free")

    terminal_steps, fibers, terminal_sponsor, fiber_provenance = middle_resolution(selected)
    occurrences = build_shell_occurrences(
        parent,
        fibers,
        fiber_provenance,
    )
    duplicates = duplicate_groups(occurrences)
    containments = strict_containments(occurrences)

    minimum = min(parent)
    backbone = frozenset(
        value - minimum
        for value in parent
        if value > minimum
    )
    recursive_occurrence_mass = sum(
        (harmonic(occurrence.values) for occurrence in occurrences),
        Fraction(0),
    )
    recursive_union = frozenset(
        value
        for occurrence in occurrences
        for value in occurrence.values
    )
    recursive_union_mass = harmonic(recursive_union)
    total_occurrence_mass = (
        harmonic(terminal_steps) + recursive_occurrence_mass
    )
    total_distinct_labels = recursive_union | terminal_steps
    total_distinct_mass = harmonic(total_distinct_labels)

    payload: dict[str, object] = {
        "certificate": "S1 deterministic coordinated deletion-DAG adapter",
        "status": "exact finite schedule-specific certificate",
        "schedule_rule": (
            "lexicographically smallest (step,left,middle,right); "
            "left sponsor for even v2(step), right sponsor for odd v2(step)"
        ),
        "parent": {
            "depth": state.depth,
            "scale": state.scale,
            "values": sorted(parent),
            "size": state.size,
        },
        "selected_progressions": [
            {
                "time": progression.time,
                "sponsor": progression.sponsor,
                "middle": progression.middle,
                "opposite": progression.opposite,
                "step": progression.step,
                "ordered_progression": [
                    progression.left,
                    progression.middle,
                    progression.right,
                ],
            }
            for progression in selected
        ],
        "residual": sorted(residual),
        "terminal_steps": sorted(terminal_steps),
        "terminal_step_provenance": {
            str(step): terminal_sponsor[step]
            for step in sorted(terminal_sponsor)
        },
        "middle_fibers": {
            str(step): sorted(fibers[step])
            for step in sorted(fibers)
        },
        "backbone": sorted(backbone),
        "shell_occurrences": [
            occurrence_record(occurrence)
            for occurrence in occurrences
        ],
        "exact_duplicate_groups": [list(group) for group in duplicates],
        "strict_containments": [list(pair) for pair in containments],
        "mass_ledger": {
            "terminal_occurrence_mass": fraction_text(harmonic(terminal_steps)),
            "recursive_occurrence_mass": fraction_text(recursive_occurrence_mass),
            "recursive_distinct_union_mass": fraction_text(recursive_union_mass),
            "recursive_duplicate_mass": fraction_text(
                recursive_occurrence_mass - recursive_union_mass
            ),
            "total_output_occurrence_mass": fraction_text(total_occurrence_mass),
            "total_distinct_label_mass": fraction_text(total_distinct_mass),
            "total_duplicate_mass": fraction_text(
                total_occurrence_mass - total_distinct_mass
            ),
        },
        "interpretation": {
            "simultaneous_recursive_occurrences": len(occurrences),
            "exact_duplicate_classes": len(duplicates),
            "strict_containment_relations": len(containments),
            "all_middle_fibers_contained_in_backbone": all(
                set(fiber) <= set(backbone)
                for fiber in fibers.values()
            ),
            "bellman_row_status": (
                "blocked_pending_overlap_and_retention_convention"
            ),
        },
    }
    verify_expected(payload)
    return payload


def verify_expected(payload: dict[str, object]) -> None:
    selected = payload["selected_progressions"]
    if not isinstance(selected, list) or len(selected) != 6:
        raise AssertionError("unexpected deletion count")
    expected_schedule = [
        (64, 65, 66, 1),
        (80, 81, 82, 1),
        (85, 86, 87, 1),
        (90, 91, 92, 1),
        (81, 86, 91, 5),
        (82, 87, 92, 5),
    ]
    actual_schedule = [
        (
            row["sponsor"],
            row["middle"],
            row["opposite"],
            row["step"],
        )
        for row in selected
    ]
    if actual_schedule != expected_schedule:
        raise AssertionError(f"schedule mismatch: {actual_schedule}")
    if payload["residual"] != [65, 66, 86, 87, 91, 92]:
        raise AssertionError("residual mismatch")
    if payload["terminal_steps"] != [1, 5]:
        raise AssertionError("terminal step mismatch")
    if payload["middle_fibers"] != {"1": [16, 21, 26], "5": [1]}:
        raise AssertionError("middle fiber mismatch")
    if payload["exact_duplicate_groups"] != [[0, 4]]:
        raise AssertionError("duplicate group mismatch")
    if payload["strict_containments"] != [[3, 2]]:
        raise AssertionError("strict containment mismatch")
    mass = payload["mass_ledger"]
    expected_mass = {
        "terminal_occurrence_mass": "6/5",
        "recursive_occurrence_mass": "259811791/84540456",
        "recursive_distinct_union_mass": "46488647/24154416",
        "recursive_duplicate_mass": "5017/4368",
        "total_output_occurrence_mass": "1806301691/422702280",
        "total_distinct_label_mass": "256597651/120772080",
        "total_duplicate_mass": "9385/4368",
    }
    if mass != expected_mass:
        raise AssertionError(f"mass ledger mismatch: {mass}")
    interpretation = payload["interpretation"]
    if not interpretation["all_middle_fibers_contained_in_backbone"]:
        raise AssertionError("middle fibers are not contained in backbone")


def serialize_payload(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_s1_deletion_dag_adapter.py [OUTPUT]")
    payload = build_payload()
    certificate = serialize_payload(payload)
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: complete schedule-specific S1 deletion-DAG adapter")
    print("selected_progressions=6")
    print("residual_size=6")
    print("terminal_steps=1,5")
    print("middle_fiber_1=16,21,26")
    print("middle_fiber_5=1")
    print("simultaneous_recursive_shell_occurrences=5")
    print("all_middle_fibers_contained_in_backbone=true")
    print("recursive_duplicate_mass=5017/4368")
    print("total_duplicate_mass=9385/4368")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
