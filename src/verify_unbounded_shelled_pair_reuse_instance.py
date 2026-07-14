#!/usr/bin/env python3
"""Verify the m=4 instance of unbounded shell-valid latent-pair reuse."""
from __future__ import annotations

from itertools import combinations
import hashlib
import json
import sys

from probe_shelled_oriented_full_edge_pair_persistence import shelled_family
from verify_full_edge_coordinated_branching import contains_four_ap, pair_weight, three_aps

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

M = 4
R = frozenset({2, 6, 18, 54})
D = 64
K = 1024
C = 55
Q = frozenset({K + C, K + C + D, K + C + 2 * D})
RAW_SUPPORT = frozenset(R | Q | {2 * q - r for q in Q for r in R})
TRANSLATION = 4 * K
SUPPORT = frozenset(value + TRANSLATION for value in RAW_SUPPORT)
SHELL_EXPONENT = K.bit_length() - 1


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    if contains_four_ap(R):
        raise AssertionError("reference set contains a four-AP")
    if contains_four_ap(RAW_SUPPORT):
        raise AssertionError("raw multiplicity-four support contains a four-AP")
    if contains_four_ap(SUPPORT):
        raise AssertionError("translated multiplicity-four support contains a four-AP")
    if not all(4 * K <= value < 8 * K for value in SUPPORT):
        raise AssertionError("translated parent escaped its standard dyadic block")

    shells, roots, references, _occurrences = shelled_family(SUPPORT)
    translated_q = frozenset(q + TRANSLATION for q in Q)
    expected_keys = []
    for r in sorted(R):
        reference = r + TRANSLATION
        key = ("side_first", reference, None, SHELL_EXPONENT)
        expected_tokens = frozenset(q - r for q in Q)
        if shells.get(key) != expected_tokens:
            raise AssertionError(f"unexpected child shell for reference {r}: {shells.get(key)}")
        if not translated_q.issubset(roots.get(key, frozenset())):
            raise AssertionError(f"common root triple missing for reference {r}")
        if references.get(key) != reference:
            raise AssertionError(f"reference mismatch for {r}")
        if len(three_aps(shells[key])) != 1:
            raise AssertionError(f"reference {r} child is not exactly one three-AP")
        expected_keys.append(key)

    common_pairs = set(combinations(sorted(translated_q), 2))
    multiplicities = {}
    for pair in sorted(common_pairs):
        count = sum(pair[0] in roots[key] and pair[1] in roots[key] for key in expected_keys)
        multiplicities[pair] = count
        if count != M:
            raise AssertionError(f"common pair {pair} has multiplicity {count}, expected {M}")

    record = {
        "schema": "unbounded_shelled_pair_reuse_instance_v1",
        "m": M,
        "reference_set": sorted(R),
        "d": D,
        "K": K,
        "c": C,
        "common_root_triple_raw": sorted(Q),
        "translation": TRANSLATION,
        "parent_block": [4 * K, 8 * K],
        "parent_support": sorted(SUPPORT),
        "parent_support_size": len(SUPPORT),
        "parent_four_ap_free": True,
        "child_shell": [K, 2 * K],
        "recursive_child_keys": [list(key) for key in expected_keys],
        "common_root_triple": sorted(translated_q),
        "common_pair_multiplicities": [
            {
                "pair": list(pair),
                "weight": f"{pair_weight(pair).numerator}/{pair_weight(pair).denominator}",
                "multiplicity": multiplicities[pair],
            }
            for pair in sorted(common_pairs)
        ],
        "maximum_certified_latent_pair_multiplicity": M,
    }
    record["payload_sha256"] = canonical_hash(record)
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
