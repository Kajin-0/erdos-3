#!/usr/bin/env python3
"""Search a structured 13-point family for sharp latent-latent critical reuse."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_critical_fractional_reserve_flow import profile
from search_lexicographic_reserve_pseudoforest_small_box import contains_four_ap


def gadget(reference_gap: int, root_offset: int) -> tuple[int, ...]:
    pivot = 65
    reference = pivot + reference_gap
    first_root = reference + root_offset
    bases = (reference, first_root, first_root + 6, first_root + 12)
    return tuple(sorted({pivot, *(value + delta for value in bases for delta in range(3))}))


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: search_sharp_latent_latent_critical_gadget.py OUTPUT")

    candidates = 0
    four_ap_free = 0
    latent_reuse = 0
    best_ratio = Fraction()
    best_rows: list[dict[str, object]] = []
    sharp_witness: dict[str, object] | None = None

    for reference_gap in range(1, 33):
        for root_offset in range(3, 49):
            parent = gadget(reference_gap, root_offset)
            if len(parent) != 13 or min(parent) < 64 or max(parent) >= 128:
                continue
            candidates += 1
            if contains_four_ap(parent):
                continue
            four_ap_free += 1
            result = profile(
                f"gadget_delta_{reference_gap}_offset_{root_offset}",
                parent,
            )
            duplicated = [
                row for row in result["demands"]
                if int(row["latent_owners"]) == 2
            ]
            if not duplicated:
                continue
            latent_reuse += 1
            maximum = max(
                Fraction(row["unassigned_ratio"])
                for row in duplicated
            )
            record = {
                "reference_gap": reference_gap,
                "root_offset": root_offset,
                "parent": parent,
                "maximum_duplicated_unassigned_ratio": str(maximum),
                "profile": result,
            }
            if maximum > best_ratio:
                best_ratio = maximum
                best_rows = [record]
            elif maximum == best_ratio:
                best_rows.append(record)
            if maximum == Fraction(1, 2) and sharp_witness is None:
                sharp_witness = record

    output = {
        "schema": "sharp_latent_latent_critical_gadget_search_v1",
        "family": {
            "pivot": 65,
            "parent_shell": [64, 128],
            "reference_gap_range": [1, 32],
            "root_offset_range": [3, 48],
            "root_spacing": 6,
        },
        "counts": {
            "candidates": candidates,
            "four_ap_free": four_ap_free,
            "with_retained_latent_reuse": latent_reuse,
        },
        "maximum_duplicated_unassigned_ratio": str(best_ratio),
        "maximum_witnesses": best_rows,
        "first_half_witness": sharp_witness,
        "checks": {
            "actual_lexicographic_retained_policy": True,
            "joint_critical_assignment_used": True,
            "half_coefficient_attained": sharp_witness is not None,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[1]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
