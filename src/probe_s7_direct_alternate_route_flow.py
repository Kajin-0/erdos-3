#!/usr/bin/env python3
"""Pack direct S7 recursive debt using only the alternate canonical pair route."""
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
        raise AssertionError("degenerate alternate-route pair")
    return (left, right) if left < right else (right, left)


def adjacent_staircase(state: RecursiveChainState) -> tuple[Pair, ...]:
    steps = state.state
    completion = state.completion
    if state.role == "right_adjacent":
        first = tuple(completion + step for step in steps)
        second = tuple(completion + 2 * step for step in steps)
    elif state.role == "left_adjacent":
        first = tuple(completion - step for step in steps)
        second = tuple(completion - 2 * step for step in steps)
    else:
        raise AssertionError("staircase requested for non-adjacent role")

    pairs = [
        ordered_pair(first[index + 1], second[index])
        for index in range(len(steps) - 1)
    ]
    pairs.append(ordered_pair(first[0], second[1]))
    if len(pairs) != len(set(pairs)):
        raise AssertionError("alternate staircase contains duplicate pairs")

    # Pointwise domination and gap decrease.
    for index in range(len(steps) - 1):
        gap = pairs[index][1] - pairs[index][0]
        if not (0 < gap < steps[index]):
            raise AssertionError("staircase pair failed assigned gap decrease")
    final_gap = pairs[-1][1] - pairs[-1][0]
    if not (0 < final_gap < steps[-1]):
        raise AssertionError("final staircase pair failed assigned gap decrease")
    return tuple(pairs)


def outer_opposite_chain(state: RecursiveChainState) -> tuple[Pair, ...]:
    if state.role != "outer":
        raise AssertionError("opposite chain requested for non-outer role")
    points = tuple(state.completion + step for step in state.state)
    pairs = tuple(
        ordered_pair(points[index], points[index + 1])
        for index in range(len(points) - 1)
    )
    for pair in pairs:
        if pair[1] - pair[0] >= state.shell_base:
            raise AssertionError("outer opposite chain failed shell descent")
    return pairs


def alternate_resources(state: RecursiveChainState) -> tuple[Pair, ...]:
    if state.role in {"right_adjacent", "left_adjacent"}:
        return adjacent_staircase(state)
    if state.role == "outer":
        return outer_opposite_chain(state)
    raise AssertionError(f"unknown completion role: {state.role}")


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_alternate_route_flow.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    instance = build_instance(Path(sys.argv[1]), Path(sys.argv[2]))
    activated: set[Pair] = instance["activated"]  # type: ignore[assignment]
    light_usage: dict[Pair, Fraction] = instance["light_usage"]  # type: ignore[assignment]
    recursive_states: tuple[RecursiveChainState, ...] = instance["recursive_states"]  # type: ignore[assignment]

    state_resources: list[tuple[Pair, ...]] = []
    pair_universe: set[Pair] = set()
    state_surpluses: list[Fraction] = []
    role_counts: dict[str, int] = defaultdict(int)

    for state in recursive_states:
        resources = alternate_resources(state)
        capacity = sum((pair_weight(pair) for pair in resources), Fraction())
        if capacity <= state.debt:
            raise AssertionError("alternate route does not dominate state debt")
        state_surpluses.append(capacity - state.debt)
        state_resources.append(resources)
        pair_universe.update(resources)
        role_counts[state.role] += 1

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
        zip(recursive_states, state_resources, strict=True)
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
    activated_pairs = set()
    light_pairs = set()
    for pair in pairs:
        available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if available < 0:
            raise AssertionError("negative alternate-route residual capacity")
        available_capacity[pair] = available
        if pair in activated:
            activated_pairs.add(pair)
        if pair in light_usage:
            light_pairs.add(pair)
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

    saturated_pairs = {
        pair
        for pair, allocated in allocated_by_pair.items()
        if available_capacity[pair] > 0 and allocated == available_capacity[pair]
    }
    maximum_utilization = max(
        (
            allocated / available_capacity[pair]
            for pair, allocated in allocated_by_pair.items()
            if available_capacity[pair] > 0
        ),
        default=Fraction(),
    )

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
        "schema": "s7_direct_alternate_route_flow_v1",
        "scope": "exact rational packing by adjacent staircases and outer opposite-copy chains",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": len(recursive_states),
            "right_adjacent_states": role_counts.get("right_adjacent", 0),
            "left_adjacent_states": role_counts.get("left_adjacent", 0),
            "outer_states": role_counts.get("outer", 0),
            "alternate_pair_occurrences": sum(len(row) for row in state_resources),
            "distinct_alternate_pairs": len(pairs),
            "activated_child_pairs": len(activated_pairs),
            "light_support_pairs": len(light_pairs),
            "allocated_pairs": len(allocated_by_pair),
            "saturated_pairs": len(saturated_pairs),
            "min_cut_states": len(cut_states),
            "min_cut_pairs": len(cut_pairs),
        },
        "masses": {
            "total_recursive_demand": serialize_mass(total_demand),
            "total_alternate_capacity": serialize_mass(
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
            "minimum_state_alternate_surplus": serialize_mass(
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
            "statewise_alternate_route_domination": min(state_surpluses) > 0,
            "exact_alternate_route_flow_feasible": unmet == 0,
            "all_allocations_within_one_pair_capacity": all(
                allocated_by_pair[pair] <= available_capacity[pair]
                for pair in allocated_by_pair
            ),
            "pointwise_or_shell_gap_decrease": True,
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
