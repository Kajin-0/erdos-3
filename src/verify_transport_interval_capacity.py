#!/usr/bin/env python3
"""Exact interval-capacity diagnostics for four-ratio rectangle transport.

This script isolates the state-independent integer geometry behind the
S_10 factor-four closure. It verifies:

1. exact transport windows [kS-U, kS+U] for k=1,2,3,4;
2. the integer coalescence threshold 2U+1 >= S;
3. an exact finite formula for the radius required to cover a target interval;
4. the recorded S_10 residual closure margin.

No external packages are required.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import sys


Interval = tuple[int, int]


@dataclass(frozen=True)
class CoverageDiagnostic:
    separation: int
    available_radius: int
    target_low: int
    target_high: int
    ratios: tuple[int, ...]
    windows: tuple[Interval, ...]
    merged_windows: tuple[Interval, ...]
    required_radius: int
    covered_target_points: int
    target_points: int

    @property
    def margin(self) -> int:
        return self.available_radius - self.required_radius

    @property
    def uncovered_target_points(self) -> int:
        return self.target_points - self.covered_target_points


def integer_windows(
    separation: int,
    radius: int,
    ratios: tuple[int, ...],
) -> tuple[Interval, ...]:
    if separation <= 0:
        raise ValueError("separation must be positive")
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    if not ratios or any(k <= 0 for k in ratios):
        raise ValueError("ratios must be positive")
    return tuple(
        (k * separation - radius, k * separation + radius)
        for k in ratios
    )


def merge_integer_intervals(
    intervals: tuple[Interval, ...],
) -> tuple[Interval, ...]:
    if not intervals:
        return ()
    ordered = sorted(intervals)
    merged: list[list[int]] = [[ordered[0][0], ordered[0][1]]]
    for low, high in ordered[1:]:
        if low > high:
            raise ValueError("invalid interval")
        if low <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], high)
        else:
            merged.append([low, high])
    return tuple((low, high) for low, high in merged)


def interval_size(interval: Interval) -> int:
    low, high = interval
    return max(0, high - low + 1)


def intersection_size(left: Interval, right: Interval) -> int:
    return interval_size(
        (max(left[0], right[0]), min(left[1], right[1]))
    )


def covered_points(
    target: Interval,
    merged_windows: tuple[Interval, ...],
) -> int:
    return sum(
        intersection_size(target, interval)
        for interval in merged_windows
    )


def nearest_center_distance(
    point: int,
    centers: tuple[int, ...],
) -> int:
    return min(abs(point - center) for center in centers)


def required_radius_for_interval(
    target: Interval,
    separation: int,
    ratios: tuple[int, ...],
) -> int:
    """Return max_{T in target} min_k |T-kS| exactly.

    Distance to a finite ordered set of centers is piecewise linear on the
    integer line. Its maximum on an interval occurs at an endpoint or at an
    integer adjacent to a midpoint between consecutive centers.
    """

    low, high = target
    if low > high:
        raise ValueError("target interval must be nonempty")
    centers = tuple(sorted(k * separation for k in ratios))
    candidates = {low, high}
    for left, right in zip(centers, centers[1:]):
        floor_mid = (left + right) // 2
        ceil_mid = (left + right + 1) // 2
        for point in (floor_mid, ceil_mid):
            if low <= point <= high:
                candidates.add(point)
    return max(
        nearest_center_distance(point, centers)
        for point in candidates
    )


def pure_layer_witness(ratio: int) -> tuple[int, int]:
    layer_sumset = {
        i + ratio * j
        for i in range(3)
        for j in range(3)
    }
    for start in sorted(layer_sumset):
        for step in range(1, max(layer_sumset) + 1):
            if all(
                start + index * step in layer_sumset
                for index in range(4)
            ):
                return start, step
    raise AssertionError(
        f"no pure-layer four-term progression for ratio {ratio}"
    )


def diagnose(
    separation: int,
    available_radius: int,
    target: Interval,
    ratios: tuple[int, ...] = (1, 2, 3, 4),
) -> CoverageDiagnostic:
    windows = integer_windows(separation, available_radius, ratios)
    merged = merge_integer_intervals(windows)
    required = required_radius_for_interval(
        target,
        separation,
        ratios,
    )
    target_count = interval_size(target)
    covered = covered_points(target, merged)
    return CoverageDiagnostic(
        separation=separation,
        available_radius=available_radius,
        target_low=target[0],
        target_high=target[1],
        ratios=ratios,
        windows=windows,
        merged_windows=merged,
        required_radius=required,
        covered_target_points=covered,
        target_points=target_count,
    )


def verify_small_boxes() -> None:
    ratios = (1, 2, 3, 4)
    for separation in range(1, 26):
        centers = tuple(k * separation for k in ratios)
        for radius in range(0, 2 * separation + 1):
            windows = integer_windows(separation, radius, ratios)
            merged = merge_integer_intervals(windows)
            direct = {
                point
                for point in range(-separation, 6 * separation + 1)
                if any(
                    abs(point - center) <= radius
                    for center in centers
                )
            }
            reconstructed = {
                point
                for low, high in merged
                for point in range(
                    max(low, -separation),
                    min(high, 6 * separation) + 1,
                )
            }
            assert direct == reconstructed

        for low in range(-separation, 5 * separation + 1):
            for high in range(
                low,
                min(5 * separation, low + separation) + 1,
            ):
                exact = required_radius_for_interval(
                    (low, high),
                    separation,
                    ratios,
                )
                brute = max(
                    nearest_center_distance(point, centers)
                    for point in range(low, high + 1)
                )
                assert exact == brute


def build_certificate() -> str:
    verify_small_boxes()

    ratios = (1, 2, 3, 4)
    for ratio in ratios:
        pure_layer_witness(ratio)

    separation = 134_217_729
    available_radius = 76_583_776
    target = (97_474_324, 613_454_687)
    result = diagnose(
        separation,
        available_radius,
        target,
        ratios,
    )

    integer_overlap_threshold = (separation - 1) // 2
    assert 2 * integer_overlap_threshold + 1 >= separation
    assert result.available_radius >= integer_overlap_threshold
    assert result.merged_windows == ((57_633_953, 613_454_692),)
    assert result.required_radius == 76_583_771
    assert result.margin == 5
    assert result.uncovered_target_points == 0
    assert result.covered_target_points == 515_980_364

    lines = [
        "FOUR-RATIO TRANSPORT INTERVAL CAPACITY",
        "",
        "state_independent_checks=verified",
        "ratios=1,2,3,4",
        "integer_coalescence_condition=2U+1>=S",
        "target_radius_formula=max_{T in I} min_k |T-kS|",
        "pure_layer_boundary_witnesses=verified",
        "",
        f"S={separation}",
        f"available_radius={available_radius}",
        (
            "normalized_available_radius="
            f"{Fraction(available_radius, separation)}"
        ),
        f"integer_overlap_threshold={integer_overlap_threshold}",
        (
            "overlap_excess="
            f"{available_radius - integer_overlap_threshold}"
        ),
        f"target_interval={target[0]},{target[1]}",
        f"target_points={result.target_points}",
        f"required_radius={result.required_radius}",
        (
            "normalized_required_radius="
            f"{Fraction(result.required_radius, separation)}"
        ),
        f"closure_margin={result.margin}",
        f"covered_target_points={result.covered_target_points}",
        f"uncovered_target_points={result.uncovered_target_points}",
        "windows:",
    ]
    for ratio, interval in zip(ratios, result.windows):
        lines.append(
            f"  k={ratio} {interval[0]} {interval[1]}"
        )
    lines.extend(
        [
            "merged_windows:",
            *[
                f"  {low} {high}"
                for low, high in result.merged_windows
            ],
            "",
            (
                "conclusion: the recorded B9 direct-support radius "
                "exceeds the exact"
            ),
            (
                "radius required to cover the complete S10 "
                "factor-four residual by 5."
            ),
            (
                "The large overlap excess does not imply a large "
                "endpoint margin."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_transport_interval_capacity.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(
            certificate,
            encoding="utf-8",
        )
    digest = hashlib.sha256(certificate.encode()).hexdigest()
    print(
        "verified: exact four-ratio transport interval capacity"
    )
    print("S10_required_radius=76583771")
    print("S10_available_radius=76583776")
    print("S10_closure_margin=5")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
