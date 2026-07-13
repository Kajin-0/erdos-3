#!/usr/bin/env python3
"""Canonical reconstruction of the recorded contaminated-backbone states.

The module centralizes the constants that were previously repeated across
multiple finite verifiers. It reconstructs the certified path S_1,...,S_10
without asserting that the path represents the full continuation tree.

Exact harmonic certificates at later depths can have numerators and
denominators containing more than Python's default 4,300 decimal digits. The
repository intentionally permits those exact integer strings.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable
import sys


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


BASE_PATTERN = frozenset(
    {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
)

SCALES = (
    64,
    256,
    2_048,
    8_192,
    32_768,
    262_144,
    1_048_576,
    8_388_608,
    67_108_864,
    536_870_912,
)

SEPARATIONS = (
    61,
    303,
    1_597,
    8_195,
    93_476,
    230_164,
    2_097_164,
    16_777_217,
    134_217_729,
)

EXPECTED_SIZES = (
    12,
    39,
    120,
    363,
    1_092,
    3_279,
    9_840,
    29_523,
    88_572,
    265_719,
)

EXPECTED_MAXIMA = (
    92,
    470,
    3_124,
    14_510,
    63_668,
    512_764,
    2_021_668,
    14_604_604,
    115_267_902,
    920_574_272,
)

EXPECTED_INCOMING_CONTAMINATION = (
    0,
    4,
    1,
    33,
    1,
    0,
    2,
    0,
    0,
    0,
)


@dataclass(frozen=True)
class CertifiedState:
    depth: int
    scale: int
    persistence: int
    values: frozenset[int]
    incoming_factor: int | None
    incoming_separation: int | None
    incoming_contamination: int

    @property
    def size(self) -> int:
        return len(self.values)

    @property
    def maximum(self) -> int:
        return max(self.values)

    @property
    def weighted_density(self) -> Fraction:
        return Fraction(self.persistence * self.size, self.scale)

    @property
    def right_shell_slack(self) -> Fraction:
        points = 2 * self.scale - 1 - self.maximum
        return Fraction(self.persistence * points, self.scale)

    @property
    def incoming_contamination_mass(self) -> Fraction:
        return Fraction(
            self.persistence * self.incoming_contamination,
            self.scale,
        )


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def three_translate_raw(
    state: Iterable[int],
    separation: int,
) -> frozenset[int]:
    if separation <= 0:
        raise ValueError("separation must be positive")
    anchor = {0} | set(state)
    return frozenset(
        value + layer * separation
        for value in anchor
        for layer in range(3)
    )


def backbone_contamination(
    parent: Iterable[int],
    scale: int,
    generated: Iterable[int],
) -> int:
    parent_set = set(parent)
    backbone = {
        value
        for value in generated
        if scale <= value < 2 * scale
    }
    if not parent_set <= backbone:
        raise ValueError("generated backbone does not contain parent state")
    return len(backbone - parent_set)


def build_certified_states() -> tuple[CertifiedState, ...]:
    current = frozenset(64 + value for value in BASE_PATTERN)
    states: list[CertifiedState] = [
        CertifiedState(
            depth=1,
            scale=SCALES[0],
            persistence=2,
            values=current,
            incoming_factor=None,
            incoming_separation=None,
            incoming_contamination=0,
        )
    ]

    for index, separation in enumerate(SEPARATIONS):
        parent = states[-1]
        next_scale = SCALES[index + 1]
        factor = next_scale // parent.scale
        generated = three_translate_raw(parent.values, separation)
        contamination = backbone_contamination(
            parent.values,
            parent.scale,
            generated,
        )
        current = frozenset(next_scale + value for value in generated)
        states.append(
            CertifiedState(
                depth=index + 2,
                scale=next_scale,
                persistence=2 * parent.persistence,
                values=current,
                incoming_factor=factor,
                incoming_separation=separation,
                incoming_contamination=contamination,
            )
        )

    verify_certified_states(tuple(states))
    return tuple(states)


def verify_certified_states(states: tuple[CertifiedState, ...]) -> None:
    if len(states) != 10:
        raise AssertionError("expected ten recorded states")
    for index, state in enumerate(states):
        if state.depth != index + 1:
            raise AssertionError("depth mismatch")
        if state.scale != SCALES[index]:
            raise AssertionError(f"scale mismatch at depth {state.depth}")
        if state.size != EXPECTED_SIZES[index]:
            raise AssertionError(f"size mismatch at depth {state.depth}")
        if min(state.values) != state.scale:
            raise AssertionError(f"minimum mismatch at depth {state.depth}")
        if state.maximum != EXPECTED_MAXIMA[index]:
            raise AssertionError(f"maximum mismatch at depth {state.depth}")
        if not all(
            state.scale <= value < 2 * state.scale
            for value in state.values
        ):
            raise AssertionError(f"shell mismatch at depth {state.depth}")
        if (
            state.incoming_contamination
            != EXPECTED_INCOMING_CONTAMINATION[index]
        ):
            raise AssertionError(
                f"contamination mismatch at depth {state.depth}"
            )


def state_by_depth(depth: int) -> CertifiedState:
    if not 1 <= depth <= 10:
        raise ValueError("depth must lie in [1,10]")
    return build_certified_states()[depth - 1]


if __name__ == "__main__":
    for state in build_certified_states():
        factor = (
            "base"
            if state.incoming_factor is None
            else state.incoming_factor
        )
        print(
            f"S{state.depth}: L={state.scale} N={state.size} "
            f"max={state.maximum} incoming_factor={factor} "
            f"contamination={state.incoming_contamination}"
        )
