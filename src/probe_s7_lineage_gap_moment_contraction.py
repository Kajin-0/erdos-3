#!/usr/bin/env python3
"""Measure dyadic gap-moment contraction in the exact S7 recursive flow."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_fractional_chain_flow import Dinic
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from s7_direct_chain_instance import Pair, RecursiveChainState, build_instance


def dyadic_base(value: int) -> int:
    if value <= 0:
        raise AssertionError("dyadic base requires a positive integer")
    return 1 << (value.bit_length() - 1)


def ratio_record(numerator: Fraction, denominator: Fraction) -> dict[str, str]:
    if denominator <= 0:
        raise AssertionError("moment ratio has nonpositive denominator")
    value = numerator / denominator
    return {"fraction": str(value), "decimal": f"{float(value):.12f}"}


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_lineage_gap_moment_contraction.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    instance = build_instance(Path(sys.argv[1]), Path(sys.argv[2]))
    light_usage: dict[Pair, Fraction] = instance["light_usage"]  # type: ignore[assignment]
    recursive_states: tuple[RecursiveChainState, ...] = instance["recursive_states"]  # type: ignore[assignment]

    pair_universe = sorted({pair for state in recursive_states for pair in state.chain})
    pair_index = {pair: index for index, pair in enumerate(pair_universe)}

    source = 0
    first_state = 1
    first_pair = first_state + len(recursive_states)
    sink = first_pair + len(pair_universe)
    network = Dinic(sink + 1)

    total_demand = Fraction()
    input_moment_1 = Fraction()
    input_moment_2 = Fraction()
    handles: list[list[tuple[Pair, tuple[int, int]]]] = []

    for state_index, state in enumerate(recursive_states):
        state_node = first_state + state_index
        total_demand += state.debt
        input_moment_1 += state.debt * state.shell_base
        input_moment_2 += state.debt * state.shell_base * state.shell_base
        network.add_edge(source, state_node, state.debt)
        row: list[tuple[Pair, tuple[int, int]]] = []
        for pair in state.chain:
            pair_node = first_pair + pair_index[pair]
            row.append((pair, network.add_edge(state_node, pair_node, state.debt)))
        handles.append(row)

    available_capacity: dict[Pair, Fraction] = {}
    for pair in pair_universe:
        available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if available < 0:
            raise AssertionError("negative residual pair capacity")
        available_capacity[pair] = available
        network.add_edge(first_pair + pair_index[pair], sink, available)

    maximum_flow = network.max_flow(source, sink)
    unmet = total_demand - maximum_flow
    if unmet != 0:
        raise AssertionError("certified S7 gap-triangular flow became infeasible")

    output_moment_1 = Fraction()
    output_moment_2 = Fraction()
    depth_release = Fraction()
    allocated_mass = Fraction()
    drop_mass: dict[int, Fraction] = defaultdict(Fraction)
    drop_edges = Counter()
    allocation_rows: list[tuple[int, Pair, str, int, int, int]] = []

    for state_index, row in enumerate(handles):
        state = recursive_states[state_index]
        for pair, (node, edge_index) in row:
            edge = network.graph[node][edge_index]
            allocated = edge.original - edge.capacity
            if allocated <= 0:
                continue
            gap = pair[1] - pair[0]
            target_base = dyadic_base(gap)
            if target_base > state.shell_base // 2:
                raise AssertionError("allocated pair failed one-level dyadic descent")
            drop = state.shell_base.bit_length() - target_base.bit_length()
            if drop < 1:
                raise AssertionError("allocated pair has nonpositive depth drop")

            allocated_mass += allocated
            output_moment_1 += allocated * target_base
            output_moment_2 += allocated * target_base * target_base
            depth_release += allocated * drop
            drop_mass[drop] += allocated
            drop_edges[drop] += 1
            allocation_rows.append(
                (state_index, pair, str(allocated), state.shell_base, target_base, drop)
            )

    if allocated_mass != total_demand:
        raise AssertionError("lineage allocation mass does not equal recursive demand")
    if output_moment_1 > input_moment_1 / 2:
        raise AssertionError("critical gap moment failed factor-one-half contraction")
    if output_moment_2 > input_moment_2 / 4:
        raise AssertionError("quadratic gap moment failed factor-one-quarter contraction")
    if depth_release < total_demand:
        raise AssertionError("logarithmic depth release is below transported demand")

    output = {
        "schema": "s7_lineage_gap_moment_contraction_v1",
        "scope": "occurrence-owned dyadic gap moments on the exact recursive S7 flow",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": len(recursive_states),
            "pair_universe": len(pair_universe),
            "positive_allocation_edges": len(allocation_rows),
            "minimum_depth_drop": min(drop_mass),
            "maximum_depth_drop": max(drop_mass),
        },
        "masses": {
            "recursive_demand": serialize_mass(total_demand),
            "allocated_lineage_mass": serialize_mass(allocated_mass),
            "input_gap_moment_p1": serialize_mass(input_moment_1),
            "output_gap_moment_p1": serialize_mass(output_moment_1),
            "released_gap_moment_p1": serialize_mass(input_moment_1 - output_moment_1),
            "input_gap_moment_p2": serialize_mass(input_moment_2),
            "output_gap_moment_p2": serialize_mass(output_moment_2),
            "released_gap_moment_p2": serialize_mass(input_moment_2 - output_moment_2),
            "dyadic_depth_release": serialize_mass(depth_release),
        },
        "ratios": {
            "p1_output_over_input": ratio_record(output_moment_1, input_moment_1),
            "p2_output_over_input": ratio_record(output_moment_2, input_moment_2),
            "depth_release_over_demand": ratio_record(depth_release, total_demand),
        },
        "depth_profile": [
            {
                "levels": levels,
                "allocation_edges": drop_edges[levels],
                "allocated_mass": serialize_mass(drop_mass[levels]),
            }
            for levels in sorted(drop_mass)
        ],
        "hashes": {
            "positive_allocations_with_depth": hashlib.sha256(
                json.dumps(allocation_rows, separators=(",", ":")).encode("utf-8")
            ).hexdigest()
        },
        "checks": {
            "exact_flow_feasible": unmet == 0,
            "allocation_mass_identity": allocated_mass == total_demand,
            "p1_factor_half_contraction": output_moment_1 <= input_moment_1 / 2,
            "p2_factor_quarter_contraction": output_moment_2 <= input_moment_2 / 4,
            "depth_release_dominates_demand": depth_release >= total_demand,
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
