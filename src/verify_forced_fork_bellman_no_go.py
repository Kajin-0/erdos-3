#!/usr/bin/env python3
"""Verify that forced-fork mass is not a standalone stored Bellman potential.

Let Psi(S) be the parent-intrinsic forced-fork lower bound and let P be the
certified persistence multiplicity. The Bellman-compatible feature suggested by
raw units is F(S)=P*Psi(S). On the recorded factor-four transition S1 -> S2,
F increases while the transition creates positive debt. Therefore no
nonnegative multiple of F can satisfy the standalone one-child Bellman
inequality on that transition.

The verifier also compares unit transition credit P*Psi with the exact debt on
all recorded factor-four steps through S5.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from certified_contaminated_states import state_by_depth
from verify_forced_fork_reserve_s1_s5 import EXPECTED


FACTOR_BY_PARENT_DEPTH = {
    1: 4,
    2: 8,
    3: 4,
    4: 4,
}

EXPECTED_PARENT_MINUS_CHILD = Fraction(-18_667_522, 146_796_195)
EXPECTED_RATIOS = {
    1: Fraction(105, 8),
    3: Fraction(
        15_368_877_363_127_658_643,
        1_722_549_498_740_988_928,
    ),
    4: Fraction(
        221_024_462_498_552_230_659_735_994_125,
        8_318_654_923_632_839_692_153_748_992,
    ),
}


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def forced_feature(depth: int) -> Fraction:
    state = state_by_depth(depth)
    return state.persistence * EXPECTED[depth]["reserve"]


def factor_four_debt(depth: int) -> Fraction:
    state = state_by_depth(depth)
    factor = FACTOR_BY_PARENT_DEPTH[depth]
    if factor != 4:
        raise ValueError("requested transition is not factor four")
    return (
        Fraction(
            state.persistence * (3 * state.size + 4),
            state.scale,
        )
        * (Fraction(8, factor) - 1)
    )


def build_certificate() -> str:
    parent_feature = forced_feature(1)
    child_feature = forced_feature(2)
    coefficient = parent_feature - child_feature
    debt = factor_four_debt(1)

    if parent_feature != Fraction(2, 21):
        raise AssertionError("S1 forced feature mismatch")
    if child_feature != Fraction(1_554_672, 6_990_295):
        raise AssertionError("S2 forced feature mismatch")
    if coefficient != EXPECTED_PARENT_MINUS_CHILD:
        raise AssertionError("S1-to-S2 feature coefficient mismatch")
    if coefficient >= 0:
        raise AssertionError("expected a negative parent-minus-child coefficient")
    if debt != Fraction(5, 4):
        raise AssertionError("S1-to-S2 debt mismatch")

    ratios: dict[int, Fraction] = {}
    for depth in (1, 3, 4):
        transition_debt = factor_four_debt(depth)
        credit = forced_feature(depth)
        ratio = transition_debt / credit
        ratios[depth] = ratio
        if ratio != EXPECTED_RATIOS[depth]:
            raise AssertionError(f"S{depth} debt-to-credit ratio mismatch")
        if ratio <= 1:
            raise AssertionError(
                f"S{depth}: unit forced-fork credit unexpectedly pays debt"
            )

    lines = [
        "verified: forced-fork stored-potential no-go",
        (
            "verified: unit forced-fork transition credit is insufficient "
            "on every recorded factor-four step through S5"
        ),
        "S1_to_S2_factor=4",
        f"S1_to_S2_bellman_debt={fraction_text(debt)}",
        f"S1_parent_forced_feature={fraction_text(parent_feature)}",
        f"S2_child_forced_feature={fraction_text(child_feature)}",
        f"S1_parent_minus_child={fraction_text(coefficient)}",
        (
            "S1_to_S2_debt_to_parent_credit="
            + fraction_text(ratios[1])
        ),
        (
            "S3_to_S4_debt_to_parent_credit="
            + fraction_text(ratios[3])
        ),
        (
            "S4_to_S5_debt_to_parent_credit="
            + fraction_text(ratios[4])
        ),
        (
            "conclusion: no nonnegative multiple of P*Psi can serve as a "
            "standalone stored Bellman potential on the recorded "
            "S1-to-S2 transition."
        ),
        (
            "conclusion: forced-fork mass remains usable only as a "
            "transition charge or as one component of a larger "
            "obstruction/packing potential."
        ),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_forced_fork_bellman_no_go.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: forced-fork Bellman no-go")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
