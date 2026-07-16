#!/usr/bin/env python3
"""Deterministic maximum matching for reserve-demand incidence graphs."""
from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

Demand = TypeVar("Demand", bound=Hashable)
Reserve = TypeVar("Reserve", bound=Hashable)


def maximum_incidence_matching(
    neighbors: Mapping[Demand, Iterable[Reserve]],
) -> tuple[dict[Demand, Reserve], tuple[Demand, ...]]:
    """Match as many demands as possible to distinct incident reserves.

    The implementation is the standard augmenting-path algorithm for bipartite
    matching.  Iteration is canonical under ``repr`` so exact certificates are
    reproducible for tuple-valued pair identities.
    """

    normalized = {
        demand: tuple(sorted(set(reserves), key=repr))
        for demand, reserves in neighbors.items()
    }
    reserve_owner: dict[Reserve, Demand] = {}
    demand_reserve: dict[Demand, Reserve] = {}

    def augment(demand: Demand, seen: set[Reserve]) -> bool:
        for reserve in normalized[demand]:
            if reserve in seen:
                continue
            seen.add(reserve)
            owner = reserve_owner.get(reserve)
            if owner is None or augment(owner, seen):
                reserve_owner[reserve] = demand
                demand_reserve[demand] = reserve
                if owner is not None and owner != demand:
                    demand_reserve.pop(owner, None)
                return True
        return False

    for demand in sorted(normalized, key=repr):
        augment(demand, set())

    unmatched = tuple(
        demand
        for demand in sorted(normalized, key=repr)
        if demand not in demand_reserve
    )
    return demand_reserve, unmatched
