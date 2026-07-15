#!/usr/bin/env python3
"""Certify terminal versus recursive heavy completion-step shells on S7."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_s7_hole_support_closure import build_s7, canonical_pair, completion_roots
from probe_sponsor_pair_transport_frontier import canonical_hash, serialize_mass

Pair = tuple[int, int]


def read_classification(path: Path) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing_index": int(row["missing_index"]),
            }
    return result


def target_orientation(target: Pair, completion: int) -> int:
    left, right = target
    gap = right - left
    if completion == left - gap:
        return 1
    if completion == right + gap:
        return -1
    raise AssertionError("selected completion is not an endpoint extension")


def harmonic(values: set[int] | tuple[int, ...]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def three_ap_witness(values: tuple[int, ...]) -> tuple[int, int, int] | None:
    lookup = set(values)
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if (left + right) % 2:
                continue
            middle = (left + right) // 2
            if middle in lookup:
                return left, middle, right
    return None


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_completion_step_terminal_split.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )

    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    classifications = read_classification(classification_path)
    target_rows = payment.get("target_rows")
    if not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks target rows")
    s7 = build_s7()

    fibers: dict[tuple[Pair, int, int], set[int]] = defaultdict(set)
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
            raise AssertionError("edge-unresolved target lacks one completion")
        completion = next(iter(completions))
        classification = classifications.get(completion)
        if classification is None or classification["status"] != "certified_S7_hole":
            continue
        support = canonical_pair(
            classification["witness"],  # type: ignore[arg-type]
            int(classification["missing_index"]),
        )
        orientation = target_orientation(target, completion)
        fibers[(support, completion, orientation)].add(target[1] - target[0])

    by_support: dict[Pair, list[tuple[int, int, set[int]]]] = defaultdict(list)
    for (support, completion, orientation), steps in fibers.items():
        by_support[support].append((completion, orientation, steps))

    terminal_rows: list[tuple[object, ...]] = []
    recursive_rows: list[tuple[object, ...]] = []
    affine_tokens: set[tuple[int, int, int, tuple[int, ...]]] = set()
    numerical_multiplicity = Counter()
    shell_size_profile = Counter()
    terminal_mass = Fraction()
    recursive_mass = Fraction()
    heavy_fibers = 0

    for support, rows in sorted(by_support.items()):
        multiplicity = len(rows)
        threshold = Fraction(1, multiplicity * (support[1] - support[0]))
        for completion, orientation, steps in sorted(rows):
            if harmonic(steps) <= threshold:
                continue
            heavy_fibers += 1
            shells: dict[int, list[int]] = defaultdict(list)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].append(step)
            for shell_base, values in sorted(shells.items()):
                state = tuple(sorted(values))
                token = (completion, orientation, shell_base, state)
                if token in affine_tokens:
                    raise AssertionError("affine heavy-shell token repeated")
                affine_tokens.add(token)
                numerical_multiplicity[(shell_base, state)] += 1
                shell_size_profile[len(state)] += 1
                mass = harmonic(state)
                witness = three_ap_witness(state)
                row = (
                    completion,
                    orientation,
                    shell_base,
                    state,
                    support,
                    f"{mass.numerator}/{mass.denominator}",
                    witness,
                )
                if witness is None:
                    terminal_rows.append(row)
                    terminal_mass += mass
                else:
                    recursive_rows.append(row)
                    recursive_mass += mass

    total_mass = terminal_mass + recursive_mass
    maximum_numerical_multiplicity = max(numerical_multiplicity.values(), default=0)
    output = {
        "schema": "s7_completion_step_heavy_terminal_split_v1",
        "scope": "resolved heavy completion-step shells on the refined S7 terminal frontier",
        "generation_six_propagated": False,
        "counts": {
            "heavy_completion_fibers": heavy_fibers,
            "resolved_heavy_shells": len(terminal_rows) + len(recursive_rows),
            "terminal_heavy_shells": len(terminal_rows),
            "recursive_heavy_shells": len(recursive_rows),
            "affine_first_appearance_tokens": len(affine_tokens),
            "distinct_numerical_shell_states": len(numerical_multiplicity),
            "maximum_numerical_state_multiplicity": maximum_numerical_multiplicity,
        },
        "masses": {
            "total_heavy_shell_mass": serialize_mass(total_mass),
            "terminal_heavy_shell_mass": serialize_mass(terminal_mass),
            "recursive_heavy_shell_mass": serialize_mass(recursive_mass),
        },
        "shell_size_profile": [
            {"points": size, "shells": shell_size_profile[size]}
            for size in sorted(shell_size_profile)
        ],
        "hashes": {
            "terminal_rows": canonical_hash(terminal_rows),
            "recursive_rows": canonical_hash(recursive_rows),
            "affine_tokens": canonical_hash(sorted(affine_tokens)),
        },
        "checks": {
            "affine_token_injective": len(affine_tokens)
            == len(terminal_rows) + len(recursive_rows),
            "mass_partition": total_mass == terminal_mass + recursive_mass,
            "all_s7_heavy_shells_terminal": not recursive_rows,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
