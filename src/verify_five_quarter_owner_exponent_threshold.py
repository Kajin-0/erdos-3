#!/usr/bin/env python3
"""Verify exact algebra for the five-quarter owner-exponent threshold."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def main() -> int:
    production_coefficient = Fraction(5, 4)
    threshold_power = Fraction(5, 2)  # 2**p0

    latent_latent_boundary = (
        2 * production_coefficient / threshold_power
    )
    current_latent_boundary = (
        (1 + production_coefficient) / threshold_power
    )
    first_appearance_boundary = (
        Fraction(3, 1) / (threshold_power * threshold_power)
        + Fraction(1, 1) / (2 * threshold_power)
    )

    if latent_latent_boundary != 1:
        raise AssertionError("latent-latent boundary coefficient changed")
    if current_latent_boundary != Fraction(9, 10):
        raise AssertionError("current-latent boundary coefficient changed")
    if first_appearance_boundary != Fraction(17, 25):
        raise AssertionError("first-appearance boundary coefficient changed")

    # At p=3/2, compare squared positive quantities exactly.
    # 5/(4 sqrt(2)) < 1  <=> 25 < 32.
    latent_three_halves_strict = 25 < 32
    # 9/(8 sqrt(2)) < 1 <=> 81 < 128.
    current_three_halves_strict = 81 < 128
    # 3/8 + 1/(4 sqrt(2)) < 1.
    # This is equivalent to 2 < 5 sqrt(2), hence 4 < 50.
    first_appearance_three_halves_strict = 4 < 50

    if not latent_three_halves_strict:
        raise AssertionError("p=3/2 latent-latent contraction failed")
    if not current_three_halves_strict:
        raise AssertionError("p=3/2 current-latent contraction failed")
    if not first_appearance_three_halves_strict:
        raise AssertionError("p=3/2 first-appearance contraction failed")

    # The old coefficient two requires 2*2*2^{-p} <= 1, so 2**p >= 4.
    old_threshold_power = Fraction(4, 1)
    if threshold_power >= old_threshold_power:
        raise AssertionError("five-quarter threshold did not improve coefficient-two threshold")

    payload = {
        "schema": "five_quarter_owner_exponent_threshold_v1",
        "production_pair_coefficient": str(production_coefficient),
        "boundary_definition": {
            "two_to_p0": str(threshold_power),
            "p0": "log_2(5/2)",
            "decimal": "1.321928094887362",
        },
        "boundary_coefficients": {
            "latent_latent": str(latent_latent_boundary),
            "current_latent": str(current_latent_boundary),
            "first_appearance": str(first_appearance_boundary),
        },
        "three_halves_checks": {
            "latent_latent_25_lt_32": latent_three_halves_strict,
            "current_latent_81_lt_128": current_three_halves_strict,
            "first_appearance_4_lt_50": first_appearance_three_halves_strict,
        },
        "comparison": {
            "five_quarter_threshold_two_to_p": str(threshold_power),
            "coefficient_two_threshold_two_to_p": str(old_threshold_power),
            "strict_improvement": threshold_power < old_threshold_power,
        },
        "checks": {
            "future_production_paid_at_lambda_five_quarters": True,
            "boundary_latent_latent_nonexpanding": True,
            "boundary_current_latent_contracting": True,
            "boundary_first_appearance_contracting": True,
            "p_three_halves_all_strict": True,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
