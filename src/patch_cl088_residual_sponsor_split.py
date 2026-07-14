#!/usr/bin/env python3
"""Canonicalize and record the certified residual/sponsor refinement as CL-088.

This patcher is intentionally idempotent. It removes every prior copy of each
CL-088 insertion before writing exactly one canonical copy.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CL087 = "| CL-087 | The certified `R_3 -> F_4` transition has 14/14 affine parents. Exact pair containment has zero missing current or latent resources. Parent pair multiplicity is at most 2 with repeated mass `7.711618836980...`; child multiplicity is at most 2 with repeated mass `0.133953757799...`. Both resource conventions contract: occurrence `2747.630136815823... < 7828.862146571999...`, union `2747.496183058024... < 7821.150527735019...`. | Exact finite affine pair-resource contraction theorem; fixed policy and quotient. |"
CL088 = "| CL-088 | Splitting every `R_4 -> F_5` minimum-backbone shell by residual versus deleted-sponsor root preserves the exact raw support union (`1489` labels), point-occurrence count (`2972`), and harmonic occurrence mass (`25.589294609269...`). Under the same retained quotient, recursive points fall `1015 -> 864`, recursive mass falls by `0.168809631114...`, latent pair occurrences fall by `32190`, and union pair-resource mass falls by `404.536054734914...`; terminal mass rises by `0.369683464666...`. | Exact finite residual-sponsor backbone refinement theorem; fixed policy and quotient, no generation six. |"

REF_LINES = (
    "- `docs/residual-sponsor-backbone-refinement.md`;",
    "- `src/verify_residual_sponsor_backbone_split.py`;",
    "- `data/residual_sponsor_backbone_split_certificate_2026-07-14.txt`;",
)

CURRENT_BLOCK = r"""---

## Certified residual-sponsor backbone refinement

A completed deletion schedule partitions each affine parent root set as

```math
P=Q\sqcup\Sigma,
```

where `Q` is the three-AP-free residual and `Sigma` is the deleted sponsor core. Splitting the minimum backbone before dyadic shelling into translated residual-root and sponsor-root pieces preserves the complete raw numerical and harmonic output. Every residual-root shell is terminal.

On the certified `R_4 -> F_5` transition the exact split preserves

```text
raw support union          = 1,489
raw point occurrences      = 2,972
raw harmonic occurrence    = 25.589294609269...
```

while changing the retained recursive frontier by

```text
recursive points           1,015 -> 864
recursive harmonic mass    2.042771729559... -> 1.873962098445...
latent pair occurrences    106,381 -> 74,191
union pair-resource mass   1,586.466623468978... -> 1,181.930568734065...
```

Terminal mass rises by `0.369683464666...`; recursive mass falls by `0.168809631114...`. The refinement therefore exposes additional terminal support without importing a new unshifted residual output and removes `404.536054734914...` of union-valued continuing pair capacity.

The active analytical object is now the sponsor core. Future transfer inequalities should charge

```math
\{(a,s):s\in\Sigma\}
\cup
\binom\Sigma2
```

to selected-progression incidence, terminal first appearance, or arithmetic obstruction export, rather than prepaying all pairs in the original root set.

Primary reference: `docs/residual-sponsor-backbone-refinement.md`.

---

"""
FOUNDATION = "## 1. Foundation and recorded exact path"

README_ITEM18 = "18. exact occurrence- and union-valued pair-resource contraction from the third to fourth retained frontier."
README_ITEM19 = "19. a certified residual-sponsor backbone split that terminalizes translated residual roots and reduces the fifth recursive pair-resource load without changing raw support or harmonic occurrence mass."
README_LINK_MARKER = "- [`docs/third-to-fourth-pair-resource-contraction.md`](docs/third-to-fourth-pair-resource-contraction.md) — exact affine pair contraction before root uniqueness."
README_LINK = "- [`docs/residual-sponsor-backbone-refinement.md`](docs/residual-sponsor-backbone-refinement.md) — symbolic and exact finite sponsor-core refinement of the minimum backbone."
README_ACTIVE_OLD = "Affine closure and union-valued pair containment now control reuse exactly across the whole retained tree. The decisive missing theorem is an economical activation or multiscale exposure bound for the pair tokens actually used."
README_ACTIVE_NEW = "Affine closure and union-valued pair containment now control reuse exactly across the whole retained tree. The certified residual-sponsor split further terminalizes translated residual roots, so the continuing resource universe is concentrated on deleted sponsor roots. The decisive missing theorem is an economical activation or multiscale exposure bound for sponsor-core pair tokens."

DECISION_LEAD = "The finite obstruction prefix is now restricted to `R_1 -> F_2` and `R_2 -> F_3`; the later transitions are closed."
DECISION_BLOCK = """### Residual-sponsor backbone refinement

The first workflow attempt did not test the mathematics: it imported a nonexistent module, and an unsafe named `git add -A` pathspec masked that exception. After the repository-wide workflow hardening pass, the original error was preserved and the probe was rewritten against the certified lexicographic propagation APIs.

The corrected exact test partitions only the already-existing translated minimum backbone. It inserts no unshifted residual output and preserves raw support, point occurrences, and harmonic occurrence mass exactly. Under the same retained quotient, the residual-root shells are terminal, recursive points fall by `151`, recursive mass falls by `0.168809631114...`, and union pair-resource mass falls by `404.536054734914...`.

This closes the finite question of whether the symbolic residual-sponsor split is useful on the recorded failing transition. It is strongly favorable. The remaining analytical target is a state-independent sponsor-core activation bound.

"""
OLD_TASKS = """The next exact work is to:

