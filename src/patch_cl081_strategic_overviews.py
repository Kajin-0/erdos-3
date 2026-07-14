#!/usr/bin/env python3
"""Bring strategic overview documents to the CL-081 frontier."""
from __future__ import annotations

from pathlib import Path

README = Path("README.md")
LANDSCAPE = Path("docs/comprehensive-research-landscape.md")
LP = Path("docs/branching-reserve-lp.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise AssertionError(f"missing patch anchor: {label}")
    return text.replace(old, new, 1)


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "11. a policy-aware exact rational LP over a full five-step subset lattice through `S_7`.",
        """11. a policy-aware exact rational LP over a full five-step subset lattice through `S_7`;
12. a rigorous point-disjoint retained quotient propagated through five levels;
13. an exact unique-root lineage identity at the first failing retained transition;
14. an exact backbone-only survivor classification and minimum-anchor transfer decomposition.""",
        "README status list",
    )
    old = r"""## Active theorem

The decisive missing object is a provenance-preserving retention quotient converting raw overlapping simultaneous outputs into legitimate Bellman children.

The intended whole-tree inequality is schematically

```math
\Delta(S)
+
\sum_{S'\in\mathrm{Child}_\pi(S)}
\left(
\mathrm{Pack}(S')+\Phi_{\rm obs}(S')
\right)
\le
\mathrm{Pack}(S)+\Phi_{\rm obs}(S)
+
\mathrm{controlled\ error}.
```

A valid theorem must handle:

- duplicate states;
- strict containments;
- partial overlaps;
- terminal-recursive overlap;
- cyclic terminal-fiber incidence;
- policy-dependent regeneration;
- cross-generation provenance reuse.

Pathwise summability, replay catalogs, and policy-ranking LP feasibility do not by themselves imply this treewise inequality.
"""
    new = r"""## Active theorem

A rigorous finite retained quotient now exists for the recorded adversarial construction. It has been propagated through five retained levels and produces point-disjoint recursive and terminal families. It is a certified finite test object, not a globally canonical or optimal quotient.

At the first failing transition all `1015` recursive survivors are minimum-translation backbone points. For a parent state `S`, `m=min(S)`, their gain is drawn from harmonic intervals

```math
(u-m,u],
\qquad
\mu_H((u-m,u])
=
\frac1{u-m}-\frac1u.
```

The decisive missing theorem is now a cumulative provenance-preserving transfer law controlling reuse of these anchor-survivor intervals across the whole retained tree. The intended inequality is schematically

```math
H_{g+1}^{\rm rec}
+
A_{g+1}
+
T_{g+1}^{\rm first}
\le
H_g^{\rm rec}
+
A_g
+
\Phi_{\rm obs,g}
+
\varepsilon_g,
```

where `A_g` is state-independent ancestor-path capacity, terminal mass is charged once, obstruction credit records completion/rectangle/extension exclusion, and `sum_g epsilon_g` is finite.

A valid theorem must still handle policy dependence, terminal-recursive interaction, bounded cross-generation provenance reuse, and the distinction between numerical coverage and provenance-valid payment. Pathwise summability and finite LP feasibility do not imply this treewise inequality.
"""
    text = replace_once(text, old, new, "README active theorem")
    old_ref = "- [`docs/branching-reserve-lp.md`](docs/branching-reserve-lp.md) — exact retained-child LP contract and current packing requirements."
    new_ref = "- [`docs/backbone-anchor-root-transfer.md`](docs/backbone-anchor-root-transfer.md) — exact backbone-only survivor and minimum-anchor transfer theorem.\n" + old_ref
    if new_ref not in text:
        text = replace_once(text, old_ref, new_ref, "README start references")
    README.write_text(text, encoding="utf-8")


