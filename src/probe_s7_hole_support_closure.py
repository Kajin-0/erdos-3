#!/usr/bin/env python3
"""Iterate the certified S7 hole-support closure on a fixed retained frontier.

The probe starts from the terminal targets of the source-weighted R4->F5
transport certificate.  At every layer it applies the following deterministic
order:

1. absorb targets that are edges of any three-AP in S7;
2. classify prescribed completion requests by the complete S7 shell saturation
   map;
3. assign one canonical adjacent support pair to every selected certified hole;
4. insert each support identity at most once;
5. transport only newly inserted support pairs that are sponsor-activated inside
   one certified fourth-generation parent;
6. continue only with genuinely new terminal target identities.

The computation never propagates a retained sixth generation.  It is an exact
finite closure diagnostic for the fixed certified frontier, not a universal
whole-tree theorem.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    pair_weight,
    parent_schedule,
    reconstruct_fourth_recursive,
    serialize_mass,
    transport,
)
from probe_terminal_pair_payment_frontier_v2 import terminal_semantics

Pair = tuple[int, int]


def build_s7() -> set[int]:
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    scales = (64, 256, 2048, 8192, 32768, 262144, 1048576)
    separations = (61, 303, 1597, 8195, 93476, 230164)
    state = {scales[0] + value for value in base}
    for index, separation in enumerate(separations):
        state = {
            scales[index + 1] + value + layer * separation
            for value in ({0} | state)
            for layer in range(3)
        }
    if (len(state), min(state), max(state)) != (9840, 1048576, 2021668):
        raise AssertionError("certified S7 reconstruction mismatch")
    return state


def completion_roots(pair: Pair, roots: set[int]) -> set[int]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return candidates & roots


def read_full_hole_map(
    path: Path,
) -> dict[int, tuple[tuple[int, int, int, int], int]]:
    holes: dict[int, tuple[tuple[int, int, int, int], int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            witness = tuple(int(row[f"p{index}"]) for index in range(4))
            missing = int(row["missing_index"])
            holes[completion] = witness, missing
    if len(holes) != 514_889:
        raise AssertionError(
            f"complete S7 saturation map changed: {len(holes)}"
        )
    return holes


def canonical_pair(witness: tuple[int, ...], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def pair_union_mass(pairs: set[Pair]) -> Fraction:
    return sum((pair_weight(pair) for pair in pairs), Fraction())


def target_union_mass(targets: set[Pair]) -> Fraction:
    return pair_union_mass(targets)


def profile_pairs(pairs: set[Pair]) -> dict[str, object]:
    return {
        "pairs": len(pairs),
        "pair_union_mass": serialize_mass(pair_union_mass(pairs)),
    }


def classify_frontier(
    frontier: dict[Pair, set[int]],
    s7: set[int],
    holes: dict[int, tuple[tuple[int, int, int, int], int]],
) -> tuple[
    dict[str, set[Pair]],
    dict[int, set[Pair]],
    dict[int, Pair],
]:
    classes: dict[str, set[Pair]] = defaultdict(set)
    targets_by_hole: dict[int, set[Pair]] = defaultdict(set)
    support_by_hole: dict[int, Pair] = {}
    lower, upper = 1_048_576, 2_097_151

    for target, natural_completions in sorted(frontier.items()):
        if completion_roots(target, s7):
            classes["S7_edge_supported"].add(target)
            continue

        certified = sorted(
            completion for completion in natural_completions if completion in holes
        )
        if certified:
            completion = certified[0]
            classes["certified_S7_hole"].add(target)
            targets_by_hole[completion].add(target)
            support_by_hole[completion] = canonical_pair(*holes[completion])
            continue

        if natural_completions and all(
            lower <= completion <= upper for completion in natural_completions
        ):
            classes["S7_admissible_extension"].add(target)
        else:
            classes["ambient_outside_S7_shell"].add(target)

    return classes, targets_by_hole, support_by_hole


def combined_source_ledger(
    source_weights_by_target: dict[Pair, list[Fraction]],
) -> tuple[Fraction, Fraction]:
    target_union = sum(
        (pair_weight(target) for target in source_weights_by_target), Fraction()
    )
    source_collision = sum(
        (
            sum(weights, Fraction()) - max(weights)
            for weights in source_weights_by_target.values()
        ),
        Fraction(),
    )
    return target_union, source_collision


def serialize_transport_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    result = []
    for row in rows:
        result.append(
            {
                key: (
                    f"{value.numerator}/{value.denominator}"
                    if isinstance(value, Fraction)
                    else list(value)
                    if isinstance(value, tuple)
                    else value
                )
                for key, value in row.items()
            }
        )
    return result


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_hole_support_closure.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )
    payment_path = Path(sys.argv[1])
    hole_map_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    holes = read_full_hole_map(hole_map_path)
    s7 = build_s7()
    source_rows = payment.get("source_rows")
    target_rows = payment.get("target_rows")
    if not isinstance(source_rows, list) or not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}

    seen_resources: set[Pair] = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    seen_targets: set[Pair] = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }

    source_weights_by_target: dict[Pair, list[Fraction]] = defaultdict(list)
    for row in target_rows:
        target = tuple(int(value) for value in row["target"])
        for record in row["source_pairs"]:
            source_weights_by_target[target].append(Fraction(record[2]))

    frontier: dict[Pair, set[int]] = {}
    for row in target_rows:
        target = tuple(int(value) for value in row["target"])
        frontier[target] = {
            int(record[2]) for record in row["completion_records"]
        }

    original_initial_mass = Fraction(
        payment["masses"]["activated_initial_union"]["fraction"]
    )
    cumulative_added_source_mass = Fraction()
    cumulative_supports: set[Pair] = set()
    residual_supports: set[Pair] = set()
    cross_parent_supports: set[Pair] = set()
    all_transport_rows: list[dict[str, object]] = []
    all_assignment_rows: list[tuple[object, ...]] = []
    layers: list[dict[str, object]] = []

    for layer_index in range(20):
        if not frontier:
            break

        classes, targets_by_hole, support_by_hole = classify_frontier(
            frontier, s7, holes
        )
        selected_holes = set(targets_by_hole)
        support_pairs = set(support_by_hole.values())
        support_multiplicity = Counter(support_by_hole.values())
        if max(support_multiplicity.values(), default=0) > 2:
            raise AssertionError("canonical support multiplicity exceeds two")

        existing_supports = support_pairs & seen_resources
        new_supports = support_pairs - seen_resources
        seen_resources.update(new_supports)
        cumulative_supports.update(support_pairs)

        owned_activated: dict[Pair, int] = {}
        owned_residual: set[Pair] = set()
        cross_parent: set[Pair] = set()
        for pair in sorted(new_supports):
            owners = [
                parent_class
                for parent_class, schedule in schedules.items()
                if set(pair) <= schedule["roots"]
            ]
            if len(owners) > 1:
                raise AssertionError("support pair belongs to several parents")
            if not owners:
                cross_parent.add(pair)
                continue
            parent_class = owners[0]
            schedule = schedules[parent_class]
            if set(pair) & schedule["sponsors"]:
                owned_activated[pair] = parent_class
            else:
                if not set(pair) <= schedule["residual"]:
                    raise AssertionError("owned support is neither sponsor nor residual")
                owned_residual.add(pair)

        residual_supports.update(owned_residual)
        cross_parent_supports.update(cross_parent)
        if set(owned_activated) | owned_residual | cross_parent != new_supports:
            raise AssertionError("support ownership partition failed")

        produced: dict[Pair, dict[str, object]] = {}
        layer_transport_rows: list[dict[str, object]] = []
        for pair, parent_class in sorted(owned_activated.items()):
            schedule = schedules[parent_class]
            result = transport(pair, schedule)
            target: Pair = result["target"]  # type: ignore[assignment]
            semantics = terminal_semantics(target, result, schedule, s7)
            natural_completion = int(semantics["natural_completion"])
            row = {
                "layer": layer_index,
                "source_pair": pair,
                "source_parent": parent_class,
                "source_weight": pair_weight(pair),
                "target": target,
                "target_weight": pair_weight(target),
                "terminal_class": result["terminal_class"],
                "path_length": len(result["path"]),
                "natural_completion": natural_completion,
            }
            layer_transport_rows.append(row)
            all_transport_rows.append(row)
            source_weights_by_target[target].append(pair_weight(pair))
            if target not in produced:
                produced[target] = {
                    "natural_completions": set(),
                    "source_count": 0,
                }
            produced[target]["natural_completions"].add(natural_completion)
            produced[target]["source_count"] += 1

        produced_targets = set(produced)
        existing_target_overlap = produced_targets & seen_targets
        new_targets = produced_targets - seen_targets
        next_frontier = {
            target: set(produced[target]["natural_completions"])
            for target in sorted(new_targets)
        }
        seen_targets.update(produced_targets)

        added_source_mass = pair_union_mass(set(owned_activated))
        cumulative_added_source_mass += added_source_mass
        combined_target_mass, combined_collision = combined_source_ledger(
            source_weights_by_target
        )
        combined_initial_mass = original_initial_mass + cumulative_added_source_mass
        combined_rhs = combined_target_mass + combined_collision
        if combined_initial_mass > combined_rhs:
            raise AssertionError("closure source-weighted inequality failed")

        class_profile = []
        for name in (
            "S7_edge_supported",
            "certified_S7_hole",
            "S7_admissible_extension",
            "ambient_outside_S7_shell",
        ):
            targets = classes.get(name, set())
            class_profile.append(
                {
                    "class": name,
                    "targets": len(targets),
                    "target_union_mass": serialize_mass(
                        target_union_mass(targets)
                    ),
                }
            )

        for completion, targets in sorted(targets_by_hole.items()):
            support = support_by_hole[completion]
            all_assignment_rows.append(
                (
                    layer_index,
                    completion,
                    support,
                    tuple(sorted(targets)),
                )
            )

        layer = {
            "layer": layer_index,
            "input_frontier": {
                "targets": len(frontier),
                "target_union_mass": serialize_mass(
                    target_union_mass(set(frontier))
                ),
            },
            "target_payment_profile": class_profile,
            "certified_holes": len(selected_holes),
            "support_identity": {
                "all": profile_pairs(support_pairs),
                "already_seen": profile_pairs(existing_supports),
                "new": profile_pairs(new_supports),
            },
            "new_support_ownership": {
                "owned_activated": profile_pairs(set(owned_activated)),
                "owned_residual": profile_pairs(owned_residual),
                "cross_parent": profile_pairs(cross_parent),
            },
            "transport": {
                "sources": len(layer_transport_rows),
                "source_initial_mass": serialize_mass(added_source_mass),
                "target_occurrence_mass": serialize_mass(
                    sum(
                        (row["target_weight"] for row in layer_transport_rows),
                        Fraction(),
                    )
                ),
                "target_union_mass": serialize_mass(
                    target_union_mass(produced_targets)
                ),
                "produced_targets": len(produced_targets),
                "existing_target_overlap": len(existing_target_overlap),
                "existing_target_overlap_mass": serialize_mass(
                    target_union_mass(existing_target_overlap)
                ),
                "new_targets": len(new_targets),
                "new_target_union_mass": serialize_mass(
                    target_union_mass(new_targets)
                ),
                "terminal_class_counts": dict(
                    sorted(
                        Counter(
                            str(row["terminal_class"])
                            for row in layer_transport_rows
                        ).items()
                    )
                ),
                "path_length_counts": {
                    str(key): value
                    for key, value in sorted(
                        Counter(
                            int(row["path_length"])
                            for row in layer_transport_rows
                        ).items()
                    )
                },
            },
            "cumulative_source_weighted_ledger": {
                "initial_mass": serialize_mass(combined_initial_mass),
                "terminal_target_union_mass": serialize_mass(
                    combined_target_mass
                ),
                "source_collision_mass": serialize_mass(combined_collision),
                "rhs": serialize_mass(combined_rhs),
                "slack": serialize_mass(combined_rhs - combined_initial_mass),
            },
        }
        layers.append(layer)

        if not owned_activated or not next_frontier:
            frontier = next_frontier
            break
        frontier = next_frontier
    else:
        raise AssertionError("S7 support closure exceeded twenty layers")

    final_target_mass, final_collision = combined_source_ledger(
        source_weights_by_target
    )
    final_initial_mass = original_initial_mass + cumulative_added_source_mass
    final_rhs = final_target_mass + final_collision

    output = {
        "schema": "s7_hole_support_closure_probe_v1",
        "scope": "fixed certified residual-sponsor R4_to_F5 terminal frontier",
        "generation_six_propagated": False,
        "saturation_map": {
            "certified_shell_holes": len(holes),
            "S7_shell_admissible_absent": 523_847,
        },
        "closure": {
            "layers_processed": len(layers),
            "terminated": not frontier or not layers[-1]["new_support_ownership"][
                "owned_activated"
            ]["pairs"],
            "remaining_unprocessed_targets": len(frontier),
            "seen_resource_pairs": len(seen_resources),
            "seen_terminal_targets": len(seen_targets),
            "cumulative_canonical_support_pairs": len(cumulative_supports),
            "cumulative_added_activated_support_pairs": len(all_transport_rows),
            "cumulative_residual_support_pairs": len(residual_supports),
            "cumulative_cross_parent_support_pairs": len(cross_parent_supports),
        },
        "layers": layers,
        "final_source_weighted_ledger": {
            "initial_mass": serialize_mass(final_initial_mass),
            "terminal_target_union_mass": serialize_mass(final_target_mass),
            "source_collision_mass": serialize_mass(final_collision),
            "rhs": serialize_mass(final_rhs),
            "slack": serialize_mass(final_rhs - final_initial_mass),
        },
        "untransported_support_sinks": {
            "residual": profile_pairs(residual_supports),
            "cross_parent": profile_pairs(cross_parent_supports),
        },
        "hashes": {
            "support_assignment_rows_sha256": canonical_hash(
                all_assignment_rows
            ),
            "transport_rows_sha256": canonical_hash(
                serialize_transport_rows(all_transport_rows)
            ),
            "seen_resource_pairs_sha256": canonical_hash(
                sorted(seen_resources)
            ),
            "seen_terminal_targets_sha256": canonical_hash(
                sorted(seen_targets)
            ),
        },
        "checks": {
            "canonical_support_multiplicity_at_most_two": True,
            "resource_identity_inserted_at_most_once": (
                len({row["source_pair"] for row in all_transport_rows})
                == len(all_transport_rows)
            ),
            "final_source_weighted_transport_inequality": (
                final_initial_mass <= final_rhs
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output_path.write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
