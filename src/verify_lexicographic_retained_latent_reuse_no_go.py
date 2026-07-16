#!/usr/bin/env python3
"""Verify latent-latent reuse under the actual lexicographic retained policy."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json

from verify_retained_provenance_second_generation import (
    DescendantOccurrence,
    build_descendant_occurrences,
    components,
    descendant_classes,
    descendant_conflict_graph,
    maximum_weight_independent_set_dp,
    resolve_lexicographic,
)
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]
Resource = tuple[int, int]


def contains_four_ap(values: tuple[int, ...]) -> bool:
    present = set(values)
    maximum = max(values)
    for start in values:
        for step in range(1, (maximum - start) // 3 + 1):
            if (
                start + step in present
                and start + 2 * step in present
                and start + 3 * step in present
            ):
                return True
    return False


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate retained no-go resource")
    return (left, right) if left < right else (right, left)


def main() -> int:
    parent = (
        25,
        31,
        32,
        33,
        68,
        69,
        70,
        73,
        74,
        75,
        78,
        79,
        80,
    )
    if contains_four_ap(parent):
        raise AssertionError("retained latent-reuse parent contains a four-AP")

    selected, residual = resolve_lexicographic(frozenset(parent))
    expected_selected = (
        (31, 32, 33, 1, 31, 33),
        (68, 69, 70, 1, 68, 70),
        (73, 74, 75, 1, 73, 75),
        (78, 79, 80, 1, 78, 80),
        (69, 74, 79, 5, 69, 79),
        (70, 75, 80, 5, 70, 80),
    )
    if selected != expected_selected:
        raise AssertionError("retained latent-reuse deletion schedule changed")

    raw_rows = build_descendant_occurrences(
        0,
        parent,
        parent,
        selected,
    )
    occurrences = tuple(
        DescendantOccurrence(
            index=index,
            parent_class=row[0],
            source=row[1],
            source_step=row[2],
            exponent=row[3],
            values=row[4],
            provenance=row[5],
            immediate_provenance=row[6],
        )
        for index, row in enumerate(raw_rows)
    )
    classes = descendant_classes(occurrences)
    adjacency = descendant_conflict_graph(classes)

    retained_indices: list[int] = []
    optimizer_counts: list[int] = []
    for component in components(adjacency):
        _weight, count, choice, _states = maximum_weight_independent_set_dp(
            component, classes, adjacency
        )
        optimizer_counts.append(count)
        retained_indices.extend(choice)
    retained = tuple(classes[index] for index in sorted(retained_indices))

    retained_rows: list[dict[str, object]] = []
    owner_map: dict[Resource, list[dict[str, object]]] = defaultdict(list)
    child_resource_identities: set[Pair] = set()

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {root - value for value, root in zip(values, roots, strict=True)}
        if len(references) != 1:
            raise AssertionError("retained no-go child is not affine")
        reference = references.pop()
        terminal = not contains_three_term_ap(values)
        retained_rows.append(
            {
                "state_index": state.index,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "exponent": state.representative.exponent,
                "reference": reference,
                "terminal": terminal,
                "values": values,
                "roots": roots,
                "weight": str(state.weight),
            }
        )

        for value, root in zip(values, roots, strict=True):
            resource = ordered_pair(reference, root)
            child_pair = (0, value)
            if child_pair in child_resource_identities:
                raise AssertionError("retained no-go current child resource repeated")
            child_resource_identities.add(child_pair)
            owner_map[resource].append(
                {
                    "state_index": state.index,
                    "kind": "current",
                    "terminal": terminal,
                    "reference": reference,
                    "child_pair": child_pair,
                }
            )

        if terminal:
            continue
        for first, second in combinations(range(len(values)), 2):
            resource = ordered_pair(roots[first], roots[second])
            child_pair = ordered_pair(values[first], values[second])
            if child_pair in child_resource_identities:
                raise AssertionError("retained no-go latent child resource repeated")
            child_resource_identities.add(child_pair)
            owner_map[resource].append(
                {
                    "state_index": state.index,
                    "kind": "latent",
                    "terminal": False,
                    "reference": reference,
                    "child_pair": child_pair,
                }
            )

    repeated = {
        resource: rows for resource, rows in owner_map.items() if len(rows) > 1
    }
    profiles: Counter[tuple[int, int, int]] = Counter()
    current_latent_mass = Fraction()
    latent_latent_mass = Fraction()
    repeated_rows: list[dict[str, object]] = []
    for resource, rows in sorted(repeated.items()):
        current_count = sum(row["kind"] == "current" for row in rows)
        latent_count = sum(row["kind"] == "latent" for row in rows)
        if current_count > 1:
            raise AssertionError("retained no-go has multiple current owners")
        profiles[(current_count, latent_count, len(rows))] += 1
        gap = resource[1] - resource[0]
        if current_count and latent_count:
            current_latent_mass += Fraction(1, gap)
        latent_latent_mass += Fraction(max(0, latent_count - 1), gap)
        repeated_rows.append(
            {
                "resource": resource,
                "gap": gap,
                "current_owners": current_count,
                "latent_owners": latent_count,
                "owners": rows,
            }
        )

    expected_retained_values = (
        (1,),
        (6, 7),
        (8,),
        (37, 42, 47),
        (43, 44, 45, 48, 49, 50, 53, 54, 55),
    )
    if tuple(row["values"] for row in retained_rows) != expected_retained_values:
        raise AssertionError("retained latent-reuse family changed")

    expected_repeated = {
        (68, 73),
        (68, 78),
        (69, 70),
        (73, 78),
    }
    if set(repeated) != expected_repeated:
        raise AssertionError("retained latent-reuse resource set changed")
    if current_latent_mass != 1:
        raise AssertionError("retained current-latent overlap changed")
    if latent_latent_mass != Fraction(1, 2):
        raise AssertionError("retained latent-latent residual changed")
    if profiles != Counter({(0, 2, 2): 3, (1, 1, 2): 1}):
        raise AssertionError("retained latent-reuse owner profiles changed")

    recursive_middle = next(
        row
        for row in retained_rows
        if row["source"] == "middle_fiber" and not row["terminal"]
    )
    recursive_backbone = next(
        row
        for row in retained_rows
        if row["source"] == "backbone"
        and not row["terminal"]
        and row["exponent"] == 5
    )
    if recursive_middle["reference"] != 31 or recursive_backbone["reference"] != 25:
        raise AssertionError("retained latent-reuse references changed")
    reference_gap = 6
    reference_capacity = Fraction(1, reference_gap)
    if latent_latent_mass / reference_capacity != 3:
        raise AssertionError("retained latent/reference ratio changed")

    output = {
        "schema": "lexicographic_retained_latent_reuse_no_go_v1",
        "parent": parent,
        "selected_schedule": selected,
        "terminal_residual": tuple(sorted(residual)),
        "counts": {
            "raw_occurrences": len(occurrences),
            "exact_classes": len(classes),
            "retained_states": len(retained),
            "optimizer_components": len(optimizer_counts),
            "nonunique_optimizer_components": sum(count > 1 for count in optimizer_counts),
            "repeated_parent_resources": len(repeated),
            "current_latent_resources": 1,
            "latent_latent_resources": 3,
            "maximum_owner_degree": 2,
            "maximum_latent_degree": 2,
            "child_recreation_resources": 0,
            "owner_cycle_rank": 0,
        },
        "masses": {
            "current_latent_overlap_fraction": str(current_latent_mass),
            "latent_latent_residual_fraction": str(latent_latent_mass),
            "branching_excess_fraction": str(
                current_latent_mass + latent_latent_mass
            ),
            "reference_pair_capacity_fraction": str(reference_capacity),
            "latent_to_reference_ratio_fraction": str(
                latent_latent_mass / reference_capacity
            ),
        },
        "retained_states": retained_rows,
        "repeated_resources": repeated_rows,
        "profiles": [
            {
                "current_owners": profile[0],
                "latent_owners": profile[1],
                "total_owners": profile[2],
                "resources": count,
            }
            for profile, count in sorted(profiles.items())
        ],
        "checks": {
            "parent_four_ap_free": True,
            "actual_lexicographic_deletion": True,
            "maximum_harmonic_point_disjoint_retention": True,
            "positive_latent_latent_residual": latent_latent_mass > 0,
            "one_reference_pair_insufficient": (
                latent_latent_mass > reference_capacity
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
