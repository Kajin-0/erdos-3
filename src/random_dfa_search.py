#!/usr/bin/env python3
"""Random search for small regular digit-language candidates.

This is the first executable search harness for the DFA model class.  It creates
small least-significant-digit-first DFAs, enforces zero-padding closure on
accepting states, checks exact 4-AP-freeness with `dfa_ap_cert.py`, and ranks
survivors with `dfa_growth_score.py`.

The search is deliberately conservative:

- every reported candidate is exactly certified 4-AP-free;
- the score is only a bounded triage score, not a full harmonic sum;
- candidates that behave like trivial one-layer digit-set DFAs can be filtered.

Example:

    python src/random_dfa_search.py --base 5 --states 3 --trials 1000 \
        --max-digits 6 --csv data/random_dfa_search.csv \
        --save-dir candidates/dfa
"""
from __future__ import annotations

import argparse
import csv
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from dfa_ap_cert import DFA, find_4ap_witness
from dfa_growth_score import score_dfa


@dataclass(frozen=True)
class SearchHit:
    rank: int
    trial: int
    seed: int
    base: int
    states: int
    accepting_states: int
    alpha: float
    spectral_radius: float
    truncated_shifted_sum: float
    max_digits: int
    accepted_counts: tuple[int, ...]
    path: str


def make_random_dfa(
    base: int,
    states: int,
    rng: random.Random,
    accept_probability: float,
    transition_bias_to_accept: float,
) -> DFA:
    names = tuple(f"q{i}" for i in range(states))
    start = names[0]

    accept = {q for q in names if rng.random() < accept_probability}
    if not accept:
        accept.add(rng.choice(names))
    # Make q0 accepting often enough to include n=0 in many candidates.
    if rng.random() < 0.5:
        accept.add(start)

    transitions: dict[str, dict[int, str]] = {}
    accept_list = sorted(accept)
    all_list = list(names)
    for q in names:
        row: dict[int, str] = {}
        for d in range(base):
            if d == 0 and q in accept:
                # Zero-padding closure for accepting states.
                row[d] = q
            elif rng.random() < transition_bias_to_accept and accept_list:
                row[d] = rng.choice(accept_list)
            else:
                row[d] = rng.choice(all_list)
        transitions[q] = row

    dfa = DFA(
        base=base,
        states=names,
        start=start,
        accept=frozenset(accept),
        transitions=transitions,
    )
    dfa.validate()
    return dfa


def one_layer_digit_signature(dfa: DFA) -> tuple[int, ...] | None:
    """Detect the simplest disguised one-layer digit-set DFA.

    Returns D if the DFA language appears to be exactly "all digits lie in D"
    under a one-step test from the start state with a self-loop accepting state
    and a sink rejecting state.  This is not full DFA minimization; it is only a
    cheap filter for the most obvious Walker-style duplicates.
    """
    if dfa.start not in dfa.accept:
        return None
    allowed = []
    rejected_targets = set()
    for d in range(dfa.base):
        nxt = dfa.next(dfa.start, d)
        if nxt == dfa.start:
            allowed.append(d)
        elif nxt not in dfa.accept:
            rejected_targets.add(nxt)
        else:
            return None
    if not allowed or 0 not in allowed:
        return None
    # Rejected targets must be absorbing rejecting sinks.
    for q in rejected_targets:
        if q in dfa.accept:
            return None
        if any(dfa.next(q, d) != q for d in range(dfa.base)):
            return None
    return tuple(allowed)


def dfa_to_jsonable(dfa: DFA) -> dict[str, object]:
    return {
        "base": dfa.base,
        "states": list(dfa.states),
        "start": dfa.start,
        "accept": sorted(dfa.accept),
        "transitions": {
            q: {str(d): dfa.next(q, d) for d in range(dfa.base)}
            for q in dfa.states
        },
    }


def write_dfa(path: Path, dfa: DFA) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dfa_to_jsonable(dfa), indent=2, sort_keys=True) + "\n")