1. certify affine root references and exact pivot updates on the existing retained frontier;
2. test the exact minimum-translation reserve on the four existing transitions;
3. quantify entering pair energy and identify a noncircular payment source;
4. prove affine entry/purification or charge non-affine recursive output to terminal or arithmetic obstruction;
5. distinguish provenance-valid release from numerical coverage among the `673` dropped roots with raw descendants;
6. formulate the resulting transfer lemma before propagating another generation.

No current theorem closes this gap. Generation six and further feature fitting are explicitly deferred."""
NEW_TASKS = """The next exact and analytical work is to:

1. measure sponsor-core size, selected-progression incidence, and pair-energy exposure on the first two retained transitions;
2. prove a weighted bound for the activated star pairs `(a,s)` and internal sponsor pairs `binom(Sigma,2)`;
3. charge popular or short sponsor differences to terminal first appearance, completion support, rectangle transport, or cheap-extension exclusion;
4. determine whether policy selection can minimize sponsor-core pair energy while preserving the one-generation harmonic lower bound;
5. formulate the sponsor-core transfer lemma before propagating another generation.

No current theorem pays for sponsor-core activation from the original root at all scales. Generation six and further feature fitting remain explicitly deferred."""

CERTIFIED_SECTION = """---

## 11. Certified retained-frontier result

The exact `R_4 -> F_5` probe verifies the symbolic refinement under the recorded lexicographic policy and maximum-harmonic same-shell retained quotient.

It inserts no unshifted residual output and preserves exactly:

```text
raw support union       = 1,489 labels
raw point occurrences   = 2,972
raw harmonic mass       = 25.589294609269...
```

The retained comparison is:

| quantity | baseline | refined split | delta |
|---|---:|---:|---:|
| terminal points | 17 | 232 | +215 |
| recursive points | 1,015 | 864 | -151 |
| terminal mass | 2.043863226048 | 2.413546690714 | +0.369683464666 |
| recursive mass | 2.042771729559 | 1.873962098445 | -0.168809631114 |
| latent pair occurrences | 106,381 | 74,191 | -32,190 |
| union pair-resource mass | 1,586.466623468978 | 1,181.930568734065 | -404.536054734914 |

Fifteen retained residual-backbone states carry `211` points and mass `1.928005934870...`; all are terminal. The refined family has only three repeated pair tokens, with repeated mass `0.019917616169...`.

Verifier and certificate:

- `src/verify_residual_sponsor_backbone_split.py`;
- `data/residual_sponsor_backbone_split_certificate_2026-07-14.txt`;
- certificate SHA-256 `28266cae2b603b7a2490d547ef96d429e06e31cba4706ccc1f0fe0dbdc7bc986`.
"""


def remove_all_exact(text: str, block: str) -> str:
    while block in text:
        text = text.replace(block, "", 1)
    return text


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_ledger() -> None:
    path = ROOT / "docs/certainty-ledger.md"
    text = path.read_text(encoding="utf-8")
    if CL087 not in text:
        raise AssertionError("missing CL-087 marker")
    lines = [line for line in text.splitlines() if line != CL088 and line not in REF_LINES]
    text = "\n".join(lines) + "\n"
    text = text.replace(CL087 + "\n", CL087 + "\n" + CL088 + "\n", 1)
    marker = "Primary latest references:\n\n"
    if marker not in text:
        raise AssertionError("missing primary-reference marker")
    refs = "".join(line + "\n" for line in REF_LINES)
    text = text.replace(marker, marker + refs, 1)
    write(path, text)


def patch_current_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = remove_all_exact(path.read_text(encoding="utf-8"), CURRENT_BLOCK)
    marker = "---\n\n" + FOUNDATION
    if marker not in text:
        raise AssertionError("missing foundation marker")
    text = text.replace(marker, CURRENT_BLOCK + FOUNDATION, 1)
    write(path, text)


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line not in {README_ITEM19, README_LINK}]
    text = "\n".join(lines) + "\n"
    if README_ITEM18 not in text or README_LINK_MARKER not in text:
        raise AssertionError("missing README insertion marker")
    text = text.replace(README_ITEM18 + "\n", README_ITEM18 + "\n" + README_ITEM19 + "\n", 1)
    text = text.replace(README_LINK_MARKER + "\n", README_LINK_MARKER + "\n" + README_LINK + "\n", 1)
    if README_ACTIVE_OLD in text:
        text = text.replace(README_ACTIVE_OLD, README_ACTIVE_NEW, 1)
    elif README_ACTIVE_NEW not in text:
        raise AssertionError("missing README active-theorem paragraph")
    write(path, text)


def patch_decision_history() -> None:
    path = ROOT / "docs/research-decision-history.md"
    text = remove_all_exact(path.read_text(encoding="utf-8"), DECISION_BLOCK)
    marker = DECISION_LEAD + "\n\n"
    if marker not in text:
        raise AssertionError("missing decision-history insertion marker")
    text = text.replace(marker, marker + DECISION_BLOCK, 1)
    if OLD_TASKS in text:
        text = text.replace(OLD_TASKS, NEW_TASKS, 1)
    elif NEW_TASKS not in text:
        raise AssertionError("missing decision-history active tasks")
    write(path, text)


def patch_refinement_note() -> None:
    path = ROOT / "docs/residual-sponsor-backbone-refinement.md"
    text = remove_all_exact(path.read_text(encoding="utf-8"), CERTIFIED_SECTION)
    write(path, text.rstrip() + "\n\n" + CERTIFIED_SECTION)


def main() -> int:
    patch_ledger()
    patch_current_program()
    patch_readme()
    patch_decision_history()
    patch_refinement_note()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
