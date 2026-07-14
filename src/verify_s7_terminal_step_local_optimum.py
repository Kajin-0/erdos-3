#!/usr/bin/env python3
"""Certify an exact one-toggle local optimum for the S7 policy score."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import (
    all_three_aps,
    canonical_set_hash,
    schedule_hash,
    v2,
)
from verify_two_coordinate_policy_family import (
    REGENERATION_CHARGE,
    SEED_CENTERS,
    fraction_text,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

DELAYED_STEPS = frozenset(
    {
        4,
        5,
        6,
        19,
        62,
        71,
        81,
        141,
        142,
        161,
        162,
        365,
        384,
        400,
        1_526,
        1_592,
        1_962,
        5_946,
        8_190,
        9_773,
        9_792,
        10_157,
        42_638,
        42_643,
        49_158,
        50_838,
        87_530,
        93_471,
        103_249,
        103_268,
        103_633,
        135_162,
        142_634,
        228_638,
        230_159,
        333_413,
        333_797,
    }
)
SEED_5_142 = frozenset({5, 142})
EXPECTED_SELECTED = 9_323
EXPECTED_RESIDUAL = 517
EXPECTED_TERMINAL_STEPS = 28
EXPECTED_OCCURRENCES = 9_295
EXPECTED_DELAYED_HASH = (
    "3b04593d5685b1b2238e3cfe41213356000108c6a0e0009513cd34ce501e77bc"
)
EXPECTED_SCHEDULE_HASH = (
    "2a4df51cdf4c33263ff09fee2b39f3bd0e74277de2d6d2fa2904752ae14f2267"
)
EXPECTED_RESIDUAL_HASH = (
    "c22896814dcec5e644db1c77dbab257faba4dd61742226b02ae89c06bdba0b7d"
)
EXPECTED_TERMINAL_HASH = (
    "a00f1eae48ed0bb18fdf7f4ba33c9e1a70fc5a827385b8113304eb57dd1e0501"
)
EXPECTED_SCORE_HASH = (
    "e29d184f2e3218b6819d79fb17e97662b66f5f562bbad49368c678d5cd3b7825"
)
EXPECTED_TERMINAL_MASS_HASH = (
    "500f670a644078e5a5343b6575576202c4ad2754d833634f5a75ad8ead55cce9"
)
EXPECTED_OCCURRENCE_MASS_HASH = (
    "0fb178165e31b923167454e38fa144f83e35819e3af2277d521195eeb7ed4850"
)
EXPECTED_CANDIDATE_COUNT = 59
EXPECTED_CANDIDATE_HASH = (
    "00dbe691a994feb6e6723c1d43a03984fd01fdba671a8fc4b972c2a81275dcef"
)
EXPECTED_ZERO_SLACK = (384, 323_640)
EXPECTED_MINIMUM_STRICT_TOGGLE = 333_432
EXPECTED_MINIMUM_STRICT_SLACK = Fraction(384, 111_292_259_161)
EXPECTED_MINIMUM_STRICT_HASH = (
    "7f3f48508675369f486df98cdd7141d8bff66e9da6c8e5b534066aa5ef990e56"
)
EXPECTED_RANKING_HASH = (
    "46e29b7e6c688b1d58bfcd066507df04f86318d9cf9f3b0780988feb838515e7"
)
EXPECTED_OLD_SCORE_HASH = (
    "248d997189a633d7f24a7ca89c5e4a59a391cbd2fd215001b6cb514b78c39ff2"
)
EXPECTED_OLD_GAP_HASH = (
    "1a640959e7851f94963570ed1371d3242dd32719d5748afebf48a461e0b19e8b"
)
CERTIFICATE_SHA256 = (
    "8bd93afd6ed9bcd856ff23b5eb671b2963d5aa8b8e47df19f726b38760085211"
)


def set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(
        fraction_text(value).encode("utf-8")
    ).hexdigest()


def pairwise_harmonic(values: Iterable[int]) -> Fraction:
    terms = [Fraction(1, value) for value in sorted(values) if value > 0]
    while len(terms) > 1:
        terms = [
            terms[index] + terms[index + 1]
            if index + 1 < len(terms)
            else terms[index]
            for index in range(0, len(terms), 2)
        ]
    return terms[0] if terms else Fraction()


def resolve_policy(
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
    delayed_steps: frozenset[int],
) -> tuple[tuple[tuple[int, ...], ...], frozenset[int]]:
    """Resolve priority exactly as undelayed lex order then delayed lex order."""
    current = set(parent)
    selected: list[tuple[int, ...]] = []

    def consume(progression: tuple[int, int, int, int]) -> None:
        step, left, middle, right = progression
        if left not in current or middle not in current or right not in current:
            return
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)

    for progression in progressions:
        step, _left, middle, _right = progression
        delayed = step in delayed_steps or (
            step == 1 and middle in SEED_CENTERS
        )
        if not delayed:
            consume(progression)

    for progression in progressions:
        step, _left, middle, _right = progression
        delayed = step in delayed_steps or (
            step == 1 and middle in SEED_CENTERS
        )
        if delayed:
            consume(progression)

    return tuple(selected), frozenset(current)


def policy_metrics(
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
    delayed_steps: frozenset[int],
) -> dict[str, object]:
    state = state_by_depth(7)
    selected, residual = resolve_policy(parent, progressions, delayed_steps)

    centers: dict[int, list[int]] = defaultdict(list)
    for _sponsor, middle, _opposite, step, _left, _right in selected:
        centers[step].append(middle)

    terminal_steps = set(centers)
    occurrence_mass = Fraction()
    occurrences = 0
    seed_shell: tuple[int, ...] = ()
    for step, values in centers.items():
        ordered = sorted(values)
        minimum = ordered[0]
        fiber = frozenset(value - minimum for value in ordered[1:])
        occurrences += len(fiber)
        occurrence_mass += pairwise_harmonic(fiber)
        if step == 1:
            seed_shell = tuple(
                sorted(value for value in fiber if 16 <= value < 32)
            )

    terminal_mass = pairwise_harmonic(terminal_steps)
    residual_error = Fraction(
        state.persistence * len(residual),
        state.scale,
    )
    regeneration = seed_shell == (16, 21, 26)
    score = (
        terminal_mass
        + 3 * occurrence_mass
        + residual_error
        + (
            Fraction(1, 10) * REGENERATION_CHARGE
            if regeneration
            else Fraction()
        )
    )
    return {
        "selected_schedule": selected,
        "residual_set": residual,
        "selected": len(selected),
        "residual": len(residual),
        "terminal_step_set": frozenset(terminal_steps),
        "terminal_steps": len(terminal_steps),
        "occurrences": occurrences,
        "terminal_mass": terminal_mass,
        "occurrence_mass": occurrence_mass,
        "residual_error": residual_error,
        "regeneration": regeneration,
        "score": score,
    }


def build_certificate() -> str:
    state = state_by_depth(7)
    parent = state.values
    progressions = all_three_aps(parent)
    if len(progressions) != 298_606:
        raise AssertionError(
            f"initial progression-count mismatch: {len(progressions)}"
        )

    if set_hash(DELAYED_STEPS) != EXPECTED_DELAYED_HASH:
        raise AssertionError("delayed-step hash mismatch")

    base = policy_metrics(parent, progressions, DELAYED_STEPS)
    compact = (
        base["selected"],
        base["residual"],
        base["terminal_steps"],
        base["occurrences"],
        base["regeneration"],
    )
    expected_compact = (
        EXPECTED_SELECTED,
        EXPECTED_RESIDUAL,
        EXPECTED_TERMINAL_STEPS,
        EXPECTED_OCCURRENCES,
        False,
    )
    if compact != expected_compact:
        raise AssertionError(f"base metric mismatch: {compact!r}")

    if schedule_hash(
        base["selected_schedule"], base["residual_set"]
    ) != EXPECTED_SCHEDULE_HASH:
        raise AssertionError("schedule hash mismatch")
    if canonical_set_hash(base["residual_set"]) != EXPECTED_RESIDUAL_HASH:
        raise AssertionError("residual hash mismatch")
    if set_hash(base["terminal_step_set"]) != EXPECTED_TERMINAL_HASH:
        raise AssertionError("terminal-step hash mismatch")
    if fraction_hash(base["score"]) != EXPECTED_SCORE_HASH:
        raise AssertionError("score hash mismatch")
    if fraction_hash(base["terminal_mass"]) != EXPECTED_TERMINAL_MASS_HASH:
        raise AssertionError("terminal-mass hash mismatch")
    if fraction_hash(base["occurrence_mass"]) != EXPECTED_OCCURRENCE_MASS_HASH:
        raise AssertionError("occurrence-mass hash mismatch")

    candidates = tuple(
        sorted(set(base["terminal_step_set"]) | set(DELAYED_STEPS))
    )
    if len(candidates) != EXPECTED_CANDIDATE_COUNT:
        raise AssertionError(f"candidate-count mismatch: {len(candidates)}")
    candidate_payload = "\n".join(str(value) for value in candidates) + "\n"
    candidate_hash = hashlib.sha256(
        candidate_payload.encode("utf-8")
    ).hexdigest()
    if candidate_hash != EXPECTED_CANDIDATE_HASH:
        raise AssertionError(f"candidate hash mismatch: {candidate_hash}")

    slacks: list[tuple[Fraction, int]] = []
    for toggle in candidates:
        delayed = frozenset(set(DELAYED_STEPS) ^ {toggle})
        neighbor = policy_metrics(parent, progressions, delayed)
        slacks.append((neighbor["score"] - base["score"], toggle))
    slacks.sort(key=lambda row: (row[0], row[1]))

    improving = tuple(toggle for slack, toggle in slacks if slack < 0)
    if improving:
        raise AssertionError(f"improving toggles found: {improving!r}")
    zero_slack = tuple(toggle for slack, toggle in slacks if slack == 0)
    if zero_slack != EXPECTED_ZERO_SLACK:
        raise AssertionError(f"zero-slack mismatch: {zero_slack!r}")

    strict = [(slack, toggle) for slack, toggle in slacks if slack > 0]
    minimum_strict_slack, minimum_strict_toggle = strict[0]
    if minimum_strict_toggle != EXPECTED_MINIMUM_STRICT_TOGGLE:
        raise AssertionError(
            f"minimum-strict toggle mismatch: {minimum_strict_toggle}"
        )
    if minimum_strict_slack != EXPECTED_MINIMUM_STRICT_SLACK:
        raise AssertionError(
            f"minimum-strict slack mismatch: {minimum_strict_slack}"
        )
    if fraction_hash(minimum_strict_slack) != EXPECTED_MINIMUM_STRICT_HASH:
        raise AssertionError("minimum-strict hash mismatch")

    ranking_payload = "".join(
        f"{toggle}:{fraction_hash(slack)}\n"
        for slack, toggle in slacks
    )
    ranking_hash = hashlib.sha256(
        ranking_payload.encode("utf-8")
    ).hexdigest()
    if ranking_hash != EXPECTED_RANKING_HASH:
        raise AssertionError(f"ranking hash mismatch: {ranking_hash}")

    old = policy_metrics(parent, progressions, SEED_5_142)
    if old["regeneration"]:
        raise AssertionError("seed_5_142 unexpectedly regenerates")
    if fraction_hash(old["score"]) != EXPECTED_OLD_SCORE_HASH:
        raise AssertionError("seed_5_142 score hash mismatch")
    old_gap = old["score"] - base["score"]
    if fraction_hash(old_gap) != EXPECTED_OLD_GAP_HASH:
        raise AssertionError("seed_5_142 gap hash mismatch")
    if not Fraction(1_915, 1_000) < old_gap < Fraction(1_916, 1_000):
        raise AssertionError("seed_5_142 gap outside compact bracket")

    lines = [
        "S7 TERMINAL-STEP LOCAL OPTIMUM",
        "",
        "score=lambda:3,gamma:1/10",
        "seed_delay=True",
        "delayed_steps=" + ",".join(map(str, sorted(DELAYED_STEPS))),
        f"delayed_step_count={len(DELAYED_STEPS)}",
        f"delayed_steps_sha256={EXPECTED_DELAYED_HASH}",
        f"selected={base['selected']}",
        f"residual={base['residual']}",
        f"terminal_steps={base['terminal_steps']}",
        f"occurrences={base['occurrences']}",
        f"regeneration={base['regeneration']}",
        f"schedule_sha256={EXPECTED_SCHEDULE_HASH}",
        f"residual_sha256={EXPECTED_RESIDUAL_HASH}",
        f"terminal_steps_sha256={EXPECTED_TERMINAL_HASH}",
        f"score_sha256={EXPECTED_SCORE_HASH}",
        f"terminal_mass_sha256={EXPECTED_TERMINAL_MASS_HASH}",
        f"occurrence_mass_sha256={EXPECTED_OCCURRENCE_MASS_HASH}",
        "",
        "candidate_rule=terminal_step_set_union_delayed_step_set",
        f"candidate_count={len(candidates)}",
        f"candidate_sha256={candidate_hash}",
        "improving_toggles=0",
        "zero_slack_toggles=384,323640",
        f"minimum_strict_toggle={minimum_strict_toggle}",
        f"minimum_strict_slack={fraction_text(minimum_strict_slack)}",
        f"minimum_strict_slack_sha256={EXPECTED_MINIMUM_STRICT_HASH}",
        f"neighbor_ranking_sha256={ranking_hash}",
        "",
        f"seed_5_142_score_sha256={EXPECTED_OLD_SCORE_HASH}",
        "seed_5_142_minus_local_optimum_gap_bracket=1915/1000,1916/1000",
        f"seed_5_142_minus_local_optimum_gap_sha256={EXPECTED_OLD_GAP_HASH}",
        "",
        (
            "conclusion: the recorded 37-step seed-delayed S7 policy is an "
            "exact one-toggle local optimum"
        ),
        (
            "within the deterministic neighborhood consisting of its "
            "terminal-step set union its delayed-step set."
        ),
        (
            "It has no improving toggle, two zero-slack toggles, and strictly "
            "positive slack for every other toggle."
        ),
        (
            "This is not a global policy optimum and does not supply a "
            "provenance-preserving retained-child Bellman inequality."
        ),
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_s7_terminal_step_local_optimum.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print(
        "certificate_sha256="
        + hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