def search(
    base: int,
    states: int,
    trials: int,
    seed: int,
    max_digits: int,
    keep: int,
    skip_digit_set_like: bool,
    accept_probability: float,
    transition_bias_to_accept: float,
    save_dir: Path | None,
) -> list[SearchHit]:
    rng = random.Random(seed)
    hits: list[tuple[float, SearchHit, DFA]] = []

    for trial in range(trials):
        trial_seed = rng.randrange(2**63)
        local_rng = random.Random(trial_seed)
        dfa = make_random_dfa(
            base=base,
            states=states,
            rng=local_rng,
            accept_probability=accept_probability,
            transition_bias_to_accept=transition_bias_to_accept,
        )

        if skip_digit_set_like and one_layer_digit_signature(dfa) is not None:
            continue

        if find_4ap_witness(dfa, want_witness=False) is not None:
            continue

        score = score_dfa(dfa, max_digits=max_digits, power_iterations=120)
        sort_key = score.truncated_shifted_sum
        placeholder = SearchHit(
            rank=0,
            trial=trial,
            seed=trial_seed,
            base=base,
            states=states,
            accepting_states=score.accepting_states,
            alpha=score.alpha,
            spectral_radius=score.spectral_radius,
            truncated_shifted_sum=score.truncated_shifted_sum,
            max_digits=max_digits,
            accepted_counts=score.accepted_counts,
            path="",
        )
        hits.append((sort_key, placeholder, dfa))
        hits.sort(key=lambda item: item[0], reverse=True)
        del hits[keep:]

    final: list[SearchHit] = []
    for rank, (_key, hit, dfa) in enumerate(hits, start=1):
        path = ""
        if save_dir is not None:
            path_obj = save_dir / f"base{base}_states{states}_rank{rank}_seed{hit.seed}.json"
            write_dfa(path_obj, dfa)
            path = str(path_obj)
        final.append(
            SearchHit(
                rank=rank,
                trial=hit.trial,
                seed=hit.seed,
                base=hit.base,
                states=hit.states,
                accepting_states=hit.accepting_states,
                alpha=hit.alpha,
                spectral_radius=hit.spectral_radius,
                truncated_shifted_sum=hit.truncated_shifted_sum,
                max_digits=hit.max_digits,
                accepted_counts=hit.accepted_counts,
                path=path,
            )
        )
    return final


def write_csv(path: Path, hits: Iterable[SearchHit]) -> None:
    rows = list(hits)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "rank",
                "trial",
                "seed",
                "base",
                "states",
                "accepting_states",
                "alpha",
                "spectral_radius",
                "truncated_shifted_sum",
                "max_digits",
                "accepted_counts",
                "path",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "rank": row.rank,
                    "trial": row.trial,
                    "seed": row.seed,
                    "base": row.base,
                    "states": row.states,
                    "accepting_states": row.accepting_states,
                    "alpha": f"{row.alpha:.12f}",
                    "spectral_radius": f"{row.spectral_radius:.12f}",
                    "truncated_shifted_sum": f"{row.truncated_shifted_sum:.12f}",
                    "max_digits": row.max_digits,
                    "accepted_counts": " ".join(map(str, row.accepted_counts)),
                    "path": row.path,
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, default=5)
    parser.add_argument("--states", type=int, default=3)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--max-digits", type=int, default=6)
    parser.add_argument("--keep", type=int, default=10)
    parser.add_argument("--accept-probability", type=float, default=0.45)
    parser.add_argument("--transition-bias-to-accept", type=float, default=0.55)
    parser.add_argument("--include-digit-set-like", action="store_true")
    parser.add_argument("--save-dir", type=Path, default=None)
    parser.add_argument("--csv", type=Path, default=None)
    args = parser.parse_args()

    hits = search(
        base=args.base,
        states=args.states,
        trials=args.trials,
        seed=args.seed,
        max_digits=args.max_digits,
        keep=args.keep,
        skip_digit_set_like=not args.include_digit_set_like,
        accept_probability=args.accept_probability,
        transition_bias_to_accept=args.transition_bias_to_accept,
        save_dir=args.save_dir,
    )

    for hit in hits:
        print(
            f"rank={hit.rank} trial={hit.trial} seed={hit.seed} "
            f"alpha={hit.alpha:.6f} trunc={hit.truncated_shifted_sum:.8f} "
            f"counts={'/'.join(map(str, hit.accepted_counts))} path={hit.path}"
        )

    if args.csv:
        write_csv(args.csv, hits)
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()
