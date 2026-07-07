#!/usr/bin/env python3
"""Stochastic periodic digit search with exact 4-AP certification.

This script is the next search layer after `periodic_exhaustive_search.py`.
The exhaustive script is reliable but becomes combinatorially expensive for
larger bases.  This file uses a witness-guided deletion/rebuild heuristic:

1. Start from full periodic digit sets.
2. Use the exact finite carry automaton to find a 4-AP witness.
3. Delete one nonzero digit appearing in that witness.
4. Repeat until the language is certified 4-AP-free.
5. Greedily try to re-add deleted digits while preserving the exact certificate.

Every final candidate is checked by the same automaton certificate.  The search
is stochastic, but reproducible through explicit seeds.

This is a search heuristic, not a proof of optimality.  Its role is to discover
candidate structures for later exact or SAT/SMT certification.
"""
from __future__ import annotations

import argparse
import csv
import random
from collections import deque
from dataclasses import dataclass
from itertools import product
from math import log
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

Mask = int
Carry = Tuple[int, int]
Transition = Tuple[int, int, bool, Tuple[int, int, int, int]]
TransitionTable = Dict[Carry, Tuple[Transition, ...]]

TARGET_ALPHA_55 = log(21) / log(55)


def mask_to_digits(mask: Mask, b: int) -> Tuple[int, ...]:
    return tuple(i for i in range(b) if (mask >> i) & 1)


def digits_to_mask(digits: Iterable[int]) -> Mask:
    mask = 0
    for d in digits:
        mask |= 1 << d
    return mask


def density_exponent(b: int, masks: Sequence[Mask]) -> float:
    return sum(log(mask.bit_count()) for mask in masks) / (len(masks) * log(b))


def carry_values() -> range:
    # Conservative carry window for the two second-difference relations.
    return range(-4, 5)


class TransitionCache:
    def __init__(self, b: int):
        self.b = b
        self.cache: Dict[Mask, TransitionTable] = {}

    def table(self, mask: Mask) -> TransitionTable:
        if mask not in self.cache:
            self.cache[mask] = self._build(mask)
        return self.cache[mask]

    def _build(self, mask: Mask) -> TransitionTable:
        b = self.b
        D = mask_to_digits(mask, b)
        Dset = set(D)
        C = set(carry_values())
        table: TransitionTable = {}

        # Optimized form of the relation check.  Instead of looping over D^4,
        # choose a1,a2 and possible outgoing carries n1,n2, then solve for
        # a0 and a3.  This reduces the transition build cost substantially.
        for c1 in C:
            for c2 in C:
                outs = set()
                for a1 in D:
                    for a2 in D:
                        for n1 in C:
                            a0 = b * n1 - c1 + 2 * a1 - a2
                            if a0 not in Dset:
                                continue
                            for n2 in C:
                                a3 = b * n2 - c2 - a1 + 2 * a2
                                if a3 in Dset:
                                    digs = (a0, a1, a2, a3)
                                    outs.add((n1, n2, len(set(digs)) > 1, digs))
                table[(c1, c2)] = tuple(sorted(outs))
        return table


def find_4ap_witness(
    b: int,
    masks: Sequence[Mask],
    cache: TransitionCache,
) -> List[Tuple[int, Tuple[int, int, int, int]]] | None:
    """Return a witness path if the periodic language contains a nontrivial 4-AP."""
    transitions = [cache.table(mask) for mask in masks]
    period = len(masks)
    start = (0, 0, 0, False)  # residue class, carry1, carry2, nontrivial?
    q = deque([(start, [])])
    seen = {start}

    while q:
        (r, c1, c2, nontrivial), path = q.popleft()
        for n1, n2, digit_nontrivial, digs in transitions[r][(c1, c2)]:
            nontrivial2 = nontrivial or digit_nontrivial
            path2 = path + [(r, digs)]
            if n1 == 0 and n2 == 0 and nontrivial2:
                return path2
            state = ((r + 1) % period, n1, n2, nontrivial2)
            if state not in seen:
                seen.add(state)
                q.append((state, path2))
    return None


@dataclass(frozen=True)
class Candidate:
    b: int
    period: int
    trial: int
    seed: int
    alpha: float
    steps: int
    masks: Tuple[Mask, ...]

    @property
    def sizes(self) -> Tuple[int, ...]:
        return tuple(mask.bit_count() for mask in self.masks)

    def digit_sets(self) -> Tuple[Tuple[int, ...], ...]:
        return tuple(mask_to_digits(mask, self.b) for mask in self.masks)


