#!/usr/bin/env python3
"""Record CL-089 through CL-092 and replace the stale retained frontier.

The patch is idempotent and changes only authoritative overview documents.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CL088 = "| CL-088 | Splitting every `R_4 -> F_5` minimum-backbone shell by residual versus deleted-sponsor root preserves the exact raw support union (`1489` labels), point-occurrence count (`2972`), and harmonic occurrence mass (`25.589294609269...`). Under the same retained quotient, recursive points fall `1015 -> 864`, recursive mass falls by `0.168809631114...`, latent pair occurrences fall by `32190`, and union pair-resource mass falls by `404.536054734914...`; terminal mass rises by `0.369683464666...`. | Exact finite residual-sponsor backbone refinement theorem; fixed policy and quotient, no generation six. |"
CL089 = "| CL-089 | A retained three-AP-free parent has no recursive descendants. The certified first retained family actually splits into 6 terminal states with 52 points and mass `0.127088543982...`, and 15 recursive states with 11701 points and mass `0.158733022746...`. Stopping the terminal parents changes the second retained optimum: ordinary recursive mass is `0.416597543898...` (`2.624517171606...` times the recursive parent mass); the residual-sponsor refinement reduces it to `0.322355467082...` (`2.030802800232...`), a `22.6218512798%` reduction. | Elementary terminal-stopping theorem plus independently certified finite correction. The historical 21-parent second frontier is diagnostic only. |"
CL090 = "| CL-090 | Retaining all three middle colors `chi(s)=v_2(s)-v_3(s) mod 3`, rather than one maximizing color, is valid. Every three-AP belongs to exactly one parity-selected side child and one middle-color child; every child is four-AP-free with pairwise-disjoint first three dilates. Hence `sum_children H(C)=2 L(B)>=4H(B)-4r_3(N)/N`. Exhaustive verification covered all 2233 four-AP-free subsets of `[1,12]` and 3174 three-AP occurrences. | Symbolic full-color branching theorem plus exhaustive finite regression. |"
CL091 = "| CL-091 | Full-color branching carries an exact pair-edge capacity: for each three-AP of step `d`, the side token `d`, middle token `d`, and doubled side reserve `2d` biject weight-preservingly to its two adjacent pair edges and outer pair edge. Consequently `sum_side(H(C)+H(2C))+sum_middle H(C)=(5/2)L(B)`, and every distinct completed in-parent target pair packs into these scale-descending edge-capacity tokens. | Symbolic pair-edge capacity identity; whole-tree first-appearance and reuse remain open. |"
CL092 = "| CL-092 | Every activated sponsor pair admits monotone forward transport: pair weight is nondecreasing and minimum deletion rank strictly increases until a direct selected edge, backward obstruction, or residual pair is reached. For a residual minimum `a`, the star pair `{a,s}` is backward exactly for even `v_2(q_s)`, and its backward mass is bounded by `2 sum_j 1/q_j` plus an injective completion-obstruction term. Parent-external completions must be split into ambient roots outside the lineage and genuine ambient holes. | Symbolic sponsor-pair transport, parity, and completion-charge theorems. |"

CURRENT_INSERT = r"""## Corrected first retained frontier

Terminal stopping is structural. A retained state with no three-term progression selects no deletion action, has no middle fibers, and emits only three-AP-free translated backbone shells. It must be recorded once as terminal and never propagated recursively.

The certified first retained family is therefore

```text
all states        = 21, points = 11,753, mass = 0.285821566728...
terminal states   =  6, points =     52, mass = 0.127088543982...
recursive states  = 15, points = 11,701, mass = 0.158733022746...
```

The six terminal parent classes are

```text
0, 1, 2, 8, 74, 86.
```

Recomputing the second frontier from only the fifteen recursive parents gives

