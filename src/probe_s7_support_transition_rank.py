#!/usr/bin/env python3
"""Diagnose rank and potential structure in the fixed S7 support cascade.

The certified closure proves finite termination on one retained frontier.  This
probe reconstructs the same closure while recording every directed transition

    activated support pair -> transported terminal target
    -> certified completion hole -> canonical witness support pair.

It then tests coordinate, gap, dyadic, deletion-rank, graph-acyclicity, and
small affine-potential hypotheses.  The output is exploratory evidence for a
state-independent transfer law; no candidate rank is asserted unless it is
verified on every recorded transition.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_hole_support_closure import (
    build_s7,
    canonical_pair,
    completion_roots,
    read_full_hole_map,
)
from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    pair_weight,
    parent_schedule,
    reconstruct_fourth_recursive,
    transport,
)
from probe_terminal_pair_payment_frontier_v2 import terminal_semantics

Pair = tuple[int, int]


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def pair_features(pair: Pair) -> dict[str, int]:
    left, right = pair
    gap = right - left
    valuation = v2(gap)
    return {
        "left": left,
        "right": right,
        "gap": gap,
        "sum": left + right,
        "v2_gap": valuation,
        "odd_gap": gap >> valuation,
    }


def pair_owner(
    pair: Pair,
    schedules: dict[int, dict[str, object]],
) -> dict[str, object]:
    owners = [
        parent_class
        for parent_class, schedule in schedules.items()
        if set(pair) <= schedule["roots"]  # type: ignore[operator]
    ]
    if len(owners) > 1:
        raise AssertionError("pair belongs to several certified parents")
    if not owners:
        return {
            "owner_class": None,
            "owner_kind": "cross_parent",
            "minimum_sponsor_rank": None,
            "maximum_sponsor_rank": None,
        }

    parent_class = owners[0]
    schedule = schedules[parent_class]
    sponsors: set[int] = schedule["sponsors"]  # type: ignore[assignment]
    tau: dict[int, int] = schedule["tau"]  # type: ignore[assignment]
    sponsor_ranks = [tau[value] for value in pair if value in sponsors]
    if sponsor_ranks:
        kind = "activated"
        minimum_rank = min(sponsor_ranks)
        maximum_rank = max(sponsor_ranks)
    else:
        residual: set[int] = schedule["residual"]  # type: ignore[assignment]
        if not set(pair) <= residual:
            raise AssertionError("owned pair is neither activated nor residual")
        kind = "residual"
        minimum_rank = None
        maximum_rank = None
    return {
        "owner_class": parent_class,
        "owner_kind": kind,
        "minimum_sponsor_rank": minimum_rank,
        "maximum_sponsor_rank": maximum_rank,
    }


def compare_values(source: int, target: int) -> str:
    if target < source:
        return "decrease"
    if target > source:
        return "increase"
    return "equal"


def tarjan_scc(edges: set[tuple[Pair, Pair]]) -> list[list[Pair]]:
    adjacency: dict[Pair, set[Pair]] = defaultdict(set)
    nodes: set[Pair] = set()
    for source, target in edges:
        nodes.add(source)
        nodes.add(target)
        if source != target:
            adjacency[source].add(target)

    index = 0
    indices: dict[Pair, int] = {}
    lowlink: dict[Pair, int] = {}
    stack: list[Pair] = []
    on_stack: set[Pair] = set()
    components: list[list[Pair]] = []

    def visit(node: Pair) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for target in sorted(adjacency[node]):
            if target not in indices:
                visit(target)
                lowlink[node] = min(lowlink[node], lowlink[target])
            elif target in on_stack:
                lowlink[node] = min(lowlink[node], indices[target])

        if lowlink[node] == indices[node]:
            component: list[Pair] = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == node:
                    break
            components.append(sorted(component))

    for node in sorted(nodes):
        if node not in indices:
            visit(node)
    return components


def dag_longest_path(edges: set[tuple[Pair, Pair]]) -> tuple[bool, int]:
    adjacency: dict[Pair, set[Pair]] = defaultdict(set)
    indegree: Counter[Pair] = Counter()
    nodes: set[Pair] = set()
    for source, target in edges:
        nodes.add(source)
        nodes.add(target)
        if source == target or target in adjacency[source]:
            continue
        adjacency[source].add(target)
        indegree[target] += 1
        indegree.setdefault(source, indegree[source])

    queue = deque(sorted(node for node in nodes if indegree[node] == 0))
    distance: dict[Pair, int] = {node: 0 for node in nodes}
    processed = 0
    while queue:
        node = queue.popleft()
        processed += 1
        for target in sorted(adjacency[node]):
            distance[target] = max(distance[target], distance[node] + 1)
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return processed == len(nodes), max(distance.values(), default=0)


def lex_candidates(
    edge_rows: list[dict[str, object]],
    maximum_length: int = 4,
) -> list[dict[str, object]]:
    feature_names = ("left", "right", "gap", "sum", "v2_gap", "odd_gap")
    unique_edges = {
        (
            tuple(row["source_support"]),  # type: ignore[arg-type]
            tuple(row["next_support"]),  # type: ignore[arg-type]
        )
        for row in edge_rows
        if row["source_support"] != row["next_support"]
    }
    feature_cache = {
        pair: pair_features(pair)
        for edge in unique_edges
        for pair in edge
    }
    matches: list[dict[str, object]] = []
    for length in range(1, maximum_length + 1):
        for names in permutations(feature_names, length):
            for signs in product((-1, 1), repeat=length):
                valid = True
                for source, target in unique_edges:
                    source_key = tuple(
                        signs[index] * feature_cache[source][name]
                        for index, name in enumerate(names)
                    )
                    target_key = tuple(
                        signs[index] * feature_cache[target][name]
                        for index, name in enumerate(names)
                    )
                    if not target_key < source_key:
                        valid = False
                        break
                if valid:
                    matches.append(
                        {
                            "features": names,
                            "signs": signs,
                            "direction": "strict_decrease",
                        }
                    )
        if matches:
            break
    return matches[:20]


def affine_candidates(
    edge_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    unique_edges = {
        (
            tuple(row["source_support"]),  # type: ignore[arg-type]
            tuple(row["next_support"]),  # type: ignore[arg-type]
        )
        for row in edge_rows
        if row["source_support"] != row["next_support"]
    }
    feature_sets = (
        ("left", "right", "gap"),
        ("sum", "gap", "v2_gap"),
        ("left", "gap", "odd_gap"),
        ("right", "gap", "odd_gap"),
    )
    cache = {
        pair: pair_features(pair)
        for edge in unique_edges
        for pair in edge
    }
    matches: list[dict[str, object]] = []
    for names in feature_sets:
        for coefficients in product(range(-4, 5), repeat=len(names)):
            if not any(coefficients):
                continue
            valid = True
            minimum_drop: int | None = None
            for source, target in unique_edges:
                source_value = sum(
                    coefficient * cache[source][name]
                    for coefficient, name in zip(coefficients, names)
                )
                target_value = sum(
                    coefficient * cache[target][name]
                    for coefficient, name in zip(coefficients, names)
                )
                drop = source_value - target_value
                if drop <= 0:
                    valid = False
                    break
                minimum_drop = drop if minimum_drop is None else min(minimum_drop, drop)
            if valid:
                matches.append(
                    {
                        "features": names,
                        "coefficients": coefficients,
                        "minimum_drop": minimum_drop,
                    }
                )
    matches.sort(
        key=lambda row: (
            sum(abs(value) for value in row["coefficients"]),  # type: ignore[arg-type]
            -int(row["minimum_drop"]),
            row["features"],
            row["coefficients"],
        )
    )
    return matches[:20]


def serial_pair(pair: Pair) -> list[int]:
    return [pair[0], pair[1]]


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_support_transition_rank.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    payment_path = Path(sys.argv[1])
    hole_map_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    target_rows = payment.get("target_rows")
    if not isinstance(source_rows, list) or not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    holes = read_full_hole_map(hole_map_path)
    s7 = build_s7()
    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}

    seen_resources: set[Pair] = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    seen_targets: set[Pair] = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }

    frontier: dict[Pair, dict[str, object]] = {}
    for row in target_rows:
        target = tuple(int(value) for value in row["target"])
        frontier[target] = {
            "natural_completions": {
                int(record[2]) for record in row["completion_records"]
            },
            "origins": set(),
        }

    edge_rows: list[dict[str, object]] = []
    transport_rows: list[dict[str, object]] = []
    introduced_layer: dict[Pair, int] = {pair: -1 for pair in seen_resources}
    layer_profile: list[dict[str, object]] = []

    for layer_index in range(20):
        if not frontier:
            break

        support_by_hole: dict[int, Pair] = {}
        edge_supported = 0
        admissible = 0
        outside_shell = 0

        for target, record in sorted(frontier.items()):
            completions: set[int] = record["natural_completions"]  # type: ignore[assignment]
            if completion_roots(target, s7):
                edge_supported += 1
                continue
            certified = sorted(value for value in completions if value in holes)
            if certified:
                completion = certified[0]
                support = canonical_pair(*holes[completion])
                support_by_hole[completion] = support
                for origin in sorted(record["origins"]):  # type: ignore[arg-type]
                    source_features = pair_features(origin)
                    next_features = pair_features(support)
                    source_owner = pair_owner(origin, schedules)
                    next_owner = pair_owner(support, schedules)
                    edge_rows.append(
                        {
                            "layer": layer_index,
                            "source_support": serial_pair(origin),
                            "frontier_target": serial_pair(target),
                            "completion": completion,
                            "next_support": serial_pair(support),
                            "source_gap": source_features["gap"],
                            "target_gap": target[1] - target[0],
                            "next_gap": next_features["gap"],
                            "source_weight": fraction_text(pair_weight(origin)),
                            "target_weight": fraction_text(pair_weight(target)),
                            "next_weight": fraction_text(pair_weight(support)),
                            "source_owner": source_owner,
                            "next_owner": next_owner,
                        }
                    )
                continue
            if completions and all(1_048_576 <= value <= 2_097_151 for value in completions):
                admissible += 1
            else:
                outside_shell += 1

        support_pairs = set(support_by_hole.values())
        existing_supports = support_pairs & seen_resources
        new_supports = support_pairs - seen_resources
        for support in new_supports:
            introduced_layer[support] = layer_index
        seen_resources.update(new_supports)

        activated: dict[Pair, int] = {}
        residual: set[Pair] = set()
        cross_parent: set[Pair] = set()
        for support in sorted(new_supports):
            owner = pair_owner(support, schedules)
            kind = owner["owner_kind"]
            if kind == "activated":
                activated[support] = int(owner["owner_class"])
            elif kind == "residual":
                residual.add(support)
            elif kind == "cross_parent":
                cross_parent.add(support)
            else:
                raise AssertionError("unknown support ownership class")

        produced: dict[Pair, dict[str, object]] = {}
        for support, parent_class in sorted(activated.items()):
            schedule = schedules[parent_class]
            result = transport(support, schedule)
            target: Pair = result["target"]  # type: ignore[assignment]
            semantics = terminal_semantics(target, result, schedule, s7)
            natural_completion = int(semantics["natural_completion"])
            transport_rows.append(
                {
                    "layer": layer_index,
                    "source_support": serial_pair(support),
                    "source_parent": parent_class,
                    "source_gap": support[1] - support[0],
                    "target": serial_pair(target),
                    "target_gap": target[1] - target[0],
                    "terminal_class": str(result["terminal_class"]),
                    "path_length": len(result["path"]),
                    "natural_completion": natural_completion,
                }
            )
            if target not in produced:
                produced[target] = {
                    "natural_completions": set(),
                    "origins": set(),
                }
            produced[target]["natural_completions"].add(natural_completion)  # type: ignore[union-attr]
            produced[target]["origins"].add(support)  # type: ignore[union-attr]

        produced_targets = set(produced)
        new_targets = produced_targets - seen_targets
        next_frontier = {target: produced[target] for target in sorted(new_targets)}
        seen_targets.update(produced_targets)

        layer_profile.append(
            {
                "layer": layer_index,
                "input_targets": len(frontier),
                "edge_supported_targets": edge_supported,
                "certified_holes": len(support_by_hole),
                "admissible_targets": admissible,
                "outside_shell_targets": outside_shell,
                "support_pairs": len(support_pairs),
                "existing_supports": len(existing_supports),
                "new_supports": len(new_supports),
                "activated_new_supports": len(activated),
                "residual_new_supports": len(residual),
                "cross_parent_new_supports": len(cross_parent),
                "produced_targets": len(produced_targets),
                "new_targets": len(new_targets),
            }
        )
        frontier = next_frontier

    if frontier:
        raise AssertionError("rank probe did not reach the certified closure")

    unique_edges: set[tuple[Pair, Pair]] = {
        (
            tuple(row["source_support"]),  # type: ignore[arg-type]
            tuple(row["next_support"]),  # type: ignore[arg-type]
        )
        for row in edge_rows
    }
    self_loops = {edge for edge in unique_edges if edge[0] == edge[1]}
    components = tarjan_scc(unique_edges)
    nontrivial_components = [component for component in components if len(component) > 1]
    acyclic_after_self_loops, longest_path = dag_longest_path(unique_edges)

    feature_profile: dict[str, Counter[str]] = {
        name: Counter()
        for name in ("left", "right", "gap", "sum", "v2_gap", "odd_gap")
    }
    counterexamples: dict[str, dict[str, list[dict[str, object]]]] = {
        name: {"not_decreasing": [], "not_increasing": []}
        for name in feature_profile
    }
    weight_ratio_min: Fraction | None = None
    weight_ratio_max: Fraction | None = None

    for source, target in sorted(unique_edges):
        if source == target:
            continue
        source_features = pair_features(source)
        target_features = pair_features(target)
        ratio = pair_weight(target) / pair_weight(source)
        weight_ratio_min = ratio if weight_ratio_min is None else min(weight_ratio_min, ratio)
        weight_ratio_max = ratio if weight_ratio_max is None else max(weight_ratio_max, ratio)
        for name in feature_profile:
            relation = compare_values(source_features[name], target_features[name])
            feature_profile[name][relation] += 1
            example = {
                "source": serial_pair(source),
                "target": serial_pair(target),
                "source_value": source_features[name],
                "target_value": target_features[name],
            }
            if relation != "decrease" and len(counterexamples[name]["not_decreasing"]) < 5:
                counterexamples[name]["not_decreasing"].append(example)
            if relation != "increase" and len(counterexamples[name]["not_increasing"]) < 5:
                counterexamples[name]["not_increasing"].append(example)

    owner_transition_profile = Counter()
    parent_relation_profile = Counter()
    sponsor_rank_profile = Counter()
    for row in edge_rows:
        source_owner = row["source_owner"]
        next_owner = row["next_owner"]
        owner_transition_profile[
            f"{source_owner['owner_kind']}->{next_owner['owner_kind']}"  # type: ignore[index]
        ] += 1
        source_parent = source_owner["owner_class"]  # type: ignore[index]
        next_parent = next_owner["owner_class"]  # type: ignore[index]
        if source_parent is not None and next_parent is not None:
            parent_relation_profile[
                compare_values(int(source_parent), int(next_parent))
            ] += 1
        source_rank = source_owner["minimum_sponsor_rank"]  # type: ignore[index]
        next_rank = next_owner["minimum_sponsor_rank"]  # type: ignore[index]
        if source_rank is not None and next_rank is not None:
            sponsor_rank_profile[
                compare_values(int(source_rank), int(next_rank))
            ] += 1

    lex = lex_candidates(edge_rows)
    affine = affine_candidates(edge_rows)
    payload = {
        "schema": "s7_support_transition_rank_probe_v1",
        "scope": "fixed certified S7 support-identity closure after merged PR18",
        "generation_six_propagated": False,
        "closure": {
            "layers_processed": len(layer_profile),
            "terminated": not frontier,
            "transition_rows": len(edge_rows),
            "unique_directed_edges": len(unique_edges),
            "support_nodes": len({node for edge in unique_edges for node in edge}),
            "self_loops": len(self_loops),
            "nontrivial_strong_components": len(nontrivial_components),
            "maximum_strong_component_size": max(
                (len(component) for component in components), default=0
            ),
            "acyclic_after_removing_self_loops": acyclic_after_self_loops,
            "longest_nonself_path": longest_path,
        },
        "layer_profile": layer_profile,
        "coordinate_relation_profile": {
            name: dict(sorted(profile.items()))
            for name, profile in feature_profile.items()
        },
        "owner_transition_profile": dict(sorted(owner_transition_profile.items())),
        "parent_class_relation_profile": dict(sorted(parent_relation_profile.items())),
        "minimum_sponsor_rank_relation_profile": dict(sorted(sponsor_rank_profile.items())),
        "weight_ratio": {
            "minimum_next_over_source": (
                fraction_text(weight_ratio_min)
                if weight_ratio_min is not None
                else None
            ),
            "maximum_next_over_source": (
                fraction_text(weight_ratio_max)
                if weight_ratio_max is not None
                else None
            ),
        },
        "strict_lexicographic_candidates": lex,
        "small_affine_candidates": affine,
        "counterexamples": counterexamples,
        "hashes": {
            "edge_rows": canonical_hash(edge_rows),
            "transport_rows": canonical_hash(transport_rows),
            "introduced_layer": canonical_hash(
                sorted((serial_pair(pair), layer) for pair, layer in introduced_layer.items())
            ),
        },
        "checks": {
            "five_layer_closure_reproduced": len(layer_profile) == 5,
            "closure_terminated": not frontier,
            "no_nontrivial_directed_cycle": not nontrivial_components,
            "dag_check": acyclic_after_self_loops,
        },
        "edge_rows": edge_rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
