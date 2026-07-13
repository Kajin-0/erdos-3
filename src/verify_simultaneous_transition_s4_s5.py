#!/usr/bin/env python3
"""Extend raw simultaneous transition and multiplicity checks through S5."""

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
    4: {
        "payload": "023330cc1babb1f10d8956f5b966a98f38d0b6f6dc062bdf1ee00c7b47976c03",
        "selected": 305,
        "residual": 58,
        "steps": 11,
        "occurrences": 46,
        "classes": 34,
        "duplicates": 7,
        "containments": 91,
        "partial": 35,
        "terminal_overlap": (1, 61, 303, 1597),
        "distribution": {1: 460, 2: 60, 3: 7, 5: 3, 6: 3, 11: 2},
        "maximum": 11,
        "maximum_labels": (1597, 3194),
        "catalog": "dd0029d181a8195b03fe7db7c69f4ce7c19c85f3af3a3589103e3a1091e2c0a1",
    },
    5: {
        "payload": "028cc066383a969cbec7b9ec285aec208c99e6c7f8fa233555067eb241e0f03b",
        "selected": 974,
        "residual": 118,
        "steps": 12,
        "occurrences": 68,
        "classes": 51,
        "duplicates": 11,
        "containments": 145,
        "partial": 88,
        "terminal_overlap": (1, 61, 303, 1597, 8195),
        "distribution": {
            1: 1482,
            2: 167,
            3: 18,
            5: 9,
            6: 9,
            10: 6,
            12: 2,
        },
        "maximum": 12,
        "maximum_labels": (8195, 16390),
        "catalog": "0cba557321d68c27d86221b45943150941b1c8108b650c916d7a773ca8ed754b",
    },
}

CERTIFICATE_SHA256 = (
    "ada237c35a0980c15cecac51e30fd43ade50948067d6f421477af1bb79239756"
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
        "SIMULTANEOUS TRANSITION EXTENSION S4-S5",
        "",
        "policy=lexicographic_coordinated",
        "harmonic_average_bound=9/8",
    ]

    for depth in (4, 5):
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
                (
                    f"S{depth}_harmonic_average_bound_verified=true"
                ),
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
                "conclusion: the raw simultaneous transition and "
                "multiplicity ledgers extend"
            ),
            (
                "through S5. Maximum multiplicity rises to 12 while "
                "harmonic-average"
            ),
            (
                "multiplicity remains below 9/8; bounded-reuse must be "
                "provenance-sensitive."
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
            "usage: verify_simultaneous_transition_s4_s5.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
