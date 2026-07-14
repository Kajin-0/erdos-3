#!/usr/bin/env python3
"""Probe third-generation retained recursion and terminal-token recreation exactly.

This is an exploratory exact computation. It reuses the certified local37 policy,
retained quotient, lexicographic child resolution, and same-shell maximum-harmonic
conflict rule. The output is deterministic JSON intended to be converted into a
fixed certificate only after the result is inspected.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from export_simultaneous_deletion_transition import verify_schedule
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import (
    DescendantOccurrence,
    build_descendant_occurrences,
    components,
    descendant_classes,
    descendant_conflict_graph,
    maximum_weight_independent_set_dp,
    resolve_lexicographic,
)
from verify_retained_terminal_split import contains_three_term_ap
from verify_s1_deletion_dag_adapter import build_shell_occurrences, middle_resolution
from verify_s7_local_optimum_transition_profile import resolve_named_policy
from verify_s7_regenerative_seed_policy_dependence import all_three_aps

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def state_records(states: tuple[object, ...]) -> list[dict[str, object]]:
    return [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "parent_class": state.representative.parent_class,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "root_provenance": list(state.representative.provenance),
            "immediate_provenance": list(
                state.representative.immediate_provenance
            ),
        }
        for state in states
    ]


def state_tokens(states: tuple[object, ...]) -> set[tuple[int, int]]:
    tokens: set[tuple[int, int]] = set()
    for state in states:
        for value, root in zip(
            state.values, state.representative.provenance, strict=True
        ):
            tokens.add((value, root))
    return tokens


def state_values(states: tuple[object, ...]) -> set[int]:
    return {value for state in states for value in state.values}


def state_value_sets(states: tuple[object, ...]) -> set[tuple[int, ...]]:
    return {tuple(state.values) for state in states}


def first_generation_raw_tokens() -> tuple[set[tuple[int, int]], int]:
    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    selected, residual = resolve_named_policy("local37", parent, progressions)
    verify_schedule(parent, selected, residual)
    _steps, fibers, _terminal_sponsor, fiber_provenance = middle_resolution(
        selected
    )
    occurrences = build_shell_occurrences(parent, fibers, fiber_provenance)
    tokens = {
        (value, root)
        for occurrence in occurrences
        for value, root in zip(
            occurrence.values, occurrence.provenance, strict=True
        )
    }
    return tokens, sum(len(occurrence.values) for occurrence in occurrences)


def propagate_recursive_states(
    recursive_second: tuple[object, ...],
) -> tuple[
    tuple[DescendantOccurrence, ...],
    tuple[object, ...],
    dict[str, int],
    list[dict[str, object]],
]:
    raw_rows: list[tuple[object, ...]] = []
    child_rows: list[dict[str, object]] = []
    for state in recursive_second:
        selected, residual = resolve_lexicographic(frozenset(state.values))
        rows = build_descendant_occurrences(
            state.index,
            state.values,
            state.representative.provenance,
            selected,
        )
        raw_rows.extend(rows)
        child_rows.append(
            {
                "parent_class": state.index,
                "parent_size": len(state.values),
                "selected_actions": len(selected),
                "residual_size": len(residual),
                "raw_outputs": len(rows),
            }
        )

    occurrences = tuple(
        DescendantOccurrence(index=index, parent_class=row[0], source=row[1],
                             source_step=row[2], exponent=row[3], values=row[4],
                             provenance=row[5], immediate_provenance=row[6])
        for index, row in enumerate(raw_rows)
    )
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
    retained_union = state_values(retained)
    if sum(len(state.values) for state in retained) != len(retained_union):
        raise AssertionError("third-generation retained states are not point-disjoint")

    metrics = {
        "recursive_second_parent_states": len(recursive_second),
        "recursive_second_parent_points": sum(
            len(state.values) for state in recursive_second
        ),
        "child_selected_actions": sum(
            int(row["selected_actions"]) for row in child_rows
        ),
        "child_terminal_residual_points": sum(
            int(row["residual_size"]) for row in child_rows
        ),
        "raw_occurrences": len(occurrences),
        "raw_occurrence_points": sum(len(row.values) for row in occurrences),
        "exact_state_classes": len(classes),
        "conflict_edges": sum(len(targets) for targets in adjacency.values()) // 2,
        "conflict_components": len(component_family),
        "largest_conflict_component": largest_component,
        "components_with_nonunique_optimum": nonunique_components,
        "dp_states_examined": total_dp_states,
        "retained_states": len(retained),
        "retained_points": len(retained_union),
    }
    return occurrences, retained, metrics, child_rows


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    if len(terminal_second) != 13 or len(recursive_second) != 14:
        raise AssertionError("certified second-generation split changed")

    first_raw_tokens, first_raw_occurrence_points = first_generation_raw_tokens()
    first_retained_tokens = state_tokens(retained_first)
    second_terminal_tokens = state_tokens(terminal_second)
    second_terminal_values = state_values(terminal_second)
    second_terminal_state_sets = state_value_sets(terminal_second)

    occurrences, retained_third, metrics, child_rows = propagate_recursive_states(
        recursive_second
    )
    terminal_third = tuple(
        state for state in retained_third
        if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )

    third_all_tokens = state_tokens(retained_third)
    third_terminal_tokens = state_tokens(terminal_third)
    third_recursive_tokens = state_tokens(recursive_third)
    third_all_values = state_values(retained_third)
    third_terminal_values = state_values(terminal_third)
    third_recursive_values = state_values(recursive_third)
    third_state_sets = state_value_sets(retained_third)

    first_mass = sum((state.weight for state in retained_first), Fraction())
    second_recursive_mass = sum(
        (state.weight for state in recursive_second), Fraction()
    )
    third_mass = sum((state.weight for state in retained_third), Fraction())
    third_terminal_mass = sum(
        (state.weight for state in terminal_third), Fraction()
    )
    third_recursive_mass = sum(
        (state.weight for state in recursive_third), Fraction()
    )
    if third_terminal_mass + third_recursive_mass != third_mass:
        raise AssertionError("third terminal/recursive mass partition failed")

    token_recreation_all = sorted(second_terminal_tokens & third_all_tokens)
    token_recreation_terminal = sorted(
        second_terminal_tokens & third_terminal_tokens
    )
    token_recreation_recursive = sorted(
        second_terminal_tokens & third_recursive_tokens
    )
    numerical_recreation_all = sorted(second_terminal_values & third_all_values)
    numerical_recreation_terminal = sorted(
        second_terminal_values & third_terminal_values
    )
    numerical_recreation_recursive = sorted(
        second_terminal_values & third_recursive_values
    )
    exact_state_regeneration = sorted(second_terminal_state_sets & third_state_sets)

    earlier_raw_token_collisions = sorted(
        second_terminal_tokens & first_raw_tokens
    )
    earlier_retained_token_collisions = sorted(
        second_terminal_tokens & first_retained_tokens
    )

    root_counts_third = Counter(
        root
        for state in retained_third
        for root in state.representative.provenance
    )

    ratios = {
        "third_total_over_second_recursive": third_mass / second_recursive_mass,
        "third_recursive_over_second_recursive": (
            third_recursive_mass / second_recursive_mass
        ),
        "third_terminal_over_third_total": (
            third_terminal_mass / third_mass if third_mass else Fraction()
        ),
        "third_recursive_over_third_total": (
            third_recursive_mass / third_mass if third_mass else Fraction()
        ),
        "third_recursive_over_first_retained": (
            third_recursive_mass / first_mass
        ),
        "three_generation_recursive_margin_from_second": (
            (second_recursive_mass - third_recursive_mass) / second_recursive_mass
        ),
    }

    payload = {
        "schema": "third_generation_recursive_frontier_probe_v1",
        "policy": "local37_then_lexicographic_recursive_only",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "metrics": {
            **metrics,
            "terminal_third_states": len(terminal_third),
            "terminal_third_points": len(third_terminal_values),
            "recursive_third_states": len(recursive_third),
            "recursive_third_points": len(third_recursive_values),
            "first_raw_distinct_tokens": len(first_raw_tokens),
            "first_raw_occurrence_points": first_raw_occurrence_points,
            "first_retained_tokens": len(first_retained_tokens),
            "second_terminal_tokens": len(second_terminal_tokens),
            "third_retained_tokens": len(third_all_tokens),
            "third_root_provenance_distinct": len(root_counts_third),
            "third_root_provenance_repeated": sum(
                multiplicity > 1 for multiplicity in root_counts_third.values()
            ),
            "third_root_provenance_max_multiplicity": max(
                root_counts_third.values(), default=0
            ),
            "earlier_raw_token_collision_count": len(
                earlier_raw_token_collisions
            ),
            "earlier_retained_token_collision_count": len(
                earlier_retained_token_collisions
            ),
            "third_same_token_recreation_count": len(token_recreation_all),
            "third_terminal_same_token_recreation_count": len(
                token_recreation_terminal
            ),
            "third_recursive_same_token_recreation_count": len(
                token_recreation_recursive
            ),
            "third_numerical_recreation_count": len(numerical_recreation_all),
            "third_terminal_numerical_recreation_count": len(
                numerical_recreation_terminal
            ),
            "third_recursive_numerical_recreation_count": len(
                numerical_recreation_recursive
            ),
            "third_exact_terminal_state_regeneration_count": len(
                exact_state_regeneration
            ),
        },
        "masses": {
            "first_retained": fraction_text(first_mass),
            "second_recursive": fraction_text(second_recursive_mass),
            "third_total": fraction_text(third_mass),
            "third_terminal": fraction_text(third_terminal_mass),
            "third_recursive": fraction_text(third_recursive_mass),
        },
        "mass_hashes": {
            "first_retained": fraction_hash(first_mass),
            "second_recursive": fraction_hash(second_recursive_mass),
            "third_total": fraction_hash(third_mass),
            "third_terminal": fraction_hash(third_terminal_mass),
            "third_recursive": fraction_hash(third_recursive_mass),
        },
        "ratios": {name: fraction_text(value) for name, value in ratios.items()},
        "ratio_hashes": {
            name: fraction_hash(value) for name, value in ratios.items()
        },
        "collisions": {
            "second_terminal_vs_first_raw_tokens": [
                list(row) for row in earlier_raw_token_collisions
            ],
            "second_terminal_vs_first_retained_tokens": [
                list(row) for row in earlier_retained_token_collisions
            ],
            "second_terminal_vs_third_all_tokens": [
                list(row) for row in token_recreation_all
            ],
            "second_terminal_vs_third_terminal_tokens": [
                list(row) for row in token_recreation_terminal
            ],
            "second_terminal_vs_third_recursive_tokens": [
                list(row) for row in token_recreation_recursive
            ],
            "second_terminal_numerical_vs_third_all": numerical_recreation_all,
            "second_terminal_numerical_vs_third_terminal": (
                numerical_recreation_terminal
            ),
            "second_terminal_numerical_vs_third_recursive": (
                numerical_recreation_recursive
            ),
            "second_terminal_exact_state_vs_third": [
                list(values) for values in exact_state_regeneration
            ],
        },
        "hashes": {
            "child_transition_summary": canonical_hash(child_rows),
            "third_retained_family": canonical_hash(
                state_records(retained_third)
            ),
            "third_terminal_family": canonical_hash(
                state_records(terminal_third)
            ),
            "third_recursive_family": canonical_hash(
                state_records(recursive_third)
            ),
            "third_all_tokens": canonical_hash(
                sorted([list(row) for row in third_all_tokens])
            ),
            "third_terminal_tokens": canonical_hash(
                sorted([list(row) for row in third_terminal_tokens])
            ),
            "third_recursive_tokens": canonical_hash(
                sorted([list(row) for row in third_recursive_tokens])
            ),
            "third_raw_occurrences": canonical_hash(
                [
                    {
                        "index": row.index,
                        "parent_class": row.parent_class,
                        "source": row.source,
                        "source_step": row.source_step,
                        "exponent": row.exponent,
                        "values": list(row.values),
                        "provenance": list(row.provenance),
                        "immediate_provenance": list(
                            row.immediate_provenance
                        ),
                    }
                    for row in occurrences
                ]
            ),
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
