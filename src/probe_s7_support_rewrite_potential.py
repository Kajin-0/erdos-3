#!/usr/bin/env python3
"""Search finite-state ranking functions for the certified S7 support rewrite.

The scalar-rank probe shows that no tested coordinate, gap, dyadic, short
lexicographic, or small affine potential decreases on every support transition.
This probe enriches a support identity with the deterministic hole event that
first introduced it:

    completion role in the terminal three-AP,
    missing-point orientation in the saturating four-AP.

It then searches for potentials of the form

    Phi(state) = c . features(state) + offset[state_type]

using exact integer difference constraints.  A candidate is reported only when
it strictly decreases on every non-identity transition of the certified fixed
frontier.  The result remains a state-specific diagnostic, not a universal
termination theorem.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_hole_support_closure import (
    build_s7,
    canonical_pair,
    completion_roots,
    read_full_hole_map,
)
from probe_s7_support_transition_rank import (
    Pair,
    dag_longest_path,
    pair_features,
    pair_owner,
    serial_pair,
    tarjan_scc,
)
from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    parent_schedule,
    reconstruct_fourth_recursive,
    transport,
)
from probe_terminal_pair_payment_frontier_v2 import terminal_semantics


def completion_role(target: Pair, completion: int) -> str:
    left, right = target
    gap = right - left
    if completion == left - gap:
        return "left_extension"
    if completion == right + gap:
        return "right_extension"
    if gap % 2 == 0 and completion == left + gap // 2:
        return "midpoint"
    raise AssertionError("completion is not a three-AP completion of target")


def hole_orientation(support: Pair, completion: int) -> str:
    left, right = support
    step = right - left
    if completion == left - step:
        return "left_missing"
    if completion == left + 2 * step:
        return "second_interior_missing"
    if completion == left + 3 * step:
        return "right_missing"
    raise AssertionError("canonical support does not match completion witness")


def label_type(label: dict[str, object]) -> str:
    if label["kind"] == "root":
        return "root"
    return f"{label['completion_role']}|{label['hole_orientation']}"


def state_features(pair: Pair, label: dict[str, object]) -> dict[str, int]:
    features = pair_features(pair)
    completion = int(label["completion"]) if label["completion"] is not None else 0
    features.update(
        {
            "completion": completion,
            "completion_minus_left": completion - pair[0],
            "completion_minus_right": completion - pair[1],
            "introduction_layer": int(label["introduction_layer"]),
        }
    )
    return features


def deterministic_label(
    layer: int,
    support: Pair,
    candidates: list[dict[str, object]],
) -> dict[str, object]:
    if not candidates:
        raise AssertionError("new support has no introducing hole event")
    chosen = min(
        candidates,
        key=lambda row: (
            int(row["completion"]),
            tuple(row["target"]),
            str(row["completion_role"]),
            str(row["hole_orientation"]),
        ),
    )
    return {
        "kind": "hole_support",
        "introduction_layer": layer,
        "completion": int(chosen["completion"]),
        "target": list(chosen["target"]),
        "completion_role": str(chosen["completion_role"]),
        "hole_orientation": str(chosen["hole_orientation"]),
        "support": serial_pair(support),
    }


def difference_constraint_offsets(
    edges: list[dict[str, object]],
    feature_names: tuple[str, ...],
    coefficients: tuple[int, ...],
) -> dict[str, int] | None:
    """Solve o_t <= o_s + c.(x_s-x_t)-1 by Bellman-Ford."""
    types = sorted(
        {str(row["source_type"]) for row in edges}
        | {str(row["target_type"]) for row in edges}
    )
    index = {name: position for position, name in enumerate(types)}
    constraints: list[tuple[int, int, int]] = []
    for row in edges:
        source_features = row["source_features"]
        target_features = row["target_features"]
        bound = (
            sum(
                coefficient
                * (
                    int(source_features[name])  # type: ignore[index]
                    - int(target_features[name])  # type: ignore[index]
                )
                for coefficient, name in zip(coefficients, feature_names)
            )
            - 1
        )
        constraints.append(
            (
                index[str(row["source_type"])],
                index[str(row["target_type"])],
                bound,
            )
        )

    distance = [0] * len(types)
    for _ in range(len(types) - 1):
        changed = False
        for source, target, bound in constraints:
            candidate = distance[source] + bound
            if distance[target] > candidate:
                distance[target] = candidate
                changed = True
        if not changed:
            break

    for source, target, bound in constraints:
        if distance[target] > distance[source] + bound:
            return None

    offsets = {name: distance[position] for name, position in index.items()}
    for row in edges:
        source_features = row["source_features"]
        target_features = row["target_features"]
        source_value = offsets[str(row["source_type"])] + sum(
            coefficient * int(source_features[name])  # type: ignore[index]
            for coefficient, name in zip(coefficients, feature_names)
        )
        target_value = offsets[str(row["target_type"])] + sum(
            coefficient * int(target_features[name])  # type: ignore[index]
            for coefficient, name in zip(coefficients, feature_names)
        )
        if source_value <= target_value:
            raise AssertionError("difference-constraint solution failed verification")
    return offsets


def search_typed_affine(
    edges: list[dict[str, object]],
) -> list[dict[str, object]]:
    feature_sets = (
        ("completion",),
        ("gap",),
        ("completion", "gap"),
        ("completion", "left"),
        ("completion", "right"),
        ("completion_minus_left", "gap"),
        ("completion_minus_right", "gap"),
        ("completion", "gap", "left"),
        ("completion", "gap", "right"),
        ("completion", "gap", "v2_gap"),
        ("left", "right", "gap"),
    )
    matches: list[dict[str, object]] = []
    for names in feature_sets:
        for coefficients in product(range(-6, 7), repeat=len(names)):
            if not any(coefficients):
                continue
            offsets = difference_constraint_offsets(edges, names, coefficients)
            if offsets is None:
                continue
            drops = []
            for row in edges:
                source_features = row["source_features"]
                target_features = row["target_features"]
                source_value = offsets[str(row["source_type"])] + sum(
                    coefficient * int(source_features[name])  # type: ignore[index]
                    for coefficient, name in zip(coefficients, names)
                )
                target_value = offsets[str(row["target_type"])] + sum(
                    coefficient * int(target_features[name])  # type: ignore[index]
                    for coefficient, name in zip(coefficients, names)
                )
                drops.append(source_value - target_value)
            matches.append(
                {
                    "features": names,
                    "coefficients": coefficients,
                    "type_offsets": offsets,
                    "minimum_drop": min(drops),
                    "maximum_drop": max(drops),
                }
            )
    matches.sort(
        key=lambda row: (
            len(row["features"]),
            sum(abs(value) for value in row["coefficients"]),  # type: ignore[arg-type]
            max(abs(value) for value in row["type_offsets"].values()),  # type: ignore[union-attr]
            -int(row["minimum_drop"]),
        )
    )
    return matches[:20]


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_support_rewrite_potential.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )
    payment_path = Path(sys.argv[1])
    hole_map_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    target_rows = payment.get("target_rows")
    if not isinstance(source_rows, list) or not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    holes = read_full_hole_map(hole_map_path)
    s7 = build_s7()
    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}

    seen_resources: set[Pair] = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    seen_targets: set[Pair] = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }
    labels: dict[Pair, dict[str, object]] = {
        pair: {
            "kind": "root",
            "introduction_layer": -1,
            "completion": None,
            "target": None,
            "completion_role": None,
            "hole_orientation": None,
            "support": serial_pair(pair),
        }
        for pair in seen_resources
    }

    frontier: dict[Pair, dict[str, object]] = {}
    for row in target_rows:
        target = tuple(int(value) for value in row["target"])
        frontier[target] = {
            "natural_completions": {
                int(record[2]) for record in row["completion_records"]
            },
            "origins": set(),
        }

    transition_rows: list[dict[str, object]] = []
    layer_profile: list[dict[str, object]] = []

    for layer_index in range(20):
        if not frontier:
            break

        events_by_support: dict[Pair, list[dict[str, object]]] = defaultdict(list)
        target_events: dict[Pair, dict[str, object]] = {}
        for target, record in sorted(frontier.items()):
            completions: set[int] = record["natural_completions"]  # type: ignore[assignment]
            if completion_roots(target, s7):
                continue
            certified = sorted(value for value in completions if value in holes)
            if not certified:
                continue
            completion = certified[0]
            support = canonical_pair(*holes[completion])
            event = {
                "completion": completion,
                "target": serial_pair(target),
                "completion_role": completion_role(target, completion),
                "hole_orientation": hole_orientation(support, completion),
                "support": serial_pair(support),
            }
            events_by_support[support].append(event)
            target_events[target] = event

        support_pairs = set(events_by_support)
        new_supports = support_pairs - seen_resources
        for support in sorted(new_supports):
            labels[support] = deterministic_label(
                layer_index, support, events_by_support[support]
            )
        seen_resources.update(new_supports)

        for target, event in sorted(target_events.items()):
            support = tuple(event["support"])  # type: ignore[arg-type]
            for origin in sorted(frontier[target]["origins"]):  # type: ignore[arg-type]
                if origin not in labels or support not in labels:
                    raise AssertionError("transition endpoint lacks first-appearance label")
                source_label = labels[origin]
                target_label = labels[support]
                transition_rows.append(
                    {
                        "layer": layer_index,
                        "source_support": serial_pair(origin),
                        "target_support": serial_pair(support),
                        "frontier_target": serial_pair(target),
                        "selected_completion": int(event["completion"]),
                        "source_type": label_type(source_label),
                        "target_type": label_type(target_label),
                        "source_label": source_label,
                        "target_label": target_label,
                        "source_features": state_features(origin, source_label),
                        "target_features": state_features(support, target_label),
                    }
                )

        activated: dict[Pair, int] = {}
        residual = 0
        cross_parent = 0
        for support in sorted(new_supports):
            owner = pair_owner(support, schedules)
            if owner["owner_kind"] == "activated":
                activated[support] = int(owner["owner_class"])
            elif owner["owner_kind"] == "residual":
                residual += 1
            else:
                cross_parent += 1

        produced: dict[Pair, dict[str, object]] = {}
        for support, parent_class in sorted(activated.items()):
            schedule = schedules[parent_class]
            result = transport(support, schedule)
            target: Pair = result["target"]  # type: ignore[assignment]
            semantics = terminal_semantics(target, result, schedule, s7)
            completion = int(semantics["natural_completion"])
            if target not in produced:
                produced[target] = {
                    "natural_completions": set(),
                    "origins": set(),
                }
            produced[target]["natural_completions"].add(completion)  # type: ignore[union-attr]
            produced[target]["origins"].add(support)  # type: ignore[union-attr]

        produced_targets = set(produced)
        new_targets = produced_targets - seen_targets
        next_frontier = {target: produced[target] for target in sorted(new_targets)}
        seen_targets.update(produced_targets)
        layer_profile.append(
            {
                "layer": layer_index,
                "input_targets": len(frontier),
                "hole_events": len(target_events),
                "support_pairs": len(support_pairs),
                "new_supports": len(new_supports),
                "activated_new_supports": len(activated),
                "residual_new_supports": residual,
                "cross_parent_new_supports": cross_parent,
                "new_targets": len(new_targets),
            }
        )
        frontier = next_frontier

    if frontier:
        raise AssertionError("rewrite-potential probe did not reach closure")

    nonself_rows = [
        row
        for row in transition_rows
        if row["source_support"] != row["target_support"]
    ]
    unique_edges = {
        (
            tuple(row["source_support"]),  # type: ignore[arg-type]
            tuple(row["target_support"]),  # type: ignore[arg-type]
        )
        for row in transition_rows
    }
    components = tarjan_scc(unique_edges)
    nontrivial_components = [component for component in components if len(component) > 1]
    dag, longest = dag_longest_path(unique_edges)

    type_edges = {
        (str(row["source_type"]), str(row["target_type"]))
        for row in nonself_rows
    }
    type_nodes = sorted({node for edge in type_edges for node in edge})
    type_profile = Counter(
        f"{row['source_type']}->{row['target_type']}"
        for row in nonself_rows
    )

    feature_relations: dict[str, Counter[str]] = defaultdict(Counter)
    for row in nonself_rows:
        source = row["source_features"]
        target = row["target_features"]
        for name in (
            "completion",
            "completion_minus_left",
            "completion_minus_right",
            "left",
            "right",
            "gap",
            "sum",
            "v2_gap",
            "odd_gap",
        ):
            source_value = int(source[name])  # type: ignore[index]
            target_value = int(target[name])  # type: ignore[index]
            relation = (
                "decrease"
                if target_value < source_value
                else "increase"
                if target_value > source_value
                else "equal"
            )
            feature_relations[name][relation] += 1

    typed_candidates = search_typed_affine(nonself_rows)
    payload = {
        "schema": "s7_support_rewrite_potential_probe_v1",
        "scope": "first-appearance-labeled rewrite on fixed certified S7 closure",
        "generation_six_propagated": False,
        "closure": {
            "layers_processed": len(layer_profile),
            "terminated": not frontier,
            "transition_rows": len(transition_rows),
            "nonidentity_transition_rows": len(nonself_rows),
            "unique_support_edges": len(unique_edges),
            "nontrivial_strong_components": len(nontrivial_components),
            "acyclic_after_self_loops": dag,
            "longest_nonself_path": longest,
        },
        "layer_profile": layer_profile,
        "state_types": type_nodes,
        "type_transition_profile": dict(sorted(type_profile.items())),
        "feature_relation_profile": {
            name: dict(sorted(profile.items()))
            for name, profile in feature_relations.items()
        },
        "typed_affine_candidates": typed_candidates,
        "hashes": {
            "transition_rows": canonical_hash(transition_rows),
            "first_appearance_labels": canonical_hash(
                sorted((serial_pair(pair), label) for pair, label in labels.items())
            ),
        },
        "checks": {
            "five_layer_closure_reproduced": len(layer_profile) == 5,
            "closure_terminated": not frontier,
            "support_graph_acyclic_after_self_loops": dag,
            "no_nontrivial_support_scc": not nontrivial_components,
        },
        "transition_rows": transition_rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
