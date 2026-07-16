#!/usr/bin/env python3
"""Search retained center/opposite reserve graphs for a rank-two component."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

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


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate reserve-search pair")
    return (left, right) if left < right else (right, left)


def orientation(step: int) -> int:
    valuation = 0
    value = step
    while value % 2 == 0:
        valuation += 1
        value //= 2
    return 1 if valuation % 2 == 0 else -1


def retained_family(parent: tuple[int, ...]) -> tuple[object, ...]:
    selected, _residual = resolve_lexicographic(frozenset(parent))
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
    for component in components(adjacency):
        _weight, _count, choice, _states = maximum_weight_independent_set_dp(
            component, classes, adjacency
        )
        retained_indices.extend(choice)
    return tuple(classes[index] for index in sorted(retained_indices))


def graph_components(
    edges: list[tuple[Pair, Pair, Resource, int, int]],
) -> list[dict[str, object]]:
    adjacency: dict[Pair, list[tuple[Pair, int]]] = defaultdict(list)
    for index, (left, right, _demand, _step, _sign) in enumerate(edges):
        adjacency[left].append((right, index))
        adjacency[right].append((left, index))

    seen_vertices: set[Pair] = set()
    seen_edges: set[int] = set()
    result: list[dict[str, object]] = []
    for start in sorted(adjacency):
        if start in seen_vertices:
            continue
        vertices: set[Pair] = {start}
        edge_indices: set[int] = set()
        seen_vertices.add(start)
        stack = [start]
        while stack:
            current = stack.pop()
            for target, edge_index in adjacency[current]:
                edge_indices.add(edge_index)
                seen_edges.add(edge_index)
                if target not in seen_vertices:
                    seen_vertices.add(target)
                    vertices.add(target)
                    stack.append(target)
        rank = len(edge_indices) - len(vertices) + 1
        if rank < 0:
            raise AssertionError("negative reserve component cycle rank")
        gaps = {pair[1] - pair[0] for pair in vertices}
        if len(gaps) != 1:
            raise AssertionError("reserve component mixed physical gaps")
        result.append(
            {
                "vertices": tuple(sorted(vertices)),
                "edge_indices": tuple(sorted(edge_indices)),
                "edges": len(edge_indices),
                "vertex_count": len(vertices),
                "cycle_rank": rank,
                "gap": gaps.pop(),
            }
        )
    if len(seen_edges) != len(edges):
        raise AssertionError("reserve graph lost an edge")
    return result


def parent_profile(parent: tuple[int, ...]) -> dict[str, object]:
    retained = retained_family(parent)
    latent_owners: dict[Resource, list[dict[str, object]]] = defaultdict(list)
    state_rows: list[dict[str, object]] = []

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {
            root - value for value, root in zip(values, roots, strict=True)
        }
        if len(references) != 1:
            raise AssertionError("reserve-search retained child is not affine")
        reference = references.pop()
        terminal = not contains_three_term_ap(values)
        source = str(state.representative.source)
        source_step = state.representative.source_step
        state_rows.append(
            {
                "state_index": int(state.index),
                "source": source,
                "source_step": source_step,
                "exponent": int(state.representative.exponent),
                "reference": reference,
                "terminal": terminal,
                "values": values,
                "roots": roots,
            }
        )
        if terminal:
            continue
        for first, second in combinations(range(len(roots)), 2):
            resource = ordered_pair(roots[first], roots[second])
            latent_owners[resource].append(
                {
                    "state_index": int(state.index),
                    "source": source,
                    "source_step": source_step,
                    "reference": reference,
                }
            )

    duplicate_rows: list[dict[str, object]] = []
    reserve_edges: list[tuple[Pair, Pair, Resource, int, int]] = []
    latent_residual = Fraction()
    for resource, rows in sorted(latent_owners.items()):
        if len(rows) <= 1:
            continue
        if len(rows) > 2:
            raise AssertionError(
                f"latent degree-two theorem failed for {parent}: {resource}, {rows}"
            )
        sources = sorted(str(row["source"]) for row in rows)
        if sources != ["backbone", "middle_fiber"]:
            raise AssertionError(
                f"unexpected duplicate owner profile for {parent}: {rows}"
            )
        middle = next(row for row in rows if row["source"] == "middle_fiber")
        step = int(middle["source_step"])
        sign = orientation(step)
        center = ordered_pair(resource[0] + sign * step, resource[1] + sign * step)
        opposite = ordered_pair(
            resource[0] + 2 * sign * step,
            resource[1] + 2 * sign * step,
        )
        if not set(center) <= set(parent) or not set(opposite) <= set(parent):
            raise AssertionError("translated reserve left parent support")
        gap = resource[1] - resource[0]
        if center[1] - center[0] != gap or opposite[1] - opposite[0] != gap:
            raise AssertionError("translated reserve changed physical gap")
        reserve_edges.append((center, opposite, resource, step, sign))
        latent_residual += Fraction(1, gap)
        duplicate_rows.append(
            {
                "demand": resource,
                "gap": gap,
                "owners": rows,
                "step": step,
                "orientation": sign,
                "center_reserve": center,
                "opposite_reserve": opposite,
            }
        )

    component_rows = graph_components(reserve_edges) if reserve_edges else []
    maximum_rank = max(
        (int(component["cycle_rank"]) for component in component_rows),
        default=0,
    )
    defect_mass = sum(
        (
            Fraction(
                max(0, int(component["edges"]) - int(component["vertex_count"])),
                int(component["gap"]),
            )
            for component in component_rows
        ),
        Fraction(),
    )
    return {
        "retained_states": len(retained),
        "recursive_states": sum(not bool(row["terminal"]) for row in state_rows),
        "duplicated_latent_resources": len(duplicate_rows),
        "latent_residual_fraction": str(latent_residual),
        "reserve_vertices": len(
            {vertex for edge in reserve_edges for vertex in edge[:2]}
        ),
        "reserve_edges": len(reserve_edges),
        "reserve_components": len(component_rows),
        "maximum_component_cycle_rank": maximum_rank,
        "reserve_defect_fraction": str(defect_mass),
        "states": state_rows,
        "duplicates": duplicate_rows,
        "components": component_rows,
    }


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: search_lexicographic_reserve_pseudoforest_small_box.py "
            "ENDPOINT OUTPUT_JSON"
        )
    endpoint = int(sys.argv[1])
    if endpoint < 4 or endpoint > 20:
        raise SystemExit("endpoint must lie in [4,20]")

    values = tuple(range(1, endpoint + 1))
    four_ap_free_parents = 0
    parents_with_latent_reuse = 0
    total_duplicate_demands = 0
    maximum_duplicate_demands = 0
    maximum_cycle_rank = 0
    cyclic_components = 0
    rank_two_components = 0
    maximum_rank_witness: dict[str, object] | None = None
    first_rank_two_witness: dict[str, object] | None = None
    latent_profile_histogram: Counter[tuple[int, int, int]] = Counter()

    for mask in range(1 << endpoint):
        parent = tuple(
            value for index, value in enumerate(values) if mask & (1 << index)
        )
        if len(parent) < 3 or contains_four_ap(parent):
            continue
        four_ap_free_parents += 1
        profile = parent_profile(parent)
        demands = int(profile["duplicated_latent_resources"])
        rank = int(profile["maximum_component_cycle_rank"])
        latent_profile_histogram[(
            demands,
            int(profile["reserve_components"]),
            rank,
        )] += 1
        if demands:
            parents_with_latent_reuse += 1
            total_duplicate_demands += demands
            maximum_duplicate_demands = max(maximum_duplicate_demands, demands)
        for component in profile["components"]:
            component_rank = int(component["cycle_rank"])
            if component_rank > 0:
                cyclic_components += 1
            if component_rank >= 2:
                rank_two_components += 1
                if first_rank_two_witness is None:
                    first_rank_two_witness = {
                        "parent": parent,
                        "profile": profile,
                    }
        if rank > maximum_cycle_rank:
            maximum_cycle_rank = rank
            maximum_rank_witness = {"parent": parent, "profile": profile}

    output = {
        "schema": "lexicographic_reserve_pseudoforest_small_box_v1",
        "endpoint": endpoint,
        "counts": {
            "four_ap_free_parents": four_ap_free_parents,
            "parents_with_latent_reuse": parents_with_latent_reuse,
            "total_duplicate_demands": total_duplicate_demands,
            "maximum_duplicate_demands": maximum_duplicate_demands,
            "cyclic_reserve_components": cyclic_components,
            "rank_two_reserve_components": rank_two_components,
            "maximum_reserve_cycle_rank": maximum_cycle_rank,
        },
        "profile_histogram": [
            {
                "duplicate_demands": profile[0],
                "reserve_components": profile[1],
                "maximum_cycle_rank": profile[2],
                "parents": count,
            }
            for profile, count in sorted(latent_profile_histogram.items())
        ],
        "maximum_rank_witness": maximum_rank_witness,
        "first_rank_two_witness": first_rank_two_witness,
        "checks": {
            "latent_degree_at_most_two": True,
            "every_duplicate_is_backbone_middle": True,
            "translated_reserves_preserve_gap": True,
            "all_reserve_components_pseudoforests": rank_two_components == 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[2]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if rank_two_components == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
