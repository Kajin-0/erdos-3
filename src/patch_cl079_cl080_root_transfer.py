#!/usr/bin/env python3
"""Idempotently record CL-079/080 and the root-transfer bottleneck."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")

ROW_079 = "| CL-079 | On the certified fourth recursive family, all-lexicographic deletion, all-reverse deletion, and each of the twelve single-parent lexicographic-to-reverse flips expand recursively under every maximum-total-harmonic retention tie choice. The best tested policy is `reverse_parent_82`, with ratio `1.197375982982...`; the baseline ratio is `1.329813898820...`. The two nonunique policies each have two tied optima with identical recursive mass. | Exact finite local policy-sensitivity theorem; not universal over all policies or retention rules. |"
ROW_080 = "| CL-080 | At the baseline fourth-to-fifth transition, all root provenance is unique. Of 1717 fourth recursive roots, 1015 survive recursively and 702 exit; 17 terminalize and 685 disappear from the retained family. The exact identity `H5_rec-H4_rec=G_4->5-L_4->5` has survivor scale gain `1.816777911848...`, exiting parent release `1.310139720502...`, and net recursive increase `0.506638191346...`; `1.386705<G/L<1.386706`. No root splits between recursive and terminal output and fifth retained root multiplicity is one. | Elementary root-lineage identity plus exact finite decomposition. |"

PROHIBITED = """# Prohibited inferences

Do not use without materially new hypotheses:

1. universal local or fixed-window contraction;
2. replay siblings as simultaneous children;
3. pathwise summability as whole-tree summability;
4. raw novelty as schedule independent;
5. `P Psi` as a standalone Bellman potential;
6. raw occurrences copied directly into a Bellman child sum;
7. exact-state quotienting alone as a containment theorem;
8. a uniform overlap constant or decreasing terminal-label rank;
9. unit harmonic or factor-two linear SCC capacity;
10. raw numerical union as stored repayment;
11. local affine obstruction coverage as complete repayment;
12. absence from a first-witness histogram as absence from all witnesses;
13. all small surviving states as negligible errors;
14. one regenerative path as whole-tree divergence;
15. regeneration as parent-intrinsic;
16. one finite policy witness as an all-policy theorem;
17. avoidance of regeneration as sufficient optimization;
18. raw occurrence or label count without harmonic/provenance weights;
19. one finite weight cone as global validation;
20. greedy composition of favorable policy delays;
21. one-toggle local optimality as global policy optimality;
22. lower raw harmonic occurrence mass as Bellman contraction;
23. one-generation retention as a bound on indefinite reuse;
24. maximum provenance multiplicity as contraction;
25. unit depth/log charge as repayment for total retained mass;
26. the full `6.828`-`6.829` ratio as recursive load;
27. discarding terminal mass instead of charging it once;
28. within-family terminal-token uniqueness as global uniqueness;
29. `(u,p)` as a collision-sound cross-generation terminal token;
30. source type and source step as sufficient collision refinement;
31. first-appearance deduplication as a bound on token-union mass;
32. the `6.2%`-`6.3%` recursive contraction or `31/500` credit as an iterating invariant;
33. a recorded recursive expansion as universal over all policies or quotients;
34. immediate provenance as globally sufficient after finite collision tests;
35. `H+2R`, `H+4T`, or `H+74R` as an iterating Bellman potential;
36. any finite `H+kR` potential after the fifth-generation zero-reserve failure;
37. maximum-harmonic local retention as globally optimal;
38. policy-LP feasibility as branching Bellman-LP feasibility;
39. the tested policy family as globally optimal;
40. random sampling as a finite certificate;
41. another fitted feature without a state-independent transfer law;
42. generation-six propagation without a predeclared conceptual test.

---

"""

BOTTLENECK = r"""# Open bottleneck OB-001: cumulative root-lineage reserve transfer

The adversarial retained construction now has:

- legitimate point-disjoint retained families through generation five;
- exact terminal/recursive partitions;
- refined terminal identities and first-appearance bookkeeping;
- exact failure of current-generation repeated-root reserve;
- local policy sensitivity at the first failing transition;
- and an exact root-lineage decomposition of that failure.

At the baseline fourth-to-fifth transition,

```math
H_5^{\mathrm{rec}}-H_4^{\mathrm{rec}}
=G_{4\to5}-L_{4\to5},
```

where `G` is harmonic scale gain along unique surviving root lineages and `L` is parent mass released by exiting lineages. The certified values satisfy

```text
G_4->5 = 1.816777911848...
L_4->5 = 1.310139720502...
G_4->5/L_4->5 = 1.386705466156...
```

Thus the first failing transition is not driven by repeated-root branching. It is driven by scale contraction along unique surviving lineages exceeding released parent mass.

The next theorem must define a state-independent cumulative ancestor-path capacity `A` and prove a transition inequality of the form

```math
H_{g+1}^{\mathrm{rec}}
+A_{g+1}
+T_{g+1}^{\mathrm{first}}
\le
H_g^{\mathrm{rec}}
+A_g
+\Phi_{\mathrm{obs},g}
+\varepsilon_g.
```

A new coordinate is admissible only if it has a transfer identity or one-sided recurrence, a bounded-reuse interpretation, and a telescoping role. Finite LP correlation is diagnostic only.

Generation six is blocked until such a lemma exists. The next concrete tasks are to classify survivor scale gain by source/shell/immediate provenance, attach terminalized roots to first-appearance `(u,p,i)` tokens, and determine what arithmetic credit is created by the 685 dropped lineages.
"""


def main() -> int:
    text = LEDGER.read_text(encoding="utf-8")
    lines = text.splitlines()
    if ROW_079 not in lines:
        index = next(i for i, line in enumerate(lines) if line.startswith("| CL-078 |"))
        lines[index + 1:index + 1] = [ROW_079, ROW_080]
    elif ROW_080 not in lines:
        index = next(i for i, line in enumerate(lines) if line == ROW_079)
        lines.insert(index + 1, ROW_080)
    text = "\n".join(lines) + "\n"

    marker = "Primary latest references:\n\n"
    additions = (
        "- `docs/fourth-to-fifth-root-transfer.md`;\n"
        "- `src/verify_fourth-to-fifth-root-transfer.py`;\n"
        "- `docs/fourth-to-fifth-policy-sensitivity.md`;\n"
        "- `src/verify_fourth_to_fifth_policy_sensitivity.py`;\n"
    )
    # Correct an earlier typo if present before testing for the canonical block.
    text = text.replace(
        "- `src/verify_fourth-to-fifth-root-transfer.py`;\n",
        "- `src/verify_fourth_to_fifth_root_transfer.py`;\n",
    )
    canonical_additions = additions.replace(
        "verify_fourth-to-fifth-root-transfer.py",
        "verify_fourth_to_fifth_root_transfer.py",
    )
    if canonical_additions not in text:
        text = text.replace(marker, marker + canonical_additions, 1)

    start = text.index("# Prohibited inferences")
    bottleneck = text.index("# Open bottleneck", start)
    text = text[:start] + PROHIBITED + text[bottleneck:]
    start = text.index("# Open bottleneck")
    text = text[:start] + BOTTLENECK.rstrip() + "\n"
    LEDGER.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
