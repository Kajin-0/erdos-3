#!/usr/bin/env python3
"""Apply the corrected retained frontier and record CL-093 through CL-096.

This wrapper first runs the previously prepared CL-089--CL-092 canonical patch,
then replaces the now-refuted constant-reuse target by the full-edge collision
fiber and unbounded shell-valid reuse frontier.
"""
from __future__ import annotations

from pathlib import Path

import patch_cl089_cl092_frontier as base

ROOT = Path(__file__).resolve().parents[1]

CL092 = "| CL-092 | Every activated sponsor pair admits monotone forward transport: pair weight is nondecreasing and minimum deletion rank strictly increases until a direct selected edge, backward obstruction, or residual pair is reached. For a residual minimum `a`, the star pair `{a,s}` is backward exactly for even `v_2(q_s)`, and its backward mass is bounded by `2 sum_j 1/q_j` plus an injective completion-obstruction term. Parent-external completions must be split into ambient roots outside the lineage and genuine ambient holes. | Symbolic sponsor-pair transport, parity, and completion-charge theorems. |"
CL093 = "| CL-093 | Oriented full-edge branching emits one side token `d`, one middle token `d`, and one doubled-side token `2d` per parent three-AP. Exact child occurrence mass is `(5/2)L(B)>=5H(B)-5r_3(N)/N`. Every physical parent pair edge belongs to at most two three-APs, so distinct current pair-union mass is at least `(5/4)L(B)>=(5/2)H(B)-(5/2)r_3(N)/N`. Exhaustive verification covered all `2233` four-AP-free subsets of `[1,12]`. | Symbolic full-edge branching and pair-union theorem plus exhaustive regression. |"
CL094 = "| CL-094 | After mandatory standard dyadic shelling, ordinary side/middle child bases satisfy `M<=N/4`, doubled-side bases satisfy `M<=N/2`, and a latent physical pair of gap `D` in a shell `[M,2M)` obeys `D<M`. Along every latent lineage `D/M` at least doubles, so no physical pair has an infinite latent lineage. Same-type collision references also satisfy explicit forbidden-gap constraints. | Symbolic dyadic gap-monotonicity and pathwise termination theorem; cross-branch multiplicity is not bounded. |"
CL095 = "| CL-095 | Shell-valid latent-pair multiplicity is unbounded. For every `m`, a finite four-AP-free parent in one standard dyadic block can emit `m` recursive first-side shells in one child block, all containing a common root three-AP and hence sharing all three of its latent pairs. A certified `m=4` instance has a 19-point parent in `[4096,8192)`, four recursive shells in `[1024,2048)`, and common pair multiplicity four. | Symbolic infinite-family no-go theorem plus exact multiplicity-four certificate. Uniform finite overlap bounds are false. |"
CL096 = "| CL-096 | Fixing one transported parent three-AP `T` and one child type, all colliding child witness progressions are exactly three affine translates of the collision reference set: side `(R_T+T)/2`, middle `2R_T-T`, doubled side `2T-R_T`. The fixed-step witnesses are pairwise disjoint, so the forced layer family has size `3|R_T|`; child witness-edge occurrence energy is respectively `2mE(T)`, `mE(T)`, or `(m/2)E(T)`. | Symbolic collision-fiber theorem. The active target is weighted three-translate exposure, not constant multiplicity. |"

