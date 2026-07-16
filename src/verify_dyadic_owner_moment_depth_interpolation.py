#!/usr/bin/env python3
"""Verify the exact p0 dyadic owner-moment/depth interpolation algebra."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def main() -> int:
    # At p0=log_2(5/2), q=2^{-p0}=2/5.
    q = Fraction(2, 5)
    moment_coefficient = Fraction(1, q)  # 5/2
    depth_coefficient = 1 - q  # 3/5

    rows = []
    for scale_drop in range(1, 65):
        excess_depth = scale_drop - 1
        moment_term = q ** excess_depth
        depth_term = depth_coefficient * excess_depth
        total = moment_term + depth_term
        if total < 1:
            raise AssertionError(
                f"interpolation failed at drop {scale_drop}: {total}"
            )
        rows.append(
            {
                "scale_drop": scale_drop,
                "moment_term": str(moment_term),
                "depth_term": str(depth_term),
                "total": str(total),
                "equality": total == 1,
            }
        )

    equality_drops = [
        row["scale_drop"] for row in rows if row["equality"]
    ]
    if equality_drops != [1, 2]:
        raise AssertionError("interpolation equality cases changed")

    first_appearance_moment = Fraction(17, 25)
    first_appearance_excess_depth = Fraction(3, 1)
    first_appearance_raw = (
        moment_coefficient * first_appearance_moment
        + depth_coefficient * first_appearance_excess_depth
    )
    if first_appearance_raw != Fraction(7, 2):
        raise AssertionError("first-appearance interpolation identity changed")

    payload = {
        "schema": "dyadic_owner_moment_depth_interpolation_v1",
        "boundary_exponent": "log_2(5/2)",
        "q_two_to_minus_p0": str(q),
        "moment_coefficient": str(moment_coefficient),
        "excess_depth_coefficient": str(depth_coefficient),
        "verified_scale_drops": [1, 64],
        "equality_scale_drops": equality_drops,
        "first_appearance_identity": {
            "normalized_moment": str(first_appearance_moment),
            "excess_depth": str(first_appearance_excess_depth),
            "reconstructed_raw_mass": str(first_appearance_raw),
        },
        "checks": {
            "dyadic_interpolation_nonnegative_slack": True,
            "equality_only_at_first_two_levels": True,
            "virtual_first_appearance_exact": True,
        },
        "rows_sha256": hashlib.sha256(
            json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
