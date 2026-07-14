#!/usr/bin/env python3
"""Certify pair-resource ownership for the complete R4->F5 retained transition.

For an affine parent S_r(P), define its resource multiset as:
- current pairs (r,p), one for each current point p-r;
- latent pairs (x,y), x<y in P.

The corresponding mass is H(S_r(P))+J(P).

For the complete fifth retained output, define used resources as:
- current pairs (p-u,p) for every terminal or recursive retained point;
- latent pairs inside each recursively continuing fifth state.

This probe checks exact pair containment, multiplicity, resource type, and the
set-valued Bellman row. No sixth generation is constructed.
"""
from __future__ import annotations

from collections import Counter, defaultdict
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


def counter_mass(counter: Counter[Pair], *, union: bool) -> Fraction:
    return sum(
        (
            pair_weight(pair) * (1 if union else multiplicity)
            for pair, multiplicity in counter.items()
        ),
        Fraction(),
    )


def affine_reference(state: object) -> int:
    roots = tuple(state.representative.provenance)
    values = tuple(state.values)
    if len(set(roots)) != len(roots):
        raise AssertionError(f"state {state.index} repeats root provenance")
    offsets = {root - value for root, value in zip(roots, values, strict=True)}
    if len(offsets) != 1:
        raise AssertionError(f"state {state.index} is not affine")
    return next(iter(offsets))


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    _occ5, retained_fifth, metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )

    parent_resources: Counter[Pair] = Counter()
    parent_kinds: dict[Pair, set[str]] = defaultdict(set)
    parent_classes: dict[Pair, set[int]] = defaultdict(set)
    parent_roots: dict[int, set[int]] = {}
    parent_references: dict[int, int] = {}
    parent_current_by_root: dict[tuple[int, int], int] = {}

    for state in recursive_fourth:
        reference = affine_reference(state)
        roots = tuple(state.representative.provenance)
        values = tuple(state.values)
        root_set = set(roots)
        if reference in root_set:
            raise AssertionError(f"reference active in parent state {state.index}")
        parent_roots[state.index] = root_set
        parent_references[state.index] = reference
        for value, root in zip(values, roots, strict=True):
            pair = (reference, root)
            if pair_weight(pair) != Fraction(1, value):
                raise AssertionError("parent current pair weight mismatch")
            parent_resources[pair] += 1
            parent_kinds[pair].add("current")
            parent_classes[pair].add(state.index)
            parent_current_by_root[(state.index, root)] = value
        for pair in combinations(sorted(root_set), 2):
            parent_resources[pair] += 1
            parent_kinds[pair].add("latent")
            parent_classes[pair].add(state.index)

    child_resources: Counter[Pair] = Counter()
    child_kinds: dict[Pair, set[str]] = defaultdict(set)
    child_classes: dict[Pair, set[int]] = defaultdict(set)
    child_parent_classes: dict[Pair, set[int]] = defaultdict(set)
    child_rows: list[dict[str, object]] = []

    for state in retained_fifth:
        representative = state.representative
        parent_class = representative.parent_class
        if parent_class not in parent_roots:
            raise AssertionError(
                f"fifth state {state.index} has unknown parent class {parent_class}"
            )
        allowed_roots = parent_roots[parent_class]
        terminal = not contains_three_term_ap(state.values)
        for value, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            reference = root - value
            pair = (reference, root)
            if root not in allowed_roots:
                raise AssertionError(
                    f"fifth root {root} left parent root universe {parent_class}"
                )
            if pair_weight(pair) != Fraction(1, value):
                raise AssertionError("child current pair weight mismatch")
            if pair not in parent_resources:
                raise AssertionError(
                    f"child current pair {pair} absent from parent resources"
                )
            if immediate != parent_current_by_root[(parent_class, root)]:
                raise AssertionError("child immediate provenance mismatch")
            child_resources[pair] += 1
            kind = "terminal_current" if terminal else "recursive_current"
            child_kinds[pair].add(kind)
            child_classes[pair].add(state.index)
            child_parent_classes[pair].add(parent_class)
            child_rows.append(
                {
                    "pair": pair,
                    "value": value,
                    "root": root,
                    "reference": reference,
                    "immediate": immediate,
                    "terminal": terminal,
                    "state_class": state.index,
                    "parent_class": parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "parent_resource_kinds": sorted(parent_kinds[pair]),
                }
            )

    for state in recursive_fifth:
        parent_class = state.representative.parent_class
        roots = tuple(sorted(state.representative.provenance))
        if len(set(roots)) != len(roots):
            raise AssertionError("fifth recursive state repeats roots")
        if not set(roots) <= parent_roots[parent_class]:
            raise AssertionError("fifth latent roots leave parent universe")
        for pair in combinations(roots, 2):
            if pair not in parent_resources:
                raise AssertionError(
                    f"fifth latent pair {pair} absent from parent resources"
                )
            child_resources[pair] += 1
            child_kinds[pair].add("recursive_latent")
            child_classes[pair].add(state.index)
            child_parent_classes[pair].add(parent_class)

    missing_child_pairs = set(child_resources) - set(parent_resources)
    if missing_child_pairs:
        raise AssertionError("child resource containment failed")

    parent_occurrence_mass = counter_mass(parent_resources, union=False)
    parent_union_mass = counter_mass(parent_resources, union=True)
    child_occurrence_mass = counter_mass(child_resources, union=False)
    child_union_mass = counter_mass(child_resources, union=True)
    repeated_child_mass = child_occurrence_mass - child_union_mass
    unused_parent_pairs = set(parent_resources) - set(child_resources)
    unused_parent_mass = sum((pair_weight(pair) for pair in unused_parent_pairs), Fraction())

    if max(parent_resources.values(), default=0) != 1:
        raise AssertionError("parent pair resource repeats")
    if max(child_resources.values(), default=0) != 1:
        raise AssertionError("child pair resource is used more than once")
    if repeated_child_mass != 0:
        raise AssertionError("child pair-resource reuse appeared")
    if parent_occurrence_mass != parent_union_mass:
        raise AssertionError("parent occurrence/union resources differ")
    if child_occurrence_mass != child_union_mass:
        raise AssertionError("child occurrence/union resources differ")
    if child_union_mass + unused_parent_mass != parent_union_mass:
        raise AssertionError("parent pair-resource partition failed")

    parent_current_pairs = {
        pair for pair, kinds in parent_kinds.items() if "current" in kinds
    }
    parent_latent_pairs = {
        pair for pair, kinds in parent_kinds.items() if "latent" in kinds
    }
    child_terminal_pairs = {
        pair for pair, kinds in child_kinds.items() if "terminal_current" in kinds
    }
    child_recursive_current_pairs = {
        pair for pair, kinds in child_kinds.items() if "recursive_current" in kinds
    }
    child_recursive_latent_pairs = {
        pair for pair, kinds in child_kinds.items() if "recursive_latent" in kinds
    }

    type_counts = {
        "terminal_from_parent_current": len(child_terminal_pairs & parent_current_pairs),
        "terminal_from_parent_latent": len(child_terminal_pairs & parent_latent_pairs),
        "recursive_current_from_parent_current": len(
            child_recursive_current_pairs & parent_current_pairs
        ),
        "recursive_current_from_parent_latent": len(
            child_recursive_current_pairs & parent_latent_pairs
        ),
        "recursive_latent_from_parent_current": len(
            child_recursive_latent_pairs & parent_current_pairs
        ),
        "recursive_latent_from_parent_latent": len(
            child_recursive_latent_pairs & parent_latent_pairs
        ),
    }

    output = {
        "schema": "pair_resource_ownership_probe_v1",
        "scope": "certified_R4_recursive_to_complete_F5_retained_transition",
        "generation_six_propagated": False,
        "counts": {
            "parent_states": len(recursive_fourth),
            "parent_current_pairs": len(parent_current_pairs),
            "parent_latent_pairs": len(parent_latent_pairs),
            "parent_resource_pairs": len(parent_resources),
            "parent_max_pair_multiplicity": max(parent_resources.values(), default=0),
            "fifth_states": len(retained_fifth),
            "fifth_current_pairs": len(child_terminal_pairs | child_recursive_current_pairs),
            "fifth_terminal_current_pairs": len(child_terminal_pairs),
            "fifth_recursive_current_pairs": len(child_recursive_current_pairs),
            "fifth_recursive_latent_pairs": len(child_recursive_latent_pairs),
            "child_resource_pairs": len(child_resources),
            "child_max_pair_multiplicity": max(child_resources.values(), default=0),
            "unused_parent_pairs": len(unused_parent_pairs),
            **type_counts,
        },
        "masses": {
            "parent_occurrence_resource": serialize_mass(parent_occurrence_mass),
            "parent_union_resource": serialize_mass(parent_union_mass),
            "child_occurrence_resource": serialize_mass(child_occurrence_mass),
            "child_union_resource": serialize_mass(child_union_mass),
            "child_repeated_resource": serialize_mass(repeated_child_mass),
            "unused_parent_resource": serialize_mass(unused_parent_mass),
            "child_over_parent_ratio": serialize_mass(
                child_union_mass / parent_union_mass
            ),
        },
        "partition_verified": (
            child_union_mass + unused_parent_mass == parent_union_mass
        ),
        "containment_verified": not missing_child_pairs,
        "child_pair_disjointness_verified": max(child_resources.values(), default=0) == 1,
        "hashes": {
            "parent_resources": canonical_hash(
                [
                    (
                        left,
                        right,
                        count,
                        sorted(parent_kinds[(left, right)]),
                        sorted(parent_classes[(left, right)]),
                    )
                    for (left, right), count in sorted(parent_resources.items())
                ]
            ),
            "child_resources": canonical_hash(
                [
                    (
                        left,
                        right,
                        count,
                        sorted(child_kinds[(left, right)]),
                        sorted(child_classes[(left, right)]),
                        sorted(child_parent_classes[(left, right)]),
                    )
                    for (left, right), count in sorted(child_resources.items())
                ]
            ),
            "child_rows": canonical_hash(child_rows),
            "unused_parent_pairs": canonical_hash(sorted(unused_parent_pairs)),
        },
        "metrics5": metrics5,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
