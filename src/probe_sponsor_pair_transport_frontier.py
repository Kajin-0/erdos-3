#!/usr/bin/env python3
"""Classify activated sponsor-core pair transport on the refined R4->F5 frontier.

The probe uses the certified residual/sponsor backbone split.  It does not fit a
potential and it does not propagate another generation.  Distinct parent pair
tokens actually used by the complete retained child resource family are
transported through the parent's certified lexicographic deletion schedule until
reaching a direct selected edge, a backward obstruction, or a residual pair.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from probe_residual_sponsor_backbone_split import (
    affine_reference,
    build_split_occurrences,
    pair_weight,
    retain_occurrences,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_provenance_second_generation import resolve_lexicographic
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Pair = tuple[int, int]


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate pair")
    return (left, right) if left < right else (right, left)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def serialize_mass(value: Fraction) -> dict[str, str]:
    return {
        "fraction": fraction_text(value),
        "decimal": decimal_text(value),
        "sha256": fraction_hash(value),
    }


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def reconstruct_fourth_recursive() -> tuple[object, ...]:
    _retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    if len(recursive_fourth) != 12:
        raise AssertionError("certified fourth recursive frontier changed")
    return recursive_fourth


def parent_schedule(parent: object) -> dict[str, object]:
    values = tuple(parent.values)
    roots = tuple(parent.representative.provenance)
    if len(set(roots)) != len(roots):
        raise AssertionError("parent root provenance is not unique")
    root_map = dict(zip(values, roots, strict=True))
    selected, residual_values = resolve_lexicographic(frozenset(values))

    tau: dict[int, int] = {}
    action_by_sponsor: dict[int, dict[str, int]] = {}
    selected_rows: list[dict[str, int]] = []
    for rank, row in enumerate(selected):
        sponsor_value, middle_value, opposite_value, step, _left, _right = row
        sponsor = root_map[sponsor_value]
        middle = root_map[middle_value]
        opposite = root_map[opposite_value]
        if sponsor in tau:
            raise AssertionError("sponsor root deleted twice")
        epsilon = 1 if middle > sponsor else -1
        q = abs(middle - sponsor)
        if q != step or opposite != sponsor + 2 * epsilon * q:
            raise AssertionError("root-coordinate action mismatch")
        action = {
            "rank": rank,
            "sponsor": sponsor,
            "middle": middle,
            "opposite": opposite,
            "q": q,
            "epsilon": epsilon,
        }
        tau[sponsor] = rank
        action_by_sponsor[sponsor] = action
        selected_rows.append(action)

    residual_roots = {root_map[value] for value in residual_values}
    sponsor_roots = set(tau)
    if residual_roots & sponsor_roots:
        raise AssertionError("root residual/sponsor partition overlaps")
    if residual_roots | sponsor_roots != set(roots):
        raise AssertionError("root residual/sponsor partition incomplete")

    incidence_mass = sum(
        (Fraction(3, 2 * int(action["q"])) for action in selected_rows),
        Fraction(),
    )
    return {
        "parent_class": parent.index,
        "roots": set(roots),
        "reference": affine_reference(parent),
        "tau": tau,
        "actions": action_by_sponsor,
        "selected_rows": selected_rows,
        "residual": residual_roots,
        "sponsors": sponsor_roots,
        "incidence_mass": incidence_mass,
    }


def completion_roots(pair: Pair, roots: set[int]) -> tuple[int, ...]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return tuple(sorted(candidates & roots))


def transport(pair: Pair, schedule: dict[str, object]) -> dict[str, object]:
    tau: dict[int, int] = schedule["tau"]  # type: ignore[assignment]
    actions: dict[int, dict[str, int]] = schedule["actions"]  # type: ignore[assignment]
    residual: set[int] = schedule["residual"]  # type: ignore[assignment]
    current = pair
    path: list[dict[str, object]] = []
    previous_rank = -1

    while True:
        left, right = current
        left_rank = tau.get(left)
        right_rank = tau.get(right)
        if left_rank is None and right_rank is None:
            if left not in residual or right not in residual:
                raise AssertionError("finite transport ended outside residual")
            return {
                "terminal_class": "residual",
                "target": current,
                "path": path,
            }

        if right_rank is None or (
            left_rank is not None and left_rank < right_rank
        ):
            sponsor, other, rank = left, right, left_rank
        else:
            sponsor, other, rank = right, left, right_rank
        if rank is None:
            raise AssertionError("missing finite deletion rank")
        if rank <= previous_rank:
            raise AssertionError("deletion rank did not increase")
        action = actions[sponsor]
        middle = int(action["middle"])
        opposite = int(action["opposite"])
        q = int(action["q"])
        epsilon = int(action["epsilon"])

        if other == middle or other == opposite:
            return {
                "terminal_class": "direct",
                "target": current,
                "path": path,
                "terminal_rank": rank,
                "terminal_q": q,
                "terminal_epsilon": epsilon,
            }

        if abs(other - middle) > abs(other - sponsor):
            return {
                "terminal_class": "backward",
                "target": current,
                "path": path,
                "terminal_rank": rank,
                "terminal_q": q,
                "terminal_epsilon": epsilon,
            }

        updated = ordered_pair(middle, other)
        if pair_weight(updated) < pair_weight(current):
            raise AssertionError("forward transport decreased pair weight")
        next_ranks = [tau[value] for value in updated if value in tau]
        if next_ranks and min(next_ranks) <= rank:
            raise AssertionError("forward transport did not raise minimum rank")
        path.append(
            {
                "from": current,
                "to": updated,
                "rank": rank,
                "q": q,
                "epsilon": epsilon,
            }
        )
        current = updated
        previous_rank = rank


def summarize_rows(rows: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    buckets: dict[object, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[row[key]].append(row)
    result: list[dict[str, object]] = []
    for value, members in buckets.items():
        initial_mass = sum((member["initial_weight"] for member in members), Fraction())
        target_mass = sum((member["target_weight"] for member in members), Fraction())
        result.append(
            {
                "key": value,
                "count": len(members),
                "initial_mass": serialize_mass(initial_mass),
                "target_occurrence_mass": serialize_mass(target_mass),
            }
        )
    return sorted(
        result,
        key=lambda row: (
            -Fraction(row["initial_mass"]["fraction"]),  # type: ignore[index]
            str(row["key"]),
        ),
    )


def main() -> int:
    parents = reconstruct_fourth_recursive()
    parent_by_index = {parent.index: parent for parent in parents}
    schedules = {parent.index: parent_schedule(parent) for parent in parents}

    split_occurrences = build_split_occurrences(parents)
    split_retained, split_metrics = retain_occurrences(split_occurrences)
    if split_metrics["retained_states"] != 37:
        raise AssertionError("refined retained frontier changed")

    occurrence_rows: list[dict[str, object]] = []
    for state in split_retained:
        parent_class = state.representative.parent_class
        parent = parent_by_index[parent_class]
        parent_roots = set(parent.representative.provenance)
        reference = affine_reference(state)
        roots = tuple(state.representative.provenance)
        terminal = not contains_three_term_ap(state.values)
        source = state.representative.source

        for root in roots:
            pair = ordered_pair(reference, root)
            if not set(pair) <= parent_roots:
                raise AssertionError("child current pair is not a parent root pair")
            occurrence_rows.append(
                {
                    "pair": pair,
                    "parent_class": parent_class,
                    "resource_kind": (
                        "current_terminal" if terminal else "current_recursive"
                    ),
                    "child_source": source,
                }
            )

        if not terminal:
            for pair in combinations(sorted(roots), 2):
                if not set(pair) <= parent_roots:
                    raise AssertionError("child latent pair is not a parent root pair")
                occurrence_rows.append(
                    {
                        "pair": pair,
                        "parent_class": parent_class,
                        "resource_kind": "latent_recursive",
                        "child_source": source,
                    }
                )

    grouped_occurrences: dict[Pair, list[dict[str, object]]] = defaultdict(list)
    for row in occurrence_rows:
        grouped_occurrences[row["pair"]].append(row)  # type: ignore[index]

    active_rows: list[dict[str, object]] = []
    inactive_residual_rows: list[dict[str, object]] = []
    for pair, members in sorted(grouped_occurrences.items()):
        parent_classes = {int(member["parent_class"]) for member in members}
        if len(parent_classes) != 1:
            raise AssertionError("pair token belongs to multiple parent classes")
        parent_class = next(iter(parent_classes))
        schedule = schedules[parent_class]
        sponsors: set[int] = schedule["sponsors"]  # type: ignore[assignment]
        roots: set[int] = schedule["roots"]  # type: ignore[assignment]
        if not set(pair) <= roots:
            raise AssertionError("activated pair left parent root universe")

        resource_kinds = tuple(sorted({str(member["resource_kind"]) for member in members}))
        child_sources = tuple(sorted({str(member["child_source"]) for member in members}))
        initial_weight = pair_weight(pair)
        completions = completion_roots(pair, roots)
        base = {
            "pair": pair,
            "parent_class": parent_class,
            "occurrence_count": len(members),
            "resource_kinds": resource_kinds,
            "child_sources": child_sources,
            "initial_weight": initial_weight,
            "completion_class": "in_parent" if completions else "parent_external",
            "completion_roots": completions,
        }

        if not (set(pair) & sponsors):
            inactive_residual_rows.append(base)
            continue

        result = transport(pair, schedule)
        target: Pair = result["target"]  # type: ignore[assignment]
        path: list[dict[str, object]] = result["path"]  # type: ignore[assignment]
        first_owner = min(
            (value for value in pair if value in schedule["tau"]),
            key=lambda value: schedule["tau"][value],  # type: ignore[index]
        )
        first_action = schedule["actions"][first_owner]  # type: ignore[index]
        active_rows.append(
            {
                **base,
                "terminal_class": result["terminal_class"],
                "target": target,
                "target_weight": pair_weight(target),
                "path_length": len(path),
                "first_q": int(first_action["q"]),
                "first_epsilon": int(first_action["epsilon"]),
                "first_rank": int(first_action["rank"]),
                "terminal_q": result.get("terminal_q"),
                "terminal_epsilon": result.get("terminal_epsilon"),
                "path_hash": canonical_hash(path),
            }
        )

    active_pairs = {row["pair"] for row in active_rows}
    if len(active_pairs) != len(active_rows):
        raise AssertionError("active union rows are not distinct")

    target_counter = Counter(row["target"] for row in active_rows)
    initial_mass = sum((row["initial_weight"] for row in active_rows), Fraction())
    target_occurrence_mass = sum(
        (row["target_weight"] for row in active_rows), Fraction()
    )
    target_union_mass = sum((pair_weight(pair) for pair in target_counter), Fraction())
    collision_mass = sum(
        (
            pair_weight(pair) * (multiplicity - 1)
            for pair, multiplicity in target_counter.items()
            if multiplicity > 1
        ),
        Fraction(),
    )
    if target_union_mass + collision_mass != target_occurrence_mass:
        raise AssertionError("terminal target first-use/collision partition failed")
    if initial_mass > target_occurrence_mass:
        raise AssertionError("transport monotonicity failed in aggregate")

    class_rows = summarize_rows(active_rows, "terminal_class")
    class_mass = {
        row["key"]: Fraction(row["target_occurrence_mass"]["fraction"])  # type: ignore[index]
        for row in class_rows
    }
    incidence_mass = sum(
        (schedule["incidence_mass"] for schedule in schedules.values()),
        Fraction(),
    )
    direct_distinct_targets = {
        row["target"] for row in active_rows if row["terminal_class"] == "direct"
    }
    direct_union_mass = sum(
        (pair_weight(pair) for pair in direct_distinct_targets), Fraction()
    )
    if direct_union_mass > incidence_mass:
        raise AssertionError("direct target mass exceeds selected-action incidence")
    rhs = (
        incidence_mass
        + class_mass.get("backward", Fraction())
        + class_mass.get("residual", Fraction())
        + collision_mass
    )
    if initial_mass > rhs:
        raise AssertionError("set-valued sponsor-pair transport inequality failed")

    path_rows = summarize_rows(active_rows, "path_length")
    completion_rows = summarize_rows(active_rows, "completion_class")
    resource_signature_rows = summarize_rows(active_rows, "resource_kinds")
    source_signature_rows = summarize_rows(active_rows, "child_sources")
    side_rows = summarize_rows(active_rows, "first_epsilon")
    parent_rows = summarize_rows(active_rows, "parent_class")

    max_target_multiplicity = max(target_counter.values(), default=0)
    collision_targets = [
        {
            "target": pair,
            "multiplicity": multiplicity,
            "weight": serialize_mass(pair_weight(pair)),
        }
        for pair, multiplicity in sorted(target_counter.items())
        if multiplicity > 1
    ]

    serial_active_rows = [
        {
            key: (
                fraction_text(value)
                if isinstance(value, Fraction)
                else list(value)
                if isinstance(value, tuple)
                else value
            )
            for key, value in row.items()
        }
        for row in active_rows
    ]
    serial_inactive_rows = [
        {
            key: (
                fraction_text(value)
                if isinstance(value, Fraction)
                else list(value)
                if isinstance(value, tuple)
                else value
            )
            for key, value in row.items()
        }
        for row in inactive_residual_rows
    ]

    output = {
        "schema": "sponsor_pair_transport_frontier_probe_v1",
        "scope": "certified_residual_sponsor_R4_to_complete_F5_retained_transition",
        "generation_six_propagated": False,
        "counts": {
            "parent_states": len(parents),
            "split_retained_states": len(split_retained),
            "resource_occurrences": len(occurrence_rows),
            "distinct_resource_pairs": len(grouped_occurrences),
            "activated_distinct_pairs": len(active_rows),
            "inactive_residual_distinct_pairs": len(inactive_residual_rows),
            "terminal_target_distinct_pairs": len(target_counter),
            "terminal_collision_targets": len(collision_targets),
            "maximum_terminal_target_multiplicity": max_target_multiplicity,
            "maximum_transport_path_length": max(
                (int(row["path_length"]) for row in active_rows), default=0
            ),
            "in_parent_completed_pairs": sum(
                row["completion_class"] == "in_parent" for row in active_rows
            ),
            "parent_external_completion_pairs": sum(
                row["completion_class"] == "parent_external" for row in active_rows
            ),
        },
        "masses": {
            "activated_initial_union": serialize_mass(initial_mass),
            "terminal_target_occurrence": serialize_mass(target_occurrence_mass),
            "terminal_target_union": serialize_mass(target_union_mass),
            "transport_collision": serialize_mass(collision_mass),
            "selected_action_incidence_bound": serialize_mass(incidence_mass),
            "direct_target_union": serialize_mass(direct_union_mass),
            "transport_rhs": serialize_mass(rhs),
            "transport_slack": serialize_mass(rhs - initial_mass),
        },
        "terminal_class_profile": class_rows,
        "transport_path_profile": path_rows,
        "completion_profile": completion_rows,
        "resource_signature_profile": resource_signature_rows,
        "child_source_profile": source_signature_rows,
        "first_sponsor_side_profile": side_rows,
        "parent_profile": parent_rows,
        "collision_targets": collision_targets,
        "hashes": {
            "active_rows": canonical_hash(serial_active_rows),
            "inactive_residual_rows": canonical_hash(serial_inactive_rows),
            "terminal_target_counter": canonical_hash(
                [(list(pair), count) for pair, count in sorted(target_counter.items())]
            ),
            "selected_schedules": canonical_hash(
                {
                    parent_class: schedule["selected_rows"]
                    for parent_class, schedule in sorted(schedules.items())
                }
            ),
        },
        "checks": {
            "transport_monotonicity": initial_mass <= target_occurrence_mass,
            "target_first_use_collision_partition": (
                target_union_mass + collision_mass == target_occurrence_mass
            ),
            "direct_incidence_bound": direct_union_mass <= incidence_mass,
            "set_valued_transport_inequality": initial_mass <= rhs,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
