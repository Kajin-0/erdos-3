#!/usr/bin/env python3
"""Test minimum-anchor translation reserve through five retained levels.

For a finite state S with m=min(S), define the prospective full-backbone
translation reserve

    A(S) = sum_{u in S, u>m} (1/(u-m) - 1/u).

This is not an arbitrary fitted feature: it is exactly the harmonic gain from
translating every nonminimum point by the minimum anchor.  The probe tests
whether one fixed nonnegative coefficient kappa makes

    H(F_g) + kappa A(F_g)

nonincreasing on the four already certified recursive transitions.  It does
not propagate generation six.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_root_lineage_transfer_classification import (
    canonical_hash,
    harmonic,
    serialize_mass,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def translation_reserve(values: tuple[int, ...]) -> Fraction:
    minimum = min(values)
    return sum(
        (
            Fraction(1, value - minimum) - Fraction(1, value)
            for value in values
            if value > minimum
        ),
        Fraction(),
    )


def generation_record(name: str, states: tuple[object, ...]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    total_harmonic = Fraction()
    total_reserve = Fraction()
    total_anchor_release = Fraction()
    for state in sorted(states, key=lambda item: item.index):
        values = tuple(state.values)
        minimum = min(values)
        harmonic_mass = harmonic(values)
        reserve = translation_reserve(values)
        anchor_release = Fraction(1, minimum)
        total_harmonic += harmonic_mass
        total_reserve += reserve
        total_anchor_release += anchor_release
        rows.append(
            {
                "state_class": state.index,
                "representative": state.representative.index,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "exponent": state.representative.exponent,
                "size": len(values),
                "minimum": minimum,
                "harmonic_mass": serialize_mass(harmonic_mass),
                "translation_reserve": serialize_mass(reserve),
                "anchor_release": serialize_mass(anchor_release),
                "reserve_over_anchor_release": serialize_mass(
                    reserve / anchor_release
                ),
            }
        )
    return {
        "name": name,
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "harmonic_mass": serialize_mass(total_harmonic),
        "translation_reserve": serialize_mass(total_reserve),
        "anchor_release": serialize_mass(total_anchor_release),
        "h_plus_a": serialize_mass(total_harmonic + total_reserve),
        "reserve_over_harmonic": serialize_mass(
            total_reserve / total_harmonic
        ),
        "reserve_over_anchor_release": serialize_mass(
            total_reserve / total_anchor_release
        ),
        "state_rows_sha256": canonical_hash(rows),
        "state_rows": rows,
    }


def rational_bound(value: Fraction | None) -> dict[str, str] | None:
    return None if value is None else serialize_mass(value)


def coefficient_interval(
    generations: list[dict[str, object]],
) -> tuple[dict[str, object], list[dict[str, object]]]:
    lower = Fraction()
    upper: Fraction | None = None
    feasible = True
    constraints: list[dict[str, object]] = []

    for current, following in zip(generations, generations[1:], strict=True):
        current_h = Fraction(current["harmonic_mass"]["fraction"])
        next_h = Fraction(following["harmonic_mass"]["fraction"])
        current_a = Fraction(current["translation_reserve"]["fraction"])
        next_a = Fraction(following["translation_reserve"]["fraction"])
        delta_h = next_h - current_h
        delta_a = next_a - current_a

        relation: str
        bound: Fraction | None
        if delta_a < 0:
            relation = "kappa_at_least"
            bound = delta_h / (-delta_a)
            effective = max(Fraction(), bound)
            lower = max(lower, effective)
        elif delta_a > 0:
            relation = "kappa_at_most"
            bound = -delta_h / delta_a
            if upper is None or bound < upper:
                upper = bound
            if bound < 0:
                feasible = False
        else:
            relation = "constant"
            bound = None
            if delta_h > 0:
                feasible = False

        constraints.append(
            {
                "transition": f"{current['name']}->{following['name']}",
                "delta_h": serialize_mass(delta_h),
                "delta_a": serialize_mass(delta_a),
                "relation": relation,
                "bound": rational_bound(bound),
            }
        )

    if upper is not None and lower > upper:
        feasible = False

    witness: Fraction | None = None
    if feasible:
        witness = lower
        if upper is not None and witness > upper:
            witness = None
            feasible = False

    return (
        {
            "feasible": feasible,
            "lower": rational_bound(lower),
            "upper": rational_bound(upper),
            "witness": rational_bound(witness),
        },
        constraints,
    )


def potential_transition(
    current: dict[str, object],
    following: dict[str, object],
    kappa: Fraction,
) -> dict[str, object]:
    current_value = Fraction(current["harmonic_mass"]["fraction"]) + kappa * Fraction(
        current["translation_reserve"]["fraction"]
    )
    next_value = Fraction(following["harmonic_mass"]["fraction"]) + kappa * Fraction(
        following["translation_reserve"]["fraction"]
    )
    return {
        "transition": f"{current['name']}->{following['name']}",
        "current": serialize_mass(current_value),
        "next": serialize_mass(next_value),
        "delta": serialize_mass(next_value - current_value),
        "ratio": serialize_mass(next_value / current_value),
        "contracts": next_value <= current_value,
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_first = tuple(
        state for state in retained_first if contains_three_term_ap(state.values)
    )
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
    _occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    families = [
        ("R1", recursive_first),
        ("R2", recursive_second),
        ("R3", recursive_third),
        ("R4", recursive_fourth),
        ("R5", recursive_fifth),
    ]
    generations = [
        generation_record(name, states) for name, states in families
    ]
    interval, constraints = coefficient_interval(generations)

    natural_kappa = Fraction(1)
    natural_rows = [
        potential_transition(current, following, natural_kappa)
        for current, following in zip(generations, generations[1:], strict=True)
    ]
    witness_rows: list[dict[str, object]] | None = None
    if interval["feasible"] and interval["witness"] is not None:
        witness = Fraction(interval["witness"]["fraction"])
        witness_rows = [
            potential_transition(current, following, witness)
            for current, following in zip(generations, generations[1:], strict=True)
        ]

    compact_generations = [
        {
            key: generation[key]
            for key in (
                "name",
                "states",
                "points",
                "harmonic_mass",
                "translation_reserve",
                "anchor_release",
                "h_plus_a",
                "reserve_over_harmonic",
                "reserve_over_anchor_release",
                "state_rows_sha256",
            )
        }
        for generation in generations
    ]
    output = {
        "schema": "anchor_translation_potential_probe_v1",
        "scope": "certified_recursive_families_R1_through_R5",
        "definition": "A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)",
        "generation_six_propagated": False,
        "generations": compact_generations,
        "constraints": constraints,
        "coefficient_interval": interval,
        "natural_kappa_one": {
            "contracts_all_transitions": all(
                bool(row["contracts"]) for row in natural_rows
            ),
            "transitions": natural_rows,
        },
        "witness_transitions": witness_rows,
        "hashes": {
            "generation_records": canonical_hash(compact_generations),
            "constraints": canonical_hash(constraints),
            "natural_kappa_one": canonical_hash(natural_rows),
            "state_rows": canonical_hash(
                [
                    {
                        "name": generation["name"],
                        "state_rows_sha256": generation["state_rows_sha256"],
                    }
                    for generation in generations
                ]
            ),
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
