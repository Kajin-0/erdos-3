#!/usr/bin/env python3
"""Minimize and canonicalize LSD-first DFA digit languages.

Random DFA search produces many duplicate presentations of the same language.
This utility makes those duplicates visible by:

1. removing unreachable states;
2. minimizing equivalent states by partition refinement;
3. renaming states canonically by breadth-first traversal from the start state;
4. emitting a stable JSON representation and SHA256 signature.

The canonical form is intended for candidate deduplication.  It assumes a complete
DFA over digits 0,...,b-1 and uses the same JSON schema as `dfa_ap_cert.py`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from dfa_ap_cert import DFA, load_dfa


def reachable_states(dfa: DFA) -> tuple[str, ...]:
    seen = {dfa.start}
    q = deque([dfa.start])
    while q:
        state = q.popleft()
        for digit in range(dfa.base):
            nxt = dfa.next(state, digit)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return tuple(s for s in dfa.states if s in seen)


def restrict_to_reachable(dfa: DFA) -> DFA:
    states = reachable_states(dfa)
    keep = set(states)
    transitions = {
        s: {d: dfa.next(s, d) for d in range(dfa.base)}
        for s in states
    }
    out = DFA(
        base=dfa.base,
        states=states,
        start=dfa.start,
        accept=frozenset(s for s in dfa.accept if s in keep),
        transitions=transitions,
    )
    out.validate()
    return out


def minimize_dfa(dfa: DFA) -> DFA:
    dfa = restrict_to_reachable(dfa)
    states = list(dfa.states)

    # Initial partition: accepting vs rejecting.
    accept_block = frozenset(s for s in states if s in dfa.accept)
    reject_block = frozenset(s for s in states if s not in dfa.accept)
    partition = [block for block in (accept_block, reject_block) if block]

    changed = True
    while changed:
        changed = False
        block_id = {state: i for i, block in enumerate(partition) for state in block}
        new_partition: list[frozenset[str]] = []
        for block in partition:
            buckets: dict[tuple[int, ...], list[str]] = {}
            for state in block:
                signature = tuple(block_id[dfa.next(state, d)] for d in range(dfa.base))
                buckets.setdefault(signature, []).append(state)
            if len(buckets) > 1:
                changed = True
            for members in buckets.values():
                new_partition.append(frozenset(members))
        partition = new_partition

    # Stable representative names before canonical BFS.
    block_index = {state: i for i, block in enumerate(partition) for state in block}
    min_states = tuple(f"m{block_index[s]}" for s in states if s in {next(iter(b)) for b in partition})
    # Easier: build transitions over block ids, then canonicalize.
    transitions_by_block: dict[str, dict[int, str]] = {}
    accept_blocks = set()
    for i, block in enumerate(partition):
        name = f"m{i}"
        rep = next(iter(block))
        if rep in dfa.accept:
            accept_blocks.add(name)
        transitions_by_block[name] = {
            d: f"m{block_index[dfa.next(rep, d)]}" for d in range(dfa.base)
        }

    minimized = DFA(
        base=dfa.base,
        states=tuple(f"m{i}" for i in range(len(partition))),
        start=f"m{block_index[dfa.start]}",
        accept=frozenset(accept_blocks),
        transitions=transitions_by_block,
    )
    minimized.validate()
    return canonical_rename(minimized)


def canonical_rename(dfa: DFA) -> DFA:
    mapping: dict[str, str] = {}
    q = deque([dfa.start])
    mapping[dfa.start] = "q0"

    while q:
        state = q.popleft()
        for digit in range(dfa.base):
            nxt = dfa.next(state, digit)
            if nxt not in mapping:
                mapping[nxt] = f"q{len(mapping)}"
                q.append(nxt)

    states = tuple(f"q{i}" for i in range(len(mapping)))
    transitions = {
        mapping[state]: {d: mapping[dfa.next(state, d)] for d in range(dfa.base)}
        for state in mapping
    }
    out = DFA(
        base=dfa.base,
        states=states,
        start="q0",
        accept=frozenset(mapping[s] for s in dfa.accept if s in mapping),
        transitions=transitions,
    )
    out.validate()
    return out


def dfa_to_canonical_dict(dfa: DFA) -> dict[str, object]:
    return {
        "base": dfa.base,
        "states": list(dfa.states),
        "start": dfa.start,
        "accept": sorted(dfa.accept),
        "transitions": {
            state: {str(digit): dfa.next(state, digit) for digit in range(dfa.base)}
            for state in dfa.states
        },
    }


def canonical_json(dfa: DFA) -> str:
    return json.dumps(dfa_to_canonical_dict(dfa), indent=2, sort_keys=True) + "\n"


def canonical_signature(dfa: DFA) -> str:
    return hashlib.sha256(canonical_json(dfa).encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dfa", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--no-minimize", action="store_true")
    args = parser.parse_args()

    dfa = load_dfa(args.dfa)
    canon = canonical_rename(restrict_to_reachable(dfa)) if args.no_minimize else minimize_dfa(dfa)
    text = canonical_json(canon)
    sig = canonical_signature(canon)

    print(f"base={canon.base}")
    print(f"states={len(canon.states)}")
    print(f"accepting_states={len(canon.accept)}")
    print(f"signature={sig}")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(f"wrote {args.output}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
