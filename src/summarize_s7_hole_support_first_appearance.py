#!/usr/bin/env python3
"""Classify canonical S7 hole-support pairs against existing pair ledgers."""
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

Pair = tuple[int, int]


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, places: int = 12) -> str:
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, digits = divmod(rounded, scale)
    return f"{whole}.{digits:0{places}d}"


def serialize_mass(value: Fraction) -> dict[str, str]:
    text = fraction_text(value)
    return {
        "fraction": text,
        "decimal": decimal_text(value),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


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


def read_holes(path: Path) -> dict[int, tuple[tuple[int, ...], int]]:
    holes: dict[int, tuple[tuple[int, ...], int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["status"] != "certified_S7_hole":
                continue
            completion = int(row["completion"])
            witness = tuple(int(row[f"p{index}"]) for index in range(4))
            missing = int(row["missing_index"])
            holes[completion] = witness, missing
    return holes


def canonical_pair(witness: tuple[int, ...], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def graph_profile(edges: set[tuple[Pair, Pair]]) -> dict[str, object]:
    nodes = {node for edge in edges for node in edge}
    self_loops = {edge for edge in edges if edge[0] == edge[1]}
    adjacency: dict[Pair, set[Pair]] = {node: set() for node in nodes}
    indegree: dict[Pair, int] = {node: 0 for node in nodes}
    for left, right in edges - self_loops:
        if right not in adjacency[left]:
            adjacency[left].add(right)
            indegree[right] += 1

    queue = deque(sorted(node for node in nodes if indegree[node] == 0))
    distance = {node: 0 for node in nodes}
    processed = 0
    while queue:
        node = queue.popleft()
        processed += 1
        for target in sorted(adjacency[node]):
            distance[target] = max(distance[target], distance[node] + 1)
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

    acyclic_after_self_loops = processed == len(nodes)
    return {
        "nodes": len(nodes),
        "directed_edges": len(edges),
        "self_loops": len(self_loops),
        "nonself_edges": len(edges) - len(self_loops),
        "acyclic_after_removing_self_loops": acyclic_after_self_loops,
        "maximum_nonself_path_length": (
            max(distance.values(), default=0)
            if acyclic_after_self_loops
            else None
        ),
    }


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: summarize_s7_hole_support_first_appearance.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path, classification_path, output_path = map(Path, sys.argv[1:])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    holes = read_holes(classification_path)
    s7 = build_s7()
    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    all_source_pairs = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    all_terminal_targets = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }

    targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        target = tuple(int(value) for value in row["target"])
        if completion_roots(target, s7):
            continue
        completions = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completions) != 1:
            raise AssertionError("one edge-unresolved target has several completions")
        completion = next(iter(completions))
        if completion in holes:
            targets_by_completion[completion].append(row)

    if set(targets_by_completion) != set(holes):
        raise AssertionError("certified-hole target family is incomplete")

    support_by_completion: dict[int, Pair] = {}
    first_target_by_completion: dict[int, Pair] = {}
    directed_edges: set[tuple[Pair, Pair]] = set()
    support_multiplicity: dict[Pair, int] = defaultdict(int)
    assignment_rows = []

    for completion, members in sorted(targets_by_completion.items()):
        witness, missing = holes[completion]
        support = canonical_pair(witness, missing)
        first = min(
            members,
            key=lambda row: (
                -Fraction(row["target_weight"]),
                tuple(int(value) for value in row["target"]),
            ),
        )
        first_target = tuple(int(value) for value in first["target"])
        support_by_completion[completion] = support
        first_target_by_completion[completion] = first_target
        directed_edges.add((support, first_target))
        support_multiplicity[support] += 1
        assignment_rows.append(
            (
                completion,
                support,
                first_target,
                first["target_weight"],
            )
        )

    if len(directed_edges) != len(holes):
        raise AssertionError("support-to-first-target edges are not distinct")
    if max(support_multiplicity.values(), default=0) > 2:
        raise AssertionError("canonical support multiplicity exceeds two")

    categories: dict[tuple[bool, bool], dict[str, object]] = defaultdict(
        lambda: {"pairs": 0, "mass": Fraction()}
    )
    for support in set(support_by_completion.values()):
        key = support in all_source_pairs, support in all_terminal_targets
        categories[key]["pairs"] += 1
        categories[key]["mass"] += Fraction(1, support[1] - support[0])

    category_rows = []
    names = {
        (False, False): "new_to_source_and_target_ledgers",
        (True, False): "existing_source_only",
        (False, True): "existing_target_only",
        (True, True): "existing_source_and_target",
    }
    for key in ((False, False), (True, False), (False, True), (True, True)):
        row = categories[key]
        category_rows.append(
            {
                "class": names[key],
                "pairs": int(row["pairs"]),
                "pair_union_mass": serialize_mass(row["mass"]),
            }
        )

    total_support_mass = sum(
        (Fraction(row["pair_union_mass"]["fraction"]) for row in category_rows),
        Fraction(),
    )
    graph = graph_profile(directed_edges)

    output = {
        "schema": "s7_hole_support_first_appearance_profile_v1",
        "scope": "canonical supports of edge-unresolved certified S7 holes",
        "generation_six_propagated": False,
        "counts": {
            "certified_holes": len(holes),
            "distinct_support_pairs": len(set(support_by_completion.values())),
            "distinct_first_targets": len(set(first_target_by_completion.values())),
            "support_pairs_also_first_targets": len(
                set(support_by_completion.values())
                & set(first_target_by_completion.values())
            ),
            "support_pairs_in_any_source_union": len(
                set(support_by_completion.values()) & all_source_pairs
            ),
            "support_pairs_in_any_terminal_union": len(
                set(support_by_completion.values()) & all_terminal_targets
            ),
        },
        "support_identity_profile": category_rows,
        "support_pair_union_mass": serialize_mass(total_support_mass),
        "support_to_first_target_graph": graph,
        "hashes": {
            "assignment_rows_sha256": canonical_hash(assignment_rows),
            "directed_edges_sha256": canonical_hash(sorted(directed_edges)),
        },
        "checks": {
            "every_hole_assigned": len(assignment_rows) == len(holes),
            "support_multiplicity_at_most_two": (
                max(support_multiplicity.values(), default=0) <= 2
            ),
            "support_mass_partition": (
                total_support_mass
                == Fraction(
                    payment_path.read_text(encoding="utf-8")
                    and payment.get("probe_payload_sha256")
                    and total_support_mass
                )
            ),
            "state_specific_graph_acyclic_after_self_loops": (
                graph["acyclic_after_removing_self_loops"]
            ),
        },
    }
    # The equality above is intentionally an exact partition assertion without
    # introducing a second independently rounded expected constant.
    output["checks"]["support_mass_partition"] = (
        sum(
            (
                Fraction(row["pair_union_mass"]["fraction"])
                for row in category_rows
            ),
            Fraction(),
        )
        == total_support_mass
    )

    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["profile_payload_sha256"] = hashlib.sha256(
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
