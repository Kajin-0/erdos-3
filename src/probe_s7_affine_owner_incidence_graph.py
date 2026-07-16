#!/usr/bin/env python3
"""Profile affine owner incidence on the certified split R4->F5 retained family."""
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
    pair_weight,
    retain_occurrences,
)
from probe_sponsor_pair_transport_frontier import serialize_mass
from probe_sponsor_pair_transport_frontier import reconstruct_fourth_recursive
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]
LeftVertex = tuple[int, int, int]
RightVertex = Pair


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate affine owner pair")
    return (left, right) if left < right else (right, left)


def connected_components(
    left_vertices: set[LeftVertex],
    right_vertices: set[RightVertex],
    edges: list[tuple[LeftVertex, RightVertex, int, int, str]],
) -> int:
    adjacency: dict[tuple[str, object], set[tuple[str, object]]] = defaultdict(set)
    for left, right, _state, _reference, _kind in edges:
        left_node = ("L", left)
        right_node = ("R", right)
        adjacency[left_node].add(right_node)
        adjacency[right_node].add(left_node)

    vertices = {
        *(("L", vertex) for vertex in left_vertices),
        *(("R", vertex) for vertex in right_vertices),
    }
    seen: set[tuple[str, object]] = set()
    components = 0
    for vertex in vertices:
        if vertex in seen:
            continue
        components += 1
        seen.add(vertex)
        stack = [vertex]
        while stack:
            current = stack.pop()
            for target in adjacency[current]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
    return components


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: probe_s7_affine_owner_incidence_graph.py OUTPUT_JSON"
        )

    parents = reconstruct_fourth_recursive()
    parent_roots = {
        parent.index: set(parent.representative.provenance) for parent in parents
    }
    retained, metrics = retain_occurrences(build_split_occurrences(parents))
    if metrics["retained_states"] != 37:
        raise AssertionError("certified split retained frontier changed")

    edges_by_gap: dict[
        int, list[tuple[LeftVertex, RightVertex, int, int, str]]
    ] = defaultdict(list)
    left_owners: dict[LeftVertex, list[tuple[int, int, RightVertex, str]]] = defaultdict(list)
    right_owners: dict[RightVertex, list[tuple[LeftVertex, int, int, str]]] = defaultdict(list)

    for state in retained:
        parent_class = int(state.representative.parent_class)
        reference = affine_reference(state)
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        if reference not in parent_roots[parent_class]:
            raise AssertionError("affine reference left parent root universe")
        if any(root - value != reference for value, root in zip(values, roots, strict=True)):
            raise AssertionError("affine root/value alignment changed")

        terminal = not contains_three_term_ap(values)
        for value, root in zip(values, roots, strict=True):
            root_pair = ordered_pair(reference, root)
            child_pair = (0, value)
            gap = value
            if root_pair[1] - root_pair[0] != gap:
                raise AssertionError("current affine owner failed gap preservation")
            left = (parent_class, root_pair[0], root_pair[1])
            edge = (left, child_pair, state.index, reference, "current")
            edges_by_gap[gap].append(edge)
            left_owners[left].append((state.index, reference, child_pair, "current"))
            right_owners[child_pair].append((left, state.index, reference, "current"))

        if terminal:
            continue
        for first, second in combinations(range(len(values)), 2):
            root_pair = ordered_pair(roots[first], roots[second])
            child_pair = ordered_pair(values[first], values[second])
            gap = child_pair[1] - child_pair[0]
            if root_pair[1] - root_pair[0] != gap:
                raise AssertionError("latent affine owner failed gap preservation")
            left = (parent_class, root_pair[0], root_pair[1])
            edge = (left, child_pair, state.index, reference, "latent")
            edges_by_gap[gap].append(edge)
            left_owners[left].append((state.index, reference, child_pair, "latent"))
            right_owners[child_pair].append((left, state.index, reference, "latent"))

    occurrence_mass = Fraction()
    parent_first_mass = Fraction()
    child_first_mass = Fraction()
    component_credit = Fraction()
    cycle_mass = Fraction()
    total_components = 0
    total_cycle_rank = 0
    cyclic_gap_graphs = 0
    maximum_gap_cycle_rank = 0

    gap_rows: list[dict[str, object]] = []
    for gap, edges in sorted(edges_by_gap.items()):
        left_vertices = {edge[0] for edge in edges}
        right_vertices = {edge[1] for edge in edges}
        components = connected_components(left_vertices, right_vertices, edges)
        beta = len(edges) - len(left_vertices) - len(right_vertices) + components
        if beta < 0:
            raise AssertionError("negative exact S7 owner cycle rank")

        occurrence = Fraction(len(edges), gap)
        parent_first = Fraction(len(left_vertices), gap)
        child_first = Fraction(len(right_vertices), gap)
        component = Fraction(components, gap)
        cycles = Fraction(beta, gap)
        if occurrence != parent_first + child_first - component + cycles:
            raise AssertionError("exact S7 owner graph identity failed")

        occurrence_mass += occurrence
        parent_first_mass += parent_first
        child_first_mass += child_first
        component_credit += component
        cycle_mass += cycles
        total_components += components
        total_cycle_rank += beta
        if beta:
            cyclic_gap_graphs += 1
        maximum_gap_cycle_rank = max(maximum_gap_cycle_rank, beta)
        gap_rows.append(
            {
                "gap": gap,
                "edges": len(edges),
                "parent_vertices": len(left_vertices),
                "child_vertices": len(right_vertices),
                "components": components,
                "cycle_rank": beta,
            }
        )

    maximum_child_degree = max((len(rows) for rows in right_owners.values()), default=0)
    maximum_parent_degree = max((len(rows) for rows in left_owners.values()), default=0)
    repeated_parent_vertices = {
        left: rows for left, rows in left_owners.items() if len(rows) > 1
    }
    recreated_child_vertices = {
        right: rows for right, rows in right_owners.items() if len(rows) > 1
    }

    branching_excess = sum(
        (
            Fraction(len(rows) - 1, left[2] - left[1])
            for left, rows in repeated_parent_vertices.items()
        ),
        Fraction(),
    )
    recreation_excess = sum(
        (
            Fraction(len(rows) - 1, right[1] - right[0])
            for right, rows in recreated_child_vertices.items()
        ),
        Fraction(),
    )
    if occurrence_mass - parent_first_mass != branching_excess:
        raise AssertionError("exact branching excess identity failed")
    if occurrence_mass - child_first_mass != recreation_excess:
        raise AssertionError("exact recreation excess identity failed")

    rectangle_token_usage: Counter[tuple[int, Pair]] = Counter()
    rectangle_rows: list[dict[str, object]] = []
    rectangle_collision_mass = Fraction()
    reference_pair_occurrence_mass = Fraction()
    near_collision_mass = Fraction()
    far_collision_mass = Fraction()

    for left, rows in sorted(repeated_parent_vertices.items()):
        references = sorted({reference for _state, reference, _child, _kind in rows})
        if len(references) != len(rows):
            raise AssertionError(
                "one retained reference emitted the same parent resource twice"
            )
        base = references[0]
        gap = left[2] - left[1]
        for state_index, reference, child_pair, kind in sorted(rows):
            if reference == base:
                continue
            reference_pair = ordered_pair(base, reference)
            if not set(reference_pair) <= parent_roots[left[0]]:
                raise AssertionError("reference rectangle left parent root universe")
            delta = reference_pair[1] - reference_pair[0]
            rectangle_token_usage[(left[0], reference_pair)] += 1
            rectangle_collision_mass += Fraction(1, gap)
            reference_pair_occurrence_mass += Fraction(1, delta)
            if delta <= gap:
                near_collision_mass += Fraction(1, gap)
            else:
                far_collision_mass += Fraction(1, gap)
            rectangle_rows.append(
                {
                    "parent_resource": left,
                    "state_index": state_index,
                    "reference_pair": reference_pair,
                    "child_pair": child_pair,
                    "resource_kind": kind,
                    "pair_gap": gap,
                    "reference_gap": delta,
                    "aspect_fraction": str(Fraction(delta, gap)),
                }
            )

    if rectangle_collision_mass != branching_excess:
        raise AssertionError("rectangle rows do not equal repeated parent-resource mass")
    if near_collision_mass + far_collision_mass != branching_excess:
        raise AssertionError("near/far rectangle split failed")

    reference_pair_union_mass = sum(
        (
            pair_weight(pair)
            for _parent_class, pair in rectangle_token_usage
        ),
        Fraction(),
    )
    repeated_reference_tokens = sum(
        count > 1 for count in rectangle_token_usage.values()
    )
    maximum_reference_token_reuse = max(
        rectangle_token_usage.values(), default=0
    )

    # Point-disjoint retained states make every numerical child resource unique.
    if maximum_child_degree != 1 or recreated_child_vertices:
        raise AssertionError("certified retained child resource recreation changed")
    if total_cycle_rank != 0 or cycle_mass:
        raise AssertionError("certified retained owner graph is no longer a forest")
    if total_components != len(left_owners):
        raise AssertionError("owner forest components no longer equal parent resources")

    output = {
        "schema": "s7_affine_owner_incidence_graph_v1",
        "scope": "certified residual-sponsor split R4-to-F5 retained family",
        "generation_six_propagated": False,
        "counts": {
            "retained_states": len(retained),
            "gap_graphs": len(gap_rows),
            "owner_edges": sum(len(edges) for edges in edges_by_gap.values()),
            "parent_resource_vertices": len(left_owners),
            "child_resource_vertices": len(right_owners),
            "components": total_components,
            "cycle_rank": total_cycle_rank,
            "cyclic_gap_graphs": cyclic_gap_graphs,
            "maximum_gap_cycle_rank": maximum_gap_cycle_rank,
            "repeated_parent_resources": len(repeated_parent_vertices),
            "recreated_child_resources": len(recreated_child_vertices),
            "maximum_parent_degree": maximum_parent_degree,
            "maximum_child_degree": maximum_child_degree,
            "rectangle_occurrences": len(rectangle_rows),
            "distinct_reference_pair_tokens": len(rectangle_token_usage),
            "repeated_reference_pair_tokens": repeated_reference_tokens,
            "maximum_reference_pair_reuse": maximum_reference_token_reuse,
        },
        "masses": {
            "occurrence_resource_mass": serialize_mass(occurrence_mass),
            "parent_first_appearance_mass": serialize_mass(parent_first_mass),
            "child_first_appearance_mass": serialize_mass(child_first_mass),
            "component_credit": serialize_mass(component_credit),
            "cycle_mass": serialize_mass(cycle_mass),
            "branching_excess": serialize_mass(branching_excess),
            "recreation_excess": serialize_mass(recreation_excess),
            "near_rectangle_collision_mass": serialize_mass(near_collision_mass),
            "far_rectangle_collision_mass": serialize_mass(far_collision_mass),
            "reference_pair_occurrence_mass": serialize_mass(reference_pair_occurrence_mass),
            "reference_pair_union_mass": serialize_mass(reference_pair_union_mass),
        },
        "gap_rows": gap_rows,
        "hashes": {
            "gap_rows": canonical_hash(gap_rows),
            "rectangle_rows": canonical_hash(rectangle_rows),
            "reference_token_usage": canonical_hash(
                [
                    (parent_class, pair, count)
                    for (parent_class, pair), count in sorted(
                        rectangle_token_usage.items()
                    )
                ]
            ),
        },
        "checks": {
            "weighted_cycle_identity": (
                occurrence_mass
                == parent_first_mass
                + child_first_mass
                - component_credit
                + cycle_mass
            ),
            "owner_graph_is_forest": total_cycle_rank == 0,
            "no_child_resource_recreation": maximum_child_degree == 1,
            "rectangle_mass_equals_branching_excess": (
                rectangle_collision_mass == branching_excess
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
