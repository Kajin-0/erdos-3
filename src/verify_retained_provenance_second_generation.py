#!/usr/bin/env python3
"""Propagate the retained S7 family and certify provenance reuse exactly."""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable
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
from verify_s7_provenance_retained_quotient import (
    conflict_graph,
    connected_components,
    exact_state_classes,
    maximum_weight_independent_sets,
)
from verify_s7_regenerative_seed_policy_dependence import all_three_aps, v2

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "first_generation_retained_states": 21,
    "first_generation_retained_labels": 11_753,
    "child_transitions_with_selected_actions": 15,
    "child_transitions_with_outputs": 19,
    "child_selected_actions": 10_426,
    "child_terminal_residual_points": 1_327,
    "second_generation_raw_occurrences": 442,
    "second_generation_exact_state_classes": 173,
    "second_generation_conflict_edges": 1_046,
    "second_generation_conflict_components": 22,
    "second_generation_largest_component": 21,
    "second_generation_dp_states_examined": 204,
    "second_generation_components_with_nonunique_optimum": 0,
    "second_generation_retained_states": 27,
    "second_generation_retained_labels": 7_925,
    "second_generation_dropped_labels": 5_900,
    "root_provenance_occurrences": 7_925,
    "root_provenance_distinct_labels": 7_648,
    "root_provenance_repeated_labels": 272,
    "root_provenance_extra_occurrences": 277,
    "root_provenance_multiplicity_1": 7_376,
    "root_provenance_multiplicity_2": 267,
    "root_provenance_multiplicity_3": 5,
    "root_provenance_maximum_multiplicity": 3,
    "root_provenance_cross_parent_reuse_labels": 265,
    "root_provenance_maximum_parent_branches": 2,
}
EXPECTED_HASHES = {
    "first_generation_retained_family": "824b2748bc81ad5668543dbc2137221532a8dacfb585defe65c730dc5bdfa691",
    "child_transition_summary": "7c18dcc4e75a1e04f5d6b23654232ec7130637ac8a0ebf96a4a94bc088a5e2bc",
    "child_transition_family": "ca166e572be9382a3aaf6164a5427971b5f1916840b9f4e1fb648c8d2a20ce59",
    "second_generation_raw_occurrence_family": "b447ee7aeb32dbc225cbe1bee83056a522343b51bca79e65d0ef166293c1ce46",
    "second_generation_exact_class_family": "393ab66f44f325a8aee598a0fafcfcb011081a2c620a896b027858170117824b",
    "second_generation_conflict_graph": "7c5554d1369685c283b6d05ba245c2264338c229f89a129e099c0d74a511454f",
    "second_generation_component_certificate": "0639678bcc2af63bd5046b67ee57f6b6b56585ec47f72c5759ad272e65cb0a43",
    "second_generation_retained_class_indices": "3deb5c599b0cbb386de854537524f72686d4c0cc3b39d6a0a75a20ea6cc0b93e",
    "second_generation_retained_representatives": "2b00bd278c4d7fb8500a4627cb40827ef7ec09b96dbf7bb0241ef779cc4ca281",
    "second_generation_retained_family": "dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596",
    "second_generation_retained_union": "ec30d00bafc325939dd770c48a101f5d42eeecefe1f819863af0067e047b6c28",
    "second_generation_dropped_union": "aa430ebe7e95014fd5104d944b3e3009fd5f1cd2f4aef2441b5e9f57d70f141f",
    "root_provenance_map": "33a9000d0c9e4568fe59124931eba19eda2ea534bc5e1b0c7932b00aad429b05",
    "root_provenance_repeated_labels": "8d6a39ffc2e92688bca56dc06e42c7cfdd9ee058f96193294023b4a2f48f184c",
    "root_provenance_triple_labels": "cd0300d94629716e5e743e34a9349d02ffec5e5ec894b21d7403a08c81fcb02b",
    "root_provenance_cross_parent_labels": "03a068c7b213d10c043f6b540a33babe52ecd93e7588a25d8eb073a5b6b01218",
}
EXPECTED_MASS_HASHES = {
    "first_generation_retained": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
    "second_generation_retained": "05febea047257947cc84dcd14b126c6a904013a3a7b1edf13a84e7ff8dd1ab1f",
    "second_generation_raw_union": "b6acc85a27c8930d3311379e7079ffcd5d178c2dc84617d868b8690acd6b5f0b",
    "second_generation_raw_class": "4004ba7a05ffe214239ed4a23253302a4cc0643e4448e61b7e543222b70ec8c3",
    "second_generation_raw_occurrence": "31511dab438b2e65c3e5b46ee7b54d4437c39ed69f53f85bdb990f8701e72755",
    "root_provenance_unique": "1ce2bbb31b3c24f418f92224ddd43f9d9a95de1c7353b057cba43688af052e7f",
    "root_provenance_occurrence": "86857e54a7a6894b4e420febb499b41eacd27e96c36df2c7ad80d6b7383fd1c5",
    "root_provenance_repeat": "54523d56a8a14c383d56861dbc74b6ec05ccb31dfe3464955bfe598a0de4110d",
}
EXPECTED_RATIOS = {
    "second_retained_over_first_retained": (
        Fraction(6_828, 1_000),
        Fraction(6_829, 1_000),
        "5e9af8fd7c914be0323c824d7f98dcea158dcd868b4c3a33a81ede7877ba252f",
    ),
    "second_retained_over_second_raw_union": (
        Fraction(896, 1_000),
        Fraction(897, 1_000),
        "826c2fc54c7f59d5e06f4120694cce2e64eb1fe6eb338e27ab7543b7ced4bad9",
    ),
    "second_retained_over_second_raw_class": (
        Fraction(639, 1_000),
        Fraction(640, 1_000),
        "8f28f4ce143bf6d05d14963b5417408d4ef818a117b94df3dc0971842cfc4690",
    ),
    "second_retained_over_second_raw_occurrence": (
        Fraction(206, 1_000),
        Fraction(207, 1_000),
        "9d8a0b68314d0fa3af861c9c75a137c5b73b18cdd67db48d2f73f25e0325f9ea",
    ),
    "second_retained_cardinality_over_raw_union": (
        Fraction(573, 1_000),
        Fraction(574, 1_000),
        "c4322b8b534e56a24e4ebf5071eabd27af983735d0ed27894b5ce24f0c7179d9",
    ),
    "provenance_occurrence_over_unique": (
        Fraction(1_040, 1_000),
        Fraction(1_041, 1_000),
        "e4386a4c58032d94284819d649884af096caeafd119b186b875815c3ad19bf54",
    ),
    "provenance_repeat_over_unique": (
        Fraction(40, 1_000),
        Fraction(41, 1_000),
        "22a80186b516b7e59be35eb9cb1deb90adf63d7d6d381dde950646c08f90569f",
    ),
}
CERTIFICATE_SHA256 = "79fca7aa04469adefdd855d08a63b4bbefd7621c6c324d54cd6748f54e734caa"


