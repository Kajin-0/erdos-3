#!/usr/bin/env python3
"""Test whether primary-chain incidences repair the exact alternate-route min cut."""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_alternate_route_flow import alternate_resources
from probe_s7_direct_fractional_chain_flow import Dinic
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from s7_direct_chain_instance import Pair, RecursiveChainState, build_instance


@dataclass
class FlowResult:
    total_demand: Fraction
    maximum_flow: Fraction
    reachable: set[int]
    first_state: int
    first_pair: int
    pair_index: dict[Pair, int]
    available_capacity: dict[Pair, Fraction]
    allocations: list[tuple[int, Pair, Fraction]]


def solve(
    states: tuple[RecursiveChainState, ...],
    resources: tuple[tuple[Pair, ...], ...],
    light_usage: dict[Pair, Fraction],
) -> FlowResult:
    pair_universe = sorted({pair for row in resources for pair in row})
    pair_index = {pair: index for index, pair in enumerate(pair_universe)}

    source = 0
    first_state = 1
    first_pair = first_state + len(states)
    sink = first_pair + len(pair_universe)
    network = Dinic(sink + 1)

    total_demand = Fraction()
    handles: list[list[tuple[Pair, tuple[int, int]]]] = []
    for state_index, (state, row) in enumerate(zip(states, resources, strict=True)):
        state_node = first_state + state_index
        total_demand += state.debt
        network.add_edge(source, state_node, state.debt)
        state_handles: list[tuple[Pair, tuple[int, int]]] = []
        for pair in row:
            pair_node = first_pair + pair_index[pair]
            state_handles.append(
                (pair, network.add_edge(state_node, pair_node, state.debt))
            )
        handles.append(state_handles)

    available_capacity: dict[Pair, Fraction] = {}
    for pair in pair_universe:
        available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if available < 0:
            raise AssertionError("negative residual physical pair capacity")
        available_capacity[pair] = available
        network.add_edge(first_pair + pair_index[pair], sink, available)

    maximum_flow = network.max_flow(source, sink)
    allocations: list[tuple[int, Pair, Fraction]] = []
    for state_index, row in enumerate(handles):
        for pair, (node, edge_index) in row:
            edge = network.graph[node][edge_index]
            allocated = edge.original - edge.capacity
            if allocated > 0:
                allocations.append((state_index, pair, allocated))

    return FlowResult(
        total_demand=total_demand,
        maximum_flow=maximum_flow,
        reachable=network.reachable(source),
        first_state=first_state,
        first_pair=first_pair,
        pair_index=pair_index,
        available_capacity=available_capacity,
        allocations=allocations,
    )


