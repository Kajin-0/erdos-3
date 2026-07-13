#!/usr/bin/env python3
"""Verify a parent-intrinsic forced-fork reserve on S1 through S7.

A coordinated deletion action is a three-term progression together with its
valuation-determined side sponsor. Call an initial progression root-forced
when its own action is the only initial deletion action whose sponsor lies in
that progression. Such a progression must be selected in every complete
coordinated deletion schedule: no other action can delete any of its points,
and later actions are a subset of the initial action family.

Grouping forced centers by step gives a schedule-independent lower bound on
total middle-fiber occurrence mass. The actual minimum center for a step may
come from an additional selected progression, so the verifier minimizes the
forced-center contribution over every initially possible center that could be
the minimum.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import sys

from certified_contaminated_states import state_by_depth, v2


EXPECTED = {
    1: {
        "ap_count": 9,
        "forced_count": 3,
        "forced_hash": "a0f1df3d11a8c1e6c8f98777418b5986c28a56f2e099fb103f51890fd719614c",
        "reserve": Fraction(1, 21),
        "threshold": Fraction(1, 21),
    },
    2: {
        "ap_count": 60,
        "forced_count": 5,
        "forced_hash": "7a275371cb8c1fb5fcd7e94a6c5145be835dcc4943e6c61e8b5d8937f8138a86",
        "reserve": Fraction(388668, 6990295),
        "threshold": Fraction(1, 18),
    },
    3: {
        "ap_count": 398,
        "forced_count": 9,
        "forced_hash": "09a93de6b3c86c6aee216c76a9ac489bd256e1dc5c04422e02da1d9bb9c68413",
        "reserve": Fraction(
            3364354489728494,
            168888762232172073,
        ),
        "threshold": Fraction(1, 51),
    },
    4: {
        "ap_count": 2195,
        "forced_count": 12,
        "forced_hash": "3f446816f1ab35e9f371414574af7faea8da4d7260d9742dbc5c1dbeaf782e0b",
        "reserve": Fraction(
            16247372897720390023737791,
            3235490759356665773610042000,
        ),
        "threshold": Fraction(1, 200),
    },
    5: {
        "ap_count": 11523,
        "forced_count": 19,
        "forced_hash": "de917fddb0044b054d762fd3e306cb8c23ebbad0239758c5a0d04369a37ead9c",
        "reserve": Fraction(
            15118361448154886467381751180403762551053086996176904193,
            9431956663304181282890330139658074870057520957610192175360,
        ),
        "threshold": Fraction(1, 624),
    },
    6: {
        "ap_count": 58708,
        "forced_count": 28,
        "forced_hash": "291806f4073029e6bb9194a42bf340217ce82e04506e5672e43e7482f83a901c",
        "reserve": Fraction(
            72927585120114691645881545095408220787760209489844521666259327235001462238082974118882821843014355712779,
            315050216918349325683496052502255571801041014957096556132652517258526878906743888867632851086308157420365600,
        ),
        "threshold": Fraction(1, 4321),
    },
    7: {
        "ap_count": 298606,
        "forced_count": 30,
        "forced_hash": "2afe3bf42d737815373302ce96288409cdef1006b999599cd7c94e539c114603",
        "reserve": Fraction(
            380161902333591535614959106854876974456494762154263187995296453435746094287074983814406561824653196721345794489530148770179141,
            5339753166754465985469934238319549987047765207625174804243333772791056153934196938947676405890983677259924675650702594542699072280,
        ),
        "threshold": Fraction(1, 14046),
    },
}


Action = tuple[int, int, int, int, int]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def all_actions(values: Iterable[int]) -> tuple[Action, ...]:
    ordered = sorted(set(values))
    value_set = set(ordered)
    maximum = ordered[-1]
    result: list[Action] = []
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            right = middle + step
            if right > maximum:
                break
            if right not in value_set:
                continue
            sponsor = left if v2(step) % 2 == 0 else right
            result.append((left, middle, right, step, sponsor))
    return tuple(result)


def canonical_action_hash(actions: Iterable[Action]) -> str:
    payload = "\n".join(
        f"{left},{middle},{right},{step},{sponsor}"
        for left, middle, right, step, sponsor in sorted(actions)
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def forced_actions(actions: tuple[Action, ...]) -> tuple[Action, ...]:
    deleting_actions: dict[int, set[int]] = defaultdict(set)
    for index, action in enumerate(actions):
        deleting_actions[action[4]].add(index)

    result: list[Action] = []
    for index, action in enumerate(actions):
        left, middle, right, _step, _sponsor = action
        actions_hitting_progression = (
            deleting_actions[left]
            | deleting_actions[middle]
            | deleting_actions[right]
        )
        if actions_hitting_progression == {index}:
            result.append(action)
    return tuple(result)


def forced_center_lower_bound(
    actions: tuple[Action, ...],
    forced: tuple[Action, ...],
) -> tuple[Fraction, dict[int, tuple[Fraction, int | None]]]:
    possible_centers: dict[int, set[int]] = defaultdict(set)
    forced_centers: dict[int, set[int]] = defaultdict(set)

    for _left, middle, _right, step, _sponsor in actions:
        possible_centers[step].add(middle)
    for _left, middle, _right, step, _sponsor in forced:
        forced_centers[step].add(middle)

    per_step: dict[int, tuple[Fraction, int | None]] = {}
    total = Fraction(0)

    for step in sorted(forced_centers):
        centers = forced_centers[step]
        if len(centers) < 2:
            per_step[step] = (Fraction(0), None)
            continue

        smallest_forced = min(centers)
        candidates = sorted(
            center
            for center in possible_centers[step]
            if center <= smallest_forced
        )
        if not candidates:
            raise AssertionError("missing possible minimum center")

        choices: list[tuple[Fraction, int]] = []
        for minimum in candidates:
            contribution = sum(
                (
                    Fraction(1, center - minimum)
                    for center in centers
                    if center > minimum
                ),
                Fraction(0),
            )
            choices.append((contribution, minimum))

        best = min(choices)
        per_step[step] = best
        total += best[0]

    return total, per_step


def verify() -> str:
    lines = [
        "verified: root-forced coordinated actions on S1 through S7",
        "verified: parent-intrinsic lower bounds for middle-fiber occurrence mass",
    ]

    for depth in range(1, 8):
        state = state_by_depth(depth)
        actions = all_actions(state.values)
        forced = forced_actions(actions)
        reserve, per_step = forced_center_lower_bound(actions, forced)
        expected = EXPECTED[depth]

        if len(actions) != expected["ap_count"]:
            raise AssertionError(f"S{depth}: action count mismatch")
        if len(forced) != expected["forced_count"]:
            raise AssertionError(f"S{depth}: forced action count mismatch")
        if canonical_action_hash(forced) != expected["forced_hash"]:
            raise AssertionError(f"S{depth}: forced action hash mismatch")
        if reserve != expected["reserve"]:
            raise AssertionError(f"S{depth}: reserve mismatch")
        if reserve < expected["threshold"]:
            raise AssertionError(f"S{depth}: threshold failure")

        detail = ";".join(
            (
                f"q={step}:lower={fraction_text(value)},"
                f"min={'none' if minimum is None else minimum}"
            )
            for step, (value, minimum) in sorted(per_step.items())
        )
        lines.append(
            f"S{depth}:actions={len(actions)},forced={len(forced)},"
            f"reserve={fraction_text(reserve)},"
            f"threshold={fraction_text(expected['threshold'])},"
            f"forced_sha256={expected['forced_hash']},"
            f"per_step={detail}"
        )

    lines.extend(
        [
            (
                "conclusion: every complete coordinated schedule on each "
                "recorded state S1 through S7 has total middle-fiber "
                "occurrence mass at least the listed parent-intrinsic reserve."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_forced_fork_reserve_s1_s7.py [OUTPUT]"
        )
    certificate = verify()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: forced-fork reserve on S1 through S7")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
