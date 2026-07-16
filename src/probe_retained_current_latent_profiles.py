#!/usr/bin/env python3
"""Profile current/latent resource reuse across the certified retained chain."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from probe_residual_sponsor_backbone_split import (
    affine_reference,
    build_split_occurrences,
    retain_occurrences,
)
from probe_sponsor_pair_transport_frontier import serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]
Resource = tuple[int, int, int]


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate retained resource pair")
    return (left, right) if left < right else (right, left)


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def classify_transition(
    name: str,
    parents: tuple[object, ...],
    children: tuple[object, ...],
) -> dict[str, object]:
    parent_roots = {
        int(parent.index): set(int(root) for root in parent.representative.provenance)
        for parent in parents
    }
    owners: dict[Resource, list[dict[str, object]]] = defaultdict(list)
    child_resource_identities: set[tuple[int, int]] = set()

    for child in children:
        parent_class = int(child.representative.parent_class)
        if parent_class not in parent_roots:
            raise AssertionError(f"{name}: child references unknown parent class")
        reference = affine_reference(child)
        values = tuple(int(value) for value in child.values)
        roots = tuple(int(root) for root in child.representative.provenance)
        terminal = not contains_three_term_ap(values)
        source = str(child.representative.source)
        if any(root - value != reference for value, root in zip(values, roots, strict=True)):
            raise AssertionError(f"{name}: affine root/value alignment failed")

        for value, root in zip(values, roots, strict=True):
            pair = ordered_pair(reference, root)
            if not set(pair) <= parent_roots[parent_class]:
                raise AssertionError(f"{name}: current resource left parent root universe")
            if pair[1] - pair[0] != value:
                raise AssertionError(f"{name}: current resource gap mismatch")
            child_identity = (0, value)
            if child_identity in child_resource_identities:
                raise AssertionError(f"{name}: point-disjoint current identity repeated")
            child_resource_identities.add(child_identity)
            resource = (parent_class, pair[0], pair[1])
            owners[resource].append(
                {
                    "state_index": int(child.index),
                    "reference": reference,
                    "kind": "current",
                    "terminal": terminal,
                    "source": source,
                }
            )

        if terminal:
            continue
        for first, second in combinations(range(len(values)), 2):
            pair = ordered_pair(roots[first], roots[second])
            if not set(pair) <= parent_roots[parent_class]:
                raise AssertionError(f"{name}: latent resource left parent root universe")
            child_identity = ordered_pair(values[first], values[second])
            if pair[1] - pair[0] != child_identity[1] - child_identity[0]:
                raise AssertionError(f"{name}: latent resource gap mismatch")
            if child_identity in child_resource_identities:
                raise AssertionError(f"{name}: point-disjoint latent identity repeated")
            child_resource_identities.add(child_identity)
            resource = (parent_class, pair[0], pair[1])
            owners[resource].append(
                {
                    "state_index": int(child.index),
                    "reference": reference,
                    "kind": "latent",
                    "terminal": False,
                    "source": source,
                }
            )

    repeated = {resource: rows for resource, rows in owners.items() if len(rows) > 1}
    occurrence_mass = Fraction()
    parent_union_mass = Fraction()
    branching_excess = Fraction()
    current_latent_mass = Fraction()
    terminal_current_latent_mass = Fraction()
    recursive_current_latent_mass = Fraction()
    latent_latent_residual = Fraction()
    repeated_profiles: Counter[tuple[int, int, int]] = Counter()
    maximum_owner_degree = 0
    maximum_latent_degree = 0
    latent_residual_resources = 0
    repeated_rows: list[dict[str, object]] = []

    for resource, rows in owners.items():
        _parent, left, right = resource
        gap = right - left
        occurrence_mass += Fraction(len(rows), gap)
        parent_union_mass += Fraction(1, gap)
        if len(rows) == 1:
            continue
        maximum_owner_degree = max(maximum_owner_degree, len(rows))
        current_rows = [row for row in rows if row["kind"] == "current"]
        latent_rows = [row for row in rows if row["kind"] == "latent"]
        if len(current_rows) > 1:
            raise AssertionError(f"{name}: one resource has multiple current owners")
        current_count = len(current_rows)
        latent_count = len(latent_rows)
        maximum_latent_degree = max(maximum_latent_degree, latent_count)
        repeated_profiles[(current_count, latent_count, len(rows))] += 1

        branching_excess += Fraction(len(rows) - 1, gap)
        if current_count and latent_count:
            current_latent_mass += Fraction(1, gap)
            if bool(current_rows[0]["terminal"]):
                terminal_current_latent_mass += Fraction(1, gap)
            else:
                recursive_current_latent_mass += Fraction(1, gap)
        residual_copies = max(0, latent_count - 1)
        latent_latent_residual += Fraction(residual_copies, gap)
        if residual_copies:
            latent_residual_resources += 1

        if (len(rows) - 1) != (
            current_count * (1 if latent_count else 0) + residual_copies
        ):
            raise AssertionError(f"{name}: current/latent multiplicity identity failed")

        repeated_rows.append(
            {
                "resource": resource,
                "gap": gap,
                "multiplicity": len(rows),
                "current_owners": current_count,
                "latent_owners": latent_count,
                "latent_residual_copies": residual_copies,
                "owners": sorted(
                    rows,
                    key=lambda row: (
                        int(row["state_index"]), str(row["kind"])
                    ),
                ),
            }
        )

    if occurrence_mass - parent_union_mass != branching_excess:
        raise AssertionError(f"{name}: occurrence/union branching identity failed")
    if branching_excess != current_latent_mass + latent_latent_residual:
        raise AssertionError(f"{name}: current/latent mass identity failed")
    if current_latent_mass != (
        terminal_current_latent_mass + recursive_current_latent_mass
    ):
        raise AssertionError(f"{name}: current owner terminal split failed")

    return {
        "name": name,
        "counts": {
            "parents": len(parents),
            "children": len(children),
            "terminal_children": sum(
                not contains_three_term_ap(child.values) for child in children
            ),
            "recursive_children": sum(
                contains_three_term_ap(child.values) for child in children
            ),
            "parent_resource_union": len(owners),
            "child_resource_occurrences": sum(len(rows) for rows in owners.values()),
            "repeated_parent_resources": len(repeated),
            "maximum_owner_degree": maximum_owner_degree,
            "maximum_latent_degree": maximum_latent_degree,
            "latent_residual_resources": latent_residual_resources,
        },
        "masses": {
            "child_resource_occurrence": serialize_mass(occurrence_mass),
            "parent_resource_union": serialize_mass(parent_union_mass),
            "branching_excess": serialize_mass(branching_excess),
            "current_latent_overlap": serialize_mass(current_latent_mass),
            "terminal_current_latent_overlap": serialize_mass(
                terminal_current_latent_mass
            ),
            "recursive_current_latent_overlap": serialize_mass(
                recursive_current_latent_mass
            ),
            "latent_latent_residual": serialize_mass(latent_latent_residual),
        },
        "profiles": [
            {
                "current_owners": profile[0],
                "latent_owners": profile[1],
                "total_owners": profile[2],
                "resources": count,
            }
            for profile, count in sorted(repeated_profiles.items())
        ],
        "repeated_rows_hash": canonical_hash(repeated_rows),
        "checks": {
            "point_disjoint_child_resources": True,
            "branching_decomposition": (
                branching_excess == current_latent_mass + latent_latent_residual
            ),
        },
    }


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: probe_retained_current_latent_profiles.py OUTPUT_JSON"
        )

    retained_first, retained_second = reconstruct_retained_families()
    recursive_first = tuple(
        state for state in retained_first if contains_three_term_ap(state.values)
    )
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
    retained_fifth, metrics5 = retain_occurrences(
        build_split_occurrences(recursive_fourth)
    )
    if metrics5["retained_states"] != 37:
        raise AssertionError("split fifth retained frontier changed")

    transitions = [
        classify_transition("R1_to_F2", recursive_first, retained_second),
        classify_transition("R2_to_F3", recursive_second, retained_third),
        classify_transition("R3_to_F4", recursive_third, retained_fourth),
        classify_transition("R4_to_F5_split", recursive_fourth, retained_fifth),
    ]

    output = {
        "schema": "retained_current_latent_profiles_v1",
        "scope": "four certified point-disjoint retained transitions",
        "generation_six_propagated": False,
        "transitions": transitions,
        "aggregate": {
            "branching_excess": serialize_mass(
                sum(
                    (
                        Fraction(row["masses"]["branching_excess"]["fraction"])
                        for row in transitions
                    ),
                    Fraction(),
                )
            ),
            "current_latent_overlap": serialize_mass(
                sum(
                    (
                        Fraction(row["masses"]["current_latent_overlap"]["fraction"])
                        for row in transitions
                    ),
                    Fraction(),
                )
            ),
            "latent_latent_residual": serialize_mass(
                sum(
                    (
                        Fraction(row["masses"]["latent_latent_residual"]["fraction"])
                        for row in transitions
                    ),
                    Fraction(),
                )
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[1]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
