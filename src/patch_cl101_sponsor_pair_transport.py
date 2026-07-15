#!/usr/bin/env python3
"""Idempotently record the sponsor-pair transport frontier as CL-101."""
from __future__ import annotations

from pathlib import Path

PROGRAM = Path("docs/current-proof-program.md")
LEDGER = Path("docs/certainty-ledger.md")
HISTORY = Path("docs/research-decision-history.md")

ROW_100_PREFIX = "| CL-100 |"
ROW_101 = "| CL-101 | On the certified residual-sponsor `R_4 -> F_5` retained transition, `75247` distinct sponsor-core pair tokens are activated. Exact monotone transport terminates `72363` backward, `1513` direct, and `1371` residual. Activated initial union mass is `1181.622166508078...`; terminal target union mass is `970.461110516518...`; collision reuse is `710.942575247229...`. The family is concentrated in `74188` recursive latent pairs and `75055` sponsor-backbone resources. Of the activated pairs, `8725` have an in-parent completion and `66522` have parent-external completion status. | Exact finite sponsor-pair transport classification; fixed refined policy and retained quotient, no generation six. |"

PROGRAM_SECTION = r"""## Exact sponsor-pair transport frontier

The state-independent sponsor-pair transport theorem has now been evaluated on the certified residual-sponsor `R_4 -> F_5` retained frontier.

```text
activated distinct pair tokens = 75,247
inactive residual pairs         =     37
backward terminal pairs         = 72,363
direct terminal pairs           =  1,513
residual terminal pairs         =  1,371
```

The activated union mass is `1181.622166508078...`. Transport produces `40512` distinct terminal targets and `19593` collision targets, with

```text
terminal target union mass = 970.461110516518...
transport collision reuse  = 710.942575247229...
maximum target multiplicity = 32.
```

The active family is almost entirely sponsor-backbone latent capacity:

```text
recursive latent pairs   = 74,188
sponsor-backbone pairs   = 75,055
middle-fiber-only pairs  =     15.
```

Completion status splits as

```text
in-parent completion      =  8,725 pairs
parent-external completion = 66,522 pairs.
```

Thus the symbolic transport inequality is valid but not yet economical. The remaining payment is concentrated in:

1. backward obstruction geometry;
2. parent-external completions;
3. terminal-target collision reuse.

Residual termination and middle-fiber activation are minor on this exact frontier. No further retained generation is needed for the next test.

Primary reference: `docs/sponsor-pair-transport-frontier.md`.
"""

OLD_STATUS = (
    "The active program now has a scale-critical three-AP transfer row. First side, middle, "
    "and doubled preimages partition one parent target with capacities `1/2,1/4,1/4`; "
    "unbounded collisions transfer to lower-scale reference-gap and rectangle-aspect tokens. "
    "The remaining theorem is global first-appearance control of the critical collision excess, "
    "plus external-completion and terminal release."
)
NEW_STATUS = (
    "The active program now has a scale-critical three-AP transfer row and an exact sponsor-pair "
    "transport classification on the refined retained frontier. The unresolved mass is concentrated "
    "in backward obstruction targets, parent-external completions, and terminal-target collision "
    "reuse. The next theorem is a union-valued first-appearance payment for those terms, not another "
    "retained generation or fitted feature."
)

OLD_TARGETS = """1. Use full-color side, doubled-side, and middle edge-capacity tokens as the local payment source for completed activated pairs.
2. Classify sponsor-pair forward-transport targets on the certified refined fourth-to-fifth transition: direct, backward, residual, transport length, and target multiplicity.
3. Bound transport-target collision reuse by a first-appearance or union-valued edge ledger.
4. Split every parent-external completion into an ambient root outside the lineage and a genuine ambient hole; charge the two classes through provenance export and four-AP completion/rectangle witnesses respectively.
5. Quantify how much of activated pair mass uses in-parent completed edges versus parent-external completions.
6. Treat the corrected residual-sponsor second frontier as the active early finite obstruction; do not propagate it to a third frontier until a specific transfer inequality is declared.
7. Do not propagate generation six.

The desired whole-tree inequality must combine affine pair union, full-color edge capacity, terminal first appearance, and bounded completion/transport reuse. Another fitted feature or another retained generation is not an approved substitute.
"""
NEW_TARGETS = """1. Split the `72363` backward targets by in-parent completion versus parent-external completion, parent class, selected step, sponsor side, and first transport rank.
2. Partition the `66522` parent-external completions into ambient roots outside the parent lineage and genuine ambient holes.
3. Charge genuine holes through four-AP completion, rectangle-aspect, reference-gap, or cheap-extension exclusion tokens.
4. Put the `19593` terminal collision targets in a union-valued first-appearance ledger and bound the exact reuse mass `710.942575247229...`.
5. Exploit concentration in parent classes `93,82,77,65` and the positive sponsor side before attempting a general all-parent estimate.
6. Treat the corrected residual-sponsor second frontier as the active early finite obstruction; do not propagate it to a third frontier until a specific transfer inequality is declared.
7. Do not propagate generation six.

The desired whole-tree inequality must combine affine pair union, full-color edge capacity, terminal first appearance, and bounded backward/completion/collision reuse. Another fitted feature or another retained generation is not an approved substitute.
"""

