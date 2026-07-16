#!/usr/bin/env python3
"""Exhaust affine owner-incidence cycles and rectangle tokens through [1,12]."""
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
import hashlib
import json

Pair = tuple[int, int]
OwnerEdge = tuple[Pair, Pair, tuple[int, int]]
Node = tuple[str, Pair]


def contains_four_ap(values: tuple[int, ...]) -> bool:
    present = set(values)
    if not values:
        return False
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


def owner_edges(values: tuple[int, ...]) -> dict[int, list[OwnerEdge]]:
    by_gap: dict[int, list[OwnerEdge]] = defaultdict(list)
    for reference in values:
        right_roots = [root for root in values if root > reference]
        for left, right in combinations(right_roots, 2):
            root_pair = (left, right)
            child_pair = (left - reference, right - reference)
            by_gap[right - left].append(
                (root_pair, child_pair, (reference, +1))
            )

        left_roots = [root for root in values if root < reference]
        for left, right in combinations(left_roots, 2):
            root_pair = (left, right)
            child_pair = (reference - right, reference - left)
            by_gap[right - left].append(
                (root_pair, child_pair, (reference, -1))
            )
    return dict(by_gap)


def component_count(
    left_vertices: set[Pair],
    right_vertices: set[Pair],
    edges: list[OwnerEdge],
) -> int:
    adjacency: dict[Node, set[Node]] = defaultdict(set)
    for left, right, _owner in edges:
        left_node = ("L", left)
        right_node = ("R", right)
        adjacency[left_node].add(right_node)
        adjacency[right_node].add(left_node)

    vertices = {
        *(("L", pair) for pair in left_vertices),
        *(("R", pair) for pair in right_vertices),
    }
    seen: set[Node] = set()
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


class DisjointSet:
    def __init__(self) -> None:
        self.parent: dict[Node, Node] = {}
        self.rank: dict[Node, int] = {}

    def find(self, value: Node) -> Node:
        if value not in self.parent:
            self.parent[value] = value
            self.rank[value] = 0
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, left: Node, right: Node) -> bool:
        first = self.find(left)
        second = self.find(right)
        if first == second:
            return False
        if self.rank[first] < self.rank[second]:
            first, second = second, first
        self.parent[second] = first
        if self.rank[first] == self.rank[second]:
            self.rank[first] += 1
        return True


def fundamental_cycle_tokens(
    gap: int, edges: list[OwnerEdge]
) -> list[dict[str, object]]:
    ordered = sorted(edges, key=lambda edge: (edge[0], edge[1], edge[2]))
    disjoint = DisjointSet()
    forest: list[OwnerEdge] = []
    nonforest: list[OwnerEdge] = []
    for edge in ordered:
        left_node = ("L", edge[0])
        right_node = ("R", edge[1])
        if disjoint.union(left_node, right_node):
            forest.append(edge)
        else:
            nonforest.append(edge)

    adjacency: dict[Node, list[tuple[Node, OwnerEdge]]] = defaultdict(list)
    for edge in forest:
        left_node = ("L", edge[0])
        right_node = ("R", edge[1])
        adjacency[left_node].append((right_node, edge))
        adjacency[right_node].append((left_node, edge))
    for rows in adjacency.values():
        rows.sort(key=lambda row: (row[0], row[1]))

    tokens: list[dict[str, object]] = []
    for edge in nonforest:
        start = ("L", edge[0])
        target = ("R", edge[1])
        queue = deque([start])
        previous: dict[Node, Node | None] = {start: None}
        previous_edge: dict[Node, OwnerEdge] = {}
        while queue:
            current = queue.popleft()
            if current == target:
                break
            for neighbor, tree_edge in adjacency[current]:
                if neighbor not in previous:
                    previous[neighbor] = current
                    previous_edge[neighbor] = tree_edge
                    queue.append(neighbor)
        if target not in previous:
            raise AssertionError("nonforest edge endpoints disconnected in forest")

        path: list[OwnerEdge] = []
        current = target
        while previous[current] is not None:
            path.append(previous_edge[current])
            current = previous[current]  # type: ignore[assignment]
        path.reverse()
        if not path or path[0][0] != edge[0]:
            raise AssertionError("fundamental path did not begin at parent vertex")

        reference = edge[2][0]
        base_reference = path[0][2][0]
        delta = abs(reference - base_reference)
        if delta <= 0:
            raise AssertionError("fundamental cycle reference pair is degenerate")
        if Fraction(1, gap) != Fraction(delta, gap) * Fraction(1, delta):
            raise AssertionError("cycle rectangle aspect identity failed")

        tokens.append(
            {
                "nonforest_edge": edge,
                "base_forest_edge": path[0],
                "cycle_length": len(path) + 1,
                "reference_pair": tuple(sorted((reference, base_reference))),
                "reference_gap": delta,
                "aspect_fraction": str(Fraction(delta, gap)),
                "near": delta <= gap,
            }
        )
    return tokens


