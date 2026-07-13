# Complete affine frontier on small `S_7` cyclic-output children

## Status

Exact fixed-policy finite theorem on the shell-resolved child states of size at
most `50` emitted by the `S_7` cyclic terminal-fiber component.

The previous local theorem checked translated-layer collisions and four-term
progressions formed by three points in one layer plus a completion point in
another layer. The current verifier generates every admissible three-translate
extension and performs a complete exact four-term-progression membership test.
It therefore includes every layer-word obstruction, not only the local
completion subset.

**Verifier:** `src/verify_s7_scc_small_state_affine_frontier.py`.

**Certificate:**
`data/s7_scc_small_state_affine_frontier_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
6a1073d6fd485c0a99526c59c32b5a0985220632e32e67fc8fed9d5b8c5234e0
```

---

## 1. Exact finite domain

The seven cyclic source steps are

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

They emit `63` shell-resolved middle-fiber occurrences representing `62` exact
numerical states. This theorem retains the `33` exact states satisfying

```math
|X|\le50.
```

Every one of these `33` states has zero intersection with the `S_7`
minimum-translation backbone. Thus, on this restricted frontier, every
numerical label is novel relative to that parent backbone.

For

```math
X\subseteq[L,2L),
```

the tested factor-`f` separation domain is

```math
\mathcal D_f(X)
=
\left\{
R:
1\le R\le
\left\lfloor
\frac{fL-1-\max X}{2}
\right\rfloor,
\quad
v_2(R)\equiv0\pmod2
\right\},
```

with `f=2` or `f=4`.

For every candidate, the verifier forms

```math
G_R(X)
=
(\{0\}\cup X)
\cup
(\{0\}\cup X+R)
\cup
(\{0\}\cup X+2R).
```

It then checks:

1. exact disjointness of the three translated copies;
2. exact containment below the next dyadic scale;
3. every possible nontrivial four-term arithmetic progression in `G_R(X)`.

No randomized sampling or incomplete witness family is used.

---

## 2. Factor-two frontier

Across the `33` small exact states:

| quantity | count |
|---|---:|
| admissible candidates | `21,724` |
| invalid by local collision/completion support | `2,128` |
| additional invalid candidates found by the complete affine test | `4,436` |
| total exact invalid candidates | `6,564` |
| exact valid candidates | `15,160` |
| layer-overlap failures | `1,424` |
| four-term-progression failures | `5,140` |
| nonempty state domains | `30` |
| completely excluded nonempty states | `1` |
| states with at least one valid candidate | `29` |

Hence

```math
\frac{6564}{21724}
=
\frac{1641}{5431}
```

of the candidate count is excluded, while

```math
\boxed{
\frac{15160}{21724}
=
\frac{3790}{5431}
}
```

remains valid.

---

## 3. Factor-four frontier

| quantity | count |
|---|---:|
| admissible candidates | `87,829` |
| invalid by local collision/completion support | `4,538` |
| additional invalid candidates found by the complete affine test | `7,568` |
| total exact invalid candidates | `12,106` |
| exact valid candidates | `75,723` |
| layer-overlap failures | `2,548` |
| four-term-progression failures | `9,558` |
| nonempty state domains | `33` |
| completely excluded states | `1` |
| states with at least one valid candidate | `32` |

Thus

```math
\boxed{
\frac{75723}{87829}
}
```

of the aggregate candidate count remains valid.

---

## 4. Connection to the 34 affine classes

For each invalid disjoint extension, the verifier selects the lexicographically
first exact four-term progression, reads its four translated-layer indices,
normalizes the layer word, and maps it into the certified `34` reversal
classes.

For both factors, deterministic first witnesses occur in `33` of the `34`
nonconstant classes. The only class absent from the first-witness histogram is
class `22`, represented by

```text
0221
```

with reverse

```text
1220.
```

The exact histogram digests are

```text
factor two:
270349594a150e57a23388aa80da8dfb2581b0dafd462f911578b645e99438af

factor four:
5da0d0cbd4934eabd3ba0a492288c871a424990f59d9c16a86b22b2204ae4339
```

This means the observed invalidity is distributed broadly across the affine
obstruction language. It does **not** prove that class `22` never occurs as a
secondary witness; only the deterministic first witness is classified.

---

## 5. Smallest exact survivors

For both factors, the first surviving state in the deterministic state order is

```math
X=\{5\},
\qquad
L=4,
\qquad
R=1.
```

The first surviving state of size at least three is

```math
X=\{16,21,26\},
\qquad
L=16,
\qquad
R=1.
```

These are exact surviving extensions, not merely candidates left unresolved by
a partial witness search.

The second example is particularly useful as a minimal nontrivial residual:
the child has three points and substantial additive structure, but its
three-translate extension at `R=1` is still disjoint, fits the required shell,
and contains no four-term arithmetic progression.

---

## 6. Consequence

The full affine obstruction language materially strengthens the local
collision/completion calculation:

```text
factor two: +4,436 additional invalid candidates
factor four: +7,568 additional invalid candidates.
```

However, most small-state candidates remain valid. Therefore the following
candidate closing principle is false on the recorded frontier:

```text
Once novel output is shell-resolved, complete one-generation affine
obstruction testing eliminates its future factor-two and factor-four cheap
extensions.
```

It does not.

The obstruction-export mechanism must use at least one additional ingredient:

1. larger child states and their denser affine spectra;
2. multi-generation accumulation of completion or rectangle support;
3. provenance-weighted reuse constraints;
4. containment or partial-overlap packing across simultaneous children;
5. a nonlinear capacity that charges surviving small extensions differently
   from large recurrent components.

---

## 7. Scope

The theorem is complete only for the `33` exact cyclic-source child states of
size at most `50` under the fixed lexicographic deletion policy.

The aggregate counts are diagnostics over exact numerical states. They are not
a simultaneous Bellman child sum, because the retention and overlap quotient
is still unproved.

The theorem also does not claim that the observed first-witness class
histograms describe every witness in every invalid extension.

---

## 8. Revised next target

The next computation should avoid merely extending the same brute-force size
cutoff without a structural purpose. The useful targets are:

1. isolate the smallest surviving states by source step and affine profile;
2. classify which survivors persist for both factors and which disappear after
   one more generation;
3. test whether the residual `{16,21,26}` extension exports completion or direct
   rectangle support after its next coordinated deletion;
4. define a residual-state quotient using scale, source SCC, affine zero-set,
   and completion radius;
5. use that quotient to search for a multi-generation contraction or the
   smallest exact recurrent counterexample.
