#!/usr/bin/env python3
"""Pack direct S7 recursive debt into one lower-gap Bellman capacity per pair."""
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


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_gap_triangular_chain_flow.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    instance = build_instance(Path(sys.argv[1]), Path(sys.argv[2]))
    activated: set[Pair] = instance["activated"]  # type: ignore[assignment]
    light_usage: dict[Pair, Fraction] = instance["light_usage"]  # type: ignore[assignment]
    recursive_states: tuple[RecursiveChainState, ...] = instance["recursive_states"]  # type: ignore[assignment]

    pair_universe = sorted(
        {pair for state in recursive_states for pair in state.chain}
    )
    pair_index = {pair: index for index, pair in enumerate(pair_universe)}

    source = 0
    first_state = 1
    first_pair = first_state + len(recursive_states)
    sink = first_pair + len(pair_universe)
    network = Dinic(sink + 1)

    total_demand = Fraction()
    allocation_handles: list[list[tuple[Pair, tuple[int, int]]]] = []
    for state_index, state in enumerate(recursive_states):
        state_node = first_state + state_index
        total_demand += state.debt
        network.add_edge(source, state_node, state.debt)
        handles: list[tuple[Pair, tuple[int, int]]] = []
        for pair in state.chain:
            pair_node = first_pair + pair_index[pair]
            handles.append(
                (pair, network.add_edge(state_node, pair_node, state.debt))
            )
        allocation_handles.append(handles)

    available_capacity: dict[Pair, Fraction] = {}
    for pair in pair_universe:
        # A lower-gap activated pair is a legitimate Bellman child term.  Its one
        # physical capacity may absorb incoming debt from larger-gap shells.
        # Light-fiber load already assigned to the same pair is subtracted.
        available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if available < 0:
            raise AssertionError("negative lower-gap residual pair capacity")
        available_capacity[pair] = available
        pair_node = first_pair + pair_index[pair]
        network.add_edge(pair_node, sink, available)

    maximum_flow = network.max_flow(source, sink)
    unmet = total_demand - maximum_flow
    reachable = network.reachable(source)

    allocated_by_pair: dict[Pair, Fraction] = defaultdict(Fraction)
    allocation_rows: list[tuple[int, Pair, str]] = []
    for state_index, handles in enumerate(allocation_handles):
        for pair, (node, edge_index) in handles:
            edge = network.graph[node][edge_index]
            allocated = edge.original - edge.capacity
            if allocated > 0:
                allocated_by_pair[pair] += allocated
                allocation_rows.append((state_index, pair, str(allocated)))

    maximum_utilization = Fraction()
    saturated_pairs: set[Pair] = set()
    activated_used: set[Pair] = set()
    light_used: set[Pair] = set()
    for pair, allocated in allocated_by_pair.items():
        capacity = available_capacity[pair]
        if allocated > capacity:
            raise AssertionError("gap-triangular allocation exceeds pair capacity")
        if capacity > 0:
            maximum_utilization = max(maximum_utilization, allocated / capacity)
        if allocated == capacity and capacity > 0:
            saturated_pairs.add(pair)
        if pair in activated:
            activated_used.add(pair)
        if pair in light_usage:
            light_used.add(pair)

    cut_states = [
        index
        for index in range(len(recursive_states))
        if first_state + index in reachable
    ]
    cut_pairs = [
        pair
        for pair in pair_universe
        if first_pair + pair_index[pair] in reachable
    ]
    cut_demand = sum(
        (recursive_states[index].debt for index in cut_states), Fraction()
    )
    cut_capacity = sum(
        (available_capacity[pair] for pair in cut_pairs), Fraction()
    )

    # Verify the triangular scale relation occurrencewise, including pairs that
    # are themselves members of the entering activated union.
    for state in recursive_states:
        for pair in state.chain:
            if pair[1] - pair[0] >= state.shell_base:
                raise AssertionError("gap-triangular edge did not descend")

    output = {
        "schema": "s7_direct_gap_triangular_chain_flow_v1",
        "scope": "exact rational lower-gap Bellman packing for recursive direct-discharge debt",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": len(recursive_states),
            "chain_pair_universe": len(pair_universe),
            "allocated_pairs": len(allocated_by_pair),
            "saturated_pairs": len(saturated_pairs),
            "activated_child_pairs_used": len(activated_used),
            "light_support_pairs_used": len(light_used),
            "min_cut_states": len(cut_states),
            "min_cut_pairs": len(cut_pairs),
        },
        "masses": {
            "total_recursive_demand": serialize_mass(total_demand),
            "total_lower_gap_capacity": serialize_mass(
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
            "min_cut_state_demand": serialize_mass(cut_demand),
            "min_cut_pair_capacity": serialize_mass(cut_capacity),
        },
        "maximum_pair_utilization": {
            "fraction": str(maximum_utilization),
            "decimal": f"{float(maximum_utilization):.12f}",
        },
        "hashes": {
            "pair_universe": hashlib.sha256(
                json.dumps(pair_universe, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "positive_allocations": hashlib.sha256(
                json.dumps(allocation_rows, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "exact_gap_triangular_flow_feasible": unmet == 0,
            "all_allocations_within_one_pair_capacity": all(
                allocated_by_pair[pair] <= available_capacity[pair]
                for pair in allocated_by_pair
            ),
            "strict_gap_descent": True,
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
