#!/usr/bin/env python3
"""Exact AP certifier for least-significant-digit-first finite automata.

This is the first non-Walker model class in the repo.  Instead of a one-layer
digit set D, it accepts a deterministic finite automaton over base-b digits.
The automaton reads digits least significant first.  This orientation matches
carry propagation for arithmetic progressions.

DFA convention
--------------
A nonnegative integer n is accepted if at least one sufficiently zero-padded
base-b LSD-first digit word for n ends in an accepting state.  In practice this
repo uses zero-padding-closed DFAs: if a state is accepting, reading additional
high zero digits keeps the computation in an accepting state.  This is the
natural convention for finite integer languages described by digit automata.

4-AP certificate
----------------
A 4-term AP x0,x1,x2,x3 is equivalent to two second-difference equations:

    x0 - 2*x1 + x2 = 0,
    x1 - 2*x2 + x3 = 0.

Reading digits LSD-first gives a finite product automaton over four DFA states
and two carries.  If there is a reachable nontrivial path that returns both
carries to zero while all four DFA states are accepting, the language contains a
nontrivial 4-AP.  If no such path exists, the language is certified 4-AP-free.

Input JSON schema
-----------------
{
  "base": 11,
  "states": ["q", "dead"],
  "start": "q",
  "accept": ["q"],
  "transitions": {
    "q": {"0": "q", "1": "q", ..., "10": "dead"},
    "dead": {"0": "dead", ..., "10": "dead"}
  }
}

The file `examples/dfa/base11_digit_set.json` encodes Walker's base-11 digit set
as a two-state DFA.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Sequence, Tuple

State = str
Digit = int
Carry = Tuple[int, int]
ProductState = Tuple[State, State, State, State, int, int, bool]
WitnessStep = Tuple[Tuple[int, int, int, int], Carry, Carry, Tuple[State, State, State, State]]


@dataclass(frozen=True)
class DFA:
    base: int
    states: tuple[State, ...]
    start: State
    accept: frozenset[State]
    transitions: dict[State, dict[int, State]]

    def next(self, state: State, digit: int) -> State:
        return self.transitions[state][digit]

    def validate(self) -> None:
        if self.base < 2:
            raise ValueError("base must be at least 2")
        if self.start not in self.states:
            raise ValueError("start state is not listed in states")
        missing_accept = self.accept - set(self.states)
        if missing_accept:
            raise ValueError(f"accept states missing from states list: {sorted(missing_accept)}")
        for state in self.states:
            if state not in self.transitions:
                raise ValueError(f"missing transition row for state {state}")
            row = self.transitions[state]
            for digit in range(self.base):
                if digit not in row:
                    raise ValueError(f"missing transition for state={state}, digit={digit}")
                if row[digit] not in self.states:
                    raise ValueError(f"transition from state={state}, digit={digit} points outside states")


def load_dfa(path: Path) -> DFA:
    raw = json.loads(path.read_text())
    transitions: dict[State, dict[int, State]] = {}
    for state, row in raw["transitions"].items():
        transitions[state] = {int(d): nxt for d, nxt in row.items()}
    dfa = DFA(
        base=int(raw["base"]),
        states=tuple(raw["states"]),
        start=raw["start"],
        accept=frozenset(raw["accept"]),
        transitions=transitions,
    )
    dfa.validate()
    return dfa


def carry_values() -> range:
    # Coefficients are 1,-2,1.  A small conservative window is enough for
    # stable carry propagation in this setting.
    return range(-4, 5)


def transition_options(dfa: DFA, states4: tuple[State, State, State, State], c1: int, c2: int):
    C = set(carry_values())
    b = dfa.base
    q0, q1, q2, q3 = states4
    for a0 in range(b):
        q0n = dfa.next(q0, a0)
        for a1 in range(b):
            q1n = dfa.next(q1, a1)
            for a2 in range(b):
                s1 = a0 - 2 * a1 + a2 + c1
                if s1 % b:
                    continue
                n1 = s1 // b
                if n1 not in C:
                    continue
                q2n = dfa.next(q2, a2)
                for a3 in range(b):
                    s2 = a1 - 2 * a2 + a3 + c2
                    if s2 % b:
                        continue
                    n2 = s2 // b
                    if n2 not in C:
                        continue
                    q3n = dfa.next(q3, a3)
                    digits = (a0, a1, a2, a3)
                    nontrivial_digit = len(set(digits)) > 1
                    yield digits, (n1, n2), (q0n, q1n, q2n, q3n), nontrivial_digit


def find_4ap_witness(dfa: DFA, want_witness: bool = False) -> list[WitnessStep] | None:
    """Return a witness path if the DFA language contains a nontrivial 4-AP."""
    start4 = (dfa.start, dfa.start, dfa.start, dfa.start)
    start: ProductState = (*start4, 0, 0, False)
    queue = deque([(start, [])])
    seen = {start}

    while queue:
        state, path = queue.popleft()
        q0, q1, q2, q3, c1, c2, nontriv = state
        states4 = (q0, q1, q2, q3)
        for digits, (n1, n2), next4, digit_nontriv in transition_options(dfa, states4, c1, c2):
            nontriv2 = nontriv or digit_nontriv
            step = (digits, (c1, c2), (n1, n2), next4)
            if n1 == 0 and n2 == 0 and nontriv2 and all(q in dfa.accept for q in next4):
                return path + [step] if want_witness else []
            next_state: ProductState = (*next4, n1, n2, nontriv2)
            if next_state not in seen:
                seen.add(next_state)
                queue.append((next_state, path + [step] if want_witness else []))
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dfa", type=Path, required=True)
    parser.add_argument("--witness", action="store_true")
    args = parser.parse_args()

    dfa = load_dfa(args.dfa)
    witness = find_4ap_witness(dfa, want_witness=args.witness)
    contains = witness is not None
    print(f"base={dfa.base}")
    print(f"states={len(dfa.states)}")
    print(f"accepting_states={len(dfa.accept)}")
    print(f"contains_nontrivial_4ap={int(contains)}")
    print(f"certified_4ap_free={int(not contains)}")
    if args.witness and witness is not None:
        print("witness_digits_lsd_first:")
        for i, (digits, old_carry, new_carry, states4) in enumerate(witness):
            print(f"  pos={i} digits={digits} carry={old_carry}->{new_carry} states={states4}")


if __name__ == "__main__":
    main()