```text
ordinary corrected F2: 27 states, 7,923 points
  terminal: 12 states, 38 points, mass 1.478795226105...
  recursive: 15 states, 7,885 points, mass 0.416597543898...

residual-sponsor F2: 45 states, 8,164 points
  terminal: 33 states, 944 points, mass 1.601039076668...
  recursive: 12 states, 7,220 points, mass 0.322355467082...
```

Thus the corrected ordinary recursive ratio is `2.624517171606...`, while residual-sponsor refinement lowers it to `2.030802800232...`, a `22.6218512798%` reduction. The historical second-to-fifth chain remains an exact finite diagnostic of the old construction, but it is not the continuation of the terminal-stopped tree.

Primary references:

- `docs/terminal-parent-stopping-lemma.md`;
- `data/first_frontier_terminal_correction_certificate.txt`;
- `src/verify_first_frontier_terminal_correction.py`.

---

## Full-color branching and pair-edge capacity

The middle-role factor-three loss was artificial. Split every middle star into all three classes

```math
\chi(s)=v_2(s)-v_3(s)\pmod3
```

and emit all nonempty color children. Every progression then has exactly two child memberships:

```text
one parity-selected side child;
one uniquely colored middle child.
```

Every child is four-AP-free and has pairwise-disjoint first three dilates. Therefore

```math
\boxed{
\sum_{\rm children}H(C)
=
2\mathcal L(B)
\ge
4H(B)-4\frac{r_3(N)}N.
}
```

The side token `d`, doubled side reserve `2d`, and middle token `d` correspond exactly to the three pair edges of one progression. Hence

```math
\boxed{
\sum_{\rm side}\left(H(C)+H(2C)\right)
+
\sum_{\rm middle}H(C)
=
\frac52\mathcal L(B).
}
```

This closes the local coefficient gap for distinct completed in-parent pair targets. The whole-tree obligations are now edge-capacity first appearance, transport-target collision reuse, parent-external ambient completions, and genuine ambient holes.

Primary references:

- `docs/full-color-coordinated-branching.md`;
- `data/full_color_coordinated_branching_summary.txt`;
- `docs/full-color-pair-edge-capacity.md`;
- `docs/sponsor-pair-forward-transport.md`;
- `docs/terminal-pair-ap-witness-bound.md`.

---

"""

OLD_TABLE = """The resulting certified frontier is:

| retained level | total states | total points | terminal states | terminal points | recursive states | recursive points |
|---|---:|---:|---:|---:|---:|---:|
| first | 21 | 11,753 | — | — | 21 | 11,753 |
| second | 27 | 7,925 | 13 | 43 | 14 | 7,882 |
| third | 32 | 4,899 | 18 | 110 | 14 | 4,789 |
| fourth | 23 | 1,794 | 11 | 77 | 12 | 1,717 |
| fifth | 21 | 1,032 | 8 | 17 | 13 | 1,015 |

Every recorded family is point-disjoint within its generation. The baseline retention optimum is unique through generation five. Nearby policy tests include two nonunique components, but their tied maximum-harmonic optima have identical recursive mass.

This quotient is a rigorous finite test object. It is not proved globally optimal or canonical."""

NEW_TABLE = """Terminal stopping changes the first retained transition. The active certified frontiers are:

| frontier | total states | total points | terminal states | terminal points | recursive states | recursive points | status |
|---|---:|---:|---:|---:|---:|---:|---|
| first | 21 | 11,753 | 6 | 52 | 15 | 11,701 | active parent frontier |
| corrected ordinary second | 27 | 7,923 | 12 | 38 | 15 | 7,885 | active exact comparison |
| corrected residual-sponsor second | 45 | 8,164 | 33 | 944 | 12 | 7,220 | active refined frontier |

The earlier construction propagated all twenty-one first states, including six terminal parents. Its exact diagnostic continuation is:

| historical retained level | total states | total points | terminal states | terminal points | recursive states | recursive points |
|---|---:|---:|---:|---:|---:|---:|
| second | 27 | 7,925 | 13 | 43 | 14 | 7,882 |
| third | 32 | 4,899 | 18 | 110 | 14 | 4,789 |
| fourth | 23 | 1,794 | 11 | 77 | 12 | 1,717 |
| fifth | 21 | 1,032 | 8 | 17 | 13 | 1,015 |

