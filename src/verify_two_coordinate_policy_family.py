#!/usr/bin/env python3
"""Certify a finite two-coordinate policy family through S7."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import heapq
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import all_three_aps, v2
from verify_s7_policy_transition_tradeoff import fraction_hash, harmonic

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LAMBDA = Fraction(3)
GAMMA = Fraction(1, 10)
REGENERATION_CHARGE = Fraction(36_953, 4_096)
SEED_CENTERS = frozenset({1_354_065, 1_354_070, 1_354_075})

EXPECTED = {
    1: {
        "winners": (
            "lex", "q142", "q161", "q30", "q40", "step5",
            "step540", "step54030",
        ),
        "winner_metrics": (6, 6, 2, 4),
        "gap_hash": "496cf601dff1b45d679d3b660ec70a7a97de1503fbe13272de83a9fa7fb9a830",
        "gap_digits": (2, 3),
        "ranking_hash": "e696cade6992501eb223811188e8a4a4487fd4abc269df75e475106bf5cd7718",
    },
    2: {
        "winners": ("step5", "step540"),
        "winner_metrics": (25, 14, 7, 18),
        "gap_hash": "8e3007fadb7ab81bdbfba7c7d0d2ec8df58cab9cae8022d6894505fe724d0e2f",
        "gap_digits": (4, 3),
        "ranking_hash": "7770b5630cd0d18b0ba85ef69cbd6bcc69ded384415959bf4bc6be007142dac0",
    },
    3: {
        "winners": ("step540",),
        "winner_metrics": (91, 29, 12, 79),
        "gap_hash": "0b5bb33a62e91508584cb485acfc8404bb1039d96d90f958ef88d17891cd7093",
        "gap_digits": (45, 45),
        "ranking_hash": "901939b22a94d6094a341d1d264b28fc5a06147a088a74ff43d5c0d4920765eb",
    },
    4: {
        "winners": ("step540",),
        "winner_metrics": (304, 59, 20, 284),
        "gap_hash": "eaa4e30c87e4b57ec23093a00fc1659b5a4331308ef29e3922d8047ff0f68aff",
        "gap_digits": (157, 157),
        "ranking_hash": "58906c9b741efdf528c469267a6a5d776467e0962c538113676a5389693d0a2b",
    },
    5: {
        "winners": ("step540",),
        "winner_metrics": (974, 118, 25, 949),
        "gap_hash": "76162a3664bc38ba99a78935cc266d759c8a2a5cec3f000ae3c4264d3379669f",
        "gap_digits": (518, 519),
        "ranking_hash": "73b67675e00b71dcf0ddefc1c9ab0f8f9738c793b1fcd508df8f05c056b710a9",
    },
    6: {
        "winners": ("step540",),
        "winner_metrics": (3041, 238, 27, 3014),
        "gap_hash": "895c49c244d9249c103486cd157d81e1e2b6086b14327daf8d18fa06ae60355c",
        "gap_digits": (1995, 1996),
        "ranking_hash": "1b39faf6007085442763a8c484fe3d13f6101fb5db72dd6461c06ee66b9353bc",
    },
    7: {
        "winners": ("hybrid5",),
        "winner_metrics": (9346, 494, 51, 9295),
        "gap_hash": "f7aaa21925e0b9eba07695a3a189d0172914d6f431ff274ff0819b8d817d03f7",
        "gap_digits": (6939, 6940),
        "ranking_hash": "06412c09bcb2ecadb230d2d4cac31df2dde9dc1e446c055695a76a49d47013e3",
    },
}

Q30_INTERACTION = {
    1: (
        "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6", "zero",
        "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6", "zero",
    ),
    2: (
        "ffef01c5535376644bc2c4d9afa2074cbeb230440c53a22820b23c1b364b5d40", "negative",
        "8e3007fadb7ab81bdbfba7c7d0d2ec8df58cab9cae8022d6894505fe724d0e2f", "positive",
    ),
    3: (
        "e2720c5a223e14be1a217fadea9603e523d5e266033c5daeb177d1de63dd2832", "negative",
        "50db2080ecd7cc0601709d82535bce469e34009cb362a13fe554db3451647c96", "positive",
    ),
    4: (
        "047ddba93da8911362eeb976232067499b821900dcf1291dc08e687b8d9bb42c", "negative",
        "9c1b1e26ae664454dc7b8c93469dbc9adaba96ac5e0edf676e98eaf6ca6100f9", "positive",
    ),
    5: (
        "5cf4f0b3c9b0d907b5f8c54682a65cf90137e2f1f6c3ece25299d2d3a4f2ada0", "negative",
        "cd2f388df26aedfe4c959988ba8f9585a834eb63e9f3bb15070637d5fd91ea0b", "positive",
    ),
    6: (
        "8a497c04058da8847044f288ed6cd82d82bc367c84d76c905e552d8611c9d7e9", "negative",
        "84eaaa3c58c52d5f8d11c6ae8cc0b032b3a3f4c7b2ecc45e87ef0293782ae57f", "positive",
    ),
    7: (
        "360c707ebdae2c5a6dad6397fa8aa1fa1626cd5b6f5f036eb89a86e75726e1a6", "negative",
        "686b22c3b7147cfadbd081be93f032b2dda758a26d582b701c1472812a7e46cc", "positive",
    ),
}

GAMMA_STAR_HASH = "bb9f501ef2310889980d046bd98601f768399f593975fc7725ef9ecae9b83a29"
GAMMA_1_16_HASH = "e4f336effcac2abd6d14e22fcf078c6d7eef16624a1199d5657a3e7b75fda2f3"
GAMMA_1_10_HASH = "4345122f1c4143b2ffbf741a6208ae7356d7927ba6abc1d55be0feba0ba41a59"
CERTIFICATE_SHA256 = "bd16d379e78feadcd32efb349302874367183101a32c9178eb439bda576e6e31"

BASE_POLICIES = {
    "lex": (frozenset(), False, False),
    "reverse": (frozenset(), False, True),
    "q30": (frozenset({30}), False, False),
    "q40": (frozenset({40}), False, False),
    "q142": (frozenset({142}), False, False),
    "q161": (frozenset({161}), False, False),
    "step5": (frozenset({5}), False, False),
    "step540": (frozenset({5, 40}), False, False),
    "step54030": (frozenset({5, 40, 30}), False, False),
}
S7_EXTRA_POLICIES = {
    "delayseed": (frozenset(), True, False),
    "hybrid5": (frozenset({5}), True, False),
    "hybrid540": (frozenset({5, 40}), True, False),
    "hybrid54030": (frozenset({5, 40, 30}), True, False),
}


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def sign_text(value: Fraction) -> str:
    if value == 0:
        return "zero"
    return "negative" if value < 0 else "positive"


def resolve_policy(
    depth: int,
    delayed_steps: frozenset[int],
    seed_delay: bool,
    reverse: bool,
) -> tuple[tuple[tuple[int, ...], ...], frozenset[int]]:
    state = state_by_depth(depth)
    progressions = all_three_aps(state.values)
    current = set(state.values)
    queue = []
    for progression in progressions:
        step, left, middle, right = progression
        if reverse:
            priority = tuple(-value for value in progression)
        else:
            delayed = step in delayed_steps or (
                seed_delay
                and depth == 7
                and step == 1
                and middle in SEED_CENTERS
            )
            priority = (delayed, progression)
        queue.append((priority, progression))
    heapq.heapify(queue)

    selected: list[tuple[int, ...]] = []
    while queue:
        _priority, (step, left, middle, right) = heapq.heappop(queue)
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)
    return tuple(selected), frozenset(current)


def middle_fibers(
    selected: tuple[tuple[int, ...], ...],
) -> dict[int, frozenset[int]]:
    centers: dict[int, list[int]] = defaultdict(list)
    for _sponsor, middle, _opposite, step, _left, _right in selected:
        centers[step].append(middle)
    result: dict[int, frozenset[int]] = {}
    for step, values in centers.items():
        ordered = sorted(values)
        minimum = ordered[0]
        result[step] = frozenset(value - minimum for value in ordered[1:])
    return result


def policy_metrics(
    depth: int,
    delayed_steps: frozenset[int],
    seed_delay: bool,
    reverse: bool,
) -> dict[str, object]:
    state = state_by_depth(depth)
    selected, residual = resolve_policy(
        depth, delayed_steps, seed_delay, reverse
    )
    fibers = middle_fibers(selected)
    steps = set(fibers)
    occurrences = [value for values in fibers.values() for value in values]
    seed_shell = tuple(
        sorted(
            value
            for value in fibers.get(1, frozenset())
            if 16 <= value < 32
        )
    )
    return {
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(steps),
        "occurrences": len(occurrences),
        "terminal_mass": harmonic(steps),
        "occurrence_mass": sum(
            (harmonic(values) for values in fibers.values()), Fraction()
        ),
        "residual_error": Fraction(
            state.persistence * len(residual), state.scale
        ),
        "regeneration": depth == 7 and seed_shell == (16, 21, 26),
    }


def score(metrics: dict[str, object], gamma: Fraction = GAMMA) -> Fraction:
    return (
        metrics["terminal_mass"]
        + LAMBDA * metrics["occurrence_mass"]
        + metrics["residual_error"]
        + (
            gamma * REGENERATION_CHARGE
            if metrics["regeneration"]
            else Fraction()
        )
    )


def build_certificate() -> str:
    rows: dict[int, tuple[dict[str, dict[str, object]], dict[str, Fraction]]] = {}

    for depth in range(1, 8):
        policies = dict(BASE_POLICIES)
        if depth == 7:
            policies.update(S7_EXTRA_POLICIES)
        metrics = {
            name: policy_metrics(depth, *arguments)
            for name, arguments in policies.items()
        }
        scores = {name: score(value) for name, value in metrics.items()}
        best = min(scores.values())
        winners = tuple(sorted(name for name, value in scores.items() if value == best))
        distinct_scores = sorted(set(scores.values()))
        minimum_gap = distinct_scores[1] - distinct_scores[0]
        ranking_payload = "".join(
            f"{name}:{fraction_text(scores[name])}\n"
            for name in sorted(scores, key=lambda item: (scores[item], item))
        )
        ranking_hash = hashlib.sha256(ranking_payload.encode("utf-8")).hexdigest()

        expected = EXPECTED[depth]
        if winners != expected["winners"]:
            raise AssertionError(f"S{depth}: winner mismatch {winners!r}")
        winner = metrics[winners[0]]
        compact = (
            winner["selected"],
            winner["residual"],
            winner["terminal_steps"],
            winner["occurrences"],
        )
        if compact != expected["winner_metrics"]:
            raise AssertionError(f"S{depth}: winner metric mismatch")
        if fraction_hash(minimum_gap) != expected["gap_hash"]:
            raise AssertionError(f"S{depth}: minimum-gap hash mismatch")
        if (
            len(str(minimum_gap.numerator)),
            len(str(minimum_gap.denominator)),
        ) != expected["gap_digits"]:
            raise AssertionError(f"S{depth}: minimum-gap digit mismatch")
        if ranking_hash != expected["ranking_hash"]:
            raise AssertionError(f"S{depth}: ranking hash mismatch")
        rows[depth] = (metrics, scores)

    for depth in range(1, 8):
        metrics, _scores = rows[depth]
        q30_alone = (
            metrics["q30"]["terminal_mass"]
            + 3 * metrics["q30"]["occurrence_mass"]
            + metrics["q30"]["residual_error"]
            - metrics["lex"]["terminal_mass"]
            - 3 * metrics["lex"]["occurrence_mass"]
            - metrics["lex"]["residual_error"]
        )
        q30_after = (
            metrics["step54030"]["terminal_mass"]
            + 3 * metrics["step54030"]["occurrence_mass"]
            + metrics["step54030"]["residual_error"]
            - metrics["step540"]["terminal_mass"]
            - 3 * metrics["step540"]["occurrence_mass"]
            - metrics["step540"]["residual_error"]
        )
        expected = Q30_INTERACTION[depth]
        observed = (
            fraction_hash(q30_alone), sign_text(q30_alone),
            fraction_hash(q30_after), sign_text(q30_after),
        )
        if observed != expected:
            raise AssertionError(f"S{depth}: q30 interaction mismatch")

    metrics7, _scores7 = rows[7]
    hybrid = metrics7["hybrid5"]
    step540 = metrics7["step540"]
    base_difference = (
        hybrid["terminal_mass"] - step540["terminal_mass"]
        + 3 * (hybrid["occurrence_mass"] - step540["occurrence_mass"])
        + hybrid["residual_error"] - step540["residual_error"]
    )
    gamma_star = base_difference / REGENERATION_CHARGE
    if fraction_hash(gamma_star) != GAMMA_STAR_HASH:
        raise AssertionError("gamma-star hash mismatch")
    if not Fraction(837, 10_000) < gamma_star < Fraction(419, 5_000):
        raise AssertionError("gamma-star bracket mismatch")

    difference_1_16 = base_difference - Fraction(1, 16) * REGENERATION_CHARGE
    difference_1_10 = base_difference - Fraction(1, 10) * REGENERATION_CHARGE
    if difference_1_16 <= 0 or fraction_hash(difference_1_16) != GAMMA_1_16_HASH:
        raise AssertionError("gamma=1/16 comparison mismatch")
    if difference_1_10 >= 0 or fraction_hash(difference_1_10) != GAMMA_1_10_HASH:
        raise AssertionError("gamma=1/10 comparison mismatch")

    lines = [
        "TWO-COORDINATE POLICY FAMILY",
        "",
        "score=T+3*O+E+gamma*G_regen",
        "lambda=3",
        "gamma=1/10",
        "regeneration_charge=36953/4096",
        "",
    ]
    for depth in range(1, 8):
        expected = EXPECTED[depth]
        lines.extend(
            [
                f"S{depth}_winners=" + ",".join(expected["winners"]),
                f"S{depth}_winner_metrics=" + ",".join(map(str, expected["winner_metrics"])),
                f"S{depth}_minimum_gap_sha256={expected['gap_hash']}",
                f"S{depth}_minimum_gap_numerator_digits={expected['gap_digits'][0]}",
                f"S{depth}_minimum_gap_denominator_digits={expected['gap_digits'][1]}",
                f"S{depth}_ranking_sha256={expected['ranking_hash']}",
                "",
            ]
        )
    lines.extend(
        [
            f"hybrid5_vs_step540_gamma_star_sha256={GAMMA_STAR_HASH}",
            "hybrid5_vs_step540_gamma_star_bracket=837/10000,419/5000",
            f"gamma_1_16_difference_sha256={GAMMA_1_16_HASH}",
            "gamma_1_16_difference_sign=positive",
            f"gamma_1_10_difference_sha256={GAMMA_1_10_HASH}",
            "gamma_1_10_difference_sign=negative",
            "",
        ]
    )
    for depth in range(1, 8):
        alone_hash, alone_sign, after_hash, after_sign = Q30_INTERACTION[depth]
        lines.extend(
            [
                f"S{depth}_q30_alone_difference_sha256={alone_hash}",
                f"S{depth}_q30_alone_difference_sign={alone_sign}",
                f"S{depth}_q30_after_step540_difference_sha256={after_hash}",
                f"S{depth}_q30_after_step540_difference_sign={after_sign}",
                "",
            ]
        )
    lines.extend(
        [
            (
                "conclusion: within the certified finite policy family, lambda=3 "
                "and gamma=1/10 select step5/step540"
            ),
            (
                "on S2, step540 on S3 through S6, and the non-regenerative "
                "hybrid5 policy on S7. The previously"
            ),
            (
                "sufficient pairwise witness gamma=1/16 fails after step540 is "
                "added; the exact lower threshold rises above 0.0837."
            ),
            (
                "Delaying q30 improves C3 in isolation on S2 through S7 but "
                "worsens it after steps 5 and 40 are delayed,"
            ),
            (
                "so favorable local policy perturbations are not composable. "
                "This is a finite ranking theorem, not a global"
            ),
            "policy optimum or a retained-child Bellman theorem.",
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_two_coordinate_policy_family.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
