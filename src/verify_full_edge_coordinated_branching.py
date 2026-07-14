#!/usr/bin/env python3
"""Exhaustively verify full-edge coordinated branching.

For every four-AP-free subset of [1,12], attach three scale-descending child
occurrences to each three-AP:

1. the parity-selected side token d;
2. the uniquely colored middle token d;
3. the doubled side token 2d.

The three occurrences are identified with the three physical pair edges of the
progression.  Verify:

- exactly three memberships per progression;
- every child is four-AP-free;
- the first three dilates of every child are pairwise disjoint;
- child occurrence mass equals (5/2) times weighted three-AP load;
- pair-edge occurrence mass equals child occurrence mass;
- every physical pair has multiplicity at most two;
- pair-union mass is at least half occurrence mass.

A second exhaustive pass over dyadic blocks [N,2N), N=2,4,8, verifies strict
scale descent for all three child types.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 12
DYADIC_BASES = (2, 4, 8)

Pair = tuple[int, int]
ChildKey = tuple[str, int, int | None]


def valuation(value: int, prime: int) -> int:
    if value <= 0:
        raise ValueError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate pair")
    return (left, right) if left < right else (right, left)


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def contains_four_ap(values: frozenset[int] | set[int]) -> bool:
    ordered = sorted(values)
    present = set(ordered)
    if not ordered:
        return False
    for left in ordered:
        for step in range(1, (ordered[-1] - left) // 3 + 1):
            if (
                left + step in present
                and left + 2 * step in present
                and left + 3 * step in present
            ):
                return True
    return False


def three_aps(
    values: frozenset[int] | set[int],
) -> tuple[tuple[int, int, int, int], ...]:
    ordered = sorted(values)
    present = set(ordered)
    rows: list[tuple[int, int, int, int]] = []
    for left in ordered:
        for middle in ordered:
            if middle <= left:
                continue
            step = middle - left
            right = middle + step
            if right in present:
                rows.append((left, middle, right, step))
    return tuple(rows)


def harmonic(values: frozenset[int] | set[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def verify_child(key: ChildKey, tokens: frozenset[int]) -> None:
    if not tokens:
        raise AssertionError(f"empty child {key}")
    if contains_four_ap(tokens):
        raise AssertionError(f"child {key} contains a four-AP: {sorted(tokens)}")
    first = set(tokens)
    second = {2 * token for token in tokens}
    third = {3 * token for token in tokens}
    if first & second:
        raise AssertionError(f"child {key} has C/2C overlap")
    if first & third:
        raise AssertionError(f"child {key} has C/3C overlap")
    if second & third:
        raise AssertionError(f"child {key} has 2C/3C overlap")


def full_edge_family(values: frozenset[int]) -> tuple[
    dict[ChildKey, frozenset[int]],
    list[dict[str, object]],
]:
    children: dict[ChildKey, set[int]] = defaultdict(set)
    occurrence_by_child_token: dict[tuple[ChildKey, int], dict[str, object]] = {}
    occurrences: list[dict[str, object]] = []

    for left, middle, right, step in three_aps(values):
        color = (valuation(step, 2) - valuation(step, 3)) % 3
        middle_key: ChildKey = ("middle", middle, color)

        if valuation(step, 2) % 2 == 0:
            side_key: ChildKey = ("side_first", left, None)
            doubled_key: ChildKey = ("double_first", left, None)
            side_pair = ordered_pair(left, middle)
            middle_pair = ordered_pair(middle, right)
        else:
            side_key = ("side_last", right, None)
            doubled_key = ("double_last", right, None)
            side_pair = ordered_pair(middle, right)
            middle_pair = ordered_pair(left, middle)

        rows = (
            (side_key, step, side_pair, "side_adjacent"),
            (middle_key, step, middle_pair, "middle_adjacent"),
            (doubled_key, 2 * step, ordered_pair(left, right), "side_outer"),
        )
        for child_key, token, pair, role in rows:
            if pair_weight(pair) != Fraction(1, token):
                raise AssertionError(
                    f"pair/token weight mismatch for {pair}, token {token}"
                )
            identity = (child_key, token)
            record = {
                "progression": (left, middle, right, step),
                "child_key": child_key,
                "token": token,
                "pair": pair,
                "role": role,
            }
            if identity in occurrence_by_child_token:
                previous = occurrence_by_child_token[identity]
                raise AssertionError(
                    f"duplicate child token {identity}: {previous} versus {record}"
                )
            occurrence_by_child_token[identity] = record
            children[child_key].add(token)
            occurrences.append(record)

    return (
        {key: frozenset(tokens) for key, tokens in children.items()},
        occurrences,
    )


def subset_record(values: frozenset[int]) -> dict[str, object]:
    aps = three_aps(values)
    children, occurrences = full_edge_family(values)

    if len(occurrences) != 3 * len(aps):
        raise AssertionError("not exactly three memberships per progression")

    progression_counts = Counter(tuple(row["progression"]) for row in occurrences)
    if set(progression_counts) != set(aps):
        raise AssertionError("progression occurrence domain mismatch")
    if any(count != 3 for count in progression_counts.values()):
        raise AssertionError("progression membership multiplicity is not three")

    role_counts_by_progression: dict[tuple[int, int, int, int], Counter[str]] = (
        defaultdict(Counter)
    )
    for row in occurrences:
        role_counts_by_progression[tuple(row["progression"])][str(row["role"])] += 1
    expected_roles = Counter(
        {"side_adjacent": 1, "middle_adjacent": 1, "side_outer": 1}
    )
    if any(counts != expected_roles for counts in role_counts_by_progression.values()):
        raise AssertionError("progression role profile changed")

    for key, tokens in children.items():
        verify_child(key, tokens)

    load = sum((Fraction(1, row[3]) for row in aps), Fraction())
    child_occurrence_mass = sum(
        (Fraction(1, int(row["token"])) for row in occurrences), Fraction()
    )
    child_set_mass = sum((harmonic(tokens) for tokens in children.values()), Fraction())
    if child_occurrence_mass != child_set_mass:
        raise AssertionError("child occurrence/set mass mismatch")
    if child_occurrence_mass != Fraction(5, 2) * load:
        raise AssertionError(
            f"full-edge mass identity failed: {child_occurrence_mass} != 5/2*{load}"
        )

    pair_counts: Counter[Pair] = Counter(tuple(row["pair"]) for row in occurrences)
    pair_occurrence_mass = sum(
        (pair_weight(pair) * count for pair, count in pair_counts.items()),
        Fraction(),
    )
    pair_union_mass = sum((pair_weight(pair) for pair in pair_counts), Fraction())
    if pair_occurrence_mass != child_occurrence_mass:
        raise AssertionError("pair occurrence mass differs from child mass")
    maximum_pair_multiplicity = max(pair_counts.values(), default=0)
    if maximum_pair_multiplicity > 2:
        raise AssertionError(
            f"pair multiplicity exceeds two: {maximum_pair_multiplicity}"
        )
    if pair_union_mass * 2 < pair_occurrence_mass:
        raise AssertionError("pair-union half-occurrence bound failed")
    if pair_union_mass < Fraction(5, 4) * load:
        raise AssertionError("pair-union 5/4-load bound failed")

    repeated_pairs = sorted(
        (pair, count) for pair, count in pair_counts.items() if count > 1
    )
    return {
        "values": list(values),
        "three_aps": len(aps),
        "children": len(children),
        "child_occurrences": len(occurrences),
        "load": fraction_text(load),
        "child_occurrence_mass": fraction_text(child_occurrence_mass),
        "pair_union_mass": fraction_text(pair_union_mass),
        "maximum_pair_multiplicity": maximum_pair_multiplicity,
        "repeated_pairs": [[list(pair), count] for pair, count in repeated_pairs],
        "children_sha256": canonical_hash(
            [[list(key), sorted(tokens)] for key, tokens in sorted(children.items())]
        ),
        "pair_multiset_sha256": canonical_hash(
            [[list(pair), count] for pair, count in sorted(pair_counts.items())]
        ),
    }


def exhaustive_interval() -> tuple[list[dict[str, object]], dict[str, int]]:
    interval = tuple(range(1, LIMIT + 1))
    records: list[dict[str, object]] = []
    metrics = Counter()
    for mask in range(1 << LIMIT):
        values = frozenset(
            interval[index]
            for index in range(LIMIT)
            if mask & (1 << index)
        )
        if contains_four_ap(values):
            continue
        record = subset_record(values)
        records.append(record)
        metrics["four_ap_free_subsets"] += 1
        metrics["subsets_with_three_aps"] += int(record["three_aps"] > 0)
        metrics["three_ap_occurrences"] += int(record["three_aps"])
        metrics["child_occurrences"] += int(record["child_occurrences"])
        metrics["child_states"] += int(record["children"])
        metrics["repeated_physical_pairs"] += len(record["repeated_pairs"])
        metrics["maximum_three_aps"] = max(
            metrics["maximum_three_aps"], int(record["three_aps"])
        )
        metrics["maximum_child_states"] = max(
            metrics["maximum_child_states"], int(record["children"])
        )
        metrics["maximum_pair_multiplicity"] = max(
            metrics["maximum_pair_multiplicity"],
            int(record["maximum_pair_multiplicity"]),
        )
    return records, dict(metrics)


def verify_dyadic_scale_descent() -> dict[str, int]:
    metrics = Counter()
    for base in DYADIC_BASES:
        interval = tuple(range(base, 2 * base))
        for mask in range(1 << len(interval)):
            values = frozenset(
                interval[index]
                for index in range(len(interval))
                if mask & (1 << index)
            )
            if contains_four_ap(values):
                continue
            children, occurrences = full_edge_family(values)
            for row in occurrences:
                token = int(row["token"])
                if not token < base:
                    raise AssertionError(
                        f"scale descent failed in [{base},{2*base}): token={token}, "
                        f"row={row}, values={sorted(values)}"
                    )
            metrics["dyadic_four_ap_free_subsets"] += 1
            metrics["dyadic_three_ap_occurrences"] += len(three_aps(values))
            metrics["dyadic_child_occurrences"] += len(occurrences)
            metrics["dyadic_child_states"] += len(children)
    return dict(metrics)


def main() -> int:
    records, metrics = exhaustive_interval()
    dyadic_metrics = verify_dyadic_scale_descent()

    if metrics["four_ap_free_subsets"] != 2_233:
        raise AssertionError(
            f"[1,12] four-AP-free subset count changed: {metrics}"
        )
    if metrics["three_ap_occurrences"] != 3_174:
        raise AssertionError(f"[1,12] three-AP count changed: {metrics}")
    if metrics["child_occurrences"] != 3 * metrics["three_ap_occurrences"]:
        raise AssertionError("aggregate three-membership identity failed")
    if metrics["maximum_pair_multiplicity"] != 2:
        raise AssertionError("sharp pair multiplicity two was not observed")

    output = {
        "schema": "full_edge_coordinated_branching_exhaustive_v1",
        "interval": [1, LIMIT],
        "dyadic_bases": list(DYADIC_BASES),
        "metrics": metrics,
        "dyadic_metrics": dyadic_metrics,
        "verified": {
            "exact_three_memberships_per_progression": True,
            "all_children_four_ap_free": True,
            "all_children_have_disjoint_first_three_dilates": True,
            "strict_dyadic_scale_descent": True,
            "child_occurrence_mass_equals_five_halves_load": True,
            "pair_occurrence_mass_equals_child_occurrence_mass": True,
            "maximum_physical_pair_multiplicity_two": True,
            "pair_union_at_least_half_occurrence": True,
            "pair_union_at_least_five_fourths_load": True,
        },
        "records_sha256": canonical_hash(records),
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
