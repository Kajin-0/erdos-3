#!/usr/bin/env python3
"""Verify the smallest point-disjoint latent-latent reuse obstruction."""
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


def main() -> int:
    parent = (1, 2, 3, 5, 6, 9)
    roots = (3, 6, 9)
    references = (1, 2)
    children = tuple(
        tuple(root - reference for root in roots) for reference in references
    )

    if contains_ap(parent, 4):
        raise AssertionError("counterexample parent contains a four-AP")
    if any(not contains_ap(child, 3) for child in children):
        raise AssertionError("counterexample child is not recursive")
    if set(children[0]) & set(children[1]):
        raise AssertionError("counterexample children are not point-disjoint")

    latent_pairs = tuple(combinations(roots, 2))
    residual = pair_energy(roots)
    if latent_pairs != ((3, 6), (3, 9), (6, 9)):
        raise AssertionError("latent pair family changed")
    if residual != Fraction(5, 6):
        raise AssertionError("latent residual changed")

    reference_gap = references[1] - references[0]
    reference_capacity = Fraction(1, reference_gap)
    if not residual < reference_capacity:
        raise AssertionError("near reference pair no longer dominates residual")
    if any(reference_gap > right - left for left, right in latent_pairs):
        raise AssertionError("counterexample contains a far-aspect rectangle")

    output = {
        "schema": "point_disjoint_latent_reuse_no_go_v1",
        "parent": parent,
        "roots": roots,
        "references": references,
        "children": children,
        "latent_pairs": latent_pairs,
        "counts": {
            "recursive_children": len(children),
            "shared_latent_resources": len(latent_pairs),
            "current_owners_per_resource": 0,
            "latent_owners_per_resource": 2,
            "owner_cycle_rank": 0,
            "child_recreation_resources": 0,
        },
        "masses": {
            "latent_latent_residual_fraction": str(residual),
            "reference_pair_capacity_fraction": str(reference_capacity),
        },
        "checks": {
            "parent_four_ap_free": True,
            "children_recursive": True,
            "children_point_disjoint": True,
            "positive_latent_latent_residual": residual > 0,
            "near_reference_payment_available": residual < reference_capacity,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
