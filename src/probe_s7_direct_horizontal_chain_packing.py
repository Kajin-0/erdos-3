#!/usr/bin/env python3
"""Profile physical horizontal-chain pair packing after direct S7 discharge."""
from __future__ import annotations

from collections import Counter, defaultdict
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


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate horizontal chain pair")
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


def pair_union_mass(pairs: set[Pair]) -> Fraction:
    return sum((pair_weight(pair) for pair in pairs), Fraction())


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_horizontal_chain_packing.py "
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

    light_supports: set[Pair] = set()
    recursive_states: list[tuple[int, str, Fraction, int, tuple[int, ...]]] = []
    terminal_shells = 0
    recursive_mass = Fraction()

    for support, roles in sorted(roles_by_support.items()):
        multiplicity = len(roles)
        threshold = (
            Fraction()
            if support in activated
            else pair_weight(support) / multiplicity
        )
        for completion, role, coefficient in sorted(roles):
            steps = groups[(support, completion, role, coefficient)]
            load = coefficient * harmonic(steps)
            if load <= threshold:
                light_supports.add(support)
                continue
            shells: dict[int, set[int]] = defaultdict(set)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].add(step)
            for shell_base, shell_steps in sorted(shells.items()):
                state = tuple(sorted(shell_steps))
                if not contains_three_term_ap(state):
                    terminal_shells += 1
                    continue
                recursive_states.append(
                    (completion, role, coefficient, shell_base, state)
                )
                recursive_mass += coefficient * harmonic(state)

    if len(recursive_states) != 278:
        raise AssertionError("recursive direct heavy frontier changed")
    if terminal_shells != 23_638:
        raise AssertionError("terminal direct heavy frontier changed")
    if light_supports & activated:
        raise AssertionError("light supports overlap entering pair reserve")

    reserve = activated | light_supports
    chain_occurrences: list[
        tuple[Pair, Fraction, int, int, str, tuple[int, ...]]
    ] = []
    state_chain_surpluses: list[Fraction] = []

    for completion, role, coefficient, shell_base, state in recursive_states:
        chain = physical_chain(completion, role, state)
        if len(chain) != len(state) - 1:
            raise AssertionError("horizontal chain length mismatch")
        chain_load = Fraction()
        for pair in chain:
            if not set(pair) <= s7:
                raise AssertionError("horizontal chain pair left S7")
            gap = pair[1] - pair[0]
            if gap >= shell_base:
                raise AssertionError("horizontal chain failed strict gap descent")
            usage = coefficient * pair_weight(pair)
            chain_load += usage
            chain_occurrences.append(
                (pair, usage, shell_base, completion, role, state)
            )
        debt = coefficient * harmonic(state)
        surplus = chain_load - debt
        if surplus <= 0:
            raise AssertionError("horizontal chain failed to dominate recursive debt")
        state_chain_surpluses.append(surplus)

    usage_by_pair: dict[Pair, Fraction] = defaultdict(Fraction)
    occurrence_count_by_pair = Counter()
    origins_by_pair: dict[Pair, set[tuple[int, str, int, tuple[int, ...]]]] = defaultdict(set)
    gap_shell_profile = Counter()
    for pair, usage, shell_base, completion, role, state in chain_occurrences:
        usage_by_pair[pair] += usage
        occurrence_count_by_pair[pair] += 1
        origins_by_pair[pair].add((completion, role, shell_base, state))
        gap = pair[1] - pair[0]
        gap_shell = 1 << (gap.bit_length() - 1)
        gap_shell_profile[gap_shell] += 1

    if any(len(origins) != count for pair, origins in origins_by_pair.items()
           for count in [occurrence_count_by_pair[pair]]):
        raise AssertionError("one embedded chain origin repeated a physical pair")

    new_pairs: set[Pair] = set()
    reserved_overlap_pairs: set[Pair] = set()
    first_use_consumed = Fraction()
    recurrence_reserved = Fraction()
    recurrence_duplicate = Fraction()
    capacity_slack = Fraction()
    maximum_usage_ratio = Fraction()

    usage_ratio_profile = Counter()
    multiplicity_profile = Counter(occurrence_count_by_pair.values())

    for pair, usage in usage_by_pair.items():
        capacity = pair_weight(pair)
        ratio = usage / capacity
        maximum_usage_ratio = max(maximum_usage_ratio, ratio)
        usage_ratio_profile[str(ratio)] += 1
        if pair in reserve:
            reserved_overlap_pairs.add(pair)
            recurrence_reserved += usage
            continue
        new_pairs.add(pair)
        consumed = min(usage, capacity)
        excess = max(usage - capacity, Fraction())
        first_use_consumed += consumed
        recurrence_duplicate += excess
        capacity_slack += capacity - consumed

    occurrence_usage = sum(usage_by_pair.values(), Fraction())
    new_union_capacity = pair_union_mass(new_pairs)
    reserved_overlap_capacity = pair_union_mass(reserved_overlap_pairs)
    recurrence_mass = recurrence_reserved + recurrence_duplicate

    if occurrence_usage != first_use_consumed + recurrence_mass:
        raise AssertionError("chain first-use/recurrence identity failed")
    if new_union_capacity != first_use_consumed + capacity_slack:
        raise AssertionError("chain new-capacity partition failed")
    if occurrence_usage <= recursive_mass:
        raise AssertionError("aggregate horizontal chain does not dominate debt")
    if new_pairs & reserve:
        raise AssertionError("new chain union overlaps reserved pair ledger")

    output = {
        "schema": "s7_direct_horizontal_chain_packing_v1",
        "scope": "physical adjacent-chain pairs from recursive direct-discharge shells",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_state_occurrences": len(recursive_states),
            "chain_pair_occurrences": len(chain_occurrences),
            "distinct_chain_pairs": len(usage_by_pair),
            "new_chain_pairs": len(new_pairs),
            "reserved_overlap_pairs": len(reserved_overlap_pairs),
            "repeated_chain_pairs": sum(
                count > 1 for count in occurrence_count_by_pair.values()
            ),
            "maximum_chain_pair_multiplicity": max(occurrence_count_by_pair.values()),
            "maximum_weighted_usage_ratio_numerator": maximum_usage_ratio.numerator,
            "maximum_weighted_usage_ratio_denominator": maximum_usage_ratio.denominator,
        },
        "masses": {
            "recursive_heavy_debt": serialize_mass(recursive_mass),
            "chain_occurrence_usage": serialize_mass(occurrence_usage),
            "chain_occurrence_surplus": serialize_mass(occurrence_usage - recursive_mass),
            "new_chain_pair_union_capacity": serialize_mass(new_union_capacity),
            "first_use_consumed_capacity": serialize_mass(first_use_consumed),
            "new_chain_capacity_slack": serialize_mass(capacity_slack),
            "reserved_overlap_pair_capacity": serialize_mass(reserved_overlap_capacity),
            "reserved_overlap_recurrence": serialize_mass(recurrence_reserved),
            "duplicate_new_pair_recurrence": serialize_mass(recurrence_duplicate),
            "total_chain_recurrence": serialize_mass(recurrence_mass),
            "minimum_state_chain_surplus": serialize_mass(min(state_chain_surpluses)),
        },
        "profiles": {
            "pair_multiplicity": [
                {"multiplicity": value, "pairs": multiplicity_profile[value]}
                for value in sorted(multiplicity_profile)
            ],
            "weighted_usage_ratio": [
                {"ratio": value, "pairs": usage_ratio_profile[value]}
                for value in sorted(
                    usage_ratio_profile, key=lambda text: Fraction(text)
                )
            ],
            "gap_shell": [
                {"shell_base": value, "occurrences": gap_shell_profile[value]}
                for value in sorted(gap_shell_profile)
            ],
        },
        "hashes": {
            "chain_occurrences": hashlib.sha256(
                json.dumps(
                    [
                        (
                            pair,
                            str(usage),
                            shell_base,
                            completion,
                            role,
                            state,
                        )
                        for pair, usage, shell_base, completion, role, state
                        in chain_occurrences
                    ],
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest(),
            "new_chain_pairs": hashlib.sha256(
                json.dumps(sorted(new_pairs), separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "strict_gap_descent": True,
            "statewise_chain_domination": min(state_chain_surpluses) > 0,
            "chain_first_use_recurrence_identity": (
                occurrence_usage == first_use_consumed + recurrence_mass
            ),
            "new_chain_disjoint_from_reserved": not (new_pairs & reserve),
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
