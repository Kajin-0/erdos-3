#!/usr/bin/env python3
"""Exhaustive period-2 digit-system search for Erdős Problem #3.

Goal
----
Search for periodic digit-restricted systems

    D_0, D_1, ..., D_{m-1} subset {0,...,b-1}

whose base-b digit language avoids 4-term arithmetic progressions and whose
fractal/logarithmic density exponent beats a target value.  The immediate target
is Walker's base-55 fixed-digit benchmark

    alpha_55 = log(21) / log(55) ~= 0.75974.

This file implements the first exact search engine: period m=2, exhaustive over
all digit-set size profiles above the target.  It uses a finite carry automaton
for the two linear equations defining a 4-term AP:

    x0 - 2*x1 + x2 = 0,
    x1 - 2*x2 + x3 = 0.

For a fixed pair (D0,D1), the checker is exact under the periodic digit model.
If the carry automaton can return to (0,0) through a nontrivial digit path, then
there is a finite 4-term AP in the digit language.  If no such return exists,
the periodic digit system is certified 4-AP-free.

This is not yet a SAT solver.  It is an exact brute-force baseline designed to
produce reliable data before adding SAT/SMT optimization.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from itertools import combinations, product
from math import log
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple
from collections import deque

Carry = Tuple[int, int]
Mask = int
TransitionTable = Dict[Mask, Dict[Carry, Tuple[Tuple[int, int, bool], ...]]]


@dataclass(frozen=True)
class SearchResult:
    b: int
    period: int
    size_profile: Tuple[int, int]
    alpha: float
    profiles_examined: int
    pairs_examined: int
    found: bool
    D0: Tuple[int, ...] | None
    D1: Tuple[int, ...] | None


def mask_to_digits(mask: Mask, b: int) -> Tuple[int, ...]:
    return tuple(i for i in range(b) if (mask >> i) & 1)


def digits_to_mask(digits: Sequence[int]) -> Mask:
    mask = 0
    for d in digits:
        mask |= 1 << d
    return mask


def masks_containing_zero_of_size(b: int, size: int) -> List[Mask]:
    if size < 1 or size > b:
        return []
    return [digits_to_mask((0,) + tail) for tail in combinations(range(1, b), size - 1)]


def density_exponent(b: int, size_profile: Sequence[int]) -> float:
    return sum(log(s) for s in size_profile) / (len(size_profile) * log(b))


def carry_values() -> range:
    # For digits 0 <= a_i < b and relation a0 - 2*a1 + a2 + c,
    # a fixed small window is enough for this four-term AP carry automaton.
    # The wider range is intentionally conservative.
    return range(-4, 5)


def precompute_transitions(b: int, masks: Iterable[Mask]) -> TransitionTable:
    """Precompute carry transitions for all masks used by the search."""
    C = list(carry_values())
    tables: TransitionTable = {}
    for mask in sorted(set(masks)):
        D = mask_to_digits(mask, b)
        table: Dict[Carry, Tuple[Tuple[int, int, bool], ...]] = {}
        for c1 in C:
            for c2 in C:
                outs = set()
                for a0, a1, a2, a3 in product(D, repeat=4):
                    s1 = a0 - 2 * a1 + a2 + c1
                    if s1 % b != 0:
                        continue
                    n1 = s1 // b
                    if n1 not in C:
                        continue
                    s2 = a1 - 2 * a2 + a3 + c2
                    if s2 % b != 0:
                        continue
                    n2 = s2 // b
                    if n2 in C:
                        outs.add((n1, n2, len({a0, a1, a2, a3}) > 1))
                table[(c1, c2)] = tuple(sorted(outs))
        tables[mask] = table
    return tables


def has_periodic_4ap(masks: Sequence[Mask], transitions: TransitionTable) -> bool:
    """Return True if the periodic digit system contains a nontrivial 4-AP."""
    m = len(masks)
    start = (0, 0, 0, False)  # residue, carry1, carry2, nontrivial digit used?
    q = deque([start])
    seen = {start}

    while q:
        r, c1, c2, nontrivial = q.popleft()
        for n1, n2, digit_nontrivial in transitions[masks[r]][(c1, c2)]:
            nontrivial2 = nontrivial or digit_nontrivial
            if n1 == 0 and n2 == 0 and nontrivial2:
                return True
            state = ((r + 1) % m, n1, n2, nontrivial2)
            if state not in seen:
                seen.add(state)
                q.append(state)
    return False


def size_profiles_above_target(
    b: int,
    target_alpha: float,
    min_size: int = 1,
) -> List[Tuple[int, int]]:
    profiles = []
    for s0 in range(min_size, b + 1):
        for s1 in range(min_size, b + 1):
            alpha = density_exponent(b, (s0, s1))
            if alpha > target_alpha:
                profiles.append((s0, s1))
    # Hardest/highest-density profiles first.
    profiles.sort(key=lambda ss: (-density_exponent(b, ss), -ss[0] * ss[1], ss))
    return profiles


def search_period2_profile(
    b: int,
    size_profile: Tuple[int, int],
    transitions: TransitionTable,
) -> Tuple[bool, int, Tuple[int, ...] | None, Tuple[int, ...] | None]:
    A = masks_containing_zero_of_size(b, size_profile[0])
    B = masks_containing_zero_of_size(b, size_profile[1])
    pairs_examined = 0
    for m0 in A:
        for m1 in B:
            pairs_examined += 1
            if not has_periodic_4ap((m0, m1), transitions):
                return True, pairs_examined, mask_to_digits(m0, b), mask_to_digits(m1, b)
    return False, pairs_examined, None, None


def search_base(
    b: int,
    target_alpha: float,
    max_profiles: int | None = None,
) -> List[SearchResult]:
    profiles = size_profiles_above_target(b, target_alpha)
    if max_profiles is not None:
        profiles = profiles[:max_profiles]

    all_masks = []
    for s0, s1 in profiles:
        all_masks.extend(masks_containing_zero_of_size(b, s0))
        all_masks.extend(masks_containing_zero_of_size(b, s1))
    transitions = precompute_transitions(b, all_masks)

    results: List[SearchResult] = []
    for index, profile in enumerate(profiles, start=1):
        found, pairs, D0, D1 = search_period2_profile(b, profile, transitions)
        result = SearchResult(
            b=b,
            period=2,
            size_profile=profile,
            alpha=density_exponent(b, profile),
            profiles_examined=index,
            pairs_examined=pairs,
            found=found,
            D0=D0,
            D1=D1,
        )
        results.append(result)
        status = "HIT" if found else "MISS"
        print(
            f"b={b:2d} profile={profile} alpha={result.alpha:.8f} "
            f"pairs={pairs:9d} {status}"
        )
        if found:
            print(f"  D0={D0}")
            print(f"  D1={D1}")
            break
    return results


def write_csv(path: Path, rows: Sequence[SearchResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "b",
                "period",
                "size_profile",
                "alpha",
                "profiles_examined",
                "pairs_examined",
                "found",
                "D0",
                "D1",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "b": row.b,
                    "period": row.period,
                    "size_profile": " ".join(map(str, row.size_profile)),
                    "alpha": f"{row.alpha:.10f}",
                    "profiles_examined": row.profiles_examined,
                    "pairs_examined": row.pairs_examined,
                    "found": int(row.found),
                    "D0": "" if row.D0 is None else " ".join(map(str, row.D0)),
                    "D1": "" if row.D1 is None else " ".join(map(str, row.D1)),
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-min", type=int, default=11)
    parser.add_argument("--b-max", type=int, default=13)
    parser.add_argument("--target-alpha", type=float, default=log(21) / log(55))
    parser.add_argument(
        "--max-profiles",
        type=int,
        default=None,
        help="Optional cap for quick exploratory runs; omit for exact run over all profiles above target.",
    )
    parser.add_argument("--csv", type=Path, default=None)
    args = parser.parse_args()

    all_results: List[SearchResult] = []
    print(f"target_alpha={args.target_alpha:.10f}")
    for b in range(args.b_min, args.b_max + 1):
        all_results.extend(search_base(b, args.target_alpha, args.max_profiles))

    if args.csv:
        write_csv(args.csv, all_results)
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()
