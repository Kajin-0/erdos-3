#!/usr/bin/env python3
"""Extend raw simultaneous transition and multiplicity checks through S7."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from export_simultaneous_deletion_transition import (
    build_payload,
    payload_digest,
)


EXPECTED = {
    6: {
        "payload": "56d2074c478a5715a60ef77a8d21c59a12f981cbcd2c130758328e7d35bd020a",
        "selected": 3041,
        "residual": 238,
        "steps": 13,
        "occurrences": 94,
        "classes": 71,
        "duplicates": 15,
        "containments": 209,
        "partial": 150,
        "terminal_overlap": (1, 61, 303, 1597, 8195, 93476),
        "distribution": {
            1: 4781,
            2: 397,
            3: 54,
            5: 27,
            6: 27,
            10: 18,
            11: 6,
            13: 2,
        },
        "maximum": 13,
        "maximum_labels": (93476, 186952),
        "catalog": "58c007732844869a880b5763a800fce414ccf80e1f78b292311dc9360f4e4beb",
    },
    7: {
        "payload": "6f682a5a7be606c622cf4e660d7300f7f1ed76ed6d2835d1a111ef43a07b5678",
        "selected": 9360,
        "residual": 480,
        "steps": 25,
        "occurrences": 127,
        "classes": 95,
        "duplicates": 20,
        "containments": 345,
        "partial": 214,
        "terminal_overlap": (
            1,
            5,
            61,
            303,
            1597,
            8195,
            49158,
            93476,
            230164,
            323640,
        ),
        "distribution": {
            1: 14679,
            2: 1105,
            3: 184,
            5: 81,
            6: 81,
            10: 54,
            11: 17,
            12: 5,
            13: 3,
            16: 1,
        },
        "maximum": 16,
        "maximum_labels": (230164,),
        "catalog": "c66b8c38d6d44acce9071ac12c6e4069ace3897db8d1427e902651a8de8deae3",
    },
}

CERTIFICATE_SHA256 = (
    "4c1767a8c0b4e65b2deb4e576bfec6f8b74e6531f4ef12e4444fd53a9d0cb94c"
)


def multiplicity_metrics(payload: dict[str, object]) -> tuple[
    dict[int, int],
    int,
    tuple[int, ...],
    str,
    Fraction,
]:
    multiplicity: dict[int, int] = {}
    for occurrence in payload["recursive_shell_occurrences"]:
        for value in occurrence["values"]:
            multiplicity[value] = multiplicity.get(value, 0) + 1

    distribution = dict(
        sorted(Counter(multiplicity.values()).items())
    )
    maximum = max(multiplicity.values())
    maximum_labels = tuple(
        value
        for value in sorted(multiplicity)
        if multiplicity[value] == maximum
    )
    catalog = "\n".join(
        f"{value}:{multiplicity[value]}"
        for value in sorted(multiplicity)
    ) + "\n"
    catalog_hash = hashlib.sha256(catalog.encode("utf-8")).hexdigest()

    union_mass = sum(
        (Fraction(1, value) for value in multiplicity),
        Fraction(0),
    )
    occurrence_mass = sum(
        (
            Fraction(count, value)
            for value, count in multiplicity.items()
        ),
        Fraction(0),
    )
    return (
        distribution,
        maximum,
        maximum_labels,
        catalog_hash,
        occurrence_mass / union_mass,
    )


def build_certificate() -> str:
    lines = [
        "SIMULTANEOUS TRANSITION EXTENSION S6-S7",
        "",
        "policy=lexicographic_coordinated",
        "harmonic_average_bound=9/8",
        "exact_integer_string_limit=unbounded",
    ]

    for depth in (6, 7):
        payload = build_payload(depth)
        expected = EXPECTED[depth]
        interpretation = payload["interpretation"]
        schedule = payload["schedule"]

        basic = (
            payload_digest(payload),
            schedule["selected_count"],
            len(schedule["residual"]),
            len(payload["terminal_outputs"]["steps"]),
            interpretation["raw_simultaneous_recursive_occurrences"],
            interpretation["exact_state_classes"],
            interpretation["exact_duplicate_classes"],
            interpretation["strict_containment_relations"],
            interpretation["partial_overlap_relations"],
            tuple(payload["terminal_recursive_overlap"]),
        )
        required = (
            expected["payload"],
            expected["selected"],
            expected["residual"],
            expected["steps"],
            expected["occurrences"],
            expected["classes"],
            expected["duplicates"],
            expected["containments"],
            expected["partial"],
            expected["terminal_overlap"],
        )
        if basic != required:
            raise AssertionError(f"S{depth}: transition mismatch")

        (
            distribution,
            maximum,
            maximum_labels,
            catalog_hash,
            harmonic_average,
        ) = multiplicity_metrics(payload)
        if distribution != expected["distribution"]:
            raise AssertionError(f"S{depth}: distribution mismatch")
        if maximum != expected["maximum"]:
            raise AssertionError(f"S{depth}: maximum mismatch")
        if maximum_labels != expected["maximum_labels"]:
            raise AssertionError(f"S{depth}: maximum labels mismatch")
        if catalog_hash != expected["catalog"]:
            raise AssertionError(f"S{depth}: catalog hash mismatch")
        if not harmonic_average < Fraction(9, 8):
            raise AssertionError(
                f"S{depth}: harmonic-average bound failed"
            )

        lines.extend(
            [
                f"S{depth}_selected={expected['selected']}",
                f"S{depth}_residual={expected['residual']}",
                f"S{depth}_terminal_steps={expected['steps']}",
                (
                    f"S{depth}_recursive_occurrences="
                    f"{expected['occurrences']}"
                ),
                f"S{depth}_exact_state_classes={expected['classes']}",
                f"S{depth}_duplicate_classes={expected['duplicates']}",
                (
                    f"S{depth}_strict_containments="
                    f"{expected['containments']}"
                ),
                f"S{depth}_partial_overlaps={expected['partial']}",
                (
                    f"S{depth}_terminal_recursive_overlap="
                    + ",".join(
                        str(value)
                        for value in expected["terminal_overlap"]
                    )
                ),
                (
                    f"S{depth}_multiplicity_distribution="
                    + ",".join(
                        f"{multiplicity}:{count}"
                        for multiplicity, count
                        in distribution.items()
                    )
                ),
                f"S{depth}_maximum_multiplicity={maximum}",
                (
                    f"S{depth}_maximum_labels="
                    + ",".join(str(value) for value in maximum_labels)
                ),
                f"S{depth}_harmonic_average_bound_verified=true",
                (
                    f"S{depth}_multiplicity_catalog_sha256="
                    f"{catalog_hash}"
                ),
                f"S{depth}_payload_sha256={expected['payload']}",
            ]
        )

    lines.extend(
        [
            "",
            (
                "conclusion: the raw simultaneous frontier extends "
                "through S7."
            ),
            (
                "At S7, terminal-recursive overlap contains additional "
                "non-separation labels,"
            ),
            (
                "so a bounded-reuse state cannot track only the latest "
                "replication separation."
            ),
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(
            f"certificate SHA-256 mismatch: {digest}"
        )
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_simultaneous_transition_s6_s7.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
