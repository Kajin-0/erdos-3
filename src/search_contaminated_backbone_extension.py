#!/usr/bin/env python3
"""Search for one more contaminated-backbone replication step.

This is an exploratory search tool, not part of the depth-five proof certificate.
It reconstructs one of the certified states, tests candidate separations R with
even v_2(R), and reports those for which

    ({0} union S) + {0,R,2R}

is four-term-progression-free and fits below the requested next dyadic scale.

The search is chunkable with --start-r and --end-r so ranges can be distributed
across machines or batch jobs.
"""

from __future__ import annotations

import argparse
import json
from multiprocessing import Pool

H = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
SCALES = [64, 256, 2048, 8192, 32768]
SEPARATIONS = [61, 303, 1597, 8195]

_GLOBAL_ANCHOR_SET: set[int] = set()
_GLOBAL_SCALE = 0
_GLOBAL_NEXT_SCALE = 0
_GLOBAL_STATE: set[int] = set()


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is defined only for positive integers")
    return (value & -value).bit_length() - 1


def three_translate_raw(anchor_set: set[int], separation: int) -> set[int]:
    return (
        anchor_set
        | {value + separation for value in anchor_set}
        | {value + 2 * separation for value in anchor_set}
    )


def first_4ap_bits(values: set[int]) -> tuple[int, int] | None:
    """Return one 4-AP witness using Python's arbitrary-precision bitsets."""

    bits = 0
    maximum = max(values)
    for value in values:
        bits |= 1 << value

    for step in range(1, maximum // 3 + 1):
        starts = bits & (bits >> step) & (bits >> (2 * step)) & (bits >> (3 * step))
        if starts:
            least_bit = starts & -starts
            first = least_bit.bit_length() - 1
            return first, step
    return None


def build_certified_states() -> list[set[int]]:
    states = [{SCALES[0] + value for value in H}]
    for index, separation in enumerate(SEPARATIONS):
        state = states[-1]
        raw = three_translate_raw({0} | state, separation)
        next_scale = SCALES[index + 1]
        states.append({next_scale + value for value in raw})
    return states


def initialize_worker(state: set[int], scale: int, next_scale: int) -> None:
    global _GLOBAL_ANCHOR_SET, _GLOBAL_SCALE, _GLOBAL_NEXT_SCALE, _GLOBAL_STATE
    _GLOBAL_STATE = state
    _GLOBAL_ANCHOR_SET = {0} | state
    _GLOBAL_SCALE = scale
    _GLOBAL_NEXT_SCALE = next_scale


def check_candidate(separation: int) -> dict[str, int | bool] | None:
    if separation <= 0 or v2(separation) % 2:
        return None

    raw = three_translate_raw(_GLOBAL_ANCHOR_SET, separation)
    if max(raw) >= _GLOBAL_NEXT_SCALE:
        return None
    if len(raw) != 3 * len(_GLOBAL_ANCHOR_SET):
        return None
    if first_4ap_bits(raw) is not None:
        return None

    backbone = {
        value
        for value in raw
        if _GLOBAL_SCALE <= value < 2 * _GLOBAL_SCALE
    }
    if not _GLOBAL_STATE <= backbone:
        return None

    return {
        "separation": separation,
        "maximum_raw": max(raw),
        "raw_size": len(raw),
        "backbone_size": len(backbone),
        "contamination": len(backbone - _GLOBAL_STATE),
        "contains_replay_state": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--state-depth",
        type=int,
        default=5,
        choices=range(1, 6),
        help="certified state S_h to extend",
    )
    parser.add_argument(
        "--factor",
        type=int,
        default=4,
        choices=(2, 4, 8, 16, 32),
        help="requested dyadic scale factor",
    )
    parser.add_argument("--start-r", type=int, default=1)
    parser.add_argument(
        "--end-r",
        type=int,
        default=None,
        help="inclusive end of the candidate range",
    )
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=8)
    args = parser.parse_args()

    states = build_certified_states()
    index = args.state_depth - 1
    state = states[index]
    scale = SCALES[index]
    next_scale = args.factor * scale

    maximum_r = (next_scale - 1 - max(state)) // 2
    start_r = max(1, args.start_r)
    end_r = maximum_r if args.end_r is None else min(args.end_r, maximum_r)

    if end_r < start_r:
        raise ValueError("empty candidate range")
    if args.workers < 1:
        raise ValueError("workers must be positive")

    candidates = range(start_r, end_r + 1)
    results: list[dict[str, int | bool]] = []

    if args.workers == 1:
        initialize_worker(state, scale, next_scale)
        for separation in candidates:
            result = check_candidate(separation)
            if result is not None:
                results.append(result)
    else:
        with Pool(
            processes=args.workers,
            initializer=initialize_worker,
            initargs=(state, scale, next_scale),
        ) as pool:
            for result in pool.imap_unordered(
                check_candidate,
                candidates,
                chunksize=args.chunksize,
            ):
                if result is not None:
                    results.append(result)

    results.sort(key=lambda item: int(item["separation"]))

    summary = {
        "state_depth": args.state_depth,
        "state_scale": scale,
        "state_size": len(state),
        "requested_factor": args.factor,
        "next_scale": next_scale,
        "start_r": start_r,
        "end_r": end_r,
        "maximum_r": maximum_r,
        "valid_count": len(results),
    }
    print(json.dumps(summary, sort_keys=True))
    for result in results:
        print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
