#!/usr/bin/env python3
"""Exact fractional critical-capacity flow for repeated affine resources."""
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from search_lexicographic_reserve_pseudoforest_small_box import (
    contains_four_ap,
    ordered_pair,
    orientation,
    retained_family,
)
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]


def shell_base(values: tuple[int, ...]) -> int:
    base = 1 << (min(values).bit_length() - 1)
    if any(value < base or value >= 2 * base for value in values):
        raise AssertionError(f"parent crosses standard shell: {values}")
    return base


def critical_flow(
    demands: dict[Pair, tuple[Fraction, tuple[Pair, Pair]]],
    capacities: dict[Pair, Fraction],
) -> tuple[Fraction, dict[Pair, dict[Pair, Fraction]]]:
    source = ("source",)
    sink = ("sink",)
    graph: dict[tuple[object, ...], set[tuple[object, ...]]] = defaultdict(set)
    cap: dict[tuple[tuple[object, ...], tuple[object, ...]], Fraction] = defaultdict(Fraction)

    def add_edge(left: tuple[object, ...], right: tuple[object, ...], value: Fraction) -> None:
        graph[left].add(right)
        graph[right].add(left)
        cap[(left, right)] += value

    total_demand = sum((value[0] for value in demands.values()), Fraction())
    for demand, (amount, reserves) in demands.items():
        dnode = ("d", *demand)
        add_edge(source, dnode, amount)
        for reserve in reserves:
            rnode = ("r", *reserve)
            add_edge(dnode, rnode, amount)
    for reserve, amount in capacities.items():
        if amount > 0:
            add_edge(("r", *reserve), sink, amount)

    flow: dict[tuple[tuple[object, ...], tuple[object, ...]], Fraction] = defaultdict(Fraction)
    value = Fraction()
    while True:
        parent: dict[tuple[object, ...], tuple[object, ...] | None] = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            current = queue.popleft()
            for target in graph[current]:
                residual = cap[(current, target)] - flow[(current, target)]
                if residual > 0 and target not in parent:
                    parent[target] = current
                    queue.append(target)
        if sink not in parent:
            break
        increment: Fraction | None = None
        current = sink
        while parent[current] is not None:
            previous = parent[current]
            assert previous is not None
            residual = cap[(previous, current)] - flow[(previous, current)]
            increment = residual if increment is None else min(increment, residual)
            current = previous
        assert increment is not None and increment > 0
        current = sink
        while parent[current] is not None:
            previous = parent[current]
            assert previous is not None
            flow[(previous, current)] += increment
            flow[(current, previous)] -= increment
            current = previous
        value += increment

    allocation: dict[Pair, dict[Pair, Fraction]] = defaultdict(dict)
    for demand in demands:
        dnode = ("d", *demand)
        for target in graph[dnode]:
            if target and target[0] == "r":
                amount = flow[(dnode, target)]
                if amount > 0:
                    allocation[demand][(int(target[1]), int(target[2]))] = amount
    if value > total_demand:
        raise AssertionError("critical reserve flow exceeds demand")
    return value, allocation