These historical families remain point-disjoint exact finite test objects, and all theorems stated specifically about their recorded transitions remain valid. They must not be interpreted as the terminal-stopped recursive tree or spliced onto either corrected second frontier."""

OLD_MASS = """Let `H_g^rec` denote recursively continuing retained harmonic mass. The four recorded ratios are:

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

NEW_MASS = """Let `H_1^rec` denote the mass of the fifteen genuinely recursive first-frontier states. The corrected first transition satisfies

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

NEW_TARGETS = """## 9. Approved next targets

1. Use full-color side, doubled-side, and middle edge-capacity tokens as the local payment source for completed activated pairs.
2. Classify sponsor-pair forward-transport targets on the certified refined fourth-to-fifth transition: direct, backward, residual, transport length, and target multiplicity.
3. Bound transport-target collision reuse by a first-appearance or union-valued edge ledger.
4. Split every parent-external completion into an ambient root outside the lineage and a genuine ambient hole; charge the two classes through provenance export and four-AP completion/rectangle witnesses respectively.
5. Quantify how much of activated pair mass uses in-parent completed edges versus parent-external completions.
6. Treat the corrected residual-sponsor second frontier as the active early finite obstruction; do not propagate it to a third frontier until a specific transfer inequality is declared.
7. Do not propagate generation six.

The desired whole-tree inequality must combine affine pair union, full-color edge capacity, terminal first appearance, and bounded completion/transport reuse. Another fitted feature or another retained generation is not an approved substitute."""

README_ACTIVE = """A rigorous finite retained quotient exists, but terminal stopping changes its active first transition. The first family contains six terminal states carrying `44.4642947826%` of its mass and fifteen recursive states. Recomputing from only those recursive parents gives a corrected ordinary second recursive ratio `2.624517171606...`; residual-sponsor refinement lowers it to `2.030802800232...`.

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

DECISION_INSERT = r"""### Terminal-parent stopping correction

The first retained family was historically propagated wholesale, but exact classification shows six of its twenty-one states are already three-AP-free. A terminal parent selects no action, has no middle fiber, and can emit only terminal translated-backbone shells. Propagating it is semantically invalid as recursive continuation.

The independent correction certificate gives:

```text
F1 terminal:  6 states,    52 points, mass 0.127088543982...
F1 recursive: 15 states, 11701 points, mass 0.158733022746...
```

Stopping those parents changes the maximum-harmonic second optimum. Ordinary corrected recursive mass is `0.416597543898...`; residual-sponsor refinement lowers it to `0.322355467082...`. The historical `0.937...` ratio is not a recursive contraction theorem.

### Full-color branching correction

The middle role need not discard two valuation colors. Emitting all three classes `v_2-v_3 mod 3` preserves every middle incidence while every color child remains four-AP-free with disjoint first three dilates. Together with parity-selected side children, every three-AP has exactly two memberships and total child mass is exactly `2 L(B)`, giving raw branching factor `4` up to Roth error.

An exhaustive regression checked all `2233` four-AP-free subsets of `[1,12]`, including `3174` three-AP occurrences.

### Sponsor transport and edge capacity

Every activated sponsor pair has a monotone deletion-rank transport to a direct edge, backward obstruction, or residual target. Full-color branching supplies an exact three-edge dictionary: side `d`, doubled side `2d`, and middle `d` carry the two adjacent and one outer pair edge of each progression. Completed in-parent distinct targets therefore have exact child-located capacity.

The unresolved terms are transport collisions, parent-external ambient completions, genuine ambient holes, and reuse of edge capacity across retained branches.

"""


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise AssertionError(f"missing {label} marker")
    return text.replace(old, new, 1)


