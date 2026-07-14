#!/usr/bin/env python3
"""Probe two simple integer-weight generation-aware retained potentials."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_generation_aware_feature_profiles import (
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

CANDIDATES = {
    "root_repeat_descendant_weight_2": {
        "feature": "root_repeat_descendant_mass",
        "coefficient": 2,
    },
    "immediate_tail_ge4_weight_4": {
        "feature": "immediate_tail_ge4_descendant_mass",
        "coefficient": 4,
    },
}


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def compact_bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = (value.numerator * denominator) // value.denominator
    lower = Fraction(lower_numerator, denominator)
    upper = Fraction(lower_numerator + 1, denominator)
    return [fraction_text(lower), fraction_text(upper)]


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences, retained_third, _metrics, _child_rows = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )
    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
    }
    profiles = {
        name: feature_profile(point_rows(states, generation=index))
        for index, (name, states) in enumerate(families.items(), start=1)
    }

    results: dict[str, object] = {}
    for name, spec in CANDIDATES.items():
        feature = str(spec["feature"])
        coefficient = int(spec["coefficient"])
        values = {
            generation: profile["current_mass"]
            + coefficient * profile[feature]
            for generation, profile in profiles.items()
        }
        delta12 = values["generation2_recursive"] - values["generation1_retained"]
        delta23 = values["generation3_recursive"] - values["generation2_recursive"]
        ratio12 = values["generation2_recursive"] / values["generation1_retained"]
        ratio23 = values["generation3_recursive"] / values["generation2_recursive"]
        ratio13 = values["generation3_recursive"] / values["generation1_retained"]
        margin12 = 1 - ratio12
        margin23 = 1 - ratio23
        if delta12 >= 0 or delta23 >= 0:
            raise AssertionError(f"candidate {name} is not strictly decreasing")
        quantities = {
            "generation1": values["generation1_retained"],
            "generation2": values["generation2_recursive"],
            "generation3": values["generation3_recursive"],
            "delta12": delta12,
            "delta23": delta23,
            "ratio12": ratio12,
            "ratio23": ratio23,
            "ratio13": ratio13,
            "margin12": margin12,
            "margin23": margin23,
        }
        results[name] = {
            "feature": feature,
            "coefficient": coefficient,
            "strictly_decreasing": True,
            "decimals": {
                key: decimal_text(value) for key, value in quantities.items()
            },
            "sha256": {
                key: fraction_hash(value) for key, value in quantities.items()
            },
            "ratio_brackets_millionth": {
                key: compact_bracket(quantities[key])
                for key in ("ratio12", "ratio23", "ratio13", "margin12", "margin23")
            },
        }

    output = {
        "schema": "candidate_generation_potentials_probe_v1",
        "family_counts": {
            name: {
                "states": len(states),
                "points": sum(len(state.values) for state in states),
            }
            for name, states in families.items()
        },
        "candidates": results,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
