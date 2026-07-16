#!/usr/bin/env python3
"""Exact joint critical-capacity assignment for affine child resources."""
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
Node = tuple[object, ...]


def shell_base(values: tuple[int, ...]) -> int:
    base = 1 << (min(values).bit_length() - 1)
    if any(value < base or value >= 2 * base for value in values):
        raise AssertionError(f"state crosses standard shell: {values}")
    return base


def maximum_fractional_assignment(
    demands: dict[Pair, tuple[Fraction, tuple[Pair, ...]]],
    capacities: dict[Pair, Fraction],
) -> tuple[Fraction, dict[Pair, dict[Pair, Fraction]]]:
    source: Node = ("source",)
    sink: Node = ("sink",)
    graph: dict[Node, set[Node]] = defaultdict(set)
    capacity: dict[tuple[Node, Node], Fraction] = defaultdict(Fraction)

    def add_edge(left: Node, right: Node, value: Fraction) -> None:
        graph[left].add(right)
        graph[right].add(left)
        capacity[(left, right)] += value

    total_demand = sum((row[0] for row in demands.values()), Fraction())
    for demand, (amount, choices) in sorted(demands.items()):
        demand_node: Node = ("d", *demand)
        add_edge(source, demand_node, amount)
        for choice in sorted(set(choices)):
            add_edge(demand_node, ("p", *choice), amount)
    for pair, amount in sorted(capacities.items()):
        if amount > 0:
            add_edge(("p", *pair), sink, amount)

    flow: dict[tuple[Node, Node], Fraction] = defaultdict(Fraction)
    value = Fraction()
    while True:
        parent: dict[Node, Node | None] = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            current = queue.popleft()
            for target in sorted(graph[current], key=repr):
                residual = capacity[(current, target)] - flow[(current, target)]
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
            residual = capacity[(previous, current)] - flow[(previous, current)]
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
    for demand in sorted(demands):
        demand_node: Node = ("d", *demand)
        for target in sorted(graph[demand_node], key=repr):
            if target and target[0] == "p":
                amount = flow[(demand_node, target)]
                if amount > 0:
                    allocation[demand][(int(target[1]), int(target[2]))] = amount
    if value > total_demand:
        raise AssertionError("critical assignment exceeds demand")
    return value, allocation


def translated_choices(
    parent: set[int],
    resource: Pair,
    middle_step: int,
) -> tuple[Pair, Pair, Pair]:
    sign = orientation(middle_step)
    center = ordered_pair(
        resource[0] + sign * middle_step,
        resource[1] + sign * middle_step,
    )
    opposite = ordered_pair(
        resource[0] + 2 * sign * middle_step,
        resource[1] + 2 * sign * middle_step,
    )
    if not set(center) <= parent or not set(opposite) <= parent:
        raise AssertionError("translated reserve left parent support")
    gap = resource[1] - resource[0]
    if center[1] - center[0] != gap or opposite[1] - opposite[0] != gap:
        raise AssertionError("translated choice changed physical gap")
    return resource, center, opposite