def replace_heading_section(text: str, heading: str, next_heading: str, block: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise AssertionError(f"cannot locate section {heading!r}")
    return text[:start] + block.rstrip() + "\n\n---\n\n" + text[end:]


def patch_ledger() -> None:
    path = ROOT / "docs/certainty-ledger.md"
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line not in {CL089, CL090, CL091, CL092}]
    text = "\n".join(lines) + "\n"
    if CL088 not in text:
        raise AssertionError("missing CL-088 ledger marker")
    additions = "\n".join((CL089, CL090, CL091, CL092)) + "\n"
    text = text.replace(CL088 + "\n", CL088 + "\n" + additions, 1)
    marker = "Primary latest references:\n\n"
    refs = (
        "- `data/first_frontier_terminal_correction_certificate.txt`;\n"
        "- `src/verify_first_frontier_terminal_correction.py`;\n"
        "- `docs/full-color-coordinated-branching.md`;\n"
        "- `data/full_color_coordinated_branching_summary.txt`;\n"
        "- `docs/full-color-pair-edge-capacity.md`;\n"
        "- `docs/sponsor-pair-forward-transport.md`;\n"
        "- `docs/residual-minimum-star-completion-charge.md`;\n"
    )
    for line in refs.splitlines():
        text = text.replace(line + "\n", "")
    if marker not in text:
        raise AssertionError("missing latest-reference marker")
    text = text.replace(marker, marker + refs, 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = path.read_text(encoding="utf-8")
    heading = "## Corrected first retained frontier"
    if heading in text:
        start = text.index(heading)
        end = text.index("## Latest exact refinement: backbone-anchor transfer", start)
        text = text[:start] + CURRENT_INSERT + text[end:]
    else:
        marker = "## Latest exact refinement: backbone-anchor transfer"
        if marker not in text:
            raise AssertionError("missing current-program insertion marker")
        text = text.replace(marker, CURRENT_INSERT + marker, 1)
    text = replace_once(text, OLD_TABLE, NEW_TABLE, "retained table")
    text = replace_once(text, OLD_MASS, NEW_MASS, "recursive mass section")
    text = replace_heading_section(
        text,
        "## 9. Approved next targets",
        "## 10. Stop list",
        NEW_TARGETS,
    )
    old_status = "The project is no longer searching for another finite-depth fitted feature or a new overlap quotient. Affine closure and pair-token containment now give exact whole-tree no-double-payment semantics. The active theorem target is an economical pair-activation or multiscale exposure bound that avoids paying the full latent root-pair energy of the initial dyadic block."
    new_status = "The active program combines terminal stopping, affine union-valued pair tokens, full-color role branching, and sponsor-pair transport. The local coefficient problem is closed for completed in-parent pair edges; the remaining theorem must bound transport collisions, parent-external completions, genuine ambient holes, and cross-branch first appearance."
    text = text.replace(old_status, new_status)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    items = [
        "20. an exact terminal-stopping correction showing that six first-frontier states were terminal and that the corrected recursive second frontier expands;",
        "21. a residual-sponsor corrected second frontier reducing recursive mass by `22.6218512798%`;",
        "22. a full-color coordinated branching theorem with exact raw factor `4` and exactly two child memberships per three-AP;",
        "23. an exact side/middle/doubled-side pair-edge capacity dictionary and monotone sponsor-pair transport theorem.",
    ]
    lines = [line for line in text.splitlines() if line not in items]
    text = "\n".join(lines) + "\n"
    marker = "19. a certified residual-sponsor backbone split that terminalizes translated residual roots and reduces the fifth recursive pair-resource load without changing raw support or harmonic occurrence mass.\n"
    if marker not in text:
        raise AssertionError("missing README claim marker")
    text = text.replace(marker, marker + "\n".join(items) + "\n", 1)
    start = text.find("A rigorous finite retained quotient now exists")
    end = text.find("## Start here", start)
    if start < 0 or end < 0:
        raise AssertionError("cannot locate README active theorem")
    text = text[:start] + README_ACTIVE.rstrip() + "\n\n" + text[end:]
    link_marker = "- [`docs/residual-sponsor-backbone-refinement.md`](docs/residual-sponsor-backbone-refinement.md) — symbolic and exact finite sponsor-core refinement of the minimum backbone.\n"
    links = (
        "- [`docs/terminal-parent-stopping-lemma.md`](docs/terminal-parent-stopping-lemma.md) — structural terminal stopping and corrected first-frontier semantics.\n"
        "- [`docs/full-color-coordinated-branching.md`](docs/full-color-coordinated-branching.md) — exact factor-four role-color branching theorem.\n"
        "- [`docs/full-color-pair-edge-capacity.md`](docs/full-color-pair-edge-capacity.md) — exact pair-edge capacity dictionary.\n"
        "- [`docs/sponsor-pair-forward-transport.md`](docs/sponsor-pair-forward-transport.md) — monotone activated-pair transport theorem.\n"
    )
    for line in links.splitlines():
        text = text.replace(line + "\n", "")
    if link_marker not in text:
        raise AssertionError("missing README link marker")
    text = text.replace(link_marker, link_marker + links, 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_history() -> None:
    path = ROOT / "docs/research-decision-history.md"
    text = path.read_text(encoding="utf-8")
    for heading in (
        "### Terminal-parent stopping correction",
        "### Full-color branching correction",
        "### Sponsor transport and edge capacity",
    ):
        if heading in text:
            start = text.index(heading)
            end = text.index("**Decisions:**", start)
            text = text[:start] + text[end:]
            break
    marker = "**Decisions:**\n"
    position = text.rfind(marker, 0, text.find("## 11. Permanent stop list"))
    if position < 0:
        raise AssertionError("missing decision insertion marker")
    text = text[:position] + DECISION_INSERT + text[position:]
    old_active_start = "## 12. Active closing target"
    old_protocol = "## 13. Documentation protocol"
    new_active = r"""## 12. Active closing target

The active transfer architecture is

```text
activated affine pair
-> monotone sponsor transport
-> distinct terminal pair target + collision reuse
-> full-color progression-edge capacity
-> external ambient completion or genuine-hole obstruction export.
```

The immediate work is to:

1. classify direct, backward, and residual transport targets on the refined certified fourth-to-fifth frontier;
2. measure target multiplicity and first-appearance collision mass;
3. distinguish in-parent, ambient-external, and genuinely absent completions;
4. pack completed targets into side, doubled-side, and middle edge capacities;
5. connect genuine holes to maximal four-AP-free completion witnesses and rectangle transport;
6. use the corrected residual-sponsor second frontier only as a finite obstruction test, not as an invitation to propagate another generation.

The historical second-to-fifth chain is retained as a diagnostic object. The active recursive tree starts from fifteen first-frontier parents. Generation six and a corrected third frontier remain blocked until a state-independent bounded-reuse inequality is fixed."""
    text = replace_heading_section(text, old_active_start, old_protocol, new_active)
    decisions = [
        "- terminal parents must stop immediately and may never be reintroduced as recursive production;",
        "- the historical second-to-fifth chain is an exact diagnostic, not the terminal-stopped recursive tree;",
        "- all three middle valuation colors are retained; choosing one color discards valid production without reducing per-progression multiplicity;",
        "- completed in-parent pair targets use explicit full-color edge capacity rather than prepaid full latent pair energy;",
        "- parent-external ambient roots and genuine ambient holes are different obstruction classes and must not be conflated;",
    ]
    decision_marker = "- a new feature is admissible only with a transition recurrence, bounded-reuse interpretation, and telescoping role.\n"
    for line in decisions:
        text = text.replace(line + "\n", "")
    if decision_marker not in text:
        raise AssertionError("missing decision bullet marker")
    text = text.replace(decision_marker, decision_marker + "\n".join(decisions) + "\n", 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_readme()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
