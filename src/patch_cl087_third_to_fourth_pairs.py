#!/usr/bin/env python3
"""Record the exact R3-to-F4 pair-resource theorem as CL-087."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")
HISTORY = Path("docs/research-decision-history.md")
README = Path("README.md")

ROW = "| CL-087 | The certified `R_3 -> F_4` transition has 14/14 affine parents. Exact pair containment has zero missing current or latent resources. Parent pair multiplicity is at most 2 with repeated mass `7.711618836980...`; child multiplicity is at most 2 with repeated mass `0.133953757799...`. Both resource conventions contract: occurrence `2747.630136815823... < 7828.862146571999...`, union `2747.496183058024... < 7821.150527735019...`. | Exact finite affine pair-resource contraction theorem; fixed policy and quotient. |"

PROGRAM_INSERT = r"""
## Third-to-fourth pair-resource contraction

The affine pair-resource regime already holds before root uniqueness. All fourteen third recursive parents are affine, every fourth current or latent resource is contained, and pair multiplicity is at most two.

```text
R3 occurrence resource = 7828.862146571999...
F4 occurrence resource = 2747.630136815823...

R3 union resource      = 7821.150527735019...
F4 union resource      = 2747.496183058024...
```

Repeated-pair mass contracts from

```text
7.711618836980... -> 0.133953757799...
```

with zero missing resource tokens. Therefore `R_3 -> F_4` is removed from the obstruction frontier in both occurrence and union conventions.

Primary reference: `docs/third-to-fourth-pair-resource-contraction.md`.

---
"""

HISTORY_INSERT = r"""
### Third-to-fourth pair-resource contraction

The pair-resource test was moved one level earlier. All fourteen `R_3` recursive states are affine. Every `F_4` current or latent pair is contained in the parent resource universe. Pair multiplicity is at most two, and both occurrence and union potentials contract by more than `5000` units of exact pair mass.

The finite obstruction prefix is now restricted to `R_1 -> F_2` and `R_2 -> F_3`; the later transitions are closed.

"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW not in text:
        anchor = next(line for line in text.splitlines() if line.startswith("| CL-086 |"))
        text = text.replace(anchor, anchor + "\n" + ROW, 1)
    refs = (
        "- `docs/third-to-fourth-pair-resource-contraction.md`;\n"
        "- `src/verify_pair_resource_third_to_fourth.py`;\n"
        "- `data/pair_resource_third_to_fourth_certificate_2026-07-14.txt`;\n"
    )
    marker = "Primary latest references:\n\n"
    if refs not in text:
        text = text.replace(marker, marker + refs, 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if "## Third-to-fourth pair-resource contraction" not in text:
        anchor = "## 1. Foundation and recorded exact path"
        text = text.replace(anchor, PROGRAM_INSERT.strip() + "\n\n" + anchor, 1)
    PROGRAM.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "### Third-to-fourth pair-resource contraction" not in text:
        anchor = "\n**Decisions:**\n\n- current-generation multiplicity is not persistent reserve;"
        text = text.replace(
            anchor,
            "\n" + HISTORY_INSERT.strip() + "\n\n**Decisions:**\n\n"
            "- current-generation multiplicity is not persistent reserve;",
            1,
        )
    decision = "- `R_3 -> F_4` is closed in both occurrence and union pair-resource conventions; only the first two retained transitions remain as finite diagnostics;"
    if decision not in text:
        marker = "- the active theorem is economical pair activation, not another retained-child quotient or affine-purification lemma;"
        text = text.replace(marker, marker + "\n" + decision, 1)
    HISTORY.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    item = "18. exact occurrence- and union-valued pair-resource contraction from the third to fourth retained frontier."
    if item not in text:
        marker = "17. a symbolic affine-closure theorem and universal union-valued pair-resource containment for every coordinated deletion output."
        text = text.replace(marker, marker + "\n" + item, 1)
    reference = "- [`docs/third-to-fourth-pair-resource-contraction.md`](docs/third-to-fourth-pair-resource-contraction.md) — exact affine pair contraction before root uniqueness."
    if reference not in text:
        marker2 = "- [`docs/affine-output-closure-and-pair-containment.md`](docs/affine-output-closure-and-pair-containment.md) — universal affine descendant and pair-resource containment theorem."
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