def profile(name: str, parent: tuple[int, ...]) -> dict[str, object]:
    if contains_four_ap(parent):
        raise AssertionError(f"{name}: parent contains a four-AP")
    parent_set = set(parent)
    parent_base = shell_base(parent)
    retained = retained_family(parent)
    owners: dict[Pair, list[dict[str, object]]] = defaultdict(list)

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {root - value for value, root in zip(values, roots, strict=True)}
        if len(references) != 1:
            raise AssertionError(f"{name}: retained child is not affine")
        reference = references.pop()
        child_base = shell_base(values)
        terminal = not contains_three_term_ap(values)
        source = str(state.representative.source)
        step = state.representative.source_step

        for root in roots:
            resource = ordered_pair(reference, root)
            owners[resource].append(
                {
                    "kind": "current",
                    "source": source,
                    "step": step,
                    "scale": child_base,
                    "terminal": terminal,
                    "ratio": Fraction(child_base, parent_base),
                }
            )
        if terminal:
            continue
        for left, right in combinations(roots, 2):
            resource = ordered_pair(left, right)
            owners[resource].append(
                {
                    "kind": "latent",
                    "source": source,
                    "step": step,
                    "scale": child_base,
                    "terminal": False,
                    "ratio": Fraction(2 * child_base, parent_base),
                }
            )

    fixed_load: dict[Pair, Fraction] = defaultdict(Fraction)
    flexible_demands: dict[Pair, tuple[Fraction, tuple[Pair, ...]]] = {}
    demand_meta: dict[Pair, dict[str, object]] = {}

    for resource, rows in owners.items():
        current_rows = [row for row in rows if row["kind"] == "current"]
        latent_rows = [row for row in rows if row["kind"] == "latent"]
        middle_latent = [row for row in latent_rows if row["source"] == "middle_fiber"]
        nonmiddle_latent = [row for row in latent_rows if row["source"] != "middle_fiber"]

        if len(middle_latent) > 1:
            raise AssertionError(f"{name}: one resource has two middle latent owners")
        if len(latent_rows) > 2:
            raise AssertionError(f"{name}: latent degree exceeded two")
        if len(current_rows) > 1 or len(rows) > 2:
            raise AssertionError(f"{name}: total owner degree exceeded two")

        for row in current_rows:
            fixed_load[resource] += Fraction(row["ratio"])

        if middle_latent:
            middle = middle_latent[0]
            choices = translated_choices(parent_set, resource, int(middle["step"]))
            amount = sum((Fraction(row["ratio"]) for row in latent_rows), Fraction())
            flexible_demands[resource] = (amount, choices)
            demand_meta[resource] = {
                "middle_scale": int(middle["scale"]),
                "step": int(middle["step"]),
                "natural": choices[0],
                "center": choices[1],
                "opposite": choices[2],
                "latent_owners": len(latent_rows),
                "current_overlap": bool(current_rows),
            }
        else:
            for row in nonmiddle_latent:
                fixed_load[resource] += Fraction(row["ratio"])

    fixed_excess = {
        resource: max(Fraction(), value - 1)
        for resource, value in fixed_load.items()
        if value > 1
    }
    pair_universe = {
        pair
        for _demand, (_amount, choices) in flexible_demands.items()
        for pair in choices
    }
    pair_universe.update(fixed_load)
    capacities = {
        pair: max(Fraction(), 1 - fixed_load.get(pair, Fraction()))
        for pair in pair_universe
    }

    flow_value, allocation = maximum_fractional_assignment(
        flexible_demands,
        capacities,
    )
    total_flexible = sum((row[0] for row in flexible_demands.values()), Fraction())
    unallocated_ratio = total_flexible - flow_value

    fixed_excess_mass = sum(
        (
            Fraction(parent_base, resource[1] - resource[0]) * ratio
            for resource, ratio in fixed_excess.items()
        ),
        Fraction(),
    )
    unallocated_mass = sum(
        (
            Fraction(parent_base, resource[1] - resource[0])
            * (amount - sum(allocation.get(resource, {}).values(), Fraction()))
            for resource, (amount, _choices) in flexible_demands.items()
        ),
        Fraction(),
    )

    recursive_current_excess = Fraction()
    terminal_current_excess = Fraction()
    for resource, rows in owners.items():
        current = [row for row in rows if row["kind"] == "current"]
        latent = [row for row in rows if row["kind"] == "latent"]
        if not current or not latent:
            continue
        total = sum((Fraction(row["ratio"]) for row in rows), Fraction())
        excess = max(Fraction(), total - 1)
        weighted = Fraction(parent_base, resource[1] - resource[0]) * excess
        if bool(current[0]["terminal"]):
            terminal_current_excess += weighted
        else:
            recursive_current_excess += weighted

    demand_rows = []
    for resource, (amount, choices) in sorted(flexible_demands.items()):
        assigned = sum(allocation.get(resource, {}).values(), Fraction())
        demand_rows.append(
            {
                "resource": resource,
                "ratio": str(amount),
                "assigned_ratio": str(assigned),
                "unassigned_ratio": str(amount - assigned),
                "choices": choices,
                "allocation": [
                    {"pair": pair, "ratio": str(value)}
                    for pair, value in sorted(allocation.get(resource, {}).items())
                ],
                **demand_meta[resource],
            }
        )

    return {
        "name": name,
        "parent": parent,
        "parent_base": parent_base,
        "counts": {
            "retained_states": len(retained),
            "owner_resources": len(owners),
            "fixed_resources": len(fixed_load),
            "flexible_middle_latent_demands": len(flexible_demands),
            "fixed_excess_resources": len(fixed_excess),
            "capacity_pairs": len(capacities),
            "current_latent_resources": sum(
                any(row["kind"] == "current" for row in rows)
                and any(row["kind"] == "latent" for row in rows)
                for rows in owners.values()
            ),
            "latent_latent_resources": sum(
                sum(row["kind"] == "latent" for row in rows) == 2
                for rows in owners.values()
            ),
        },
        "ratios": {
            "total_flexible_demand": str(total_flexible),
            "assigned_flexible_demand": str(flow_value),
            "unallocated_flexible_demand": str(unallocated_ratio),
            "maximum_fixed_load": str(max(fixed_load.values(), default=Fraction())),
            "minimum_pair_capacity": str(min(capacities.values(), default=Fraction())),
        },
        "masses": {
            "fixed_excess": str(fixed_excess_mass),
            "unallocated_flexible": str(unallocated_mass),
            "total_critical_residual": str(fixed_excess_mass + unallocated_mass),
            "terminal_current_excess": str(terminal_current_excess),
            "recursive_current_excess": str(recursive_current_excess),
        },
        "fixed_excess": [
            {"resource": resource, "ratio": str(value)}
            for resource, value in sorted(fixed_excess.items())
        ],
        "demands": demand_rows,
        "checks": {
            "all_middle_latent_occurrences_are_jointly_assigned": True,
            "duplicated_latent_owners_share_one_flexible_demand": True,
            "natural_center_opposite_choices_preserve_gap": True,
            "fixed_current_and_nonmiddle_loads_reserved_before_flow": True,
            "all_flexible_demands_assigned": unallocated_ratio == 0,
        },
    }


