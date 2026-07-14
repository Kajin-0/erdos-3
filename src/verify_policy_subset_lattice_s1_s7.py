#!/usr/bin/env python3
"""Certify the exact five-step policy subset lattice through S7."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import heapq
import json
import sys

from branching_reserve_lp import export_lp, parse_constraint, verify_weights
from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import all_three_aps, v2
from verify_two_coordinate_policy_family import (
    REGENERATION_CHARGE,
    SEED_CENTERS,
    fraction_text,
    middle_fibers,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SUBSET_STEPS = (5, 40, 30, 161, 142)
SUBSETS = tuple(
    subset
    for size in range(len(SUBSET_STEPS) + 1)
    for subset in combinations(SUBSET_STEPS, size)
)
CHOSEN = {
    1: "plain_none",
    2: "plain_5",
    3: "plain_5_161_142",
    4: "plain_5_40",
    5: "plain_5_40",
    6: "plain_5_40",
    7: "seed_5_142",
}
WEIGHTS = {"lambda": Fraction(3), "gamma": Fraction(1, 10)}
EXPECTED_PROGRESSION_COUNTS = {
    1: 9,
    2: 60,
    3: 398,
    4: 2_195,
    5: 11_523,
    6: 58_708,
    7: 298_606,
}
EXPECTED_CHOSEN_METRICS = {
    1: (6, 6, 2, 4, False),
    2: (25, 14, 7, 18, False),
    3: (90, 30, 13, 77, False),
    4: (304, 59, 20, 284, False),
    5: (974, 118, 25, 949, False),
    6: (3_041, 238, 27, 3_014, False),
    7: (9_347, 493, 50, 9_297, False),
}
EXPECTED_WINNER_HASHES = {
    1: "8fec88c89d27b095f80c2b40ccde8e42786c6f09573ac5352a507ac2f123b82d",
    2: "e790a923e6d12ec7da08251f974bc25e30c9a55eaa8da8c870c94b6034a45f90",
    3: "388efdfbadf6ce391aca2238c0336672f014cb5d0a198f7d5c3c0aaf5dc0ef22",
    4: "b01313341fdb88c6da897762216cf4c12d03d0c00b1db97af6595460c730907e",
    5: "b01313341fdb88c6da897762216cf4c12d03d0c00b1db97af6595460c730907e",
    6: "b01313341fdb88c6da897762216cf4c12d03d0c00b1db97af6595460c730907e",
    7: "d619ea36d6ee8d9134ddc83dc43a6a788cac415d8f1c4fa87f0372e6b415987e",
}
EXPECTED_CONSTRAINTS = 250
EXPECTED_JSONL_BYTES = 1_295_230
EXPECTED_JSONL_SHA256 = "e439db76aef083e35239386c040d9fca934508d53a383836f4c78efa74ea85af"
EXPECTED_LP_BYTES = 1_543_499
EXPECTED_LP_LINES = 257
EXPECTED_LP_SHA256 = "f3775bccfcfea11783e9777fa5b402f6f86b4d58b431b700509373cd35ef8f70"
EXPECTED_ACTIVE_COUNT = 47
EXPECTED_ACTIVE_SHA256 = "14d4538f638b69ca5763abb9c9f1e8cc3756d1e56105eb0ebf29d212ec953fb0"
STRICT_MINIMUM_NAME = "S7:seed_5_142<=seed_5"
STRICT_MINIMUM_HASH = "94b80ff019f4ba5a4e740db7a11dfb5be412dae92c5ad6a3f863692ce5018d38"
S7_TERMINAL_MASS_HASH = "35da913066b9bafd4496f57528781b57384989eeb2d2f1f4855320c54d8831a6"
S7_OCCURRENCE_MASS_HASH = "a8ed8fe436bc596559bf0ff41e5a590a03122eae5f2d8f301151fbc383a22f21"
CERTIFICATE_SHA256 = "85667125996eb7d3f33d6bdf6ddd78ad1cefbad8c229d57402711e20d17a2287"


def policy_name(subset: tuple[int, ...], seed_delay: bool) -> str:
    prefix = "seed_" if seed_delay else "plain_"
    suffix = "none" if not subset else "_".join(map(str, subset))
    return prefix + suffix


def pairwise_harmonic(values: object) -> Fraction:
    terms = [Fraction(1, value) for value in sorted(values) if value > 0]
    while len(terms) > 1:
        terms = [
            terms[index] + terms[index + 1]
            if index + 1 < len(terms)
            else terms[index]
            for index in range(0, len(terms), 2)
        ]
    return terms[0] if terms else Fraction()


def resolve_cached(
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
    delayed_steps: frozenset[int],
    seed_delay: bool,
    reverse: bool,
) -> tuple[tuple[tuple[int, ...], ...], frozenset[int]]:
    current = set(parent)
    queue = []
    for progression in progressions:
        step, _left, middle, _right = progression
        if reverse:
            priority = tuple(-value for value in progression)
        else:
            delayed = step in delayed_steps or (
                seed_delay
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


def policy_metrics(
    depth: int,
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
    delayed_steps: frozenset[int],
    seed_delay: bool,
    reverse: bool,
) -> dict[str, object]:
    state = state_by_depth(depth)
    selected, residual = resolve_cached(
        parent,
        progressions,
        delayed_steps,
        seed_delay,
        reverse,
    )
    fibers = middle_fibers(selected)
    terminal_steps = set(fibers)
    terminal_mass = pairwise_harmonic(terminal_steps)
    occurrence_mass = sum(
        (pairwise_harmonic(values) for values in fibers.values()),
        Fraction(),
    )
    residual_error = Fraction(
        state.persistence * len(residual),
        state.scale,
    )
    seed_shell = tuple(
        sorted(
            value
            for value in fibers.get(1, frozenset())
            if 16 <= value < 32
        )
    )
    regeneration = depth == 7 and seed_shell == (16, 21, 26)
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
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(terminal_steps),
        "occurrences": sum(len(values) for values in fibers.values()),
        "terminal_mass": terminal_mass,
        "occurrence_mass": occurrence_mass,
        "residual_error": residual_error,
        "regeneration": regeneration,
        "score": score,
    }


def build_metrics() -> dict[int, dict[str, dict[str, object]]]:
    result: dict[int, dict[str, dict[str, object]]] = {}
    for depth in range(1, 8):
        parent = state_by_depth(depth).values
        progressions = all_three_aps(parent)
        if len(progressions) != EXPECTED_PROGRESSION_COUNTS[depth]:
            raise AssertionError(
                f"S{depth} progression-count mismatch: {len(progressions)}"
            )
        policies: dict[str, dict[str, object]] = {}
        for subset in SUBSETS:
            name = policy_name(subset, False)
            policies[name] = policy_metrics(
                depth,
                parent,
                progressions,
                frozenset(subset),
                False,
                False,
            )
        if depth == 7:
            for subset in SUBSETS:
                name = policy_name(subset, True)
                policies[name] = policy_metrics(
                    depth,
                    parent,
                    progressions,
                    frozenset(subset),
                    True,
                    False,
                )
            policies["reverse"] = policy_metrics(
                depth,
                parent,
                progressions,
                frozenset(),
                False,
                True,
            )
        result[depth] = policies
    return result


def build_rows(
    metrics: dict[int, dict[str, dict[str, object]]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for depth in range(1, 8):
        chosen_name = CHOSEN[depth]
        chosen = metrics[depth][chosen_name]
        for alternative_name in sorted(metrics[depth]):
            if alternative_name == chosen_name:
                continue
            alternative = metrics[depth][alternative_name]
            delta_terminal = (
                alternative["terminal_mass"] - chosen["terminal_mass"]
            )
            delta_occurrence = (
                alternative["occurrence_mass"] - chosen["occurrence_mass"]
            )
            delta_error = (
                alternative["residual_error"] - chosen["residual_error"]
            )
            delta_regeneration = (
                REGENERATION_CHARGE
                if alternative["regeneration"]
                else Fraction()
            ) - (
                REGENERATION_CHARGE
                if chosen["regeneration"]
                else Fraction()
            )
            rows.append(
                {
                    "name": (
                        f"S{depth}:{chosen_name}<={alternative_name}"
                    ),
                    "debt": fraction_text(
                        -(delta_terminal + delta_error)
                    ),
                    "parent": {
                        "gamma": fraction_text(delta_regeneration),
                        "lambda": fraction_text(delta_occurrence),
                    },
                    "children": [],
                }
            )
    return rows


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(
        fraction_text(value).encode("utf-8")
    ).hexdigest()


def build_certificate() -> str:
    metrics = build_metrics()

    for depth in range(1, 8):
        chosen = metrics[depth][CHOSEN[depth]]
        compact = (
            chosen["selected"],
            chosen["residual"],
            chosen["terminal_steps"],
            chosen["occurrences"],
            chosen["regeneration"],
        )
        if compact != EXPECTED_CHOSEN_METRICS[depth]:
            raise AssertionError(
                f"S{depth} chosen metric mismatch: {compact!r}"
            )
        best = min(value["score"] for value in metrics[depth].values())
        winners = tuple(
            sorted(
                name
                for name, value in metrics[depth].items()
                if value["score"] == best
            )
        )
        payload = "\n".join(winners) + "\n"
        winner_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        if winner_hash != EXPECTED_WINNER_HASHES[depth]:
            raise AssertionError(
                f"S{depth} winner-set hash mismatch: {winner_hash}"
            )
        if CHOSEN[depth] not in winners:
            raise AssertionError(f"S{depth} chosen policy is not optimal")

    s7_ranking = sorted(
        metrics[7].items(),
        key=lambda item: (item[1]["score"], item[0]),
    )
    if s7_ranking[0][0] != "seed_5_142":
        raise AssertionError("S7 winner mismatch")
    if s7_ranking[1][0] != "seed_5":
        raise AssertionError("S7 runner-up mismatch")
    s7_gap = s7_ranking[1][1]["score"] - s7_ranking[0][1]["score"]
    if fraction_hash(s7_gap) != STRICT_MINIMUM_HASH:
        raise AssertionError("S7 score-gap hash mismatch")
    if not Fraction(3, 2_000) < s7_gap < Fraction(751, 500_000):
        raise AssertionError("S7 score gap outside compact bracket")

    chosen7 = metrics[7]["seed_5_142"]
    if fraction_hash(chosen7["terminal_mass"]) != S7_TERMINAL_MASS_HASH:
        raise AssertionError("S7 terminal-mass hash mismatch")
    if fraction_hash(chosen7["occurrence_mass"]) != S7_OCCURRENCE_MASS_HASH:
        raise AssertionError("S7 occurrence-mass hash mismatch")

    rows = build_rows(metrics)
    if len(rows) != EXPECTED_CONSTRAINTS:
        raise AssertionError(f"constraint count mismatch: {len(rows)}")
    jsonl = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    jsonl_bytes = len(jsonl.encode("utf-8"))
    jsonl_hash = hashlib.sha256(jsonl.encode("utf-8")).hexdigest()
    if jsonl_bytes != EXPECTED_JSONL_BYTES:
        raise AssertionError(f"JSONL byte-count mismatch: {jsonl_bytes}")
    if jsonl_hash != EXPECTED_JSONL_SHA256:
        raise AssertionError(f"JSONL hash mismatch: {jsonl_hash}")

    constraints = [
        parse_constraint(row, index)
        for index, row in enumerate(rows, start=1)
    ]
    valid, report = verify_weights(constraints, WEIGHTS)
    if not valid:
        raise AssertionError(report)
    slacks = [
        (constraint.slack(WEIGHTS), constraint.name)
        for constraint in constraints
    ]
    active = tuple(name for slack, name in slacks if slack == 0)
    if len(active) != EXPECTED_ACTIVE_COUNT:
        raise AssertionError(f"active count mismatch: {len(active)}")
    active_payload = "\n".join(active) + "\n"
    active_hash = hashlib.sha256(
        active_payload.encode("utf-8")
    ).hexdigest()
    if active_hash != EXPECTED_ACTIVE_SHA256:
        raise AssertionError(f"active hash mismatch: {active_hash}")

    strict_slack, strict_name = min(
        (slack, name)
        for slack, name in slacks
        if slack > 0
    )
    if strict_name != STRICT_MINIMUM_NAME:
        raise AssertionError(f"strict minimum mismatch: {strict_name}")
    if fraction_hash(strict_slack) != STRICT_MINIMUM_HASH:
        raise AssertionError("strict-minimum hash mismatch")

    lp = export_lp(constraints)
    lp_bytes = len(lp.encode("utf-8"))
    lp_lines = len(lp.splitlines())
    lp_hash = hashlib.sha256(lp.encode("utf-8")).hexdigest()
    if lp_bytes != EXPECTED_LP_BYTES:
        raise AssertionError(f"LP byte-count mismatch: {lp_bytes}")
    if lp_lines != EXPECTED_LP_LINES:
        raise AssertionError(f"LP line-count mismatch: {lp_lines}")
    if lp_hash != EXPECTED_LP_SHA256:
        raise AssertionError(f"LP hash mismatch: {lp_hash}")

    lines = [
        "POLICY SUBSET-LATTICE LP S1-S7",
        "",
        "subset_steps=5,40,30,161,142",
        "S1_S6_plain_subsets_per_state=32",
        "S7_plain_subsets=32",
        "S7_seed_subsets=32",
        "S7_reverse_policy=1",
        "features=lambda,gamma",
        "weights=lambda:3,gamma:1/10",
        f"constraints={len(constraints)}",
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
        (
            "strict_minimum_slack_numerator_digits="
            f"{len(str(strict_slack.numerator))}"
        ),
        (
            "strict_minimum_slack_denominator_digits="
            f"{len(str(strict_slack.denominator))}"
        ),
        "",
        "S1_chosen=plain_none",
        "S2_chosen=plain_5",
        "S3_chosen=plain_5_161_142",
        "S4_chosen=plain_5_40",
        "S5_chosen=plain_5_40",
        "S6_chosen=plain_5_40",
        "S7_chosen=seed_5_142",
        "S7_runner_up=seed_5",
        "S7_chosen_selected=9347",
        "S7_chosen_residual=493",
        "S7_chosen_terminal_steps=50",
        "S7_chosen_occurrences=9297",
        "S7_chosen_regeneration=False",
        f"S7_chosen_terminal_mass_sha256={S7_TERMINAL_MASS_HASH}",
        f"S7_chosen_occurrence_mass_sha256={S7_OCCURRENCE_MASS_HASH}",
        "S7_score_gap_bracket=3/2000,751/500000",
        "",
        (
            "conclusion: exhaustive enumeration of the five-step subset lattice "
            "on S7, with and without the seed delay, changes the exact "
            "non-regenerative winner from seed_5 to seed_5_142."
        ),
        (
            "The witness lambda=3,gamma=1/10 remains feasible after adding all "
            "64 S7 subset policies and reverse deletion, for 250 exact "
            "policy-ranking constraints."
        ),
        (
            "This finite result still does not establish global schedule "
            "optimality or a provenance-preserving retained-child Bellman "
            "inequality."
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
            "usage: verify_policy_subset_lattice_s1_s7.py [OUTPUT]"
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
