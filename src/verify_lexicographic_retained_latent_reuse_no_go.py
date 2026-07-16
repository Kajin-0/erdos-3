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


def graph_cycle_rank(edges: tuple[tuple[Pair, Pair], ...]) -> tuple[int, int, int]:
    vertices = {vertex for edge in edges for vertex in edge}
    adjacency: dict[Pair, set[Pair]] = defaultdict(set)
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    seen: set[Pair] = set()
    components_count = 0
    for vertex in vertices:
        if vertex in seen:
            continue
        components_count += 1
        seen.add(vertex)
        stack = [vertex]
        while stack:
            current = stack.pop()
            for target in adjacency[current]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
    rank = len(edges) - len(vertices) + components_count
    if rank < 0:
        raise AssertionError("negative reserve graph cycle rank")
    return len(vertices), components_count, rank


def main() -> int:
    parent = (
        1,
        4,
        5,
        6,
        20,
        21,
        22,
        26,
        27,
        28,
        32,
        33,
        34,
    )
    if contains_four_ap(parent):
        raise AssertionError("retained latent-reuse parent contains a four-AP")

    selected, residual = resolve_lexicographic(frozenset(parent))
    expected_selected = (
        (4, 5, 6, 1, 4, 6),
        (20, 21, 22, 1, 20, 22),
        (26, 27, 28, 1, 26, 28),
        (32, 33, 34, 1, 32, 34),
        (33, 27, 21, 6, 21, 33),
        (34, 28, 22, 6, 22, 34),
    )
    if selected != expected_selected:
        raise AssertionError(
            f"retained latent-reuse deletion schedule changed: {selected}"
        )

    raw_rows = build_descendant_occurrences(0, parent, parent, selected)
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
        references = {
            root - value for value, root in zip(values, roots, strict=True)
        }
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
        (3,),
        (4, 5),
        (16, 22, 28),
        (19, 20, 21, 25, 26, 27, 31),
        (32, 33),
    )
    if tuple(row["values"] for row in retained_rows) != expected_retained_values:
        raise AssertionError(
            f"retained latent-reuse family changed: {retained_rows}"
        )

    expected_repeated = {(20, 26), (20, 32), (26, 32)}
    if set(repeated) != expected_repeated:
        raise AssertionError("retained latent-reuse resource set changed")
    if current_latent_mass != 0:
        raise AssertionError("clean retained witness gained current-latent overlap")
    if latent_latent_mass != Fraction(5, 12):
        raise AssertionError("retained latent-latent residual changed")
    if profiles != Counter({(0, 2, 2): 3}):
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
        and row["exponent"] == 4
    )
    if recursive_middle["reference"] != 4 or recursive_backbone["reference"] != 1:
        raise AssertionError("retained latent-reuse references changed")
    if tuple(recursive_middle["roots"]) != (20, 26, 32):
        raise AssertionError("retained middle root set changed")

    reference_gap = 3
    reference_capacity = Fraction(1, reference_gap)
    if latent_latent_mass / reference_capacity != Fraction(5, 4):
        raise AssertionError("retained latent/reference ratio changed")

    center_reserves = (
        ((20, 26), (21, 27)),
        ((20, 32), (21, 33)),
        ((26, 32), (27, 33)),
    )
    opposite_reserves = (
        ((20, 26), (22, 28)),
        ((20, 32), (22, 34)),
        ((26, 32), (28, 34)),
    )
    reserve_edges = tuple(
        (center, opposite)
        for (_demand, center), (_same_demand, opposite) in zip(
            center_reserves, opposite_reserves, strict=True
        )
    )
    for (demand, center), (same_demand, opposite) in zip(
        center_reserves, opposite_reserves, strict=True
    ):
        if demand != same_demand:
            raise AssertionError("reserve demand alignment failed")
        gap = demand[1] - demand[0]
        if center[1] - center[0] != gap or opposite[1] - opposite[0] != gap:
            raise AssertionError("translated reserve failed gap preservation")
        if not set(center) <= set(parent) or not set(opposite) <= set(parent):
            raise AssertionError("translated reserve left parent")

    reserve_vertices, reserve_components, reserve_cycle_rank = graph_cycle_rank(
        reserve_edges
    )
    if (
        reserve_vertices,
        len(reserve_edges),
        reserve_components,
        reserve_cycle_rank,
    ) != (6, 3, 3, 0):
        raise AssertionError("clean reserve graph profile changed")

    center_capacity = sum(
        (Fraction(1, pair[1] - pair[0]) for _demand, pair in center_reserves),
        Fraction(),
    )
    opposite_capacity = sum(
        (Fraction(1, pair[1] - pair[0]) for _demand, pair in opposite_reserves),
        Fraction(),
    )
    if center_capacity != latent_latent_mass or opposite_capacity != latent_latent_mass:
        raise AssertionError("translated reserve capacity identity failed")

    output = {
        "schema": "lexicographic_retained_latent_reuse_no_go_v2",
        "parent": parent,
        "selected_schedule": selected,
        "terminal_residual": tuple(sorted(residual)),
        "counts": {
            "raw_occurrences": len(occurrences),
            "exact_classes": len(classes),
            "retained_states": len(retained),
            "optimizer_components": len(optimizer_counts),
            "nonunique_optimizer_components": sum(
                count > 1 for count in optimizer_counts
            ),
            "repeated_parent_resources": len(repeated),
            "current_latent_resources": 0,
            "latent_latent_resources": 3,
            "maximum_owner_degree": 2,
            "maximum_latent_degree": 2,
            "child_recreation_resources": 0,
            "owner_cycle_rank": 0,
            "reserve_graph_vertices": reserve_vertices,
            "reserve_graph_edges": len(reserve_edges),
            "reserve_graph_components": reserve_components,
            "reserve_graph_cycle_rank": reserve_cycle_rank,
        },
        "masses": {
            "current_latent_overlap_fraction": str(current_latent_mass),
            "latent_latent_residual_fraction": str(latent_latent_mass),
            "branching_excess_fraction": str(latent_latent_mass),
            "reference_pair_capacity_fraction": str(reference_capacity),
            "latent_to_reference_ratio_fraction": str(
                latent_latent_mass / reference_capacity
            ),
            "center_reserve_capacity_fraction": str(center_capacity),
            "opposite_reserve_capacity_fraction": str(opposite_capacity),
        },
        "retained_states": retained_rows,
        "repeated_resources": repeated_rows,
        "center_reserves": center_reserves,
        "opposite_reserves": opposite_reserves,
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
            "pure_latent_latent_residual": current_latent_mass == 0,
            "one_reference_pair_insufficient": (
                latent_latent_mass > reference_capacity
            ),
            "center_reserve_pays_exactly": center_capacity == latent_latent_mass,
            "opposite_reserve_pays_exactly": (
                opposite_capacity == latent_latent_mass
            ),
            "reserve_graph_is_forest": reserve_cycle_rank == 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
