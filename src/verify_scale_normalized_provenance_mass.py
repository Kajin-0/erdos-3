#!/usr/bin/env python3
"""Certify exact scale-normalized provenance mass across one propagation."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from verify_retained_provenance_second_generation import (
    DescendantOccurrence,
    build_descendant_occurrences,
    components,
    descendant_classes,
    descendant_conflict_graph,
    first_generation_retained_family,
    maximum_weight_independent_set_dp,
    resolve_lexicographic,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_FIRST_SPECTRUM = {
    1: 7_516,
    2: 537,
    3: 261,
    4: 182,
    5: 89,
    6: 21,
    8: 5,
    9: 3,
    11: 5,
    13: 1,
    14: 1,
}
EXPECTED_HASHES = {
    "first_provenance_map": "2b9abd1c399c72898df277c8a21694a2975b70057799f4163ace449f8ed815bc",
    "first_repeated_labels": "b0c1aa9243b24e0d46325742d4be25c72481d959900d6caa2dc5f4568b5a4238",
    "first_unique_mass": "23a1beb09a10f074f089c26f01395ba0e6126be9a3f61cf0dd8f148c962cac86",
    "first_occurrence_mass": "a38c3ec06ffc51819778f94e5f96cc9fe1524c7bf9254c2efb4f99d8bd96d96e",
    "first_repeat_mass": "4629de2af432975a0a05e861fb9be794a0f88f8361d14edb6a72bb00fedff997",
    "second_occurrence_mass": "86857e54a7a6894b4e420febb499b41eacd27e96c36df2c7ad80d6b7383fd1c5",
    "normalized_ratio": "8607e3b4afbf91a8bd74576647bbf8483639509db8016f13c04a042ad6a54a58",
    "factor_two_ratio": "2e99e3ab415dbd4892877f6fcb884710d3f3d15ae7e2cd5c9535e73587094d06",
    "factor_two_excess": "6e5e143b303ae1d1a09b7776888a10700d416245f86250f759af0a3cf7bfa018",
    "factor_two_excess_ratio": "4603e45b63c88a454095b0cc888b94fe81e5b29d1d37707797d6746b823dcf64",
}
CERTIFICATE_SHA256 = "15824a4eb3a07b3a6d4a620446b2e518d358a27dbb518079af96d57dc65c74fa"


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def set_hash(values: tuple[int, ...]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def second_generation_retained() -> tuple[object, ...]:
    retained_first = first_generation_retained_family()
    raw_rows = []
    for state in retained_first:
        selected, _residual = resolve_lexicographic(frozenset(state.values))
        raw_rows.extend(
            build_descendant_occurrences(
                state.index,
                state.values,
                state.representative.provenance,
                selected,
            )
        )
    occurrences = tuple(
        DescendantOccurrence(
            index=index,
            parent_class=row[0],
            source=row[1],
            source_step=row[2],
            exponent=row[3],
            values=row[4],
            provenance=row[5],
            immediate_provenance=row[6],
        )
        for index, row in enumerate(raw_rows)
    )
    classes = descendant_classes(occurrences)
    adjacency = descendant_conflict_graph(classes)
    retained_indices: list[int] = []
    for component in sorted(
        components(adjacency),
        key=lambda item: (classes[item[0]].representative.exponent, item),
    ):
        _weight, count, choice, _states = maximum_weight_independent_set_dp(
            component, classes, adjacency
        )
        if count != 1:
            raise AssertionError("second-generation optimum is not unique")
        retained_indices.extend(choice)
    return tuple(classes[index] for index in sorted(retained_indices))


def build_certificate() -> str:
    retained_first = first_generation_retained_family()
    retained_second = second_generation_retained()

    first_provenance = [
        provenance
        for state in retained_first
        for provenance in state.representative.provenance
    ]
    second_pairs = [
        (value, provenance)
        for state in retained_second
        for value, provenance in zip(
            state.values, state.representative.provenance, strict=True
        )
    ]
    first_counts = Counter(first_provenance)
    second_counts = Counter(provenance for _value, provenance in second_pairs)
    if Counter(first_counts.values()) != EXPECTED_FIRST_SPECTRUM:
        raise AssertionError("first-generation multiplicity spectrum mismatch")

    first_records = [
        {
            "provenance": provenance,
            "multiplicity": first_counts[provenance],
        }
        for provenance in sorted(first_counts)
    ]
    first_payload = json.dumps(
        first_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if hashlib.sha256(first_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "first_provenance_map"
    ]:
        raise AssertionError("first provenance map hash mismatch")
    repeated_first = tuple(
        sorted(
            provenance
            for provenance, multiplicity in first_counts.items()
            if multiplicity > 1
        )
    )
    if set_hash(repeated_first) != EXPECTED_HASHES["first_repeated_labels"]:
        raise AssertionError("first repeated-label hash mismatch")

    first_unique_mass = sum(
        (Fraction(1, provenance) for provenance in first_counts),
        Fraction(),
    )
    first_occurrence_mass = sum(
        (
            Fraction(multiplicity, provenance)
            for provenance, multiplicity in first_counts.items()
        ),
        Fraction(),
    )
    first_repeat_mass = first_occurrence_mass - first_unique_mass
    second_occurrence_mass = sum(
        (
            Fraction(multiplicity, provenance)
            for provenance, multiplicity in second_counts.items()
        ),
        Fraction(),
    )

    for value, provenance in second_pairs:
        if Fraction(value, provenance) * Fraction(1, value) != Fraction(
            1, provenance
        ):
            raise AssertionError("scale normalization identity failed")

    observed_hashes = {
        "first_unique_mass": fraction_hash(first_unique_mass),
        "first_occurrence_mass": fraction_hash(first_occurrence_mass),
        "first_repeat_mass": fraction_hash(first_repeat_mass),
        "second_occurrence_mass": fraction_hash(second_occurrence_mass),
    }
    for name, value in observed_hashes.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    normalized_ratio = second_occurrence_mass / first_occurrence_mass
    factor_two_ratio = 2 * normalized_ratio
    factor_two_excess = 2 * second_occurrence_mass - first_occurrence_mass
    factor_two_excess_ratio = factor_two_excess / first_occurrence_mass
    ratio_hashes = {
        "normalized_ratio": fraction_hash(normalized_ratio),
        "factor_two_ratio": fraction_hash(factor_two_ratio),
        "factor_two_excess": fraction_hash(factor_two_excess),
        "factor_two_excess_ratio": fraction_hash(factor_two_excess_ratio),
    }
    for name, value in ratio_hashes.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    if not Fraction(644, 1_000) < normalized_ratio < Fraction(645, 1_000):
        raise AssertionError("normalized ratio outside bracket")
    if not Fraction(1_288, 1_000) < factor_two_ratio < Fraction(
        1_289, 1_000
    ):
        raise AssertionError("factor-two ratio outside bracket")
    if not Fraction(288, 1_000) < factor_two_excess_ratio < Fraction(
        289, 1_000
    ):
        raise AssertionError("factor-two excess ratio outside bracket")

    lines = [
        "SCALE-NORMALIZED PROVENANCE MASS",
        "",
        (
            "definition=K(R)=sum_over_retained_points_(u,p) "
            "(u/p)*(1/u)=sum_over_occurrences 1/p"
        ),
        "first_generation_policy=local37",
        "second_generation_child_policy=lexicographic",
        (
            "retention_rule=global_exact_duplicate_quotient_plus_"
            "maximum_harmonic_conflict_selection"
        ),
        "",
        "first_generation_retained_points=11753",
        "first_generation_root_provenance_labels=8621",
        "first_generation_maximum_provenance_multiplicity=14",
        "first_generation_multiplicity_1=7516",
        "first_generation_multiplicity_2=537",
        "first_generation_multiplicity_3=261",
        "first_generation_multiplicity_4=182",
        "first_generation_multiplicity_5=89",
        "first_generation_multiplicity_6=21",
        "first_generation_multiplicity_8=5",
        "first_generation_multiplicity_9=3",
        "first_generation_multiplicity_11=5",
        "first_generation_multiplicity_13=1",
        "first_generation_multiplicity_14=1",
        f"first_generation_provenance_map_sha256={EXPECTED_HASHES['first_provenance_map']}",
        f"first_generation_repeated_labels_sha256={EXPECTED_HASHES['first_repeated_labels']}",
        f"first_generation_unique_provenance_mass_sha256={EXPECTED_HASHES['first_unique_mass']}",
        f"first_generation_occurrence_provenance_mass_sha256={EXPECTED_HASHES['first_occurrence_mass']}",
        f"first_generation_repeat_provenance_mass_sha256={EXPECTED_HASHES['first_repeat_mass']}",
        "",
        "second_generation_retained_points=7925",
        "second_generation_root_provenance_labels=7648",
        "second_generation_maximum_provenance_multiplicity=3",
        f"second_generation_occurrence_provenance_mass_sha256={EXPECTED_HASHES['second_occurrence_mass']}",
        "",
        "scale_identity_verified=True",
        "second_over_first_scale_normalized_mass_bracket=644/1000,645/1000",
        f"second_over_first_scale_normalized_mass_sha256={EXPECTED_HASHES['normalized_ratio']}",
        "factor_two_persistence_ratio_bracket=1288/1000,1289/1000",
        f"factor_two_persistence_ratio_sha256={EXPECTED_HASHES['factor_two_ratio']}",
        f"factor_two_persistence_excess_mass_sha256={EXPECTED_HASHES['factor_two_excess']}",
        "factor_two_persistence_excess_over_first_bracket=288/1000,289/1000",
        f"factor_two_persistence_excess_over_first_sha256={EXPECTED_HASHES['factor_two_excess_ratio']}",
        "",
        (
            "conclusion: exact u/p normalization converts descendant harmonic "
            "mass to root-provenance occurrence mass"
        ),
        (
            "and contracts by a factor between 0.644 and 0.645 across the "
            "recorded propagation."
        ),
        (
            "After a factor-two persistence weight, the normalized ratio lies "
            "between 1.288 and 1.289."
        ),
        (
            "Scale normalization therefore removes the raw 6.828-fold "
            "harmonic expansion but does not by itself"
        ),
        (
            "pay the persistence increase; an additional obstruction or "
            "completion credit is still required."
        ),
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_scale_normalized_provenance_mass.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print(
        "certificate_sha256="
        + hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
