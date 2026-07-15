#!/usr/bin/env python3
"""Profile star-rectangle first appearance on repeated S7 heavy states."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_s7_heavy_state_reference_reserve import dyadic_band, harmonic
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


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_star_rectangle_first_appearance.py "
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

    by_oriented_state: dict[tuple[int, tuple[int, ...], int], list[int]] = defaultdict(list)
    for support, rows in sorted(by_support.items()):
        multiplicity = len(rows)
        threshold = Fraction(1, multiplicity * (support[1] - support[0]))
        for completion, orientation, steps in sorted(rows):
            if harmonic(steps) <= threshold:
                continue
            shells: dict[int, list[int]] = defaultdict(list)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].append(step)
            for shell_base, values in sorted(shells.items()):
                state = tuple(sorted(values))
                by_oriented_state[(shell_base, state, orientation)].append(completion)

    full_configurations: set[tuple[int, int, int, int]] = set()
    abstract_multiplicity = Counter()
    occurrence_mass = Fraction()
    full_rows: list[tuple[object, ...]] = []

    for (_shell, state, orientation), completions in sorted(by_oriented_state.items()):
        references = sorted(completions)
        if len(references) <= 1:
            continue
        base = references[0]
        for completion in references[1:]:
            difference = completion - base
            for step in state:
                configuration = (
                    base + orientation * step,
                    base + 2 * orientation * step,
                    completion + orientation * step,
                    completion + 2 * orientation * step,
                )
                if configuration in full_configurations:
                    raise AssertionError("star-rectangle configuration repeated")
                full_configurations.add(configuration)
                band = dyadic_band(difference, step)
                abstract = (difference, step, band, orientation)
                abstract_multiplicity[abstract] += 1
                occurrence_mass += Fraction(1, step)
                recovered_base = 2 * configuration[0] - configuration[1]
                recovered_completion = 2 * configuration[2] - configuration[3]
                recovered_signed_step = configuration[1] - configuration[0]
                if (
                    recovered_base != base
                    or recovered_completion != completion
                    or abs(recovered_signed_step) != step
                    or (1 if recovered_signed_step > 0 else -1) != orientation
                ):
                    raise AssertionError("star rectangle failed inverse reconstruction")
                full_rows.append(
                    (
                        configuration,
                        base,
                        completion,
                        difference,
                        step,
                        band,
                        orientation,
                    )
                )

    abstract_union_mass = sum(
        (Fraction(1, token[1]) for token in abstract_multiplicity), Fraction()
    )
    abstract_collision_mass = occurrence_mass - abstract_union_mass
    multiplicity_profile = Counter(abstract_multiplicity.values())

    output = {
        "schema": "s7_star_rectangle_first_appearance_profile_v1",
        "scope": "repeated oriented heavy completion-step states on S7",
        "generation_six_propagated": False,
        "counts": {
            "star_rectangle_configurations": len(full_configurations),
            "distinct_abstract_aspect_tokens": len(abstract_multiplicity),
            "reused_abstract_aspect_tokens": sum(
                multiplicity > 1 for multiplicity in abstract_multiplicity.values()
            ),
            "maximum_abstract_aspect_multiplicity": max(
                abstract_multiplicity.values(), default=0
            ),
        },
        "masses": {
            "star_rectangle_occurrence_mass": serialize_mass(occurrence_mass),
            "abstract_aspect_union_mass": serialize_mass(abstract_union_mass),
            "abstract_aspect_collision_mass": serialize_mass(
                abstract_collision_mass
            ),
        },
        "abstract_multiplicity_profile": [
            {
                "multiplicity": value,
                "tokens": multiplicity_profile[value],
            }
            for value in sorted(multiplicity_profile)
        ],
        "hashes": {
            "full_configurations": canonical_hash(sorted(full_rows)),
            "abstract_aspect_tokens": canonical_hash(
                sorted(
                    (token, multiplicity)
                    for token, multiplicity in abstract_multiplicity.items()
                )
            ),
        },
        "checks": {
            "full_configuration_injective": len(full_configurations)
            == len(full_rows),
            "abstract_first_use_collision_identity": occurrence_mass
            == abstract_union_mass + abstract_collision_mass,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
