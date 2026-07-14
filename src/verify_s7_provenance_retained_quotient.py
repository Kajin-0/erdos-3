#!/usr/bin/env python3
"""Certify a point-disjoint retained-child quotient for the local S7 policy."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from export_simultaneous_deletion_transition import (
    canonical_set_hash,
    verify_schedule,
)
from verify_s1_deletion_dag_adapter import (
    ShellOccurrence,
    build_shell_occurrences,
    harmonic,
    middle_resolution,
)
from verify_s7_local_optimum_transition_profile import resolve_named_policy
from verify_s7_regenerative_seed_policy_dependence import all_three_aps

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "raw_occurrences": 131,
    "exact_state_classes": 87,
    "conflict_edges": 290,
    "conflict_components": 20,
    "largest_conflict_component": 13,
    "component_candidate_subsets_examined": 14_342,
    "component_feasible_independent_subsets": 123,
    "components_with_nonunique_optimum": 0,
    "retained_state_classes": 21,
    "retained_backbone_classes": 2,
    "retained_middle_fiber_classes": 19,
    "retained_distinct_labels": 11_753,
    "dropped_distinct_labels": 5_018,
}
EXPECTED_CLASS_FAMILY_HASH = (
    "085466945406ef79efa8069407a616746fcef531e84fbbb6d67575cc9f0eb171"
)
EXPECTED_CONFLICT_GRAPH_HASH = (
    "c497e9dbe6a22269f0b67f23b07ecf08a0967365f5e328fef262276cfca398aa"
)
EXPECTED_COMPONENT_CERTIFICATE_HASH = (
    "08ad3ea2a4997b8e77eca0484e277c16f2204f875738a9a2a17255c13c4df499"
)
EXPECTED_RETAINED_CLASS_HASH = (
    "06974ccdaf87ca0bb4d6402b1dbb1859e768febc7f6032cf59c7a929e1f0ac56"
)
EXPECTED_REPRESENTATIVE_HASH = (
    "2e9adb1bb0610a90ebbed4c073a770f404cde36eb5c7b59627f4a454f8c3be09"
)
EXPECTED_RETAINED_FAMILY_HASH = (
    "824b2748bc81ad5668543dbc2137221532a8dacfb585defe65c730dc5bdfa691"
)
EXPECTED_RETAINED_UNION_HASH = (
    "798ff914c5f10ea5fd102c8652f748f2807b3c237b06d6f822dc62be52378a0a"
)
EXPECTED_DROPPED_UNION_HASH = (
    "76afbef3d33f42ca3fcfeb5790a40384d383425872cd8b22c6c9eb80c9ef2d32"
)
EXPECTED_RETAINED_MASS_HASH = (
    "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446"
)
EXPECTED_RAW_CLASS_MASS_HASH = (
    "23791250ca8f7452c88dd22eed503989268ee49d30cfa9d7ffef6052d4e55daa"
)
EXPECTED_RAW_UNION_MASS_HASH = (
    "1ae8ae9c2b1e46f73760c731701d24550999513c77780ed86df718b67994acf0"
)
EXPECTED_RAW_OCCURRENCE_MASS_HASH = (
    "afcbddf8690fad4239ac33a6412649f2aa90d87188f7ec4b84724457b521a880"
)
EXPECTED_RATIO_HASHES = {
    "retained_over_raw_union_mass": (
        Fraction(731, 1_000),
        Fraction(732, 1_000),
        "c788311f7cbefaed1a849f778b59a19632f0de4ecee0a7fe9aa02b1cbfdc0c46",
    ),
    "retained_over_raw_exact_class_mass": (
        Fraction(654, 1_000),
        Fraction(655, 1_000),
        "1666a082934bd39a8fceeba00a95c308de91b2ad5eb6e65907ac6b23738ae23f",
    ),
    "retained_over_raw_occurrence_mass": (
        Fraction(582, 1_000),
        Fraction(583, 1_000),
        "c5c8da4298da145b5a7786e0f53feb700ead90af4500e42274f0001e455c56ca",
    ),
    "retained_over_raw_union_cardinality": (
        Fraction(700, 1_000),
        Fraction(701, 1_000),
        "2b65f7ebfeaf1082584087fb4b7e9a85ed8eb4939513eec863a94547a3cfcaca",
    ),
}
CERTIFICATE_SHA256 = (
    "2a1dd14ee54a9a1b39cc19d4fefc70f54b1157be82f496e2107d3a717052ff92"
)


@dataclass(frozen=True)
class ExactStateClass:
    index: int
    representative: ShellOccurrence
    members: tuple[int, ...]
    values: tuple[int, ...]
    weight: Fraction


def fraction_hash(value: Fraction) -> str:
    payload = f"{value.numerator}/{value.denominator}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def exact_state_classes(
    occurrences: tuple[ShellOccurrence, ...],
) -> tuple[ExactStateClass, ...]:
    groups: dict[tuple[int, ...], list[ShellOccurrence]] = defaultdict(list)
    for occurrence in occurrences:
        groups[occurrence.values].append(occurrence)

    result: list[ExactStateClass] = []
    for values, members in sorted(groups.items()):
        representative = min(
            members,
            key=lambda occurrence: (
                0 if occurrence.source == "backbone" else 1,
                -1 if occurrence.source_step is None else occurrence.source_step,
                occurrence.index,
            ),
        )
        result.append(
            ExactStateClass(
                index=len(result),
                representative=representative,
                members=tuple(occurrence.index for occurrence in members),
                values=values,
                weight=harmonic(values),
            )
        )
    return tuple(result)


def conflict_graph(
    classes: tuple[ExactStateClass, ...],
) -> dict[int, set[int]]:
    adjacency = {state.index: set() for state in classes}
    value_sets = [set(state.values) for state in classes]
    for left in range(len(classes)):
        for right in range(left + 1, len(classes)):
            if (
                classes[left].representative.exponent
                == classes[right].representative.exponent
                and value_sets[left] & value_sets[right]
            ):
                adjacency[left].add(right)
                adjacency[right].add(left)
    return adjacency


def connected_components(
    adjacency: dict[int, set[int]],
) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    result: list[tuple[int, ...]] = []
    for vertex in sorted(adjacency):
        if vertex in seen:
            continue
        stack = [vertex]
        seen.add(vertex)
        component: list[int] = []
        while stack:
            current = stack.pop()
            component.append(current)
            for target in sorted(adjacency[current], reverse=True):
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        result.append(tuple(sorted(component)))
    return tuple(result)


def maximum_weight_independent_sets(
    component: tuple[int, ...],
    classes: tuple[ExactStateClass, ...],
    adjacency: dict[int, set[int]],
) -> tuple[Fraction, tuple[tuple[int, ...], ...], int, int]:
    best_weight = Fraction(-1)
    optimizers: list[tuple[int, ...]] = []
    feasible = 0
    total = 1 << len(component)

    for mask in range(total):
        chosen: list[int] = []
        valid = True
        for offset, vertex in enumerate(component):
            if not (mask >> offset) & 1:
                continue
            if any(target in adjacency[vertex] for target in chosen):
                valid = False
                break
            chosen.append(vertex)
        if not valid:
            continue
        feasible += 1
        weight = sum(
            (classes[vertex].weight for vertex in chosen),
            Fraction(),
        )
        choice = tuple(chosen)
        if weight > best_weight:
            best_weight = weight
            optimizers = [choice]
        elif weight == best_weight:
            optimizers.append(choice)

    return best_weight, tuple(sorted(optimizers)), feasible, total


def build_certificate() -> str:
    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    selected, residual = resolve_named_policy("local37", parent, progressions)
    verify_schedule(parent, selected, residual)
    _steps, fibers, _terminal_sponsor, fiber_provenance = middle_resolution(
        selected
    )
    occurrences = build_shell_occurrences(parent, fibers, fiber_provenance)
    classes = exact_state_classes(occurrences)
    adjacency = conflict_graph(classes)
    components = connected_components(adjacency)

    ordered_components = tuple(
        sorted(
            components,
            key=lambda component: (
                classes[component[0]].representative.exponent,
                component,
            ),
        )
    )
    selected_classes: list[int] = []
    component_rows: list[tuple[int, tuple[int, ...], tuple[int, ...], int]] = []
    total_examined = 0
    total_feasible = 0
    nonunique = 0
    for component in ordered_components:
        _weight, optimizers, feasible, total = maximum_weight_independent_sets(
            component, classes, adjacency
        )
        total_examined += total
        total_feasible += feasible
        if len(optimizers) != 1:
            nonunique += 1
        choice = optimizers[0]
        selected_classes.extend(choice)
        component_rows.append(
            (
                classes[component[0]].representative.exponent,
                component,
                choice,
                len(optimizers),
            )
        )

    selected_indices = tuple(sorted(selected_classes))
    retained = tuple(classes[index] for index in selected_indices)
    retained_union = frozenset(
        value for state in retained for value in state.values
    )
    raw_union = frozenset(
        value for state in classes for value in state.values
    )
    dropped_union = raw_union - retained_union

    retained_mass = sum((state.weight for state in retained), Fraction())
    raw_class_mass = sum((state.weight for state in classes), Fraction())
    raw_union_mass = harmonic(raw_union)
    raw_occurrence_mass = sum(
        (harmonic(occurrence.values) for occurrence in occurrences),
        Fraction(),
    )

    class_records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "members": list(state.members),
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
        }
        for state in classes
    ]
    class_payload = json.dumps(
        class_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    class_hash = hashlib.sha256(class_payload.encode("utf-8")).hexdigest()
    if class_hash != EXPECTED_CLASS_FAMILY_HASH:
        raise AssertionError(f"class-family hash mismatch: {class_hash}")

    edge_payload = "".join(
        f"{left}->{right}\n"
        for left in sorted(adjacency)
        for right in sorted(adjacency[left])
        if left < right
    )
    graph_hash = hashlib.sha256(edge_payload.encode("utf-8")).hexdigest()
    if graph_hash != EXPECTED_CONFLICT_GRAPH_HASH:
        raise AssertionError(f"conflict-graph hash mismatch: {graph_hash}")

    component_payload = "".join(
        f"{exponent}:{','.join(map(str, component))}:{optimizer_count}:"
        f"{','.join(map(str, choice))}\n"
        for exponent, component, choice, optimizer_count in component_rows
    )
    component_hash = hashlib.sha256(
        component_payload.encode("utf-8")
    ).hexdigest()
    if component_hash != EXPECTED_COMPONENT_CERTIFICATE_HASH:
        raise AssertionError(f"component hash mismatch: {component_hash}")

    selected_payload = ",".join(map(str, selected_indices))
    selected_hash = hashlib.sha256(
        selected_payload.encode("utf-8")
    ).hexdigest()
    if selected_hash != EXPECTED_RETAINED_CLASS_HASH:
        raise AssertionError("retained-class hash mismatch")

    representative_indices = tuple(
        state.representative.index for state in retained
    )
    representative_payload = ",".join(map(str, representative_indices))
    representative_hash = hashlib.sha256(
        representative_payload.encode("utf-8")
    ).hexdigest()
    if representative_hash != EXPECTED_REPRESENTATIVE_HASH:
        raise AssertionError("representative hash mismatch")

    retained_records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
        }
        for state in retained
    ]
    retained_payload = json.dumps(
        retained_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    retained_hash = hashlib.sha256(
        retained_payload.encode("utf-8")
    ).hexdigest()
    if retained_hash != EXPECTED_RETAINED_FAMILY_HASH:
        raise AssertionError("retained-family hash mismatch")

    retained_backbone = sum(
        state.representative.source == "backbone" for state in retained
    )
    retained_middle = sum(
        state.representative.source == "middle_fiber" for state in retained
    )
    conflict_edges = sum(len(targets) for targets in adjacency.values()) // 2
    observed = {
        "raw_occurrences": len(occurrences),
        "exact_state_classes": len(classes),
        "conflict_edges": conflict_edges,
        "conflict_components": len(components),
        "largest_conflict_component": max(len(component) for component in components),
        "component_candidate_subsets_examined": total_examined,
        "component_feasible_independent_subsets": total_feasible,
        "components_with_nonunique_optimum": nonunique,
        "retained_state_classes": len(retained),
        "retained_backbone_classes": retained_backbone,
        "retained_middle_fiber_classes": retained_middle,
        "retained_distinct_labels": len(retained_union),
        "dropped_distinct_labels": len(dropped_union),
    }
    if observed != EXPECTED:
        raise AssertionError(f"retention metric mismatch: {observed!r}")

    if sum(len(state.values) for state in retained) != len(retained_union):
        raise AssertionError("retained states are not point-disjoint")
    if not all(
        len(state.values) == len(state.representative.provenance)
        for state in retained
    ):
        raise AssertionError("retained provenance is incomplete")
    if canonical_set_hash(retained_union) != EXPECTED_RETAINED_UNION_HASH:
        raise AssertionError("retained-union hash mismatch")
    if canonical_set_hash(dropped_union) != EXPECTED_DROPPED_UNION_HASH:
        raise AssertionError("dropped-union hash mismatch")

    mass_hashes = {
        "retained": fraction_hash(retained_mass),
        "raw_class": fraction_hash(raw_class_mass),
        "raw_union": fraction_hash(raw_union_mass),
        "raw_occurrence": fraction_hash(raw_occurrence_mass),
    }
    expected_mass_hashes = {
        "retained": EXPECTED_RETAINED_MASS_HASH,
        "raw_class": EXPECTED_RAW_CLASS_MASS_HASH,
        "raw_union": EXPECTED_RAW_UNION_MASS_HASH,
        "raw_occurrence": EXPECTED_RAW_OCCURRENCE_MASS_HASH,
    }
    if mass_hashes != expected_mass_hashes:
        raise AssertionError(f"mass hash mismatch: {mass_hashes!r}")

    ratios = {
        "retained_over_raw_union_mass": retained_mass / raw_union_mass,
        "retained_over_raw_exact_class_mass": retained_mass / raw_class_mass,
        "retained_over_raw_occurrence_mass": retained_mass / raw_occurrence_mass,
        "retained_over_raw_union_cardinality": Fraction(
            len(retained_union), len(raw_union)
        ),
    }
    for name, value in ratios.items():
        lower, upper, expected_hash = EXPECTED_RATIO_HASHES[name]
        if not lower < value < upper:
            raise AssertionError(f"{name} outside compact bracket")
        if fraction_hash(value) != expected_hash:
            raise AssertionError(f"{name} hash mismatch")

    lines = [
        "S7 PROVENANCE RETAINED-CHILD QUOTIENT",
        "",
        "policy=local37",
        (
            "duplicate_rule=one_exact_state_class_with_backbone_then_"
            "source_step_then_occurrence_representative"
        ),
        "conflict_rule=nonempty_numerical_intersection_within_dyadic_shell",
        (
            "selection_rule=unique_maximum_harmonic_independent_set_per_"
            "conflict_component"
        ),
        "",
        f"raw_occurrences={observed['raw_occurrences']}",
        f"exact_state_classes={observed['exact_state_classes']}",
        f"conflict_edges={observed['conflict_edges']}",
        f"conflict_components={observed['conflict_components']}",
        f"largest_conflict_component={observed['largest_conflict_component']}",
        (
            "component_candidate_subsets_examined="
            f"{observed['component_candidate_subsets_examined']}"
        ),
        (
            "component_feasible_independent_subsets="
            f"{observed['component_feasible_independent_subsets']}"
        ),
        (
            "components_with_nonunique_optimum="
            f"{observed['components_with_nonunique_optimum']}"
        ),
        f"class_family_sha256={EXPECTED_CLASS_FAMILY_HASH}",
        f"conflict_graph_sha256={EXPECTED_CONFLICT_GRAPH_HASH}",
        f"component_certificate_sha256={EXPECTED_COMPONENT_CERTIFICATE_HASH}",
        "",
        f"retained_state_classes={observed['retained_state_classes']}",
        f"retained_backbone_classes={observed['retained_backbone_classes']}",
        (
            "retained_middle_fiber_classes="
            f"{observed['retained_middle_fiber_classes']}"
        ),
        f"retained_distinct_labels={observed['retained_distinct_labels']}",
        f"dropped_distinct_labels={observed['dropped_distinct_labels']}",
        "retained_point_disjoint=True",
        "retained_provenance_assigned=True",
        f"retained_class_indices_sha256={EXPECTED_RETAINED_CLASS_HASH}",
        f"retained_representatives_sha256={EXPECTED_REPRESENTATIVE_HASH}",
        f"retained_family_sha256={EXPECTED_RETAINED_FAMILY_HASH}",
        f"retained_union_sha256={EXPECTED_RETAINED_UNION_HASH}",
        f"dropped_union_sha256={EXPECTED_DROPPED_UNION_HASH}",
        "",
        f"retained_harmonic_mass_sha256={EXPECTED_RETAINED_MASS_HASH}",
        f"raw_exact_class_mass_sha256={EXPECTED_RAW_CLASS_MASS_HASH}",
        f"raw_union_mass_sha256={EXPECTED_RAW_UNION_MASS_HASH}",
        f"raw_occurrence_mass_sha256={EXPECTED_RAW_OCCURRENCE_MASS_HASH}",
        "retained_over_raw_union_mass_bracket=731/1000,732/1000",
        (
            "retained_over_raw_union_mass_sha256="
            f"{EXPECTED_RATIO_HASHES['retained_over_raw_union_mass'][2]}"
        ),
        "retained_over_raw_exact_class_mass_bracket=654/1000,655/1000",
        (
            "retained_over_raw_exact_class_mass_sha256="
            f"{EXPECTED_RATIO_HASHES['retained_over_raw_exact_class_mass'][2]}"
        ),
        "retained_over_raw_occurrence_mass_bracket=582/1000,583/1000",
        (
            "retained_over_raw_occurrence_mass_sha256="
            f"{EXPECTED_RATIO_HASHES['retained_over_raw_occurrence_mass'][2]}"
        ),
        "retained_over_raw_union_cardinality_bracket=700/1000,701/1000",
        (
            "retained_over_raw_union_cardinality_sha256="
            f"{EXPECTED_RATIO_HASHES['retained_over_raw_union_cardinality'][2]}"
        ),
        "",
        (
            "conclusion: exact duplicate quotienting followed by componentwise "
            "maximum-harmonic conflict selection"
        ),
        (
            "produces a unique 21-state point-disjoint recursive family with "
            "explicit representative provenance."
        ),
        (
            "This is a legitimate one-generation retained-child quotient for "
            "the recorded local-optimum transition."
        ),
        (
            "Cross-generation provenance reuse and the resulting Bellman "
            "inequality remain open."
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
            "usage: verify_s7_provenance_retained_quotient.py [OUTPUT]"
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
