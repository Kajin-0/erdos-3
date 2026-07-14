#!/usr/bin/env python3
"""Resolve recursive-mass ranges across tied maximum-harmonic retention choices.

This extends the exact fourth-to-fifth policy-sensitivity experiment.  For the
baseline, all-reverse, and each single-parent reverse flip, every same-shell
conflict component is optimized first for total harmonic mass.  Among all
maximum-total-harmonic independent sets, a second exact dynamic program computes
minimum and maximum recursively continuing harmonic mass.

The output answers whether the fourth-to-fifth expansion can be removed solely by
choosing a different tied maximum-harmonic retained family.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import sys

from probe_fourth_to_fifth_policy_sensitivity import (
    compact_bracket,
    decimal_text,
    fraction_hash,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import (
    DescendantOccurrence,
    build_descendant_occurrences,
    components,
    descendant_classes,
    descendant_conflict_graph,
)
from verify_retained_terminal_split import contains_three_term_ap
from verify_s7_regenerative_seed_policy_dependence import all_three_aps, resolve

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(30_000)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def component_optimal_recursive_range(
    component: tuple[int, ...],
    classes: tuple[object, ...],
    adjacency: dict[int, set[int]],
) -> tuple[Fraction, Fraction, Fraction, int, int]:
    """Return max total weight, min/max recursive weight, count, DP states."""
    position = {vertex: index for index, vertex in enumerate(component)}
    neighbor_masks: list[int] = []
    total_weights: list[Fraction] = []
    recursive_weights: list[Fraction] = []
    for vertex in component:
        mask = 0
        for target in adjacency[vertex]:
            if target in position:
                mask |= 1 << position[target]
        neighbor_masks.append(mask)
        total_weights.append(classes[vertex].weight)
        recursive_weights.append(
            classes[vertex].weight
            if contains_three_term_ap(classes[vertex].values)
            else Fraction()
        )

    @lru_cache(maxsize=None)
    def solve(mask: int) -> tuple[Fraction, Fraction, Fraction, int]:
        if mask == 0:
            return Fraction(), Fraction(), Fraction(), 1
        index = (mask & -mask).bit_length() - 1
        without = mask & ~(1 << index)
        ex_total, ex_min_rec, ex_max_rec, ex_count = solve(without)
        included_mask = without & ~neighbor_masks[index]
        in_total, in_min_rec, in_max_rec, in_count = solve(included_mask)
        in_total += total_weights[index]
        in_min_rec += recursive_weights[index]
        in_max_rec += recursive_weights[index]

        if in_total > ex_total:
            return in_total, in_min_rec, in_max_rec, in_count
        if ex_total > in_total:
            return ex_total, ex_min_rec, ex_max_rec, ex_count
        return (
            ex_total,
            min(ex_min_rec, in_min_rec),
            max(ex_max_rec, in_max_rec),
            ex_count + in_count,
        )

    total, min_rec, max_rec, count = solve((1 << len(component)) - 1)
    return total, min_rec, max_rec, count, solve.cache_info().currsize


def policy_range(
    raw_rows: list[tuple[object, ...]],
) -> dict[str, object]:
    occurrences = tuple(
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
        for index, row in enumerate(raw_rows)
    )
    classes = descendant_classes(occurrences)
    adjacency = descendant_conflict_graph(classes)
    component_family = sorted(
        components(adjacency),
        key=lambda item: (classes[item[0]].representative.exponent, item),
    )

    total_mass = Fraction()
    min_recursive_mass = Fraction()
    max_recursive_mass = Fraction()
    optimizer_count = 1
    nonunique_components = 0
    dp_states = 0
    component_rows: list[dict[str, object]] = []
    for component in component_family:
        total, min_rec, max_rec, count, states = component_optimal_recursive_range(
            component, classes, adjacency
        )
        total_mass += total
        min_recursive_mass += min_rec
        max_recursive_mass += max_rec
        optimizer_count *= count
        dp_states += states
        if count != 1:
            nonunique_components += 1
            component_rows.append(
                {
                    "exponent": classes[component[0]].representative.exponent,
                    "vertices": list(component),
                    "optimizer_count": count,
                    "total_mass_sha256": fraction_hash(total),
                    "min_recursive_mass_sha256": fraction_hash(min_rec),
                    "max_recursive_mass_sha256": fraction_hash(max_rec),
                    "recursive_mass_varies": min_rec != max_rec,
                }
            )

    return {
        "raw_occurrences": len(occurrences),
        "exact_state_classes": len(classes),
        "conflict_components": len(component_family),
        "nonunique_components": nonunique_components,
        "global_optimizer_count": optimizer_count,
        "dp_states_examined": dp_states,
        "total_mass": total_mass,
        "min_recursive_mass": min_recursive_mass,
        "max_recursive_mass": max_recursive_mass,
        "nonunique_component_rows": component_rows,
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
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
    if len(recursive_fourth) != 12:
        raise AssertionError("certified fourth recursive family changed")

    parent_mass = sum((state.weight for state in recursive_fourth), Fraction())
    alternatives: dict[int, dict[bool, list[tuple[object, ...]]]] = {}
    for state in recursive_fourth:
        progressions = all_three_aps(state.values)
        by_direction: dict[bool, list[tuple[object, ...]]] = {}
        for reverse in (False, True):
            selected, _residual = resolve(
                frozenset(state.values), progressions, reverse=reverse
            )
            by_direction[reverse] = build_descendant_occurrences(
                state.index,
                state.values,
                state.representative.provenance,
                selected,
            )
        alternatives[state.index] = by_direction

    parent_indices = tuple(state.index for state in recursive_fourth)
    policies: list[tuple[str, frozenset[int]]] = [
        ("all_lexicographic", frozenset()),
        ("all_reverse", frozenset(parent_indices)),
    ]
    policies.extend(
        (f"reverse_parent_{index}", frozenset({index}))
        for index in parent_indices
    )

    records: list[dict[str, object]] = []
    for name, reversed_parents in policies:
        raw_rows = [
            row
            for index in parent_indices
            for row in alternatives[index][index in reversed_parents]
        ]
        result = policy_range(raw_rows)
        min_ratio = result["min_recursive_mass"] / parent_mass
        max_ratio = result["max_recursive_mass"] / parent_mass
        records.append(
            {
                "policy": name,
                "reversed_parents": sorted(reversed_parents),
                "raw_occurrences": result["raw_occurrences"],
                "exact_state_classes": result["exact_state_classes"],
                "conflict_components": result["conflict_components"],
                "nonunique_components": result["nonunique_components"],
                "global_optimizer_count": result["global_optimizer_count"],
                "dp_states_examined": result["dp_states_examined"],
                "total_mass_decimal": decimal_text(result["total_mass"]),
                "total_mass_sha256": fraction_hash(result["total_mass"]),
                "min_recursive_mass_decimal": decimal_text(
                    result["min_recursive_mass"]
                ),
                "max_recursive_mass_decimal": decimal_text(
                    result["max_recursive_mass"]
                ),
                "min_recursive_mass_sha256": fraction_hash(
                    result["min_recursive_mass"]
                ),
                "max_recursive_mass_sha256": fraction_hash(
                    result["max_recursive_mass"]
                ),
                "min_recursive_ratio_decimal": decimal_text(min_ratio),
                "max_recursive_ratio_decimal": decimal_text(max_ratio),
                "min_recursive_ratio_bracket_millionth": compact_bracket(min_ratio),
                "max_recursive_ratio_bracket_millionth": compact_bracket(max_ratio),
                "min_recursive_ratio_sha256": fraction_hash(min_ratio),
                "max_recursive_ratio_sha256": fraction_hash(max_ratio),
                "every_max_harmonic_optimum_expands": min_ratio > 1,
                "nonunique_component_rows": result["nonunique_component_rows"],
            }
        )

    records.sort(
        key=lambda row: (
            Fraction(row["min_recursive_ratio_bracket_millionth"][0]),
            row["policy"],
        )
    )
    best = records[0]
    output = {
        "schema": "fourth_to_fifth_retention_tie_range_probe_v1",
        "scope": "fourteen_deletion_policies_all_maximum_harmonic_retention_ties",
        "parent_mass_decimal": decimal_text(parent_mass),
        "parent_mass_sha256": fraction_hash(parent_mass),
        "policy_count": len(records),
        "all_tested_max_harmonic_optima_expand": all(
            row["every_max_harmonic_optimum_expands"] for row in records
        ),
        "best_policy": best["policy"],
        "best_min_recursive_ratio_decimal": best[
            "min_recursive_ratio_decimal"
        ],
        "best_min_recursive_ratio_sha256": best[
            "min_recursive_ratio_sha256"
        ],
        "records": records,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
