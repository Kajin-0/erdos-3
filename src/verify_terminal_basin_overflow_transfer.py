#!/usr/bin/env python3
"""Exhaustively verify terminal-basin overflow transfer on [1,14]."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from verify_full_edge_coordinated_branching import contains_four_ap, pair_weight, valuation

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 14
INF = 10**9
Pair = tuple[int, int]


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def fraction_record(value: Fraction) -> dict[str, str]:
    text = f"{value.numerator}/{value.denominator}"
    return {
        "fraction": text,
        "decimal": f"{float(value):.12f}",
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def three_aps(values: set[int]) -> list[tuple[int, int]]:
    rows = []
    for left in sorted(values):
        for middle in sorted(value for value in values if value > left):
            step = middle - left
            if middle + step in values:
                rows.append((left, step))
    return rows


def deletion_schedule(initial: frozenset[int]) -> tuple[dict[int, int], dict[int, tuple[int, int]], frozenset[int], list[dict[str, object]]]:
    current = set(initial)
    rank: dict[int, int] = {}
    action: dict[int, tuple[int, int]] = {}
    rows = []
    while True:
        aps = three_aps(current)
        if not aps:
            break
        left, step = min(aps, key=lambda row: (row[1], row[0]))
        points = (left, left + step, left + 2 * step)
        if valuation(step, 2) % 2 == 0:
            sponsor = points[0]
            middle = points[1]
            opposite = points[2]
            orientation = "left"
        else:
            sponsor = points[2]
            middle = points[1]
            opposite = points[0]
            orientation = "right"
        index = len(rows)
        rank[sponsor] = index
        action[sponsor] = (middle, opposite)
        rows.append(
            {
                "index": index,
                "sponsor": sponsor,
                "middle": middle,
                "opposite": opposite,
                "step": step,
                "orientation": orientation,
            }
        )
        current.remove(sponsor)
    residual = frozenset(current)
    if three_aps(set(residual)):
        raise AssertionError("deletion schedule did not terminate")
    return rank, action, residual, rows


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("pair endpoints coincide")
    return (left, right) if left < right else (right, left)


def terminal_map(
    pair: Pair,
    rank: dict[int, int],
    action: dict[int, tuple[int, int]],
) -> tuple[Pair, str, int, tuple[Pair, ...]]:
    current = pair
    path = [current]
    transports = 0
    while True:
        left, right = current
        left_rank = rank.get(left, INF)
        right_rank = rank.get(right, INF)
        if left_rank == INF and right_rank == INF:
            return current, "residual", transports, tuple(path)
        if left_rank == right_rank:
            raise AssertionError("distinct sponsors share deletion rank")
        if left_rank < right_rank:
            sponsor, other = left, right
        else:
            sponsor, other = right, left
        middle, opposite = action[sponsor]
        if other == middle or other == opposite:
            return current, "direct", transports, tuple(path)
        if abs(other - middle) <= abs(other - sponsor):
            next_pair = ordered_pair(middle, other)
            old_owner_rank = min(left_rank, right_rank)
            new_owner_rank = min(rank.get(next_pair[0], INF), rank.get(next_pair[1], INF))
            if not new_owner_rank > old_owner_rank:
                raise AssertionError("transport rank did not increase")
            if pair_weight(next_pair) < pair_weight(current):
                raise AssertionError("transport pair weight decreased")
            current = next_pair
            path.append(current)
            transports += 1
            if transports > len(rank):
                raise AssertionError("transport did not terminate")
            continue
        return current, "backward", transports, tuple(path)


def next_power_two_strict(value: int) -> int:
    if value < 1:
        return 1
    return 1 << value.bit_length()


def pair_mass(pairs: set[Pair] | frozenset[Pair]) -> Fraction:
    return sum((pair_weight(pair) for pair in pairs), Fraction())


def verify_family(
    initial: frozenset[int],
    family_name: str,
    activated: frozenset[Pair],
    rank: dict[int, int],
    action: dict[int, tuple[int, int]],
    residual: frozenset[int],
) -> dict[str, object]:
    if len(activated) != len(set(activated)):
        raise AssertionError("activated pair family is not distinct")
    terminal_rows = {
        pair: terminal_map(pair, rank, action)
        for pair in activated
    }
    basins: dict[Pair, list[Pair]] = defaultdict(list)
    terminal_type: dict[Pair, str] = {}
    maximum_path = 0
    for pair, (target, kind, transports, _path) in terminal_rows.items():
        basins[target].append(pair)
        terminal_type[target] = kind
        maximum_path = max(maximum_path, transports)

    representatives: set[Pair] = set()
    for target, members in basins.items():
        representative = target if target in activated else min(members)
        representatives.add(representative)
    if len(representatives) != len(basins):
        raise AssertionError("one representative per basin failed")
    overflow = set(activated) - representatives

    target_set = set(basins)
    representative_mass = pair_mass(representatives)
    target_mass = pair_mass(target_set)
    if representative_mass > target_mass:
        raise AssertionError("representative terminal transport failed")

    fibers: dict[tuple[int, str], set[int]] = defaultdict(set)
    overflow_owner_rows = []
    for pair in sorted(overflow):
        left, right = pair
        left_rank = rank.get(left, INF)
        right_rank = rank.get(right, INF)
        if left_rank == INF and right_rank == INF:
            raise AssertionError("residual-residual pair entered overflow")
        owner = left if left_rank < right_rank else right
        other = right if owner == left else left
        side = "right" if other > owner else "left"
        distance = abs(other - owner)
        key = (owner, side)
        if distance in fibers[key]:
            raise AssertionError("duplicate owner-distance token")
        fibers[key].add(distance)
        overflow_owner_rows.append(
            {
                "pair": list(pair),
                "owner": owner,
                "side": side,
                "distance": distance,
                "terminal": list(terminal_rows[pair][0]),
            }
        )

    diameter = max(initial) - min(initial) if len(initial) > 1 else 0
    shell_base = next_power_two_strict(diameter)
    fiber_mass = Fraction()
    shell_count = 0
    for (owner, side), distances in fibers.items():
        if contains_four_ap(frozenset(distances)):
            raise AssertionError("owner-distance fiber contains a four-AP")
        counterpart = {
            owner + distance if side == "right" else owner - distance
            for distance in distances
        }
        if not counterpart <= initial:
            raise AssertionError("owner-distance fiber escaped root set")
        if any(not 0 < distance < shell_base for distance in distances):
            raise AssertionError("owner-distance fiber failed scale descent")
        fiber_mass += sum((Fraction(1, distance) for distance in distances), Fraction())
        shell_count += len({distance.bit_length() - 1 for distance in distances})

    overflow_mass = pair_mass(overflow)
    if overflow_mass != fiber_mass:
        raise AssertionError("overflow fiber mass identity failed")
    activated_mass = pair_mass(set(activated))
    if activated_mass != representative_mass + overflow_mass:
        raise AssertionError("activated representative/overflow identity failed")
    rhs = target_mass + fiber_mass
    if activated_mass > rhs:
        raise AssertionError("terminal-basin overflow row failed")

    target_counts = Counter(terminal_type.values())
    return {
        "family": family_name,
        "activated_pairs": len(activated),
        "terminal_basins": len(basins),
        "representatives": len(representatives),
        "overflow_pairs": len(overflow),
        "owner_distance_fibers": len(fibers),
        "owner_distance_shells": shell_count,
        "direct_targets": target_counts["direct"],
        "backward_targets": target_counts["backward"],
        "residual_targets": target_counts["residual"],
        "maximum_transport_path": maximum_path,
        "activated_mass": fraction_record(activated_mass),
        "representative_mass": fraction_record(representative_mass),
        "terminal_target_mass": fraction_record(target_mass),
        "overflow_mass": fraction_record(overflow_mass),
        "row_rhs": fraction_record(rhs),
        "row_surplus": fraction_record(rhs - activated_mass),
        "overflow_rows_sha256": canonical_hash(overflow_owner_rows),
    }


def selected_edge_family(schedule: list[dict[str, object]]) -> frozenset[Pair]:
    pairs = set()
    for row in schedule:
        sponsor = int(row["sponsor"])
        middle = int(row["middle"])
        opposite = int(row["opposite"])
        pairs.add(ordered_pair(sponsor, middle))
        pairs.add(ordered_pair(sponsor, opposite))
        pairs.add(ordered_pair(middle, opposite))
    return frozenset(pairs)


def main() -> int:
    metrics = Counter()
    records_hash = hashlib.sha256()
    aggregate = defaultdict(Fraction)
    maximum_overflow = None
    maximum_path = None

    for mask in range(1 << LIMIT):
        initial = frozenset(index + 1 for index in range(LIMIT) if mask & (1 << index))
        if len(initial) < 2 or contains_four_ap(initial):
            continue
        rank, action, residual, schedule = deletion_schedule(initial)
        families = {
            "all_pairs": frozenset(combinations(sorted(initial), 2)),
            "selected_edges": selected_edge_family(schedule),
        }
        family_rows = []
        for name, activated in families.items():
            row = verify_family(initial, name, activated, rank, action, residual)
            family_rows.append(row)
            metrics[f"{name}_families"] += 1
            for field in (
                "activated_pairs",
                "terminal_basins",
                "overflow_pairs",
                "owner_distance_fibers",
                "owner_distance_shells",
                "direct_targets",
                "backward_targets",
                "residual_targets",
            ):
                metrics[f"{name}_{field}"] += int(row[field])
            aggregate[f"{name}_activated_mass"] += Fraction(row["activated_mass"]["fraction"])
            aggregate[f"{name}_terminal_mass"] += Fraction(row["terminal_target_mass"]["fraction"])
            aggregate[f"{name}_overflow_mass"] += Fraction(row["overflow_mass"]["fraction"])
            aggregate[f"{name}_surplus"] += Fraction(row["row_surplus"]["fraction"])
            if maximum_overflow is None or row["overflow_pairs"] > maximum_overflow["overflow_pairs"]:
                maximum_overflow = {"initial": sorted(initial), **row}
            if maximum_path is None or row["maximum_transport_path"] > maximum_path["maximum_transport_path"]:
                maximum_path = {"initial": sorted(initial), **row}
        record = {
            "initial": sorted(initial),
            "actions": len(schedule),
            "residual": sorted(residual),
            "families": family_rows,
        }
        records_hash.update(
            (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        )
        metrics["root_sets"] += 1
        metrics["actions"] += len(schedule)

    output = {
        "schema": "terminal_basin_overflow_transfer_certificate_v1",
        "interval": [1, LIMIT],
        "metrics": dict(metrics),
        "aggregate_masses": {
            name: fraction_record(value) for name, value in sorted(aggregate.items())
        },
        "maximum_overflow_witness": maximum_overflow,
        "maximum_transport_path_witness": maximum_path,
        "verified": {
            "deterministic_transport_terminates": True,
            "transport_weight_nondecreasing": True,
            "one_representative_per_terminal_basin": True,
            "terminal_targets_distinct": True,
            "all_overflow_pairs_have_sponsor_owner": True,
            "all_owner_distance_fibers_four_ap_free": True,
            "overflow_mass_equals_fiber_mass": True,
            "terminal_basin_overflow_row": True,
        },
        "records_sha256": records_hash.hexdigest(),
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
