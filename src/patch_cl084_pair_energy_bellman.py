#!/usr/bin/env python3
"""Record the exact fifth-frontier pair-energy Bellman row as CL-084."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")
README = Path("README.md")

ROW = "| CL-084 | The certified `R_4 -> F_5` retained transition has 12/12 affine fourth recursive states and 13/13 affine fifth recursive states, with root and pair multiplicity exactly one. Exact pair energy satisfies `H(F_5)+J(R_5^rec)<=J(R_4^rec)`: left `1586.466623468978...`, right `2743.858245303490...`, surplus `1157.391621834512...`, ratio `0.578188259610...`. | Exact finite retained-child Bellman theorem; fixed policy and quotient, no generation six. |"

PROGRAM_INSERT = r"""
## First exact pair-energy Bellman row

The adversarial fourth-to-fifth retained transition is now closed by a state-independent symbolic potential.

Both recursive frontiers are fully affine and have no root or pair duplication:

```text
R4: 12 states, 1717 roots, 370505 distinct pairs
R5: 13 states, 1015 roots, 106381 distinct pairs
```

The complete fifth output satisfies

```math
\boxed{
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4^{\rm rec}).
}
```

Exact values:

```text
H(F5)+J(R5_rec) = 1586.466623468978...
J(R4_rec)       = 2743.858245303490...
surplus          = 1157.391621834512...
ratio            = 0.578188259610...
```

This is a legitimate retained-child Bellman row with no fitted coefficient. It explains why raw recursive harmonic mass may expand while cumulative affine capacity contracts strongly.

The active frontier moves earlier: determine where affine coordinates and pair uniqueness first emerge, and control occurrence-versus-union pair energy before generation four.

Primary reference: `docs/fifth-generation-pair-energy-bellman-row.md`.

---
"""

HISTORY_INSERT = r"""
### Exact fifth-frontier pair-energy row

The pair-energy potential was tested on the first previously failing retained transition. Every fourth and fifth recursive state is affine, every root and pair has multiplicity one, and

```math
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4^{\rm rec})
```

with ratio `0.578188259610...` and surplus `1157.391621834512...`.

This is the first exact retained-child Bellman row with a state-independent symbolic potential and no fitted coefficient. The fourth-to-fifth expansion is closed. The unresolved frontier moves to earlier generations, where root and pair reuse may still occur and affine coverage has not yet been certified.

"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-083 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = (
        "- `docs/fifth-generation-pair-energy-bellman-row.md`;\n"
        "- `src/verify_pair_energy_frontier.py`;\n"
        "- `data/pair_energy_frontier_certificate_2026-07-14.txt`;\n"
    )
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    inference = "46. the fourth-to-fifth raw harmonic expansion as an obstruction after root-pair energy is included."
    if inference not in text:
        marker2 = "45. immediate provenance as a second copy of harmonic pair capacity when the coarse affine token `(u,p)` repeats."
        text = text.replace(marker2, marker2 + "\n" + inference, 1)

    old = (
        "The source and shell classification is complete on the baseline transition: all "
        "`1015` survivors are backbone translations. The affine pivot pair-energy theorem "
        "now gives an exact no-reuse potential whenever recursive states have one common "
        "root reference and child root sets are disjoint. Generation six remains blocked. "
        "The next concrete targets are to certify the affine hypotheses on the retained "
        "frontier, control the entering pair energy `J(P)`, and determine what terminal or "
        "arithmetic credit is created before or when non-affine structure enters that regime."
    )
    new = (
        "The fourth-to-fifth frontier is now closed exactly: every recursive state on both "
        "sides is affine, root and pair multiplicities are one, and `H(F_5)+J(R_5^rec)` is "
        "only `57.8189%` of `J(R_4^rec)`. Generation six remains blocked and unnecessary. "
        "The next concrete targets are the earlier transitions: certify affine coverage, "
        "measure occurrence-versus-union pair energy, and control repeated `(u,p)` pair tokens "
        "before the unique-root regime begins."
    )
    if old in text:
        text = text.replace(old, new, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## First exact pair-energy Bellman row" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)

    old_targets = """1. Certify the affine root-coordinate hypotheses on the existing retained frontier: one common reference root per state and exact pivot update `p-r -> p-a`.
2. Compute occurrence and first-appearance root-pair mass by generation, including exact `(u,p)` collision/reuse ledgers.
3. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
4. Compute entering root-pair energy `J(P)` by generation and identify which earlier production, terminal, completion, rectangle, or exclusion terms can pay it.
5. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
6. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
7. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    new_targets = """1. Export affine-state coverage and occurrence/union pair-energy profiles for `R_1,R_2,R_3`.
2. Test the exact Bellman rows `H(F_{g+1})+J_union(R_{g+1})<=J_union(R_g)+reuse_charge_g` for `g=1,2,3`.
3. Compute exact first-appearance and reused `(u,p)` mass by transition; immediate provenance remains metadata, not additional pair credit.
4. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
5. Identify a structural payment for entering pair energy from parent production, terminalization, completion, rectangle support, or cheap-extension exclusion.
6. Test the exact translation reserve only as a diagnostic comparison; pair energy is now the principal candidate potential.
7. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
8. Do not propagate generation six.
"""
    if old_targets in text:
        text = text.replace(old_targets, new_targets, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "### Exact fifth-frontier pair-energy row" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + HISTORY_INSERT.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decisions = (
        "- the fourth-to-fifth retained expansion is closed by pair energy and is no longer an open obstruction;\n"
        "- pair energy, not scalar translation reserve, is the principal cumulative affine potential;\n"
        "- generation six is unnecessary until earlier-generation affine entry and pair reuse are resolved;"
    )
    if decisions not in text:
        marker = "- `(u,p)` is the capacity-level token in the affine regime; `(u,p,i)` is history metadata unless a separate resource is proved;"
        text = text.replace(marker, marker + "\n" + decisions, 1)
    HISTORY.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    item = "15. an exact pair-energy Bellman row closing the recorded fourth-to-fifth retained expansion."
    if item not in text:
        marker = "14. an exact backbone-only survivor classification and minimum-anchor transfer decomposition."
        text = text.replace(marker, marker + "\n" + item, 1)
    reference = "- [`docs/fifth-generation-pair-energy-bellman-row.md`](docs/fifth-generation-pair-energy-bellman-row.md) — exact affine pair-energy Bellman row at the first failing retained transition."
    if reference not in text:
        marker2 = "- [`docs/backbone-anchor-root-transfer.md`](docs/backbone-anchor-root-transfer.md) — exact backbone-only survivor and minimum-anchor transfer theorem."
        text = text.replace(marker2, marker2 + "\n" + reference, 1)
    README.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_history()
    patch_readme()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