@dataclass(frozen=True)
class DescendantOccurrence:
    index: int
    parent_class: int
    source: str
    source_step: int | None
    exponent: int
    values: tuple[int, ...]
    provenance: tuple[int, ...]
    immediate_provenance: tuple[int, ...]


@dataclass(frozen=True)
class DescendantClass:
    index: int
    representative: DescendantOccurrence
    members: tuple[int, ...]
    values: tuple[int, ...]
    weight: Fraction


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def shell_partition(values: Iterable[int]) -> dict[int, tuple[int, ...]]:
    shells: dict[int, list[int]] = defaultdict(list)
    for value in sorted(set(values)):
        shells[value.bit_length() - 1].append(value)
    return {
        exponent: tuple(shells[exponent])
        for exponent in sorted(shells)
    }


def resolve_lexicographic(
    parent: frozenset[int],
) -> tuple[tuple[tuple[int, ...], ...], frozenset[int]]:
    progressions = all_three_aps(parent)
    current = set(parent)
    selected: list[tuple[int, ...]] = []
    for step, left, middle, right in progressions:
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)
    residual = frozenset(current)
    if all_three_aps(residual):
        raise AssertionError("lexicographic residual contains a three-term AP")
    return tuple(selected), residual


def selected_middle_resolution(
    selected: tuple[tuple[int, ...], ...],
) -> tuple[dict[int, frozenset[int]], dict[tuple[int, int], int]]:
    centers: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for sponsor, middle, _opposite, step, _left, _right in selected:
        centers[step].append((middle, sponsor))
    fibers: dict[int, frozenset[int]] = {}
    provenance: dict[tuple[int, int], int] = {}
    for step in sorted(centers):
        ordered = sorted(centers[step])
        minimum = ordered[0][0]
        differences: set[int] = set()
        for center, sponsor in ordered[1:]:
            difference = center - minimum
            differences.add(difference)
            provenance[(step, difference)] = sponsor
        fibers[step] = frozenset(differences)
    return fibers, provenance


