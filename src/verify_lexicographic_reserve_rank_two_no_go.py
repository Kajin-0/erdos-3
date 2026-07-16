#!/usr/bin/env python3
"""Verify a policy-compatible rank-two center/opposite reserve obstruction."""
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
    for left, second in combinations(values, 2):
        step = second - left
        if left + 2 * step in present and left + 3 * step in present:
            return True
    return False


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate rank-two reserve pair")
    return (left, right) if left < right else (right, left)


def orientation(step: int) -> int:
    valuation = 0
    value = step
    while value % 2 == 0:
        valuation += 1
        value //= 2
    return 1 if valuation % 2 == 0 else -1


def retained_family(parent: tuple[int, ...]) -> tuple[tuple[object, ...], tuple[int, ...]]:
    selected, residual = resolve_lexicographic(frozenset(parent))
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
    return retained, tuple(optimizer_counts)


def graph_components(
    edges: list[dict[str, object]],
) -> list[dict[str, object]]:
    adjacency: dict[Pair, list[tuple[Pair, int]]] = defaultdict(list)
    for index, edge in enumerate(edges):
        left = edge["center_reserve"]
        right = edge["opposite_reserve"]
        if not isinstance(left, tuple) or not isinstance(right, tuple):
            raise AssertionError("invalid reserve edge")
        adjacency[left].append((right, index))
        adjacency[right].append((left, index))

    seen: set[Pair] = set()
    result: list[dict[str, object]] = []
    for start in sorted(adjacency):
        if start in seen:
            continue
        vertices = {start}
        edge_indices: set[int] = set()
        seen.add(start)
        stack = [start]
        while stack:
            current = stack.pop()
            for target, edge_index in adjacency[current]:
                edge_indices.add(edge_index)
                if target not in seen:
                    seen.add(target)
                    vertices.add(target)
                    stack.append(target)

        gaps = {right - left for left, right in vertices}
        if len(gaps) != 1:
            raise AssertionError("reserve component mixed gaps")
        gap = gaps.pop()
        cycle_rank = len(edge_indices) - len(vertices) + 1
        if cycle_rank < 0:
            raise AssertionError("negative reserve cycle rank")
        result.append(
            {
                "vertices": tuple(sorted(vertices)),
                "edge_indices": tuple(sorted(edge_indices)),
                "edges": len(edge_indices),
                "vertex_count": len(vertices),
                "cycle_rank": cycle_rank,
                "gap": gap,
                "defect": Fraction(max(0, len(edge_indices) - len(vertices)), gap),
            }
        )
    return result


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def json_value(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, tuple):
        return [json_value(item) for item in value]
    if isinstance(value, list):
        return [json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    return value


def main() -> int:
    parent = (
        1,
        9194,
        9200,
        9206,
        10595,
        10600,
        10605,
        11296,
        11300,
        11304,
        11599,
        11600,
        11601,
        11996,
        11997,
        11999,
        12000,
        12001,
        12004,
        12005,
        12006,
        12012,
        12046,
        12047,
        12049,
        12050,
        12051,
        12054,
        12055,
        12056,
        12062,
        12096,
        12097,
        12099,
        12100,
        12101,
        12104,
        12105,
        12106,
        12112,
    )
    if contains_four_ap(parent):
        raise AssertionError("rank-two reserve parent contains a four-AP")

    selected, residual = resolve_lexicographic(frozenset(parent))
    selected_set = set(selected)
    required_actions: set[tuple[int, ...]] = {
        (11599, 11600, 11601, 1, 11599, 11601),
        (11296, 11300, 11304, 4, 11296, 11304),
        (10595, 10600, 10605, 5, 10595, 10605),
        (9206, 9200, 9194, 6, 9194, 9206),
    }
    for base in (12000, 12050, 12100):
        required_actions.update(
            {
                (base - 1, base, base + 1, 1, base - 1, base + 1),
                (base + 4, base + 5, base + 6, 1, base + 4, base + 6),
                (base - 3, base + 1, base + 5, 4, base - 3, base + 5),
                (base - 4, base + 1, base + 6, 5, base - 4, base + 6),
                (base + 12, base + 6, base, 6, base, base + 12),
            }
        )
    if not required_actions <= selected_set:
        missing = sorted(required_actions - selected_set)
        raise AssertionError(f"required selected actions disappeared: {missing}")

    retained, optimizer_counts = retained_family(parent)
    if len(retained) != 7:
        raise AssertionError("rank-two retained state count changed")

    expected_middle = {
        1: (
            (400, 405, 450, 455, 500, 505),
            (11999, 12004, 12049, 12054, 12099, 12104),
        ),
        4: ((701, 751, 801), (11997, 12047, 12097)),
        5: ((1401, 1451, 1501), (11996, 12046, 12096)),
        6: ((2806, 2856, 2906), (12012, 12062, 12112)),
    }
    retained_rows: list[dict[str, object]] = []
    recursive_states: list[object] = []
    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        terminal = not contains_three_term_ap(values)
        source = str(state.representative.source)
        step = state.representative.source_step
        retained_rows.append(
            {
                "state_index": int(state.index),
                "source": source,
                "source_step": step,
                "exponent": int(state.representative.exponent),
                "terminal": terminal,
                "values": values,
                "roots": roots,
                "weight": fraction_text(state.weight),
            }
        )
        if not terminal:
            recursive_states.append(state)

    for step, (values, roots) in expected_middle.items():
        matching = [
            row
            for row in retained_rows
            if row["source"] == "middle_fiber" and row["source_step"] == step
        ]
        if len(matching) != 1:
            raise AssertionError(f"step-{step} retained middle state changed")
        if matching[0]["values"] != values or matching[0]["roots"] != roots:
            raise AssertionError(f"step-{step} retained middle payload changed")
        if matching[0]["terminal"]:
            raise AssertionError(f"step-{step} retained middle state became terminal")

    backbone_rows = [row for row in retained_rows if row["source"] == "backbone"]
    if len(backbone_rows) != 1 or backbone_rows[0]["terminal"]:
        raise AssertionError("rank-two retained backbone changed")

    latent_owners: dict[Resource, list[dict[str, object]]] = defaultdict(list)
    for state in recursive_states:
        roots = tuple(int(root) for root in state.representative.provenance)
        source = str(state.representative.source)
        step = state.representative.source_step
        for left, right in combinations(roots, 2):
            resource = ordered_pair(left, right)
            latent_owners[resource].append(
                {
                    "state_index": int(state.index),
                    "source": source,
                    "source_step": step,
                }
            )

    duplicate_edges: list[dict[str, object]] = []
    latent_residual = Fraction()
    for resource, owners in sorted(latent_owners.items()):
        if len(owners) <= 1:
            continue
        if len(owners) != 2:
            raise AssertionError("latent degree exceeded two")
        sources = sorted(str(owner["source"]) for owner in owners)
        if sources != ["backbone", "middle_fiber"]:
            raise AssertionError("duplicate was not backbone-middle")
        middle = next(owner for owner in owners if owner["source"] == "middle_fiber")
        step = int(middle["source_step"])
        sign = orientation(step)
        center = ordered_pair(
            resource[0] + sign * step,
            resource[1] + sign * step,
        )
        opposite = ordered_pair(
            resource[0] + 2 * sign * step,
            resource[1] + 2 * sign * step,
        )
        if not set(center) <= set(parent) or not set(opposite) <= set(parent):
            raise AssertionError("reserve left parent support")
        gap = resource[1] - resource[0]
        if center[1] - center[0] != gap or opposite[1] - opposite[0] != gap:
            raise AssertionError("reserve changed gap")
        latent_residual += Fraction(1, gap)
        duplicate_edges.append(
            {
                "demand": resource,
                "gap": gap,
                "step": step,
                "owners": owners,
                "center_reserve": center,
                "opposite_reserve": opposite,
            }
        )

    if len(duplicate_edges) != 24:
        raise AssertionError("rank-two duplicate demand count changed")
    if latent_residual != Fraction(250399, 263340):
        raise AssertionError("rank-two latent residual changed")

    reserve_components = graph_components(duplicate_edges)
    rank_two = [component for component in reserve_components if component["cycle_rank"] >= 2]
    expected_bad_vertices = {
        (
            (12000, 12050),
            (12001, 12051),
            (12005, 12055),
            (12006, 12056),
        ),
        (
            (12000, 12100),
            (12001, 12101),
            (12005, 12105),
            (12006, 12106),
        ),
        (
            (12050, 12100),
            (12051, 12101),
            (12055, 12105),
            (12056, 12106),
        ),
    }
    if len(reserve_components) != 12:
        raise AssertionError("rank-two reserve component count changed")
    if len(rank_two) != 3:
        raise AssertionError("rank-two reserve obstruction count changed")
    if {component["vertices"] for component in rank_two} != expected_bad_vertices:
        raise AssertionError("rank-two reserve vertices changed")
    if any(
        component["edges"] != 5
        or component["vertex_count"] != 4
        or component["cycle_rank"] != 2
        for component in rank_two
    ):
        raise AssertionError("rank-two reserve component profile changed")

    defect = sum((component["defect"] for component in reserve_components), Fraction())
    if defect != Fraction(1, 20):
        raise AssertionError("rank-two reserve defect changed")
    bad_profile = Counter(
        (
            int(component["gap"]),
            int(component["edges"]),
            int(component["vertex_count"]),
            int(component["cycle_rank"]),
        )
        for component in rank_two
    )
    if bad_profile != Counter({(50, 5, 4, 2): 2, (100, 5, 4, 2): 1}):
        raise AssertionError("rank-two component histogram changed")

    serial_components = json_value(reserve_components)
    serial_edges = json_value(duplicate_edges)
    output: dict[str, object] = {
        "schema": "lexicographic_reserve_rank_two_no_go_v1",
        "parent": parent,
        "selected_actions": len(selected),
        "terminal_residual": tuple(sorted(residual)),
        "counts": {
            "retained_states": len(retained),
            "recursive_states": len(recursive_states),
            "optimizer_components": len(optimizer_counts),
            "nonunique_optimizer_components": sum(count > 1 for count in optimizer_counts),
            "duplicated_latent_demands": len(duplicate_edges),
            "reserve_vertices": len(
                {
                    vertex
                    for edge in duplicate_edges
                    for vertex in (edge["center_reserve"], edge["opposite_reserve"])
                }
            ),
            "reserve_components": len(reserve_components),
            "rank_two_components": len(rank_two),
            "maximum_cycle_rank": max(
                int(component["cycle_rank"]) for component in reserve_components
            ),
        },
        "masses": {
            "latent_residual": fraction_text(latent_residual),
            "two_choice_reserve_defect": fraction_text(defect),
        },
        "retained_states": json_value(retained_rows),
        "duplicate_edges": serial_edges,
        "reserve_components": serial_components,
        "checks": {
            "parent_four_ap_free": True,
            "actual_lexicographic_deletion": True,
            "maximum_harmonic_point_disjoint_retention": True,
            "latent_degree_at_most_two": True,
            "three_rank_two_components": len(rank_two) == 3,
            "pseudoforest_conjecture_false": defect > 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
