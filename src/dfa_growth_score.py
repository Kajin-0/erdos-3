#!/usr/bin/env python3
"""Growth and truncated harmonic triage for LSD-first DFA digit languages.

This is not a full transfer-operator harmonic scorer.  It is a practical triage
layer for regular-language candidates:

1. estimate the exponential growth exponent from the productive transition graph;
2. compute exact accepted counts by digit length;
3. enumerate accepted integers up to a bounded digit length;
4. compute a truncated shifted harmonic sum over that bounded prefix.

The growth exponent is

    alpha = log(rho(A_prod)) / log(b),

where A_prod is the digit-transition matrix induced on states that are both
reachable from the start and capable of reaching an accepting state.  Rejecting
sink components must be excluded: they can have spectral radius b while
contributing no accepted words.  If alpha < 1, the full shifted reciprocal sum is
expected to converge for regular languages with the usual zero-padding closure.

The truncated shifted sum is

    H_M = sum_{0 <= n < b^M, accepted(n)} 1/(n+1).

It is a lower bound for the full shifted sum when the accepted language is
zero-padding closed.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import log
from pathlib import Path
from typing import Sequence

from dfa_ap_cert import DFA, load_dfa


@dataclass(frozen=True)
class GrowthScore:
    base: int
    states: int
    accepting_states: int
    spectral_radius: float
    alpha: float
    max_digits: int
    truncated_shifted_sum: float
    accepted_counts: tuple[int, ...]


def productive_states(dfa: DFA) -> tuple[str, ...]:
    """Return states lying on some start-to-accepting path.

    The accepted-language growth rate is controlled by the subgraph of states
    that are both reachable from ``dfa.start`` and coaccessible to an accepting
    state.  Reachable rejecting sinks are deliberately excluded.
    """
    reachable: set[str] = set()
    stack = [dfa.start]
    while stack:
        state = stack.pop()
        if state in reachable:
            continue
        reachable.add(state)
        for digit in range(dfa.base):
            stack.append(dfa.next(state, digit))

    reverse: dict[str, set[str]] = {state: set() for state in dfa.states}
    for state in dfa.states:
        for digit in range(dfa.base):
            reverse[dfa.next(state, digit)].add(state)

    coaccessible: set[str] = set()
    stack = list(dfa.accept)
    while stack:
        state = stack.pop()
        if state in coaccessible:
            continue
        coaccessible.add(state)
        stack.extend(reverse[state])

    return tuple(
        state
        for state in dfa.states
        if state in reachable and state in coaccessible
    )


def transition_matrix(
    dfa: DFA,
    states: Sequence[str] | None = None,
) -> list[list[int]]:
    """Build the digit-transition matrix induced on ``states``.

    Transitions leaving the selected state set are omitted.  With ``states=None``
    the complete DFA transition matrix is returned, which is still required for
    exact accepted-word counts.
    """
    selected = tuple(dfa.states if states is None else states)
    index = {state: i for i, state in enumerate(selected)}
    n = len(selected)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for state in selected:
        i = index[state]
        for digit in range(dfa.base):
            target = dfa.next(state, digit)
            j = index.get(target)
            if j is not None:
                matrix[i][j] += 1
    return matrix


def mat_vec(matrix: list[list[int]], vec: list[float]) -> list[float]:
    out = [0.0 for _ in vec]
    for i, row in enumerate(matrix):
        vi = vec[i]
        if vi == 0.0:
            continue
        for j, aij in enumerate(row):
            if aij:
                out[j] += vi * aij
    return out


def spectral_radius_power(matrix: list[list[int]], iterations: int = 200) -> float:
    n = len(matrix)
    if n == 0:
        return 0.0
    vec = [1.0 / n for _ in range(n)]
    last_norm = 1.0
    for _ in range(iterations):
        nxt = mat_vec(matrix, vec)
        norm = max(abs(x) for x in nxt)
        if norm == 0.0:
            return 0.0
        vec = [x / norm for x in nxt]
        last_norm = norm
    # Collatz-style Rayleigh estimate using total mass ratio.
    nxt = mat_vec(matrix, vec)
    denom = sum(vec)
    return sum(nxt) / denom if denom else last_norm


def accepted_counts_by_length(dfa: DFA, max_digits: int) -> tuple[int, ...]:
    index = {state: i for i, state in enumerate(dfa.states)}
    accept_idx = {index[s] for s in dfa.accept}
    matrix = transition_matrix(dfa)

    counts = []
    vec = [0 for _ in dfa.states]
    vec[index[dfa.start]] = 1
    for _length in range(max_digits + 1):
        counts.append(sum(vec[i] for i in accept_idx))
        nxt = [0 for _ in dfa.states]
        for i, row in enumerate(matrix):
            if vec[i] == 0:
                continue
            for j, aij in enumerate(row):
                if aij:
                    nxt[j] += vec[i] * aij
        vec = nxt
    return tuple(counts)


def accepts_number(dfa: DFA, n: int, width: int, pad_zeros: int = 8) -> bool:
    state = dfa.start
    x = n
    for _ in range(width):
        digit = x % dfa.base
        x //= dfa.base
        state = dfa.next(state, digit)
    # A bounded zero-padding check makes the convention explicit without risking
    # a nonterminating loop for DFAs that never reach an accepting state by zeros.
    for _ in range(pad_zeros):
        if state in dfa.accept:
            return True
        state = dfa.next(state, 0)
    return state in dfa.accept


def truncated_shifted_sum(dfa: DFA, max_digits: int) -> float:
    limit = dfa.base**max_digits
    total = 0.0
    for n in range(limit):
        if accepts_number(dfa, n, max_digits):
            total += 1.0 / (n + 1)
    return total


def score_dfa(dfa: DFA, max_digits: int, power_iterations: int) -> GrowthScore:
    growth_states = productive_states(dfa)
    matrix = transition_matrix(dfa, growth_states)
    rho = spectral_radius_power(matrix, power_iterations)
    alpha = log(rho) / log(dfa.base) if rho > 0 else float("-inf")
    counts = accepted_counts_by_length(dfa, max_digits)
    trunc = truncated_shifted_sum(dfa, max_digits)
    return GrowthScore(
        base=dfa.base,
        states=len(dfa.states),
        accepting_states=len(dfa.accept),
        spectral_radius=rho,
        alpha=alpha,
        max_digits=max_digits,
        truncated_shifted_sum=trunc,
        accepted_counts=counts,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dfa", type=Path, required=True)
    parser.add_argument("--max-digits", type=int, default=6)
    parser.add_argument("--power-iterations", type=int, default=200)
    args = parser.parse_args()

    dfa = load_dfa(args.dfa)
    score = score_dfa(dfa, args.max_digits, args.power_iterations)
    print(f"base={score.base}")
    print(f"states={score.states}")
    print(f"accepting_states={score.accepting_states}")
    print(f"productive_states={len(productive_states(dfa))}")
    print(f"spectral_radius={score.spectral_radius:.12f}")
    print(f"alpha={score.alpha:.12f}")
    print(f"max_digits={score.max_digits}")
    print(f"truncated_shifted_sum={score.truncated_shifted_sum:.12f}")
    print("accepted_counts_by_length=" + " ".join(map(str, score.accepted_counts)))


if __name__ == "__main__":
    main()
