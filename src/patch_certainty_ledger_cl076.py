#!/usr/bin/env python3
"""Idempotently add CL-076 and the revised provenance-reserve bottleneck."""
from __future__ import annotations

from pathlib import Path

PATH = Path("docs/certainty-ledger.md")
ROW_075 = "| CL-075 | The 43 second-generation terminal `(u,p)` tokens have no collision with first-generation raw or retained tokens, but `(60,1354490)` recurs as a third-generation terminal sink. Both occurrences are step-5 middle fibers; immediate provenance differs (`2810` versus `440`) and separates the collision. Numerical identity is much coarser: 28 labels and seven complete terminal numerical states recur. | Exact finite cross-generation token-collision and signature-refinement theorem. |"
ROW_076 = "| CL-076 | With current harmonic mass coefficient fixed to one, an exact 11-feature screen finds four feasible standalone nonnegative corrections. In particular, `Phi_rep=H+2R`, where `R` is descendant harmonic mass on points whose root provenance repeats within the retained generation, contracts by `27.4704%`-`27.4705%` and then `6.0556%`-`6.0557%`. Independently, `Phi_tail=H+4T`, where `T` is descendant mass with immediate-provenance depth drop at least four, contracts on both transitions and has second-transition margin `0.1313%`-`0.1314%`. | Exact finite three-generation retained-potential theorem. |"

TAIL = r"""# Open bottleneck OB-001: provenance-reserve validation

The adversarial local-optimum transition now has:

- a legitimate point-disjoint retained-child quotient;
- exact terminal/recursive partitions through generation three;
- an explicit raw recursive-mass failure at generation three;
- a complete terminal identity and first-appearance ledger;
- an explicit failure of `(u,p)` repaired locally by immediate provenance;
- and two same-form retained potentials that contract across both observed recursive transitions.

The primary candidate is

```math
\mathrm{RecPack}(F)=H(F)+2R(F),
```

where `R(F)` is current harmonic mass on points whose original root provenance repeats within the retained generation. The secondary candidate is

```math
\mathrm{RecPack}_{\mathrm{tail}}(F)=H(F)+4T(F),
```

where `T(F)` is current harmonic mass on points with immediate-provenance depth drop at least four.

The next theorem must test these same coordinates on the fourth retained recursive generation, across alternative policies, and under branching terminal recreation. A finite success is not yet a whole-tree Carleson or Bellman theorem.

The target remains

```math
\Delta(S)
+
\mathrm{TermSink}_{\mathrm{first}}(S)
+
\sum_{S'\in\mathrm{RecChild}_\pi(S)}
\mathrm{RecPack}(S')
\le
\mathrm{RecPack}(S)
+
\Phi_{\mathrm{obs}}(S)
+
\mathrm{controlled\ error}.
```
"""


def main() -> int:
    text = PATH.read_text(encoding="utf-8")
    if ROW_076 not in text:
        if ROW_075 not in text:
            raise AssertionError("CL-075 anchor not found")
        text = text.replace(ROW_075, ROW_075 + "\n" + ROW_076, 1)

    reference_anchor = "Primary latest references:\n\n"
    if "- `docs/generation-aware-retained-potentials.md`;" not in text:
        if reference_anchor not in text:
            raise AssertionError("reference anchor not found")
        text = text.replace(
            reference_anchor,
            reference_anchor
            + "- `docs/generation-aware-retained-potentials.md`;\n"
            + "- `src/verify_generation_aware_retained_potentials.py`;\n",
            1,
        )

    inference_anchor = "34. immediate provenance as globally sufficient after one finite collision test;\n"
    inference_row = "35. `H+2R` or `H+4T` as a universal Bellman potential after two finite transitions;\n"
    if inference_row not in text:
        if inference_anchor not in text:
            raise AssertionError("prohibited-inference anchor not found")
        text = text.replace(inference_anchor, inference_anchor + inference_row, 1)

    text = text.replace(
        "35. maximum-harmonic local retention as globally optimal;\n"
        "36. policy-LP feasibility as branching Bellman-LP feasibility;\n"
        "37. the tested policy family as globally optimal;\n"
        "38. random sampling as a finite certificate;\n"
        "39. the rejected depth-ten anchor reduction.\n",
        "36. maximum-harmonic local retention as globally optimal;\n"
        "37. policy-LP feasibility as branching Bellman-LP feasibility;\n"
        "38. the tested policy family as globally optimal;\n"
        "39. random sampling as a finite certificate;\n"
        "40. the rejected depth-ten anchor reduction.\n",
        1,
    )

    heading = "# Open bottleneck OB-001:"
    if heading not in text:
        raise AssertionError("open bottleneck heading not found")
    prefix = text.split(heading, 1)[0]
    text = prefix + TAIL
    PATH.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
