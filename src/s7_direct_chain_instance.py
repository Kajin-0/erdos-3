#!/usr/bin/env python3
"""Build the exact direct-discharge recursive horizontal-chain instance on S7."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json

from probe_s7_direct_pair_discharge import completion_candidates, harmonic
from probe_s7_hole_support_closure import build_s7, canonical_pair, read_full_hole_map
from probe_sponsor_pair_transport_frontier import pair_weight
from verify_retained_terminal_split import contains_three_term_ap


Pair = tuple[int, int]


@dataclass(frozen=True)
class RecursiveChainState:
    completion: int
    role: str
    coefficient: Fraction
    shell_base: int
    state: tuple[int, ...]
    debt: Fraction
    chain: tuple[Pair, ...]


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


def build_instance(
    payment_path: Path, hole_map_path: Path
) -> dict[str, object]:
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    if not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks source rows")

    s7 = build_s7()
    holes = read_full_hole_map(hole_map_path)
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
    recursive_states: list[RecursiveChainState] = []
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
                if chain_capacity <= debt:
                    raise AssertionError("horizontal chain does not dominate debt")
                recursive_states.append(
                    RecursiveChainState(
                        completion=completion,
                        role=role,
                        coefficient=coefficient,
                        shell_base=shell_base,
                        state=state,
                        debt=debt,
                        chain=chain,
                    )
                )

    if len(recursive_states) != 278:
        raise AssertionError("recursive direct heavy frontier changed")
    if terminal_shells != 23_638:
        raise AssertionError("terminal direct heavy frontier changed")
    if set(light_usage) & activated:
        raise AssertionError("light support usage overlaps activated pair debt")
    for pair, usage in light_usage.items():
        if usage > pair_weight(pair):
            raise AssertionError("light support usage exceeds pair capacity")

    return {
        "s7": s7,
        "activated": activated,
        "light_usage": dict(light_usage),
        "recursive_states": tuple(recursive_states),
        "terminal_shells": terminal_shells,
    }
