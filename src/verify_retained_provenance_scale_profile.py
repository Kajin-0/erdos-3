#!/usr/bin/env python3
"""Certify scale contraction and repeated-provenance concentration exactly."""
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

EXPECTED_RETAINED_POINTS = 7_925
EXPECTED_RETAINED_FAMILY_SHA256 = (
    "dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596"
)
EXPECTED_RATIO_RECORD_BYTES = 1_287_870
EXPECTED_RATIO_RECORD_SHA256 = (
    "904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3"
)
EXPECTED_HISTOGRAM_SHA256 = {
    "shell_drop": "4d7edd939fd9e06aa12a685c01d0a604036ecaa85032ad51b78b860bc01c1f56",
    "floor_log": "95bfd05af985ecdd6ea67222ce8ebb1a95929cbfcc41d6885f8c4eb32f1f9639",
    "ceil_log": "f2803e264d336efaf0ea5541b6a68edb97553c7e202b641876a72c63df6b2b4c",
}
EXPECTED_MIN_RATIO = Fraction(505_417, 112_004)
EXPECTED_MIN_RECORD_SHA256 = (
    "8dec55d97ff8205fff1ac3946486e84dcc1e7e163ffab9291654d5e1be06f948"
)
EXPECTED_MAX_RATIO = Fraction(1_354_066)
EXPECTED_MAX_RECORD_SHA256 = (
    "5b9e2566b5ce69bd185dabf30ac91c70df8f7b202ded4853631ed503cc47d7c5"
)
EXPECTED_COUNTS = {
    "root_provenance_repeated_labels": 272,
    "repeated_provenance_occurrences": 549,
    "unique_provenance_occurrences": 7_376,
    "floor_log_at_least_8_points": 196,
    "floor_log_at_least_16_points": 4,
}
EXPECTED_MASS_SHA256 = {
    "first_generation_retained": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
    "second_generation_retained": "05febea047257947cc84dcd14b126c6a904013a3a7b1edf13a84e7ff8dd1ab1f",
    "root_provenance_occurrence": "86857e54a7a6894b4e420febb499b41eacd27e96c36df2c7ad80d6b7383fd1c5",
    "intergeneration_debt": "f91ef6347dbcfbbfaa1516df5b6d68536ee5ea911286cdbf8fa12fde001fe1a2",
    "shell_depth_charge": "edf1c7251293bb339125b444b1588284bab7b071181227802bb25fde63bfd1dc",
    "floor_log_charge": "7f6e4cbbd98a866dc97d45586c1d6cdb8db7be5b83d3caf17999ac1ce98d00b5",
    "ceil_log_charge": "27e320117e1b96e139a0d512a9ba02e2862d43fc0cf566d2d4dcc90f63efed64",
    "repeated_root": "469d700a86d08d6e66941c948b2c90e86a3b8416c6cc163aa01809aa8bde6daa",
    "repeated_descendant": "efaf397a17a94b0d1c10818f13a5c247018533de5c49047ed78b7f21dd4e5116",
    "unique_root": "bbf65cb92921dd48ec594e89dd7d78c502253b091ef9f1df08f9a6919f50b69e",
    "unique_descendant": "0e35b95d31a2b98ca374627458474dc692863748b60728a483d17b73dcb8f911",
}
EXPECTED_RATIOS = {
    "second_retained_over_root_occurrence": (
        Fraction(399), Fraction(400),
        "23660d568c5e330387a3ed1a2824e2a28d32dfe8bd00817330d063b7786682dd",
    ),
    "debt_over_shell_depth_charge": (
        Fraction(86), Fraction(87),
        "e231de949c20a23ab840afb904c92010a2c48d3457ce9aef5296cf39a46a1629",
    ),
    "debt_over_floor_log_charge": (
        Fraction(99), Fraction(100),
        "02b799f46b84409a1f43e4d930e22904976ca3d29da767e7b18c5500588c19d1",
    ),
    "debt_over_ceil_log_charge": (
        Fraction(77), Fraction(78),
        "4e6048b6552685bd7afd370ef372ce322c15b05bc776864e57b91c69cc0ddfd3",
    ),
    "repeated_root_mass_share": (
        Fraction(76, 1_000), Fraction(77, 1_000),
        "4b942d0a9ba133c2a6796bd0cd73d815182b14eb4c15ad478de7f3812555b95d",
    ),
    "repeated_descendant_mass_share": (
        Fraction(948, 1_000), Fraction(949, 1_000),
        "2850e28861722ac0071d2eed1296f5617b7f8122540e5c97f0e5c9a5366ef11a",
    ),
    "repeated_provenance_expansion": (
        Fraction(4_928), Fraction(4_929),
        "1fcd50b042757014887936414f9440a515790d1b7eb31740ec3a0d3ebb1dadfc",
    ),
    "unique_provenance_expansion": (
        Fraction(22), Fraction(23),
        "fbafd2813c3fe71926c38eff05a6f6ab45d02ee6838f50a73c29e0749ea976a7",
    ),
    "floor_log_at_least_8_descendant_mass_share": (
        Fraction(943, 1_000), Fraction(944, 1_000),
        "4c3f35ca0ade9c74a603a237b3ba49437e7cbed59419b5cf4540baa32aa58df6",
    ),
    "floor_log_at_least_16_descendant_mass_share": (
        Fraction(698, 1_000), Fraction(699, 1_000),
        "0f332788f980c8d06ffc2fd323daa7644bbd0b92f212166281905b809fa2b145",
    ),
    "floor_log_20_descendant_mass_share": (
        Fraction(512, 1_000), Fraction(513, 1_000),
        "8476e2b1be43f63225a78a30befc332f2861199cf73f46bb20a6531d754a2b8c",
    ),
}
CERTIFICATE_SHA256 = (
    "a38089295cec338b9155ea15bccff0a70dd55f1fea46c4a8deb2e13f390fd012"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def display_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return fraction_text(value)


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def record_hash(record: dict[str, object]) -> str:
    payload = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def histogram_hash(rows: list[dict[str, object]], key: str) -> str:
    histogram = Counter(int(row[key]) for row in rows)
    payload = "".join(
        f"{value}:{histogram[value]}\n"
        for value in sorted(histogram)
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def floor_log_ratio(root: int, descendant: int) -> int:
    return (root // descendant).bit_length() - 1


def ceil_log_ratio(root: int, descendant: int) -> int:
    floor = floor_log_ratio(root, descendant)
    if root == descendant * (1 << floor):
        return floor
    return floor + 1


def reconstruct_retained_families() -> tuple[tuple[object, ...], tuple[object, ...]]:
    retained_first = first_generation_retained_family()
    raw_rows: list[tuple[object, ...]] = []
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
        DescendantOccurrence(index, *row)
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
            raise AssertionError("second-generation retained optimum is not unique")
        retained_indices.extend(choice)
    retained_second = tuple(classes[index] for index in sorted(retained_indices))

    records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "parent_class": state.representative.parent_class,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
            "immediate_provenance": list(
                state.representative.immediate_provenance
            ),
        }
        for state in retained_second
    ]
    payload = json.dumps(records, sort_keys=True, separators=(",", ":")) + "\n"
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if digest != EXPECTED_RETAINED_FAMILY_SHA256:
        raise AssertionError(f"second-generation retained-family mismatch: {digest}")
    return retained_first, retained_second


def build_ratio_rows(retained_second: tuple[object, ...]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for state in retained_second:
        representative = state.representative
        for descendant, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            rows.append(
                {
                    "class": state.index,
                    "u": descendant,
                    "p": root,
                    "immediate": immediate,
                    "parent": representative.parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "exponent": representative.exponent,
                    "shell_drop": (
                        root.bit_length() - descendant.bit_length()
                    ),
                    "floor_log": floor_log_ratio(root, descendant),
                    "ceil_log": ceil_log_ratio(root, descendant),
                }
            )
    if len(rows) != EXPECTED_RETAINED_POINTS:
        raise AssertionError(f"retained-point mismatch: {len(rows)}")
    return rows


def assert_ratio(name: str, value: Fraction) -> None:
    lower, upper, expected_hash = EXPECTED_RATIOS[name]
    if not lower < value < upper:
        raise AssertionError(f"{name} outside compact bracket: {value}")
    digest = fraction_hash(value)
    if digest != expected_hash:
        raise AssertionError(f"{name} hash mismatch: {digest}")


def build_certificate() -> str:
    retained_first, retained_second = reconstruct_retained_families()
    rows = build_ratio_rows(retained_second)

    ratio_payload = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    ratio_bytes = len(ratio_payload.encode("utf-8"))
    ratio_hash = hashlib.sha256(ratio_payload.encode("utf-8")).hexdigest()
    if (
        ratio_bytes != EXPECTED_RATIO_RECORD_BYTES
        or ratio_hash != EXPECTED_RATIO_RECORD_SHA256
    ):
        raise AssertionError("ratio-record payload mismatch")

    observed_histograms = {
        key: histogram_hash(rows, key)
        for key in EXPECTED_HISTOGRAM_SHA256
    }
    if observed_histograms != EXPECTED_HISTOGRAM_SHA256:
        raise AssertionError("scale histogram mismatch")

    minimum_record = min(rows, key=lambda row: Fraction(row["p"], row["u"]))
    maximum_record = max(rows, key=lambda row: Fraction(row["p"], row["u"]))
    minimum_ratio = Fraction(minimum_record["p"], minimum_record["u"])
    maximum_ratio = Fraction(maximum_record["p"], maximum_record["u"])
    if minimum_ratio != EXPECTED_MIN_RATIO:
        raise AssertionError("minimum root/descendant ratio mismatch")
    if maximum_ratio != EXPECTED_MAX_RATIO:
        raise AssertionError("maximum root/descendant ratio mismatch")
    if record_hash(minimum_record) != EXPECTED_MIN_RECORD_SHA256:
        raise AssertionError("minimum ratio record mismatch")
    if record_hash(maximum_record) != EXPECTED_MAX_RECORD_SHA256:
        raise AssertionError("maximum ratio record mismatch")

    provenance_counts = Counter(int(row["p"]) for row in rows)
    repeated_roots = {
        root for root, multiplicity in provenance_counts.items()
        if multiplicity > 1
    }
    repeated_rows = [row for row in rows if row["p"] in repeated_roots]
    unique_rows = [row for row in rows if row["p"] not in repeated_roots]
    observed_counts = {
        "root_provenance_repeated_labels": len(repeated_roots),
        "repeated_provenance_occurrences": len(repeated_rows),
        "unique_provenance_occurrences": len(unique_rows),
        "floor_log_at_least_8_points": sum(
            int(row["floor_log"]) >= 8 for row in rows
        ),
        "floor_log_at_least_16_points": sum(
            int(row["floor_log"]) >= 16 for row in rows
        ),
    }
    if observed_counts != EXPECTED_COUNTS:
        raise AssertionError(f"count mismatch: {observed_counts!r}")
    if any(
        row["p"] not in repeated_roots
        for row in rows
        if int(row["floor_log"]) >= 8
    ):
        raise AssertionError("large scale contraction without repeated provenance")

    first_mass = sum((state.weight for state in retained_first), Fraction())
    second_mass = sum((state.weight for state in retained_second), Fraction())
    root_occurrence_mass = sum(
        (Fraction(1, int(row["p"])) for row in rows), Fraction()
    )
    debt = second_mass - first_mass
    shell_charge = sum(
        (
            Fraction(int(row["shell_drop"]), int(row["p"]))
            for row in rows
        ),
        Fraction(),
    )
    floor_charge = sum(
        (
            Fraction(int(row["floor_log"]), int(row["p"]))
            for row in rows
        ),
        Fraction(),
    )
    ceil_charge = sum(
        (
            Fraction(int(row["ceil_log"]), int(row["p"]))
            for row in rows
        ),
        Fraction(),
    )
    repeated_root_mass = sum(
        (Fraction(1, int(row["p"])) for row in repeated_rows), Fraction()
    )
    repeated_descendant_mass = sum(
        (Fraction(1, int(row["u"])) for row in repeated_rows), Fraction()
    )
    unique_root_mass = root_occurrence_mass - repeated_root_mass
    unique_descendant_mass = second_mass - repeated_descendant_mass

    observed_mass_hashes = {
        "first_generation_retained": fraction_hash(first_mass),
        "second_generation_retained": fraction_hash(second_mass),
        "root_provenance_occurrence": fraction_hash(root_occurrence_mass),
        "intergeneration_debt": fraction_hash(debt),
        "shell_depth_charge": fraction_hash(shell_charge),
        "floor_log_charge": fraction_hash(floor_charge),
        "ceil_log_charge": fraction_hash(ceil_charge),
        "repeated_root": fraction_hash(repeated_root_mass),
        "repeated_descendant": fraction_hash(repeated_descendant_mass),
        "unique_root": fraction_hash(unique_root_mass),
        "unique_descendant": fraction_hash(unique_descendant_mass),
    }
    if observed_mass_hashes != EXPECTED_MASS_SHA256:
        raise AssertionError("mass hash mismatch")

    floor_tail_8_mass = sum(
        (
            Fraction(1, int(row["u"]))
            for row in rows
            if int(row["floor_log"]) >= 8
        ),
        Fraction(),
    )
    floor_tail_16_mass = sum(
        (
            Fraction(1, int(row["u"]))
            for row in rows
            if int(row["floor_log"]) >= 16
        ),
        Fraction(),
    )
    floor_20_mass = sum(
        (
            Fraction(1, int(row["u"]))
            for row in rows
            if int(row["floor_log"]) == 20
        ),
        Fraction(),
    )

    ratios = {
        "second_retained_over_root_occurrence": second_mass / root_occurrence_mass,
        "debt_over_shell_depth_charge": debt / shell_charge,
        "debt_over_floor_log_charge": debt / floor_charge,
        "debt_over_ceil_log_charge": debt / ceil_charge,
        "repeated_root_mass_share": repeated_root_mass / root_occurrence_mass,
        "repeated_descendant_mass_share": repeated_descendant_mass / second_mass,
        "repeated_provenance_expansion": (
            repeated_descendant_mass / repeated_root_mass
        ),
        "unique_provenance_expansion": unique_descendant_mass / unique_root_mass,
        "floor_log_at_least_8_descendant_mass_share": (
            floor_tail_8_mass / second_mass
        ),
        "floor_log_at_least_16_descendant_mass_share": (
            floor_tail_16_mass / second_mass
        ),
        "floor_log_20_descendant_mass_share": floor_20_mass / second_mass,
    }
    for name, value in ratios.items():
        assert_ratio(name, value)

    lines = [
        "SECOND-GENERATION PROVENANCE SCALE PROFILE",
        "",
        "first_generation_policy=local37",
        (
            "first_generation_retention=exact_duplicate_quotient_plus_"
            "maximum_harmonic_conflict_selection"
        ),
        "child_transition_policy=lexicographic_coordinated_deletion",
        "second_generation_retention=same_global_exact_duplicate_and_conflict_rule",
        "",
        "retained_points=7925",
        f"ratio_record_bytes={ratio_bytes}",
        f"ratio_record_sha256={ratio_hash}",
        f"shell_drop_histogram_sha256={observed_histograms['shell_drop']}",
        f"floor_log_histogram_sha256={observed_histograms['floor_log']}",
        f"ceil_log_histogram_sha256={observed_histograms['ceil_log']}",
        "",
        f"minimum_root_over_descendant_ratio={display_fraction(minimum_ratio)}",
        f"minimum_ratio_record_sha256={EXPECTED_MIN_RECORD_SHA256}",
        f"maximum_root_over_descendant_ratio={display_fraction(maximum_ratio)}",
        f"maximum_ratio_record_sha256={EXPECTED_MAX_RECORD_SHA256}",
        "",
        "root_provenance_repeated_labels=272",
        "repeated_provenance_occurrences=549",
        "unique_provenance_occurrences=7376",
        "all_floor_log_at_least_8_repeated=True",
        "floor_log_at_least_8_points=196",
        "floor_log_at_least_16_points=4",
        "",
        f"first_generation_retained_mass_sha256={observed_mass_hashes['first_generation_retained']}",
        f"second_generation_retained_mass_sha256={observed_mass_hashes['second_generation_retained']}",
        f"root_provenance_occurrence_mass_sha256={observed_mass_hashes['root_provenance_occurrence']}",
        f"intergeneration_debt_mass_sha256={observed_mass_hashes['intergeneration_debt']}",
        f"shell_depth_charge_sha256={observed_mass_hashes['shell_depth_charge']}",
        f"floor_log_charge_sha256={observed_mass_hashes['floor_log_charge']}",
        f"ceil_log_charge_sha256={observed_mass_hashes['ceil_log_charge']}",
        "",
        "second_retained_over_root_occurrence_mass_bracket=399,400",
        f"second_retained_over_root_occurrence_mass_sha256={EXPECTED_RATIOS['second_retained_over_root_occurrence'][2]}",
        "debt_over_shell_depth_charge_bracket=86,87",
        f"debt_over_shell_depth_charge_sha256={EXPECTED_RATIOS['debt_over_shell_depth_charge'][2]}",
        "debt_over_floor_log_charge_bracket=99,100",
        f"debt_over_floor_log_charge_sha256={EXPECTED_RATIOS['debt_over_floor_log_charge'][2]}",
        "debt_over_ceil_log_charge_bracket=77,78",
        f"debt_over_ceil_log_charge_sha256={EXPECTED_RATIOS['debt_over_ceil_log_charge'][2]}",
        "",
        "repeated_root_mass_share_bracket=76/1000,77/1000",
        f"repeated_root_mass_share_sha256={EXPECTED_RATIOS['repeated_root_mass_share'][2]}",
        "repeated_descendant_mass_share_bracket=948/1000,949/1000",
        f"repeated_descendant_mass_share_sha256={EXPECTED_RATIOS['repeated_descendant_mass_share'][2]}",
        "repeated_provenance_expansion_bracket=4928,4929",
        f"repeated_provenance_expansion_sha256={EXPECTED_RATIOS['repeated_provenance_expansion'][2]}",
        "unique_provenance_expansion_bracket=22,23",
        f"unique_provenance_expansion_sha256={EXPECTED_RATIOS['unique_provenance_expansion'][2]}",
        "",
        "floor_log_at_least_8_descendant_mass_share_bracket=943/1000,944/1000",
        f"floor_log_at_least_8_descendant_mass_share_sha256={EXPECTED_RATIOS['floor_log_at_least_8_descendant_mass_share'][2]}",
        "floor_log_at_least_16_descendant_mass_share_bracket=698/1000,699/1000",
        f"floor_log_at_least_16_descendant_mass_share_sha256={EXPECTED_RATIOS['floor_log_at_least_16_descendant_mass_share'][2]}",
        "floor_log_20_descendant_mass_share_bracket=512/1000,513/1000",
        f"floor_log_20_descendant_mass_share_sha256={EXPECTED_RATIOS['floor_log_20_descendant_mass_share'][2]}",
        "",
        (
            "conclusion: repeated root provenance is strongly concentrated at "
            "the largest scale contractions."
        ),
        (
            "Every retained point with floor_log2(root/descendant) at least 8 "
            "has repeated root provenance."
        ),
        (
            "Repeated provenance contributes between 94.8% and 94.9% of "
            "descendant harmonic mass while carrying only 7.6% to 7.7% of "
            "occurrence-weighted root mass."
        ),
        (
            "Unit dyadic-depth and logarithmic charges cannot repay the "
            "intergeneration debt; even the optimistic ceil-log charge requires "
            "coefficient greater than 77."
        ),
        (
            "The next Bellman coordinate must couple repeated provenance with "
            "scale contraction rather than treat multiplicity or depth independently."
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
            "usage: verify_retained_provenance_scale_profile.py [OUTPUT]"
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
