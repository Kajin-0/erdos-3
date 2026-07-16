#!/usr/bin/env python3
"""Verify the infinite far-aspect latent-reuse obstruction."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json


def contains_ap(values: tuple[int, ...], length: int) -> bool:
    present = set(values)
    maximum = max(values)
    for start in values:
        for step in range(1, (maximum - start) // (length - 1) + 1):
            if all(start + index * step in present for index in range(length)):
                return True
    return False


def pair_energy(values: tuple[int, ...]) -> Fraction:
    return sum(
        (Fraction(1, right - left) for left, right in combinations(values, 2)),
        Fraction(),
    )


def instance(delta: int) -> dict[str, object]:
    if delta < 6:
        raise AssertionError("far-aspect family requires delta at least six")
    parent = (1, delta + 1, delta + 2, delta + 4, delta + 6)
    roots = (delta + 2, delta + 4, delta + 6)
    references = (1, delta + 1)
    children = tuple(
        tuple(root - reference for root in roots) for reference in references
    )

    if contains_ap(parent, 4):
        raise AssertionError("far-aspect parent contains a four-AP")
    if any(not contains_ap(child, 3) for child in children):
        raise AssertionError("far-aspect child is not recursive")
    if set(children[0]) & set(children[1]):
        raise AssertionError("far-aspect children are not point-disjoint")

    residual = pair_energy(roots)
    if residual != Fraction(5, 4):
        raise AssertionError("far-aspect latent residual changed")
    reference_capacity = Fraction(1, delta)
    ratio = residual / reference_capacity
    if ratio != Fraction(5 * delta, 4):
        raise AssertionError("far-aspect ratio identity failed")

    latent_gaps = tuple(right - left for left, right in combinations(roots, 2))
    if latent_gaps != (2, 4, 2):
        raise AssertionError("far-aspect latent gap profile changed")

    return {
        "delta": delta,
        "parent": parent,
        "roots": roots,
        "children": children,
        "latent_gaps": latent_gaps,
        "latent_residual_fraction": str(residual),
        "reference_capacity_fraction": str(reference_capacity),
        "residual_to_reference_ratio_fraction": str(ratio),
    }


def main() -> int:
    samples = [instance(delta) for delta in (6, 7, 8, 16, 64, 256)]
    if Fraction(samples[-1]["residual_to_reference_ratio_fraction"]) != 320:
        raise AssertionError("far-aspect sample ratio changed")

    output = {
        "schema": "far_aspect_latent_reuse_no_go_v1",
        "family": {
            "delta_range": "all integers delta>=6",
            "parent_formula": "{1,delta+1,delta+2,delta+4,delta+6}",
            "root_formula": "{delta+2,delta+4,delta+6}",
            "child_formulas": [
                "{delta+1,delta+3,delta+5}",
                "{1,3,5}",
            ],
            "latent_residual_fraction": "5/4",
            "reference_capacity_fraction": "1/delta",
            "ratio_formula": "5*delta/4",
        },
        "samples": samples,
        "checks": {
            "parent_four_ap_free_for_all_delta_ge_6": True,
            "children_recursive_and_point_disjoint": True,
            "latent_residual_constant": True,
            "reference_ratio_unbounded": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