def build_descendant_occurrences(
    parent_class: int,
    values: tuple[int, ...],
    root_provenance: tuple[int, ...],
    selected: tuple[tuple[int, ...], ...],
) -> list[tuple[int, str, int | None, int, tuple[int, ...], tuple[int, ...], tuple[int, ...]]]:
    root_map = dict(zip(values, root_provenance, strict=True))
    fibers, fiber_provenance = selected_middle_resolution(selected)
    minimum = min(values)
    backbone = {value - minimum for value in values if value > minimum}
    result = []
    for exponent, shell_values in shell_partition(backbone).items():
        immediate = tuple(minimum + value for value in shell_values)
        provenance = tuple(root_map[value] for value in immediate)
        result.append(
            (
                parent_class,
                "backbone",
                None,
                exponent,
                shell_values,
                provenance,
                immediate,
            )
        )
    for step in sorted(fibers):
        for exponent, shell_values in shell_partition(fibers[step]).items():
            immediate = tuple(
                fiber_provenance[(step, value)] for value in shell_values
            )
            provenance = tuple(root_map[value] for value in immediate)
            result.append(
                (
                    parent_class,
                    "middle_fiber",
                    step,
                    exponent,
                    shell_values,
                    provenance,
                    immediate,
                )
            )
    return result


def descendant_classes(
    occurrences: tuple[DescendantOccurrence, ...],
) -> tuple[DescendantClass, ...]:
    groups: dict[tuple[int, ...], list[DescendantOccurrence]] = defaultdict(list)
    for occurrence in occurrences:
        groups[occurrence.values].append(occurrence)
    result: list[DescendantClass] = []
    for values, members in sorted(groups.items()):
        representative = min(
            members,
            key=lambda occurrence: (
                occurrence.parent_class,
                0 if occurrence.source == "backbone" else 1,
                -1 if occurrence.source_step is None else occurrence.source_step,
                occurrence.index,
            ),
        )
        result.append(
            DescendantClass(
                index=len(result),
                representative=representative,
                members=tuple(occurrence.index for occurrence in members),
                values=values,
                weight=harmonic(values),
            )
        )
    return tuple(result)