def patch_landscape() -> None:
    text = LANDSCAPE.read_text(encoding="utf-8")
    text = text.replace("through claim `CL-065`", "through claim `CL-081`", 1)

    text = replace_once(
        text,
        "The current objective is a policy-aware retained-child inequality of the schematic form",
        """A rigorous finite retained quotient has now been propagated through five levels of the recorded adversarial construction. The quotient is point-disjoint and exact, but it is not proved globally canonical or optimal.

The current objective is a policy-aware retained-child inequality of the schematic form""",
        "landscape executive retained quotient",
    )
    text = text.replace(
        "The decisive missing object is a **provenance-preserving retention quotient** converting raw overlapping simultaneous output into legitimate Bellman children.",
        "The decisive missing object is now a **state-independent cumulative root-lineage transfer law** controlling how provenance-labeled anchor-survivor intervals are created, reused, terminalized, discarded, or converted into arithmetic obstruction. The finite quotient supplies legitimate test rows but not the whole-tree theorem.",
        1,
    )
    text = text.replace(
        "| Retained-child packing | open | decisive missing theorem |",
        "| Retained-child packing | finite point-disjoint quotient through generation five; global theorem open | cumulative ancestor-path transfer and bounded reuse remain missing |",
        1,
    )
    text = text.replace(
        "Earlier models remain benchmarks, counterexamples, or infrastructure. The active route is retained-child packing.",
        "Earlier models remain benchmarks, counterexamples, or infrastructure. The active route is retained-child packing plus cumulative backbone-anchor interval transfer.",
        1,
    )

    old_heading = """## 8.5 The retention theorem comes before the final LP

The exact LP harness accepts only legitimate retained-child rows. A valid retention contract must specify:"""
    new_heading = """## 8.5 Finite retention exists; the global transfer theorem comes before the final LP

The recorded construction now has legitimate point-disjoint retained families through generation five. This proves that the overlap problem can be resolved on the finite adversarial frontier. It does not prove that maximum-harmonic retention is globally canonical, optimal, or compatible with a telescoping whole-tree potential.

The exact LP harness accepts only mathematically legitimate retained-child rows. A global retention and transfer contract must specify:"""
    text = replace_once(text, old_heading, new_heading, "landscape retention section")
    text = text.replace(
        "Without this contract, an exactly feasible LP can encode the wrong inequality.",
        "Without this global contract and a bounded-reuse law, an exactly feasible LP can encode the wrong inequality even though the recorded finite retained rows are legitimate.",
        1,
    )

    text = text.replace(
        "### I.1 Provenance-preserving retention quotient\n\nDefine a canonical or policy-dependent map from raw simultaneous output to retained children and prove:",
        "### I.1 State-independent retention and ancestor-transfer contract\n\nGeneralize the certified finite retained quotient and define a cumulative anchor/root-lineage state. Prove:",
        1,
    )
    text = text.replace(
        "- preservation of required provenance;\n- prevention of repeated payment.",
        "- preservation of required provenance;\n- prevention of repeated payment;\n- bounded reuse or obstruction export for anchor-survivor intervals.",
        1,
    )
    text = text.replace(
        "### I.2 First legitimate retained-child Bellman row\n\nConstruct one exact row, beginning with `S_1` or `S_2`, from the proved retention quotient. The children must come from mathematics, not from a fitted surrogate.",
        "### I.2 First state-independent transfer row\n\nThe recorded construction already supplies exact finite retained rows. The next target is one symbolic row whose ancestor-path capacity and release terms are defined independently of the recorded generation and whose children come from the proved retention semantics.",
        1,
    )

    text = text.replace(
        "Provenance-preserving retention quotient          [OPEN]\n    |\nLegitimate retained-child Bellman rows            [OPEN]",
        "Finite point-disjoint retained quotient          [DONE ON RECORDED FRONTIER]\n    |\nGlobal retention / anchor-interval transfer       [OPEN]\n    |\nState-independent retained-child Bellman rows     [OPEN]",
        1,
    )

    old_program = """1. **Freeze state-specific `S_10` work.** Reopen it only to test a general reserve recurrence.
2. **Define retention on `S_1` and `S_2`.** Specify support ownership, provenance ownership, duplicate merging, containment, partial overlap, terminal-recursive overlap, and discarded mass.
3. **Export the first real Bellman row.** Use `src/branching_reserve_lp.py` only after the theorem determines the children.
4. **Add one structurally motivated coordinate at a time.** Candidate features include demand-aware completion deficit, rectangle deficit, outgoing SCC capacity, provenance reuse capacity, regeneration charge, and nonlinear internal capacity.
5. **Test one definition through `S_3,...,S_7`.** The objective is a stable theorem, not a fit at any cost.
6. **Stop or reformulate if the state dimension does not stabilize.** An indefinitely expanding feature list is evidence that the architecture is missing a deeper invariant."""
    new_program = """1. **Freeze state-specific `S_10` work.** Reopen it only to test a general reserve recurrence.
2. **Use the certified five-level retained quotient as the adversarial test frontier.** Do not reopen raw child semantics unless a precise global retention defect is identified.
3. **Develop anchor-survivor interval transfer.** For each backbone continuation, track the provenance-labeled interval `(u-min(S),u]`, its first use, release, and possible arithmetic obstruction export.
4. **Test the exact translation reserve on `R_1,...,R_5`.** Record either a fixed-coefficient theorem or the smallest exact no-go subsystem; do not propagate generation six.
5. **Refine dropped-lineage release by provenance.** Numerical coverage alone is not payment.
6. **Stop or reformulate if interval state does not compress.** An indefinitely expanding provenance signature is evidence that a deeper invariant is missing."""
    text = replace_once(text, old_program, new_program, "landscape immediate program")

    text = text.replace(
        "- a stable two-coordinate policy witness across a 250-constraint full five-step subset lattice through `S_7`.",
        "- a stable two-coordinate policy witness across a 250-constraint full five-step subset lattice through `S_7`;\n- a point-disjoint retained quotient propagated through generation five;\n- an exact unique-root transfer identity;\n- and an exact backbone-only minimum-anchor transfer classification.",
        1,
    )
    old_bottom = r"""The decisive open problem is not another candidate search, another selected path, or another finite policy ranking. It is

```math
\boxed{
\text{construct a provenance-preserving retained-child packing theorem}
}
```

and use it to prove a policy-aware branching Bellman or Carleson inequality."""
    new_bottom = r"""The decisive open problem is not another candidate search, another selected path, another finite policy ranking, or another arbitrary feature fit. It is

```math
\boxed{
\text{control provenance-labeled backbone intervals across the retained tree}
}
```

through a state-independent retention, bounded-reuse, and obstruction-export theorem, then use it to prove a policy-aware branching Bellman or Carleson inequality."""
    text = replace_once(text, old_bottom, new_bottom, "landscape bottom line")
    LANDSCAPE.write_text(text, encoding="utf-8")


