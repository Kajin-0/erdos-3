#!/usr/bin/env python3
"""Test residual/sponsor splitting of the R4->F5 backbone outputs.

For each recursive parent, the coordinated deletion schedule partitions parent
points into:
- a three-AP-free residual Q;
- deleted sponsor points S.

The ordinary minimum backbone translates all parent points except the minimum.
This probe partitions that backbone occurrence into the translated residual
part and translated sponsor part before dyadic shelling.  The residual part is
terminal by translation invariance of three-AP-freeness.  Fibers are unchanged.

The complete split raw family is passed through the same exact-state quotient
and componentwise maximum-harmonic conflict retention as the baseline.  The
probe compares retained terminal/recursive mass and exact pair-resource load.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import sys

from exact_s1_child_ledger import coordinated_schedule, v2
from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from verify_retained_provenance_second_generation import (
    DescendantClass,
    Occurrence,
    dyadic_shells,
    fibers_by_step,
    harmonic,
    retained_children,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Pair = tuple[int, int]


def pair_weight(pair: Pair) -> Fraction:
    left, right = pair
    if not left < right:
        raise AssertionError(f"invalid pair {pair}")
    return Fraction(1, right - left)


def counter_mass(counter: Counter[Pair], *, union: bool) -> Fraction:
    return sum(
        (
            pair_weight(pair) * (1 if union else multiplicity)
            for pair, multiplicity in counter.items()
        ),
        Fraction(),
    )


def affine_reference(state: DescendantClass) -> int:
    values = tuple(state.values)
    roots = tuple(state.representative.provenance)
    if len(set(roots)) != len(roots):
        raise AssertionError(f"state {state.index} repeats roots")
    offsets = {root - value for value, root in zip(values, roots, strict=True)}
    if len(offsets) != 1:
        raise AssertionError(f"state {state.index} is not affine")
    return next(iter(offsets))


def resource_profile(states: tuple[DescendantClass, ...]) -> dict[str, object]:
    current: Counter[Pair] = Counter()
    latent: Counter[Pair] = Counter()
    terminal_states = 0
    recursive_states = 0
    terminal_points = 0
    recursive_points = 0
    terminal_mass = Fraction()
    recursive_mass = Fraction()
    for state in states:
        reference = affine_reference(state)
        roots = tuple(state.representative.provenance)
        terminal = not contains_three_term_ap(state.values)
        for value, root in zip(state.values, roots, strict=True):
            pair = (reference, root)
            if pair_weight(pair) != Fraction(1, value):
                raise AssertionError("current resource weight mismatch")
            current[pair] += 1
        if terminal:
            terminal_states += 1
            terminal_points += len(state.values)
            terminal_mass += state.weight
        else:
            recursive_states += 1
            recursive_points += len(state.values)
            recursive_mass += state.weight
            latent.update(combinations(sorted(roots), 2))
    all_resources = current + latent
    return {
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "terminal_states": terminal_states,
        "terminal_points": terminal_points,
        "recursive_states": recursive_states,
        "recursive_points": recursive_points,
        "terminal_mass": serialize_mass(terminal_mass),
        "recursive_mass": serialize_mass(recursive_mass),
        "total_mass": serialize_mass(terminal_mass + recursive_mass),
        "current_resource_occurrences": sum(current.values()),
        "current_distinct_resources": len(current),
        "latent_resource_occurrences": sum(latent.values()),
        "latent_distinct_resources": len(latent),
        "total_resource_occurrences": sum(all_resources.values()),
        "total_distinct_resources": len(all_resources),
        "maximum_resource_multiplicity": max(all_resources.values(), default=0),
        "repeated_resource_tokens": sum(count > 1 for count in all_resources.values()),
        "occurrence_resource_mass": serialize_mass(
            counter_mass(all_resources, union=False)
        ),
        "union_resource_mass": serialize_mass(
            counter_mass(all_resources, union=True)
        ),
        "repeated_resource_mass": serialize_mass(
            counter_mass(all_resources, union=False)
            - counter_mass(all_resources, union=True)
        ),
        "hashes": {
            "current_resources": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(current.items())]
            ),
            "latent_resources": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(latent.items())]
            ),
            "all_resources": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(all_resources.items())]
            ),
        },
    }


def build_split_occurrences(
    parents: tuple[DescendantClass, ...],
) -> tuple[Occurrence, ...]:
    occurrences: list[Occurrence] = []
    next_index = 0
    for parent in parents:
        values = tuple(parent.values)
        representative = parent.representative
        immediate_map = dict(zip(values, representative.immediate_provenance, strict=True))
        root_map = dict(zip(values, representative.provenance, strict=True))
        schedule = coordinated_schedule(values)
        residual = set(schedule.residual)
        sponsor_points: set[int] = set()
        for action in schedule.actions:
            sponsor_is_right = v2(action.q) % 2 == 0
            for center in action.centers:
                sponsor = center + action.q if sponsor_is_right else center - action.q
                if sponsor not in values:
                    raise AssertionError("schedule sponsor absent from parent")
                if sponsor in sponsor_points:
                    raise AssertionError("sponsor selected more than once")
                sponsor_points.add(sponsor)
        if residual & sponsor_points:
            raise AssertionError("residual/sponsor partition overlaps")
        if residual | sponsor_points != set(values):
            raise AssertionError("residual/sponsor partition is incomplete")
        if contains_three_term_ap(tuple(sorted(residual))):
            raise AssertionError("coordinated residual is not three-AP-free")

        if residual:
            residual_values = tuple(sorted(residual))
            occurrences.append(
                Occurrence(
                    index=next_index,
                    parent_class=parent.index,
                    parent_representative=representative.index,
                    source="terminal_residual",
                    source_step=None,
                    exponent=None,
                    values=residual_values,
                    immediate_provenance=tuple(immediate_map[value] for value in residual_values),
                    provenance=tuple(root_map[value] for value in residual_values),
                    weight=harmonic(residual_values),
                )
            )
            next_index += 1

        minimum = min(values)
        backbone_by_role = {
            "backbone_residual": {},
            "backbone_sponsor": {},
        }
        for point in values:
            if point == minimum:
                continue
            difference = point - minimum
            role = "backbone_residual" if point in residual else "backbone_sponsor"
            backbone_by_role[role][difference] = point

        for role, difference_to_parent in backbone_by_role.items():
            differences = tuple(sorted(difference_to_parent))
            for exponent, shell_values in dyadic_shells(differences):
                if role == "backbone_residual" and contains_three_term_ap(shell_values):
                    raise AssertionError("translated residual backbone shell is not terminal")
                immediate = tuple(difference_to_parent[value] for value in shell_values)
                roots = tuple(root_map[value] for value in immediate)
                occurrences.append(
                    Occurrence(
                        index=next_index,
                        parent_class=parent.index,
                        parent_representative=representative.index,
                        source=role,
                        source_step=None,
                        exponent=exponent,
                        values=shell_values,
                        immediate_provenance=immediate,
                        provenance=roots,
                        weight=harmonic(shell_values),
                    )
                )
                next_index += 1

        fibers = fibers_by_step(schedule)
        for step in sorted(fibers):
            values_by_sponsor = fibers[step]
            sponsor_values = set(values_by_sponsor.values())
            if not sponsor_values <= sponsor_points:
                raise AssertionError("middle fiber contains a non-sponsor root")
            fiber_values = tuple(sorted(values_by_sponsor))
            for exponent, shell_values in dyadic_shells(fiber_values):
                immediate = tuple(values_by_sponsor[value] for value in shell_values)
                roots = tuple(root_map[value] for value in immediate)
                occurrences.append(
                    Occurrence(
                        index=next_index,
                        parent_class=parent.index,
                        parent_representative=representative.index,
                        source="middle_fiber",
                        source_step=step,
                        exponent=exponent,
                        values=shell_values,
                        immediate_provenance=immediate,
                        provenance=roots,
                        weight=harmonic(shell_values),
                    )
                )
                next_index += 1
    return tuple(occurrences)


def support_union(occurrences: tuple[Occurrence, ...]) -> set[int]:
    return {value for occurrence in occurrences for value in occurrence.values}


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    baseline_occurrences, baseline_retained, baseline_metrics, _rows5 = propagate_recursive_states(
        recursive_fourth
    )

    split_occurrences = build_split_occurrences(recursive_fourth)
    split_retained, split_metrics = retained_children(split_occurrences)

    baseline_union = support_union(baseline_occurrences)
    split_union = support_union(split_occurrences)
    if baseline_union != split_union:
        raise AssertionError("role split changed the raw numerical support union")

    baseline_profile = resource_profile(baseline_retained)
    split_profile = resource_profile(split_retained)

    split_source_counts = Counter(
        occurrence.source for occurrence in split_occurrences
    )
    retained_source_counts = Counter(
        state.representative.source for state in split_retained
    )
    residual_backbone_retained = tuple(
        state
        for state in split_retained
        if state.representative.source == "backbone_residual"
    )
    if any(contains_three_term_ap(state.values) for state in residual_backbone_retained):
        raise AssertionError("retained residual-backbone state is recursive")

    output = {
        "schema": "residual_sponsor_backbone_split_probe_v1",
        "scope": "certified_R4_recursive_to_complete_F5_retained_transition",
        "generation_six_propagated": False,
        "raw_support_union_preserved": True,
        "raw_support_union_size": len(split_union),
        "baseline": {
            "raw_occurrences": len(baseline_occurrences),
            "raw_occurrence_points": sum(len(item.values) for item in baseline_occurrences),
            "retention_metrics": baseline_metrics,
            "profile": baseline_profile,
        },
        "split": {
            "raw_occurrences": len(split_occurrences),
            "raw_occurrence_points": sum(len(item.values) for item in split_occurrences),
            "raw_source_counts": dict(sorted(split_source_counts.items())),
            "retention_metrics": split_metrics,
            "retained_source_counts": dict(sorted(retained_source_counts.items())),
            "retained_residual_backbone_states": len(residual_backbone_retained),
            "retained_residual_backbone_points": sum(
                len(state.values) for state in residual_backbone_retained
            ),
            "retained_residual_backbone_mass": serialize_mass(
                sum((state.weight for state in residual_backbone_retained), Fraction())
            ),
            "profile": split_profile,
        },
        "comparison": {
            "total_mass_delta": serialize_mass(
                Fraction(split_profile["total_mass"]["fraction"])
                - Fraction(baseline_profile["total_mass"]["fraction"])
            ),
            "terminal_mass_delta": serialize_mass(
                Fraction(split_profile["terminal_mass"]["fraction"])
                - Fraction(baseline_profile["terminal_mass"]["fraction"])
            ),
            "recursive_mass_delta": serialize_mass(
                Fraction(split_profile["recursive_mass"]["fraction"])
                - Fraction(baseline_profile["recursive_mass"]["fraction"])
            ),
            "recursive_points_delta": (
                split_profile["recursive_points"] - baseline_profile["recursive_points"]
            ),
            "latent_occurrences_delta": (
                split_profile["latent_resource_occurrences"]
                - baseline_profile["latent_resource_occurrences"]
            ),
            "union_resource_mass_delta": serialize_mass(
                Fraction(split_profile["union_resource_mass"]["fraction"])
                - Fraction(baseline_profile["union_resource_mass"]["fraction"])
            ),
            "occurrence_resource_mass_delta": serialize_mass(
                Fraction(split_profile["occurrence_resource_mass"]["fraction"])
                - Fraction(baseline_profile["occurrence_resource_mass"]["fraction"])
            ),
        },
        "hashes": {
            "split_occurrences": canonical_hash(
                [
                    {
                        "parent_class": item.parent_class,
                        "source": item.source,
                        "source_step": item.source_step,
                        "exponent": item.exponent,
                        "values": item.values,
                        "immediate": item.immediate_provenance,
                        "roots": item.provenance,
                    }
                    for item in split_occurrences
                ]
            ),
            "split_retained": canonical_hash(
                [
                    {
                        "values": state.values,
                        "source": state.representative.source,
                        "parent_class": state.representative.parent_class,
                        "immediate": state.representative.immediate_provenance,
                        "roots": state.representative.provenance,
                    }
                    for state in split_retained
                ]
            ),
            "baseline_profile": canonical_hash(baseline_profile),
            "split_profile": canonical_hash(split_profile),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
