#!/usr/bin/env python3
"""Compute exact affine pair-resource rows for R1->F2 and R2->F3.

For each affine recursive parent family, the resource multiset contains current
pairs (r,p) and all latent root pairs inside each parent state.  The complete
retained child family contributes every current pair and latent pairs of its
recursively continuing states.

The probe records exact containment, occurrence/union resource mass,
resource multiplicity, type conversion, and Bellman surplus.  It uses only the
already certified retained families through F3 and does not construct a new
frontier.
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
        raise AssertionError(f"invalid root pair {pair}")
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


def transition_record(
    name: str,
    parents: tuple[object, ...],
    children: tuple[object, ...],
) -> dict[str, object]:
    parent_resources: Counter[Pair] = Counter()
    parent_kinds: dict[Pair, set[str]] = defaultdict(set)
    parent_classes: dict[Pair, set[int]] = defaultdict(set)
    parent_roots: dict[int, set[int]] = {}
    parent_current_by_root: dict[tuple[int, int], int] = {}
    parent_references: dict[int, int] = {}

    for state in parents:
        reference = affine_reference(state)
        roots = tuple(state.representative.provenance)
        values = tuple(state.values)
        root_set = set(roots)
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
    missing_current: Counter[Pair] = Counter()
    missing_latent: Counter[Pair] = Counter()

    recursive_children = tuple(
        state for state in children if contains_three_term_ap(state.values)
    )
    terminal_children = tuple(
        state for state in children if not contains_three_term_ap(state.values)
    )

    for state in children:
        representative = state.representative
        parent_class = representative.parent_class
        if parent_class not in parent_roots:
            raise AssertionError(
                f"child state {state.index} has unknown parent class {parent_class}"
            )
        allowed_roots = parent_roots[parent_class]
        terminal = not contains_three_term_ap(state.values)
        # The symbolic closure theorem predicts every child is affine. Verify
        # this independently of the parent-resource membership test.
        affine_reference(state)
        for value, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            reference = root - value
            pair = (reference, root)
            if root not in allowed_roots or pair not in parent_resources:
                missing_current[pair] += 1
                continue
            if immediate != parent_current_by_root[(parent_class, root)]:
                raise AssertionError("child immediate provenance mismatch")
            child_resources[pair] += 1
            child_kinds[pair].add(
                "terminal_current" if terminal else "recursive_current"
            )
            child_classes[pair].add(state.index)
            child_parent_classes[pair].add(parent_class)

    for state in recursive_children:
        parent_class = state.representative.parent_class
        allowed_roots = parent_roots[parent_class]
        roots = tuple(sorted(state.representative.provenance))
        if len(set(roots)) != len(roots):
            raise AssertionError("recursive child repeats a root within one state")
        for pair in combinations(roots, 2):
            if not set(pair) <= allowed_roots or pair not in parent_resources:
                missing_latent[pair] += 1
                continue
            child_resources[pair] += 1
            child_kinds[pair].add("recursive_latent")
            child_classes[pair].add(state.index)
            child_parent_classes[pair].add(parent_class)

    parent_occurrence_mass = counter_mass(parent_resources, union=False)
    parent_union_mass = counter_mass(parent_resources, union=True)
    child_occurrence_mass = counter_mass(child_resources, union=False)
    child_union_mass = counter_mass(child_resources, union=True)
    parent_repeated_mass = parent_occurrence_mass - parent_union_mass
    child_repeated_mass = child_occurrence_mass - child_union_mass

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

    all_contained = not missing_current and not missing_latent
    return {
        "name": name,
        "parent": {
            "states": len(parents),
            "points": sum(len(state.values) for state in parents),
            "affine_states": len(parents),
            "resource_occurrences": sum(parent_resources.values()),
            "distinct_resources": len(parent_resources),
            "maximum_resource_multiplicity": max(parent_resources.values(), default=0),
            "repeated_resource_tokens": sum(
                count > 1 for count in parent_resources.values()
            ),
            "current_pairs": len(parent_current_pairs),
            "latent_pairs": len(parent_latent_pairs),
            "occurrence_resource_mass": serialize_mass(parent_occurrence_mass),
            "union_resource_mass": serialize_mass(parent_union_mass),
            "repeated_resource_mass": serialize_mass(parent_repeated_mass),
        },
        "child": {
            "total_states": len(children),
            "total_points": sum(len(state.values) for state in children),
            "terminal_states": len(terminal_children),
            "recursive_states": len(recursive_children),
            "affine_states": len(children),
            "resource_occurrences": sum(child_resources.values()),
            "distinct_resources": len(child_resources),
            "maximum_resource_multiplicity": max(child_resources.values(), default=0),
            "repeated_resource_tokens": sum(
                count > 1 for count in child_resources.values()
            ),
            "terminal_current_pairs": len(child_terminal_pairs),
            "recursive_current_pairs": len(child_recursive_current_pairs),
            "recursive_latent_pairs": len(child_recursive_latent_pairs),
            "occurrence_resource_mass": serialize_mass(child_occurrence_mass),
            "union_resource_mass": serialize_mass(child_union_mass),
            "repeated_resource_mass": serialize_mass(child_repeated_mass),
        },
        "containment": {
            "missing_current_occurrences": sum(missing_current.values()),
            "missing_current_pairs": len(missing_current),
            "missing_latent_occurrences": sum(missing_latent.values()),
            "missing_latent_pairs": len(missing_latent),
            "all_resources_contained": all_contained,
            "missing_current_examples": [
                (left, right, count)
                for (left, right), count in sorted(missing_current.items())[:20]
            ],
            "missing_latent_examples": [
                (left, right, count)
                for (left, right), count in sorted(missing_latent.items())[:20]
            ],
        },
        "type_counts": {
            "terminal_from_parent_current": len(
                child_terminal_pairs & parent_current_pairs
            ),
            "terminal_from_parent_latent": len(
                child_terminal_pairs & parent_latent_pairs
            ),
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
        },
        "bellman": {
            "occurrence_left": serialize_mass(child_occurrence_mass),
            "occurrence_right": serialize_mass(parent_occurrence_mass),
            "occurrence_surplus": serialize_mass(
                parent_occurrence_mass - child_occurrence_mass
            ),
            "occurrence_ratio": serialize_mass(
                child_occurrence_mass / parent_occurrence_mass
            ),
            "occurrence_verified": (
                all_contained and child_occurrence_mass <= parent_occurrence_mass
            ),
            "union_left": serialize_mass(child_union_mass),
            "union_right": serialize_mass(parent_union_mass),
            "union_surplus": serialize_mass(parent_union_mass - child_union_mass),
            "union_ratio": serialize_mass(child_union_mass / parent_union_mass),
            "union_verified": all_contained and child_union_mass <= parent_union_mass,
        },
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
            "missing_current": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(missing_current.items())]
            ),
            "missing_latent": canonical_hash(
                [(left, right, count) for (left, right), count in sorted(missing_latent.items())]
            ),
            "parent_references": canonical_hash(sorted(parent_references.items())),
        },
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_first = tuple(
        state for state in retained_first if contains_three_term_ap(state.values)
    )
    if len(recursive_first) != len(retained_first):
        raise AssertionError("first retained family unexpectedly contains terminal states")
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )

    rows = [
        transition_record("R1_to_F2", recursive_first, retained_second),
        transition_record("R2_to_F3", recursive_second, retained_third),
    ]
    output = {
        "schema": "pair_resource_early_transitions_probe_v1",
        "scope": "certified_R1_to_F2_and_R2_to_F3_retained_transitions",
        "later_generation_propagated_for_test": False,
        "transitions": rows,
        "hashes": {
            "transition_summaries": canonical_hash(
                [
                    {
                        key: row[key]
                        for key in (
                            "name",
                            "parent",
                            "child",
                            "containment",
                            "type_counts",
                            "bellman",
                            "hashes",
                        )
                    }
                    for row in rows
                ]
            )
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
