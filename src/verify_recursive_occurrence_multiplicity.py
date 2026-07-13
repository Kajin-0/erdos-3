#!/usr/bin/env python3
"""Verify exact recursive-label occurrence multiplicities on S1 through S3.

For raw simultaneous recursive occurrences C_i, let m(u) be the number of
occurrences containing label u. Then

    sum_i H(C_i) = sum_u m(u)/u

and, with M=max_u m(u),

    sum_i H(C_i) <= M H(union_i C_i).

The verifier records both the maximum and the harmonic-average multiplicity.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from export_simultaneous_deletion_transition import build_payload


EXPECTED = {
    1: {
        "distribution": {1: 7, 2: 4},
        "maximum": 2,
        "max_labels": (1, 16, 21, 26),
        "catalog_sha256": (
            "9680d1e76ac3035fb6ba26e432f466dab2de675c6b1a24f89586a86cfeecd6cc"
        ),
        "excess": Fraction(5017, 4368),
        "ratio_bound": Fraction(8, 5),
    },
    2: {
        "distribution": {1: 36, 2: 7, 3: 3},
        "maximum": 3,
        "max_labels": (61, 87, 122),
        "catalog_sha256": (
            "99210bbd67a374077349d053a7a0ed74e8e56ee2b73628a518cd23d9a86518ab"
        ),
        "excess": Fraction(1_720_946_837_057, 11_385_890_360_130),
        "ratio_bound": Fraction(11, 10),
    },
    3: {
        "distribution": {1: 162, 2: 10, 3: 2, 6: 1, 7: 1},
        "maximum": 7,
        "max_labels": (303,),
        "catalog_sha256": (
            "ac489a948644e027caf2862db4b1429f50e11e7fbc763c74d697a26e84b4faf0"
        ),
        "excess": Fraction(
            767_969_830_085_807,
            5_412_538_546_014_600,
        ),
        "ratio_bound": Fraction(11, 10),
    },
}

CERTIFICATE_SHA256 = (
    "9774ea7c8cbd3626b3120ade6b48344008b5f1706b05e253923393cc8495e7e8"
)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def metrics(depth: int) -> tuple[
    dict[int, int],
    int,
    tuple[int, ...],
    str,
    Fraction,
    Fraction,
]:
    payload = build_payload(depth)
    multiplicity: dict[int, int] = {}
    for occurrence in payload["recursive_shell_occurrences"]:
        for value in occurrence["values"]:
            multiplicity[value] = multiplicity.get(value, 0) + 1

    distribution = dict(
        sorted(Counter(multiplicity.values()).items())
    )
    maximum = max(multiplicity.values())
    max_labels = tuple(
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
        max_labels,
        catalog_hash,
        union_mass,
        occurrence_mass,
    )


def build_certificate() -> str:
    lines = [
        "RECURSIVE OCCURRENCE MULTIPLICITY",
        "",
        "identity=sum_i H(C_i)=sum_u m(u)/u",
        "bound=sum_i H(C_i)<=M*H(union_i C_i)",
        "verified_depths=1,2,3",
    ]

    for depth in (1, 2, 3):
        (
            distribution,
            maximum,
            max_labels,
            catalog_hash,
            union_mass,
            occurrence_mass,
        ) = metrics(depth)
        expected = EXPECTED[depth]

        if distribution != expected["distribution"]:
            raise AssertionError(f"S{depth}: distribution mismatch")
        if maximum != expected["maximum"]:
            raise AssertionError(f"S{depth}: maximum mismatch")
        if max_labels != expected["max_labels"]:
            raise AssertionError(f"S{depth}: maximum labels mismatch")
        if catalog_hash != expected["catalog_sha256"]:
            raise AssertionError(f"S{depth}: catalog hash mismatch")

        excess = occurrence_mass - union_mass
        if excess != expected["excess"]:
            raise AssertionError(f"S{depth}: duplicate excess mismatch")

        ratio = occurrence_mass / union_mass
        if not ratio < expected["ratio_bound"]:
            raise AssertionError(
                f"S{depth}: harmonic-average bound failed"
            )
        if not occurrence_mass <= maximum * union_mass:
            raise AssertionError(
                f"S{depth}: maximum multiplicity bound failed"
            )

        distribution_text = ",".join(
            f"{multiplicity}:{count}"
            for multiplicity, count in distribution.items()
        )
        lines.extend(
            [
                (
                    f"S{depth}_multiplicity_distribution="
                    f"{distribution_text}"
                ),
                f"S{depth}_maximum_multiplicity={maximum}",
                (
                    f"S{depth}_maximum_labels="
                    + ",".join(str(value) for value in max_labels)
                ),
                (
                    f"S{depth}_duplicate_excess="
                    f"{fraction_text(excess)}"
                ),
                (
                    f"S{depth}_harmonic_average_multiplicity="
                    f"{fraction_text(ratio)}"
                ),
                (
                    f"S{depth}_harmonic_average_bound="
                    f"{fraction_text(expected['ratio_bound'])}"
                ),
                f"S{depth}_catalog_sha256={catalog_hash}",
            ]
        )

    lines.extend(
        [
            "",
            (
                "conclusion: pointwise multiplicity gives an exact local "
                "packing bound,"
            ),
            (
                "but the maximum multiplicity grows from 2 to 7 by S3 "
                "while the harmonic"
            ),
            (
                "average remains below the recorded small constants. A "
                "whole-tree theorem"
            ),
            (
                "must track provenance reuse rather than rely only on local "
                "maximum multiplicity."
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
            "usage: verify_recursive_occurrence_multiplicity.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
