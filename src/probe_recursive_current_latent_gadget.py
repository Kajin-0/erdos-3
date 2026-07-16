#!/usr/bin/env python3
"""Verify a shell-valid recursive current-latent critical no-go gadget."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json

from search_lexicographic_reserve_pseudoforest_small_box import contains_four_ap
from search_recursive_current_latent_small_box import parent_profile


def shell_base(values: tuple[int, ...]) -> int:
    base = 1 << (min(values).bit_length() - 1)
    if any(value < base or value >= 2 * base for value in values):
        raise AssertionError(f"values cross standard shell: {values}")
    return base


def main() -> int:
    parent = (
        65,
        97,
        98,
        99,
        113,
        114,
        115,
        119,
        120,
        121,
        125,
        126,
        127,
    )
    if contains_four_ap(parent):
        raise AssertionError("recursive current-latent gadget contains a four-AP")
    parent_base = shell_base(parent)
    if parent_base != 64:
        raise AssertionError("recursive current-latent parent shell changed")

    profile = parent_profile(parent)
    expected_states = (
        (126, (127,), (1,), "middle_fiber", True),
        (97, (113, 119, 125), (16, 22, 28), "middle_fiber", False),
        (
            65,
            (97, 98, 99, 113, 114, 115, 119, 120, 121, 125, 126, 127),
            (32, 33, 34, 48, 49, 50, 54, 55, 56, 60, 61, 62),
            "backbone",
            False,
        ),
    )
    actual_states = tuple(
        (
            int(row["reference"]),
            tuple(int(value) for value in row["roots"]),
            tuple(int(value) for value in row["values"]),
            str(row["source"]),
            bool(row["terminal"]),
        )
        for row in profile["states"]
    )
    if actual_states != expected_states:
        raise AssertionError(f"recursive current-latent retained family changed: {actual_states}")

    expected_recursive = {(97, 113), (97, 119), (97, 125)}
    actual_recursive = {
        tuple(int(value) for value in row["resource"])
        for row in profile["recursive_current_latent_rows"]
    }
    if actual_recursive != expected_recursive:
        raise AssertionError("recursive current-latent resource set changed")

    state_scale = {
        int(row["state_index"]): shell_base(tuple(int(value) for value in row["values"]))
        for row in profile["states"]
    }
    ratio_rows: list[dict[str, object]] = []
    maximum_ratio = Fraction()
    for row in profile["current_latent_rows"]:
        current = row["current"]
        latent = row["latent"]
        if len(current) != 1 or len(latent) != 1:
            raise AssertionError("critical no-go owner degree changed")
        current_scale = state_scale[int(current[0]["state_index"])]
        latent_scale = state_scale[int(latent[0]["state_index"])]
        ratio = Fraction(current_scale + 2 * latent_scale, parent_base)
        maximum_ratio = max(maximum_ratio, ratio)
        ratio_rows.append(
            {
                "resource": row["resource"],
                "current_terminal": bool(current[0]["terminal"]),
                "current_scale": current_scale,
                "latent_scale": latent_scale,
                "combined_ratio": str(ratio),
                "critical_excess_ratio": str(max(Fraction(), ratio - 1)),
            }
        )

    if maximum_ratio != Fraction(5, 4):
        raise AssertionError("recursive current-latent critical ratio changed")
    recursive_rows = [row for row in ratio_rows if not bool(row["current_terminal"])]
    if len(recursive_rows) != 3 or any(row["combined_ratio"] != "5/4" for row in recursive_rows):
        raise AssertionError("recursive current-latent no-go profile changed")

    output = {
        "schema": "recursive_current_latent_critical_no_go_v1",
        "parent": parent,
        "parent_base": parent_base,
        "profile": profile,
        "critical_rows": ratio_rows,
        "maximum_combined_ratio": str(maximum_ratio),
        "checks": {
            "parent_four_ap_free": True,
            "parent_inside_one_standard_shell": True,
            "actual_lexicographic_retained_policy": True,
            "recursive_current_latent_exists": True,
            "zero_correction_critical_packing_fails": maximum_ratio > 1,
            "recursive_middle_current_residual_ratio": "1/4",
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
