#!/usr/bin/env python3
"""Record affine output closure and universal pair containment as CL-086."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")
README = Path("README.md")
LANDSCAPE = Path("docs/comprehensive-research-landscape.md")

ROW = "| CL-086 | Coordinated deletion preserves affine root coordinates: terminal residuals remain `S_r(P_R)`, backbone shells are `S_a(Q)`, and a step-`q` middle fiber is `S_{t_0}(T_q\\{t_0})`, where `t_0` is the sponsor root of the minimum center. Consequently every child current/latent pair is a parent current or latent pair, and union-valued pair capacity is nonincreasing for arbitrary simultaneous output and retention. Occurrence expansion equals exact repeated-pair mass. | Symbolic whole-family affine closure and pair-resource containment theorem. Entering/economically activated pair energy remains open. |"

PROGRAM_INSERT = r"""
## Universal affine closure and pair-resource containment

Affine structure is not a late-generation accident. It is preserved exactly by every output type in the coordinated deletion construction.

For an affine parent

```math
S_r(P)=\{p-r:p\in P\},
```

one has:

```text
terminal residual: S_r(P_R)
backbone shell:    S_a(Q), a=min(P)
middle-fiber shell:S_{t_0}(Q),
```

where `t_0` is the sponsor root attached to the minimum selected center for that step.

For the middle fiber, if centers are `c_j=p_j-r` and sponsors have roots `t_j=p_j+epsilon(q)q`, then

```math
c_j-c_0
=p_j-p_0
=t_j-t_0.
```

Thus every descendant remains affine under the repository provenance convention.

Define the parent resource universe

```math
\mathcal U_r(P)
=
\{(r,p):p\in P\}
\cup
\binom P2.
```

Every terminal current pair, recursive current pair, and recursive latent pair emitted by the parent belongs to `\mathcal U_r(P)`. Therefore for any simultaneous retained family,

```math
\boxed{
\mathcal U_\cup(\mathrm{Child}(\mathcal F))
\subseteq
\mathcal U_\cup(\mathcal F).
}
```

The global overlap and repeated-payment problem is therefore solved at the level of distinct pair tokens. Occurrence-valued expansion is exactly

```math
R_{\rm pair}
=
W_{\rm occ}-W_\cup.
```

The remaining theorem is no longer a retention quotient or cross-generation reuse theorem. It is an economical **pair-activation theorem**: avoid prepaying the full latent pair energy, or charge activated pair mass to summable production, terminal, or arithmetic obstruction terms.

Primary reference: `docs/affine-output-closure-and-pair-containment.md`.

---
"""

HISTORY_INSERT = r"""
### Universal affine closure and pair containment

The finite affine observations were generalized symbolically. Terminal residuals, backbone shells, and middle-fiber shells of every affine parent are affine. In particular, a fixed-step middle fiber has values `t-t_0` in sponsor-root coordinates.

Every child current or latent pair is therefore already a parent pair resource. Union-valued pair capacity is nonincreasing for arbitrary simultaneous output and retained subfamilies, while occurrence-valued excess is exactly repeated pair-token mass.

This resolves the long-standing overlap/provenance bookkeeping bottleneck at the level of distinct resources. The active analytical bottleneck is now economical pair activation or a summable bound on the activated pair universe, not another retention rule.

