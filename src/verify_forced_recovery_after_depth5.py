#!/usr/bin/env python3
"""Verify the finite forced-recovery result after the depth-five burst.

The certified contaminated-backbone chain ends at a 1092-point state S5 in the
standard dyadic shell [32768,65536). This program verifies:

1. the recorded S5 hash;
2. no sponsor-compatible disjoint three-translate continuation fits at dyadic
   scale factor 2 or 4 while remaining four-term-progression-free;
3. R=65547 gives an exact-backbone factor-8 recovery and is the first valid
   sponsor-compatible exact-backbone separation;
4. the resulting 3279-point state S6 has the recorded hash;
5. no sponsor-compatible disjoint continuation of S6 works at factor 2 or 4.

The negative searches are chunkable. The default ``quick`` mode checks the
state hashes and selected recovery only. Use ``--mode all`` for every recorded
negative search, or one of ``s5-cheap`` and ``s6-cheap``. Range arguments allow
independent distributed reproduction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from multiprocessing import Pool
from typing import Iterable

H = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
SCALES = [64, 256, 2048, 8192, 32768]
SEPARATIONS = [61, 303, 1597, 8195]
RECOVERY_SEPARATION = 65547
RECOVERY_SCALE = 262144

EXPECTED_S5_HASH = "a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841"
EXPECTED_RECOVERY_RAW_HASH = "fd54f32a858cf81b0236aa992447d99d91710193623948cb23ecf77466a2660c"
EXPECTED_S6_HASH = "ff10f8482f475206eba84c4cbbcef48ec0402ec1870edf81575495b9aae7d463"

EXPECTED_DOMAINS = {
    (5, 2): (933, 622, 0),
    (5, 4): (33701, 22467, 0),
    (6, 2): (33690, 22459, 0),
    (6, 4): (295834, 197222, 0),
}

_GLOBAL_STATE: set[int] = set()
_GLOBAL_ANCHOR_SET: set[int] = set()
_GLOBAL_SCALE = 0
_GLOBAL_NEXT_SCALE = 0


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is defined only for positive integers")
    return (value & -value).bit_length() - 1


def state_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def three_translate_raw(anchor_set: set[int], separation: int) -> set[int]:
    return (
        anchor_set
        | {value + separation for value in anchor_set}
        | {value + 2 * separation for value in anchor_set}
    )


def first_4ap_bits(values: set[int]) -> tuple[int, int] | None:
    """Return one four-term progression using an arbitrary-precision bitset."""
    bits = 0
    maximum = max(values)
    for value in values:
        bits |= 1 << value

    for step in range(1, maximum // 3 + 1):
        starts = bits & (bits >> step) & (bits >> (2 * step)) & (bits >> (3 * step))
        if starts:
            least_bit = starts & -starts
            return least_bit.bit_length() - 1, step
    return None


def build_s5() -> set[int]:
    state = {SCALES[0] + value for value in H}
    for index, separation in enumerate(SEPARATIONS):
        raw = three_translate_raw({0} | state, separation)
        state = {SCALES[index + 1] + value for value in raw}
    return state


def build_s6(s5: set[int]) -> tuple[set[int], set[int]]:
    raw = three_translate_raw({0} | s5, RECOVERY_SEPARATION)
    return raw, {RECOVERY_SCALE + value for value in raw}


def initialize_worker(state: set[int], scale: int, next_scale: int) -> None:
    global _GLOBAL_STATE, _GLOBAL_ANCHOR_SET, _GLOBAL_SCALE, _GLOBAL_NEXT_SCALE
    _GLOBAL_STATE = state
    _GLOBAL_ANCHOR_SET = {0} | state
    _GLOBAL_SCALE = scale
    _GLOBAL_NEXT_SCALE = next_scale


def check_candidate(separation: int) -> dict[str, int] | None:
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
        "backbone_size": len(backbone),
        "contamination": len(backbone - _GLOBAL_STATE),
    }


def candidate_domain(state: set[int], scale: int, factor: int) -> tuple[int, list[int]]:
    next_scale = factor * scale
    maximum_r = (next_scale - 1 - max(state)) // 2
    candidates = [
        separation
        for separation in range(1, maximum_r + 1)
        if v2(separation) % 2 == 0
    ]
    return maximum_r, candidates


def scan(
    state: set[int],
    scale: int,
    factor: int,
    workers: int,
    start_r: int | None,
    end_r: int | None,
) -> dict[str, object]:
    maximum_r, full_candidates = candidate_domain(state, scale, factor)
    lower = 1 if start_r is None else max(1, start_r)
    upper = maximum_r if end_r is None else min(maximum_r, end_r)
    candidates = [value for value in full_candidates if lower <= value <= upper]

    if not candidates:
        raise ValueError("empty candidate range")

    next_scale = factor * scale
    valid: list[dict[str, int]] = []
    if workers == 1:
        initialize_worker(state, scale, next_scale)
        for separation in candidates:
            result = check_candidate(separation)
            if result is not None:
                valid.append(result)
    else:
        with Pool(
            processes=workers,
            initializer=initialize_worker,
            initargs=(state, scale, next_scale),
        ) as pool:
            for result in pool.imap_unordered(check_candidate, candidates, chunksize=1):
                if result is not None:
                    valid.append(result)

    valid.sort(key=lambda item: item["separation"])
    full_range = lower == 1 and upper == maximum_r
    summary: dict[str, object] = {
        "scale": scale,
        "state_size": len(state),
        "factor": factor,
        "next_scale": next_scale,
        "maximum_r": maximum_r,
        "start_r": lower,
        "end_r": upper,
        "candidate_count": len(candidates),
        "valid_count": len(valid),
        "full_range": full_range,
        "valid": valid,
    }
    return summary


def verify_quick() -> tuple[set[int], set[int]]:
    s5 = build_s5()
    if len(s5) != 1092 or min(s5) != 32768 or max(s5) != 63668:
        raise AssertionError("unexpected S5 geometry")
    if state_hash(s5) != EXPECTED_S5_HASH:
        raise AssertionError("S5 hash mismatch")
    if first_4ap_bits(s5) is not None:
        raise AssertionError("S5 contains a four-term progression")

    # Exact backbone recovery requires R>=2L. Check every sponsor-compatible
    # candidate from 2L through the recorded first valid value.
    first_exact: int | None = None
    for separation in range(2 * 32768, RECOVERY_SEPARATION + 1):
        if v2(separation) % 2:
            continue
        raw = three_translate_raw({0} | s5, separation)
        if len(raw) != 3 * (len(s5) + 1):
            continue
        if max(raw) >= RECOVERY_SCALE:
            continue
        if first_4ap_bits(raw) is not None:
            continue
        backbone = {value for value in raw if 32768 <= value < 65536}
        if backbone == s5:
            first_exact = separation
            break

    if first_exact != RECOVERY_SEPARATION:
        raise AssertionError(f"unexpected first exact recovery: {first_exact}")

    recovery_raw, s6 = build_s6(s5)
    if state_hash(recovery_raw) != EXPECTED_RECOVERY_RAW_HASH:
        raise AssertionError("recovery raw-state hash mismatch")
    if len(s6) != 3279 or min(s6) != 262144 or max(s6) != 456906:
        raise AssertionError("unexpected S6 geometry")
    if state_hash(s6) != EXPECTED_S6_HASH:
        raise AssertionError("S6 hash mismatch")
    if first_4ap_bits(recovery_raw) is not None or first_4ap_bits(s6) is not None:
        raise AssertionError("selected factor-eight recovery is not four-term-progression-free")

    backbone = {value for value in recovery_raw if 32768 <= value < 65536}
    if backbone != s5:
        raise AssertionError("selected recovery is not exact-backbone")

    return s5, s6


def verify_full_summary(depth: int, factor: int, summary: dict[str, object]) -> None:
    expected_maximum, expected_candidates, expected_valid = EXPECTED_DOMAINS[(depth, factor)]
    if not summary["full_range"]:
        return
    if summary["maximum_r"] != expected_maximum:
        raise AssertionError("candidate maximum mismatch")
    if summary["candidate_count"] != expected_candidates:
        raise AssertionError("candidate count mismatch")
    if summary["valid_count"] != expected_valid:
        raise AssertionError("unexpected valid continuation")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("quick", "s5-cheap", "s6-cheap", "all"),
        default="quick",
    )
    parser.add_argument("--workers", type=int, default=max(1, min(8, os.cpu_count() or 1)))
    parser.add_argument("--start-r", type=int, default=None)
    parser.add_argument("--end-r", type=int, default=None)
    args = parser.parse_args()

    if args.workers < 1:
        raise ValueError("workers must be positive")

    s5, s6 = verify_quick()
    print("verified: S5 and selected exact factor-eight recovery")
    print(f"s5_sha256={EXPECTED_S5_HASH}")
    print(f"recovery_separation={RECOVERY_SEPARATION}")
    print(f"recovery_raw_sha256={EXPECTED_RECOVERY_RAW_HASH}")
    print(f"s6_sha256={EXPECTED_S6_HASH}")

    requested: list[tuple[int, set[int], int, int]] = []
    if args.mode in ("s5-cheap", "all"):
        requested.extend([(5, s5, 32768, 2), (5, s5, 32768, 4)])
    if args.mode in ("s6-cheap", "all"):
        requested.extend([(6, s6, 262144, 2), (6, s6, 262144, 4)])

    for depth, state, scale, factor in requested:
        summary = scan(
            state,
            scale,
            factor,
            args.workers,
            args.start_r,
            args.end_r,
        )
        verify_full_summary(depth, factor, summary)
        output = dict(summary)
        output.pop("valid")
        print(json.dumps(output, sort_keys=True))
        for result in summary["valid"]:  # type: ignore[index]
            print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
