#!/usr/bin/env python3
"""Compare exact one-generation transition load for two complete S7 policies."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import (
    all_three_aps,
    middle_fibers,
    middle_shells,
    resolve,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "lexicographic": {
        "selected": 9360,
        "residual": 480,
        "terminal_steps": 25,
        "middle_shells": 124,
        "fiber_occurrences": 9335,
        "fiber_union": 6683,
        "imported_union": 312,
        "novel_union": 6371,
        "incidence_edges": 75,
        "scc_count": 19,
        "cyclic_scc_count": 1,
        "largest_scc": 7,
        "maximum_multiplicity": 15,
        "edge_sha256": (
            "f34eb463b3929166945e9db93878774e4b5ca2c241793c4c004aae597ed84bf1"
        ),
        "largest_scc_sha256": (
            "cb78b3ba8da7507643570284d8b1278aa65833a7343bf209c99626ee1a894786"
        ),
        "terminal_mass_sha256": (
            "ef3142242664f73530a522264392acd65e856b412e14600361eaa86693437bc9"
        ),
        "occurrence_mass_sha256": (
            "a84004ce0681ad1bf307ce2b9bffa9194a2b542529cd631fe1b0244236161480"
        ),
        "union_mass_sha256": (
            "3cc8b5a12dee4d0a7250bba894f6abd86e2ae3f5f65f0e94be35a85364690594"
        ),
        "duplicate_mass_sha256": (
            "e97c81f29f389c5c269d4eaf97bda5492ee14fe1f8451c3e159eeeb18f969b91"
        ),
        "average_multiplicity_sha256": (
            "59384bade89a2fb6acbe3150aaf2bc1ea3f5af356fd66c777d94a5339a9457dd"
        ),
    },
    "reverse_lexicographic": {
        "selected": 9180,
        "residual": 660,
        "terminal_steps": 2252,
        "middle_shells": 2374,
        "fiber_occurrences": 6928,
        "fiber_union": 2239,
        "imported_union": 1,
        "novel_union": 2238,
        "incidence_edges": 3087,
        "scc_count": 1967,
        "cyclic_scc_count": 1,
        "largest_scc": 286,
        "maximum_multiplicity": 160,
        "edge_sha256": (
            "0ba8c675768a6f4bd551936cde942d1ad8f992e977a63b6379c782cdfacc6546"
        ),
        "largest_scc_sha256": (
            "5e0ad0aeb220cc662cfde095bae3a89dbb197c4d674563ce5975d5b5f3c21c6c"
        ),
        "terminal_mass_sha256": (
            "c67cea75b2dfaa8690efa91cb7ac31fa8456eb6d3146bac9317f618bbe2fd79a"
        ),
        "occurrence_mass_sha256": (
            "0b1962149add4e9b0a4ca73442b4d6c0bcc9655cdb8dd49e2a38d7c319c6ef4c"
        ),
        "union_mass_sha256": (
            "2dc89277b97b88fbc6a3db0af108de6807a6321b2f60c14fd9c8359b311e7359"
        ),
        "duplicate_mass_sha256": (
            "32b3966afb8a6812204bf18de2de1064358f8795c0203444f0388560910b7cd0"
        ),
        "average_multiplicity_sha256": (
            "9bd318a8c68e1c9c323fb3ef7ee7d22a9891a4cd304c7bbbfb87069e45e8b139"
        ),
    },
}
EXPECTED_RATIO_SHA256 = {
    "terminal": "726bd1baca36f50393c839e4dbb183b835d52c9f17ce66151c7afad5bb199b22",
    "occurrence": "2c1e9173c39de09a6725e956ac5561760620355e1259bf104cb65811841573df",
    "union": "487595d4b71249d5a191d5447737842baa6387fe2894a11af68d0f72056f9740",
    "duplicate": "0f310dcc689cd3c5c646270d619f620b681a3b071d7369456938f2c53bd71d89",
    "average": "134e31f7a871c678cf27219fbe08d1193e72f4826451dd0f4947ca79927ed585",
}
CERTIFICATE_SHA256 = (
    "e4313f37643ad729fb8faa160ae63d5d59d61c521b149258a6aa131485dec70d"
)


def harmonic(values: Iterable[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values if value > 0), Fraction())


def fraction_hash(value: Fraction) -> str:
    payload = f"{value.numerator}/{value.denominator}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def edge_hash(edges: Iterable[tuple[int, int]]) -> str:
    payload = "".join(
        f"{source}->{target}\n"
        for source, target in sorted(set(edges))
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def strongly_connected_components(
    nodes: set[int],
    edges: set[tuple[int, int]],
) -> tuple[tuple[int, ...], ...]:
    graph: dict[int, list[int]] = defaultdict(list)
    for source, target in edges:
        graph[source].append(target)

    index = 0
    stack: list[int] = []
    on_stack: set[int] = set()
    first_index: dict[int, int] = {}
    low_link: dict[int, int] = {}
    result: list[tuple[int, ...]] = []

    def visit(vertex: int) -> None:
        nonlocal index
        first_index[vertex] = index
        low_link[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack.add(vertex)
        for target in sorted(graph[vertex]):
            if target not in first_index:
                visit(target)
                low_link[vertex] = min(low_link[vertex], low_link[target])
            elif target in on_stack:
                low_link[vertex] = min(low_link[vertex], first_index[target])
        if low_link[vertex] == first_index[vertex]:
            component: list[int] = []
            while True:
                target = stack.pop()
                on_stack.remove(target)
                component.append(target)
                if target == vertex:
                    break
            result.append(tuple(sorted(component)))

    for vertex in sorted(nodes):
        if vertex not in first_index:
            visit(vertex)
    return tuple(sorted(result))


def policy_metrics(reverse: bool) -> dict[str, object]:
    state = state_by_depth(7)
    parent = state.values
    progressions = all_three_aps(parent)
    selected, residual = resolve(parent, progressions, reverse)
    _centers, fibers = middle_fibers(selected)
    shells = middle_shells(fibers)
    steps = set(fibers)
    occurrences = [value for values in fibers.values() for value in values]
    union = set(occurrences)
    multiplicity = Counter(occurrences)
    minimum = min(parent)
    backbone = {value - minimum for value in parent if value > minimum}
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
    }


def assert_between(value: Fraction, lower: Fraction, upper: Fraction) -> None:
    if not lower < value < upper:
        raise AssertionError(f"expected {lower} < {value} < {upper}")


def build_certificate() -> str:
    observed = {
        "lexicographic": policy_metrics(False),
        "reverse_lexicographic": policy_metrics(True),
    }
    for name, expected in EXPECTED.items():
        compact = {key: observed[name][key] for key in expected}
        if compact != expected:
            raise AssertionError(f"{name} metric mismatch: {compact!r}")

    lex = observed["lexicographic"]
    reverse = observed["reverse_lexicographic"]
    ratios = {
        "terminal": reverse["terminal_mass"] / lex["terminal_mass"],
        "occurrence": reverse["occurrence_mass"] / lex["occurrence_mass"],
        "union": reverse["union_mass"] / lex["union_mass"],
        "duplicate": reverse["duplicate_mass"] / lex["duplicate_mass"],
        "average": reverse["average_multiplicity"] / lex["average_multiplicity"],
    }
    for name, value in ratios.items():
        if fraction_hash(value) != EXPECTED_RATIO_SHA256[name]:
            raise AssertionError(f"{name} ratio hash mismatch")

    assert_between(lex["terminal_mass"], Fraction(13, 10), Fraction(4, 3))
    assert_between(reverse["terminal_mass"], Fraction(11, 5), Fraction(9, 4))
    assert_between(lex["occurrence_mass"], Fraction(19, 10), Fraction(2))
    assert_between(reverse["occurrence_mass"], Fraction(144), Fraction(145))
    assert_between(lex["union_mass"], Fraction(17, 10), Fraction(7, 4))
    assert_between(reverse["union_mass"], Fraction(19, 5), Fraction(4))
    assert_between(lex["duplicate_mass"], Fraction(3, 16), Fraction(1, 5))
    assert_between(reverse["duplicate_mass"], Fraction(140), Fraction(141))
    assert_between(lex["average_multiplicity"], Fraction(11, 10), Fraction(10, 9))
    assert_between(reverse["average_multiplicity"], Fraction(37), Fraction(38))
    assert_between(ratios["terminal"], Fraction(5, 3), Fraction(17, 10))
    assert_between(ratios["occurrence"], Fraction(75), Fraction(76))
    assert_between(ratios["union"], Fraction(2), Fraction(9, 4))
    assert_between(ratios["duplicate"], Fraction(744), Fraction(745))
    assert_between(ratios["average"], Fraction(33), Fraction(34))
    if lex["residual_error"] != Fraction(15, 256):
        raise AssertionError("lex residual error mismatch")
    if reverse["residual_error"] != Fraction(165, 2048):
        raise AssertionError("reverse residual error mismatch")

    lines = [
        "S7 POLICY TRANSITION TRADEOFF",
        "",
    ]
    for name in ("lexicographic", "reverse_lexicographic"):
        prefix = "lex" if name == "lexicographic" else "reverse"
        row = observed[name]
        for key in (
            "selected",
            "residual",
            "terminal_steps",
            "middle_shells",
            "fiber_occurrences",
            "fiber_union",
            "imported_union",
            "novel_union",
            "incidence_edges",
            "scc_count",
            "cyclic_scc_count",
            "largest_scc",
            "maximum_multiplicity",
            "edge_sha256",
            "largest_scc_sha256",
            "terminal_mass_sha256",
            "occurrence_mass_sha256",
            "union_mass_sha256",
            "duplicate_mass_sha256",
            "average_multiplicity_sha256",
        ):
            lines.append(f"{prefix}_{key}={row[key]}")
        lines.append(
            f"{prefix}_residual_error={row['residual_error'].numerator}/"
            f"{row['residual_error'].denominator}"
        )
        lines.append("")

    lines.extend(
        [
            "lex_terminal_mass_bracket=13/10,4/3",
            "reverse_terminal_mass_bracket=11/5,9/4",
            "lex_occurrence_mass_bracket=19/10,2",
            "reverse_occurrence_mass_bracket=144,145",
            "lex_union_mass_bracket=17/10,7/4",
            "reverse_union_mass_bracket=19/5,4",
            "lex_duplicate_mass_bracket=3/16,1/5",
            "reverse_duplicate_mass_bracket=140,141",
            "lex_average_multiplicity_bracket=11/10,10/9",
            "reverse_average_multiplicity_bracket=37,38",
            "",
            "reverse_over_lex_terminal_mass_bracket=5/3,17/10",
            "reverse_over_lex_occurrence_mass_bracket=75,76",
            "reverse_over_lex_union_mass_bracket=2,9/4",
            "reverse_over_lex_duplicate_mass_bracket=744,745",
            "reverse_over_lex_average_multiplicity_bracket=33,34",
        ]
    )
    for name in ("terminal", "occurrence", "union", "duplicate", "average"):
        lines.append(
            f"reverse_over_lex_{name}_sha256={EXPECTED_RATIO_SHA256[name]}"
        )
    lines.extend(
        [
            "",
            (
                "conclusion: avoiding the canonical regenerative seed by the "
                "reverse policy does not reduce raw one-generation cost."
            ),
            (
                "It produces more terminal classes, more shells, a 286-label "
                "cyclic SCC, over 75 times the middle-fiber occurrence mass,"
            ),
            (
                "and over 744 times the duplicate mass of the lexicographic "
                "schedule. Policy optimization must use complete transition cost."
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
        raise SystemExit("usage: verify_s7_policy_transition_tradeoff.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