def deletion_rebuild_trial(
    b: int,
    period: int,
    seed: int,
    max_steps: int = 10_000,
) -> Candidate:
    rng = random.Random(seed)
    cache = TransitionCache(b)
    masks = [(1 << b) - 1 for _ in range(period)]
    steps = 0

    # Deletion phase: remove digits from AP witnesses until AP-free.
    while steps < max_steps:
        witness = find_4ap_witness(b, masks, cache)
        if witness is None:
            break

        choices = []
        for r, digs in witness:
            for d in set(digs):
                if d != 0 and ((masks[r] >> d) & 1):
                    choices.append((r, d))

        if not choices:
            break

        # Random witness cut.  This keeps the search exploratory; later SAT/SMT
        # tooling should replace this with an exact optimizer.
        r, d = rng.choice(choices)
        masks[r] &= ~(1 << d)
        steps += 1

        # Avoid meaningless degenerate layers.
        if any(mask.bit_count() < 2 for mask in masks):
            break

    # Rebuild phase: greedily try to recover deleted digits while preserving
    # exact AP-freeness.
    improved = True
    while improved:
        improved = False
        candidates = [
            (r, d)
            for r in range(period)
            for d in range(1, b)
            if not ((masks[r] >> d) & 1)
        ]
        rng.shuffle(candidates)
        candidates.sort(key=lambda rd: (rd[1], rng.random()))

        for r, d in candidates:
            new_masks = list(masks)
            new_masks[r] |= 1 << d
            if find_4ap_witness(b, new_masks, cache) is None:
                masks = new_masks
                improved = True
                break

    # Final exact certification.
    witness = find_4ap_witness(b, masks, cache)
    if witness is not None:
        raise RuntimeError("internal error: final candidate is not AP-free")

    return Candidate(
        b=b,
        period=period,
        trial=-1,
        seed=seed,
        alpha=density_exponent(b, masks),
        steps=steps,
        masks=tuple(masks),
    )


def search(
    b_min: int,
    b_max: int,
    periods: Sequence[int],
    trials: int,
    seed_base: int,
) -> List[Candidate]:
    best: List[Candidate] = []
    for period in periods:
        for b in range(b_min, b_max + 1):
            local_best: Candidate | None = None
            for trial in range(trials):
                seed = seed_base * period * b + trial
                cand0 = deletion_rebuild_trial(b, period, seed)
                cand = Candidate(
                    b=b,
                    period=period,
                    trial=trial,
                    seed=seed,
                    alpha=cand0.alpha,
                    steps=cand0.steps,
                    masks=cand0.masks,
                )
                if local_best is None or cand.alpha > local_best.alpha:
                    local_best = cand
            assert local_best is not None
            best.append(local_best)
            status = "TARGET" if local_best.alpha > TARGET_ALPHA_55 else "below"
            print(
                f"period={period} b={b} best_alpha={local_best.alpha:.10f} "
                f"sizes={local_best.sizes} {status} seed={local_best.seed}"
            )
    return best


def write_csv(path: Path, candidates: Sequence[Candidate]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    max_period = max(c.period for c in candidates) if candidates else 0
    fields = [
        "period",
        "b",
        "trials",
        "best_trial",
        "seed",
        "alpha",
        "target_hit",
        "sizes",
        "steps",
    ] + [f"D{i}" for i in range(max_period)]

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for cand in candidates:
            row = {
                "period": cand.period,
                "b": cand.b,
                "trials": "",
                "best_trial": cand.trial,
                "seed": cand.seed,
                "alpha": f"{cand.alpha:.10f}",
                "target_hit": int(cand.alpha > TARGET_ALPHA_55),
                "sizes": " ".join(map(str, cand.sizes)),
                "steps": cand.steps,
            }
            for i, D in enumerate(cand.digit_sets()):
                row[f"D{i}"] = " ".join(map(str, D))
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-min", type=int, default=14)
    parser.add_argument("--b-max", type=int, default=18)
    parser.add_argument("--periods", type=int, nargs="+", default=[2, 3])
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--seed-base", type=int, default=10_000)
    parser.add_argument("--csv", type=Path, default=None)
    args = parser.parse_args()

    candidates = search(args.b_min, args.b_max, args.periods, args.trials, args.seed_base)
    if args.csv:
        write_csv(args.csv, candidates)
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()
