#!/usr/bin/env python3
"""Record the exact pair-resource partition as CL-085."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")
README = Path("README.md")
PAIR_NOTE = Path("docs/fifth-generation-pair-energy-bellman-row.md")

ROW = "| CL-085 | The complete fifth retained current-plus-latent pair resource set is an exact multiplicity-one subset of the fourth latent root-pair set. Counts: 372222 fourth resources, 107413 used fifth resources, 264809 unused; all 17 terminal current pairs, 1015 recursive current pairs, and 106381 recursive latent pairs come from fourth latent pairs, with zero child pair reuse. Exact resource identity: used `1586.466623468978...` plus unused `1158.927755372724...` equals parent `H(R_4)+J(R_4)=2745.394378841703...`. | Exact finite pair-resource containment and partition theorem; fixed policy and quotient. |"

PROGRAM_INSERT = r"""
## Exact pair-resource ownership at the fifth frontier

The scalar pair-energy row has been upgraded to an explicit set-valued resource partition.

The fourth recursive frontier contains

```text
1,717 current pairs
370,505 latent pairs
372,222 total pair resources.
```

The complete fifth retained family uses

```text
1,032 current pairs
106,381 recursive latent pairs
107,413 total pair resources.
```

Every fifth resource is a distinct fourth **latent** pair. No fifth resource uses a fourth current pair and no pair is paid twice.

```math
\boxed{
\operatorname{Used}(F_5)
+
\operatorname{Unused}(R_4\to F_5)
=
H(R_4)+J(R_4).
}
```

Exact masses:

```text
used   = 1586.466623468978...
unused = 1158.927755372724...
total  = 2745.394378841703...
```

This closes containment, terminal-recursive interaction, and repeated-payment semantics on the recorded transition.

Primary reference: `docs/fifth-generation-pair-resource-partition.md`.

---
"""

HISTORY_INSERT = r"""
### Pair-resource ownership certification

The fifth pair-energy row was strengthened from a numerical inequality to an exact token partition. All `107413` fifth current and latent resources are distinct members of the fourth latent pair universe. None uses a fourth current pair, and `264809` fourth resources remain unused.

The recorded transition therefore satisfies an exact set-valued conservation identity, not only a scalar bound. The open problem moves entirely to the earlier retained prefix where affine coverage and pair multiplicity have not yet been classified.

"""

PAIR_INSERT = r"""
## Resource-ownership strengthening

The companion theorem `docs/fifth-generation-pair-resource-partition.md` proves explicit token ownership:

```text
all 107,413 fifth current/latent resources
are distinct fourth latent root pairs;
no fourth current pair is used;
264,809 fourth resources remain unused.
```

Thus the Bellman inequality in this note is an exact pair-resource partition, not merely a true comparison of two rational numbers.

---
"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-084 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = (
        "- `docs/fifth-generation-pair-resource-partition.md`;\n"
        "- `src/verify_pair_resource_ownership.py`;\n"
        "- `data/pair_resource_ownership_certificate_2026-07-14.txt`;\n"
    )
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## Exact pair-resource ownership at the fifth frontier" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "### Pair-resource ownership certification" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + HISTORY_INSERT.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decision = "- the fifth-frontier pair row has exact token ownership and no repeated payment; future work should reuse this resource schema rather than fit scalar surrogates;"
    if decision not in text:
        marker = "- generation six is unnecessary until earlier-generation affine entry and pair reuse are resolved;"
        text = text.replace(marker, marker + "\n" + decision, 1)
    HISTORY.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    item = "16. an exact pair-resource partition proving containment and zero repeated payment at the fifth frontier."
    if item not in text:
        marker = "15. an exact pair-energy Bellman row closing the recorded fourth-to-fifth retained expansion."
        text = text.replace(marker, marker + "\n" + item, 1)
    reference = "- [`docs/fifth-generation-pair-resource-partition.md`](docs/fifth-generation-pair-resource-partition.md) — explicit fifth-child to fourth-pair ownership and unused-capacity theorem."
    if reference not in text:
        marker2 = "- [`docs/fifth-generation-pair-energy-bellman-row.md`](docs/fifth-generation-pair-energy-bellman-row.md) — exact affine pair-energy Bellman row at the first failing retained transition."
        text = text.replace(marker2, marker2 + "\n" + reference, 1)
    README.write_text(text, encoding="utf-8")


def patch_pair_note() -> None:
    text = PAIR_NOTE.read_text(encoding="utf-8")
    if "## Resource-ownership strengthening" not in text:
        anchor = "## 1. Pair energy"
        text = text.replace(anchor, PAIR_INSERT.strip() + "\n\n" + anchor, 1)
    PAIR_NOTE.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    patch_history()
    patch_readme()
    patch_pair_note()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
