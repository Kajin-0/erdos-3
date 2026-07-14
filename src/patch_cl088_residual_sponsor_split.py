#!/usr/bin/env python3
"""Record the certified residual/sponsor backbone refinement as CL-088."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise AssertionError(f"missing {label} marker")
    if text.count(old) != 1:
        raise AssertionError(f"nonunique {label} marker")
    return text.replace(old, new, 1)


def patch_ledger() -> None:
    path = ROOT / "docs/certainty-ledger.md"
    text = path.read_text(encoding="utf-8")
    cl087 = "| CL-087 | The certified `R_3 -> F_4` transition has 14/14 affine parents. Exact pair containment has zero missing current or latent resources. Parent pair multiplicity is at most 2 with repeated mass `7.711618836980...`; child multiplicity is at most 2 with repeated mass `0.133953757799...`. Both resource conventions contract: occurrence `2747.630136815823... < 7828.862146571999...`, union `2747.496183058024... < 7821.150527735019...`. | Exact finite affine pair-resource contraction theorem; fixed policy and quotient. |"
    cl088 = "| CL-088 | Splitting every `R_4 -> F_5` minimum-backbone shell by residual versus deleted-sponsor root preserves the exact raw support union (`1489` labels), point-occurrence count (`2972`), and harmonic occurrence mass (`25.589294609269...`). Under the same retained quotient, recursive points fall `1015 -> 864`, recursive mass falls by `0.168809631114...`, latent pair occurrences fall by `32190`, and union pair-resource mass falls by `404.536054734914...`; terminal mass rises by `0.369683464666...`. | Exact finite residual-sponsor backbone refinement theorem; fixed policy and quotient, no generation six. |"
    text = replace_once(text, cl087, cl087 + "\n" + cl088, "CL-087")
    refs = "Primary latest references:\n\n"
    new_refs = (
        "Primary latest references:\n\n"
        "- `docs/residual-sponsor-backbone-refinement.md`;\n"
        "- `src/verify_residual_sponsor_backbone_split.py`;\n"
        "- `data/residual_sponsor_backbone_split_certificate_2026-07-14.txt`;\n"
    )
    text = replace_once(text, refs, new_refs, "primary references")
    path.write_text(text, encoding="utf-8")


def patch_current_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = path.read_text(encoding="utf-8")
    marker = "---\n\n## 1. Foundation and recorded exact path"
    section = r"""---

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

## 1. Foundation and recorded exact path"""
    text = replace_once(text, marker, section, "foundation section")
    path.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    item18 = "18. exact occurrence- and union-valued pair-resource contraction from the third to fourth retained frontier."
    item19 = "19. a certified residual-sponsor backbone split that terminalizes translated residual roots and reduces the fifth recursive pair-resource load without changing raw support or harmonic occurrence mass."
    text = replace_once(text, item18, item18 + "\n" + item19, "README status item")
    link_marker = "- [`docs/third-to-fourth-pair-resource-contraction.md`](docs/third-to-fourth-pair-resource-contraction.md) — exact affine pair contraction before root uniqueness."
    link_new = link_marker + "\n- [`docs/residual-sponsor-backbone-refinement.md`](docs/residual-sponsor-backbone-refinement.md) — symbolic and exact finite sponsor-core refinement of the minimum backbone."
    text = replace_once(text, link_marker, link_new, "README start link")
    active = "Affine closure and union-valued pair containment now control reuse exactly across the whole retained tree. The decisive missing theorem is an economical activation or multiscale exposure bound for the pair tokens actually used."
    active_new = "Affine closure and union-valued pair containment now control reuse exactly across the whole retained tree. The certified residual-sponsor split further terminalizes translated residual roots, so the continuing resource universe is concentrated on deleted sponsor roots. The decisive missing theorem is an economical activation or multiscale exposure bound for sponsor-core pair tokens."
    text = replace_once(text, active, active_new, "README active theorem")
    path.write_text(text, encoding="utf-8")


def patch_decision_history() -> None:
    path = ROOT / "docs/research-decision-history.md"
    text = path.read_text(encoding="utf-8")
    lead = "The finite obstruction prefix is now restricted to `R_1 -> F_2` and `R_2 -> F_3`; the later transitions are closed."
    marker = lead + "\n\n**Decisions:**\n"
    section = lead + """

### Residual-sponsor backbone refinement

The first workflow attempt did not test the mathematics: it imported a nonexistent module, and an unsafe named `git add -A` pathspec masked that exception. After the repository-wide workflow hardening pass, the original error was preserved and the probe was rewritten against the certified lexicographic propagation APIs.

The corrected exact test partitions only the already-existing translated minimum backbone. It inserts no unshifted residual output and preserves raw support, point occurrences, and harmonic occurrence mass exactly. Under the same retained quotient, the residual-root shells are terminal, recursive points fall by `151`, recursive mass falls by `0.168809631114...`, and union pair-resource mass falls by `404.536054734914...`.

This closes the finite question of whether the symbolic residual-sponsor split is useful on the recorded failing transition. It is strongly favorable. The remaining analytical target is a state-independent sponsor-core activation bound.

**Decisions:**
"""
    text = replace_once(text, marker, section, "third-to-fourth decision boundary")
    old_tasks = """The next exact work is to:

1. certify affine root references and exact pivot updates on the existing retained frontier;
2. test the exact minimum-translation reserve on the four existing transitions;
3. quantify entering pair energy and identify a noncircular payment source;
4. prove affine entry/purification or charge non-affine recursive output to terminal or arithmetic obstruction;
5. distinguish provenance-valid release from numerical coverage among the `673` dropped roots with raw descendants;
6. formulate the resulting transfer lemma before propagating another generation.

No current theorem closes this gap. Generation six and further feature fitting are explicitly deferred."""
    new_tasks = """The next exact and analytical work is to:

1. measure sponsor-core size, selected-progression incidence, and pair-energy exposure on the first two retained transitions;
2. prove a weighted bound for the activated star pairs `(a,s)` and internal sponsor pairs `binom(Sigma,2)`;
3. charge popular or short sponsor differences to terminal first appearance, completion support, rectangle transport, or cheap-extension exclusion;
4. determine whether policy selection can minimize sponsor-core pair energy while preserving the one-generation harmonic lower bound;
5. formulate the sponsor-core transfer lemma before propagating another generation.

No current theorem pays for sponsor-core activation from the original root at all scales. Generation six and further feature fitting remain explicitly deferred."""
    text = replace_once(text, old_tasks, new_tasks, "active tasks")
    path.write_text(text, encoding="utf-8")


def patch_refinement_note() -> None:
    path = ROOT / "docs/residual-sponsor-backbone-refinement.md"
    text = path.read_text(encoding="utf-8")
    if "## 11. Certified retained-frontier result" in text:
        return
    addition = """

---

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
    path.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_current_program()
    patch_readme()
    patch_decision_history()
    patch_refinement_note()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
