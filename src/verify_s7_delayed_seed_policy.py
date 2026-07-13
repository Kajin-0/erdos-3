#!/usr/bin/env python3
"""Verify the exact tradeoff from delaying three unforced S7 q=1 actions."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import heapq
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import (
    all_three_aps,
    canonical_regenerations,
    canonical_set_hash,
    middle_fibers,
    middle_shells,
    schedule_hash,
    v2,
)
from verify_s7_policy_transition_tradeoff import (
    edge_hash,
    fraction_hash,
    harmonic,
    policy_metrics,
    set_hash,
    strongly_connected_components,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

DELAYED_CENTERS = frozenset({1_354_065, 1_354_070, 1_354_075})
EXPECTED = {
    "selected": 9_358,
    "residual": 482,
    "terminal_steps": 31,
    "middle_shells": 123,
    "fiber_occurrences": 9_327,
    "fiber_union": 7_511,
    "imported_union": 326,
    "novel_union": 7_185,
    "incidence_edges": 69,
    "scc_count": 25,
    "cyclic_scc_count": 1,
    "largest_scc": 7,
    "maximum_multiplicity": 14,
    "q1_centers": 2_913,
    "q1_minimum": 1_354_049,
    "schedule_sha256": (
        "dc4de4415754f43b6b23746a1285487baebf3fd105b364bd4d3c6f0daeb325b7"
    ),
    "residual_sha256": (
        "152a6154aef54029a70b7defe58389391514442155b4dc55b0a246e39b55b912"
    ),
    "q1_centers_sha256": (
        "7c650f8b794a24d71b78e912059f2bb0bcd618a2635b56bb72389aaed242146a"
    ),
    "q1_fiber_sha256": (
        "0e36c95ff3d51a3bb1481b90f6928811ebcbe2d458c9de5af2d3b0144d4d4be9"
    ),
    "edge_sha256": (
        "84223ba922ba2efdefd4c4862d49d78de60aa41e0ce22523ddf5cfff0c0c186c"
    ),
    "largest_scc_sha256": (
        "cb78b3ba8da7507643570284d8b1278aa65833a7343bf209c99626ee1a894786"
    ),
    "terminal_mass_sha256": (
        "05fe692fe9a3a96fa2a5fb53c0e2df0c8fdec93951e7c70c142dad9c5166a672"
    ),
    "occurrence_mass_sha256": (
        "61a2dd2e0e26321a03a0c35276c97aeec563eeb6485e3fe192406160199304b9"
    ),
    "union_mass_sha256": (
        "b4ef186149d69ffb14c22a2f95a377d3c0a9d92c72f8f9de126d5c86ada32ce5"
    ),
    "duplicate_mass_sha256": (
        "17bda8abf2988c82e198772526024ea7b066f78b32aed49bcea807ea65f06e51"
    ),
    "average_multiplicity_sha256": (
        "e9dd59c762bdf8587480f21798b8c1838c5133861c60341632bdad23291fc607"
    ),
}
EXPECTED_RATIO_SHA256 = {
    "terminal": "52da921bff0fa9bdb02995d7e08d46a279cc6e7da3e058be356365511c21abd9",
    "occurrence": "5bf6641082915ef94a35a5f5cce0b24a8655a268fa09eb77ba911caef47330ef",
    "union": "a5eca5182b397caa3fd4980b87c32ca6dc560d3e97f58923e5497d5d491e48cf",
    "duplicate": "97db80eb73f959ad7586fe89a8e15f8ed1a984e095ceae8435e8d6664bbffd45",
    "average": "bbad7ebb6efea50e5496ad06aa748eca4e4de299c5fd901d6b333b0c6ee8118a",
}
EXPECTED_DIFFERENCE_SHA256 = {
    "terminal_increase": "73690f788b4d1abf1a732d94739995697bd351334e0905a73fee212dd7b6940a",
    "occurrence_reduction": "0ec585dfc2ed72867755258a9f662950653eb1ab9ec5987acbbf8cd1bb7ec114",
    "union_reduction": "eeb05bb9d768fe56d2d26456cb2ed7f25cc2b6d8f1828fda801e077bdc9bef2a",
    "duplicate_reduction": "3a4eea2c641b19a8241761bcabe0e8d5e6074ba37429e1ec5a71176290c46402",
    "average_reduction": "25bdb0157612588f16131bf3bad3557ea5dee747ac02cb951f2f55fc59554b82",
}
CERTIFICATE_SHA256 = (
    "37ed54c207820478fb5b2b2843342b2aebd9b274b4dd5ef1e6cf79e3d627f4e9"
)


def resolve_delayed() -> tuple[tuple[tuple[int, ...], ...], frozenset[int]]:
    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    current = set(parent)
    queue = [
        (
            (
                step == 1 and middle in DELAYED_CENTERS,
                (step, left, middle, right),
            ),
            (step, left, middle, right),
        )
        for step, left, middle, right in progressions
    ]
    heapq.heapify(queue)
    selected: list[tuple[int, ...]] = []
    while queue:
        _priority, (step, left, middle, right) = heapq.heappop(queue)
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)
    return tuple(selected), frozenset(current)


def delayed_metrics() -> dict[str, object]:
    state = state_by_depth(7)
    selected, residual = resolve_delayed()
    centers, fibers = middle_fibers(selected)
    shells = middle_shells(fibers)
    steps = set(fibers)
    occurrences = [value for values in fibers.values() for value in values]
    union = set(occurrences)
    multiplicity = Counter(occurrences)
    minimum = min(state.values)
    backbone = {value - minimum for value in state.values if value > minimum}
    imported = union & backbone
    novel = union - backbone

    terminal_mass = harmonic(steps)
    occurrence_mass = sum(
        (harmonic(values) for values in fibers.values()),
        Fraction(),
    )
    union_mass = harmonic(union)
    duplicate_mass = occurrence_mass - union_mass
    average_multiplicity = occurrence_mass / union_mass

    edges = {
        (step, value)
        for step, values in fibers.items()
        for value in values
        if value in steps
    }
    components = strongly_connected_components(steps, edges)
    cyclic = tuple(
        component
        for component in components
        if len(component) > 1 or (component[0], component[0]) in edges
    )
    largest = max(components, key=lambda component: (len(component), component))
    regenerations = canonical_regenerations(shells)
    seed_shells = [
        row for row in shells if frozenset(row[2]) == frozenset({16, 21, 26})
    ]

    return {
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(steps),
        "middle_shells": len(shells),
        "fiber_occurrences": len(occurrences),
        "fiber_union": len(union),
        "imported_union": len(imported),
        "novel_union": len(novel),
        "incidence_edges": len(edges),
        "scc_count": len(components),
        "cyclic_scc_count": len(cyclic),
        "largest_scc": len(largest),
        "maximum_multiplicity": max(multiplicity.values()),
        "q1_centers": len(centers[1]),
        "q1_minimum": centers[1][0],
        "schedule_sha256": schedule_hash(selected, residual),
        "residual_sha256": canonical_set_hash(residual),
        "q1_centers_sha256": canonical_set_hash(centers[1]),
        "q1_fiber_sha256": canonical_set_hash(fibers[1]),
        "edge_sha256": edge_hash(edges),
        "largest_scc_sha256": set_hash(largest),
        "terminal_mass_sha256": fraction_hash(terminal_mass),
        "occurrence_mass_sha256": fraction_hash(occurrence_mass),
        "union_mass_sha256": fraction_hash(union_mass),
        "duplicate_mass_sha256": fraction_hash(duplicate_mass),
        "average_multiplicity_sha256": fraction_hash(average_multiplicity),
        "terminal_mass": terminal_mass,
        "occurrence_mass": occurrence_mass,
        "union_mass": union_mass,
        "duplicate_mass": duplicate_mass,
        "average_multiplicity": average_multiplicity,
        "residual_error": Fraction(state.persistence * len(residual), state.scale),
        "regenerations": regenerations,
        "seed_shells": len(seed_shells),
        "q1_center_set": set(centers[1]),
    }


def assert_between(value: Fraction, lower: Fraction, upper: Fraction) -> None:
    if not lower < value < upper:
        raise AssertionError(f"expected {lower} < {value} < {upper}")


def build_certificate() -> str:
    delayed = delayed_metrics()
    compact = {key: delayed[key] for key in EXPECTED}
    if compact != EXPECTED:
        raise AssertionError(f"delayed metric mismatch: {compact!r}")
    if delayed["regenerations"] or delayed["seed_shells"]:
        raise AssertionError("delayed policy retains canonical regeneration")

    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    from verify_s7_regenerative_seed_policy_dependence import resolve
    lex_schedule, _ = resolve(parent, progressions, False)
    lex_centers, _ = middle_fibers(lex_schedule)
    if set(lex_centers[1]) - delayed["q1_center_set"] != set(DELAYED_CENTERS):
        raise AssertionError("delayed q=1 center difference mismatch")
    if delayed["q1_center_set"] - set(lex_centers[1]):
        raise AssertionError("delayed policy introduced a new q=1 center")

    lex = policy_metrics(False)
    ratios = {
        "terminal": delayed["terminal_mass"] / lex["terminal_mass"],
        "occurrence": delayed["occurrence_mass"] / lex["occurrence_mass"],
        "union": delayed["union_mass"] / lex["union_mass"],
        "duplicate": delayed["duplicate_mass"] / lex["duplicate_mass"],
        "average": delayed["average_multiplicity"] / lex["average_multiplicity"],
    }
    differences = {
        "terminal_increase": delayed["terminal_mass"] - lex["terminal_mass"],
        "occurrence_reduction": lex["occurrence_mass"] - delayed["occurrence_mass"],
        "union_reduction": lex["union_mass"] - delayed["union_mass"],
        "duplicate_reduction": lex["duplicate_mass"] - delayed["duplicate_mass"],
        "average_reduction": lex["average_multiplicity"] - delayed["average_multiplicity"],
    }
    for name, value in ratios.items():
        if fraction_hash(value) != EXPECTED_RATIO_SHA256[name]:
            raise AssertionError(f"{name} ratio hash mismatch")
    for name, value in differences.items():
        if fraction_hash(value) != EXPECTED_DIFFERENCE_SHA256[name]:
            raise AssertionError(f"{name} difference hash mismatch")

    assert_between(delayed["terminal_mass"], Fraction(33, 20), Fraction(5, 3))
    assert_between(delayed["occurrence_mass"], Fraction(7, 4), Fraction(9, 5))
    assert_between(delayed["union_mass"], Fraction(8, 5), Fraction(5, 3))
    assert_between(delayed["duplicate_mass"], Fraction(1, 8), Fraction(2, 15))
    assert_between(delayed["average_multiplicity"], Fraction(27, 25), Fraction(13, 12))
    assert_between(ratios["terminal"], Fraction(6, 5), Fraction(5, 4))
    assert_between(ratios["occurrence"], Fraction(9, 10), Fraction(14, 15))
    assert_between(ratios["union"], Fraction(19, 20), Fraction(24, 25))
    assert_between(ratios["duplicate"], Fraction(2, 3), Fraction(7, 10))
    assert_between(ratios["average"], Fraction(24, 25), Fraction(49, 50))
    if delayed["residual_error"] != Fraction(241, 4096):
        raise AssertionError("delayed residual error mismatch")
    if delayed["residual_error"] - lex["residual_error"] != Fraction(1, 4096):
        raise AssertionError("residual error increment mismatch")

    lines = [
        "S7 DELAYED-SEED POLICY",
        "",
        "policy: lexicographic priority except three q1 seed centers are last",
        "delayed_centers=1354065,1354070,1354075",
        "q1_selected_difference_from_lex=1354065,1354070,1354075",
        "seed_shells=0",
        "canonical_regenerations=0",
        "",
    ]
    for key in EXPECTED:
        lines.append(f"delayed_{key}={delayed[key]}")
    lines.append(f"delayed_residual_error={delayed['residual_error']}")
    lines.extend(
        [
            "",
            "delayed_terminal_mass_bracket=33/20,5/3",
            "delayed_occurrence_mass_bracket=7/4,9/5",
            "delayed_union_mass_bracket=8/5,5/3",
            "delayed_duplicate_mass_bracket=1/8,2/15",
            "delayed_average_multiplicity_bracket=27/25,13/12",
            "",
            "delayed_over_lex_terminal_mass_bracket=6/5,5/4",
            "delayed_over_lex_occurrence_mass_bracket=9/10,14/15",
            "delayed_over_lex_union_mass_bracket=19/20,24/25",
            "delayed_over_lex_duplicate_mass_bracket=2/3,7/10",
            "delayed_over_lex_average_multiplicity_bracket=24/25,49/50",
            "delayed_minus_lex_residual_error=1/4096",
        ]
    )
    for name in ("terminal", "occurrence", "union", "duplicate", "average"):
        lines.append(f"delayed_over_lex_{name}_sha256={EXPECTED_RATIO_SHA256[name]}")
    for name in (
        "terminal_increase",
        "occurrence_reduction",
        "union_reduction",
        "duplicate_reduction",
        "average_reduction",
    ):
        lines.append(f"{name}_sha256={EXPECTED_DIFFERENCE_SHA256[name]}")
    lines.extend(
        [
            "",
            (
                "conclusion: delaying only the three unforced seed-producing "
                "actions removes canonical regeneration and improves"
            ),
            (
                "shell count, occurrence mass, union mass, duplicate mass, "
                "average multiplicity, and maximum multiplicity"
            ),
            (
                "relative to pure lexicographic deletion. The tradeoff is six "
                "additional terminal classes, higher terminal mass,"
            ),
            (
                "and a residual-error increase of exactly 1/4096. This is an "
                "exact Pareto tradeoff, not a completed Bellman proof."
            ),
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_s7_delayed_seed_policy.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
