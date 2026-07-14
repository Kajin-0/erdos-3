#!/usr/bin/env python3
"""Record the affine pivot pair-energy theorem as CL-082."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")

ROW = "| CL-082 | For an affine state `S_r(P)={p-r:p in P}`, pivot `a=min(P)`, and pairwise root-disjoint children `S_a(Q_i)`, the root-pair energy `J(P)=sum_{x<y in P}1/(y-x)` satisfies `sum_i(H(S_a(Q_i))+J(Q_i))<=J(P)`. Hence every root pair pays at most once in an affine pivot forest, and terminal harmonic mass plus frontier pair energy is bounded by the entering pair energy. | Symbolic treewise packing theorem; no AP hypothesis. Initial pair-energy control and affine-entry theorem remain open. |"

PROGRAM_INSERT = r"""
## Symbolic affine pivot packing theorem

For an affine root state

```math
S_r(P)=\{p-r:p\in P\},
\qquad
r<\min P,
```

minimum translation at `a=min(P)` is exactly the reference pivot

```math
r\longrightarrow a,
\qquad
p-r\longrightarrow p-a.
```

Define root-pair energy

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

For pairwise root-disjoint retained children `S_a(Q_i)`,

```math
\boxed{
\sum_i
\left(
H(S_a(Q_i))+J(Q_i)
\right)
\le
J(P).
}
```

Every harmonic child term is charged to one ordered pivot pair `(a,p)`, while each child pair energy uses a distinct pair internal to one `Q_i`. Thus cross-generation reuse is exactly controlled inside an affine pivot forest.

This does **not** bound the entering `J(P)`. The active theorem has separated into two tasks:

1. certify and generalize entry into the affine root-pivot regime;
2. pay for entering pair energy through earlier recursive production, terminal first appearance, or arithmetic obstruction export.

Primary reference: `docs/affine-pivot-pair-energy.md`.

---
"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-081 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = "- `docs/affine-pivot-pair-energy.md`;\n- `src/probe_affine_root_pivot.py`;\n"
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    inference = "44. root-pair energy `J(P)` as automatically bounded by current harmonic mass or by four-AP-freeness alone."
    if inference not in text:
        marker2 = "43. scalar minimum-anchor mass `1/min(S)` as complete payment for all enabled backbone intervals."
        text = text.replace(marker2, marker2 + "\n" + inference, 1)

    old = (
        "The source and shell classification is now complete on the baseline transition: "
        "all `1015` survivors are backbone translations, the twelve minimum anchors have "
        "no raw output, and three parent classes carry nearly `88%` of gain. Generation "
        "six remains blocked. The next concrete target is a state-independent transfer "
        "law for provenance-labeled anchor-survivor intervals `(u-min(S),u]`, coupled to "
        "first-appearance terminal credit and a provenance-valid classification of the "
        "`673` dropped roots that generated raw descendants."
    )
    new = (
        "The source and shell classification is complete on the baseline transition: all "
        "`1015` survivors are backbone translations. The affine pivot pair-energy theorem "
        "now gives an exact no-reuse potential whenever recursive states have one common "
        "root reference and child root sets are disjoint. Generation six remains blocked. "
        "The next concrete targets are to certify the affine hypotheses on the retained "
        "frontier, control the entering pair energy `J(P)`, and determine what terminal or "
        "arithmetic credit is created before or when non-affine structure enters that regime."
    )
    if old in text:
        text = text.replace(old, new, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## Symbolic affine pivot packing theorem" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)

    old_targets = """1. Define a provenance-labeled anchor-survivor interval state for `(u-min(S),u]` and state exactly when that interval is created, retained, released, or reused.
2. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
3. Attach the 17 terminalized roots injectively to first-appearance `(u,p,i)` terminal tokens.
4. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
5. Prove a bounded-reuse or obstruction-export lemma for anchor-survivor intervals.
6. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    new_targets = """1. Certify the affine root-coordinate hypotheses on the existing retained frontier: one common reference root per state and exact pivot update `p-r -> p-a`.
2. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
3. Compute entering root-pair energy `J(P)` by generation and identify which earlier production, terminal, completion, rectangle, or exclusion terms can pay it.
4. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
5. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
6. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    if old_targets in text:
        text = text.replace(old_targets, new_targets, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    block = r"""
### Affine pivot pair-energy theorem

For an affine root state `S_r(P)={p-r:p in P}`, minimum translation at `a=min(P)` changes the common root reference from `r` to `a`. For pairwise root-disjoint children `S_a(Q_i)`, define

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

Exact pair bookkeeping gives

```math
\sum_i
\left(
H(S_a(Q_i))+J(Q_i)
\right)
\le
J(P).
```

Therefore every root pair is used at most once in an affine pivot forest. Cross-generation reuse is not the unresolved issue inside this model. The unresolved issues are entry into the affine regime and payment for the entering pair energy.

"""
    if "### Affine pivot pair-energy theorem" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + block.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decisions = (
        "- affine pivot forests admit an exact pair-energy Bellman potential, so root-pair reuse is controlled once affine coordinates and root-disjoint children are established;\n"
        "- the new bottleneck is the entering pair energy and an affine-entry theorem, not another local reuse coefficient;"
    )
    if decisions not in text:
        marker = "- the baseline failing survivor family is backbone-only, and scalar minimum-anchor release is not sufficient payment for enabled translation intervals;"
        text = text.replace(marker, marker + "\n" + decisions, 1)

    old = """1. define provenance-labeled anchor-survivor interval state and its one-step transfer semantics;
2. test the exact minimum-translation reserve on the four existing transitions;
3. attach the `17` terminalized roots injectively to first-appearance `(u,p,i)` tokens;
4. distinguish provenance-valid release from numerical coverage among the `673` dropped roots with raw descendants;
5. formulate a bounded-reuse or obstruction-export lemma before propagating another generation.
"""
    new = """1. certify affine root references and exact pivot updates on the existing retained frontier;
2. test the exact minimum-translation reserve on the four existing transitions;
3. quantify entering pair energy and identify a noncircular payment source;
4. prove affine entry/purification or charge non-affine recursive output to terminal or arithmetic obstruction;
5. distinguish provenance-valid release from numerical coverage among the `673` dropped roots with raw descendants;
6. formulate the resulting transfer lemma before propagating another generation.
"""
    if old in text:
        text = text.replace(old, new, 1)
    HISTORY.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
