#!/usr/bin/env python3
"""Exhaustively verify reserve matching and recursive-export conservation."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import hashlib
import json

from reserve_recursive_export import maximum_incidence_matching

Edge = tuple[int, int]


def independent_matching_size(
    neighbors: dict[int, tuple[int, ...]],
    reserve_count: int,
) -> int:
    """Independent bitmask DP for maximum demand-to-reserve matching size."""

    reachable = {0}
    for demand in sorted(neighbors):
        updated = set(reachable)
        for used in reachable:
            for reserve in neighbors[demand]:
                bit = 1 << reserve
                if not used & bit:
                    updated.add(used | bit)
        reachable = updated
    return max(mask.bit_count() for mask in reachable) if reachable else 0


def component_profiles(vertex_count: int, edges: tuple[Edge, ...]) -> list[tuple[int, int]]:
    adjacency: dict[int, set[int]] = defaultdict(set)
    edge_indices: dict[int, list[int]] = defaultdict(list)
    for index, (left, right) in enumerate(edges):
        adjacency[left].add(right)
        adjacency[right].add(left)
        edge_indices[left].append(index)
        edge_indices[right].append(index)

    seen: set[int] = set()
    result: list[tuple[int, int]] = []
    for start in range(vertex_count):
        if start in seen or start not in adjacency:
            continue
        vertices = {start}
        indices: set[int] = set()
        seen.add(start)
        stack = [start]
        while stack:
            current = stack.pop()
            indices.update(edge_indices[current])
            for target in adjacency[current]:
                if target not in seen:
                    seen.add(target)
                    vertices.add(target)
                    stack.append(target)
        result.append((len(indices), len(vertices)))
    return result


def verify_instance(
    vertex_count: int,
    edges: tuple[Edge, ...],
    availability_mask: int,
) -> tuple[int, int]:
    neighbors: dict[int, tuple[int, ...]] = {}
    for demand, edge in enumerate(edges):
        neighbors[demand] = tuple(
            vertex for vertex in edge if availability_mask & (1 << vertex)
        )

    matching, unmatched = maximum_incidence_matching(neighbors)
    expected = independent_matching_size(neighbors, vertex_count)
    if len(matching) != expected:
        raise AssertionError(
            f"augmenting matcher is not maximum: {vertex_count=}, {edges=}, "
            f"{availability_mask=}, got={len(matching)}, expected={expected}"
        )
    if len(matching) + len(unmatched) != len(edges):
        raise AssertionError("reserve matching/export count did not conserve demands")
    if len(set(matching.values())) != len(matching):
        raise AssertionError("one physical reserve was matched twice")
    for demand, reserve in matching.items():
        if reserve not in neighbors[demand]:
            raise AssertionError("matched demand used a nonincident reserve")
    if set(matching) & set(unmatched):
        raise AssertionError("matched demand was also exported")
    if set(matching) | set(unmatched) != set(range(len(edges))):
        raise AssertionError("reserve matching/export partition is incomplete")

    if availability_mask == (1 << vertex_count) - 1:
        full_expected = sum(
            min(edge_count, component_vertices)
            for edge_count, component_vertices in component_profiles(
                vertex_count, edges
            )
        )
        if len(matching) != full_expected:
            raise AssertionError(
                "full two-choice matching did not equal component min(E,V)"
            )

    return len(matching), len(unmatched)


def main() -> int:
    simple_instances = 0
    simple_availability_tests = 0
    multigraph_instances = 0
    multigraph_availability_tests = 0
    maximum_simple_exports = 0
    maximum_multigraph_exports = 0
    availability_histogram: Counter[tuple[int, int]] = Counter()

    for vertex_count in range(1, 6):
        possible = tuple(combinations(range(vertex_count), 2))
        for edge_mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if edge_mask & (1 << index)
            )
            simple_instances += 1
            for availability_mask in range(1 << vertex_count):
                matched, exported = verify_instance(
                    vertex_count, edges, availability_mask
                )
                simple_availability_tests += 1
                maximum_simple_exports = max(maximum_simple_exports, exported)
                availability_histogram[(matched, exported)] += 1

    vertex_count = 4
    possible = tuple(combinations(range(vertex_count), 2))
    for multiplicities in product(range(3), repeat=len(possible)):
        edges = tuple(
            edge
            for edge, multiplicity in zip(possible, multiplicities, strict=True)
            for _copy in range(multiplicity)
        )
        multigraph_instances += 1
        for availability_mask in range(1 << vertex_count):
            _matched, exported = verify_instance(
                vertex_count, edges, availability_mask
            )
            multigraph_availability_tests += 1
            maximum_multigraph_exports = max(maximum_multigraph_exports, exported)

    rank_two_pattern: tuple[Edge, ...] = (
        (0, 1),
        (2, 3),
        (1, 2),
        (1, 3),
        (3, 0),
    )
    matching, unmatched = maximum_incidence_matching(
        {index: edge for index, edge in enumerate(rank_two_pattern)}
    )
    if len(matching) != 4 or len(unmatched) != 1:
        raise AssertionError("rank-two K4-minus-edge export profile changed")

    defect = Fraction(len(unmatched), 50)
    defect += Fraction(len(unmatched), 100)
    defect += Fraction(len(unmatched), 50)
    if defect != Fraction(1, 20):
        raise AssertionError("rank-two three-copy export mass changed")

    output: dict[str, object] = {
        "schema": "reserve_recursive_export_verifier_v1",
        "counts": {
            "simple_graph_instances": simple_instances,
            "simple_availability_tests": simple_availability_tests,
            "double_edge_multigraph_instances": multigraph_instances,
            "multigraph_availability_tests": multigraph_availability_tests,
            "maximum_simple_exports": maximum_simple_exports,
            "maximum_multigraph_exports": maximum_multigraph_exports,
        },
        "rank_two_pattern": {
            "edges": rank_two_pattern,
            "matched_demands": len(matching),
            "exported_demands": len(unmatched),
            "three_copy_export_mass": str(defect),
        },
        "availability_histogram_sha256": hashlib.sha256(
            json.dumps(
                [
                    (matched, exported, count)
                    for (matched, exported), count in sorted(
                        availability_histogram.items()
                    )
                ],
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
        "checks": {
            "augmenting_matching_is_maximum": True,
            "matched_reserves_are_injective": True,
            "unmatched_demands_are_exact_exports": True,
            "full_graph_match_count_is_min_edges_vertices_per_component": True,
            "capacity_deletion_conserves_every_demand": True,
            "rank_two_example_exports_one_per_component": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
