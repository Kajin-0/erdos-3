#!/usr/bin/env python3
"""Solve exact fractional horizontal-chain capacity packing on the direct S7 frontier."""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_pair_discharge import completion_candidates, harmonic
from probe_s7_hole_support_closure import build_s7, canonical_pair, read_full_hole_map
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap


Pair = tuple[int, int]


@dataclass
class Edge:
    to: int
    reverse: int
    capacity: Fraction
    original: Fraction


class Dinic:
    def __init__(self, size: int) -> None:
        self.graph: list[list[Edge]] = [[] for _ in range(size)]
        self.level = [-1] * size
        self.cursor = [0] * size

    def add_edge(self, source: int, target: int, capacity: Fraction) -> tuple[int, int]:
        if capacity < 0:
            raise ValueError("negative flow capacity")
        forward = Edge(target, len(self.graph[target]), capacity, capacity)
        reverse = Edge(source, len(self.graph[source]), Fraction(), Fraction())
        self.graph[source].append(forward)
        self.graph[target].append(reverse)
        return source, len(self.graph[source]) - 1

    def build_levels(self, source: int, sink: int) -> bool:
        self.level = [-1] * len(self.graph)
        self.level[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            node = queue.popleft()
            for edge in self.graph[node]:
                if edge.capacity > 0 and self.level[edge.to] < 0:
                    self.level[edge.to] = self.level[node] + 1
                    queue.append(edge.to)
        return self.level[sink] >= 0

    def send(self, node: int, sink: int, amount: Fraction) -> Fraction:
        if node == sink:
            return amount
        while self.cursor[node] < len(self.graph[node]):
            index = self.cursor[node]
            edge = self.graph[node][index]
            if edge.capacity > 0 and self.level[edge.to] == self.level[node] + 1:
                sent = self.send(edge.to, sink, min(amount, edge.capacity))
                if sent > 0:
                    edge.capacity -= sent
                    reverse = self.graph[edge.to][edge.reverse]
                    reverse.capacity += sent
                    return sent
            self.cursor[node] += 1
        return Fraction()

    def max_flow(self, source: int, sink: int) -> Fraction:
        total = Fraction()
        infinity = sum(
            (edge.capacity for edge in self.graph[source]), Fraction()
        )
        while self.build_levels(source, sink):
            self.cursor = [0] * len(self.graph)
            while True:
                sent = self.send(source, sink, infinity)
                if sent == 0:
                    break
                total += sent
        return total

    def reachable(self, source: int) -> set[int]:
        seen = {source}
        queue: deque[int] = deque([source])
        while queue:
            node = queue.popleft()
            for edge in self.graph[node]:
                if edge.capacity > 0 and edge.to not in seen:
                    seen.add(edge.to)
                    queue.append(edge.to)
        return seen


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate chain pair")
    return (left, right) if left < right else (right, left)


def physical_chain(
    completion: int, role: str, state: tuple[int, ...]
) -> tuple[Pair, ...]:
    if role == "right_adjacent":
        points = tuple(completion + step for step in state)
    elif role in {"left_adjacent", "outer"}:
        points = tuple(sorted(completion - step for step in state))
    else:
        raise AssertionError(f"unknown completion role: {role}")
    return tuple(
        ordered_pair(points[index], points[index + 1])
        for index in range(len(points) - 1)
    )


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_fractional_chain_flow.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    payment = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    if not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks source rows")

    s7 = build_s7()
    holes = read_full_hole_map(Path(sys.argv[2]))
    activated: set[Pair] = {
        tuple(int(value) for value in row["pair"])
        for row in source_rows
    }
    if len(activated) != 75_247:
        raise AssertionError("activated S7 pair union changed")

    selected_holes: list[tuple[Pair, int, str, int, Fraction, Pair]] = []
    for pair in sorted(activated):
        candidates = completion_candidates(pair)
        if any(completion in s7 for completion, _role, _step, _alpha in candidates):
            continue
        certified = [row for row in candidates if row[0] in holes]
        if not certified:
            continue
        completion, role, step, coefficient = min(certified)
        selected_holes.append(
            (
                pair,
                completion,
                role,
                step,
                coefficient,
                canonical_pair(*holes[completion]),
            )
        )

    groups: dict[tuple[Pair, int, str, Fraction], set[int]] = defaultdict(set)
    roles_by_support: dict[Pair, set[tuple[int, str, Fraction]]] = defaultdict(set)
    for _pair, completion, role, step, coefficient, support in selected_holes:
        groups[(support, completion, role, coefficient)].add(step)
        roles_by_support[support].add((completion, role, coefficient))

    light_usage: dict[Pair, Fraction] = defaultdict(Fraction)
    recursive_states: list[
        tuple[int, str, Fraction, int, tuple[int, ...], Fraction]
    ] = []
    terminal_shells = 0

    for support, roles in sorted(roles_by_support.items()):
        multiplicity = len(roles)
        threshold = (
            Fraction()
            if support in activated
            else pair_weight(support) / multiplicity
        )
        for completion, role, coefficient in sorted(roles):
            steps = groups[(support, completion, role, coefficient)]
            role_load = coefficient * harmonic(steps)
            if role_load <= threshold:
                light_usage[support] += role_load
                continue
            shells: dict[int, set[int]] = defaultdict(set)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].add(step)
            for shell_base, shell_steps in sorted(shells.items()):
                state = tuple(sorted(shell_steps))
                debt = coefficient * harmonic(state)
                if not contains_three_term_ap(state):
                    terminal_shells += 1
                    continue
                recursive_states.append(
                    (completion, role, coefficient, shell_base, state, debt)
                )

    if len(recursive_states) != 278 or terminal_shells != 23_638:
        raise AssertionError("direct heavy frontier changed")
    if set(light_usage) & activated:
        raise AssertionError("light support usage overlaps activated pair debt")
    for pair, usage in light_usage.items():
        if usage > pair_weight(pair):
            raise AssertionError("light support usage exceeds physical capacity")

    state_chains: list[tuple[Pair, ...]] = []
    pair_universe: set[Pair] = set()
    for completion, role, _coefficient, shell_base, state, debt in recursive_states:
        chain = physical_chain(completion, role, state)
        if len(chain) != len(state) - 1:
            raise AssertionError("horizontal chain length mismatch")
        chain_capacity = Fraction()
        for pair in chain:
            if not set(pair) <= s7:
                raise AssertionError("horizontal chain pair left S7")
            if pair[1] - pair[0] >= shell_base:
                raise AssertionError("horizontal chain failed strict gap descent")
            chain_capacity += pair_weight(pair)
            pair_universe.add(pair)
        if chain_capacity <= debt:
            raise AssertionError("state chain capacity does not dominate debt")
        state_chains.append(chain)

    states = len(recursive_states)
    pairs = sorted(pair_universe)
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    source = 0
    first_state = 1
    first_pair = first_state + states
    sink = first_pair + len(pairs)
    network = Dinic(sink + 1)

    total_demand = Fraction()
    source_edges: list[tuple[int, int]] = []
    state_pair_edges: list[list[tuple[Pair, tuple[int, int]]]] = []
    for state_index, ((*_metadata, debt), chain) in enumerate(
        zip(recursive_states, state_chains, strict=True)
    ):
        state_node = first_state + state_index
        total_demand += debt
        source_edges.append(network.add_edge(source, state_node, debt))
        row_edges: list[tuple[Pair, tuple[int, int]]] = []
        for pair in chain:
            pair_node = first_pair + pair_index[pair]
            handle = network.add_edge(state_node, pair_node, debt)
            row_edges.append((pair, handle))
        state_pair_edges.append(row_edges)

    available_capacity: dict[Pair, Fraction] = {}
    pair_sink_edges: dict[Pair, tuple[int, int]] = {}
    for pair in pairs:
        if pair in activated:
            available = Fraction()
        else:
            available = pair_weight(pair) - light_usage.get(pair, Fraction())
        if available < 0:
            raise AssertionError("negative residual pair capacity")
        available_capacity[pair] = available
        pair_node = first_pair + pair_index[pair]
        pair_sink_edges[pair] = network.add_edge(pair_node, sink, available)

    flow = network.max_flow(source, sink)
    unmet = total_demand - flow
    reachable = network.reachable(source)

    used_pairs: set[Pair] = set()
    saturated_pairs: set[Pair] = set()
    allocation_rows: list[tuple[int, Pair, str]] = []
    maximum_utilization = Fraction()
    allocated_by_pair: dict[Pair, Fraction] = defaultdict(Fraction)

    for state_index, row_edges in enumerate(state_pair_edges):
        for pair, (node, edge_index) in row_edges:
            edge = network.graph[node][edge_index]
            allocated = edge.original - edge.capacity
            if allocated > 0:
                used_pairs.add(pair)
                allocated_by_pair[pair] += allocated
                allocation_rows.append((state_index, pair, str(allocated)))

    for pair, allocated in allocated_by_pair.items():
        available = available_capacity[pair]
        if allocated > available:
            raise AssertionError("fractional allocation exceeds pair capacity")
        if available > 0:
            maximum_utilization = max(maximum_utilization, allocated / available)
        if allocated == available and available > 0:
            saturated_pairs.add(pair)

    cut_states = [
        index
        for index in range(states)
        if first_state + index in reachable
    ]
    cut_pairs = [
        pair
        for pair in pairs
        if first_pair + pair_index[pair] in reachable
    ]
    cut_demand = sum(
        (recursive_states[index][-1] for index in cut_states), Fraction()
    )
    cut_capacity = sum(
        (available_capacity[pair] for pair in cut_pairs), Fraction()
    )

    output = {
        "schema": "s7_direct_fractional_chain_flow_v1",
        "scope": "exact rational packing of recursive direct-discharge debt into horizontal-chain pair capacity",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_states": states,
            "chain_pair_universe": len(pairs),
            "used_chain_pairs": len(used_pairs),
            "saturated_chain_pairs": len(saturated_pairs),
            "activated_pair_overlaps": sum(pair in activated for pair in pairs),
            "light_support_overlaps": sum(pair in light_usage for pair in pairs),
            "min_cut_states": len(cut_states),
            "min_cut_pairs": len(cut_pairs),
        },
        "masses": {
            "total_recursive_demand": serialize_mass(total_demand),
            "available_chain_pair_capacity": serialize_mass(
                sum(available_capacity.values(), Fraction())
            ),
            "maximum_flow": serialize_mass(flow),
            "unmet_demand": serialize_mass(unmet),
            "used_pair_capacity": serialize_mass(
                sum(allocated_by_pair.values(), Fraction())
            ),
            "residual_used_pair_capacity": serialize_mass(
                sum(
                    (
                        available_capacity[pair] - allocated_by_pair[pair]
                        for pair in used_pairs
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
                json.dumps(pairs, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "positive_allocations": hashlib.sha256(
                json.dumps(allocation_rows, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "exact_fractional_packing_feasible": unmet == 0,
            "all_allocations_within_capacity": all(
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