def descendant_conflict_graph(
    classes: tuple[DescendantClass, ...],
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


def components(adjacency: dict[int, set[int]]) -> tuple[tuple[int, ...], ...]:
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


def maximum_weight_independent_set_dp(
    component: tuple[int, ...],
    classes: tuple[DescendantClass, ...],
    adjacency: dict[int, set[int]],
) -> tuple[Fraction, int, tuple[int, ...], int]:
    position = {vertex: index for index, vertex in enumerate(component)}
    neighbor_masks: list[int] = []
    for vertex in component:
        mask = 0
        for target in adjacency[vertex]:
            if target in position:
                mask |= 1 << position[target]
        neighbor_masks.append(mask)
    weights = [classes[vertex].weight for vertex in component]

    @lru_cache(maxsize=None)
    def solve(mask: int) -> tuple[Fraction, int, int]:
        if mask == 0:
            return Fraction(), 1, 0
        index = (mask & -mask).bit_length() - 1
        without = mask & ~(1 << index)
        excluded_weight, excluded_count, excluded_choice = solve(without)
        included_mask = without & ~neighbor_masks[index]
        included_weight, included_count, included_choice = solve(included_mask)
        included_weight += weights[index]
        included_choice |= 1 << index
        if included_weight > excluded_weight:
            return included_weight, included_count, included_choice
        if excluded_weight > included_weight:
            return excluded_weight, excluded_count, excluded_choice

        def choice_tuple(choice_mask: int) -> tuple[int, ...]:
            return tuple(
                component[offset]
                for offset in range(len(component))
                if (choice_mask >> offset) & 1
            )

        canonical = min(
            excluded_choice,
            included_choice,
            key=choice_tuple,
        )
        return excluded_weight, excluded_count + included_count, canonical

    weight, count, choice_mask = solve((1 << len(component)) - 1)
    choice = tuple(
        component[offset]
        for offset in range(len(component))
        if (choice_mask >> offset) & 1
    )
    return weight, count, choice, solve.cache_info().currsize


def first_generation_retained_family() -> tuple[object, ...]:
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
    retained_indices: list[int] = []
    for component in sorted(
        connected_components(adjacency),
        key=lambda item: (classes[item[0]].representative.exponent, item),
    ):
        _weight, optimizers, _feasible, _total = maximum_weight_independent_sets(
            component, classes, adjacency
        )
        if len(optimizers) != 1:
            raise AssertionError("first-generation optimum is not unique")
        retained_indices.extend(optimizers[0])
    return tuple(classes[index] for index in sorted(retained_indices))


def build_certificate() -> str:
    retained_first = first_generation_retained_family()
    first_records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
        }
        for state in retained_first
    ]
    first_payload = json.dumps(
        first_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if hashlib.sha256(first_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "first_generation_retained_family"
    ]:
        raise AssertionError("first-generation retained-family hash mismatch")

    raw_rows = []
    child_stats = []
    transition_records = []
    for state in retained_first:
        values = frozenset(state.values)
        selected, residual = resolve_lexicographic(values)
        child_rows = build_descendant_occurrences(
            state.index,
            state.values,
            state.representative.provenance,
            selected,
        )
        child_stats.append(
            (
                state.index,
                len(values),
                len(selected),
                len(residual),
                len(child_rows),
            )
        )
        raw_rows.extend(child_rows)
        transition_records.append(
            {
                "parent_class": state.index,
                "values": list(state.values),
                "root_provenance": list(state.representative.provenance),
                "selected": [list(row) for row in selected],
                "residual": sorted(residual),
            }
        )

    child_stats_payload = "".join(
        f"{parent}:{size}:{selected}:{residual}:{outputs}\n"
        for parent, size, selected, residual, outputs in sorted(child_stats)
    )
    if hashlib.sha256(child_stats_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "child_transition_summary"
    ]:
        raise AssertionError("child-transition summary hash mismatch")
    transition_payload = json.dumps(
        transition_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if hashlib.sha256(transition_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "child_transition_family"
    ]:
        raise AssertionError("child-transition family hash mismatch")

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
    occurrence_records = [
        {
            "index": occurrence.index,
            "parent_class": occurrence.parent_class,
            "source": occurrence.source,
            "source_step": occurrence.source_step,
            "exponent": occurrence.exponent,
            "values": list(occurrence.values),
            "provenance": list(occurrence.provenance),
            "immediate_provenance": list(occurrence.immediate_provenance),
        }
        for occurrence in occurrences
    ]
    occurrence_payload = json.dumps(
        occurrence_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if hashlib.sha256(occurrence_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "second_generation_raw_occurrence_family"
    ]:
        raise AssertionError("second-generation occurrence hash mismatch")

    classes = descendant_classes(occurrences)
    class_records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "parent_class": state.representative.parent_class,
            "members": list(state.members),
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
            "immediate_provenance": list(
                state.representative.immediate_provenance
            ),
        }
        for state in classes
    ]
    class_payload = json.dumps(
        class_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if hashlib.sha256(class_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "second_generation_exact_class_family"
    ]:
        raise AssertionError("second-generation class hash mismatch")

    adjacency = descendant_conflict_graph(classes)
    edge_payload = "".join(
        f"{left}->{right}\n"
        for left in sorted(adjacency)
        for right in sorted(adjacency[left])
        if left < right
    )
    if hashlib.sha256(edge_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "second_generation_conflict_graph"
    ]:
        raise AssertionError("second-generation conflict graph mismatch")

    retained_indices: list[int] = []
    component_rows = []
    total_dp_states = 0
    nonunique = 0
    component_family = sorted(
        components(adjacency),
        key=lambda item: (classes[item[0]].representative.exponent, item),
    )
    for component in component_family:
        _weight, count, choice, dp_states = maximum_weight_independent_set_dp(
            component, classes, adjacency
        )
        if count != 1:
            nonunique += 1
        retained_indices.extend(choice)
        total_dp_states += dp_states
        component_rows.append(
            (
                classes[component[0]].representative.exponent,
                component,
                count,
                choice,
                dp_states,
            )
        )
    component_payload = "".join(
        f"{exponent}:{','.join(map(str, component))}:{count}:"
        f"{','.join(map(str, choice))}:{dp_states}\n"
        for exponent, component, count, choice, dp_states in component_rows
    )
    if hashlib.sha256(component_payload.encode("utf-8")).hexdigest() != EXPECTED_HASHES[
        "second_generation_component_certificate"
    ]:
        raise AssertionError("second-generation component hash mismatch")

    retained_indices_tuple = tuple(sorted(retained_indices))
    retained = tuple(classes[index] for index in retained_indices_tuple)
    retained_union = frozenset(
        value for state in retained for value in state.values
    )
    raw_union = frozenset(value for state in classes for value in state.values)
    dropped_union = raw_union - retained_union
    if sum(len(state.values) for state in retained) != len(retained_union):
        raise AssertionError("second-generation retained states overlap")

    retained_index_hash = hashlib.sha256(
        ",".join(map(str, retained_indices_tuple)).encode("utf-8")
    ).hexdigest()
    representative_indices = tuple(
        state.representative.index for state in retained
    )
    representative_hash = hashlib.sha256(
        ",".join(map(str, representative_indices)).encode("utf-8")
    ).hexdigest()
    retained_records = [
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
        for state in retained
    ]
    retained_payload = json.dumps(
        retained_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    observed_retained_hashes = {
        "second_generation_retained_class_indices": retained_index_hash,
        "second_generation_retained_representatives": representative_hash,
        "second_generation_retained_family": hashlib.sha256(
            retained_payload.encode("utf-8")
        ).hexdigest(),
        "second_generation_retained_union": canonical_set_hash(retained_union),
        "second_generation_dropped_union": canonical_set_hash(dropped_union),
    }
    for name, value in observed_retained_hashes.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    first_retained_mass = sum(
        (state.weight for state in retained_first), Fraction()
    )
    second_retained_mass = sum(
        (state.weight for state in retained), Fraction()
    )
    second_raw_union_mass = harmonic(raw_union)
    second_raw_class_mass = sum(
        (state.weight for state in classes), Fraction()
    )
    second_raw_occurrence_mass = sum(
        (harmonic(occurrence.values) for occurrence in occurrences),
        Fraction(),
    )

    provenance_occurrences = []
    provenance_classes: dict[int, set[int]] = defaultdict(set)
    provenance_parents: dict[int, set[int]] = defaultdict(set)
    provenance_points: dict[int, list[tuple[object, ...]]] = defaultdict(list)
    for state in retained:
        representative = state.representative
        for value, provenance in zip(
            state.values, representative.provenance, strict=True
        ):
            provenance_occurrences.append(provenance)
            provenance_classes[provenance].add(state.index)
            provenance_parents[provenance].add(representative.parent_class)
            provenance_points[provenance].append(
                (
                    state.index,
                    value,
                    representative.parent_class,
                    representative.source,
                    representative.source_step,
                )
            )
    provenance_counts = Counter(provenance_occurrences)
    provenance_records = [
        {
            "provenance": provenance,
            "multiplicity": provenance_counts[provenance],
            "descendant_classes": sorted(provenance_classes[provenance]),
            "first_generation_parent_classes": sorted(
                provenance_parents[provenance]
            ),
            "occurrences": [
                list(row) for row in sorted(provenance_points[provenance])
            ],
        }
        for provenance in sorted(provenance_counts)
    ]
    provenance_payload = json.dumps(
        provenance_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    repeated_labels = tuple(
        sorted(
            provenance
            for provenance, multiplicity in provenance_counts.items()
            if multiplicity > 1
        )
    )
    triple_labels = tuple(
        sorted(
            provenance
            for provenance, multiplicity in provenance_counts.items()
            if multiplicity == 3
        )
    )
    cross_parent_labels = tuple(
        sorted(
            provenance
            for provenance, parents in provenance_parents.items()
            if len(parents) > 1
        )
    )
    observed_provenance_hashes = {
        "root_provenance_map": hashlib.sha256(
            provenance_payload.encode("utf-8")
        ).hexdigest(),
        "root_provenance_repeated_labels": set_hash(repeated_labels),
        "root_provenance_triple_labels": set_hash(triple_labels),
        "root_provenance_cross_parent_labels": set_hash(cross_parent_labels),
    }
    for name, value in observed_provenance_hashes.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    provenance_unique_mass = sum(
        (Fraction(1, provenance) for provenance in provenance_counts),
        Fraction(),
    )
    provenance_occurrence_mass = sum(
        (
            Fraction(multiplicity, provenance)
            for provenance, multiplicity in provenance_counts.items()
        ),
        Fraction(),
    )
    provenance_repeat_mass = (
        provenance_occurrence_mass - provenance_unique_mass
    )

    observed = {
        "first_generation_retained_states": len(retained_first),
        "first_generation_retained_labels": sum(
            len(state.values) for state in retained_first
        ),
        "child_transitions_with_selected_actions": sum(
            selected > 0 for _parent, _size, selected, _residual, _outputs in child_stats
        ),
        "child_transitions_with_outputs": sum(
            outputs > 0 for _parent, _size, _selected, _residual, outputs in child_stats
        ),
        "child_selected_actions": sum(
            selected for _parent, _size, selected, _residual, _outputs in child_stats
        ),
        "child_terminal_residual_points": sum(
            residual for _parent, _size, _selected, residual, _outputs in child_stats
        ),
        "second_generation_raw_occurrences": len(occurrences),
        "second_generation_exact_state_classes": len(classes),
        "second_generation_conflict_edges": sum(
            len(targets) for targets in adjacency.values()
        ) // 2,
        "second_generation_conflict_components": len(component_family),
        "second_generation_largest_component": max(
            len(component) for component in component_family
        ),
        "second_generation_dp_states_examined": total_dp_states,
        "second_generation_components_with_nonunique_optimum": nonunique,
        "second_generation_retained_states": len(retained),
        "second_generation_retained_labels": len(retained_union),
        "second_generation_dropped_labels": len(dropped_union),
        "root_provenance_occurrences": len(provenance_occurrences),
        "root_provenance_distinct_labels": len(provenance_counts),
        "root_provenance_repeated_labels": len(repeated_labels),
        "root_provenance_extra_occurrences": (
            len(provenance_occurrences) - len(provenance_counts)
        ),
        "root_provenance_multiplicity_1": sum(
            multiplicity == 1 for multiplicity in provenance_counts.values()
        ),
        "root_provenance_multiplicity_2": sum(
            multiplicity == 2 for multiplicity in provenance_counts.values()
        ),
        "root_provenance_multiplicity_3": sum(
            multiplicity == 3 for multiplicity in provenance_counts.values()
        ),
        "root_provenance_maximum_multiplicity": max(
            provenance_counts.values()
        ),
        "root_provenance_cross_parent_reuse_labels": len(cross_parent_labels),
        "root_provenance_maximum_parent_branches": max(
            len(parents) for parents in provenance_parents.values()
        ),
    }
    if observed != EXPECTED:
        raise AssertionError(f"metric mismatch: {observed!r}")

    observed_mass_hashes = {
        "first_generation_retained": fraction_hash(first_retained_mass),
        "second_generation_retained": fraction_hash(second_retained_mass),
        "second_generation_raw_union": fraction_hash(second_raw_union_mass),
        "second_generation_raw_class": fraction_hash(second_raw_class_mass),
        "second_generation_raw_occurrence": fraction_hash(
            second_raw_occurrence_mass
        ),
        "root_provenance_unique": fraction_hash(provenance_unique_mass),
        "root_provenance_occurrence": fraction_hash(
            provenance_occurrence_mass
        ),
        "root_provenance_repeat": fraction_hash(provenance_repeat_mass),
    }
    if observed_mass_hashes != EXPECTED_MASS_HASHES:
        raise AssertionError("mass hash mismatch")

    ratios = {
        "second_retained_over_first_retained": (
            second_retained_mass / first_retained_mass
        ),
        "second_retained_over_second_raw_union": (
            second_retained_mass / second_raw_union_mass
        ),
        "second_retained_over_second_raw_class": (
            second_retained_mass / second_raw_class_mass
        ),
        "second_retained_over_second_raw_occurrence": (
            second_retained_mass / second_raw_occurrence_mass
        ),
        "second_retained_cardinality_over_raw_union": Fraction(
            len(retained_union), len(raw_union)
        ),
        "provenance_occurrence_over_unique": (
            provenance_occurrence_mass / provenance_unique_mass
        ),
        "provenance_repeat_over_unique": (
            provenance_repeat_mass / provenance_unique_mass
        ),
    }
    for name, value in ratios.items():
        lower, upper, expected_hash = EXPECTED_RATIOS[name]
        if not lower < value < upper:
            raise AssertionError(f"{name} outside compact bracket")
        if fraction_hash(value) != expected_hash:
            raise AssertionError(f"{name} hash mismatch")

    lines = [
        "SECOND-GENERATION PROVENANCE REUSE",
        "",
        "first_generation_policy=local37",
        (
            "first_generation_retention=exact_duplicate_quotient_plus_"
            "maximum_harmonic_conflict_selection"
        ),
        "child_transition_policy=lexicographic_coordinated_deletion",
        (
            "second_generation_retention=same_global_exact_duplicate_"
            "and_conflict_rule"
        ),
        "",
        "first_generation_retained_states=21",
        "first_generation_retained_labels=11753",
        (
            "first_generation_retained_family_sha256="
            f"{EXPECTED_HASHES['first_generation_retained_family']}"
        ),
        "child_transitions_with_selected_actions=15",
        "child_transitions_with_outputs=19",
        "child_selected_actions=10426",
        "child_terminal_residual_points=1327",
        (
            "child_transition_summary_sha256="
            f"{EXPECTED_HASHES['child_transition_summary']}"
        ),
        (
            "child_transition_family_sha256="
            f"{EXPECTED_HASHES['child_transition_family']}"
        ),
        "",
        "second_generation_raw_occurrences=442",
        "second_generation_exact_state_classes=173",
        "second_generation_conflict_edges=1046",
        "second_generation_conflict_components=22",
        "second_generation_largest_component=21",
        "second_generation_dp_states_examined=204",
        "second_generation_components_with_nonunique_optimum=0",
        (
            "second_generation_raw_occurrence_family_sha256="
            f"{EXPECTED_HASHES['second_generation_raw_occurrence_family']}"
        ),
        (
            "second_generation_exact_class_family_sha256="
            f"{EXPECTED_HASHES['second_generation_exact_class_family']}"
        ),
        (
            "second_generation_conflict_graph_sha256="
            f"{EXPECTED_HASHES['second_generation_conflict_graph']}"
        ),
        (
            "second_generation_component_certificate_sha256="
            f"{EXPECTED_HASHES['second_generation_component_certificate']}"
        ),
        "",
        "second_generation_retained_states=27",
        "second_generation_retained_labels=7925",
        "second_generation_dropped_labels=5900",
        "second_generation_point_disjoint=True",
        "second_generation_root_provenance_assigned=True",
        (
            "second_generation_retained_class_indices_sha256="
            f"{EXPECTED_HASHES['second_generation_retained_class_indices']}"
        ),
        (
            "second_generation_retained_representatives_sha256="
            f"{EXPECTED_HASHES['second_generation_retained_representatives']}"
        ),
        (
            "second_generation_retained_family_sha256="
            f"{EXPECTED_HASHES['second_generation_retained_family']}"
        ),
        (
            "second_generation_retained_union_sha256="
            f"{EXPECTED_HASHES['second_generation_retained_union']}"
        ),
        (
            "second_generation_dropped_union_sha256="
            f"{EXPECTED_HASHES['second_generation_dropped_union']}"
        ),
        "",
        (
            "first_generation_retained_mass_sha256="
            f"{EXPECTED_MASS_HASHES['first_generation_retained']}"
        ),
        (
            "second_generation_retained_mass_sha256="
            f"{EXPECTED_MASS_HASHES['second_generation_retained']}"
        ),
        (
            "second_generation_raw_union_mass_sha256="
            f"{EXPECTED_MASS_HASHES['second_generation_raw_union']}"
        ),
        (
            "second_generation_raw_class_mass_sha256="
            f"{EXPECTED_MASS_HASHES['second_generation_raw_class']}"
        ),
        (
            "second_generation_raw_occurrence_mass_sha256="
            f"{EXPECTED_MASS_HASHES['second_generation_raw_occurrence']}"
        ),
        "second_over_first_retained_mass_bracket=6828/1000,6829/1000",
        (
            "second_over_first_retained_mass_sha256="
            f"{EXPECTED_RATIOS['second_retained_over_first_retained'][2]}"
        ),
        "second_retained_over_raw_union_mass_bracket=896/1000,897/1000",
        (
            "second_retained_over_raw_union_mass_sha256="
            f"{EXPECTED_RATIOS['second_retained_over_second_raw_union'][2]}"
        ),
        (
            "second_retained_over_raw_exact_class_mass_bracket="
            "639/1000,640/1000"
        ),
        (
            "second_retained_over_raw_exact_class_mass_sha256="
            f"{EXPECTED_RATIOS['second_retained_over_second_raw_class'][2]}"
        ),
        (
            "second_retained_over_raw_occurrence_mass_bracket="
            "206/1000,207/1000"
        ),
        (
            "second_retained_over_raw_occurrence_mass_sha256="
            f"{EXPECTED_RATIOS['second_retained_over_second_raw_occurrence'][2]}"
        ),
        (
            "second_retained_over_raw_union_cardinality_bracket="
            "573/1000,574/1000"
        ),
        (
            "second_retained_over_raw_union_cardinality_sha256="
            f"{EXPECTED_RATIOS['second_retained_cardinality_over_raw_union'][2]}"
        ),
        "",
        "root_provenance_occurrences=7925",
        "root_provenance_distinct_labels=7648",
        "root_provenance_repeated_labels=272",
        "root_provenance_extra_occurrences=277",
        "root_provenance_multiplicity_1=7376",
        "root_provenance_multiplicity_2=267",
        "root_provenance_multiplicity_3=5",
        "root_provenance_maximum_multiplicity=3",
        "root_provenance_cross_parent_reuse_labels=265",
        "root_provenance_maximum_parent_branches=2",
        (
            "root_provenance_map_sha256="
            f"{EXPECTED_HASHES['root_provenance_map']}"
        ),
        (
            "root_provenance_repeated_labels_sha256="
            f"{EXPECTED_HASHES['root_provenance_repeated_labels']}"
        ),
        (
            "root_provenance_triple_labels_sha256="
            f"{EXPECTED_HASHES['root_provenance_triple_labels']}"
        ),
        (
            "root_provenance_cross_parent_labels_sha256="
            f"{EXPECTED_HASHES['root_provenance_cross_parent_labels']}"
        ),
        (
            "root_provenance_unique_mass_sha256="
            f"{EXPECTED_MASS_HASHES['root_provenance_unique']}"
        ),
        (
            "root_provenance_occurrence_mass_sha256="
            f"{EXPECTED_MASS_HASHES['root_provenance_occurrence']}"
        ),
        (
            "root_provenance_repeat_mass_sha256="
            f"{EXPECTED_MASS_HASHES['root_provenance_repeat']}"
        ),
        (
            "root_provenance_occurrence_over_unique_mass_bracket="
            "1040/1000,1041/1000"
        ),
        (
            "root_provenance_occurrence_over_unique_mass_sha256="
            f"{EXPECTED_RATIOS['provenance_occurrence_over_unique'][2]}"
        ),
        (
            "root_provenance_repeat_over_unique_mass_bracket="
            "40/1000,41/1000"
        ),
        (
            "root_provenance_repeat_over_unique_mass_sha256="
            f"{EXPECTED_RATIOS['provenance_repeat_over_unique'][2]}"
        ),
        "",
        (
            "conclusion: propagating the 21 retained states through "
            "lexicographic coordinated deletion and"
        ),
        (
            "reapplying the global provenance quotient produces a unique "
            "27-state point-disjoint descendant family."
        ),
        (
            "Original S7 provenance reuse has maximum multiplicity three and "
            "harmonic overhead between 4.0% and 4.1%,"
        ),
        (
            "but retained harmonic mass expands by a factor between 6.828 "
            "and 6.829."
        ),
        (
            "Thus bounded one-step provenance multiplicity alone is not a "
            "Bellman contraction coordinate."
        ),
        (
            "Cross-generation scale, obstruction, and repeated-provenance "
            "capacity must be coupled."
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
            "usage: verify_retained_provenance_second_generation.py [OUTPUT]"
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
