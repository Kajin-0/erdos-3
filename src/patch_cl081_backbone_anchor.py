#!/usr/bin/env python3
"""Idempotently record CL-081 and the backbone-anchor research pivot."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")

ROW_081 = "| CL-081 | At the certified fourth-to-fifth baseline transition, all `1015` recursively surviving roots are carried by minimum-translation backbone occurrences and none by middle fibers. The twelve parent minima are exactly the twelve roots with no raw descendant output. Surviving shell drops are `1,2,5,7,9,10`; classes `77,68,24` carry `87.7945%`–`87.7946%` of gain. Aggregate full translation reserve is `9.928706884742...`, retained gain is `1.816777911848...`, and minimum-anchor release is only `0.364729899662...`. | Exact finite backbone-anchor transfer theorem; fixed policy and retention. |"

PROGRAM_INSERT = r"""
## Latest exact refinement: backbone-anchor transfer

The fourth-to-fifth survivor classification is complete for the certified baseline transition:

```text
surviving roots              = 1,015
surviving backbone roots     = 1,015
surviving middle-fiber roots = 0
minimum-anchor roots         = 12
minimum anchors with no raw output = 12
```

For a recursive parent state `S` with `m=min(S)`, the exact prospective translation reserve is

```math
A(S)
=
\sum_{u\in S,\ u>m}
\left(
\frac1{u-m}-\frac1u
\right).
```

Every retained survivor gain is the harmonic measure of an anchor-survivor interval `(u-m,u]`. The aggregate baseline values are

```text
sum A(S)                 = 9.928706884742...
retained survivor gain   = 1.816777911848...
minimum-anchor release   = 0.364729899662...
```

Thus scalar anchor mass is not complete payment. The missing state must control provenance-labeled anchor-survivor intervals, their reuse, and the release created when they terminate or are removed.

Primary reference: `docs/backbone-anchor-root-transfer.md`.

---
"""

HISTORY_INSERT = r"""
### Backbone-anchor refinement

The exact source classification of the first failing transition is now complete. All `1015` recursively surviving roots continue through minimum-translation backbone occurrences; no middle-fiber root survives. The twelve minimum-anchor roots are exactly the twelve roots with no raw descendant output.

For each parent state `S`, `m=min(S)`, the full prospective translation gain is

```math
A(S)
=
\sum_{u>m}
\left(
\frac1{u-m}-\frac1u
\right).
```

Across the twelve parents,

```text
full translation reserve = 9.928706884742...
retained survivor gain    = 1.816777911848...
minimum-anchor release    = 0.364729899662...
```

Six parent states expand and six contract. Classes `77`, `68`, and `24` carry `87.7945%`–`87.7946%` of survivor gain. The correct local object is therefore a provenance-labeled anchor-survivor interval, not scalar minimum-anchor mass.

"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW_081 not in text:
        anchor = next(
            line for line in text.splitlines() if line.startswith("| CL-080 |")
        )
        text = text.replace(anchor, anchor + "\n" + ROW_081, 1)

    reference_anchor = "Primary latest references:\n\n"
    references = (
        "- `docs/backbone-anchor-root-transfer.md`;\n"
        "- `src/verify_root_lineage_transfer_classification.py`;\n"
        "- `src/verify_backbone_anchor_transfer.py`;\n"
    )
    if references not in text:
        text = text.replace(reference_anchor, reference_anchor + references, 1)

    prohibited = "43. scalar minimum-anchor mass `1/min(S)` as complete payment for all enabled backbone intervals."
    if prohibited not in text:
        marker = "42. generation-six propagation without a predeclared conceptual test."
        text = text.replace(marker, marker + "\n" + prohibited, 1)

    old = (
        "Generation six is blocked until such a lemma exists. The next concrete tasks "
        "are to classify survivor scale gain by source/shell/immediate provenance, "
        "attach terminalized roots to first-appearance `(u,p,i)` tokens, and determine "
        "what arithmetic credit is created by the 685 dropped lineages."
    )
    new = (
        "The source and shell classification is now complete on the baseline transition: "
        "all `1015` survivors are backbone translations, the twelve minimum anchors have "
        "no raw output, and three parent classes carry nearly `88%` of gain. Generation "
        "six remains blocked. The next concrete target is a state-independent transfer "
        "law for provenance-labeled anchor-survivor intervals `(u-min(S),u]`, coupled to "
        "first-appearance terminal credit and a provenance-valid classification of the "
        "`673` dropped roots that generated raw descendants."
    )
    if old in text:
        text = text.replace(old, new, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## Latest exact refinement: backbone-anchor transfer" not in text:
        anchor = "---\n\n## 1. Foundation and recorded exact path"
        text = text.replace(
            anchor,
            PROGRAM_INSERT.strip() + "\n\n## 1. Foundation and recorded exact path",
            1,
        )

    old_targets = """1. Classify the certified survivor scale gain by parent state, source type, shell, and immediate provenance.
2. Prove a reserve-transfer lemma that charges lost or created scale capacity to terminalization, discarded lineages, or arithmetic obstruction.
3. Attach the 17 terminalized roots injectively to first-appearance `(u,p,i)` terminal tokens.
4. Test whether the 685 dropped lineages create completion, rectangle, or future-extension exclusion credit.
5. Define cumulative ancestor-path capacity only after the transfer decomposition identifies its conserved quantity.
6. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    new_targets = """1. Define a provenance-labeled anchor-survivor interval state for `(u-min(S),u]` and state exactly when that interval is created, retained, released, or reused.
2. Test the exact translation reserve `A(S)=sum_{u>min(S)}(1/(u-min(S))-1/u)` on the existing four transitions; record either a coefficient theorem or the smallest exact no-go subsystem.
3. Attach the 17 terminalized roots injectively to first-appearance `(u,p,i)` terminal tokens.
4. Refine the 673 dropped roots with raw descendants by provenance, distinguishing valid retained coverage from numerical coverage by unrelated lineages.
5. Prove a bounded-reuse or obstruction-export lemma for anchor-survivor intervals.
6. Test any proposed lemma on the existing four transitions before adding another generation.
"""
    if old_targets in text:
        text = text.replace(old_targets, new_targets, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "### Backbone-anchor refinement" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + HISTORY_INSERT.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decision = "- the baseline failing survivor family is backbone-only, and scalar minimum-anchor release is not sufficient payment for enabled translation intervals;"
    if decision not in text:
        marker = "- the missing resource is cumulative ancestor-path scale capacity plus terminal/drop/obstruction release;"
        text = text.replace(marker, marker + "\n" + decision, 1)

    old = """1. classify survivor scale gain by parent state, source type, shell, and immediate provenance;
2. attach the `17` terminalized roots injectively to first-appearance `(u,p,i)` tokens;
3. determine what completion, rectangle, or future-extension exclusion is created by the `685` dropped lineages;
4. formulate a transfer lemma before propagating another generation.
"""
    new = """1. define provenance-labeled anchor-survivor interval state and its one-step transfer semantics;
2. test the exact minimum-translation reserve on the four existing transitions;
3. attach the `17` terminalized roots injectively to first-appearance `(u,p,i)` tokens;
4. distinguish provenance-valid release from numerical coverage among the `673` dropped roots with raw descendants;
5. formulate a bounded-reuse or obstruction-export lemma before propagating another generation.
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