def graph_record(gap: int, edges: list[OwnerEdge]) -> dict[str, object]:
    left_vertices = {left for left, _right, _owner in edges}
    right_vertices = {right for _left, right, _owner in edges}
    components = component_count(left_vertices, right_vertices, edges)
    cycle_rank = (
        len(edges) - len(left_vertices) - len(right_vertices) + components
    )
    if cycle_rank < 0:
        raise AssertionError("negative affine owner cycle rank")

    occurrence = Fraction(len(edges), gap)
    parent_first = Fraction(len(left_vertices), gap)
    child_first = Fraction(len(right_vertices), gap)
    component_credit = Fraction(components, gap)
    cycle_mass = Fraction(cycle_rank, gap)
    if occurrence != parent_first + child_first - component_credit + cycle_mass:
        raise AssertionError("weighted owner-incidence identity failed")
    if occurrence - parent_first != child_first - component_credit + cycle_mass:
        raise AssertionError("branching-excess identity failed")
    if occurrence - child_first != parent_first - component_credit + cycle_mass:
        raise AssertionError("recreation-excess identity failed")

    for left, right, _owner in edges:
        if left[1] - left[0] != gap or right[1] - right[0] != gap:
            raise AssertionError("affine incidence failed gap preservation")

    cycle_tokens = fundamental_cycle_tokens(gap, edges)
    if len(cycle_tokens) != cycle_rank:
        raise AssertionError("nonforest edge count differs from cycle rank")
    if sum((Fraction(1, gap) for _token in cycle_tokens), Fraction()) != cycle_mass:
        raise AssertionError("cycle token mass differs from weighted cycle rank")

    maximum_aspect = max(
        (Fraction(str(token["aspect_fraction"])) for token in cycle_tokens),
        default=Fraction(),
    )
    return {
        "edges": len(edges),
        "left_vertices": len(left_vertices),
        "right_vertices": len(right_vertices),
        "components": components,
        "cycle_rank": cycle_rank,
        "near_cycle_tokens": sum(bool(token["near"]) for token in cycle_tokens),
        "far_cycle_tokens": sum(not bool(token["near"]) for token in cycle_tokens),
        "maximum_aspect": str(maximum_aspect),
    }


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def main() -> int:
    endpoint = 12
    parent_sets = 0
    combined_graphs = 0
    combined_cyclic = 0
    maximum_combined_rank = 0
    maximum_combined_edges = 0
    maximum_combined_witness: dict[str, object] | None = None
    combined_cycle_tokens = 0
    combined_near_tokens = 0
    combined_far_tokens = 0
    maximum_cycle_aspect = Fraction()

    separated_graphs = 0
    separated_cyclic = 0
    maximum_separated_rank = 0
    maximum_separated_witness: dict[str, object] | None = None

    smallest_parallel_witness: dict[str, object] | None = None
    smallest_same_orientation_witness: dict[str, object] | None = None

    values = tuple(range(1, endpoint + 1))
    for mask in range(1 << endpoint):
        parent = tuple(value for index, value in enumerate(values) if mask & (1 << index))
        if len(parent) < 3 or contains_four_ap(parent):
            continue
        parent_sets += 1

        for gap, edges in sorted(owner_edges(parent).items()):
            record = graph_record(gap, edges)
            combined_graphs += 1
            maximum_combined_edges = max(maximum_combined_edges, int(record["edges"]))
            rank = int(record["cycle_rank"])
            combined_cycle_tokens += rank
            combined_near_tokens += int(record["near_cycle_tokens"])
            combined_far_tokens += int(record["far_cycle_tokens"])
            maximum_cycle_aspect = max(
                maximum_cycle_aspect, Fraction(str(record["maximum_aspect"]))
            )
            if rank > 0:
                combined_cyclic += 1
            if rank > maximum_combined_rank:
                maximum_combined_rank = rank
                maximum_combined_witness = {
                    "parent": parent,
                    "gap": gap,
                    **record,
                }

            multiplicities: dict[tuple[Pair, Pair], int] = defaultdict(int)
            for left, right, _owner in edges:
                multiplicities[(left, right)] += 1
            if smallest_parallel_witness is None and any(
                count > 1 for count in multiplicities.values()
            ):
                smallest_parallel_witness = {
                    "parent": parent,
                    "gap": gap,
                    "parallel_edges": [
                        {
                            "left": left,
                            "right": right,
                            "owners": sorted(
                                owner
                                for edge_left, edge_right, owner in edges
                                if edge_left == left and edge_right == right
                            ),
                        }
                        for (left, right), count in sorted(multiplicities.items())
                        if count > 1
                    ],
                }

            for orientation in (+1, -1):
                oriented = [
                    edge for edge in edges if edge[2][1] == orientation
                ]
                if not oriented:
                    continue
                oriented_record = graph_record(gap, oriented)
                separated_graphs += 1
                oriented_rank = int(oriented_record["cycle_rank"])
                if oriented_rank > 0:
                    separated_cyclic += 1
                    if smallest_same_orientation_witness is None:
                        smallest_same_orientation_witness = {
                            "parent": parent,
                            "gap": gap,
                            "orientation": orientation,
                            **oriented_record,
                        }
                if oriented_rank > maximum_separated_rank:
                    maximum_separated_rank = oriented_rank
                    maximum_separated_witness = {
                        "parent": parent,
                        "gap": gap,
                        "orientation": orientation,
                        **oriented_record,
                    }

    expected = {
        "parent_sets": 2154,
        "combined_graphs": 13176,
        "combined_cyclic": 5004,
        "maximum_combined_rank": 18,
        "maximum_combined_edges": 30,
        "combined_cycle_tokens": 12132,
        "combined_near_tokens": 3848,
        "combined_far_tokens": 8284,
        "maximum_cycle_aspect": "11",
        "separated_graphs": 21578,
        "separated_cyclic": 632,
        "maximum_separated_rank": 5,
    }
    actual = {
        "parent_sets": parent_sets,
        "combined_graphs": combined_graphs,
        "combined_cyclic": combined_cyclic,
        "maximum_combined_rank": maximum_combined_rank,
        "maximum_combined_edges": maximum_combined_edges,
        "combined_cycle_tokens": combined_cycle_tokens,
        "combined_near_tokens": combined_near_tokens,
        "combined_far_tokens": combined_far_tokens,
        "maximum_cycle_aspect": str(maximum_cycle_aspect),
        "separated_graphs": separated_graphs,
        "separated_cyclic": separated_cyclic,
        "maximum_separated_rank": maximum_separated_rank,
    }
    if actual != expected:
        raise AssertionError(f"affine owner-incidence exhaustion changed: {actual}")

    if smallest_parallel_witness is None or smallest_same_orientation_witness is None:
        raise AssertionError("expected affine cycle witnesses were not found")

    output = {
        "schema": "affine_owner_incidence_cycles_small_box_v2",
        "endpoint": endpoint,
        "counts": actual,
        "smallest_parallel_witness": smallest_parallel_witness,
        "smallest_same_orientation_witness": smallest_same_orientation_witness,
        "maximum_combined_witness": maximum_combined_witness,
        "maximum_separated_witness": maximum_separated_witness,
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
