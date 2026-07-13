# Audit of the proposed depth-ten factor-four exclusion

## Status

The complete factor-four exclusion from the recorded state `S_10` is **not yet certified**.

The currently committed exploratory pipeline proposes

```math
314986450
\to177844250
\to2520
\to1866
\to893
\to0.
```

Several later stages are exact conditional reductions, and explicit witnesses have been recorded for part of the final residual. However, two independent gaps prevent the conclusion

```math
N_{10,4}=0
```

from being entered in the certainty ledger.

---

## 1. Unsupported anchor reduction

The dominant reduction is implemented in

```text
src/verify_depth10_factor4_anchor_reduction.cpp
```

and removes `177841730` candidates. Its removal loop uses the following relation:

```math
x=3d\in S_{10},
\qquad
s\in S_{10},
```

with

```math
R=s-d
```

or

```math
2R=s-d.
```

The source does not output four progression points and does not invoke a proved lemma showing that this relation forces a four-term progression.

The audit verifier

```text
src/audit_depth10_factor4_anchor_reduction.py
```

constructs the exact example

```math
d=201326592,
\qquad
x=603979776=3d,
```

```math
s=536870912,
\qquad
R=s-d=335544320.
```

This separation:

1. is sponsor-compatible;
2. lies in the genuinely new factor-four range;
3. has disjoint translate layers.

The nine points whose presence follows solely from the three base values `0`, `x`, `s` and the three translate layers contain no four-term arithmetic progression.

This does not prove that the full candidate at this separation is four-term-progression-free. It proves that the relation used by the reduction is not itself a valid direct witness. A further state-specific lemma or an explicit witness-generating check is required before the `177841730` removals can be certified.

---

## 2. Incomplete terminal witness data

The terminal residual verifier expects

```text
893
```

explicit witness records and the assembled file

```text
data/depth10_factor4_residual_witnesses_2026-07-12.txt
```

with certified hashes.

The repository currently contains only:

```text
data/depth10_factor4_residual_witnesses_2026-07-12.part00.txt  180 records
data/depth10_factor4_residual_witnesses_2026-07-12.part01.txt  180 records
data/depth10_factor4_residual_witnesses_2026-07-12.part02.txt  180 records
data/depth10_factor4_residual_witnesses_2026-07-12.part03.txt  180 records
```

Thus only

```math
720
```

of the required `893` records are present. The final

```math
893-720=173
```

witnesses and the canonical assembled file are absent.

---

## 3. What remains valid

The following results remain certified:

1. the complete factor-two inheritance exclusion
   ```math
   N_{10,2}=0;
   ```
2. the exact factor-four layer-disjoint domain count
   ```math
   348012826;
   ```
3. removal of the inherited interval, leaving
   ```math
   314986450
   ```
   genuinely new factor-four candidates;
4. the prior theorem
   ```math
   N_{9,4}=0;
   ```
5. the complete exact factor-eight child fan from `S_10`.

The missing-interior, mixed-completion, and terminal-witness programs may be retained as conditional exploratory components, but they do not bypass the unsupported anchor reduction.

---

## 4. Required repair

A complete certificate must do both of the following:

1. replace the anchor reduction with either:
   - an explicit four-point witness formula proved for every removed candidate, or
   - a verifier that outputs and checks an actual four-term progression for every removal;
2. provide all `893` terminal witness records and the canonical assembled witness file.

Until both repairs are complete, the correct repository status is:

```math
\boxed{
N_{10,2}=0,
\qquad
N_{10,4}\text{ unresolved}.
}
```
