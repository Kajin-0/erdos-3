#!/usr/bin/env python3
"""Measure sponsor-core activation on the four certified retained transitions.

The residual/sponsor backbone theorem reduces the recursively active root universe
of an affine parent to the roots deleted as sponsors by coordinated deletion.  For
an ordered sponsor set Sigma and parent minimum root a, the available continuing
pair universe is

    {(a,s): s in Sigma, s != a} union binom(Sigma, 2).

This probe applies the exact split to R1->F2 through R4->F5, reruns the same
maximum-harmonic retained quotient, and measures:

- available sponsor-core pair energy;
- recursively activated current-plus-latent pair energy;
- direct selected-progression edge energy;
- weighted selected-step incidence sum 1/q;
- exact pair ownership by the first deleted sponsor;
- the dyadic distance/selected-step profile of activated pairs;
- baseline versus refined terminal and recursive frontiers.

No sixth generation is constructed.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import sys

from probe_residual_sponsor_backbone_split import (
    affine_reference,
    build_split_occurrences,
    occurrence_harmonic_mass,
    resource_profile,
    retain_occurrences,
    support_union,
)
from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import resolve_lexicographic
from verify_retained_terminal_split import contains_three_term_ap
from verify_s1_deletion_dag_adapter import harmonic

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)

Pair = tuple[int, int]


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError(f"degenerate pair ({left},{right})")
    return (left, right) if left < right else (right, left)


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


def ratio_record(numerator: Fraction, denominator: Fraction) -> dict[str, str] | None:
    if denominator == 0:
        return None
    return serialize_mass(numerator / denominator)


def signed_floor_log2_ratio(numerator: int, denominator: int) -> int:
    """Return floor(log2(numerator/denominator)) using integer arithmetic."""
    if numerator <= 0 or denominator <= 0:
        raise ValueError("ratio inputs must be positive")
    if numerator >= denominator:
        return (numerator // denominator).bit_length() - 1
    ceiling = (denominator + numerator - 1) // numerator
    return -(ceiling - 1).bit_length()


def state_signature(states: tuple[object, ...]) -> str:
    rows = [
        {
            "index": state.index,
            "values": list(state.values),
            "parent": state.representative.parent_class,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "provenance": list(state.representative.provenance),
            "immediate": list(state.representative.immediate_provenance),
        }
        for state in states
    ]
    return canonical_hash(rows)


def recursive_states(states: tuple[object, ...]) -> tuple[object, ...]:
    return tuple(state for state in states if contains_three_term_ap(state.values))


def schedule_data(state: object) -> dict[str, object]:
    values = tuple(state.values)
    roots = tuple(state.representative.provenance)
    reference = affine_reference(state)
    root_map = dict(zip(values, roots, strict=True))
    selected, residual_frozen = resolve_lexicographic(frozenset(values))
    residual_points = set(residual_frozen)
    sponsor_points = [int(row[0]) for row in selected]
    if len(sponsor_points) != len(set(sponsor_points)):
        raise AssertionError(f"parent {state.index} repeats a sponsor")
    if residual_points & set(sponsor_points):
        raise AssertionError(f"parent {state.index} residual/sponsor overlap")
    if residual_points | set(sponsor_points) != set(values):
        raise AssertionError(f"parent {state.index} residual/sponsor partition incomplete")

    root_set = set(roots)
    residual_roots = {root_map[value] for value in residual_points}
    sponsor_roots_ordered = [root_map[value] for value in sponsor_points]
    sponsor_roots = set(sponsor_roots_ordered)
    if residual_roots & sponsor_roots or residual_roots | sponsor_roots != root_set:
        raise AssertionError(f"parent {state.index} root partition failed")

    minimum_point = min(values)
    minimum_root = root_map[minimum_point]
    if minimum_root != min(root_set):
        raise AssertionError(f"parent {state.index} minimum root mismatch")

    deletion_rank = {root: rank for rank, root in enumerate(sponsor_roots_ordered)}
    action_by_sponsor: dict[int, dict[str, object]] = {}
    action_edge_counter: Counter[Pair] = Counter()
    selected_step_mass = Fraction()
    selected_action_edge_occurrence_mass = Fraction()
    selected_full_triple_occurrence_mass = Fraction()
    deleted_sponsor_harmonic_mass = Fraction()

    for row in selected:
        sponsor, middle, opposite, step, left, right = map(int, row)
        sponsor_root = root_map[sponsor]
        middle_root = root_map[middle]
        opposite_root = root_map[opposite]
        left_root = root_map[left]
        right_root = root_map[right]
        if middle - left != step or right - middle != step:
            raise AssertionError("selected action is not a three-term progression")
        if middle_root - left_root != step or right_root - middle_root != step:
            raise AssertionError("root-coordinate progression mismatch")
        edge_pairs = {
            ordered_pair(sponsor_root, middle_root),
            ordered_pair(sponsor_root, opposite_root),
        }
        if len(edge_pairs) != 2:
            raise AssertionError("selected action edge collapse")
        for pair in edge_pairs:
            action_edge_counter[pair] += 1
        selected_step_mass += Fraction(1, step)
        selected_action_edge_occurrence_mass += Fraction(3, 2 * step)
        selected_full_triple_occurrence_mass += Fraction(5, 2 * step)
        deleted_sponsor_harmonic_mass += Fraction(1, sponsor)
        action_by_sponsor[sponsor_root] = {
            "step": step,
            "sponsor_point": sponsor,
            "middle_root": middle_root,
            "opposite_root": opposite_root,
            "direct_edges": edge_pairs,
        }

    if set(action_by_sponsor) != sponsor_roots:
        raise AssertionError(f"parent {state.index} action/sponsor mismatch")

    full_pairs = set(combinations(sorted(root_set), 2))
    residual_pairs = set(combinations(sorted(residual_roots), 2))
    elimination_pairs = full_pairs - residual_pairs
    core_pairs = set(combinations(sorted(sponsor_roots), 2))
    core_pairs.update(
        ordered_pair(minimum_root, sponsor_root)
        for sponsor_root in sponsor_roots
        if sponsor_root != minimum_root
    )
    if not core_pairs <= elimination_pairs:
        raise AssertionError(f"parent {state.index} core not contained in eliminated pairs")
    unused_cross_pairs = elimination_pairs - core_pairs

    full_energy = sum((pair_weight(pair) for pair in full_pairs), Fraction())
    residual_energy = sum((pair_weight(pair) for pair in residual_pairs), Fraction())
    elimination_energy = sum(
        (pair_weight(pair) for pair in elimination_pairs), Fraction()
    )
    core_energy = sum((pair_weight(pair) for pair in core_pairs), Fraction())
    unused_cross_energy = sum(
        (pair_weight(pair) for pair in unused_cross_pairs), Fraction()
    )
    if full_energy - residual_energy != elimination_energy:
        raise AssertionError("pair-energy deletion identity failed")
    if core_energy + unused_cross_energy != elimination_energy:
        raise AssertionError("core/cross partition identity failed")
    action_edge_occurrence_check = counter_mass(action_edge_counter, union=False)
    if action_edge_occurrence_check != selected_action_edge_occurrence_mass:
        raise AssertionError("selected action-edge energy identity failed")

    def owner(pair: Pair) -> int:
        candidates = [root for root in pair if root in sponsor_roots]
        if not candidates:
            raise AssertionError(f"pair {pair} has no sponsor owner")
        return min(candidates, key=lambda root: deletion_rank[root])

    return {
        "state": state,
        "reference": reference,
        "root_set": root_set,
        "residual_roots": residual_roots,
        "sponsor_roots": sponsor_roots,
        "minimum_root": minimum_root,
        "deletion_rank": deletion_rank,
        "action_by_sponsor": action_by_sponsor,
        "action_edge_counter": action_edge_counter,
        "core_pairs": core_pairs,
        "elimination_pairs": elimination_pairs,
        "unused_cross_pairs": unused_cross_pairs,
        "owner": owner,
        "selected_actions": len(selected),
        "selected_step_mass": selected_step_mass,
        "selected_action_edge_occurrence_mass": selected_action_edge_occurrence_mass,
        "selected_full_triple_occurrence_mass": selected_full_triple_occurrence_mass,
        "deleted_sponsor_harmonic_mass": deleted_sponsor_harmonic_mass,
        "parent_harmonic_mass": harmonic(values),
        "full_energy": full_energy,
        "residual_energy": residual_energy,
        "elimination_energy": elimination_energy,
        "core_energy": core_energy,
        "unused_cross_energy": unused_cross_energy,
    }


def active_resources_by_parent(
    states: tuple[object, ...],
) -> tuple[dict[int, Counter[Pair]], dict[int, dict[Pair, set[str]]]]:
    resources: dict[int, Counter[Pair]] = defaultdict(Counter)
    kinds: dict[int, dict[Pair, set[str]]] = defaultdict(lambda: defaultdict(set))
    for state in states:
        if not contains_three_term_ap(state.values):
            continue
        representative = state.representative
        parent_class = representative.parent_class
        reference = affine_reference(state)
        roots = tuple(representative.provenance)
        for root in roots:
            pair = ordered_pair(reference, root)
            resources[parent_class][pair] += 1
            kinds[parent_class][pair].add("recursive_current")
        for pair in combinations(sorted(roots), 2):
            resources[parent_class][pair] += 1
            kinds[parent_class][pair].add("recursive_latent")
    return dict(resources), {
        parent: dict(pair_kinds) for parent, pair_kinds in kinds.items()
    }


def histogram_records(
    count_histogram: Counter[int], mass_histogram: dict[int, Fraction]
) -> list[dict[str, object]]:
    return [
        {
            "floor_log2_distance_over_selected_step": scale,
            "resource_occurrences": count_histogram[scale],
            "mass": serialize_mass(mass_histogram[scale]),
        }
        for scale in sorted(count_histogram)
    ]


def transition_record(
    name: str,
    parents: tuple[object, ...],
    baseline_occurrences: tuple[object, ...],
    baseline_retained: tuple[object, ...],
) -> dict[str, object]:
    split_occurrences = build_split_occurrences(parents)
    split_retained, split_retention_metrics = retain_occurrences(split_occurrences)

    if support_union(baseline_occurrences) != support_union(split_occurrences):
        raise AssertionError(f"{name}: split changed raw support")
    if sum(len(item.values) for item in baseline_occurrences) != sum(
        len(item.values) for item in split_occurrences
    ):
        raise AssertionError(f"{name}: split changed raw point occurrences")
    if occurrence_harmonic_mass(baseline_occurrences) != occurrence_harmonic_mass(
        split_occurrences
    ):
        raise AssertionError(f"{name}: split changed raw harmonic occurrence mass")

    schedules = {state.index: schedule_data(state) for state in parents}
    if len(schedules) != len(parents):
        raise AssertionError(f"{name}: duplicate parent class index")

    baseline_active_by_parent, _baseline_kinds = active_resources_by_parent(
        baseline_retained
    )
    refined_active_by_parent, refined_kinds = active_resources_by_parent(split_retained)

    core_counter: Counter[Pair] = Counter()
    elimination_counter: Counter[Pair] = Counter()
    unused_cross_counter: Counter[Pair] = Counter()
    action_edge_counter: Counter[Pair] = Counter()
    refined_active_counter: Counter[Pair] = Counter()
    baseline_active_counter: Counter[Pair] = Counter()

    total_selected_actions = 0
    selected_step_mass = Fraction()
    action_edge_occurrence_mass = Fraction()
    action_full_triple_occurrence_mass = Fraction()
    sponsor_harmonic_mass = Fraction()
    parent_harmonic_mass = Fraction()

    scale_counts: Counter[int] = Counter()
    scale_masses: dict[int, Fraction] = defaultdict(Fraction)
    role_counts: Counter[str] = Counter()
    role_masses: dict[str, Fraction] = defaultdict(Fraction)
    direct_action_edge_occurrences = 0
    direct_action_edge_mass = Fraction()
    nondirect_occurrences = 0
    nondirect_mass = Fraction()
    missing_core: list[tuple[int, Pair, int]] = []
    parent_rows: list[dict[str, object]] = []

    for parent in parents:
        data = schedules[parent.index]
        core_pairs = data["core_pairs"]
        elimination_pairs = data["elimination_pairs"]
        unused_cross_pairs = data["unused_cross_pairs"]
        core_counter.update(core_pairs)
        elimination_counter.update(elimination_pairs)
        unused_cross_counter.update(unused_cross_pairs)
        action_edge_counter.update(data["action_edge_counter"])
        total_selected_actions += int(data["selected_actions"])
        selected_step_mass += data["selected_step_mass"]
        action_edge_occurrence_mass += data["selected_action_edge_occurrence_mass"]
        action_full_triple_occurrence_mass += data[
            "selected_full_triple_occurrence_mass"
        ]
        sponsor_harmonic_mass += data["deleted_sponsor_harmonic_mass"]
        parent_harmonic_mass += data["parent_harmonic_mass"]

        baseline_counter = baseline_active_by_parent.get(parent.index, Counter())
        refined_counter = refined_active_by_parent.get(parent.index, Counter())
        baseline_active_counter.update(baseline_counter)
        refined_active_counter.update(refined_counter)

        parent_direct_mass = Fraction()
        parent_nondirect_mass = Fraction()
        parent_scale_counts: Counter[int] = Counter()
        parent_scale_masses: dict[int, Fraction] = defaultdict(Fraction)

        for pair, multiplicity in refined_counter.items():
            if pair not in core_pairs:
                missing_core.append((parent.index, pair, multiplicity))
                continue
            owner = data["owner"](pair)
            action = data["action_by_sponsor"][owner]
            distance = pair[1] - pair[0]
            step = int(action["step"])
            scale = signed_floor_log2_ratio(distance, step)
            mass = pair_weight(pair) * multiplicity
            scale_counts[scale] += multiplicity
            scale_masses[scale] += mass
            parent_scale_counts[scale] += multiplicity
            parent_scale_masses[scale] += mass

            minimum_root = int(data["minimum_root"])
            sponsor_roots = data["sponsor_roots"]
            if minimum_root not in sponsor_roots and minimum_root in pair:
                role = "minimum_to_sponsor_star"
            elif minimum_root in pair:
                role = "internal_sponsor_pair_through_minimum"
            else:
                role = "internal_sponsor_pair"
            role_counts[role] += multiplicity
            role_masses[role] += mass

            if pair in action["direct_edges"]:
                direct_action_edge_occurrences += multiplicity
                direct_action_edge_mass += mass
                parent_direct_mass += mass
            else:
                nondirect_occurrences += multiplicity
                nondirect_mass += mass
                parent_nondirect_mass += mass

        refined_occurrence_mass_parent = counter_mass(refined_counter, union=False)
        refined_union_mass_parent = counter_mass(refined_counter, union=True)
        core_mass_parent = data["core_energy"]
        step_mass_parent = data["selected_step_mass"]
        parent_rows.append(
            {
                "parent_class": parent.index,
                "parent_points": len(parent.values),
                "parent_mass": serialize_mass(parent.weight),
                "selected_actions": data["selected_actions"],
                "residual_roots": len(data["residual_roots"]),
                "sponsor_roots": len(data["sponsor_roots"]),
                "minimum_is_sponsor": data["minimum_root"] in data["sponsor_roots"],
                "selected_step_mass": serialize_mass(step_mass_parent),
                "deleted_sponsor_harmonic_mass": serialize_mass(
                    data["deleted_sponsor_harmonic_mass"]
                ),
                "sponsor_core_pairs": len(core_pairs),
                "sponsor_core_mass": serialize_mass(core_mass_parent),
                "elimination_pair_mass": serialize_mass(data["elimination_energy"]),
                "unused_cross_pair_mass": serialize_mass(data["unused_cross_energy"]),
                "baseline_active_resource_occurrences": sum(
                    baseline_counter.values()
                ),
                "refined_active_resource_occurrences": sum(refined_counter.values()),
                "refined_active_distinct_resources": len(refined_counter),
                "refined_active_occurrence_mass": serialize_mass(
                    refined_occurrence_mass_parent
                ),
                "refined_active_union_mass": serialize_mass(refined_union_mass_parent),
                "activation_over_core": ratio_record(
                    refined_occurrence_mass_parent, core_mass_parent
                ),
                "activation_over_selected_step": ratio_record(
                    refined_occurrence_mass_parent, step_mass_parent
                ),
                "core_over_selected_step": ratio_record(
                    core_mass_parent, step_mass_parent
                ),
                "activation_over_deleted_sponsor_harmonic": ratio_record(
                    refined_occurrence_mass_parent,
                    data["deleted_sponsor_harmonic_mass"],
                ),
                "direct_action_edge_mass": serialize_mass(parent_direct_mass),
                "nondirect_mass": serialize_mass(parent_nondirect_mass),
                "scale_histogram": histogram_records(
                    parent_scale_counts, parent_scale_masses
                ),
            }
        )

    if missing_core:
        raise AssertionError(
            f"{name}: {len(missing_core)} refined active resources outside sponsor core"
        )

    parent_rows.sort(
        key=lambda row: Fraction(row["activation_over_selected_step"]["fraction"]),
        reverse=True,
    )

    baseline_profile = resource_profile(baseline_retained)
    refined_profile = resource_profile(split_retained)
    baseline_active_occurrence_mass = counter_mass(
        baseline_active_counter, union=False
    )
    baseline_active_union_mass = counter_mass(baseline_active_counter, union=True)
    refined_active_occurrence_mass = counter_mass(
        refined_active_counter, union=False
    )
    refined_active_union_mass = counter_mass(refined_active_counter, union=True)
    core_occurrence_mass = counter_mass(core_counter, union=False)
    core_union_mass = counter_mass(core_counter, union=True)
    elimination_occurrence_mass = counter_mass(elimination_counter, union=False)
    elimination_union_mass = counter_mass(elimination_counter, union=True)
    unused_cross_occurrence_mass = counter_mass(unused_cross_counter, union=False)
    action_edge_union_mass = counter_mass(action_edge_counter, union=True)

    if core_occurrence_mass + unused_cross_occurrence_mass != elimination_occurrence_mass:
        raise AssertionError(f"{name}: aggregate core/cross identity failed")
    if action_edge_occurrence_mass != counter_mass(action_edge_counter, union=False):
        raise AssertionError(f"{name}: aggregate selected-action edge identity failed")

    role_records = [
        {
            "role": role,
            "resource_occurrences": role_counts[role],
            "mass": serialize_mass(role_masses[role]),
        }
        for role in sorted(role_counts)
    ]

    return {
        "name": name,
        "parents": {
            "states": len(parents),
            "points": sum(len(state.values) for state in parents),
            "harmonic_mass": serialize_mass(parent_harmonic_mass),
            "selected_actions": total_selected_actions,
            "sponsor_roots_occurrences": total_selected_actions,
            "selected_step_mass": serialize_mass(selected_step_mass),
            "deleted_sponsor_harmonic_mass": serialize_mass(sponsor_harmonic_mass),
            "selected_action_edge_occurrence_mass": serialize_mass(
                action_edge_occurrence_mass
            ),
            "selected_action_edge_union_mass": serialize_mass(action_edge_union_mass),
            "selected_full_triple_occurrence_mass": serialize_mass(
                action_full_triple_occurrence_mass
            ),
        },
        "available_pair_resources": {
            "sponsor_core_occurrences": sum(core_counter.values()),
            "sponsor_core_distinct": len(core_counter),
            "sponsor_core_maximum_multiplicity": max(core_counter.values(), default=0),
            "sponsor_core_occurrence_mass": serialize_mass(core_occurrence_mass),
            "sponsor_core_union_mass": serialize_mass(core_union_mass),
            "elimination_occurrences": sum(elimination_counter.values()),
            "elimination_distinct": len(elimination_counter),
            "elimination_occurrence_mass": serialize_mass(elimination_occurrence_mass),
            "elimination_union_mass": serialize_mass(elimination_union_mass),
            "unused_cross_occurrences": sum(unused_cross_counter.values()),
            "unused_cross_distinct": len(unused_cross_counter),
            "unused_cross_occurrence_mass": serialize_mass(
                unused_cross_occurrence_mass
            ),
            "core_plus_unused_equals_elimination": True,
        },
        "activated_recursive_resources": {
            "baseline_occurrences": sum(baseline_active_counter.values()),
            "baseline_distinct": len(baseline_active_counter),
            "baseline_occurrence_mass": serialize_mass(
                baseline_active_occurrence_mass
            ),
            "baseline_union_mass": serialize_mass(baseline_active_union_mass),
            "refined_occurrences": sum(refined_active_counter.values()),
            "refined_distinct": len(refined_active_counter),
            "refined_maximum_multiplicity": max(
                refined_active_counter.values(), default=0
            ),
            "refined_repeated_tokens": sum(
                count > 1 for count in refined_active_counter.values()
            ),
            "refined_occurrence_mass": serialize_mass(
                refined_active_occurrence_mass
            ),
            "refined_union_mass": serialize_mass(refined_active_union_mass),
            "occurrence_mass_reduction": serialize_mass(
                baseline_active_occurrence_mass - refined_active_occurrence_mass
            ),
            "union_mass_reduction": serialize_mass(
                baseline_active_union_mass - refined_active_union_mass
            ),
            "all_refined_resources_in_sponsor_core": True,
            "direct_action_edge_occurrences": direct_action_edge_occurrences,
            "direct_action_edge_mass": serialize_mass(direct_action_edge_mass),
            "nondirect_occurrences": nondirect_occurrences,
            "nondirect_mass": serialize_mass(nondirect_mass),
            "direct_mass_share": ratio_record(
                direct_action_edge_mass, refined_active_occurrence_mass
            ),
            "role_profile": role_records,
            "scale_profile": histogram_records(scale_counts, scale_masses),
        },
        "candidate_ratios": {
            "refined_activation_over_sponsor_core_occurrence": ratio_record(
                refined_active_occurrence_mass, core_occurrence_mass
            ),
            "refined_activation_over_sponsor_core_union": ratio_record(
                refined_active_union_mass, core_union_mass
            ),
            "refined_activation_over_selected_step_mass": ratio_record(
                refined_active_occurrence_mass, selected_step_mass
            ),
            "refined_union_activation_over_selected_step_mass": ratio_record(
                refined_active_union_mass, selected_step_mass
            ),
            "sponsor_core_over_selected_step_mass": ratio_record(
                core_occurrence_mass, selected_step_mass
            ),
            "refined_activation_over_action_edge_mass": ratio_record(
                refined_active_occurrence_mass, action_edge_occurrence_mass
            ),
            "refined_activation_over_deleted_sponsor_harmonic": ratio_record(
                refined_active_occurrence_mass, sponsor_harmonic_mass
            ),
            "selected_step_over_parent_harmonic": ratio_record(
                selected_step_mass, parent_harmonic_mass
            ),
        },
        "retained_frontier": {
            "raw_support_preserved": True,
            "raw_point_occurrences_preserved": True,
            "raw_harmonic_occurrence_preserved": True,
            "baseline": baseline_profile,
            "refined": refined_profile,
            "recursive_point_change": (
                int(refined_profile["recursive_points"])
                - int(baseline_profile["recursive_points"])
            ),
            "terminal_point_change": (
                int(refined_profile["terminal_points"])
                - int(baseline_profile["terminal_points"])
            ),
            "recursive_mass_change": serialize_mass(
                Fraction(refined_profile["recursive_mass"]["fraction"])
                - Fraction(baseline_profile["recursive_mass"]["fraction"])
            ),
            "terminal_mass_change": serialize_mass(
                Fraction(refined_profile["terminal_mass"]["fraction"])
                - Fraction(baseline_profile["terminal_mass"]["fraction"])
            ),
            "split_retention_metrics": split_retention_metrics,
        },
        "parent_extrema": {
            "maximum_activation_over_selected_step": parent_rows[0][
                "activation_over_selected_step"
            ]
            if parent_rows
            else None,
            "maximum_core_over_selected_step": max(
                (
                    row["core_over_selected_step"]
                    for row in parent_rows
                    if row["core_over_selected_step"] is not None
                ),
                key=lambda record: Fraction(record["fraction"]),
                default=None,
            ),
        },
        "parent_rows": parent_rows,
        "hashes": {
            "parents": state_signature(parents),
            "baseline_retained": state_signature(baseline_retained),
            "refined_retained": state_signature(split_retained),
            "sponsor_core": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(core_counter.items())]
            ),
            "refined_active": canonical_hash(
                [
                    (
                        left,
                        right,
                        count,
                        sorted(
                            {
                                kind
                                for parent_kinds in refined_kinds.values()
                                for pair, kinds in parent_kinds.items()
                                if pair == (left, right)
                                for kind in kinds
                            }
                        ),
                    )
                    for (left, right), count in sorted(refined_active_counter.items())
                ]
            ),
        },
    }


def main() -> int:
    retained_first, retained_second_certified = reconstruct_retained_families()
    r1 = recursive_states(retained_first)
    if len(r1) != len(retained_first):
        raise AssertionError("R1 unexpectedly contains terminal states")

    occ2, retained_second, _metrics2, _rows2 = propagate_recursive_states(r1)
    if state_signature(retained_second) != state_signature(retained_second_certified):
        raise AssertionError("reconstructed F2 differs from certified retained family")
    r2 = recursive_states(retained_second)

    occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(r2)
    r3 = recursive_states(retained_third)

    occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(r3)
    r4 = recursive_states(retained_fourth)

    occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(r4)

    transitions = [
        transition_record("R1_to_F2", r1, occ2, retained_second),
        transition_record("R2_to_F3", r2, occ3, retained_third),
        transition_record("R3_to_F4", r3, occ4, retained_fourth),
        transition_record("R4_to_F5", r4, occ5, retained_fifth),
    ]

    maximum_activation_ratio = max(
        (
            (
                Fraction(
                    row["candidate_ratios"][
                        "refined_activation_over_selected_step_mass"
                    ]["fraction"]
                ),
                row["name"],
            )
            for row in transitions
        ),
        default=(Fraction(), ""),
    )
    maximum_union_activation_ratio = max(
        (
            (
                Fraction(
                    row["candidate_ratios"][
                        "refined_union_activation_over_selected_step_mass"
                    ]["fraction"]
                ),
                row["name"],
            )
            for row in transitions
        ),
        default=(Fraction(), ""),
    )

    output = {
        "schema": "sponsor_core_activation_frontier_probe_v1",
        "scope": "certified_R1_through_R4_recursive_transitions_with_residual_sponsor_refinement",
        "generation_six_propagated": False,
        "symbolic_identities": {
            "pair_energy_deletion": "J(P)-J(Q)=sum of pair weights incident to deleted sponsors at first deletion",
            "sponsor_core_partition": "core_energy+unused_residual_sponsor_cross_energy=J(P)-J(Q)",
            "action_edge_energy": "sum_selected [1/q+1/(2q)]=(3/2) sum_selected 1/q",
        },
        "transitions": transitions,
        "finite_candidate_constants": {
            "maximum_refined_activation_over_selected_step_mass": serialize_mass(
                maximum_activation_ratio[0]
            ),
            "attained_at": maximum_activation_ratio[1],
            "maximum_refined_union_activation_over_selected_step_mass": serialize_mass(
                maximum_union_activation_ratio[0]
            ),
            "union_attained_at": maximum_union_activation_ratio[1],
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
