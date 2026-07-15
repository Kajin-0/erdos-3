#!/usr/bin/env python3
"""Classify exact terminal-target payment on the refined R4->F5 frontier.

This probe does not propagate generation six.  It reuses the certified
residual/sponsor retained frontier and the deterministic sponsor-pair transport
map, but replaces the earlier initial-pair completion flag with the prescribed
completion of the terminal direct/backward/residual target.  It also computes
the exact source-weighted collision term in every terminal transport fiber.

The certified S7 root universe is used only for a finite external-root split.
A completion outside S7 is reported as ambient_unresolved, not as a genuine
hole in a hypothetical maximal ambient counterexample.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from probe_residual_sponsor_backbone_split import (
    affine_reference,
    build_split_occurrences,
    pair_weight,
    retain_occurrences,
)
from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    decimal_text,
    fraction_text,
    ordered_pair,
    parent_schedule,
    reconstruct_fourth_recursive,
    serialize_mass,
    transport,
)
from verify_retained_terminal_split import contains_three_term_ap
from verify_s7_regenerative_seed_policy_dependence import all_three_aps

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Pair = tuple[int, int]


def json_value(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, tuple):
        return [json_value(item) for item in value]
    if isinstance(value, list):
        return [json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    return value


def summarize_source_rows(
    rows: list[dict[str, object]], key: str
) -> list[dict[str, object]]:
    buckets: dict[object, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[row[key]].append(row)
    result: list[dict[str, object]] = []
    for value, members in buckets.items():
        initial = sum((row["initial_weight"] for row in members), Fraction())
        target_occurrence = sum(
            (row["target_weight"] for row in members), Fraction()
        )
        result.append(
            {
                "key": value,
                "count": len(members),
                "initial_mass": serialize_mass(initial),
                "target_occurrence_mass": serialize_mass(target_occurrence),
            }
        )
    return sorted(
        result,
        key=lambda row: (
            -Fraction(row["initial_mass"]["fraction"]),  # type: ignore[index]
            str(row["key"]),
        ),
    )


def summarize_target_rows(
    rows: list[dict[str, object]], key: str
) -> list[dict[str, object]]:
    buckets: dict[object, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[row[key]].append(row)
    result: list[dict[str, object]] = []
    for value, members in buckets.items():
        target_union = sum((row["target_weight"] for row in members), Fraction())
        source_collision = sum(
            (row["source_collision_weight"] for row in members), Fraction()
        )
        terminal_collision = sum(
            (row["terminal_collision_weight"] for row in members), Fraction()
        )
        amplification = sum(
            (row["transport_amplification_slack"] for row in members), Fraction()
        )
        result.append(
            {
                "key": value,
                "count": len(members),
                "target_union_mass": serialize_mass(target_union),
                "source_collision_mass": serialize_mass(source_collision),
                "terminal_collision_mass": serialize_mass(terminal_collision),
                "transport_amplification_slack": serialize_mass(amplification),
            }
        )
    return sorted(
        result,
        key=lambda row: (
            -Fraction(row["target_union_mass"]["fraction"]),  # type: ignore[index]
            str(row["key"]),
        ),
    )


def pair_source_class(pair: Pair, schedule: dict[str, object]) -> str:
    sponsors: set[int] = schedule["sponsors"]  # type: ignore[assignment]
    residual: set[int] = schedule["residual"]  # type: ignore[assignment]
    sponsor_count = sum(value in sponsors for value in pair)
    if sponsor_count == 2:
        return "sponsor_sponsor"
    if sponsor_count != 1:
        raise AssertionError("activated pair has invalid sponsor count")
    residual_value = next(value for value in pair if value in residual)
    if residual_value == min(schedule["roots"]):  # type: ignore[arg-type]
        return "residual_minimum_star"
    return "residual_sponsor"


def terminal_semantics(
    target: Pair,
    result: dict[str, object],
    schedule: dict[str, object],
    ambient_roots: set[int],
) -> dict[str, object]:
    terminal_class = str(result["terminal_class"])
    roots: set[int] = schedule["roots"]  # type: ignore[assignment]
    tau: dict[int, int] = schedule["tau"]  # type: ignore[assignment]
    actions: dict[int, dict[str, int]] = schedule["actions"]  # type: ignore[assignment]

    terminal_owner: int | None = None
    terminal_rank: int | None = None
    terminal_step: int | None = None
    terminal_epsilon: int | None = None

    if terminal_class == "residual":
        left, right = target
        completion = 2 * right - left
        witness = tuple(sorted((left, right, completion)))
    else:
        owners = [value for value in target if value in tau]
        if not owners:
            raise AssertionError("non-residual terminal target has no sponsor owner")
        terminal_owner = min(owners, key=lambda value: tau[value])
        other = target[1] if target[0] == terminal_owner else target[0]
        action = actions[terminal_owner]
        terminal_rank = int(action["rank"])
        terminal_step = int(action["q"])
        terminal_epsilon = int(action["epsilon"])

        if terminal_class == "direct":
            middle = int(action["middle"])
            opposite = int(action["opposite"])
            if other == middle:
                completion = opposite
            elif other == opposite:
                completion = middle
            else:
                raise AssertionError("direct target is not a selected-action edge")
            witness = tuple(sorted((terminal_owner, other, completion)))
            if not set(witness) <= roots:
                raise AssertionError("direct target witness left the parent")
        elif terminal_class == "backward":
            completion = 2 * terminal_owner - other
            witness = tuple(sorted((other, terminal_owner, completion)))
        else:
            raise AssertionError(f"unknown terminal class: {terminal_class}")

    if completion in roots:
        completion_status = "in_parent"
        left, middle, right = witness
        if middle - left != right - middle:
            raise AssertionError("in-parent prescribed completion is not a three-AP")
        if not set(target) <= set(witness):
            raise AssertionError("terminal target is not an edge of its witness")
    elif completion in ambient_roots:
        completion_status = "external_in_S7"
    else:
        completion_status = "ambient_unresolved"

    return {
        "terminal_owner": terminal_owner,
        "terminal_rank": terminal_rank,
        "terminal_step": terminal_step,
        "terminal_epsilon": terminal_epsilon,
        "natural_completion": completion,
        "natural_witness": witness,
        "completion_status": completion_status,
    }


def parent_three_ap_capacity(roots: set[int]) -> Fraction:
    load = sum(
        (Fraction(1, int(row[0])) for row in all_three_aps(frozenset(roots))),
        Fraction(),
    )
    return Fraction(5, 2) * load


def build_parent_profile(
    source_rows: list[dict[str, object]],
    schedules: dict[int, dict[str, object]],
) -> list[dict[str, object]]:
    by_parent: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in source_rows:
        by_parent[int(row["parent_class"])].append(row)

    result: list[dict[str, object]] = []
    for parent_class, members in sorted(by_parent.items()):
        targets: dict[Pair, list[dict[str, object]]] = defaultdict(list)
        for row in members:
            targets[row["target"]].append(row)  # type: ignore[index]

        initial = sum((row["initial_weight"] for row in members), Fraction())
        target_union = sum((pair_weight(target) for target in targets), Fraction())
        completed_union = sum(
            (
                pair_weight(target)
                for target, rows in targets.items()
                if any(row["completion_status"] == "in_parent" for row in rows)
            ),
            Fraction(),
        )
        external_union = sum(
            (
                pair_weight(target)
                for target, rows in targets.items()
                if not any(row["completion_status"] == "in_parent" for row in rows)
            ),
            Fraction(),
        )
        source_collision = Fraction()
        terminal_collision = Fraction()
        for target, rows in targets.items():
            weights = [row["initial_weight"] for row in rows]
            source_collision += sum(weights, Fraction()) - max(weights)
            terminal_collision += (len(rows) - 1) * pair_weight(target)

        capacity = parent_three_ap_capacity(
            schedules[parent_class]["roots"]  # type: ignore[arg-type]
        )
        if completed_union > capacity:
            raise AssertionError("completed terminal targets exceed parent AP capacity")

        result.append(
            {
                "parent_class": parent_class,
                "source_pairs": len(members),
                "terminal_targets": len(targets),
                "activated_initial_mass": serialize_mass(initial),
                "target_union_mass": serialize_mass(target_union),
                "completed_target_union_mass": serialize_mass(completed_union),
                "parent_external_target_union_mass": serialize_mass(external_union),
                "source_collision_mass": serialize_mass(source_collision),
                "terminal_collision_mass": serialize_mass(terminal_collision),
                "parent_three_ap_edge_capacity": serialize_mass(capacity),
                "completed_capacity_slack": serialize_mass(capacity - completed_union),
            }
        )
    return sorted(
        result,
        key=lambda row: -Fraction(row["activated_initial_mass"]["fraction"]),  # type: ignore[index]
    )


def main() -> int:
    include_rows = "--include-rows" in sys.argv[1:]
    parents = reconstruct_fourth_recursive()
    parent_by_index = {parent.index: parent for parent in parents}
    schedules = {parent.index: parent_schedule(parent) for parent in parents}
    ambient_roots = set(state_by_depth(7).values)

    for schedule in schedules.values():
        if not schedule["roots"] <= ambient_roots:  # type: ignore[operator]
            raise AssertionError("parent root universe left certified S7")

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

    source_rows: list[dict[str, object]] = []
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

        base = {
            "pair": pair,
            "parent_class": parent_class,
            "occurrence_count": len(members),
            "resource_kinds": tuple(
                sorted({str(member["resource_kind"]) for member in members})
            ),
            "child_sources": tuple(
                sorted({str(member["child_source"]) for member in members})
            ),
            "initial_weight": pair_weight(pair),
        }
        if not (set(pair) & sponsors):
            inactive_residual_rows.append(base)
            continue

        result = transport(pair, schedule)
        target: Pair = result["target"]  # type: ignore[assignment]
        path: list[dict[str, object]] = result["path"]  # type: ignore[assignment]
        semantics = terminal_semantics(target, result, schedule, ambient_roots)
        source_rows.append(
            {
                **base,
                "pair_source_class": pair_source_class(pair, schedule),
                "terminal_class": result["terminal_class"],
                "target": target,
                "target_weight": pair_weight(target),
                "path_length": len(path),
                "path_hash": canonical_hash(path),
                **semantics,
            }
        )

    global_targets: dict[Pair, list[dict[str, object]]] = defaultdict(list)
    for row in source_rows:
        global_targets[row["target"]].append(row)  # type: ignore[index]

    target_rows: list[dict[str, object]] = []
    for target, members in sorted(global_targets.items()):
        source_weights = [row["initial_weight"] for row in members]
        maximum_source_weight = max(source_weights)
        first_candidates = [
            row for row in members if row["initial_weight"] == maximum_source_weight
        ]
        first_source = min(
            first_candidates,
            key=lambda row: (int(row["parent_class"]), row["pair"]),
        )
        source_collision = sum(source_weights, Fraction()) - maximum_source_weight
        target_weight = pair_weight(target)
        terminal_collision = (len(members) - 1) * target_weight
        amplification = terminal_collision - source_collision
        if amplification < 0:
            raise AssertionError("source collision exceeds terminal collision")

        statuses = {str(row["completion_status"]) for row in members}
        if "in_parent" in statuses:
            global_status = "in_parent"
        elif "external_in_S7" in statuses:
            global_status = "external_in_S7"
        else:
            global_status = "ambient_unresolved"

        completion_records = sorted(
            {
                (
                    int(row["parent_class"]),
                    str(row["terminal_class"]),
                    int(row["natural_completion"]),
                    str(row["completion_status"]),
                )
                for row in members
            }
        )
        target_rows.append(
            {
                "target": target,
                "target_weight": target_weight,
                "source_count": len(members),
                "parent_classes": tuple(
                    sorted({int(row["parent_class"]) for row in members})
                ),
                "terminal_classes": tuple(
                    sorted({str(row["terminal_class"]) for row in members})
                ),
                "completion_status": global_status,
                "completion_records": tuple(completion_records),
                "first_source_pair": first_source["pair"],
                "first_source_parent": first_source["parent_class"],
                "first_source_weight": maximum_source_weight,
                "source_collision_weight": source_collision,
                "terminal_collision_weight": terminal_collision,
                "transport_amplification_slack": amplification,
                "source_pairs": tuple(
                    sorted(
                        (
                            int(row["parent_class"]),
                            row["pair"],
                            fraction_text(row["initial_weight"]),
                        )
                        for row in members
                    )
                ),
            }
        )

    initial_mass = sum((row["initial_weight"] for row in source_rows), Fraction())
    first_source_mass = sum(
        (row["first_source_weight"] for row in target_rows), Fraction()
    )
    source_collision_mass = sum(
        (row["source_collision_weight"] for row in target_rows), Fraction()
    )
    target_union_mass = sum(
        (row["target_weight"] for row in target_rows), Fraction()
    )
    target_occurrence_mass = sum(
        (row["target_weight"] * int(row["source_count"]) for row in target_rows),
        Fraction(),
    )
    terminal_collision_mass = sum(
        (row["terminal_collision_weight"] for row in target_rows), Fraction()
    )
    amplification_slack = sum(
        (row["transport_amplification_slack"] for row in target_rows), Fraction()
    )

    if initial_mass != first_source_mass + source_collision_mass:
        raise AssertionError("source first-use/collision identity failed")
    if first_source_mass > target_union_mass:
        raise AssertionError("first-source mass exceeds target union")
    if source_collision_mass > terminal_collision_mass:
        raise AssertionError("source collision does not refine terminal collision")
    if terminal_collision_mass - source_collision_mass != amplification_slack:
        raise AssertionError("transport amplification partition failed")
    if target_union_mass + terminal_collision_mass != target_occurrence_mass:
        raise AssertionError("terminal target first-use/collision partition failed")
    if initial_mass > target_union_mass + source_collision_mass:
        raise AssertionError("source-weighted transport inequality failed")

    status_mass: dict[str, Fraction] = defaultdict(Fraction)
    for row in target_rows:
        status_mass[str(row["completion_status"])] += row["target_weight"]

    parent_profile = build_parent_profile(source_rows, schedules)
    multiplicity_profile = Counter(int(row["source_count"]) for row in target_rows)

    serial_source_rows = json_value(source_rows)
    serial_target_rows = json_value(target_rows)
    output: dict[str, object] = {
        "schema": "terminal_pair_payment_frontier_probe_v2",
        "scope": "certified_residual_sponsor_R4_to_complete_F5_retained_transition",
        "generation_six_propagated": False,
        "ambient_semantics": (
            "S7 membership is certified; outside-S7 completions remain ambient_unresolved"
        ),
        "counts": {
            "parent_states": len(parents),
            "split_retained_states": len(split_retained),
            "resource_occurrences": len(occurrence_rows),
            "distinct_resource_pairs": len(grouped_occurrences),
            "activated_distinct_pairs": len(source_rows),
            "inactive_residual_distinct_pairs": len(inactive_residual_rows),
            "terminal_target_distinct_pairs": len(target_rows),
            "terminal_collision_targets": sum(
                int(row["source_count"]) > 1 for row in target_rows
            ),
            "maximum_terminal_target_multiplicity": max(
                (int(row["source_count"]) for row in target_rows), default=0
            ),
            "maximum_transport_path_length": max(
                (int(row["path_length"]) for row in source_rows), default=0
            ),
            "cross_parent_terminal_targets": sum(
                len(row["parent_classes"]) > 1 for row in target_rows
            ),
            "in_parent_terminal_targets": sum(
                row["completion_status"] == "in_parent" for row in target_rows
            ),
            "external_in_S7_terminal_targets": sum(
                row["completion_status"] == "external_in_S7" for row in target_rows
            ),
            "ambient_unresolved_terminal_targets": sum(
                row["completion_status"] == "ambient_unresolved"
                for row in target_rows
            ),
        },
        "masses": {
            "activated_initial_union": serialize_mass(initial_mass),
            "first_source_mass": serialize_mass(first_source_mass),
            "source_weighted_collision": serialize_mass(source_collision_mass),
            "terminal_target_union": serialize_mass(target_union_mass),
            "terminal_target_occurrence": serialize_mass(target_occurrence_mass),
            "terminal_weight_collision": serialize_mass(terminal_collision_mass),
            "transport_amplification_slack": serialize_mass(amplification_slack),
            "source_weighted_rhs": serialize_mass(
                target_union_mass + source_collision_mass
            ),
            "source_weighted_slack": serialize_mass(
                target_union_mass + source_collision_mass - initial_mass
            ),
            "in_parent_target_union": serialize_mass(
                status_mass.get("in_parent", Fraction())
            ),
            "external_in_S7_target_union": serialize_mass(
                status_mass.get("external_in_S7", Fraction())
            ),
            "ambient_unresolved_target_union": serialize_mass(
                status_mass.get("ambient_unresolved", Fraction())
            ),
        },
        "source_terminal_class_profile": summarize_source_rows(
            source_rows, "terminal_class"
        ),
        "source_pair_class_profile": summarize_source_rows(
            source_rows, "pair_source_class"
        ),
        "source_completion_status_profile": summarize_source_rows(
            source_rows, "completion_status"
        ),
        "source_path_length_profile": summarize_source_rows(
            source_rows, "path_length"
        ),
        "source_parent_profile": summarize_source_rows(source_rows, "parent_class"),
        "target_completion_status_profile": summarize_target_rows(
            target_rows, "completion_status"
        ),
        "target_terminal_class_profile": summarize_target_rows(
            target_rows, "terminal_classes"
        ),
        "target_parent_span_profile": summarize_target_rows(
            [
                {**row, "parent_span": len(row["parent_classes"])}
                for row in target_rows
            ],
            "parent_span",
        ),
        "target_multiplicity_profile": [
            {"multiplicity": value, "targets": multiplicity_profile[value]}
            for value in sorted(multiplicity_profile)
        ],
        "parent_payment_profile": parent_profile,
        "hashes": {
            "source_rows": canonical_hash(serial_source_rows),
            "target_rows": canonical_hash(serial_target_rows),
            "inactive_residual_rows": canonical_hash(json_value(inactive_residual_rows)),
        },
        "checks": {
            "source_first_use_collision_identity": (
                initial_mass == first_source_mass + source_collision_mass
            ),
            "first_source_bounded_by_target_union": (
                first_source_mass <= target_union_mass
            ),
            "source_collision_refines_terminal_collision": (
                source_collision_mass <= terminal_collision_mass
            ),
            "transport_amplification_partition": (
                terminal_collision_mass - source_collision_mass
                == amplification_slack
            ),
            "terminal_target_first_use_collision_partition": (
                target_union_mass + terminal_collision_mass
                == target_occurrence_mass
            ),
            "source_weighted_transport_inequality": (
                initial_mass <= target_union_mass + source_collision_mass
            ),
            "completed_parent_capacity": all(
                Fraction(row["completed_target_union_mass"]["fraction"])
                <= Fraction(row["parent_three_ap_edge_capacity"]["fraction"])
                for row in parent_profile
            ),
        },
    }
    if include_rows:
        output["source_rows"] = serial_source_rows
        output["target_rows"] = serial_target_rows

    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
