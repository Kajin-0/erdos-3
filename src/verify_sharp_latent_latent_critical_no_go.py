#!/usr/bin/env python3
"""Verify sharp half-scale middle output and unit latent-latent residual."""
from __future__ import annotations

import hashlib
import json

from probe_critical_fractional_reserve_flow import profile
from search_lexicographic_reserve_pseudoforest_small_box import contains_four_ap


def main() -> int:
    parent = (
        65,
        67,
        68,
        69,
        99,
        100,
        101,
        105,
        106,
        107,
        111,
        112,
        113,
    )
    if contains_four_ap(parent):
        raise AssertionError("sharp latent-latent parent contains a four-AP")

    result = profile("sharp_latent_latent_critical_no_go", parent)
    if result["parent_base"] != 64:
        raise AssertionError("sharp latent-latent parent shell changed")
    if int(result["counts"]["latent_latent_resources"]) != 3:
        raise AssertionError("sharp latent-latent resource count changed")
    if result["ratios"]["total_flexible_demand"] != "6":
        raise AssertionError("sharp total latent demand changed")
    if result["ratios"]["assigned_flexible_demand"] != "3":
        raise AssertionError("sharp assigned latent demand changed")
    if result["ratios"]["unallocated_flexible_demand"] != "3":
        raise AssertionError("sharp unallocated latent demand changed")

    duplicated = [
        row for row in result["demands"]
        if int(row["latent_owners"]) == 2
    ]
    if len(duplicated) != 3:
        raise AssertionError("sharp duplicated demand rows changed")
    for row in duplicated:
        if (
            row["ratio"] != "2"
            or row["assigned_ratio"] != "1"
            or row["unassigned_ratio"] != "1"
            or int(row["middle_scale"]) != 32
        ):
            raise AssertionError(f"sharp duplicated demand changed: {row}")

    output = {
        "schema": "sharp_latent_latent_critical_no_go_v1",
        "parent": parent,
        "profile": result,
        "checks": {
            "parent_four_ap_free": True,
            "actual_lexicographic_retained_policy": True,
            "middle_shell_reaches_parent_half_scale": True,
            "latent_latent_residual_coefficient_one_attained": True,
            "joint_natural_center_opposite_assignment_insufficient": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
