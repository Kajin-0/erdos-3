#!/usr/bin/env python3
"""Certify the exact four-generation retained-feature LP and H+74R witness."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from probe_four_generation_feature_lp import (
    FEATURES,
    TRANSITIONS,
    enumerate_primal_vertices,
)
from probe_generation_aware_feature_profiles import (
    feature_profile,
    fraction_hash,
    point_rows,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_SOURCE_HASHES = {
    "generation1_retained": {
        "current_mass": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
        "root_repeat_descendant_mass": "543d8bd71c223f034a1c2e02636888caa509e72203d9199a0ca982aad096b975",
    },
    "generation2_recursive": {
        "current_mass": "539dfbe1e345d4e6f1e0ed1c08cfedd1eba8c3f9d195fc078ae9ac0d5e391775",
        "root_repeat_descendant_mass": "b990ee4d972d408a1775b2e62adc5c1e58d3d8737b7486a8a92a00d376bda690",
    },
    "generation3_recursive": {
        "current_mass": "ea01006a6cee2ea0c2cb23704e253b5871c528357b3698b4ca2076ddc7233210",
        "root_repeat_descendant_mass": "66810024432052aa1d66120407feeeca0f551553805400f6f9a0910b81a963b9",
    },
    "generation4_recursive": {
        "current_mass": "03cac9573c3d61ac9c8a0c4066cbb8d6ea9ece01606602cacc9604634f9b1ba9",
        "root_repeat_descendant_mass": "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6",
    },
}
EXPECTED_MINIMUM_COEFFICIENT_HASH = (
    "5b7cef5910cb64ec02a096277bc05ec406f32630e1719132147babbe1e950327"
)
CERTIFICATE_SHA256 = (
    "33ea9fe812714f0e5a51d0d6301c1b7bbf3a981ca13ebf7ac256302ea5153b3c"
)


def assert_between(value: Fraction, lower: Fraction, upper: Fraction, name: str) -> None:
    if not lower < value < upper:
        raise AssertionError(f"{name} outside exact bracket: {value}")


def build_certificate() -> str:
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
    for family, expected in EXPECTED_SOURCE_HASHES.items():
        for feature, expected_hash in expected.items():
            observed = fraction_hash(profiles[family][feature])
            if observed != expected_hash:
                raise AssertionError(f"{family}.{feature} hash mismatch: {observed}")

    deltas = {
        "generation2_minus_generation1": {
            feature: profiles["generation2_recursive"][feature]
            - profiles["generation1_retained"][feature]
            for feature in ("current_mass",) + FEATURES
        },
        "generation3_minus_generation2": {
            feature: profiles["generation3_recursive"][feature]
            - profiles["generation2_recursive"][feature]
            for feature in ("current_mass",) + FEATURES
        },
        "generation4_minus_generation3": {
            feature: profiles["generation4_recursive"][feature]
            - profiles["generation3_recursive"][feature]
            for feature in ("current_mass",) + FEATURES
        },
    }
    vertices = enumerate_primal_vertices(deltas)
    vertices.sort(
        key=lambda row: (
            len(row["support"]),
            sum(row["weights"].values(), Fraction()),
            tuple(row["support"]),
        )
    )
    if len(vertices) != 18:
        raise AssertionError(f"basic-feasible count mismatch: {len(vertices)}")
    best = vertices[0]
    if best["support"] != ["root_repeat_descendant_mass"]:
        raise AssertionError(f"unexpected sparsest support: {best['support']!r}")
    threshold = best["weights"]["root_repeat_descendant_mass"]
    if fraction_hash(threshold) != EXPECTED_MINIMUM_COEFFICIENT_HASH:
        raise AssertionError("minimum coefficient hash mismatch")
    assert_between(threshold, Fraction(73_015, 1_000), Fraction(9_127, 125), "minimum coefficient")
    if best["active_rows"] != ["generation4_minus_generation3"]:
        raise AssertionError(f"active-row mismatch: {best['active_rows']!r}")

    coefficient = Fraction(74)
    potentials = {
        name: profile["current_mass"]
        + coefficient * profile["root_repeat_descendant_mass"]
        for name, profile in profiles.items()
    }
    ratios = {
        "generation2_over_generation1": (
            potentials["generation2_recursive"] / potentials["generation1_retained"]
        ),
        "generation3_over_generation2": (
            potentials["generation3_recursive"] / potentials["generation2_recursive"]
        ),
        "generation4_over_generation3": (
            potentials["generation4_recursive"] / potentials["generation3_recursive"]
        ),
    }
    margins = {name: Fraction(1) - value for name, value in ratios.items()}
    assert_between(
        ratios["generation2_over_generation1"],
        Fraction(618_519, 1_000_000),
        Fraction(15_463, 25_000),
        "ratio12",
    )
    assert_between(
        ratios["generation3_over_generation2"],
        Fraction(122_393, 1_000_000),
        Fraction(61_197, 500_000),
        "ratio23",
    )
    assert_between(
        ratios["generation4_over_generation3"],
        Fraction(991_321, 1_000_000),
        Fraction(495_661, 500_000),
        "ratio34",
    )
    assert_between(margins["generation2_over_generation1"], Fraction(381_480, 1_000_000), Fraction(381_481, 1_000_000), "margin12")
    assert_between(margins["generation3_over_generation2"], Fraction(877_606, 1_000_000), Fraction(877_607, 1_000_000), "margin23")
    assert_between(margins["generation4_over_generation3"], Fraction(8_678, 1_000_000), Fraction(8_679, 1_000_000), "margin34")

    lines = [
        "FOUR-GENERATION RETAINED FEATURE LP",
        "",
        "policy=local37_then_lexicographic_recursive_only",
        "retention=global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "current_harmonic_weight=1",
        "tested_nonnegative_features=11",
        "recursive_transitions=3",
        "",
        "generation1_retained_states=21",
        "generation1_retained_points=11753",
        "generation2_recursive_states=14",
        "generation2_recursive_points=7882",
        "generation3_recursive_states=14",
        "generation3_recursive_points=4789",
        "generation4_recursive_states=12",
        "generation4_recursive_points=1717",
        "",
        "basic_feasible_vertices=18",
        "primal_feasible=True",
        "exact_infeasibility_certificate=False",
        "sparsest_support=root_repeat_descendant_mass",
        "active_constraint=generation4_minus_generation3",
        "minimum_coefficient_bracket=73015/1000,9127/125",
        f"minimum_coefficient_sha256={EXPECTED_MINIMUM_COEFFICIENT_HASH}",
        "",
        "integer_witness_coefficient=74",
        "integer_witness=Phi_g=H_g+74*R_g",
        "ratio_generation2_over_generation1_bracket=618519/1000000,15463/25000",
        "ratio_generation3_over_generation2_bracket=122393/1000000,61197/500000",
        "ratio_generation4_over_generation3_bracket=991321/1000000,495661/500000",
        "margin_generation2_bracket=381480/1000000,381481/1000000",
        "margin_generation3_bracket=877606/1000000,877607/1000000",
        "margin_generation4_bracket=8678/1000000,8679/1000000",
        "strictly_contracts_all_three_transitions=True",
        "",
        "conclusion: the exact eleven-feature cone is feasible through generation four.",
        "A single repeated-root descendant-mass coordinate suffices, but only with coefficient above 73.015.",
        "The clean integer witness H+74R contracts on every recorded recursive transition.",
        "This is a fixed-policy, fixed-retention four-generation theorem, not a universal Bellman potential.",
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_four_generation_feature_lp.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
