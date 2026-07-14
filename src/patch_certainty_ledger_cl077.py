#!/usr/bin/env python3
"""Idempotently record the fourth-generation provenance-reserve frontier."""
from __future__ import annotations

from pathlib import Path

PATH = Path("docs/certainty-ledger.md")
ROW_076 = "| CL-076 | With current harmonic mass coefficient fixed to one, an exact 11-feature screen finds four feasible standalone nonnegative corrections. In particular, `Phi_rep=H+2R`, where `R` is descendant harmonic mass on points whose root provenance repeats within the retained generation, contracts by `27.4704%`-`27.4705%` and then `6.0556%`-`6.0557%`. Independently, `Phi_tail=H+4T`, where `T` is descendant mass with immediate-provenance depth drop at least four, contracts on both transitions and has second-transition margin `0.1313%`-`0.1314%`. | Exact finite three-generation retained-potential theorem. |"
ROW_077 = "| CL-077 | Propagating the 14 third-generation recursive states and reapplying the same quotient produces a unique point-disjoint fourth family with 23 states and 1794 points, split into 11 terminal states with 77 points and 12 recursive states with 1717 points. `H4_rec/H3_rec` is `2.849279`-`2.849280`. The CL-076 candidates fail: `H+2R` expands by `2.711908`-`2.711909` because repeated-root reserve vanishes, and `H+4T` expands by `9.636610`-`9.636611` because the immediate depth-four tail regenerates. Seven `(u,p)` terminal collisions occur, but no `(u,p,i)` collision is recorded through generation four. | Exact finite fourth-generation potential no-go and refined-token survival theorem. |"

TAIL = r"""# Open bottleneck OB-001: exact four-generation feature LP

The adversarial retained construction now has:

- legitimate point-disjoint retained families through generation four;
- exact terminal/recursive partitions at generations two, three, and four;
- recursive mass ratios below one, above two, and above 2.84 on successive transitions;
- a complete first-appearance terminal ledger;
- failure of `(u,p)` and finite survival of `(u,p,i)`;
- two exact three-generation reserve witnesses;
- and an exact fourth-generation failure of both witnesses.

The next theorem is an exact nonnegative feature-feasibility problem. Export the three recursive transitions into a common rational matrix with current harmonic coefficient fixed to one. Test whether any nonnegative combination of the existing provenance, multiplicity, and depth features makes all three rows nonpositive.

If feasible, record a sparse rational witness. If infeasible, extract the smallest exact Farkas or dual obstruction before introducing cumulative provenance, ancestor-path, terminal-release, or affine-obstruction coordinates.

The whole-tree target remains

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
    if ROW_077 not in text:
        if ROW_076 not in text:
            raise AssertionError("CL-076 anchor not found")
        text = text.replace(ROW_076, ROW_076 + "\n" + ROW_077, 1)

    reference_anchor = "Primary latest references:\n\n"
    additions = (
        "- `docs/fourth-generation-provenance-reserve-frontier.md`;\n"
        "- `src/verify_fourth_generation_potential_frontier.py`;\n"
    )
    if "- `docs/fourth-generation-provenance-reserve-frontier.md`;" not in text:
        if reference_anchor not in text:
            raise AssertionError("reference anchor not found")
        text = text.replace(reference_anchor, reference_anchor + additions, 1)

    inference_anchor = "35. `H+2R` or `H+4T` as a universal Bellman potential after two finite transitions;\n"
    inference_row = "36. `H+2R` or `H+4T` as an iterating potential after the fourth-generation failure;\n"
    if inference_row not in text:
        if inference_anchor not in text:
            raise AssertionError("inference anchor not found")
        text = text.replace(inference_anchor, inference_anchor + inference_row, 1)

    replacements = {
        "36. maximum-harmonic local retention as globally optimal;": "37. maximum-harmonic local retention as globally optimal;",
        "37. policy-LP feasibility as branching Bellman-LP feasibility;": "38. policy-LP feasibility as branching Bellman-LP feasibility;",
        "38. the tested policy family as globally optimal;": "39. the tested policy family as globally optimal;",
        "39. random sampling as a finite certificate;": "40. random sampling as a finite certificate;",
        "40. the rejected depth-ten anchor reduction.": "41. the rejected depth-ten anchor reduction.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new, 1)

    heading = "# Open bottleneck OB-001:"
    if heading not in text:
        raise AssertionError("open bottleneck heading not found")
    text = text.split(heading, 1)[0] + TAIL
    PATH.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
