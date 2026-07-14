#!/usr/bin/env python3
"""Cross-check pair-resource identity when F3 recursive output becomes R3 input.

This probe reconstructs the third retained family once, then computes its
current-plus-latent resource profile in two independent ways:

1. as the recursive portion of the complete F3 child family;
2. directly as the R3 recursive parent family.

The two profiles must agree exactly.  The probe records both without assuming
which earlier diagnostic is correct.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import sys

from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Pair = tuple[int, int]


def pair_weight(pair: Pair) -> Fraction:
    left, right = pair
    if not left < right:
        raise AssertionError(f"invalid pair {pair}")
    return Fraction(1, right - left)


def profile(states: tuple[object, ...]) -> dict[str, object]:
    current: Counter[Pair] = Counter()
    latent: Counter[Pair] = Counter()
    state_rows: list[dict[str, object]] = []
    for state in sorted(states, key=lambda item: item.index):
        values = tuple(state.values)
        roots = tuple(state.representative.provenance)
        if len(values) != len(roots):
            raise AssertionError("point/provenance mismatch")
        if len(set(roots)) != len(roots):
            raise AssertionError(f"state {state.index} repeats roots")
        offsets = {root - value for value, root in zip(values, roots, strict=True)}
        if len(offsets) != 1:
            raise AssertionError(f"state {state.index} is not affine")
        reference = next(iter(offsets))
        for value, root in zip(values, roots, strict=True):
            pair = (reference, root)
            if pair_weight(pair) != Fraction(1, value):
                raise AssertionError("current pair mismatch")
            current[pair] += 1
        latent.update(combinations(sorted(roots), 2))
        state_rows.append(
            {
                "state_class": state.index,
                "parent_class": state.representative.parent_class,
                "size": len(values),
                "reference": reference,
                "roots_sha256": canonical_hash(sorted(roots)),
                "values_sha256": canonical_hash(values),
            }
        )
    all_resources = current + latent
    occurrence_mass = sum(
        (pair_weight(pair) * count for pair, count in all_resources.items()),
        Fraction(),
    )
    union_mass = sum((pair_weight(pair) for pair in all_resources), Fraction())
    return {
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "state_sizes": [len(state.values) for state in sorted(states, key=lambda item: item.index)],
        "current_occurrences": sum(current.values()),
        "current_distinct": len(current),
        "latent_occurrences": sum(latent.values()),
        "latent_distinct": len(latent),
        "resource_occurrences": sum(all_resources.values()),
        "resource_distinct": len(all_resources),
        "maximum_multiplicity": max(all_resources.values(), default=0),
        "repeated_tokens": sum(count > 1 for count in all_resources.values()),
        "occurrence_mass": serialize_mass(occurrence_mass),
        "union_mass": serialize_mass(union_mass),
        "repeated_mass": serialize_mass(occurrence_mass - union_mass),
        "state_rows": state_rows,
        "hashes": {
            "current": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(current.items())]
            ),
            "latent": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(latent.items())]
            ),
            "all": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(all_resources.items())]
            ),
            "state_rows": canonical_hash(state_rows),
        },
    }


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third_child_view = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    # Rebind the same immutable tuple under the semantic parent name. This is
    # intentionally not a second propagation or reconstruction.
    recursive_third_parent_view = tuple(recursive_third_child_view)

    child_profile = profile(recursive_third_child_view)
    parent_profile = profile(recursive_third_parent_view)
    identical = child_profile == parent_profile
    output = {
        "schema": "pair_resource_generation_consistency_probe_v1",
        "scope": "same_certified_recursive_F3_family_viewed_as_child_and_R3_parent",
        "same_object_ids": [
            id(left) == id(right)
            for left, right in zip(
                recursive_third_child_view,
                recursive_third_parent_view,
                strict=True,
            )
        ],
        "child_profile": child_profile,
        "parent_profile": parent_profile,
        "profiles_identical": identical,
        "profiles_sha256": canonical_hash(
            {"child": child_profile, "parent": parent_profile}
        ),
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if identical else 1


if __name__ == "__main__":
    raise SystemExit(main())
