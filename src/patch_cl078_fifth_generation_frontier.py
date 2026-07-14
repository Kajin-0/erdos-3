#!/usr/bin/env python3
"""Idempotently record the fifth-generation frontier in authoritative docs."""
from __future__ import annotations

from pathlib import Path

LEDGER = Path("docs/certainty-ledger.md")
PROGRAM = Path("docs/current-proof-program.md")

ROW_077 = "| CL-077 | Propagating the 14 third-generation recursive states and reapplying the same quotient produces a unique point-disjoint fourth family with 23 states and 1794 points, split into 11 terminal states with 77 points and 12 recursive states with 1717 points. `H4_rec/H3_rec` is `2.849279`-`2.849280`. The CL-076 candidates fail: `H+2R` expands by `2.711908`-`2.711909` because repeated-root reserve vanishes, and `H+4T` expands by `9.636610`-`9.636611` because the immediate depth-four tail regenerates. Seven `(u,p)` terminal collisions occur, but no `(u,p,i)` collision is recorded through generation four. | Exact finite fourth-generation potential no-go and refined-token survival theorem. |"
ROW_078 = "| CL-078 | Propagating the 12 fourth-generation recursive states and reapplying the same quotient produces a unique point-disjoint fifth family with 21 states and 1032 points, split into 8 terminal states with 17 points and 13 recursive states with 1015 points. `H5_rec/H4_rec` is `1.329813`-`1.329814`. Repeated-root descendant mass is exactly zero at both levels, so no finite coefficient in `H+kR` can repair this transition. Two `(u,p)` terminal collisions occur, but no `(u,p,i)` collision is recorded through generation five. | Exact finite fifth-generation repeated-root no-go and refined-token survival theorem. |"

OLD_PROGRAM_BLOCK = """The current frontier supplies:

```text
legitimate point-disjoint retained children through generation four
exact terminal/recursive partitions
three alternating recursive-mass transitions
an exact first-appearance terminal ledger
an (u,p) token failure and an (u,p,i) finite repair
two three-generation reserve witnesses
a fourth-generation exact failure of both witnesses.
```

The next mathematical object is an exact rational feature LP over all three recursive transitions:

```text
generation 1 -> generation 2 recursive
generation 2 recursive -> generation 3 recursive
generation 3 recursive -> generation 4 recursive.
```

The LP must test whether any nonnegative combination of the existing feature family makes every transition nonexpanding. If infeasible, the smallest exact Farkas/dual obstruction becomes the next theorem. New coordinates should be introduced only after that exhaustion.
"""

NEW_PROGRAM_BLOCK = """The current frontier supplies:

```text
legitimate point-disjoint retained children through generation five
exact terminal/recursive partitions
four recorded recursive-mass transitions
an exact first-appearance terminal ledger
an (u,p) token failure and an (u,p,i) finite repair through generation five
two three-generation reserve witnesses
a fourth-generation failure of both small witnesses
and a fifth-generation no-go for every finite H+kR potential.
```

The next mathematical object is an exact rational feature LP over all four recursive transitions:

```text
generation 1 -> generation 2 recursive
generation 2 recursive -> generation 3 recursive
generation 3 recursive -> generation 4 recursive
generation 4 recursive -> generation 5 recursive.
```

The LP must test whether any nonnegative combination of the existing eleven-feature family makes every transition nonexpanding. Its exact outcome is still pending. If infeasible, the smallest exact Farkas/dual obstruction becomes the next theorem. New coordinates should be introduced only after that exhaustion.
"""

OLD_TARGETS = """1. Export the three recursive transitions into one exact rational feature matrix.
2. Solve the nonnegative feature-feasibility LP with current harmonic coefficient fixed to one.
3. Extract a sparse rational witness or the smallest exact dual obstruction.
4. Test refined terminal token `(u,p,i)` in the same first-appearance accounting schema.
5. Add cumulative provenance or path-capacity coordinates only if the current LP is infeasible.
6. Test policy sensitivity on the smallest retained families before propagating generation five.
7. Attach completion, rectangle, or cheap-extension exclusion credit to reserve release.
8. Prove a branching terminal-output Carleson bound or isolate the first unbounded refined-token reuse mechanism.
"""

NEW_TARGETS = """1. Complete the exact eleven-feature LP over all four recorded recursive transitions.
2. Extract a sparse rational witness or the smallest exact Farkas/dual obstruction.
3. Add cumulative provenance or ancestor-path capacity only if the current LP is infeasible.
4. Test policy sensitivity on the smallest retained families before propagating generation six.
5. Attach completion, rectangle, or cheap-extension exclusion credit to reserve release.
6. Prove a branching terminal-output Carleson bound or isolate the first unbounded refined-token reuse mechanism.
"""


def patch_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if ROW_078 not in text:
        if ROW_077 not in text:
            raise AssertionError("CL-077 anchor not found")
        text = text.replace(ROW_077, ROW_077 + "\n" + ROW_078, 1)
    if "`H+2R` or `H+4T` as an iterating potential after the fourth-generation failure;" in text and "`H+kR` as an iterating potential after the fifth-generation zero-reserve failure;" not in text:
        text = text.replace(
            "36. `H+2R` or `H+4T` as an iterating potential after the fourth-generation failure;",
            "36. `H+2R` or `H+4T` as an iterating potential after the fourth-generation failure;\n37. `H+kR` as an iterating potential after the fifth-generation zero-reserve failure;",
            1,
        )
        for old in range(37, 42):
            text = text.replace(f"\n{old}. ", f"\n{old + 1}. ", 1)
    LEDGER.write_text(text, encoding="utf-8")


def patch_program() -> None:
    text = PROGRAM.read_text(encoding="utf-8")
    if OLD_PROGRAM_BLOCK in text:
        text = text.replace(OLD_PROGRAM_BLOCK, NEW_PROGRAM_BLOCK, 1)
    elif NEW_PROGRAM_BLOCK not in text:
        raise AssertionError("proof-program frontier block not found")
    if OLD_TARGETS in text:
        text = text.replace(OLD_TARGETS, NEW_TARGETS, 1)
    elif NEW_TARGETS not in text:
        raise AssertionError("approved-target block not found")
    text = text.replace(
        "Terminal identities and retained generations through the fourth frontier:",
        "Terminal identities and retained generations through the fifth frontier:",
        1,
    )
    PROGRAM.write_text(text, encoding="utf-8")


def main() -> int:
    patch_ledger()
    patch_program()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
