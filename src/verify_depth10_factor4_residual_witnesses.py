#!/usr/bin/env python3
"""Verify explicit 4-AP witnesses for the final 893 S10 factor-four candidates."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

FNV_OFFSET = 1469598103934665603
FNV_PRIME = 1099511628211
EXPECTED_RESIDUAL_FNV = 0x843F253A7C74453C
EXPECTED_WITNESS_FNV = 0x95DA837E14FE741A
EXPECTED_WITNESS_SHA256 = "5c78595c28ddb36f484cc0afc5217d2a3b737782cbc0672b1255934b4cb85571"


def fnv64(data: bytes) -> int:
    value = FNV_OFFSET
    for byte in data:
        value ^= byte
        value = (value * FNV_PRIME) & ((1 << 64) - 1)
    return value


def fnv_values(values: list[int]) -> int:
    return fnv64("".join(f"{value}," for value in values).encode())


def raw(state: set[int], separation: int) -> set[int]:
    anchor = {0} | state
    return anchor | {x + separation for x in anchor} | {
        x + 2 * separation for x in anchor
    }


def build_s10() -> set[int]:
    state = {64 + x for x in {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}}
    for scale, separation in (
        (256, 61),
        (2048, 303),
        (8192, 1597),
        (32768, 8195),
        (262144, 93476),
        (1048576, 230164),
        (8388608, 2097164),
        (67108864, 16777217),
        (536870912, 134217729),
    ):
        state = {scale + x for x in raw(state, separation)}
    return state


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: verify_depth10_factor4_residual_witnesses.py "
            "RESIDUAL_LIST WITNESS_FILE"
        )

    residual_path = Path(sys.argv[1])
    witness_path = Path(sys.argv[2])
    residual = [int(line) for line in residual_path.read_text().split()]
    if (
        len(residual) != 893
        or residual[0] != 97530521
        or residual[-1] != 613340173
        or fnv_values(residual) != EXPECTED_RESIDUAL_FNV
    ):
        raise AssertionError("residual list mismatch")

    witness_bytes = witness_path.read_bytes()
    if fnv64(witness_bytes) != EXPECTED_WITNESS_FNV:
        raise AssertionError("witness FNV-64 mismatch")
    if hashlib.sha256(witness_bytes).hexdigest() != EXPECTED_WITNESS_SHA256:
        raise AssertionError("witness SHA-256 mismatch")

    records: dict[int, tuple[tuple[int, int, int, int], str]] = {}
    class_counts: dict[str, int] = {}
    for line in witness_bytes.decode().splitlines():
        fields = line.split()
        if len(fields) != 6:
            raise AssertionError(f"invalid witness row: {line}")
        separation = int(fields[0])
        progression = tuple(map(int, fields[1:5]))
        witness_class = fields[5]
        if separation in records:
            raise AssertionError(f"duplicate witness for R={separation}")
        records[separation] = (progression, witness_class)
        class_counts[witness_class] = class_counts.get(witness_class, 0) + 1

    if sorted(records) != residual:
        raise AssertionError("witness keys do not equal the residual list")
    if class_counts != {
        "rectangle": 821,
        "anchor_completion": 50,
        "terminal_full": 22,
    }:
        raise AssertionError(f"unexpected witness class counts: {class_counts}")

    state = build_s10()
    if len(state) != 265719 or min(state) != 536870912 or max(state) != 920574272:
        raise AssertionError("S10 reconstruction mismatch")
    anchor = {0} | state

    for separation in residual:
        progression, _ = records[separation]
        first, second, third, fourth = progression
        difference = second - first
        if (
            difference <= 0
            or third - second != difference
            or fourth - third != difference
        ):
            raise AssertionError(f"not a nontrivial 4-AP for R={separation}")
        for point in progression:
            if not (
                point in anchor
                or point - separation in anchor
                or point - 2 * separation in anchor
            ):
                raise AssertionError(
                    f"witness point {point} absent from candidate R={separation}"
                )

    print("verified: explicit witnesses for all 893 terminal structural candidates")
    print("rectangle_witnesses=821")
    print("anchor_completion_witnesses=50")
    print("full_parent_terminal_witnesses=22")
    print("witness_fnv64=95da837e14fe741a")
    print(f"witness_sha256={EXPECTED_WITNESS_SHA256}")
    print("N_10_4=0")


if __name__ == "__main__":
    main()