def shifted(values: tuple[int, ...], delta: int) -> tuple[int, ...]:
    return tuple(value + delta for value in values)


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_critical_fractional_reserve_flow.py OUTPUT")

    clean = shifted((1, 4, 5, 6, 20, 21, 22, 26, 27, 28, 32, 33, 34), 64)
    current_no_go = (
        65,
        97,
        98,
        99,
        113,
        114,
        115,
        119,
        120,
        121,
        125,
        126,
        127,
    )
    rank_two_raw = (
        1,
        9194,
        9200,
        9206,
        10595,
        10600,
        10605,
        11296,
        11300,
        11304,
        11599,
        11600,
        11601,
        11996,
        11997,
        11999,
        12000,
        12001,
        12004,
        12005,
        12006,
        12012,
        12046,
        12047,
        12049,
        12050,
        12051,
        12054,
        12055,
        12056,
        12062,
        12096,
        12097,
        12099,
        12100,
        12101,
        12104,
        12105,
        12106,
        12112,
    )
    rank_two = shifted(rank_two_raw, 16384)

    profiles = [
        profile("clean_latent_reuse", clean),
        profile("recursive_current_latent_no_go", current_no_go),
        profile("rank_two_raw_reserve_no_go", rank_two),
    ]
    checks = {
        "clean_profile_closes_jointly": (
            profiles[0]["ratios"]["unallocated_flexible_demand"] == "0"
            and profiles[0]["masses"]["fixed_excess"] == "0"
        ),
        "recursive_current_no_go_retains_fixed_excess": (
            Fraction(profiles[1]["masses"]["fixed_excess"]) > 0
        ),
        "rank_two_raw_no_go_closes_jointly": (
            profiles[2]["ratios"]["unallocated_flexible_demand"] == "0"
        ),
    }
    if not checks["clean_profile_closes_jointly"]:
        raise AssertionError("clean critical assignment changed")
    if not checks["recursive_current_no_go_retains_fixed_excess"]:
        raise AssertionError("sharp recursive current excess disappeared")

    output = {
        "schema": "critical_joint_fractional_assignment_v3",
        "profiles": profiles,
        "checks": checks,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[1]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
