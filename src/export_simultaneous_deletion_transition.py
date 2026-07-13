#!/usr/bin/env python3
"""Export exact raw simultaneous outputs for one coordinated deletion schedule.

The exporter fixes the lexicographic coordinated policy, resolves all terminal
step labels and middle multiplicity fibers, shells every recursive output, and
records point-level provenance plus every exact duplicate, containment, and
partial overlap. The output is the complete raw simultaneous occurrence family
for that schedule. It is not a disjoint retained-child Bellman family.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import argparse
import hashlib
import heapq
import json
import sys

from certified_contaminated_states import state_by_depth, v2
from verify_s1_deletion_dag_adapter import (
    SelectedProgression,
    ShellOccurrence,
    all_three_aps,
    build_shell_occurrences,
    duplicate_groups,
    fraction_text,
    harmonic,
    middle_resolution,
    strict_containments,
)


EXPECTED = {
    1: (
        "98d55ecdbbf94402eee1b82a2437d531fd2ad2d933924597d79a7266a4ac73ae",
        6, 6, 2, 5, 4, 1, 1, 0, [1],
        "0", "5017/4368", "0",
    ),
    2: (
        "8cc11f1cdff33b6b8756d33b97fc6b550159e9ffc9fda5032e35f3195b739b4e",
        26, 13, 5, 11, 10, 1, 3, 5, [1, 61],
        "383/10614",
        "218348937262/1897648393355",
        "239396453/200655312",
    ),
    3: (
        "7bd2e36bb5f1ee4485739b910b3e804fb311da2019d54e09dfdc91df899c75c7",
        92, 28, 10, 25, 21, 3, 23, 15, [1, 61, 303],
        "741175084808507/5412538546014600",
        "1/202",
        (
            "263794861279616516530714602143928959351406948378652487/"
            "188399844058271400580736246041286596162958326209093600"
        ),
    ),
}

CERTIFICATE_SHA256 = (
    "e8162ee59d496bec8fe2d4103edc8f79de9fbd42444ef37f41fc317aec13a14b"
)


def canonical_set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def resolve_schedule(
    values: Iterable[int],
) -> tuple[tuple[SelectedProgression, ...], frozenset[int]]:
    """Resolve the lexicographic policy using one initial AP heap.

    Deletion cannot create a new progression, so stale heap entries are simply
    discarded. This is equivalent to re-enumerating the current state at every
    step but scales to the recorded S3 reference.
    """

    current = set(values)
    queue = all_three_aps(current)
    heapq.heapify(queue)
    selected: list[SelectedProgression] = []

    while queue:
        step, left, middle, right = heapq.heappop(queue)
        if not {left, middle, right} <= current:
            continue
        if v2(step) % 2 == 0:
            sponsor, opposite = left, right
        else:
            sponsor, opposite = right, left
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


def verify_schedule(
    parent: frozenset[int],
    selected: tuple[SelectedProgression, ...],
    residual: frozenset[int],
) -> None:
    working = set(parent)
    deletion_time: dict[int, int] = {}

    for progression in selected:
        if not {
            progression.left,
            progression.middle,
            progression.right,
        } <= working:
            raise AssertionError("selected progression is unavailable")
        if progression.middle - progression.left != progression.step:
            raise AssertionError("left difference mismatch")
        if progression.right - progression.middle != progression.step:
            raise AssertionError("right difference mismatch")
        expected = (
            progression.left
            if v2(progression.step) % 2 == 0
            else progression.right
        )
        if progression.sponsor != expected:
            raise AssertionError("coordinated sponsor mismatch")
        deletion_time[progression.sponsor] = progression.time
        working.remove(progression.sponsor)

    if frozenset(working) != residual:
        raise AssertionError("residual mismatch")
    if all_three_aps(residual):
        raise AssertionError("terminal residual contains a three-term AP")

    infinity = len(selected) + 1
    for progression in selected:
        source_time = deletion_time[progression.sponsor]
        for target in (progression.middle, progression.opposite):
            if source_time >= deletion_time.get(target, infinity):
                raise AssertionError("deletion-DAG edge is not time increasing")


def schedule_hash(
    selected: tuple[SelectedProgression, ...],
    residual: frozenset[int],
) -> str:
    record = {
        "selected": [
            [
                progression.sponsor,
                progression.middle,
                progression.opposite,
                progression.step,
                progression.left,
                progression.right,
            ]
            for progression in selected
        ],
        "residual": sorted(residual),
    }
    payload = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def partial_overlaps(
    occurrences: tuple[ShellOccurrence, ...],
) -> list[tuple[int, int, tuple[int, ...]]]:
    sets = [set(occurrence.values) for occurrence in occurrences]
    result: list[tuple[int, int, tuple[int, ...]]] = []

    for left in range(len(sets)):
        for right in range(left + 1, len(sets)):
            intersection = sets[left] & sets[right]
            if not intersection:
                continue
            if sets[left] <= sets[right] or sets[right] <= sets[left]:
                continue
            result.append(
                (left, right, tuple(sorted(intersection)))
            )
    return sorted(result)


def occurrence_record(occurrence: ShellOccurrence) -> dict[str, object]:
    return {
        "index": occurrence.index,
        "source": occurrence.source,
        "source_step": occurrence.source_step,
        "shell_exponent": occurrence.exponent,
        "shell_scale": 1 << occurrence.exponent,
        "values": list(occurrence.values),
        "provenance_origins": list(occurrence.provenance),
        "harmonic_mass": fraction_text(harmonic(occurrence.values)),
        "state_sha256": canonical_set_hash(occurrence.values),
    }


def build_payload(depth: int) -> dict[str, object]:
    state = state_by_depth(depth)
    parent = state.values
    selected, residual = resolve_schedule(parent)
    verify_schedule(parent, selected, residual)

    (
        terminal_steps,
        fibers,
        terminal_sponsor,
        fiber_provenance,
    ) = middle_resolution(selected)
    occurrences = build_shell_occurrences(
        parent,
        fibers,
        fiber_provenance,
    )
    duplicates = duplicate_groups(occurrences)
    containments = sorted(strict_containments(occurrences))
    partial = partial_overlaps(occurrences)

    minimum = min(parent)
    backbone = frozenset(
        value - minimum
        for value in parent
        if value > minimum
    )
    middle_union = frozenset(
        value
        for fiber in fibers.values()
        for value in fiber
    )
    imported = middle_union & backbone
    novel = middle_union - backbone
    recursive_union = frozenset(
        value
        for occurrence in occurrences
        for value in occurrence.values
    )

    middle_occurrence_mass = sum(
        (harmonic(fiber) for fiber in fibers.values()),
        Fraction(0),
    )
    recursive_occurrence_mass = sum(
        (harmonic(occurrence.values) for occurrence in occurrences),
        Fraction(0),
    )
    terminal_mass = harmonic(terminal_steps)

    point_provenance: dict[int, list[dict[str, object]]] = defaultdict(list)
    exact_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for occurrence in occurrences:
        exact_groups[occurrence.values].append(occurrence.index)
        for value, origin in zip(
            occurrence.values,
            occurrence.provenance,
        ):
            point_provenance[value].append(
                {
                    "occurrence": occurrence.index,
                    "source": occurrence.source,
                    "source_step": occurrence.source_step,
                    "origin": origin,
                }
            )

    exact_classes = [
        {
            "representative": indices[0],
            "members": indices,
            "multiplicity": len(indices),
            "values": list(values),
            "state_sha256": canonical_set_hash(values),
        }
        for values, indices in sorted(exact_groups.items())
    ]

    total_labels = set(terminal_steps) | set(recursive_union)
    return {
        "schema": "simultaneous_deletion_transition/v1",
        "semantics": (
            "one_complete_schedule_specific_simultaneous_output_family_"
            "before_retention_quotient"
        ),
        "policy": (
            "lexicographically_smallest_step_left_middle_right_"
            "coordinated_side_sponsor"
        ),
        "parent": {
            "depth": state.depth,
            "scale": state.scale,
            "size": state.size,
            "maximum": state.maximum,
            "values": sorted(parent),
            "state_sha256": canonical_set_hash(parent),
        },
        "schedule": {
            "selected_count": len(selected),
            "schedule_sha256": schedule_hash(selected, residual),
            "selected": [
                {
                    "time": progression.time,
                    "step": progression.step,
                    "left": progression.left,
                    "middle": progression.middle,
                    "right": progression.right,
                    "sponsor": progression.sponsor,
                    "opposite": progression.opposite,
                }
                for progression in selected
            ],
            "residual": sorted(residual),
            "residual_sha256": canonical_set_hash(residual),
        },
        "terminal_outputs": {
            "steps": sorted(terminal_steps),
            "provenance_sponsor": {
                str(step): terminal_sponsor[step]
                for step in sorted(terminal_sponsor)
            },
            "harmonic_mass": fraction_text(terminal_mass),
        },
        "backbone": {
            "values": sorted(backbone),
            "state_sha256": canonical_set_hash(backbone),
            "harmonic_mass": fraction_text(harmonic(backbone)),
        },
        "middle_fibers": {
            str(step): {
                "values": sorted(fibers[step]),
                "state_sha256": canonical_set_hash(fibers[step]),
                "harmonic_mass": fraction_text(harmonic(fibers[step])),
            }
            for step in sorted(fibers)
        },
        "recursive_shell_occurrences": [
            occurrence_record(occurrence)
            for occurrence in occurrences
        ],
        "exact_state_classes": exact_classes,
        "exact_duplicate_groups": [
            list(group)
            for group in duplicates
        ],
        "strict_containments": [
            {"inner": inner, "outer": outer}
            for inner, outer in containments
        ],
        "partial_overlaps": [
            {
                "left": left,
                "right": right,
                "values": list(values),
                "harmonic_mass": fraction_text(harmonic(values)),
            }
            for left, right, values in partial
        ],
        "recursive_label_provenance": {
            str(value): point_provenance[value]
            for value in sorted(point_provenance)
        },
        "terminal_recursive_overlap": sorted(
            set(terminal_steps) & set(recursive_union)
        ),
        "mass_ledger": {
            "middle_fiber_occurrence_mass": fraction_text(
                middle_occurrence_mass
            ),
            "middle_fiber_distinct_union_mass": fraction_text(
                harmonic(middle_union)
            ),
            "middle_fiber_internal_duplicate_mass": fraction_text(
                middle_occurrence_mass - harmonic(middle_union)
            ),
            "middle_fiber_imported_distinct_mass": fraction_text(
                harmonic(imported)
            ),
            "middle_fiber_novel_distinct_mass": fraction_text(
                harmonic(novel)
            ),
            "recursive_shell_occurrence_mass": fraction_text(
                recursive_occurrence_mass
            ),
            "recursive_distinct_union_mass": fraction_text(
                harmonic(recursive_union)
            ),
            "recursive_duplicate_mass": fraction_text(
                recursive_occurrence_mass - harmonic(recursive_union)
            ),
            "terminal_occurrence_mass": fraction_text(terminal_mass),
            "total_output_occurrence_mass": fraction_text(
                terminal_mass + recursive_occurrence_mass
            ),
            "total_distinct_label_mass": fraction_text(
                harmonic(total_labels)
            ),
            "total_duplicate_mass": fraction_text(
                terminal_mass
                + recursive_occurrence_mass
                - harmonic(total_labels)
            ),
        },
        "interpretation": {
            "complete_for_fixed_policy": True,
            "raw_simultaneous_recursive_occurrences": len(occurrences),
            "exact_state_classes": len(exact_classes),
            "exact_duplicate_classes": len(duplicates),
            "strict_containment_relations": len(containments),
            "partial_overlap_relations": len(partial),
            "retention_quotient_applied": False,
            "bellman_row_status": (
                "blocked_until_retention_and_bounded_overlap_rule_"
                "is_supplied"
            ),
        },
    }


def serialize_payload(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def payload_digest(payload: dict[str, object]) -> str:
    return hashlib.sha256(
        serialize_payload(payload).encode("utf-8")
    ).hexdigest()


def expected_record(depth: int) -> dict[str, object]:
    (
        digest,
        selected,
        residual,
        terminal_steps,
        occurrences,
        classes,
        duplicate_classes,
        containments,
        partial,
        terminal_overlap,
        internal_duplicate_mass,
        imported_mass,
        novel_mass,
    ) = EXPECTED[depth]
    return {
        "payload_sha256": digest,
        "selected": selected,
        "residual": residual,
        "terminal_steps": terminal_steps,
        "recursive_occurrences": occurrences,
        "exact_state_classes": classes,
        "exact_duplicate_classes": duplicate_classes,
        "strict_containments": containments,
        "partial_overlaps": partial,
        "terminal_recursive_overlap": terminal_overlap,
        "middle_internal_duplicate_mass": internal_duplicate_mass,
        "middle_imported_distinct_mass": imported_mass,
        "middle_novel_distinct_mass": novel_mass,
    }


def verify_expected(depth: int, payload: dict[str, object]) -> None:
    interpretation = payload["interpretation"]
    mass = payload["mass_ledger"]
    schedule = payload["schedule"]
    terminal = payload["terminal_outputs"]
    actual = {
        "payload_sha256": payload_digest(payload),
        "selected": schedule["selected_count"],
        "residual": len(schedule["residual"]),
        "terminal_steps": len(terminal["steps"]),
        "recursive_occurrences": (
            interpretation["raw_simultaneous_recursive_occurrences"]
        ),
        "exact_state_classes": interpretation["exact_state_classes"],
        "exact_duplicate_classes": (
            interpretation["exact_duplicate_classes"]
        ),
        "strict_containments": (
            interpretation["strict_containment_relations"]
        ),
        "partial_overlaps": interpretation["partial_overlap_relations"],
        "terminal_recursive_overlap": (
            payload["terminal_recursive_overlap"]
        ),
        "middle_internal_duplicate_mass": (
            mass["middle_fiber_internal_duplicate_mass"]
        ),
        "middle_imported_distinct_mass": (
            mass["middle_fiber_imported_distinct_mass"]
        ),
        "middle_novel_distinct_mass": (
            mass["middle_fiber_novel_distinct_mass"]
        ),
    }
    expected = expected_record(depth)
    if actual != expected:
        raise AssertionError(
            f"S{depth} transition mismatch:\n"
            f"actual={actual!r}\nexpected={expected!r}"
        )


def build_certificate() -> str:
    lines = [
        "SIMULTANEOUS DELETION TRANSITION EXPORTER",
        "",
        "schema=simultaneous_deletion_transition/v1",
        (
            "semantics=one_complete_schedule_specific_simultaneous_"
            "output_family_before_retention_quotient"
        ),
        (
            "policy=lexicographically_smallest_step_left_middle_right_"
            "coordinated_side_sponsor"
        ),
        "verified_depths=1,2,3",
    ]

    for depth in (1, 2, 3):
        payload = build_payload(depth)
        verify_expected(depth, payload)
        record = expected_record(depth)
        lines.extend(
            [
                f"S{depth}_selected={record['selected']}",
                f"S{depth}_residual={record['residual']}",
                f"S{depth}_terminal_steps={record['terminal_steps']}",
                (
                    f"S{depth}_recursive_occurrences="
                    f"{record['recursive_occurrences']}"
                ),
                (
                    f"S{depth}_exact_state_classes="
                    f"{record['exact_state_classes']}"
                ),
                (
                    f"S{depth}_exact_duplicate_classes="
                    f"{record['exact_duplicate_classes']}"
                ),
                (
                    f"S{depth}_strict_containments="
                    f"{record['strict_containments']}"
                ),
                (
                    f"S{depth}_partial_overlaps="
                    f"{record['partial_overlaps']}"
                ),
                (
                    f"S{depth}_terminal_recursive_overlap="
                    + ",".join(
                        str(value)
                        for value in record[
                            "terminal_recursive_overlap"
                        ]
                    )
                ),
                (
                    f"S{depth}_middle_internal_duplicate_mass="
                    f"{record['middle_internal_duplicate_mass']}"
                ),
                (
                    f"S{depth}_middle_imported_distinct_mass="
                    f"{record['middle_imported_distinct_mass']}"
                ),
                (
                    f"S{depth}_middle_novel_distinct_mass="
                    f"{record['middle_novel_distinct_mass']}"
                ),
                (
                    f"S{depth}_payload_sha256="
                    f"{record['payload_sha256']}"
                ),
            ]
        )

    lines.extend(
        [
            "",
            (
                "conclusion: the exporter records the complete raw "
                "simultaneous output family"
            ),
            (
                "for one fixed coordinated schedule, including shell "
                "resolution, point-level"
            ),
            (
                "provenance, exact duplicates, strict containments, "
                "and partial overlaps."
            ),
            "No retention quotient or Bellman child sum is inferred.",
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(
            f"certificate SHA-256 mismatch: {digest}"
        )
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    test_parser = subparsers.add_parser("self-test")
    test_parser.add_argument("output", nargs="?", type=Path)

    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--state-depth", type=int, required=True)
    export_parser.add_argument("--output", type=Path)

    args = parser.parse_args()
    if args.command == "self-test":
        certificate = build_certificate()
        if args.output is not None:
            args.output.write_text(certificate, encoding="utf-8")
        print(certificate, end="")
        return 0

    payload = build_payload(args.state_depth)
    serialized = serialize_payload(payload)
    if args.output is None:
        sys.stdout.write(serialized)
    else:
        args.output.write_text(serialized, encoding="utf-8")
        print(
            "recursive_occurrences="
            f"{payload['interpretation']['raw_simultaneous_recursive_occurrences']}"
        )
        print(f"payload_sha256={payload_digest(payload)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
