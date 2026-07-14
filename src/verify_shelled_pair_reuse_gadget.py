#!/usr/bin/env python3
"""Verify an explicit shell-valid latent-pair reuse gadget."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from probe_shelled_oriented_full_edge_pair_persistence import shelled_family
from verify_full_edge_coordinated_branching import contains_four_ap, pair_weight, three_aps

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

K = 16
SUPPORT = frozenset({0, 2, 19, 23, 25, 27, 36, 44, 46, 50, 52, 54})
FIRST_KEY = ("side_first", 2, None, 4)
SECOND_KEY = ("side_first", 0, None, 4)
SHARED_PAIR = (23, 27)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    if contains_four_ap(SUPPORT):
        raise AssertionError("reuse gadget support contains a four-AP")

    shells, roots, references, _occurrences = shelled_family(SUPPORT)
    expected = {
        FIRST_KEY: {
            "tokens": frozenset({17, 21, 25}),
            "roots": frozenset({19, 23, 27}),
            "reference": 2,
        },
        SECOND_KEY: {
            "tokens": frozenset({23, 25, 27}),
            "roots": frozenset({23, 25, 27}),
            "reference": 0,
        },
    }
    for key, row in expected.items():
        if shells.get(key) != row["tokens"]:
            raise AssertionError(f"unexpected tokens for {key}: {shells.get(key)}")
        if roots.get(key) != row["roots"]:
            raise AssertionError(f"unexpected roots for {key}: {roots.get(key)}")
        if references.get(key) != row["reference"]:
            raise AssertionError(f"unexpected reference for {key}")
        if len(three_aps(shells[key])) != 1:
            raise AssertionError(f"shell {key} is not exactly one recursive three-AP")

    first_pairs = set(combinations(sorted(roots[FIRST_KEY]), 2))
    second_pairs = set(combinations(sorted(roots[SECOND_KEY]), 2))
    intersection = first_pairs & second_pairs
    if intersection != {SHARED_PAIR}:
        raise AssertionError(f"unexpected latent-pair intersection: {intersection}")
    if pair_weight(SHARED_PAIR) != Fraction(1, 4):
        raise AssertionError("shared pair weight changed")

    record = {
        "schema": "shelled_pair_reuse_gadget_certificate_v1",
        "K": K,
        "support": sorted(SUPPORT),
        "support_size": len(SUPPORT),
        "support_span": max(SUPPORT) - min(SUPPORT),
        "support_four_ap_free": True,
        "first_shell_key": list(FIRST_KEY),
        "first_tokens": sorted(shells[FIRST_KEY]),
        "first_roots": sorted(roots[FIRST_KEY]),
        "second_shell_key": list(SECOND_KEY),
        "second_tokens": sorted(shells[SECOND_KEY]),
        "second_roots": sorted(roots[SECOND_KEY]),
        "shared_latent_pair": list(SHARED_PAIR),
        "shared_pair_weight": "1/4",
        "recursive_shells": 2,
        "latent_pair_reuse_multiplicity": 2,
    }
    record["payload_sha256"] = canonical_hash(record)
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
