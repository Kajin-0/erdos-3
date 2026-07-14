#!/usr/bin/env python3
"""Solve the exact nonnegative retained-feature LP through generation five."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from probe_four_generation_feature_lp import (
    FEATURES,
    compact_record,
    fraction_text,
    primal_lhs,
    solve_square,
)
from probe_generation_aware_feature_profiles import (
    FEATURE_NAMES,
    decimal_text,
    feature_profile,
    fraction_hash,
    point_rows,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

TRANSITIONS5 = (
    "generation2_minus_generation1",
    "generation3_minus_generation2",
    "generation4_minus_generation3",
    "generation5_minus_generation4",
)


def enumerate_primal_vertices5(
    deltas: dict[str, dict[str, Fraction]],
) -> list[dict[str, object]]:
    b = {
        transition: -deltas[transition]["current_mass"]
        for transition in TRANSITIONS5
    }
    candidates: dict[tuple[tuple[str, str], ...], dict[str, object]] = {}
    if all(primal_lhs(deltas, transition, {}) <= 0 for transition in TRANSITIONS5):
        candidates[()] = {
            "support": [],
            "weights": {},
            "slacks": {
                transition: -primal_lhs(deltas, transition, {})
                for transition in TRANSITIONS5
            },
            "active_rows": [],
        }
    for support_size in range(1, 5):
        for support in combinations(FEATURES, support_size):
            for active in combinations(TRANSITIONS5, support_size):
                matrix = [
                    [deltas[transition][feature] for feature in support]
                    for transition in active
                ]
                solution = solve_square(
                    matrix,
                    [b[transition] for transition in active],
                )
                if solution is None or any(value < 0 for value in solution):
                    continue
                weights = dict(zip(support, solution, strict=True))
                lhs = {
                    transition: primal_lhs(deltas, transition, weights)
                    for transition in TRANSITIONS5
                }
                if any(value > 0 for value in lhs.values()):
                    continue
                key = tuple(
                    sorted(
                        (feature, fraction_text(value))
                        for feature, value in weights.items()
                        if value != 0
                    )
                )
                candidates[key] = {
                    "support": [
                        feature for feature, value in weights.items() if value != 0
                    ],
                    "weights": {
                        feature: value
                        for feature, value in weights.items()
                        if value != 0
                    },
                    "slacks": {
                        transition: -value for transition, value in lhs.items()
                    },
                    "active_rows": [
                        transition for transition, value in lhs.items() if value == 0
                    ],
                }
    return list(candidates.values())


def dual_boundaries5(
    deltas: dict[str, dict[str, Fraction]],
) -> list[tuple[str, list[Fraction]]]:
    rows: list[tuple[str, list[Fraction]]] = []
    for index in range(4):
        row = [Fraction() for _ in range(4)]
        row[index] = Fraction(1)
        rows.append((f"y{index + 1}_zero", row))
    for feature in FEATURES:
        rows.append(
            (
                feature + "_zero",
                [deltas[transition][feature] for transition in TRANSITIONS5],
            )
        )
    return rows


def enumerate_dual_vertices5(
    deltas: dict[str, dict[str, Fraction]],
) -> list[dict[str, object]]:
    b = [-deltas[transition]["current_mass"] for transition in TRANSITIONS5]
    boundaries = dual_boundaries5(deltas)
    candidates: dict[tuple[str, ...], dict[str, object]] = {}
    for selected in combinations(boundaries, 3):
        matrix = [[Fraction(1) for _ in range(4)]] + [row for _name, row in selected]
        solution = solve_square(
            matrix,
            [Fraction(1), Fraction(), Fraction(), Fraction()],
        )
        if solution is None or any(value < 0 for value in solution):
            continue
        feature_products = {
            feature: sum(
                solution[index] * deltas[transition][feature]
                for index, transition in enumerate(TRANSITIONS5)
            )
            for feature in FEATURES
        }
        if any(value < 0 for value in feature_products.values()):
            continue
        objective = sum(solution[index] * b[index] for index in range(4))
        key = tuple(fraction_text(value) for value in solution)
        candidates[key] = {
            "y": solution,
            "objective": objective,
            "active_boundaries": [name for name, _row in selected],
            "feature_products": feature_products,
        }
    return list(candidates.values())


def compact_dual5(candidate: dict[str, object]) -> dict[str, object]:
    y = candidate["y"]
    objective = candidate["objective"]
    products = candidate["feature_products"]
    return {
        "y": [fraction_text(value) for value in y],
        "y_decimals": [decimal_text(value) for value in y],
        "y_hashes": [fraction_hash(value) for value in y],
        "objective": fraction_text(objective),
        "objective_decimal": decimal_text(objective),
        "objective_sha256": fraction_hash(objective),
        "active_boundaries": candidate["active_boundaries"],
        "feature_product_decimals": {
            feature: decimal_text(value) for feature, value in products.items()
        },
        "feature_product_hashes": {
            feature: fraction_hash(value) for feature, value in products.items()
        },
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(recursive_second)
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(recursive_third)
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    _occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(recursive_fourth)
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
        "generation4_recursive": recursive_fourth,
        "generation5_recursive": recursive_fifth,
    }
    profiles = {
        name: feature_profile(point_rows(states, generation=index))
        for index, (name, states) in enumerate(families.items(), start=1)
    }
    ordered_names = tuple(families)
    deltas = {
        TRANSITIONS5[index]: {
            feature: profiles[ordered_names[index + 1]][feature]
            - profiles[ordered_names[index]][feature]
            for feature in FEATURE_NAMES
        }
        for index in range(4)
    }

    primal = enumerate_primal_vertices5(deltas)
    primal.sort(
        key=lambda row: (
            len(row["support"]),
            sum(row["weights"].values(), Fraction()),
            tuple(row["support"]),
        )
    )
    dual = enumerate_dual_vertices5(deltas)
    dual.sort(key=lambda row: (row["objective"], tuple(row["y"])))
    best_primal = compact_record(primal[0]) if primal else None
    best_dual = compact_dual5(dual[0]) if dual else None
    infeasibility_certificate = bool(
        not primal and dual and dual[0]["objective"] < 0
    )

    output = {
        "schema": "five_generation_feature_lp_probe_v1",
        "features": list(FEATURES),
        "transitions": list(TRANSITIONS5),
        "family_counts": {
            name: {
                "states": len(states),
                "points": sum(len(state.values) for state in states),
            }
            for name, states in families.items()
        },
        "profile_hashes": {
            name: {
                feature: fraction_hash(value)
                for feature, value in profile.items()
            }
            for name, profile in profiles.items()
        },
        "delta_hashes": {
            name: {
                feature: fraction_hash(value)
                for feature, value in row.items()
            }
            for name, row in deltas.items()
        },
        "primal_basic_feasible_count": len(primal),
        "primal_feasible": bool(primal),
        "best_primal": best_primal,
        "dual_vertex_count": len(dual),
        "best_dual": best_dual,
        "exact_infeasibility_certificate": infeasibility_certificate,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