COLLISION_SECTION = r"""## Full-edge collision frontier

The full-edge construction emits the three edge weights of every parent
three-AP:

```math
\frac1d,\qquad\frac1d,\qquad\frac1{2d}.
```

Consequently

```math
\sum_{m full\mbox{-}edge\ children}H(C)
=
\frac52\mathcal L(B)
\ge
5H(B)-5\frac{r_3(N)}N.
```

A physical parent pair belongs to at most two three-APs, so the distinct
current pair union satisfies

```math
W_\cup(E(B))
\ge
\frac54\mathcal L(B)
\ge
\frac52H(B)-\frac52\frac{r_3(N)}N.
```

This does not imply bounded recursive latent reuse. Uniform finite
multiplicity is false. For every `m`, there is a four-AP-free parent in one
standard dyadic block with `m` recursive side shells sharing one root
three-AP. The certified `m=4` instance uses a 19-point parent in
`[4096,8192)` and four recursive children in `[1024,2048)`.

The reuse geometry is nevertheless rigid. Fix a transported parent witness
`T` and its collision reference set `R_T`. The complete child witness fiber is
one of

```math
\frac12(R_T+T),
\qquad
2R_T-T,
\qquad
2T-R_T,
```

for side, middle, and doubled-side transport. Each expression is three equal
translates of an affine image of `R_T`. Fixed-step witnesses are pairwise
disjoint, so the layer family has exactly `3|R_T|` points.

Mandatory shelling supplies a path coordinate. If a physical pair has gap `D`
in a shell of base `M`, then `D<M`; along every descendant lineage `D/M` at
least doubles. Thus every latent lineage terminates, although arbitrarily many
branches may carry the pair at one scale.

The active theorem is now a weighted three-translate exposure inequality that
charges collision multiplicity to the forced reference-set layers and their
later scale descent. Neither another constant-overlap lemma nor another
retained generation is admissible.

Primary references:

- `docs/full-edge-coordinated-branching.md`;
- `data/full_edge_coordinated_branching_summary.txt`;
- `docs/full-edge-dyadic-gap-monotonicity.md`;
- `docs/full-edge-collision-fiber-theorem.md`;
- `docs/parametric-shelled-pair-reuse-gadget.md`;
- `docs/unbounded-shelled-latent-pair-reuse.md`;
- `data/shelled_pair_reuse_gadget_summary.txt`;
- `data/unbounded_shelled_pair_reuse_instance_summary.txt`.

---

"""

NEW_TARGETS = r"""## 9. Approved next targets

1. Formulate a weighted collision-fiber exposure `X(T,R_T)` for the forced three-translate families `(R_T+T)/2`, `2R_T-T`, and `2T-R_T`.
2. Prove a transition inequality in which child active-edge occurrence mass is paid by parent active-edge first appearance plus decrease of `X` under dyadic shell descent.
3. Use `D/M` as the path coordinate: it at least doubles along every latent-pair lineage, but branch multiplicity must be charged through the reference-set layers.
4. Separate transport collisions by side, middle, and doubled-side scaling coefficients `2`, `1`, and `1/2` relative to the transported parent witness energy.
5. Retain sponsor-pair direct/backward/residual classification only as an input to the same collision/external-completion ledger.
6. Resolve the independent CL-087 generation-consistency audit before using its numerical metrics in any transfer fit.
7. Do not propagate the corrected second frontier, and do not generate generation six.

The desired theorem is a weighted three-translate exposure law. Uniform latent-pair multiplicity bounds, pairwise recursive-shell disjointness, and gap monotonicity without a branch charge are permanently rejected targets."""

HISTORY_INSERT = r"""### Full-edge collision and unbounded reuse

Full-edge branching closes the local edge-production coefficient: occurrence
mass has factor `5`, and current pair-union mass has factor at least `5/2`.
Mandatory shelling makes every latent-pair lineage finite because normalized
gap `D/M` at least doubles.

Cross-branch reuse is nevertheless unbounded. A parametric three-layer family
produces arbitrarily many recursive side shells sharing one root progression.
The `m=4` certificate gives four copies of all three common latent pairs in one
transition.

Fixing one transported parent witness reveals the exact collision geometry:
all preimage child witnesses are three affine translates of their reference
set. The correct reserve is therefore weighted three-translate exposure, not
a uniform overlap constant.

"""


