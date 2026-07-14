#!/usr/bin/env python3
"""Solve the exact nonnegative retained-feature LP through generation four."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from probe_fourth_generation_potential_frontier import potential_quantities
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

FEATURES = tuple(feature for feature in FEATURE_NAMES if feature != "current_mass")
TRANSITIONS = (
    "generation2_minus_generation1",
    "generation3_minus_generation2",
    "generation4_minus_generation3",
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def solve_square(
    matrix: list[list[Fraction]],
    rhs: list[Fraction],
) -> list[Fraction] | None:
    size = len(matrix)
    augmented = [list(row) + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            return None
        if pivot != column:
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                augmented[row][index] - factor * augmented[column][index]
                for index in range(size + 1)
            ]
    return [augmented[index][-1] for index in range(size)]


def primal_lhs(
    deltas: dict[str, dict[str, Fraction]],
    transition: str,
    weights: dict[str, Fraction],
) -> Fraction:
    return deltas[transition]["current_mass"] + sum(
        deltas[transition][feature] * weights.get(feature, Fraction())
        for feature in FEATURES
    )


def enumerate_primal_vertices(
    deltas: dict[str, dict[str, Fraction]],
) -> list[dict[str, object]]:
    b = {
        transition: -deltas[transition]["current_mass"]
        for transition in TRANSITIONS
    }
    candidates: dict[tuple[tuple[str, str], ...], dict[str, object]] = {}
    if all(primal_lhs(deltas, transition, {}) <= 0 for transition in TRANSITIONS):
        candidates[()] = {
            "support": [],
            "weights": {},
            "slacks": {
                transition: -primal_lhs(deltas, transition, {})
                for transition in TRANSITIONS
            },
        }
    for support_size in range(1, 4):
        for support in combinations(FEATURES, support_size):
            for active in combinations(TRANSITIONS, support_size):
                matrix = [
                    [deltas[transition][feature] for feature in support]
                    for transition in active
                ]
                solution = solve_square(matrix, [b[transition] for transition in active])
                if solution is None or any(value < 0 for value in solution):
                    continue
                weights = dict(zip(support, solution, strict=True))
                lhs = {
                    transition: primal_lhs(deltas, transition, weights)
                    for transition in TRANSITIONS
                }
                if any(value > 0 for value in lhs.values()):
                    continue
                key = tuple(sorted((feature, fraction_text(value)) for feature, value in weights.items() if value != 0))
                candidates[key] = {
                    "support": [feature for feature, value in weights.items() if value != 0],
                    "weights": {
                        feature: value for feature, value in weights.items() if value != 0
                    },
                    "slacks": {transition: -value for transition, value in lhs.items()},
                    "active_rows": [
                        transition for transition, value in lhs.items() if value == 0
                    ],
                }
    return list(candidates.values())


def dual_boundary_rows(
    deltas: dict[str, dict[str, Fraction]],
) -> list[tuple[str, list[Fraction]]]:
    rows = [
        ("y1_zero", [Fraction(1), Fraction(), Fraction()]),
        ("y2_zero", [Fraction(), Fraction(1), Fraction()]),
        ("y3_zero", [Fraction(), Fraction(), Fraction(1)]),
    ]
    for feature in FEATURES:
        rows.append(
            (
                feature + "_zero",
                [deltas[transition][feature] for transition in TRANSITIONS],
            )
        )
    return rows


def enumerate_dual_vertices(
    deltas: dict[str, dict[str, Fraction]],
) -> list[dict[str, object]]:
    b = [-deltas[transition]["current_mass"] for transition in TRANSITIONS]
    boundaries = dual_boundary_rows(deltas)
    candidates: dict[tuple[str, str, str], dict[str, object]] = {}
    for (name_left, row_left), (name_right, row_right) in combinations(boundaries, 2):
        matrix = [
            [Fraction(1), Fraction(1), Fraction(1)],
            row_left,
            row_right,
        ]
        solution = solve_square(matrix, [Fraction(1), Fraction(), Fraction()])
        if solution is None or any(value < 0 for value in solution):
            continue
        feature_products = {
            feature: sum(
                solution[index] * deltas[transition][feature]
                for index, transition in enumerate(TRANSITIONS)
            )
            for feature in FEATURES
        }
        if any(value < 0 for value in feature_products.values()):
            continue
        objective = sum(solution[index] * b[index] for index in range(3))
        key = tuple(fraction_text(value) for value in solution)
        candidates[key] = {
            "y": solution,
            "objective": objective,
            "active_boundaries": [name_left, name_right],
            "feature_products": feature_products,
        }
    return list(candidates.values())


def compact_record(candidate: dict[str, object]) -> dict[str, object]:
    weights = candidate["weights"]
    slacks = candidate["slacks"]
    return {
        "support": candidate["support"],
        "weights": {name: fraction_text(value) for name, value in weights.items()},
        "weight_decimals": {name: decimal_text(value) for name, value in weights.items()},
        "weight_hashes": {name: fraction_hash(value) for name, value in weights.items()},
        "slacks": {name: fraction_text(value) for name, value in slacks.items()},
        "slack_decimals": {name: decimal_text(value) for name, value in slacks.items()},
        "slack_hashes": {name: fraction_hash(value) for name, value in slacks.items()},
        "active_rows": candidate.get("active_rows", []),
    }


def compact_dual(candidate: dict[str, object]) -> dict[str, object]:
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
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences3, retained_third, _metrics3, _child_rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )
    _occurrences4, retained_fourth, _metrics4, _child_rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth
        if contains_three_term_ap(state.values)
    )

    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
        "generation4_recursive": recursive_fourth,
    }
    profiles = {
        name: feature_profile(point_rows(states, generation=index))
        for index, (name, states) in enumerate(families.items(), start=1)
    }
    deltas = {
        "generation2_minus_generation1": {
            feature: profiles["generation2_recursive"][feature]
            - profiles["generation1_retained"][feature]
            for feature in FEATURE_NAMES
        },
        "generation3_minus_generation2": {
            feature: profiles["generation3_recursive"][feature]
            - profiles["generation2_recursive"][feature]
            for feature in FEATURE_NAMES
        },
        "generation4_minus_generation3": {
            feature: profiles["generation4_recursive"][feature]
            - profiles["generation3_recursive"][feature]
            for feature in FEATURE_NAMES
        },
    }

    primal = enumerate_primal_vertices(deltas)
    primal.sort(
        key=lambda row: (
            len(row["support"]),
            sum(row["weights"].values(), Fraction()),
            tuple(row["support"]),
        )
    )
    dual = enumerate_dual_vertices(deltas)
    dual.sort(key=lambda row: (row["objective"], tuple(row["y"])))
    best_primal = compact_record(primal[0]) if primal else None
    best_dual = compact_dual(dual[0]) if dual else None

    infeasibility_certificate = bool(
        not primal and dual and dual[0]["objective"] < 0
    )
    output = {
        "schema": "four_generation_feature_lp_probe_v1",
        "features": list(FEATURES),
        "transitions": list(TRANSITIONS),
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
