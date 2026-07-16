#!/usr/bin/env python3
"""Certify that S7 off-diagonal cross pairs are latent, not new capacity."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_fractional_chain_flow import Dinic
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from s7_direct_chain_instance import Pair, RecursiveChainState, build_instance


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate off-diagonal pair")
    return (left, right) if left < right else (right, left)


def offdiagonal_pairs(state: RecursiveChainState) -> tuple[Pair, ...]:
    steps = state.state
    completion = state.completion
    role = state.role

    if role == "right_adjacent":
        first = tuple(completion + step for step in steps)
        second = tuple(completion + 2 * step for step in steps)
    elif role == "left_adjacent":
        first = tuple(completion - step for step in steps)
        second = tuple(completion - 2 * step for step in steps)
    elif role == "outer":
        first = tuple(completion - step for step in steps)
        second = tuple(completion + step for step in steps)
    else:
        raise AssertionError(f"unknown completion role: {role}")

    pairs = tuple(
        ordered_pair(first[index], second[other])
        for index in range(len(steps))
        for other in range(len(steps))
        if index != other
    )
    if len(pairs) != len(set(pairs)):
        raise AssertionError("one state has duplicate off-diagonal physical pairs")
    return pairs


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_offdiagonal_cross_flow.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    instance = build_instance(Path(sys.argv[1]), Path(sys.argv[2]))
    s7: set[int] = instance["s7"]  # type: ignore[assignment]
    activated: set[Pair] = instance["activated"]  # type: ignore[assignment]
    light_usage: dict[Pair, Fraction] = instance["light_usage"]  # type: ignore[assignment]
    recursive_states: tuple[RecursiveChainState, ...] = instance["recursive_states"]  # type: ignore[assignment]

    state_pairs: list[tuple[Pair, ...]] = []
    pair_universe: set[Pair] = set()
    state_surpluses: list[Fraction] = []

    for state in recursive_states:
        pairs = offdiagonal_pairs(state)
        capacity = Fraction()
        for pair in pairs:
            if not set(pair) <= s7:
                raise AssertionError("off-diagonal pair left S7")
            capacity += pair_weight(pair)
            pair_universe.add(pair)
        if capacity <= state.debt:
            raise AssertionError("off-diagonal pair energy does not dominate state debt")
        state_surpluses.append(capacity - state.debt)
        state_pairs.append(pairs)

    pairs = sorted(pair_universe)
    pair_index = {pair: index for index, pair in enumerate(pairs)}

    source = 0
    first_state = 1
    first_pair = first_state + len(recursive_states)
    sink = first_pair + len(pairs)
    network = Dinic(sink + 1)

    total_demand = Fraction()
    handles: list[list[tuple[Pair, tuple[int, int]]]] = []
    for state_index, (state, resources) in enumerate(
        zip(recursive_states, state_pairs, strict=True)
    ):
        state_node = first_state + state_index
        total_demand += state.debt
        network.add_edge(source, state_node, state.debt)
        row: list[tuple[Pair, tuple[int, int]]] = []
        for pair in resources:
            pair_node = first_pair + pair_index[pair]
            row.append(
                (pair, network.add_edge(state_node, pair_node, state.debt))
            )
        handles.append(row)

    available_capacity: dict[Pair, Fraction] = {}
    entering_overlaps: set[Pair] = set()
    light_overlaps: set[Pair] = set()
    latent_union_capacity = Fraction()
    for pair in pairs:
        latent_union_capacity += pair_weight(pair)
        if pair in activated:
            entering_overlaps.add(pair)
            available = Fraction()
        else:
            available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if pair in light_usage:
            light_overlaps.add(pair)
        if available < 0:
            raise AssertionError("negative off-diagonal residual capacity")
        available_capacity[pair] = available
        pair_node = first_pair + pair_index[pair]
        network.add_edge(pair_node, sink, available)

    maximum_flow = network.max_flow(source, sink)
    unmet = total_demand - maximum_flow
    reachable = network.reachable(source)

    allocated_by_pair: dict[Pair, Fraction] = defaultdict(Fraction)
    allocation_rows: list[tuple[int, Pair, str]] = []
    for state_index, row in enumerate(handles):
        for pair, (node, edge_index) in row:
            edge = network.graph[node][edge_index]
            allocated = edge.original - edge.capacity
            if allocated > 0:
                allocated_by_pair[pair] += allocated
                allocation_rows.append((state_index, pair, str(allocated)))

    cut_states = [
        index
        for index in range(len(recursive_states))
        if first_state + index in reachable
    ]
    cut_pairs = [
        pair
        for pair in pairs
        if first_pair + pair_index[pair] in reachable
    ]
    cut_demand = sum(
        (recursive_states[index].debt for index in cut_states), Fraction()
    )
    cut_capacity = sum(
        (available_capacity[pair] for pair in cut_pairs), Fraction()
    )

    occurrence_count = sum(len(row) for row in state_pairs)
    expected_counts = {
        "recursive_states": 278,
        "offdiagonal_pair_occurrences": 19_226,
        "distinct_offdiagonal_pairs": 13_547,
        "entering_activated_overlaps": 13_547,
        "light_support_overlaps": 0,
        "allocated_pairs": 0,
        "min_cut_states": 278,
        "min_cut_pairs": 13_547,
    }
    actual_counts = {
        "recursive_states": len(recursive_states),
        "offdiagonal_pair_occurrences": occurrence_count,
        "distinct_offdiagonal_pairs": len(pairs),
        "entering_activated_overlaps": len(entering_overlaps),
        "light_support_overlaps": len(light_overlaps),
        "allocated_pairs": len(allocated_by_pair),
        "min_cut_states": len(cut_states),
        "min_cut_pairs": len(cut_pairs),
    }
    if actual_counts != expected_counts:
        raise AssertionError(f"off-diagonal no-go profile changed: {actual_counts}")
    if entering_overlaps != pair_universe:
        raise AssertionError("some off-diagonal pair is not already activated")
    if any(available_capacity.values()):
        raise AssertionError("strict-new off-diagonal capacity unexpectedly appeared")
    if maximum_flow != 0 or unmet != total_demand:
        raise AssertionError("strict-new off-diagonal no-go changed")
    if cut_demand != total_demand or cut_capacity != 0:
        raise AssertionError("off-diagonal min-cut certificate changed")

    output = {
        "schema": "s7_direct_offdiagonal_latent_capacity_no_go_v1",
        "scope": "strict-new unmatched cross-copy capacity on the direct S7 recursive frontier",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": expected_counts,
        "masses": {
            "total_recursive_demand": serialize_mass(total_demand),
            "latent_offdiagonal_pair_union_capacity": serialize_mass(
                latent_union_capacity
            ),
            "available_new_offdiagonal_capacity": serialize_mass(Fraction()),
            "maximum_strict_new_flow": serialize_mass(maximum_flow),
            "unmet_demand": serialize_mass(unmet),
            "minimum_state_offdiagonal_surplus": serialize_mass(
                min(state_surpluses)
            ),
            "min_cut_state_demand": serialize_mass(cut_demand),
            "min_cut_new_pair_capacity": serialize_mass(cut_capacity),
        },
        "hashes": {
            "pair_universe": hashlib.sha256(
                json.dumps(pairs, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "positive_allocations": hashlib.sha256(
                json.dumps(allocation_rows, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "statewise_offdiagonal_domination": min(state_surpluses) > 0,
            "all_offdiagonal_pairs_are_entering_activated_pairs": (
                entering_overlaps == pair_universe
            ),
            "strict_new_offdiagonal_capacity_is_zero": not any(
                available_capacity.values()
            ),
            "exact_no_go_min_cut": (
                maximum_flow == 0
                and unmet == total_demand
                and cut_demand == total_demand
                and cut_capacity == 0
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[3]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    print("verified: off-diagonal surplus is entirely latent entering pair energy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
