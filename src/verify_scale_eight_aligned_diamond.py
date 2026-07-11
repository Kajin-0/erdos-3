#!/usr/bin/env python3
"""Certify the scale-eight self-replicating aligned-diamond family.

The construction uses base 8. Let

    L_h = 8^(h+1),
    S_1 = 64 + {0,1,2,16,17,18,21,22,23,26,27,28}.

For h >= 1 put A_h = {0} union S_h and choose

    k_h = 6  if h is odd,
          1  if h is even,
    R_h = 2 L_h + k_h L_h / 8.

Then

    S_(h+1) = 8 L_h + (A_h union (A_h+R_h) union (A_h+2R_h)).

The script performs two exact checks:

1. It builds the finite LSD-first base-8 automaton for the union of all S_h and
   proves by a finite product/carry search that the language contains no
   nontrivial four-term arithmetic progression.
2. It checks the recursive shells explicitly through a configurable finite
   depth and verifies the cardinality and side-anchor orientation invariants.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict, deque
from collections.abc import Iterable
from dataclasses import dataclass
from typing import DefaultDict

BASE = 8
H = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
BASE_PAIRS = {(value % BASE, value // BASE) for value in H}
TYPES = {"A": 6, "B": 1}
OPPOSITE = {"A": "B", "B": "A"}

NFAState = str
DFAState = int
Digit = int
NFA = dict[NFAState, dict[Digit, set[NFAState]]]
DFA = dict[DFAState, dict[Digit, DFAState]]


@dataclass(frozen=True)
class Certificate:
    dfa_states: int
    accepting_states: int
    product_states: int
    signature: str


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is defined here only for positive integers")
    return (value & -value).bit_length() - 1


def first_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    ordered = sorted(set(values))
    values_set = set(ordered)
    for i, first in enumerate(ordered):
        for last in ordered[i + 3 :]:
            span = last - first
            if span % 3:
                continue
            step = span // 3
            if first + step in values_set and first + 2 * step in values_set:
                return first, step
    return None


def layer_type(h: int) -> str:
    return "A" if h % 2 else "B"


def separation(h: int, scale: int) -> int:
    k = TYPES[layer_type(h)]
    return 2 * scale + k * (scale // BASE)


def next_state(h: int, scale: int, state: set[int]) -> tuple[int, set[int]]:
    anchor_set = {0} | state
    step = separation(h, scale)
    raw = (
        anchor_set
        | {value + step for value in anchor_set}
        | {value + 2 * step for value in anchor_set}
    )
    return BASE * scale, {BASE * scale + value for value in raw}


def transform_terminal(terminal: int, type_name: str, choice: int) -> tuple[int, int]:
    coefficient = 16 + TYPES[type_name]
    high, low = divmod(choice * coefficient, BASE)
    carry, new_low = divmod(terminal + low, BASE)
    new_high = 1 + high + carry
    if not (0 <= new_low < BASE and 0 <= new_high < BASE):
        raise AssertionError("digit transform left the base-8 alphabet")
    return new_low, new_high


def add_transition(
    transitions: DefaultDict[NFAState, DefaultDict[Digit, set[NFAState]]],
    source: NFAState,
    digit: Digit,
    target: NFAState,
) -> None:
    transitions[source][digit].add(target)


def build_nfa() -> tuple[NFA, NFAState, NFAState]:
    transitions: DefaultDict[NFAState, DefaultDict[Digit, set[NFAState]]] = defaultdict(
        lambda: defaultdict(set)
    )
    start = "start"
    accept = "accept"

    # Base state S_1. After the least-significant digit, the automaton stores
    # each possible terminal digit c of the word (low, c, 1).
    for low, terminal in sorted(BASE_PAIRS):
        add_transition(transitions, start, low, f"q:{terminal}:A")

    # A leaf created from a=0 has h low zeroes. The parity of h determines
    # whether the current outer step uses type A (k=6) or B (k=1).
    add_transition(transitions, start, 0, "zero:odd")
    add_transition(transitions, "zero:odd", 0, "zero:even")
    add_transition(transitions, "zero:even", 0, "zero:odd")

    for zero_state, type_name in (("zero:odd", "A"), ("zero:even", "B")):
        coefficient = 16 + TYPES[type_name]
        for choice in range(3):
            high, low = divmod(choice * coefficient, BASE)
            add_transition(
                transitions,
                zero_state,
                low,
                f"q:{high}:{OPPOSITE[type_name]}",
            )

    # q:c:t means that c is the current terminal digit and t is the type of
    # the next optional outer replication. Reading c terminates the chain;
    # reading a transformed digit applies one more outer layer.
    for terminal in range(BASE):
        for type_name in TYPES:
            source = f"q:{terminal}:{type_name}"
            add_transition(transitions, source, terminal, "expect-leading-one")
            for choice in range(3):
                low, high = transform_terminal(terminal, type_name, choice)
                add_transition(
                    transitions,
                    source,
                    low,
                    f"q:{high}:{OPPOSITE[type_name]}",
                )

    add_transition(transitions, "expect-leading-one", 1, accept)
    add_transition(transitions, accept, 0, accept)
    return {state: dict(row) for state, row in transitions.items()}, start, accept


def determinize(nfa: NFA, start: NFAState, accept: NFAState) -> tuple[DFA, set[int]]:
    start_subset = frozenset({start})
    ids = {start_subset: 0}
    queue = deque([start_subset])
    dfa: DFA = {}
    accepting: set[int] = set()

    while queue:
        subset = queue.popleft()
        state_id = ids[subset]
        if accept in subset:
            accepting.add(state_id)
        row: dict[int, int] = {}
        for digit in range(BASE):
            target = frozenset(
                next_state
                for nfa_state in subset
                for next_state in nfa.get(nfa_state, {}).get(digit, set())
            )
            if target not in ids:
                ids[target] = len(ids)
                queue.append(target)
            row[digit] = ids[target]
        dfa[state_id] = row

    return dfa, accepting


def dfa_signature(dfa: DFA, accepting: set[int]) -> str:
    payload = {
        "base": BASE,
        "states": [f"q{i}" for i in range(len(dfa))],
        "start": "q0",
        "accept": [f"q{i}" for i in sorted(accepting)],
        "transitions": {
            f"q{state}": {
                str(digit): f"q{dfa[state][digit]}" for digit in range(BASE)
            }
            for state in range(len(dfa))
        },
    }
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def accepts_integer(dfa: DFA, accepting: set[int], value: int) -> bool:
    if value < 0:
        return False
    state = 0
    current = value
    while current:
        state = dfa[state][current % BASE]
        current //= BASE
    for _ in range(len(dfa) + 1):
        if state in accepting:
            return True
        state = dfa[state][0]
    return False


def carry_closure() -> tuple[int, ...]:
    values = {
        a0 - 2 * a1 + a2
        for a0 in range(BASE)
        for a1 in range(BASE)
        for a2 in range(BASE)
    }
    carries = {0}
    changed = True
    while changed:
        changed = False
        for carry in tuple(carries):
            for value in values:
                total = value + carry
                if total % BASE:
                    continue
                next_carry = total // BASE
                if next_carry not in carries:
                    carries.add(next_carry)
                    changed = True
    return tuple(sorted(carries))


def digit_options(carry1: int, carry2: int, carries: tuple[int, ...]):
    for a1 in range(BASE):
        for a2 in range(BASE):
            for next1 in carries:
                a0 = BASE * next1 - carry1 + 2 * a1 - a2
                if not 0 <= a0 < BASE:
                    continue
                for next2 in carries:
                    a3 = BASE * next2 - carry2 - a1 + 2 * a2
                    if 0 <= a3 < BASE:
                        digits = (a0, a1, a2, a3)
                        yield digits, next1, next2, len(set(digits)) > 1


def certify_4ap_free(dfa: DFA, accepting: set[int]) -> int:
    carries = carry_closure()
    options = {
        (c1, c2): tuple(digit_options(c1, c2, carries))
        for c1 in carries
        for c2 in carries
    }

    start = (0, 0, 0, 0, 0, 0, False)
    queue = deque([start])
    seen = {start}

    while queue:
        q0, q1, q2, q3, carry1, carry2, nontrivial = queue.popleft()
        for digits, next1, next2, digit_nontrivial in options[(carry1, carry2)]:
            a0, a1, a2, a3 = digits
            target = (
                dfa[q0][a0],
                dfa[q1][a1],
                dfa[q2][a2],
                dfa[q3][a3],
                next1,
                next2,
                nontrivial or digit_nontrivial,
            )
            if target in seen:
                continue
            if (
                next1 == 0
                and next2 == 0
                and target[6]
                and all(state in accepting for state in target[:4])
            ):
                raise AssertionError("the automaton language contains a nontrivial 4-AP")
            seen.add(target)
            queue.append(target)

    return len(seen)


def verify_recursive_shells(dfa: DFA, accepting: set[int], depth: int) -> None:
    scale = 64
    state = {scale + value for value in H}

    for h in range(1, depth + 1):
        expected_size = (9 * (3**h) - 3) // 2
        if len(state) != expected_size:
            raise AssertionError(f"wrong cardinality at depth {h}")
        if not all(scale <= value < 2 * scale for value in state):
            raise AssertionError(f"state left its dyadic shell at depth {h}")
        witness = first_4ap(state)
        if witness is not None:
            raise AssertionError(f"finite state has a 4-AP at depth {h}: {witness}")

        accepted_shell = {
            value
            for value in range(scale, 2 * scale)
            if accepts_integer(dfa, accepting, value)
        }
        if accepted_shell != state:
            raise AssertionError(f"automaton/recursion mismatch at depth {h}")

        if h == depth:
            break

        step = separation(h, scale)
        if not (step > max(state)):
            raise AssertionError("translate layers are not disjoint")
        if v2(step) % 2:
            raise AssertionError("coordinated side anchor is not the left endpoint")

        next_scale, state = next_state(h, scale, state)
        if next_scale != BASE * scale:
            raise AssertionError("scale recurrence failed")
        scale = next_scale


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=5)
    args = parser.parse_args()
    if args.depth < 1:
        raise ValueError("depth must be positive")

    nfa, nfa_start, nfa_accept = build_nfa()
    dfa, accepting = determinize(nfa, nfa_start, nfa_accept)
    signature = dfa_signature(dfa, accepting)
    product_states = certify_4ap_free(dfa, accepting)
    verify_recursive_shells(dfa, accepting, args.depth)

    certificate = Certificate(
        dfa_states=len(dfa),
        accepting_states=len(accepting),
        product_states=product_states,
        signature=signature,
    )

    print("verified: recursive shells match the automaton")
    print("verified: every checked finite shell is 4-AP-free")
    print("verified: v2(R_h) is even at every checked replication level")
    print("verified: the full automaton language is 4-AP-free")
    print(f"depth_checked={args.depth}")
    print(f"dfa_states={certificate.dfa_states}")
    print(f"accepting_states={certificate.accepting_states}")
    print(f"product_states={certificate.product_states}")
    print(f"dfa_signature={certificate.signature}")


if __name__ == "__main__":
    main()
