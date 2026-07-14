#!/usr/bin/env python3
"""Run the CL-089--CL-092 documentation patch without Python escape corruption.

The original patch module stores LaTeX-bearing Markdown in ordinary string
literals.  At runtime, ``\f`` in ``\frac`` and ``\r`` in ``\rm`` become
control characters.  This runner installs raw canonical strings and replaces
the recursive-mass section by heading boundaries, making repeated runs
idempotent even after partial documentation updates.
"""
from __future__ import annotations

from pathlib import Path

import patch_cl089_cl092_frontier as frontier


OLD_MASS = r"""Let `H_g^rec` denote recursively continuing retained harmonic mass. The four recorded ratios are:

```math
0.937
<
\frac{H_2^{\mathrm{rec}}}{H_1}
<
0.938,
```

```math
2.011553
<
\frac{H_3^{\mathrm{rec}}}{H_2^{\mathrm{rec}}}
<
2.011554,
```

```math
2.849279
<
\frac{H_4^{\mathrm{rec}}}{H_3^{\mathrm{rec}}}
<
2.849280,
```

and

```math
1.329813
<
\frac{H_5^{\mathrm{rec}}}{H_4^{\mathrm{rec}}}
<
1.329814.
```

Raw recursive harmonic mass is not an iterating Bellman potential.

Terminal output must be carried separately through a first-appearance ledger. It cannot be discarded, and it must not be counted as persistent recursive debt."""

NEW_MASS = r"""Let `H_1^rec` denote the mass of the fifteen genuinely recursive first-frontier states. The corrected first transition satisfies

```math
\frac{H_{2,\rm ordinary}^{\rm rec}}{H_1^{\rm rec}}
=
2.624517171606...,
```

and the residual-sponsor refinement gives

```math
\frac{H_{2,\rm sponsor}^{\rm rec}}{H_1^{\rm rec}}
=
2.030802800232....
```

The refinement removes `0.094242076816...` of recursive mass, or `22.6218512798%` of the corrected ordinary recursive load, while increasing terminal mass by `0.122243850563...`.

The formerly quoted ratio

```math
0.937
<
\frac{H_{2,\rm historical}^{\rm rec}}{H_1^{\rm total}}
<
0.938
```

compared a historical child to total first-frontier mass and arose from propagating six terminal parents. It is not a recursive contraction theorem.

The later historical ratios `2.011553...`, `2.849279...`, and `1.329813...` remain exact statements for the old diagnostic chain only. No corrected third frontier has been constructed, and none should be constructed before a state-independent activation-transfer lemma is fixed.

Raw recursive harmonic mass remains nonmonotone and is not an iterating Bellman potential. Terminal output must be charged once through a first-appearance ledger and must never be propagated as recursive debt."""

README_ACTIVE = r"""A rigorous finite retained quotient exists, but terminal stopping changes its active first transition. The first family contains six terminal states carrying `44.4642947826%` of its mass and fifteen recursive states. Recomputing from only those recursive parents gives a corrected ordinary second recursive ratio `2.624517171606...`; residual-sponsor refinement lowers it to `2.030802800232...`.

The historical second-to-fifth retained chain remains an exact finite diagnostic of the old all-parent construction. It is not the continuation of the correctly terminal-stopped tree.

The local production theorem has also strengthened. Retaining all three middle colors gives exactly two child memberships per three-AP and

```math
\sum_{\rm children}H(C)
=
2\mathcal L(B)
\ge
4H(B)-4\frac{r_3(N)}N.
```

The side token `d`, doubled side reserve `2d`, and middle token `d` form an exact weight-preserving dictionary for the three pair edges of the progression. Completed in-parent target pairs therefore pack into explicit scale-descending edge capacity.

The active theorem is now a bounded-reuse transfer law for these capacities. It must control sponsor-pair transport collisions, ambient completion roots outside the current lineage, genuine ambient holes with four-AP witnesses, terminal first appearance, and dyadic boundary transport. Generation six and propagation of the corrected second frontier remain blocked until that law is specified."""


def safe_patch_program() -> None:
    path = Path(frontier.ROOT) / "docs/current-proof-program.md"
    text = path.read_text(encoding="utf-8")

    heading = "## Corrected first retained frontier"
    next_heading = "## Latest exact refinement: backbone-anchor transfer"
    if heading in text:
        start = text.index(heading)
        end = text.index(next_heading, start)
        text = text[:start] + frontier.CURRENT_INSERT + text[end:]
    else:
        if next_heading not in text:
            raise AssertionError("missing current-program insertion marker")
        text = text.replace(next_heading, frontier.CURRENT_INSERT + next_heading, 1)

    text = frontier.replace_once(
        text,
        frontier.OLD_TABLE,
        frontier.NEW_TABLE,
        "retained table",
    )
    text = frontier.replace_heading_section(
        text,
        "## 3. Recursive and terminal mass",
        "## 4. Terminal identities",
        "## 3. Recursive and terminal mass\n\n" + NEW_MASS,
    )
    text = frontier.replace_heading_section(
        text,
        "## 9. Approved next targets",
        "## 10. Stop list",
        frontier.NEW_TARGETS,
    )

    old_status = (
        "The project is no longer searching for another finite-depth fitted "
        "feature or a new overlap quotient. Affine closure and pair-token "
        "containment now give exact whole-tree no-double-payment semantics. "
        "The active theorem target is an economical pair-activation or "
        "multiscale exposure bound that avoids paying the full latent root-pair "
        "energy of the initial dyadic block."
    )
    new_status = (
        "The active program combines terminal stopping, affine union-valued "
        "pair tokens, full-color role branching, and sponsor-pair transport. "
        "The local coefficient problem is closed for completed in-parent pair "
        "edges; the remaining theorem must bound transport collisions, "
        "parent-external completions, genuine ambient holes, and cross-branch "
        "first appearance."
    )
    text = text.replace(old_status, new_status)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def install_runtime_fixes() -> None:
    frontier.OLD_MASS = OLD_MASS
    frontier.NEW_MASS = NEW_MASS
    frontier.README_ACTIVE = README_ACTIVE
    frontier.patch_program = safe_patch_program


def main() -> int:
    install_runtime_fixes()
    return frontier.main()


if __name__ == "__main__":
    raise SystemExit(main())