LEDGER_REFS = (
    "- `docs/sponsor-pair-transport-frontier.md`;\n"
    "- `src/verify_sponsor_pair_transport_frontier.py`;\n"
    "- `data/sponsor_pair_transport_frontier_certificate_2026-07-14.txt`;\n"
)

BOTTLENECK = r"""# Open bottleneck OB-001: economical sponsor-pair activation transfer

Universal affine closure and pair-resource containment control distinct pair tokens across descendants. The remaining issue is economical activation: pay only the pair resources actually used by recursive retained output.

On the certified residual-sponsor `R_4 -> F_5` transition:

```text
activated pair union mass       = 1181.622166508078...
backward initial mass            =  760.440265648176...
direct initial mass              =  417.530512851610...
residual initial mass            =    3.651388008292...
terminal target union mass       =  970.461110516518...
transport collision reuse        =  710.942575247229...
```

The transport classification shows:

```text
backward targets           = 72,363
parent-external completions = 66,522
collision targets           = 19,593
maximum target multiplicity = 32.
```

The exact activation set is concentrated in recursive latent sponsor-backbone pairs. Residual termination and middle-fiber activation are negligible on this frontier.

The next theorem must combine:

1. full-color edge capacity for completed in-parent targets;
2. a first-appearance union ledger for terminal transport targets;
3. bounded collision reuse through rectangle-aspect or reference-gap tokens;
4. a split of external completions into ambient roots and genuine holes;
5. completion, rectangle, or cheap-extension exclusion credit for genuine holes.

The large positive slack in the raw set-valued transport inequality is not closure: it contains the unpaid backward and collision terms on the right-hand side. Generation six and additional fitted features remain blocked.
"""

HISTORY_INSERT = r"""### Exact sponsor-pair transport classification

The symbolic transport theorem was evaluated on the certified residual-sponsor `R_4 -> F_5` retained frontier. Of `75247` activated distinct pair tokens, `72363` terminate backward, `1513` direct, and `1371` residual. The activated family is almost entirely recursive latent sponsor-backbone capacity.

Transport produces `40512` distinct terminal target pairs and `19593` collision targets. The exact collision-reuse mass is `710.942575247229...`, with maximum target multiplicity `32`. Parent-external completion status occurs for `66522` activated pairs, compared with `8725` in-parent completions.

**Decision:** residual termination and middle-fiber activation are not the main frontier. The next proof effort must control backward geometry, external completions, and collision reuse with union-valued first-appearance tokens.

"""


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if OLD_STATUS in text:
        text = text.replace(OLD_STATUS, NEW_STATUS, 1)
    elif NEW_STATUS not in text:
        raise AssertionError("proof-program status anchor changed")

    marker = "\n---\n\n## 1. Foundation and recorded exact path"
    if PROGRAM_SECTION not in text:
        if marker not in text:
            raise AssertionError("proof-program foundation marker changed")
        text = text.replace(marker, "\n---\n\n" + PROGRAM_SECTION.rstrip() + marker, 1)

    if OLD_TARGETS in text:
        text = text.replace(OLD_TARGETS, NEW_TARGETS, 1)
    elif NEW_TARGETS not in text:
        raise AssertionError("proof-program approved-target block changed")
    PROGRAM.write_text(text, encoding="utf-8")


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    lines = text.splitlines()
    if ROW_101 not in lines:
        index = max(i for i, line in enumerate(lines) if line.startswith(ROW_100_PREFIX))
        lines.insert(index + 1, ROW_101)
    text = "\n".join(lines) + "\n"

    marker = "Primary latest references:\n\n"
    if LEDGER_REFS not in text:
        if marker not in text:
            raise AssertionError("certainty-ledger reference marker changed")
        text = text.replace(marker, marker + LEDGER_REFS, 1)

    start = text.index("# Open bottleneck")
    text = text[:start] + BOTTLENECK.rstrip() + "\n"
    LEDGER.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    anchor = (
        "The unresolved terms are transport collisions, parent-external ambient completions, "
        "genuine ambient holes, and reuse of edge capacity across retained branches.\n\n"
    )
    if HISTORY_INSERT not in text:
        if anchor not in text:
            raise AssertionError("decision-history sponsor-transport anchor changed")
        text = text.replace(anchor, anchor + HISTORY_INSERT, 1)
    HISTORY.write_text(text, encoding="utf-8")


def main() -> int:
    patch_program()
    patch_ledger()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
