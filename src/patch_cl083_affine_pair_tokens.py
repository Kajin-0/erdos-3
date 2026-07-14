#!/usr/bin/env python3
"""Record the affine root-pair token theorem as CL-083."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")
TERMINAL = Path("docs/terminal-sink-first-appearance-ledger.md")

ROW = "| CL-083 | In an affine root forest, `(u,p)` is bijective with the root pair `(p-u,p)` and has weight `1/u=1/(p-(p-u))`. The global first-appearance mass of coarse point tokens is therefore at most the entering pair energy `J(P_0)`. A repeated `(u,p)` is genuine reuse of one pair resource; adding immediate provenance distinguishes histories but cannot create additional pair capacity. | Symbolic affine first-appearance and pair-reuse theorem. Affine coverage and entering `J(P_0)` payment remain open. |"

PROGRAM_INSERT = r"""
## Affine pair-token first-appearance theorem

For every affine point with current label `u` and root provenance `p`,

```math
r=p-u
```

is its root reference. Thus the coarse point token `(u,p)` is exactly the root pair `(r,p)` and has pair weight `1/(p-r)=1/u`.

For any affine forest over root universe `P_0`,

```math
\boxed{
\sum_{\text{first-appearance }(u,p)}\frac1u
\le
J(P_0).
}
```

A repeated coarse token is true reuse of the same pair capacity. Immediate provenance may distinguish occurrence histories, but it must not be treated as a second copy of the pair resource.

This gives a precise decomposition

```text
raw point mass
=
first-appearance pair mass
+
pair-reuse mass.
```

The first term is controlled by `J(P_0)`. The remaining structural target is pair-reuse mass plus payment for the entering pair energy.

Primary reference: `docs/affine-root-pair-token-ledger.md`.

---
"""

TERMINAL_INSERT = r"""
## Affine pair-capacity interpretation

When a terminal point belongs to an affine root state, its coarse token

```math
(u,p)
```

already determines the affine reference

```math
r=p-u.
```

Therefore `(u,p)` is the root pair `(r,p)` with weight `1/(p-r)=1/u`. In a fixed root universe `P_0`, first-appearance terminal pair mass satisfies

```math
\sum_{\text{first terminal }(u,p)}\frac1u
\le
J(P_0).
```

A collision of `(u,p)` is genuine pair-resource reuse. Refining the token to `(u,p,i)` may distinguish genealogical histories, but does not create another pair credit. The refined token should be treated as metadata unless a separate non-pair resource is proved.

This interpretation applies only after the affine root-reference hypotheses are verified.

---
"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-082 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = "- `docs/affine-root-pair-token-ledger.md`;\n"
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    inference = "45. immediate provenance as a second copy of harmonic pair capacity when the coarse affine token `(u,p)` repeats."
    if inference not in text:
        marker2 = "44. root-pair energy `J(P)` as automatically bounded by current harmonic mass or by four-AP-freeness alone."
        text = text.replace(marker2, marker2 + "\n" + inference, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## Affine pair-token first-appearance theorem" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)
    old = """1. Certify the affine root-coordinate hypotheses on the existing retained frontier: one common reference root per state and exact pivot update `p-r -> p-a`.
2. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
3. Compute entering root-pair energy `J(P)` by generation and identify which earlier production, terminal, completion, rectangle, or exclusion terms can pay it.
4. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
5. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
6. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    new = """1. Certify the affine root-coordinate hypotheses on the existing retained frontier: one common reference root per state and exact pivot update `p-r -> p-a`.
2. Compute occurrence and first-appearance root-pair mass by generation, including exact `(u,p)` collision/reuse ledgers.
3. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
4. Compute entering root-pair energy `J(P)` by generation and identify which earlier production, terminal, completion, rectangle, or exclusion terms can pay it.
5. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
6. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
7. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    if old in text:
        text = text.replace(old, new, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    block = r"""
### Affine pair-token interpretation

In an affine state, `(u,p)` determines reference root `r=p-u` and therefore identifies one root pair `(r,p)` of weight `1/u`. First-appearance coarse-token mass is a sub-sum of entering pair energy. A recurrence of `(u,p)` is exact reuse of the same pair resource, not merely an inadequate signature.

Immediate provenance may distinguish histories, but it cannot manufacture another copy of root-pair capacity. Pair-resource accounting should therefore merge repeated `(u,p)` tokens and track the excess as pair-reuse mass.

"""
    if "### Affine pair-token interpretation" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + block.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decision = "- `(u,p)` is the capacity-level token in the affine regime; `(u,p,i)` is history metadata unless a separate resource is proved;"
    if decision not in text:
        marker = "- the new bottleneck is the entering pair energy and an affine-entry theorem, not another local reuse coefficient;"
        text = text.replace(marker, marker + "\n" + decision, 1)
    HISTORY.write_text(text, encoding="utf-8")


def patch_terminal() -> None:
    text = TERMINAL.read_text(encoding="utf-8")
    if "## Affine pair-capacity interpretation" not in text:
        anchor = "## 5. Candidate Bellman form"
        text = text.replace(anchor, TERMINAL_INSERT.strip() + "\n\n" + anchor, 1)
    TERMINAL.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_history()
    patch_terminal()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
