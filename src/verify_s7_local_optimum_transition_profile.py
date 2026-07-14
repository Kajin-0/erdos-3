#!/usr/bin/env python3
"""Compare raw S7 transition structure for three exact policies."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from export_simultaneous_deletion_transition import (
    canonical_set_hash,
    partial_overlaps,
    resolve_schedule as resolve_lexicographic,
    schedule_hash,
    verify_schedule,
)
from verify_s1_deletion_dag_adapter import (
    SelectedProgression,
    build_shell_occurrences,
    duplicate_groups,
    harmonic,
    middle_resolution,
    strict_containments,
)
from verify_s7_policy_transition_tradeoff import strongly_connected_components
from verify_s7_regenerative_seed_policy_dependence import all_three_aps
from verify_s7_terminal_step_local_optimum import (
    DELAYED_STEPS,
    SEED_5_142,
    resolve_policy,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

COUNT_KEYS = (
    "selected",
    "residual",
    "terminal_steps",
    "fiber_occurrences",
    "fiber_union",
    "imported_union",
    "novel_union",
    "shell_occurrences",
    "state_classes",
    "duplicate_groups",
    "containments",
    "partial_overlaps",
    "recursive_union",
    "maximum_multiplicity",
    "terminal_recursive_overlap",
    "incidence_edges",
    "scc_count",
    "cyclic_scc_count",
    "largest_scc",
)
HASH_KEYS = (
    "counts_hash",
    "schedule_hash",
    "residual_hash",
    "terminal_hash",
    "recursive_union_hash",
    "occurrence_family_hash",
    "duplicate_groups_hash",
    "containments_hash",
    "partial_overlaps_hash",
    "edge_hash",
    "largest_scc_hash",
)
MASS_KEYS = (
    ("terminal_mass", "terminal_mass"),
    ("middle_occurrence_mass", "middle_occurrence_mass"),
    ("middle_union_mass", "middle_union_mass"),
    ("duplicate_mass", "duplicate_mass"),
    ("average_multiplicity", "average_multiplicity"),
    ("recursive_occurrence_mass", "recursive_occurrence_mass"),
    ("recursive_union_mass", "recursive_union_mass"),
)

EXPECTED = {
    "lex": {
        "selected": 9_360,
        "residual": 480,
        "terminal_steps": 25,
        "fiber_occurrences": 9_335,
        "fiber_union": 6_683,
        "imported_union": 312,
        "novel_union": 6_371,
        "shell_occurrences": 127,
        "state_classes": 95,
        "duplicate_groups": 20,
        "containments": 345,
        "partial_overlaps": 214,
        "recursive_union": 16_210,
        "maximum_multiplicity": 16,
        "terminal_recursive_overlap": 10,
        "incidence_edges": 75,
        "scc_count": 19,
        "cyclic_scc_count": 1,
        "largest_scc": 7,
        "counts_hash": "d1d7c93f8551bb936ea7412edacfffbe61163e77a25ca8cc7ef2b9fd6342b4d3",
        "schedule_hash": "12a369aa926f3ceac00943e8a383a9f635ec9f16b33565ec29f90c2d3d1d8ac1",
        "residual_hash": "b4517f0c67753b3297549dc7acc52818a85cb1df9261ce1a30cb78ec8d129a33",
        "terminal_hash": "6ecab6a471d01b79ece12b53056794475b459a4b19272e43a4342d4c9f787db5",
        "recursive_union_hash": "1fda4d9f611c935b1eb4892fb0c0d599eb32723e6c6e6f5248707a2169164bd2",
        "occurrence_family_hash": "af8b9d3104050c2f565925c87cc95d7c4d1ab8cc396fff98d67b3425ce420c73",
        "duplicate_groups_hash": "dd1b2aee270ed1e5d6763b80505aab7284e9224d86dd1f4f665bdd32b8491c70",
        "containments_hash": "4aab3dc9aadcd79d9a722820476bfb8ef3b5a53cbea7d3908ee7227ca54ee199",
        "partial_overlaps_hash": "a5f502b5bee1634950248feb814ad165bd96cde353e74dce67393146f89fd9de",
        "edge_hash": "f34eb463b3929166945e9db93878774e4b5ca2c241793c4c004aae597ed84bf1",
        "largest_scc_hash": "cb78b3ba8da7507643570284d8b1278aa65833a7343bf209c99626ee1a894786",
        "terminal_mass_hash": "ef3142242664f73530a522264392acd65e856b412e14600361eaa86693437bc9",
        "middle_occurrence_mass_hash": "a84004ce0681ad1bf307ce2b9bffa9194a2b542529cd631fe1b0244236161480",
        "middle_union_mass_hash": "3cc8b5a12dee4d0a7250bba894f6abd86e2ae3f5f65f0e94be35a85364690594",
        "duplicate_mass_hash": "e97c81f29f389c5c269d4eaf97bda5492ee14fe1f8451c3e159eeeb18f969b91",
        "average_multiplicity_hash": "59384bade89a2fb6acbe3150aaf2bc1ea3f5af356fd66c777d94a5339a9457dd",
        "recursive_occurrence_mass_hash": "3f01decaf3f24e15cd2c06aed25e67f30d68d471fd2215c6d46868a553d209f2",
        "recursive_union_mass_hash": "a0287dbf7335ea2e6bb3d0a19f74219c1dfeac7820a27da6fff13528c85cf753",
    },
    "seed_5_142": {
        "selected": 9_347,
        "residual": 493,
        "terminal_steps": 50,
        "fiber_occurrences": 9_297,
        "fiber_union": 6_169,
        "imported_union": 305,
        "novel_union": 5_864,
        "shell_occurrences": 227,
        "state_classes": 144,
        "duplicate_groups": 45,
        "containments": 1_028,
        "partial_overlaps": 1_180,
        "recursive_union": 15_703,
        "maximum_multiplicity": 34,
        "terminal_recursive_overlap": 12,
        "incidence_edges": 141,
        "scc_count": 49,
        "cyclic_scc_count": 1,
        "largest_scc": 2,
        "counts_hash": "f7921938d52e9836a167c06bd72f2348c6b7865bad34900ab4f3fb302d2cfe43",
        "schedule_hash": "8f57e8dc76d5aaf21ffe3f3a6c38285872abbab1dbe6c17282538a8c9c16c851",
        "residual_hash": "e8b39fe1d14a69c365c7b27d1c18a734385f37c243fd8dcf3294ab3fd843c948",
        "terminal_hash": "9bd82f8ddcfd31747cb606f92b5e4f18acba4a3f9cd81a5281234ffecc18fa9e",
        "recursive_union_hash": "a04810ed30688625e8018770dfedf3504ebbb9af65a0dd48d367e025fc73ff8f",
        "occurrence_family_hash": "4318b7aca388ea6a60514868fc2ae353c935cf4d8e1b3508132f726dc9ca41b4",
        "duplicate_groups_hash": "17a25b746d6e74daebd4820c8a491cdfcd75d1204a22029ba67269eabb6fd34c",
        "containments_hash": "62657110d5aea938ce4e39ecbf5a492ea5486f8dd176440b1030ccd3457d8c86",
        "partial_overlaps_hash": "4b502da103aef672271d108b5c60d5eb79ba4e9e22fcc733367fc77bc66476fd",
        "edge_hash": "0ddfa39842deaebd73b51772651bc66a4008d2d7cfc82a74c5acdfaec6188079",
        "largest_scc_hash": "dc4263117417fa9bf50183ec65cac8b5c7d32fc7fc84e40b118a41ace61c3b50",
        "terminal_mass_hash": "35da913066b9bafd4496f57528781b57384989eeb2d2f1f4855320c54d8831a6",
        "middle_occurrence_mass_hash": "a8ed8fe436bc596559bf0ff41e5a590a03122eae5f2d8f301151fbc383a22f21",
        "middle_union_mass_hash": "ab950196bcf00151ecf473f2471a5f3d95bb9e1b9c4200de67a44e6b5081764e",
        "duplicate_mass_hash": "5bfb1a06a98a2fb29fd36db6c71fd91e1fd0d630c935fb74fc158bd3c06ab358",
        "average_multiplicity_hash": "f92a4ce2b4364fd7c17bf64110eb97549fb5b2ff6feba4ca6e3adf20a9217433",
        "recursive_occurrence_mass_hash": "2bfcdee1fda1cc869d50df1cdeec04e02bbc2468ed06ede01921b3726bb95f12",
        "recursive_union_mass_hash": "62262d27045665e11e8c36052cac1d60186a8c2d1a0f4854971a7e524e03bcf0",
    },
    "local37": {
        "selected": 9_323,
        "residual": 517,
        "terminal_steps": 28,
        "fiber_occurrences": 9_295,
        "fiber_union": 7_278,
        "imported_union": 346,
        "novel_union": 6_932,
        "shell_occurrences": 131,
        "state_classes": 87,
        "duplicate_groups": 22,
        "containments": 229,
        "partial_overlaps": 390,
        "recursive_union": 16_771,
        "maximum_multiplicity": 18,
        "terminal_recursive_overlap": 8,
        "incidence_edges": 83,
        "scc_count": 28,
        "cyclic_scc_count": 0,
        "largest_scc": 1,
        "counts_hash": "638c9e480d04e941fe3bc4be77670a029f838c0e76a034519e5d6021a09c99cd",
        "schedule_hash": "2a4df51cdf4c33263ff09fee2b39f3bd0e74277de2d6d2fa2904752ae14f2267",
        "residual_hash": "c22896814dcec5e644db1c77dbab257faba4dd61742226b02ae89c06bdba0b7d",
        "terminal_hash": "a00f1eae48ed0bb18fdf7f4ba33c9e1a70fc5a827385b8113304eb57dd1e0501",
        "recursive_union_hash": "de9e23fb35ad521cec6dc9b89b5701746f381e9ea603a04edd15c828969021c9",
        "occurrence_family_hash": "3a7c73fcc59f7a57aa57f113c8ce46b94a4ba3141e2cfb79ef13ac66377a6ac6",
        "duplicate_groups_hash": "2f6e039d46d9c254b0499f0f498b9469b7043d47877edc3d90cf3e0955e57100",
        "containments_hash": "bd66936fb020deb4077b69a91024179b9908f081887247d2409cc269a7e434b3",
        "partial_overlaps_hash": "e5c750fc36983fffd591fd32da761f6b47bef1f915bced44c6bbfffb9f3c7211",
        "edge_hash": "e0bca0f91a4b101f4773f589935f9da934f3ffbb4db24130fa4fe8fcdc201d38",
        "largest_scc_hash": "ae4a4bec511679258c335f39896e42e847c77893872e8653edb32ea125328dc4",
        "terminal_mass_hash": "500f670a644078e5a5343b6575576202c4ad2754d833634f5a75ad8ead55cce9",
        "middle_occurrence_mass_hash": "0fb178165e31b923167454e38fa144f83e35819e3af2277d521195eeb7ed4850",
        "middle_union_mass_hash": "d40835db1c0994b801aef60c0f148c2684b8bb8d52e2bbd335a560402003ce3c",
        "duplicate_mass_hash": "98e8427e32b6cca8b336a9c3036e507571c31619f2b28a4a51708beb7a939ac0",
        "average_multiplicity_hash": "74d14b601d9fdc173c4ea37085562d2ffb1098908d62735bcee9d35e9b7b3a53",
        "recursive_occurrence_mass_hash": "afcbddf8690fad4239ac33a6412649f2aa90d87188f7ec4b84724457b521a880",
        "recursive_union_mass_hash": "1ae8ae9c2b1e46f73760c731701d24550999513c77780ed86df718b67994acf0",
    },
}

RATIO_EXPECTED = {
    "local_over_lex_middle_occurrence_mass": (
        Fraction(247, 1_000),
        Fraction(248, 1_000),
        "3bea9faaab936801f25953b3038d3825eccbfdc27187b5a60fb167c55d80a2a1",
    ),
    "local_over_seed_middle_occurrence_mass": (
        Fraction(513, 1_000),
        Fraction(514, 1_000),
        "d05b955c4096aea63bf98b1a7884651fc7e9f34cecf6dd0d897d67f03c580ad3",
    ),
    "local_over_lex_recursive_occurrence_mass": (
        Fraction(254, 1_000),
        Fraction(255, 1_000),
        "daa2feadc0925edb810977df8fec6745fd37e7b01bf6dcc957e29da1034e31fc",
    ),
    "local_over_seed_recursive_occurrence_mass": (
        Fraction(522, 1_000),
        Fraction(523, 1_000),
        "cb184ecea3ad19807bdd8b5022bf4509eae4f85f6082f63d9f534fdbc1b6af7c",
    ),
}
CERTIFICATE_SHA256 = (
    "1bf8d15efd7c8cb1f9b04fba769d19e43d2b630d9fe36f141bbcc4466f9bb19e"
)


def fraction_hash(value: Fraction) -> str:
    payload = f"{value.numerator}/{value.denominator}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def edge_hash(edges: Iterable[tuple[int, int]]) -> str:
    payload = "".join(
        f"{source}->{target}\n"
        for source, target in sorted(set(edges))
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def convert_selected(
    rows: tuple[tuple[int, ...], ...],
) -> tuple[SelectedProgression, ...]:
    return tuple(
        SelectedProgression(
            time=index,
            sponsor=row[0],
            middle=row[1],
            opposite=row[2],
            step=row[3],
            left=row[4],
            right=row[5],
        )
        for index, row in enumerate(rows, start=1)
    )


def resolve_named_policy(
    name: str,
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
) -> tuple[tuple[SelectedProgression, ...], frozenset[int]]:
    if name == "lex":
        return resolve_lexicographic(parent)
    delayed = SEED_5_142 if name == "seed_5_142" else DELAYED_STEPS
    rows, residual = resolve_policy(parent, progressions, delayed)
    return convert_selected(rows), residual


def build_profile(
    name: str,
    parent: frozenset[int],
    progressions: list[tuple[int, int, int, int]],
) -> dict[str, object]:
    selected, residual = resolve_named_policy(name, parent, progressions)
    verify_schedule(parent, selected, residual)
    terminal_steps, fibers, _terminal_sponsor, fiber_provenance = (
        middle_resolution(selected)
    )
    occurrences = build_shell_occurrences(parent, fibers, fiber_provenance)
    duplicates = duplicate_groups(occurrences)
    containments = tuple(sorted(strict_containments(occurrences)))
    partial = tuple(partial_overlaps(occurrences))

    exact_classes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for occurrence in occurrences:
        exact_classes[occurrence.values].append(occurrence.index)

    minimum = min(parent)
    backbone = frozenset(
        value - minimum for value in parent if value > minimum
    )
    middle_values = [
        value for fiber in fibers.values() for value in fiber
    ]
    middle_union = frozenset(middle_values)
    imported = middle_union & backbone
    novel = middle_union - backbone
    recursive_union = frozenset(
        value for occurrence in occurrences for value in occurrence.values
    )
    multiplicity = Counter(
        value for occurrence in occurrences for value in occurrence.values
    )

    edges = {
        (step, value)
        for step, values in fibers.items()
        for value in values
        if value in terminal_steps
    }
    components = strongly_connected_components(set(terminal_steps), edges)
    cyclic = tuple(
        component
        for component in components
        if len(component) > 1 or (component[0], component[0]) in edges
    )
    largest = max(components, key=lambda component: (len(component), component))

    terminal_mass = harmonic(terminal_steps)
    middle_occurrence_mass = sum(
        (harmonic(values) for values in fibers.values()),
        Fraction(),
    )
    middle_union_mass = harmonic(middle_union)
    duplicate_mass = middle_occurrence_mass - middle_union_mass
    average_multiplicity = middle_occurrence_mass / middle_union_mass
    recursive_occurrence_mass = sum(
        (harmonic(occurrence.values) for occurrence in occurrences),
        Fraction(),
    )
    recursive_union_mass = harmonic(recursive_union)

    counts = {
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(terminal_steps),
        "fiber_occurrences": len(middle_values),
        "fiber_union": len(middle_union),
        "imported_union": len(imported),
        "novel_union": len(novel),
        "shell_occurrences": len(occurrences),
        "state_classes": len(exact_classes),
        "duplicate_groups": len(duplicates),
        "containments": len(containments),
        "partial_overlaps": len(partial),
        "recursive_union": len(recursive_union),
        "maximum_multiplicity": max(multiplicity.values()),
        "terminal_recursive_overlap": len(
            set(terminal_steps) & set(recursive_union)
        ),
        "incidence_edges": len(edges),
        "scc_count": len(components),
        "cyclic_scc_count": len(cyclic),
        "largest_scc": len(largest),
    }
    counts_payload = json.dumps(
        counts, sort_keys=True, separators=(",", ":")
    ) + "\n"

    occurrence_records = [
        {
            "source": occurrence.source,
            "source_step": occurrence.source_step,
            "exponent": occurrence.exponent,
            "values": list(occurrence.values),
            "provenance": list(occurrence.provenance),
        }
        for occurrence in occurrences
    ]
    occurrence_payload = json.dumps(
        occurrence_records, sort_keys=True, separators=(",", ":")
    ) + "\n"
    duplicate_payload = json.dumps(
        duplicates, separators=(",", ":")
    ) + "\n"
    containment_payload = "".join(
        f"{inner}->{outer}\n" for inner, outer in containments
    )
    partial_payload = "".join(
        f"{left},{right}:{','.join(map(str, values))}\n"
        for left, right, values in partial
    )

    return {
        **counts,
        "counts_hash": hashlib.sha256(
            counts_payload.encode("utf-8")
        ).hexdigest(),
        "schedule_hash": schedule_hash(selected, residual),
        "residual_hash": canonical_set_hash(residual),
        "terminal_hash": canonical_set_hash(terminal_steps),
        "recursive_union_hash": canonical_set_hash(recursive_union),
        "occurrence_family_hash": hashlib.sha256(
            occurrence_payload.encode("utf-8")
        ).hexdigest(),
        "duplicate_groups_hash": hashlib.sha256(
            duplicate_payload.encode("utf-8")
        ).hexdigest(),
        "containments_hash": hashlib.sha256(
            containment_payload.encode("utf-8")
        ).hexdigest(),
        "partial_overlaps_hash": hashlib.sha256(
            partial_payload.encode("utf-8")
        ).hexdigest(),
        "edge_hash": edge_hash(edges),
        "largest_scc_hash": canonical_set_hash(largest),
        "terminal_mass": terminal_mass,
        "middle_occurrence_mass": middle_occurrence_mass,
        "middle_union_mass": middle_union_mass,
        "duplicate_mass": duplicate_mass,
        "average_multiplicity": average_multiplicity,
        "recursive_occurrence_mass": recursive_occurrence_mass,
        "recursive_union_mass": recursive_union_mass,
    }


def build_certificate() -> str:
    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    if len(progressions) != 298_606:
        raise AssertionError("initial progression count mismatch")

    profiles = {
        name: build_profile(name, parent, progressions)
        for name in ("lex", "seed_5_142", "local37")
    }

    for name, expected in EXPECTED.items():
        profile = profiles[name]
        for key in COUNT_KEYS + HASH_KEYS:
            if profile[key] != expected[key]:
                raise AssertionError(
                    f"{name} {key} mismatch: {profile[key]!r}"
                )
        for label, key in MASS_KEYS:
            observed_hash = fraction_hash(profile[key])
            if observed_hash != expected[f"{label}_hash"]:
                raise AssertionError(f"{name} {label} hash mismatch")

    local = profiles["local37"]
    lex = profiles["lex"]
    seed = profiles["seed_5_142"]
    ratios = {
        "local_over_lex_middle_occurrence_mass": (
            local["middle_occurrence_mass"] / lex["middle_occurrence_mass"]
        ),
        "local_over_seed_middle_occurrence_mass": (
            local["middle_occurrence_mass"] / seed["middle_occurrence_mass"]
        ),
        "local_over_lex_recursive_occurrence_mass": (
            local["recursive_occurrence_mass"] / lex["recursive_occurrence_mass"]
        ),
        "local_over_seed_recursive_occurrence_mass": (
            local["recursive_occurrence_mass"] / seed["recursive_occurrence_mass"]
        ),
    }
    for name, value in ratios.items():
        lower, upper, expected_hash = RATIO_EXPECTED[name]
        if not lower < value < upper:
            raise AssertionError(f"{name} outside compact bracket")
        if fraction_hash(value) != expected_hash:
            raise AssertionError(f"{name} hash mismatch")

    if local["cyclic_scc_count"] != 0:
        raise AssertionError("local policy retains a cyclic terminal-fiber SCC")
    if not (
        local["partial_overlaps"] > lex["partial_overlaps"]
        and local["maximum_multiplicity"] > lex["maximum_multiplicity"]
    ):
        raise AssertionError("mixed overlap tradeoff was not reproduced")

    lines = [
        "S7 LOCAL-OPTIMUM RAW TRANSITION PROFILE",
        "",
        "policies=lex,seed_5_142,local37",
        "local_score=lambda:3,gamma:1/10",
        "",
    ]
    for name in ("lex", "seed_5_142", "local37"):
        profile = profiles[name]
        expected = EXPECTED[name]
        lines.append(f"[{name}]")
        for key in COUNT_KEYS:
            lines.append(f"{key}={profile[key]}")
        for key in HASH_KEYS:
            lines.append(f"{key}={profile[key]}")
        for label, _key in MASS_KEYS:
            lines.append(
                f"{label}_sha256={expected[f'{label}_hash']}"
            )
        lines.append("")

    for name in (
        "local_over_lex_middle_occurrence_mass",
        "local_over_seed_middle_occurrence_mass",
        "local_over_lex_recursive_occurrence_mass",
        "local_over_seed_recursive_occurrence_mass",
    ):
        lower, upper, expected_hash = RATIO_EXPECTED[name]
        lines.append(
            f"{name}_bracket={lower.numerator}/{lower.denominator},"
            f"{upper.numerator}/{upper.denominator}"
        )
        lines.append(f"{name}_sha256={expected_hash}")

    lines.extend(
        [
            "",
            (
                "conclusion: the exact local-optimum policy eliminates "
                "terminal-fiber cycles and sharply lowers harmonic occurrence load"
            ),
            (
                "relative to both reference policies, but it does not produce "
                "a disjoint raw family."
            ),
            (
                "Compared with lexicographic deletion, partial overlaps rise "
                "from 214 to 390 and maximum point multiplicity rises from 16 to 18."
            ),
            (
                "A provenance-preserving retention quotient remains necessary "
                "before any raw occurrence family can enter a Bellman child sum."
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
        raise SystemExit(
            "usage: verify_s7_local_optimum_transition_profile.py [OUTPUT]"
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
