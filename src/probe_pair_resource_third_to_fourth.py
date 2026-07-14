#!/usr/bin/env python3
"""Diagnose pair-resource transport from R3 recursive states to complete F4.

Unlike the certified R4->F5 theorem, this probe does not assume root or pair
uniqueness. It records:
- affine coverage of R3 parents;
- parent current/latent pair occurrence and union capacity;
- F4 current/recursive-latent pair containment;
- pair-use multiplicity and repeated pair-resource mass;
- occurrence and union Bellman rows;
- exact missing-resource witnesses, if any.

No fifth or sixth generation beyond the already certified F4 construction is
needed for the resource test itself, although the standard reconstruction is
used to obtain the existing F4 family.
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


def affine_reference(state: object) -> int | None:
    roots = tuple(state.representative.provenance)
    values = tuple(state.values)
    if len(set(roots)) != len(roots):
        return None
    offsets = {root - value for root, value in zip(roots, values, strict=True)}
    return next(iter(offsets)) if len(offsets) == 1 else None


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
    _occ4, retained_fourth, metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    terminal_fourth = tuple(
        state for state in retained_fourth if not contains_three_term_ap(state.values)
    )

    parent_resources: Counter[Pair] = Counter()
    parent_kinds: dict[Pair, set[str]] = defaultdict(set)
    parent_classes: dict[Pair, set[int]] = defaultdict(set)
    parent_roots: dict[int, set[int]] = {}
    parent_current_by_root: dict[tuple[int, int], int] = {}
    affine_parent_classes: set[int] = set()
    nonaffine_parent_rows: list[dict[str, object]] = []

    for state in recursive_third:
        reference = affine_reference(state)
        roots = tuple(state.representative.provenance)
        values = tuple(state.values)
        if reference is None:
            nonaffine_parent_rows.append(
                {
                    "state_class": state.index,
                    "source": state.representative.source,
                    "source_step": state.representative.source_step,
                    "exponent": state.representative.exponent,
                    "size": len(values),
                    "distinct_roots": len(set(roots)),
                    "harmonic_mass": serialize_mass(state.weight),
                    "tokens_sha256": canonical_hash(
                        sorted(zip(values, roots, strict=True))
                    ),
                }
            )
            continue
        affine_parent_classes.add(state.index)
        root_set = set(roots)
        parent_roots[state.index] = root_set
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
    missing_current: Counter[Pair] = Counter()
    missing_latent: Counter[Pair] = Counter()
    child_from_nonaffine_points = 0
    child_from_nonaffine_mass = Fraction()
    affine_child_current_mass = Fraction()

    for state in retained_fourth:
        representative = state.representative
        parent_class = representative.parent_class
        terminal = not contains_three_term_ap(state.values)
        if parent_class not in affine_parent_classes:
            child_from_nonaffine_points += len(state.values)
            child_from_nonaffine_mass += state.weight
            continue
        allowed_roots = parent_roots[parent_class]
        for value, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            reference = root - value
            pair = (reference, root)
            affine_child_current_mass += Fraction(1, value)
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

    for state in recursive_fourth:
        parent_class = state.representative.parent_class
        if parent_class not in affine_parent_classes:
            continue
        allowed_roots = parent_roots[parent_class]
        roots = tuple(sorted(state.representative.provenance))
        if len(set(roots)) != len(roots):
            # Equal-root latent pairs have no positive difference and are not
            # valid pair resources. Record all ordinary distinct-root pairs.
            roots = tuple(sorted(set(roots)))
        for pair in combinations(roots, 2):
            if not set(pair) <= allowed_roots or pair not in parent_resources:
                missing_latent[pair] += 1
                continue
            child_resources[pair] += 1
            child_kinds[pair].add("recursive_latent")
            child_classes[pair].add(state.index)

    parent_occurrence_mass = counter_mass(parent_resources, union=False)
    parent_union_mass = counter_mass(parent_resources, union=True)
    child_occurrence_mass = counter_mass(child_resources, union=False)
    child_union_mass = counter_mass(child_resources, union=True)
    child_repeated_mass = child_occurrence_mass - child_union_mass
    missing_current_mass = counter_mass(missing_current, union=False)
    missing_latent_mass = counter_mass(missing_latent, union=False)

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

    output = {
        "schema": "pair_resource_third_to_fourth_probe_v1",
        "scope": "certified_R3_recursive_to_complete_F4_retained_transition",
        "generation_five_or_six_propagated_for_test": False,
        "parent": {
            "recursive_states": len(recursive_third),
            "points": sum(len(state.values) for state in recursive_third),
            "affine_states": len(affine_parent_classes),
            "nonaffine_states": len(nonaffine_parent_rows),
            "affine_parent_classes": sorted(affine_parent_classes),
            "nonaffine_rows": nonaffine_parent_rows,
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
            "repeated_resource_mass": serialize_mass(
                parent_occurrence_mass - parent_union_mass
            ),
        },
        "child": {
            "total_states": len(retained_fourth),
            "total_points": sum(len(state.values) for state in retained_fourth),
            "terminal_states": len(terminal_fourth),
            "recursive_states": len(recursive_fourth),
            "resources_from_affine_parents": sum(child_resources.values()),
            "distinct_resources_from_affine_parents": len(child_resources),
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
            "current_mass_from_affine_parents": serialize_mass(
                affine_child_current_mass
            ),
            "points_from_nonaffine_parents": child_from_nonaffine_points,
            "mass_from_nonaffine_parents": serialize_mass(
                child_from_nonaffine_mass
            ),
        },
        "containment": {
            "missing_current_occurrences": sum(missing_current.values()),
            "missing_current_pairs": len(missing_current),
            "missing_current_mass": serialize_mass(missing_current_mass),
            "missing_latent_occurrences": sum(missing_latent.values()),
            "missing_latent_pairs": len(missing_latent),
            "missing_latent_mass": serialize_mass(missing_latent_mass),
            "all_affine_parent_resources_contained": (
                not missing_current and not missing_latent
            ),
            "missing_current_examples": [
                (left, right, count)
                for (left, right), count in sorted(missing_current.items())[:25]
            ],
            "missing_latent_examples": [
                (left, right, count)
                for (left, right), count in sorted(missing_latent.items())[:25]
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
            "occurrence_verified": (
                not missing_current
                and not missing_latent
                and child_occurrence_mass <= parent_occurrence_mass
            ),
            "union_left": serialize_mass(child_union_mass),
            "union_right": serialize_mass(parent_union_mass),
            "union_surplus": serialize_mass(
                parent_union_mass - child_union_mass
            ),
            "union_verified": (
                not missing_current
                and not missing_latent
                and child_union_mass <= parent_union_mass
            ),
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
        },
        "metrics4": metrics4,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