def replace_section(text: str, heading: str, next_heading: str, block: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise AssertionError(f"cannot locate section {heading!r}")
    return text[:start] + block.rstrip() + "\n\n---\n\n" + text[end:]


def patch_ledger() -> None:
    path = ROOT / "docs/certainty-ledger.md"
    text = path.read_text(encoding="utf-8")
    rows = {CL093, CL094, CL095, CL096}
    text = "\n".join(line for line in text.splitlines() if line not in rows) + "\n"
    if CL092 not in text:
        raise AssertionError("missing CL-092 marker")
    text = text.replace(CL092 + "\n", CL092 + "\n" + "\n".join((CL093, CL094, CL095, CL096)) + "\n", 1)
    marker = "Primary latest references:\n\n"
    refs = (
        "- `docs/full-edge-coordinated-branching.md`;\n"
        "- `data/full_edge_coordinated_branching_summary.txt`;\n"
        "- `docs/full-edge-dyadic-gap-monotonicity.md`;\n"
        "- `docs/full-edge-collision-fiber-theorem.md`;\n"
        "- `docs/unbounded-shelled-latent-pair-reuse.md`;\n"
        "- `data/unbounded_shelled_pair_reuse_instance_summary.txt`;\n"
    )
    for line in refs.splitlines():
        text = text.replace(line + "\n", "")
    if marker not in text:
        raise AssertionError("missing latest-reference marker")
    text = text.replace(marker, marker + refs, 1)
    prohibited = "14. a universal finite bound on recursive latent-pair multiplicity;\n15. pairwise latent-pair disjointness of recursive full-edge shells;\n16. dyadic gap monotonicity alone as a cross-branch reuse theorem.\n"
    pmark = "# Prohibited inferences\n"
    if prohibited not in text:
        if pmark not in text:
            raise AssertionError("missing prohibited-inference marker")
        # Append to the existing numbered list immediately before its next divider.
        divider = text.find("\n---\n", text.find(pmark))
        if divider < 0:
            divider = len(text)
        text = text[:divider].rstrip() + "\n" + prohibited + "\n" + text[divider:].lstrip("\n")
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = path.read_text(encoding="utf-8")
    heading = "## Full-edge collision frontier"
    next_heading = "## Latest exact refinement: backbone-anchor transfer"
    if heading in text:
        text = replace_section(text, heading, next_heading, COLLISION_SECTION)
    else:
        if next_heading not in text:
            raise AssertionError("missing collision-section insertion marker")
        text = text.replace(next_heading, COLLISION_SECTION + next_heading, 1)
    text = replace_section(text, "## 9. Approved next targets", "## 10. Stop list", NEW_TARGETS)
    old = "The active program combines terminal stopping, affine union-valued pair tokens, full-color role branching, and sponsor-pair transport. The local coefficient problem is closed for completed in-parent pair edges; the remaining theorem must bound transport collisions, parent-external completions, genuine ambient holes, and cross-branch first appearance."
    new = "The active program combines terminal stopping, oriented full-edge branching, affine active-pair transport, and dyadic shell descent. The local current-edge coefficient is closed, but recursive latent-pair multiplicity is unbounded. The remaining theorem is a weighted three-translate collision-fiber exposure law, together with external-completion and terminal first-appearance bookkeeping."
    text = text.replace(old, new)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    items = [
        "24. a full-edge branching theorem with exact occurrence factor `5` and current pair-union factor at least `5/2`;",
        "25. a dyadic gap-monotonicity theorem proving every latent physical-pair lineage terminates;",
        "26. an unbounded shell-valid latent-pair reuse theorem, with a certified multiplicity-four instance;",
        "27. a collision-fiber theorem identifying every fixed-witness reuse family as three affine translates of its reference set.",
    ]
    lines = [line for line in text.splitlines() if line not in items]
    text = "\n".join(lines) + "\n"
    marker = "23. an exact side/middle/doubled-side pair-edge capacity dictionary and monotone sponsor-pair transport theorem.\n"
    if marker not in text:
        raise AssertionError("missing README claim-23 marker")
    text = text.replace(marker, marker + "\n".join(items) + "\n", 1)
    old = "The active theorem is now a bounded-reuse transfer law for these capacities. It must control sponsor-pair transport collisions, ambient completion roots outside the current lineage, genuine ambient holes with four-AP witnesses, terminal first appearance, and dyadic boundary transport. Generation six and propagation of the corrected second frontier remain blocked until that law is specified."
    new = "Uniform bounded reuse is false: shell-valid latent-pair multiplicity is unbounded. Every fixed-witness collision fiber is instead three affine translates of its reference set, while normalized pair gap grows geometrically along each lineage. The active theorem is a weighted three-translate exposure law that pays branch multiplicity through these forced layers. Generation six and propagation of the corrected second frontier remain blocked."
    text = text.replace(old, new)
    link_marker = "- [`docs/sponsor-pair-forward-transport.md`](docs/sponsor-pair-forward-transport.md) — monotone activated-pair transport theorem.\n"
    links = (
        "- [`docs/full-edge-coordinated-branching.md`](docs/full-edge-coordinated-branching.md) — exact occurrence-factor-five and current pair-union theorem.\n"
        "- [`docs/full-edge-dyadic-gap-monotonicity.md`](docs/full-edge-dyadic-gap-monotonicity.md) — pathwise latent-pair termination under mandatory shelling.\n"
        "- [`docs/full-edge-collision-fiber-theorem.md`](docs/full-edge-collision-fiber-theorem.md) — exact three-translate collision geometry.\n"
        "- [`docs/unbounded-shelled-latent-pair-reuse.md`](docs/unbounded-shelled-latent-pair-reuse.md) — arbitrary one-generation latent-pair multiplicity.\n"
    )
    for line in links.splitlines():
        text = text.replace(line + "\n", "")
    if link_marker not in text:
        raise AssertionError("missing README sponsor-transport link")
    text = text.replace(link_marker, link_marker + links, 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_history() -> None:
    path = ROOT / "docs/research-decision-history.md"
    text = path.read_text(encoding="utf-8")
    heading = "### Full-edge collision and unbounded reuse"
    if heading in text:
        start = text.index(heading)
        end = text.index("**Decisions:**", start)
        text = text[:start] + text[end:]
    marker = "**Decisions:**\n"
    stop = text.find("## 11. Permanent stop list")
    position = text.rfind(marker, 0, stop)
    if position < 0:
        raise AssertionError("missing history decision marker")
    text = text[:position] + HISTORY_INSERT + text[position:]
    decisions = [
        "- recursive latent-pair multiplicity has no universal finite bound;",
        "- pairwise latent-pair disjointness is false even after mandatory dyadic shelling;",
        "- dyadic gap growth proves pathwise termination but does not control branch count;",
        "- every fixed-witness collision fiber must be accounted for as three affine translates of a reference set;",
        "- the active reserve is weighted three-translate exposure, not scalar overlap multiplicity;",
    ]
    dmark = "- parent-external ambient roots and genuine ambient holes are different obstruction classes and must not be conflated;\n"
    for line in decisions:
        text = text.replace(line + "\n", "")
    if dmark not in text:
        raise AssertionError("missing history decision insertion marker")
    text = text.replace(dmark, dmark + "\n".join(decisions) + "\n", 1)
    stop_items = [
        "29. a universal finite recursive latent-pair overlap constant;",
        "30. pairwise recursive-shell latent-pair disjointness;",
        "31. dyadic gap monotonicity without a cross-branch exposure charge.",
    ]
    lines = [line for line in text.splitlines() if line not in stop_items]
    text = "\n".join(lines) + "\n"
    smark = "28. generation-six propagation without a predeclared conceptual test.\n"
    if smark not in text:
        raise AssertionError("missing stop-list item 28")
    text = text.replace(smark, smark + "\n".join(stop_items) + "\n", 1)
    old_start = "## 12. Active closing target"
    protocol = "## 13. Documentation protocol"
    active = r"""## 12. Active closing target

The active transfer architecture is

```text
child active edge
-> oriented completion transport
-> fixed parent witness T
-> collision reference set R_T
-> forced three-translate layer family
-> dyadic descent or terminal/external-completion release.
```

The immediate work is to:

1. define a weighted exposure for the three collision maps `(R_T+T)/2`, `2R_T-T`, and `2T-R_T`;
2. prove that exposure decreases or is released under shell descent, using geometric growth of `D/M` along each lineage;
3. retain first-appearance accounting for parent active edges and terminal targets;
4. separate ambient external roots from genuine holes and completion/rectangle witnesses;
5. resolve the CL-087 finite consistency audit before using its numerical pair-resource values;
6. avoid corrected-third-frontier and generation-six propagation.

The historical retained chain remains diagnostic only. Constant overlap bounds are permanently excluded by the unbounded reuse construction."""
    text = replace_section(text, old_start, protocol, active)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    base.main()
    patch_ledger()
    patch_program()
    patch_readme()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
