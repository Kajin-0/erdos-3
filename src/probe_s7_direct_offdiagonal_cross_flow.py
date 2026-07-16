#!/usr/bin/env python3
"""Pack direct S7 recursive debt into unmatched cross-copy physical pairs."""
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
    for pair in pairs:
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

    saturated_pairs: set[Pair] = set()
    maximum_utilization = Fraction()
    for pair, allocated in allocated_by_pair.items():
        available = available_capacity[pair]
        if allocated > available:
            raise AssertionError("off-diagonal flow exceeds physical pair capacity")
        if available > 0:
            maximum_utilization = max(maximum_utilization, allocated / available)
        if available > 0 and allocated == available:
            saturated_pairs.add(pair)

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

    output = {
        "schema": "s7_direct_offdiagonal_cross_flow_v1",
        "scope": "exact rational packing into unmatched cross-copy pairs",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": len(recursive_states),
            "offdiagonal_pair_occurrences": sum(len(row) for row in state_pairs),
            "distinct_offdiagonal_pairs": len(pairs),
            "entering_activated_overlaps": len(entering_overlaps),
            "light_support_overlaps": len(light_overlaps),
            "allocated_pairs": len(allocated_by_pair),
            "saturated_pairs": len(saturated_pairs),
            "min_cut_states": len(cut_states),
            "min_cut_pairs": len(cut_pairs),
        },
        "masses": {
            "total_recursive_demand": serialize_mass(total_demand),
            "available_new_offdiagonal_capacity": serialize_mass(
                sum(available_capacity.values(), Fraction())
            ),
            "maximum_flow": serialize_mass(maximum_flow),
            "unmet_demand": serialize_mass(unmet),
            "allocated_capacity": serialize_mass(
                sum(allocated_by_pair.values(), Fraction())
            ),
            "unused_capacity_on_allocated_pairs": serialize_mass(
                sum(
                    (
                        available_capacity[pair] - allocated_by_pair[pair]
                        for pair in allocated_by_pair
                    ),
                    Fraction(),
                )
            ),
            "minimum_state_offdiagonal_surplus": serialize_mass(
                min(state_surpluses)
            ),
            "min_cut_state_demand": serialize_mass(cut_demand),
            "min_cut_pair_capacity": serialize_mass(cut_capacity),
        },
        "maximum_pair_utilization": {
            "fraction": str(maximum_utilization),
            "decimal": f"{float(maximum_utilization):.12f}",
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
            "exact_new_offdiagonal_flow_feasible": unmet == 0,
            "all_allocations_within_capacity": all(
                allocated_by_pair[pair] <= available_capacity[pair]
                for pair in allocated_by_pair
            ),
            "entering_pairs_reserved": all(
                available_capacity[pair] == 0 for pair in entering_overlaps
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[3]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if unmet == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