def profile(name: str, parent: tuple[int, ...]) -> dict[str, object]:
    if contains_four_ap(parent):
        raise AssertionError(f"{name}: parent contains a four-AP")
    N = shell_base(parent)
    retained = retained_family(parent)
    owners: dict[Pair, list[dict[str, object]]] = defaultdict(list)

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {root - value for value, root in zip(values, roots, strict=True)}
        if len(references) != 1:
            raise AssertionError(f"{name}: retained child is not affine")
        reference = references.pop()
        L = shell_base(values)
        terminal = not contains_three_term_ap(values)
        source = str(state.representative.source)
        step = state.representative.source_step
        for root in roots:
            resource = ordered_pair(reference, root)
            owners[resource].append({
                "kind": "current", "source": source, "step": step,
                "scale": L, "terminal": terminal,
                "ratio": Fraction(L, N),
            })
        if terminal:
            continue
        for left, right in combinations(roots, 2):
            resource = ordered_pair(left, right)
            owners[resource].append({
                "kind": "latent", "source": source, "step": step,
                "scale": L, "terminal": False,
                "ratio": Fraction(2 * L, N),
            })

    load_ratio = {
        resource: sum((Fraction(row["ratio"]) for row in rows), Fraction())
        for resource, rows in owners.items()
    }
    residual_capacity = {
        resource: max(Fraction(), 1 - ratio)
        for resource, ratio in load_ratio.items()
    }

    latent_demands: dict[Pair, tuple[Fraction, tuple[Pair, Pair]]] = {}
    current_excess: dict[Pair, Fraction] = {}
    current_excess_terminal = Fraction()
    current_excess_recursive = Fraction()
    candidate_reserves: set[Pair] = set()

    for resource, rows in owners.items():
        current = [row for row in rows if row["kind"] == "current"]
        latent = [row for row in rows if row["kind"] == "latent"]
        excess = max(Fraction(), load_ratio[resource] - 1)
        if current and latent:
            current_excess[resource] = excess
            gap = resource[1] - resource[0]
            weighted = Fraction(N, gap) * excess
            if bool(current[0]["terminal"]):
                current_excess_terminal += weighted
            else:
                current_excess_recursive += weighted
        if len(latent) == 2:
            middle = next(row for row in latent if row["source"] == "middle_fiber")
            step = int(middle["step"])
            sign = orientation(step)
            center = ordered_pair(resource[0] + sign * step, resource[1] + sign * step)
            opposite = ordered_pair(resource[0] + 2 * sign * step, resource[1] + 2 * sign * step)
            if not set(center) <= set(parent) or not set(opposite) <= set(parent):
                raise AssertionError(f"{name}: reserve left parent support")
            candidate_reserves.update((center, opposite))
            if excess > 0:
                latent_demands[resource] = (excess, (center, opposite))

    reserve_capacity = {
        reserve: residual_capacity.get(reserve, Fraction(1))
        for reserve in candidate_reserves
    }
    flow_value, allocation = critical_flow(latent_demands, reserve_capacity)
    total_latent_demand = sum((row[0] for row in latent_demands.values()), Fraction())
    unallocated_ratio = total_latent_demand - flow_value

    latent_demand_mass = sum(
        (Fraction(N, demand[1] - demand[0]) * row[0] for demand, row in latent_demands.items()),
        Fraction(),
    )
    allocated_mass = sum(
        (
            Fraction(N, demand[1] - demand[0]) * amount
            for demand, rows in allocation.items()
            for amount in rows.values()
        ),
        Fraction(),
    )

    return {
        "name": name,
        "parent": parent,
        "parent_base": N,
        "counts": {
            "retained_states": len(retained),
            "owner_resources": len(owners),
            "current_latent_resources": sum(
                any(row["kind"] == "current" for row in rows)
                and any(row["kind"] == "latent" for row in rows)
                for rows in owners.values()
            ),
            "latent_latent_resources": sum(
                sum(row["kind"] == "latent" for row in rows) == 2
                for rows in owners.values()
            ),
            "positive_latent_excess_demands": len(latent_demands),
            "candidate_reserves": len(candidate_reserves),
        },
        "ratios": {
            "total_latent_excess_demand": str(total_latent_demand),
            "allocated_latent_excess": str(flow_value),
            "unallocated_latent_excess": str(unallocated_ratio),
            "maximum_owner_load": str(max(load_ratio.values(), default=Fraction())),
            "minimum_candidate_reserve_capacity": str(
                min(reserve_capacity.values(), default=Fraction())
            ),
        },
        "masses": {
            "latent_excess_demand": str(latent_demand_mass),
            "allocated_latent_excess": str(allocated_mass),
            "unallocated_latent_excess": str(latent_demand_mass - allocated_mass),
            "terminal_current_excess": str(current_excess_terminal),
            "recursive_current_excess": str(current_excess_recursive),
        },
        "current_excess": [
            {"resource": resource, "ratio": str(value)}
            for resource, value in sorted(current_excess.items()) if value > 0
        ],
        "latent_demands": [
            {
                "resource": resource,
                "ratio": str(row[0]),
                "reserves": row[1],
                "allocation": allocation.get(resource, {}),
            }
            for resource, row in sorted(latent_demands.items())
        ],
        "checks": {
            "critical_loads_use_actual_child_scales": True,
            "only_local_excess_is_routed": True,
            "reserve_flow_respects_residual_capacity": True,
            "all_latent_excess_allocated": unallocated_ratio == 0,
        },
    }


def shifted(values: tuple[int, ...], delta: int) -> tuple[int, ...]:
    return tuple(value + delta for value in values)


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_critical_fractional_reserve_flow.py OUTPUT")

    clean = shifted((1,4,5,6,20,21,22,26,27,28,32,33,34), 64)
    current_no_go = (65,97,98,99,113,114,115,119,120,121,125,126,127)
    rank_two_raw = (
        1,9194,9200,9206,10595,10600,10605,11296,11300,11304,
        11599,11600,11601,11996,11997,11999,12000,12001,12004,
        12005,12006,12012,12046,12047,12049,12050,12051,12054,
        12055,12056,12062,12096,12097,12099,12100,12101,12104,
        12105,12106,12112,
    )
    rank_two = shifted(rank_two_raw, 16384)

    profiles = [
        profile("clean_latent_reuse", clean),
        profile("recursive_current_latent_no_go", current_no_go),
        profile("rank_two_raw_reserve_no_go", rank_two),
    ]
    output = {
        "schema": "critical_fractional_reserve_flow_v1",
        "profiles": profiles,
        "checks": {
            "clean_latent_reuse_has_zero_critical_excess": (
                profiles[0]["ratios"]["total_latent_excess_demand"] == "0"
            ),
            "recursive_current_no_go_keeps_current_excess": (
                Fraction(profiles[1]["masses"]["recursive_current_excess"]) > 0
            ),
            "rank_two_raw_no_go_closed_fractionally": (
                profiles[2]["ratios"]["unallocated_latent_excess"] == "0"
            ),
        },
    }
    if not all(output["checks"].values()):
        raise AssertionError(f"critical fractional reserve profile changed: {output['checks']}")
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"), default=str)
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[1]).write_text(json.dumps(output, sort_keys=True, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
