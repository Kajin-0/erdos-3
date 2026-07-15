#!/usr/bin/env python3
"""Summarize edge and saturation payment of second-layer support targets."""
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
)

Pair = tuple[int, int]


def read_classification(path: Path) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing": int(row["missing_index"]),
            }
    return result


def canonical_pair(witness: tuple[int, ...], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            pair = witness[index], witness[index + 1]
            if pair[1] - pair[0] != witness[1] - witness[0]:
                raise AssertionError("canonical support pair changed witness step")
            return pair
    raise AssertionError("hole witness has no adjacent support pair")


def profile_pairs(pairs: set[Pair]) -> dict[str, object]:
    return {
        "pairs": len(pairs),
        "pair_union_mass": serialize_mass(
            sum((pair_weight(pair) for pair in pairs), Fraction())
        ),
    }


def main() -> int:
    if len(sys.argv) != 6:
        raise SystemExit(
            "usage: summarize_s7_incremental_support_target_payment.py "
            "TARGET_REQUESTS_JSON SECOND_CLASSIFICATION_TSV "
            "TERMINAL_PAYMENT_JSON FIRST_CLASSIFICATION_TSV OUTPUT_JSON"
        )
    requests_path = Path(sys.argv[1])
    second_classification_path = Path(sys.argv[2])
    payment_path = Path(sys.argv[3])
    first_classification_path = Path(sys.argv[4])
    output_path = Path(sys.argv[5])

    requests = json.loads(requests_path.read_text(encoding="utf-8"))
    second_classification = read_classification(second_classification_path)
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    first_classification = read_classification(first_classification_path)
    records = requests.get("targets")
    if not isinstance(records, list):
        raise AssertionError("second-layer request payload lacks targets")

    requested_values = {
        value
        for row in records
        if row["status"] == "completion_requested"
        for value in map(int, row["natural_completions"])
    }
    if set(second_classification) != requested_values:
        raise AssertionError("second-layer saturation family mismatch")

    classified_rows: list[dict[str, object]] = []
    targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    selected_holes: dict[int, tuple[tuple[int, ...], int]] = {}
    for row in records:
        weight = Fraction(row["target_weight"])
        if row["status"] == "S7_edge_supported":
            classified_rows.append(
                {
                    **row,
                    "payment_class": "S7_edge_supported",
                    "selected_completion": None,
                    "target_weight_fraction": weight,
                }
            )
            continue

        completions = tuple(map(int, row["natural_completions"]))
        certified = sorted(
            completion
            for completion in completions
            if second_classification[completion]["status"]
            == "certified_S7_hole"
        )
        if certified:
            selected = certified[0]
            payment_class = "certified_S7_hole"
            selected_holes[selected] = (
                second_classification[selected]["witness"],  # type: ignore[index]
                int(second_classification[selected]["missing"]),
            )
        else:
            selected = min(completions)
            if any(
                second_classification[completion]["status"]
                != "S7_admissible_extension"
                for completion in completions
            ):
                raise AssertionError("unknown second-layer saturation status")
            payment_class = "S7_admissible_extension"

        classified = {
            **row,
            "payment_class": payment_class,
            "selected_completion": selected,
            "target_weight_fraction": weight,
        }
        classified_rows.append(classified)
        targets_by_completion[selected].append(classified)

    profile: dict[str, dict[str, object]] = defaultdict(
        lambda: {"targets": 0, "mass": Fraction()}
    )
    for row in classified_rows:
        key = str(row["payment_class"])
        profile[key]["targets"] += 1
        profile[key]["mass"] += row["target_weight_fraction"]

    payment_profile = [
        {
            "class": key,
            "targets": int(values["targets"]),
            "target_union_mass": serialize_mass(values["mass"]),
        }
        for key, values in sorted(
            profile.items(), key=lambda item: -item[1]["mass"]
        )
    ]

    completion_first = Fraction()
    completion_reuse = Fraction()
    for members in targets_by_completion.values():
        total = sum(
            (row["target_weight_fraction"] for row in members), Fraction()
        )
        first = max(row["target_weight_fraction"] for row in members)
        completion_first += first
        completion_reuse += total - first

    second_supports = {
        canonical_pair(witness, missing)
        for witness, missing in selected_holes.values()
    }
    first_supports = {
        canonical_pair(
            record["witness"],  # type: ignore[arg-type]
            int(record["missing"]),
        )
        for record in first_classification.values()
        if record["status"] == "certified_S7_hole"
    }
    source_rows = payment.get("source_rows")
    target_rows = payment.get("target_rows")
    if not isinstance(source_rows, list) or not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks pair ledgers")
    original_sources = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    original_targets = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }
    prior_resource_union = original_sources | first_supports
    prior_any_pair_union = prior_resource_union | original_targets
    new_to_prior_resources = second_supports - prior_resource_union
    new_to_any_prior_ledger = second_supports - prior_any_pair_union

    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}
    owned_activated: set[Pair] = set()
    owned_residual: set[Pair] = set()
    cross_parent: set[Pair] = set()
    for pair in sorted(new_to_prior_resources):
        owners = [
            parent_class
            for parent_class, schedule in schedules.items()
            if set(pair) <= schedule["roots"]
        ]
        if len(owners) > 1:
            raise AssertionError("second-layer support has several parent owners")
        if not owners:
            cross_parent.add(pair)
            continue
        schedule = schedules[owners[0]]
        if set(pair) & schedule["sponsors"]:
            owned_activated.add(pair)
        else:
            if not set(pair) <= schedule["residual"]:
                raise AssertionError("second-layer support has invalid ownership")
            owned_residual.add(pair)

    if owned_activated | owned_residual | cross_parent != new_to_prior_resources:
        raise AssertionError("second-layer support ownership partition failed")

    total_target_mass = sum(
        (row["target_weight_fraction"] for row in classified_rows), Fraction()
    )
    output = {
        "schema": "s7_incremental_support_target_payment_summary_v1",
        "scope": "new terminal targets from first-layer canonical support transport",
        "generation_six_propagated": False,
        "counts": {
            "incremental_targets": len(classified_rows),
            "distinct_completion_requests": len(second_classification),
            "selected_certified_holes": len(selected_holes),
        },
        "target_union_mass": serialize_mass(total_target_mass),
        "payment_profile": payment_profile,
        "completion_first_use": {
            "distinct_selected_completions": len(targets_by_completion),
            "first_target_mass": serialize_mass(completion_first),
            "completion_reuse_mass": serialize_mass(completion_reuse),
        },
        "second_layer_support_identity": {
            "all": profile_pairs(second_supports),
            "already_in_prior_resource_union": profile_pairs(
                second_supports & prior_resource_union
            ),
            "new_to_prior_resource_union": profile_pairs(
                new_to_prior_resources
            ),
            "new_to_any_prior_pair_ledger": profile_pairs(
                new_to_any_prior_ledger
            ),
        },
        "new_support_ownership": {
            "owned_activated": profile_pairs(owned_activated),
            "owned_residual": profile_pairs(owned_residual),
            "cross_parent": profile_pairs(cross_parent),
        },
        "hashes": {
            "classified_target_rows_sha256": canonical_hash(
                [
                    {
                        key: (
                            f"{value.numerator}/{value.denominator}"
                            if isinstance(value, Fraction)
                            else value
                        )
                        for key, value in row.items()
                    }
                    for row in classified_rows
                ]
            ),
            "second_support_pairs_sha256": canonical_hash(
                sorted(second_supports)
            ),
        },
        "checks": {
            "target_mass_partition": (
                sum(
                    (
                        Fraction(row["target_union_mass"]["fraction"])
                        for row in payment_profile
                    ),
                    Fraction(),
                )
                == total_target_mass
            ),
            "completion_first_use_partition": (
                completion_first + completion_reuse
                == sum(
                    (
                        row["target_weight_fraction"]
                        for members in targets_by_completion.values()
                        for row in members
                    ),
                    Fraction(),
                )
            ),
            "second_support_identity_partition": (
                (second_supports & prior_resource_union)
                | new_to_prior_resources
                == second_supports
            ),
            "new_support_ownership_partition": (
                owned_activated | owned_residual | cross_parent
                == new_to_prior_resources
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["summary_payload_sha256"] = hashlib.sha256(
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
