#!/usr/bin/env python3
"""Probe a shell-valid candidate attaining the latent-latent critical coefficient."""
from __future__ import annotations

import hashlib
import json

from probe_critical_fractional_reserve_flow import profile
from search_lexicographic_reserve_pseudoforest_small_box import contains_four_ap


def main() -> int:
    parent = (
        65,
        81,
        82,
        83,
        97,
        98,
        99,
        103,
        104,
        105,
        109,
        110,
        111,
    )
    if contains_four_ap(parent):
        raise AssertionError("sharp latent-latent candidate contains a four-AP")

    result = profile("sharp_latent_latent_candidate", parent)
    output = {
        "schema": "sharp_latent_latent_critical_candidate_v1",
        "profile": result,
        "checks": {
            "parent_four_ap_free": True,
            "parent_inside_standard_shell_64": result["parent_base"] == 64,
            "candidate_attains_half_residual": (
                result["masses"]["fixed_excess"] == "0"
                and result["ratios"]["unallocated_flexible_demand"] == "3/2"
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
