#!/usr/bin/env python3
"""Test local deletion-policy sensitivity of the fourth-to-fifth retained transition.

The fourth-generation retained family is reconstructed using the certified fixed
construction.  Each of its twelve recursive parents is resolved once with the
lexicographic deletion schedule and once with the reverse-lexicographic schedule.
The probe then evaluates:

* the all-lexicographic certified baseline;
* the all-reverse policy;
* each of the twelve single-parent lexicographic-to-reverse flips.

Every assembled occurrence family is passed through the same exact-state quotient
and componentwise maximum-harmonic same-shell independent-set rule.  This is a
finite policy-sensitivity experiment, not a universal retention theorem.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_third_generation_recursive_frontier import (
    canonical_hash,
    propagate_recursive_states,
    state_records,
)
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import (
    DescendantOccurrence,
    build_descendant_occurrences,
    components,
    descendant_classes,
    descendant_conflict_graph,
    maximum_weight_independent_set_dp,
)
from verify_retained_terminal_split import contains_three_term_ap
from verify_s7_regenerative_seed_policy_dependence import all_three_aps, resolve

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(30_000)

EXPECTED_BASELINE_RECURSIVE_HASH = (
    "7335c3e6111ce0225098f3fc769fb67592c942caf0c21a6481fce731aff1dc99"
)
EXPECTED_BASELINE_RATIO_HASH = (
    "8d55faef41edb883a3d2d229690ef16db69bd1be23f85871c21c3206319e0534"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def compact_bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = (value.numerator * denominator) // value.denominator
    return [
        fraction_text(Fraction(lower_numerator, denominator)),
        fraction_text(Fraction(lower_numerator + 1, denominator)),
    ]


def recursive_family_hash(states: tuple[object, ...]) -> str:
    return canonical_hash(state_records(states))


def quotient(
    raw_rows: list[tuple[object, ...]],
) -> tuple[tuple[DescendantOccurrence, ...], tuple[object, ...], dict[str, int]]:
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
    values = [value for state in retained for value in state.values]
    if len(values) != len(set(values)):
        raise AssertionError("retained policy family is not point-disjoint")

    metrics = {
        "raw_occurrences": len(occurrences),
        "raw_occurrence_points": sum(len(row.values) for row in occurrences),
        "exact_state_classes": len(classes),
        "conflict_edges": sum(len(targets) for targets in adjacency.values()) // 2,
        "conflict_components": len(component_family),
        "largest_conflict_component": largest_component,
        "components_with_nonunique_optimum": nonunique_components,
        "dp_states_examined": total_dp_states,
        "retained_states": len(retained),
        "retained_points": len(values),
    }
    return occurrences, retained, metrics


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
    alternatives: dict[int, dict[bool, dict[str, object]]] = {}
    for state in recursive_fourth:
        progressions = all_three_aps(state.values)
        by_direction: dict[bool, dict[str, object]] = {}
        for reverse in (False, True):
            selected, residual = resolve(
                frozenset(state.values), progressions, reverse=reverse
            )
            rows = build_descendant_occurrences(
                state.index,
                state.values,
                state.representative.provenance,
                selected,
            )
            by_direction[reverse] = {
                "selected": len(selected),
                "residual": len(residual),
                "rows": rows,
            }
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
        raw_rows: list[tuple[object, ...]] = []
        selected_actions = 0
        residual_points = 0
        for index in parent_indices:
            choice = alternatives[index][index in reversed_parents]
            raw_rows.extend(choice["rows"])
            selected_actions += int(choice["selected"])
            residual_points += int(choice["residual"])

        _occurrences, retained, metrics = quotient(raw_rows)
        terminal = tuple(
            state for state in retained if not contains_three_term_ap(state.values)
        )
        recursive = tuple(
            state for state in retained if contains_three_term_ap(state.values)
        )
        total_mass = sum((state.weight for state in retained), Fraction())
        terminal_mass = sum((state.weight for state in terminal), Fraction())
        recursive_mass = sum((state.weight for state in recursive), Fraction())
        if terminal_mass + recursive_mass != total_mass:
            raise AssertionError("terminal/recursive policy mass partition failed")
        ratio = recursive_mass / parent_mass

        record = {
            "policy": name,
            "reversed_parents": sorted(reversed_parents),
            "selected_actions": selected_actions,
            "terminal_residual_points": residual_points,
            **metrics,
            "terminal_states": len(terminal),
            "terminal_points": sum(len(state.values) for state in terminal),
            "recursive_states": len(recursive),
            "recursive_points": sum(len(state.values) for state in recursive),
            "total_mass_decimal": decimal_text(total_mass),
            "terminal_mass_decimal": decimal_text(terminal_mass),
            "recursive_mass_decimal": decimal_text(recursive_mass),
            "recursive_ratio_decimal": decimal_text(ratio),
            "recursive_ratio_bracket_millionth": compact_bracket(ratio),
            "total_mass_sha256": fraction_hash(total_mass),
            "terminal_mass_sha256": fraction_hash(terminal_mass),
            "recursive_mass_sha256": fraction_hash(recursive_mass),
            "recursive_ratio_sha256": fraction_hash(ratio),
            "retained_family_sha256": canonical_hash(state_records(retained)),
            "terminal_family_sha256": canonical_hash(state_records(terminal)),
            "recursive_family_sha256": recursive_family_hash(recursive),
            "strict_recursive_contraction": ratio < 1,
        }
        records.append(record)

    baseline = next(row for row in records if row["policy"] == "all_lexicographic")
    if baseline["recursive_family_sha256"] != EXPECTED_BASELINE_RECURSIVE_HASH:
        raise AssertionError("baseline fifth recursive family hash changed")
    if baseline["recursive_ratio_sha256"] != EXPECTED_BASELINE_RATIO_HASH:
        raise AssertionError("baseline fifth recursive ratio hash changed")

    records.sort(
        key=lambda row: (
            Fraction(row["recursive_ratio_bracket_millionth"][0]),
            row["policy"],
        )
    )
    best = records[0]
    contraction_policies = [
        row["policy"] for row in records if row["strict_recursive_contraction"]
    ]
    output = {
        "schema": "fourth_to_fifth_policy_sensitivity_probe_v1",
        "scope": "baseline_all_reverse_and_twelve_single_parent_reverse_flips",
        "parent_policy": "certified_local37_then_lexicographic_through_generation_four",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "fourth_recursive": {
            "states": len(recursive_fourth),
            "points": sum(len(state.values) for state in recursive_fourth),
            "mass_decimal": decimal_text(parent_mass),
            "mass_sha256": fraction_hash(parent_mass),
            "parent_classes": list(parent_indices),
        },
        "policy_count": len(records),
        "contraction_policy_count": len(contraction_policies),
        "contraction_policies": contraction_policies,
        "best_policy": best["policy"],
        "best_recursive_ratio_decimal": best["recursive_ratio_decimal"],
        "best_recursive_ratio_sha256": best["recursive_ratio_sha256"],
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
