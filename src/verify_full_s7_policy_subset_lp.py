#!/usr/bin/env python3
"""Certify the exact delay-subset policy LP through the full S7 64-policy family."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from branching_reserve_lp import export_lp, parse_constraint, verify_weights
from certified_contaminated_states import state_by_depth

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SUBSET_STEPS = (5, 40, 30, 161, 142)
SUBSETS = tuple(
    subset
    for size in range(len(SUBSET_STEPS) + 1)
    for subset in combinations(SUBSET_STEPS, size)
)
SEED_CENTERS = frozenset({1_354_065, 1_354_070, 1_354_075})
REGENERATION_CHARGE = Fraction(36_953, 4_096)
WEIGHTS = {"lambda": Fraction(3), "gamma": Fraction(1, 10)}
CHOSEN = {
    1: "delay_none",
    2: "delay_5",
    3: "delay_5_161_142",
    4: "delay_5_40",
    5: "delay_5_40",
    6: "delay_5_40",
    7: "seed_delay_5_142",
}
EXPECTED_PROGRESSION_COUNTS = {
    1: 9,
    2: 60,
    3: 398,
    4: 2_195,
    5: 11_523,
    6: 58_708,
    7: 298_606,
}
EXPECTED_WINNER_METRICS = {
    1: (6, 6, 2, 4, False),
    2: (25, 14, 7, 18, False),
    3: (90, 30, 13, 77, False),
    4: (304, 59, 20, 284, False),
    5: (974, 118, 25, 949, False),
    6: (3_041, 238, 27, 3_014, False),
    7: (9_347, 493, 50, 9_297, False),
}
EXPECTED_GAP_HASHES = {
    1: "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6",
    2: "8e3007fadb7ab81bdbfba7c7d0d2ec8df58cab9cae8022d6894505fe724d0e2f",
    3: "f63047846da4fbe9897d75156ec8ec2386709bc6a64d40c9305e7a03f7e2358c",
    4: "f6efdb50570f350f59056ab5b9086e40b354b72baf084056ebeab2c9183355a8",
    5: "c2bbd7b788caeeace703f57afaac6ff7f7136feea1ca8d6d3bb9a34cc4cc582d",
    6: "4d4b1dfe4e4b331875e91dfc2c36be3060f6d92e229df53e9842db90dff557bd",
    7: "94b80ff019f4ba5a4e740db7a11dfb5be412dae92c5ad6a3f863692ce5018d38",
}
EXPECTED_CONSTRAINTS = 249
EXPECTED_JSONL_BYTES = 1_257_772
EXPECTED_JSONL_SHA256 = "c8986841eb8e936848d26ef769e6314052987b42a59a0f6430dfcf2bc01b4f4d"
EXPECTED_LP_BYTES = 1_511_038
EXPECTED_LP_LINES = 256
EXPECTED_LP_SHA256 = "45c1f50bbac2b9d50a6b3d5dd99ff874f24ef965e046e476567fa2d9b3375985"
EXPECTED_ACTIVE_COUNT = 47
EXPECTED_ACTIVE_SHA256 = "d6913498d788323c69bade7513294c758022f439108f535675cfe495c4814027"
STRICT_MINIMUM_NAME = "S7:seed_delay_5_142<=seed_delay_5"
STRICT_MINIMUM_HASH = "94b80ff019f4ba5a4e740db7a11dfb5be412dae92c5ad6a3f863692ce5018d38"
CERTIFICATE_SHA256 = "36b93f5c52e55b7e0a182be0476881c4cd13bfbf17690261fa58c071509783c3"

Progression = tuple[int, int, int, int]
Selected = tuple[int, int, int, int, int, int]


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def all_three_aps(values: frozenset[int]) -> tuple[Progression, ...]:
    ordered = sorted(values)
    present = set(ordered)
    result: list[Progression] = []
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            right = middle + step
            if right in present:
                result.append((step, left, middle, right))
    return tuple(sorted(result))


def pairwise_harmonic(values: object) -> Fraction:
    terms = [Fraction(1, value) for value in values if value > 0]
    while len(terms) > 1:
        terms = [
            terms[index] + terms[index + 1]
            if index + 1 < len(terms)
            else terms[index]
            for index in range(0, len(terms), 2)
        ]
    return terms[0] if terms else Fraction()


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def policy_name(subset: tuple[int, ...], seed_delay: bool) -> str:
    base = "delay_none" if not subset else "delay_" + "_".join(map(str, subset))
    return "seed_" + base if seed_delay else base


def resolve_cached(
    depth: int,
    progressions: tuple[Progression, ...],
    delayed_steps: tuple[int, ...],
    seed_delay: bool,
) -> tuple[tuple[Selected, ...], frozenset[int]]:
    current = set(state_by_depth(depth).values)
    delayed_set = set(delayed_steps)
    normal: list[Progression] = []
    delayed: list[Progression] = []
    for progression in progressions:
        step, _left, middle, _right = progression
        is_delayed = step in delayed_set or (
            seed_delay
            and depth == 7
            and step == 1
            and middle in SEED_CENTERS
        )
        (delayed if is_delayed else normal).append(progression)

    selected: list[Selected] = []
    for step, left, middle, right in normal + delayed:
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)
    return tuple(selected), frozenset(current)


def policy_metrics(
    depth: int,
    progressions: tuple[Progression, ...],
    delayed_steps: tuple[int, ...],
    seed_delay: bool,
) -> dict[str, object]:
    state = state_by_depth(depth)
    selected, residual = resolve_cached(
        depth,
        progressions,
        delayed_steps,
        seed_delay,
    )
    centers: dict[int, list[int]] = defaultdict(list)
    for _sponsor, middle, _opposite, step, _left, _right in selected:
        centers[step].append(middle)

    fibers: dict[int, frozenset[int]] = {}
    for step, values in centers.items():
        ordered = sorted(values)
        minimum = ordered[0]
        fibers[step] = frozenset(value - minimum for value in ordered[1:])

    steps = set(fibers)
    seed_shell = tuple(
        sorted(
            value
            for value in fibers.get(1, frozenset())
            if 16 <= value < 32
        )
    )
    regeneration = depth == 7 and seed_shell == (16, 21, 26)
    return {
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(steps),
        "occurrences": sum(len(values) for values in fibers.values()),
        "terminal_mass": pairwise_harmonic(steps),
        "occurrence_mass": sum(
            (pairwise_harmonic(values) for values in fibers.values()),
            Fraction(),
        ),
        "residual_error": Fraction(
            state.persistence * len(residual),
            state.scale,
        ),
        "regeneration": regeneration,
    }


def score(metrics: dict[str, object]) -> Fraction:
    return (
        metrics["terminal_mass"]
        + WEIGHTS["lambda"] * metrics["occurrence_mass"]
        + metrics["residual_error"]
        + (
            WEIGHTS["gamma"] * REGENERATION_CHARGE
            if metrics["regeneration"]
            else Fraction()
        )
    )


def comparison_row(
    depth: int,
    chosen_name: str,
    chosen: dict[str, object],
    alternative_name: str,
    alternative: dict[str, object],
) -> dict[str, object]:
    delta_terminal = alternative["terminal_mass"] - chosen["terminal_mass"]
    delta_occurrence = alternative["occurrence_mass"] - chosen["occurrence_mass"]
    delta_error = alternative["residual_error"] - chosen["residual_error"]
    delta_regeneration = (
        int(alternative["regeneration"]) - int(chosen["regeneration"])
    ) * REGENERATION_CHARGE
    return {
        "name": f"S{depth}:{chosen_name}<={alternative_name}",
        "debt": fraction_text(-(delta_terminal + delta_error)),
        "parent": {
            "gamma": fraction_text(delta_regeneration),
            "lambda": fraction_text(delta_occurrence),
        },
        "children": [],
    }


def build_certificate() -> str:
    winners_by_depth: dict[int, tuple[str, ...]] = {}
    rows: list[dict[str, object]] = []

    for depth in range(1, 8):
        progressions = all_three_aps(state_by_depth(depth).values)
        if len(progressions) != EXPECTED_PROGRESSION_COUNTS[depth]:
            raise AssertionError(f"S{depth} progression count mismatch")
        seed_modes = (False, True) if depth == 7 else (False,)
        metrics = {
            policy_name(subset, seed_delay): policy_metrics(
                depth,
                progressions,
                subset,
                seed_delay,
            )
            for seed_delay in seed_modes
            for subset in SUBSETS
        }
        scores = {name: score(value) for name, value in metrics.items()}
        best = min(scores.values())
        winners = tuple(sorted(name for name, value in scores.items() if value == best))
        winners_by_depth[depth] = winners
        if CHOSEN[depth] not in winners:
            raise AssertionError(f"S{depth} chosen policy is not optimal")

        chosen = metrics[CHOSEN[depth]]
        observed_metrics = (
            chosen["selected"],
            chosen["residual"],
            chosen["terminal_steps"],
            chosen["occurrences"],
            chosen["regeneration"],
        )
        if observed_metrics != EXPECTED_WINNER_METRICS[depth]:
            raise AssertionError(f"S{depth} winner metric mismatch: {observed_metrics}")

        distinct_scores = sorted(set(scores.values()))
        gap = distinct_scores[1] - distinct_scores[0] if len(distinct_scores) > 1 else Fraction()
        if fraction_hash(gap) != EXPECTED_GAP_HASHES[depth]:
            raise AssertionError(f"S{depth} score-gap mismatch")

        for alternative_name in sorted(metrics):
            if alternative_name == CHOSEN[depth]:
                continue
            rows.append(
                comparison_row(
                    depth,
                    CHOSEN[depth],
                    chosen,
                    alternative_name,
                    metrics[alternative_name],
                )
            )

    if winners_by_depth[7] != ("seed_delay_5_142",):
        raise AssertionError(f"S7 winner mismatch: {winners_by_depth[7]}")
    if len(rows) != EXPECTED_CONSTRAINTS:
        raise AssertionError(f"constraint count mismatch: {len(rows)}")

    jsonl = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    jsonl_bytes = len(jsonl.encode("utf-8"))
    jsonl_hash = hashlib.sha256(jsonl.encode("utf-8")).hexdigest()
    if jsonl_bytes != EXPECTED_JSONL_BYTES or jsonl_hash != EXPECTED_JSONL_SHA256:
        raise AssertionError("canonical JSONL mismatch")

    constraints = [
        parse_constraint(row, index)
        for index, row in enumerate(rows, start=1)
    ]
    valid, report = verify_weights(constraints, WEIGHTS)
    if not valid:
        raise AssertionError(report)

    slacks = [(constraint.slack(WEIGHTS), constraint.name) for constraint in constraints]
    active = tuple(name for slack, name in slacks if slack == 0)
    active_payload = "\n".join(active) + "\n"
    active_hash = hashlib.sha256(active_payload.encode("utf-8")).hexdigest()
    if len(active) != EXPECTED_ACTIVE_COUNT or active_hash != EXPECTED_ACTIVE_SHA256:
        raise AssertionError("active equality mismatch")

    strict_slack, strict_name = min(
        (slack, name) for slack, name in slacks if slack > 0
    )
    if strict_name != STRICT_MINIMUM_NAME:
        raise AssertionError(f"strict minimum mismatch: {strict_name}")
    if fraction_hash(strict_slack) != STRICT_MINIMUM_HASH:
        raise AssertionError("strict minimum slack mismatch")

    lp = export_lp(constraints)
    lp_bytes = len(lp.encode("utf-8"))
    lp_lines = len(lp.splitlines())
    lp_hash = hashlib.sha256(lp.encode("utf-8")).hexdigest()
    if (
        lp_bytes != EXPECTED_LP_BYTES
        or lp_lines != EXPECTED_LP_LINES
        or lp_hash != EXPECTED_LP_SHA256
    ):
        raise AssertionError("CPLEX-LP export mismatch")

    lines = [
        "FULL S7 DELAY-SUBSET POLICY LP",
        "",
        "subset_steps=5,40,30,161,142",
        "S1_S6_policies_per_state=32",
        "S7_policies=64",
        "features=lambda,gamma",
        "weights=lambda:3,gamma:1/10",
        f"constraints={len(rows)}",
        f"jsonl_bytes={jsonl_bytes}",
        f"jsonl_sha256={jsonl_hash}",
        f"lp_bytes={lp_bytes}",
        f"lp_lines={lp_lines}",
        f"lp_sha256={lp_hash}",
        "",
        "result=FEASIBLE",
        f"active_equalities={len(active)}",
        f"active_equalities_sha256={active_hash}",
        f"strict_minimum_constraint={strict_name}",
        f"strict_minimum_slack_sha256={STRICT_MINIMUM_HASH}",
        f"strict_minimum_slack_numerator_digits={len(str(strict_slack.numerator))}",
        f"strict_minimum_slack_denominator_digits={len(str(strict_slack.denominator))}",
        "",
        "S1_chosen=delay_none",
        "S2_chosen=delay_5",
        "S3_chosen=delay_5_161_142",
        "S4_chosen=delay_5_40",
        "S5_chosen=delay_5_40",
        "S6_chosen=delay_5_40",
        "S7_chosen=seed_delay_5_142",
        "",
        (
            "conclusion: lambda=3,gamma=1/10 remains feasible after exact "
            "enumeration of all 64 S7 policies formed by the 32 delay subsets, "
            "with and without seed delay."
        ),
        (
            "The S7 optimum changes from seed_delay_5 to seed_delay_5_142. "
            "This remains a finite policy-ranking LP, not a retained-child "
            "Bellman theorem."
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
        raise SystemExit("usage: verify_full_s7_policy_subset_lp.py [OUTPUT]")
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