def patch_lp() -> None:
    text = LP.read_text(encoding="utf-8")
    text = text.replace(
        "Without this contract, an exactly solved LP can represent the wrong inequality.",
        "The recorded adversarial construction now has exact point-disjoint retained rows through generation five. Without a state-independent global version of this contract and bounded cross-generation reuse, an exactly solved LP can still represent the wrong whole-tree inequality.",
        1,
    )
    text = text.replace(
        "## 10. Active next LP input\n\nThe next dataset must include external export from the high-growth cyclic component. Candidate variables are:",
        "## 10. Active next LP input\n\nThe cyclic-component variables remain relevant to the raw `S_7` frontier, but the five-generation retained frontier isolates a newer transfer object: provenance-labeled minimum-anchor intervals `(u-min(S),u]`. The next theorem-level dataset must include exact creation, retention, release, and reuse of these intervals. Candidate variables are:",
        1,
    )
    text = text.replace(
        "- target interval demand;\n- dyadic slack as an auxiliary term.",
        "- target interval demand;\n- dyadic slack as an auxiliary term;\n- anchor-survivor interval mass;\n- first-use versus repeated-use interval capacity;\n- minimum-anchor release;\n- provenance-valid coverage of dropped raw descendants.",
        1,
    )
    text = text.replace(
        "- a valid retention quotient;",
        "- a globally canonical or state-independent retention theorem;",
        1,
    )
    LP.write_text(text, encoding="utf-8")


def main() -> int:
    patch_readme()
    patch_landscape()
    patch_lp()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
