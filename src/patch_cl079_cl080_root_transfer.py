#!/usr/bin/env python3
"""Idempotently record CL-079/080 and the root-transfer research pivot."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
HISTORY = Path("docs/research-decision-history.md")

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

HISTORY_PHASE = r"""## 10. Retained propagation and root-lineage transfer phase

The retained quotient was propagated through five recorded levels. Static current-generation features produced exact finite witnesses, including `H+74R` through generation four, but generation five has

```math
R_4=R_5=0
```

while recursive harmonic mass expands by a factor between `1.329813` and `1.329814`. No finite coefficient in `H+kR` repairs that transition.

The first failing transition was then tested under all-lexicographic deletion, all-reverse deletion, and each single-parent lexicographic-to-reverse flip. All fourteen tested policies expand under every maximum-harmonic retention tie. The best tested policy, `reverse_parent_82`, lowers the ratio to `1.197375982982...` but does not contract.

At the baseline transition all root provenance is unique. The exact lineage identity is

```math
H_5^{\mathrm{rec}}-H_4^{\mathrm{rec}}
=G_{4\to5}-L_{4\to5},
```

with

```text
surviving-lineage scale gain = 1.816777911848...
exiting parent release       = 1.310139720502...
net recursive increase       = 0.506638191346...
```

Of `1717` fourth recursive roots, `1015` survive and `702` exit; `17` terminalize and `685` disappear from the retained family. No root splits between recursive and terminal output.

**Decisions:**

- current-generation multiplicity is not persistent reserve;
- finite feature-LP witnesses are diagnostics, not theorem candidates without a transfer law;
- nearby deletion-policy changes do not remove the first failing expansion, although policy remains quantitatively important;
- the missing resource is cumulative ancestor-path scale capacity plus terminal/drop/obstruction release;
- generation six is blocked until a state-independent transfer lemma is proposed;
- a new feature is admissible only with a transition recurrence, bounded-reuse interpretation, and telescoping role.

---

"""

HISTORY_ACTIVE = r"""## 12. Active closing target

The active target is a cumulative root-lineage reserve-transfer theorem:

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

Here `A_g` must be a state-independent ancestor-path capacity, `T^{first}` is newly terminal first-appearance credit, and `Phi_obs` records completion, rectangle, or cheap-extension exclusion created when capacity is released.

The next exact work is to:

1. classify survivor scale gain by parent state, source type, shell, and immediate provenance;
2. attach the `17` terminalized roots injectively to first-appearance `(u,p,i)` tokens;
3. determine what completion, rectangle, or future-extension exclusion is created by the `685` dropped lineages;
4. formulate a transfer lemma before propagating another generation.

No current theorem closes this gap. Generation six and further feature fitting are explicitly deferred.

---

"""


def patch_ledger() -> None:
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
        "- `src/verify_fourth_to_fifth_root_transfer.py`;\n"
        "- `docs/fourth-to-fifth-policy-sensitivity.md`;\n"
        "- `src/verify_fourth_to_fifth_policy_sensitivity.py`;\n"
    )
    text = text.replace(
        "- `src/verify_fourth-to-fifth-root-transfer.py`;\n",
        "- `src/verify_fourth_to_fifth_root_transfer.py`;\n",
    )
    if additions not in text:
        text = text.replace(marker, marker + additions, 1)

    start = text.index("# Prohibited inferences")
    bottleneck = text.index("# Open bottleneck", start)
    text = text[:start] + PROHIBITED + text[bottleneck:]
    start = text.index("# Open bottleneck")
    text = text[:start] + BOTTLENECK.rstrip() + "\n"
    LEDGER.write_text(text, encoding="utf-8")


def patch_history() -> None:
    text = HISTORY.read_text(encoding="utf-8")
    if "## 10. Retained propagation and root-lineage transfer phase" not in text:
        anchor = "## 10. Permanent stop list"
        if anchor not in text:
            raise AssertionError("decision-history stop-list anchor not found")
        text = text.replace(anchor, HISTORY_PHASE + "## 11. Permanent stop list", 1)
    else:
        text = text.replace("## 10. Permanent stop list", "## 11. Permanent stop list", 1)

    for item in (
        "26. current-generation multiplicity as persistent reserve;",
        "27. another feature-fit/one-more-generation loop without a transfer lemma;",
        "28. generation-six propagation without a predeclared conceptual test.",
    ):
        if item not in text:
            needle = "25. the rejected depth-ten anchor reduction."
            replacement = needle + "\n" + item
            text = text.replace(needle, replacement, 1)

    active_start = text.index("## 11. Active closing target") if "## 11. Active closing target" in text else text.index("## 12. Active closing target")
    protocol_marker = "## 12. Documentation protocol" if "## 12. Documentation protocol" in text else "## 13. Documentation protocol"
    protocol_start = text.index(protocol_marker, active_start)
    text = text[:active_start] + HISTORY_ACTIVE + text[protocol_start:]
    text = text.replace("## 12. Documentation protocol", "## 13. Documentation protocol", 1)
    HISTORY.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