def state_record(index: int, state: RecursiveChainState) -> dict[str, object]:
    return {
        "index": index,
        "completion": state.completion,
        "role": state.role,
        "coefficient": str(state.coefficient),
        "shell_base": state.shell_base,
        "state": state.state,
        "size": len(state.state),
        "debt": str(state.debt),
        "primary_chain": state.chain,
        "alternate_resources": alternate_resources(state),
    }


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_alternate_cut_primary_repair.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    instance = build_instance(Path(sys.argv[1]), Path(sys.argv[2]))
    light_usage: dict[Pair, Fraction] = instance["light_usage"]  # type: ignore[assignment]
    states: tuple[RecursiveChainState, ...] = instance["recursive_states"]  # type: ignore[assignment]

    alternate = tuple(alternate_resources(state) for state in states)
    alternate_result = solve(states, alternate, light_usage)
    alternate_unmet = alternate_result.total_demand - alternate_result.maximum_flow
    cut_states = tuple(
        index
        for index in range(len(states))
        if alternate_result.first_state + index in alternate_result.reachable
    )
    cut_pairs = tuple(
        pair
        for pair, pair_index in alternate_result.pair_index.items()
        if alternate_result.first_pair + pair_index in alternate_result.reachable
    )
    cut_demand = sum((states[index].debt for index in cut_states), Fraction())
    cut_capacity = sum(
        (alternate_result.available_capacity[pair] for pair in cut_pairs), Fraction()
    )

    if len(cut_states) != 19 or len(cut_pairs) != 176:
        raise AssertionError("alternate-route min-cut identity changed")
    if alternate_unmet <= 0 or cut_demand - cut_capacity != alternate_unmet:
        raise AssertionError("alternate-route min-cut deficit identity failed")

    cut_set = set(cut_states)
    mixed_resources: list[tuple[Pair, ...]] = []
    for index, state in enumerate(states):
        row = list(alternate[index])
        if index in cut_set:
            row.extend(state.chain)
        mixed_resources.append(tuple(dict.fromkeys(row)))

    mixed = solve(states, tuple(mixed_resources), light_usage)
    mixed_unmet = mixed.total_demand - mixed.maximum_flow

    route_mass = defaultdict(Fraction)
    route_edges = Counter()
    primary_states: set[int] = set()
    primary_pairs: set[Pair] = set()
    for state_index, pair, allocated in mixed.allocations:
        alt_set = set(alternate[state_index])
        primary_set = set(states[state_index].chain) if state_index in cut_set else set()
        if pair in primary_set and pair not in alt_set:
            route = "primary_only"
            primary_states.add(state_index)
            primary_pairs.add(pair)
        elif pair in primary_set and pair in alt_set:
            route = "shared"
            primary_states.add(state_index)
            primary_pairs.add(pair)
        else:
            route = "alternate_only"
        route_mass[route] += allocated
        route_edges[route] += 1

    primary_candidate_pairs = {
        pair for index in cut_states for pair in states[index].chain
    }
    alternate_pair_universe = set(alternate_result.pair_index)
    new_primary_identities = primary_candidate_pairs - alternate_pair_universe
    overlapping_primary_identities = primary_candidate_pairs & alternate_pair_universe

    role_profile = Counter(states[index].role for index in cut_states)
    shell_profile = Counter(states[index].shell_base for index in cut_states)
    size_profile = Counter(len(states[index].state) for index in cut_states)

    cut_rows = [state_record(index, states[index]) for index in cut_states]
    output = {
        "schema": "s7_alternate_cut_primary_repair_v1",
        "scope": "primary-chain augmentation restricted to the exact alternate-route min cut",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": len(states),
            "alternate_cut_states": len(cut_states),
            "alternate_cut_pairs": len(cut_pairs),
            "primary_candidate_pairs": len(primary_candidate_pairs),
            "new_primary_pair_identities": len(new_primary_identities),
            "overlapping_primary_pair_identities": len(overlapping_primary_identities),
            "mixed_positive_allocation_edges": len(mixed.allocations),
            "states_using_primary_route": len(primary_states),
            "primary_pairs_used": len(primary_pairs),
        },
        "masses": {
            "total_recursive_demand": serialize_mass(mixed.total_demand),
            "alternate_maximum_flow": serialize_mass(alternate_result.maximum_flow),
            "alternate_unmet_demand": serialize_mass(alternate_unmet),
            "alternate_cut_demand": serialize_mass(cut_demand),
            "alternate_cut_capacity": serialize_mass(cut_capacity),
            "mixed_maximum_flow": serialize_mass(mixed.maximum_flow),
            "mixed_unmet_demand": serialize_mass(mixed_unmet),
            "mixed_alternate_only_allocation": serialize_mass(
                route_mass["alternate_only"]
            ),
            "mixed_primary_only_allocation": serialize_mass(route_mass["primary_only"]),
            "mixed_shared_allocation": serialize_mass(route_mass["shared"]),
        },
        "cut_profiles": {
            "role": [
                {"role": role, "states": role_profile[role]}
                for role in sorted(role_profile)
            ],
            "shell_base": [
                {"shell_base": base, "states": shell_profile[base]}
                for base in sorted(shell_profile)
            ],
            "size": [
                {"size": size, "states": size_profile[size]}
                for size in sorted(size_profile)
            ],
        },
        "cut_states": cut_rows,
        "hashes": {
            "cut_states": hashlib.sha256(
                json.dumps(cut_rows, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            ).hexdigest(),
            "mixed_allocations": hashlib.sha256(
                json.dumps(
                    [
                        (index, pair, str(value))
                        for index, pair, value in mixed.allocations
                    ],
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "alternate_exact_min_cut": cut_demand - cut_capacity == alternate_unmet,
            "primary_augmentation_restricted_to_cut": True,
            "mixed_flow_feasible": mixed_unmet == 0,
            "mixed_allocation_mass_identity": sum(
                (value for _index, _pair, value in mixed.allocations), Fraction()
            )
            == mixed.maximum_flow,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[3]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