"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-085 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = "- `docs/affine-output-closure-and-pair-containment.md`;\n"
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    inference = "47. non-affine middle-fiber structure as an unavoidable feature of the coordinated deletion descendants under the recorded root-provenance convention."
    if inference not in text:
        marker2 = "46. the fourth-to-fifth raw harmonic expansion as an obstruction after root-pair energy is included."
        text = text.replace(marker2, marker2 + "\n" + inference, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if text.startswith("# Current proof program: root-lineage reserve transfer"):
        text = text.replace(
            "# Current proof program: root-lineage reserve transfer",
            "# Current proof program: affine pair-resource activation",
            1,
        )
    if "## Universal affine closure and pair-resource containment" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)
    old_status = (
        "The project is no longer searching for another finite-depth fitted feature. "
        "The active theorem target is a cumulative ancestor-path capacity that explains "
        "where harmonic reserve goes when provenance multiplicity disappears and unique "
        "lineages continue contracting."
    )
    new_status = (
        "The project is no longer searching for another finite-depth fitted feature or a "
        "new overlap quotient. Affine closure and pair-token containment now give exact "
        "whole-tree no-double-payment semantics. The active theorem target is an economical "
        "pair-activation or multiscale exposure bound that avoids paying the full latent "
        "root-pair energy of the initial dyadic block."
    )
    if old_status in text:
        text = text.replace(old_status, new_status, 1)

    old_targets = """1. Export affine-state coverage and occurrence/union pair-energy profiles for `R_1,R_2,R_3`.
2. Test the exact Bellman rows `H(F_{g+1})+J_union(R_{g+1})<=J_union(R_g)+reuse_charge_g` for `g=1,2,3`.
3. Compute exact first-appearance and reused `(u,p)` mass by transition; immediate provenance remains metadata, not additional pair credit.
4. Prove an affine-entry or affine-purification theorem for recursively continuing states, separating non-affine middle-fiber structure as terminal or obstruction output.
5. Identify a structural payment for entering pair energy from parent production, terminalization, completion, rectangle support, or cheap-extension exclusion.
6. Test the exact translation reserve only as a diagnostic comparison; pair energy is now the principal candidate potential.
7. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
8. Do not propagate generation six.
"""
    new_targets = """1. Quantify occurrence versus union pair resources on `R_1,R_2,R_3` and isolate exact repeated-pair mass.
2. Replace full latent `J(P)` by an activated-pair ledger that opens a token only when a pivot, terminal point, or recursive child actually uses it.
3. Prove a multiscale bound for activated pair mass using four-AP-freeness, fixed-step run structure, coordinated deletion, or stopping-time sparsity.
4. Relate activated pair mass to the existing one-generation harmonic production and summable `r_3(N)/N` error.
5. Determine whether completion, rectangle support, and cheap-extension exclusion pay for dense clusters of short root pairs.
6. Compute exact first-appearance and reused `(u,p)` mass by transition; immediate provenance remains metadata, not additional pair credit.
7. Use earlier-generation finite diagnostics only to discover the activation law or its smallest obstruction.
8. Do not propagate generation six.
"""
    if old_targets in text:
        text = text.replace(old_targets, new_targets, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "### Universal affine closure and pair containment" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + HISTORY_INSERT.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decisions = (
        "- affine entry is automatic from the initial state under terminal, backbone, and middle-fiber output;\n"
        "- union-valued pair containment resolves duplicate, containment, partial-overlap, and cross-generation payment semantics;\n"
        "- the active theorem is economical pair activation, not another retained-child quotient or affine-purification lemma;"
    )
    if decisions not in text:
        marker = "- the fifth-frontier pair row has exact token ownership and no repeated payment; future work should reuse this resource schema rather than fit scalar surrogates;"
        text = text.replace(marker, marker + "\n" + decisions, 1)
    HISTORY.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    item = "17. a symbolic affine-closure theorem and universal union-valued pair-resource containment for every coordinated deletion output."
    if item not in text:
        marker = "16. an exact pair-resource partition proving containment and zero repeated payment at the fifth frontier."
        text = text.replace(marker, marker + "\n" + item, 1)
    reference = "- [`docs/affine-output-closure-and-pair-containment.md`](docs/affine-output-closure-and-pair-containment.md) — universal affine descendant and pair-resource containment theorem."
    if reference not in text:
        marker2 = "- [`docs/fifth-generation-pair-resource-partition.md`](docs/fifth-generation-pair-resource-partition.md) — explicit fifth-child to fourth-pair ownership and unused-capacity theorem."
        text = text.replace(marker2, marker2 + "\n" + reference, 1)
    old = (
        "The decisive missing theorem is now a cumulative provenance-preserving transfer "
        "law controlling reuse of these anchor-survivor intervals across the whole retained tree."
    )
    new = (
        "Affine closure and union-valued pair containment now control reuse exactly across "
        "the whole retained tree. The decisive missing theorem is an economical activation "
        "or multiscale exposure bound for the pair tokens actually used."
    )
    if old in text:
        text = text.replace(old, new, 1)
    README.write_text(text, encoding="utf-8")


def patch_landscape() -> None:
    text = LANDSCAPE.read_text(encoding="utf-8")
    text = text.replace("through claim `CL-081`", "through claim `CL-086`", 1)
    old = "The decisive missing object is now a **state-independent cumulative root-lineage transfer law** controlling how provenance-labeled anchor-survivor intervals are created, reused, terminalized, discarded, or converted into arithmetic obstruction. The finite quotient supplies legitimate test rows but not the whole-tree theorem."
    new = "Affine closure and universal pair-resource containment now provide a state-independent whole-tree quotient at the level of distinct root pairs. Creation, reuse, terminalization, and recursive continuation are exact pair-token operations. The decisive missing object is an **economical pair-activation theorem** controlling only the pair tokens actually exposed, rather than prepaying the full latent pair energy."
    if old in text:
        text = text.replace(old, new, 1)
    LANDSCAPE.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_history()
    patch_readme()
    patch_landscape()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
