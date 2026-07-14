#!/usr/bin/env python3
"""Test residual/sponsor splitting of the R4->F5 backbone outputs.

For each recursive parent, lexicographic coordinated deletion partitions the
parent points into:

- a three-AP-free residual Q;
- deleted sponsor points Sigma.

The ordinary minimum backbone translates every parent point except its minimum.
This probe partitions that translated backbone into residual-root and
sponsor-root parts *before* dyadic shelling.  The translated residual-root part
is terminal by translation invariance and heredity of three-AP-freeness.
Middle fibers are unchanged.

No unshifted residual is inserted into the recursive-output family.  Therefore
the split construction preserves exactly the raw numerical support, point
occurrences, and harmonic occurrence mass of the certified baseline transition.
The split raw family is then passed through the same exact-state quotient and
componentwise maximum-harmonic same-shell retention rule.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import sys

from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import (
    DescendantClass,
    DescendantOccurrence,
    components,
    descendant_classes,
    descendant_conflict_graph,
    maximum_weight_independent_set_dp,
    resolve_lexicographic,
    selected_middle_resolution,
    shell_partition,
)
from verify_retained_terminal_split import contains_three_term_ap
from verify_s1_deletion_dag_adapter import harmonic

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)

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
    occurrence_mass = counter_mass(all_resources, union=False)
    union_mass = counter_mass(all_resources, union=True)
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
        "occurrence_resource_mass": serialize_mass(occurrence_mass),
        "union_resource_mass": serialize_mass(union_mass),
        "repeated_resource_mass": serialize_mass(occurrence_mass - union_mass),
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


def retain_occurrences(
    occurrences: tuple[DescendantOccurrence, ...],
) -> tuple[tuple[DescendantClass, ...], dict[str, int]]:
    classes = descendant_classes(occurrences)
    adjacency = descendant_conflict_graph(classes)
    component_family = sorted(
        components(adjacency),
        key=lambda item: (classes[item[0]].representative.exponent, item),
    )

    retained_indices: list[int] = []
    total_dp_states = 0
    nonunique_components = 0
    largest_component = 0
    for component in component_family:
        _weight, count, choice, dp_states = maximum_weight_independent_set_dp(
            component, classes, adjacency
        )
        if count != 1:
            nonunique_components += 1
        retained_indices.extend(choice)
        total_dp_states += dp_states
        largest_component = max(largest_component, len(component))

    retained = tuple(classes[index] for index in sorted(retained_indices))
    retained_union = {value for state in retained for value in state.values}
    if sum(len(state.values) for state in retained) != len(retained_union):
        raise AssertionError("split retained states are not point-disjoint")

    metrics = {
        "raw_occurrences": len(occurrences),
        "raw_occurrence_points": sum(len(item.values) for item in occurrences),
        "exact_state_classes": len(classes),
        "conflict_edges": sum(len(targets) for targets in adjacency.values()) // 2,
        "conflict_components": len(component_family),
        "largest_conflict_component": largest_component,
        "components_with_nonunique_optimum": nonunique_components,
        "dp_states_examined": total_dp_states,
        "retained_states": len(retained),
        "retained_points": len(retained_union),
    }
    return retained, metrics


def build_split_occurrences(
    parents: tuple[DescendantClass, ...],
) -> tuple[DescendantOccurrence, ...]:
    rows: list[
        tuple[
            int,
            str,
            int | None,
            int,
            tuple[int, ...],
            tuple[int, ...],
            tuple[int, ...],
        ]
    ] = []

    for parent in parents:
        values = tuple(parent.values)
        representative = parent.representative
        root_map = dict(zip(values, representative.provenance, strict=True))

        selected, residual_frozen = resolve_lexicographic(frozenset(values))
        residual = set(residual_frozen)
        sponsor_points = {row[0] for row in selected}

        if residual & sponsor_points:
            raise AssertionError("residual/sponsor partition overlaps")
        if residual | sponsor_points != set(values):
            raise AssertionError("residual/sponsor partition is incomplete")
        if contains_three_term_ap(tuple(sorted(residual))):
            raise AssertionError("coordinated residual is not three-AP-free")

        minimum = min(values)
        backbone_by_role: dict[str, dict[int, int]] = {
            "backbone_residual": {},
            "backbone_sponsor": {},
        }
        for point in values:
            if point == minimum:
                continue
            difference = point - minimum
            role = "backbone_residual" if point in residual else "backbone_sponsor"
            backbone_by_role[role][difference] = point

        for role in ("backbone_residual", "backbone_sponsor"):
            difference_to_parent = backbone_by_role[role]
            for exponent, shell_values in shell_partition(
                difference_to_parent
            ).items():
                if role == "backbone_residual" and contains_three_term_ap(shell_values):
                    raise AssertionError(
                        "translated residual backbone shell is not terminal"
                    )
                immediate = tuple(
                    difference_to_parent[value] for value in shell_values
                )
                roots = tuple(root_map[value] for value in immediate)
                rows.append(
                    (
                        parent.index,
                        role,
                        None,
                        exponent,
                        shell_values,
                        roots,
                        immediate,
                    )
                )

        fibers, fiber_provenance = selected_middle_resolution(selected)
        for step in sorted(fibers):
            for exponent, shell_values in shell_partition(fibers[step]).items():
                immediate = tuple(
                    fiber_provenance[(step, value)] for value in shell_values
                )
                if not set(immediate) <= sponsor_points:
                    raise AssertionError("middle fiber contains a non-sponsor point")
                roots = tuple(root_map[value] for value in immediate)
                rows.append(
                    (
                        parent.index,
                        "middle_fiber",
                        step,
                        exponent,
                        shell_values,
                        roots,
                        immediate,
                    )
                )

    return tuple(
        DescendantOccurrence(
            index=index,
            parent_class=row[0],
            source=row[1],
            source_step=row[2],
            exponent=row[3],
            values=row[4],
            provenance=row[5],
            immediate_provenance=row[6],
        )
        for index, row in enumerate(rows)
    )


def support_union(occurrences: tuple[DescendantOccurrence, ...]) -> set[int]:
    return {value for occurrence in occurrences for value in occurrence.values}


def occurrence_harmonic_mass(
    occurrences: tuple[DescendantOccurrence, ...],
) -> Fraction:
    return sum((harmonic(item.values) for item in occurrences), Fraction())


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
    baseline_occurrences, baseline_retained, baseline_metrics, _rows5 = (
        propagate_recursive_states(recursive_fourth)
    )

    split_occurrences = build_split_occurrences(recursive_fourth)
    split_retained, split_metrics = retain_occurrences(split_occurrences)

    baseline_union = support_union(baseline_occurrences)
    split_union = support_union(split_occurrences)
    if baseline_union != split_union:
        raise AssertionError("role split changed the raw numerical support union")

    baseline_points = sum(len(item.values) for item in baseline_occurrences)
    split_points = sum(len(item.values) for item in split_occurrences)
    if baseline_points != split_points:
        raise AssertionError("role split changed raw point-occurrence count")

    baseline_occurrence_mass = occurrence_harmonic_mass(baseline_occurrences)
    split_occurrence_mass = occurrence_harmonic_mass(split_occurrences)
    if baseline_occurrence_mass != split_occurrence_mass:
        raise AssertionError("role split changed raw harmonic occurrence mass")

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
        "schema": "residual_sponsor_backbone_split_probe_v2",
        "scope": "certified_R4_recursive_to_complete_F5_retained_transition",
        "generation_six_propagated": False,
        "unshifted_residual_inserted": False,
        "raw_support_union_preserved": True,
        "raw_point_occurrences_preserved": True,
        "raw_harmonic_occurrence_mass_preserved": True,
        "raw_support_union_size": len(split_union),
        "raw_harmonic_occurrence_mass": serialize_mass(split_occurrence_mass),
        "baseline": {
            "raw_occurrences": len(baseline_occurrences),
            "raw_occurrence_points": baseline_points,
            "retention_metrics": baseline_metrics,
            "profile": baseline_profile,
        },
        "split": {
            "raw_occurrences": len(split_occurrences),
            "raw_occurrence_points": split_points,
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
