#!/usr/bin/env python3
"""Verify a no-go result for three naive nonnegative reserve coordinates.

The recorded factor-four transition S_6 -> S_7 increases all three coordinates:
weighted density, right-shell slack, and incoming contamination mass. Therefore
no nonnegative linear combination of those coordinates can pay the strictly
positive factor-four Bellman debt on this transition.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from certified_contaminated_states import state_by_depth


def q(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def build_certificate() -> str:
    parent = state_by_depth(6)
    child = state_by_depth(7)

    if child.incoming_factor != 4:
        raise AssertionError("S6 -> S7 is not the recorded factor-four step")
    if child.incoming_contamination != 2:
        raise AssertionError("unexpected S7 contamination")

    debt = Fraction(
        parent.persistence * (3 * parent.size + 4),
        parent.scale,
    )
    if debt != Fraction(9_841, 4_096):
        raise AssertionError("factor-four Bellman debt mismatch")

    differences = {
        "weighted_density": (
            parent.weighted_density - child.weighted_density
        ),
        "right_shell_slack": (
            parent.right_shell_slack - child.right_shell_slack
        ),
        "incoming_contamination_mass": (
            parent.incoming_contamination_mass
            - child.incoming_contamination_mass
        ),
    }
    expected = {
        "weighted_density": Fraction(-1_641, 4_096),
        "right_shell_slack": Fraction(-52_437, 8_192),
        "incoming_contamination_mass": Fraction(-1, 4_096),
    }
    if differences != expected:
        raise AssertionError(f"coordinate differences mismatch: {differences}")
    if not all(value < 0 for value in differences.values()):
        raise AssertionError("every naive coordinate must increase")

    lines = [
        "NAIVE RESERVE COORDINATE NO-GO",
        "",
        "transition=S6_to_S7",
        "factor=4",
        f"parent_scale={parent.scale}",
        f"parent_size={parent.size}",
        f"parent_persistence={parent.persistence}",
        f"child_scale={child.scale}",
        f"child_size={child.size}",
        f"child_persistence={child.persistence}",
        f"bellman_debt={q(debt)}",
    ]
    for name, value in differences.items():
        lines.append(f"parent_minus_child_{name}={q(value)}")
    lines.extend(
        [
            "",
            "For nonnegative weights a,b,c:",
            (
                "Phi=a*weighted_density+b*right_shell_slack+"
                "c*incoming_contamination_mass"
            ),
            "Phi(S6)-Phi(S7)<=0",
            f"required_drop={q(debt)}>0",
            (
                "conclusion=no_nonnegative_linear_combination_"
                "can_pay_this_step"
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_naive_reserve_no_go.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: naive reserve coordinate no-go at S6 -> S7")
    print("bellman_debt=9841/4096")
    print("weighted_density_drop=-1641/4096")
    print("right_shell_slack_drop=-52437/8192")
    print("incoming_contamination_mass_drop=-1/4096")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
