# Half-scale exact-tail basin

## Status

Elementary induction theorem with exact rational layer-pattern verification and a finite `S_10` entry count.

This enlarges the previous basin criterion from

```math
0<k\le L/32
```

to the sharp open half-scale range

```math
\boxed{0<k<L/2}
```

provided the first exact step is already four-term-progression-free.

**Verifier:** `src/verify_half_scale_exact_tail_basin.py`.

---

## 1. The theorem

Let

```math
\min S=L,
\qquad
S\subseteq[L,7L/4),
```

and assume that `S` is four-term-progression-free. Put

```math
A=\{0\}\cup S.
```

Choose an integer offset `k` satisfying

```math
0<k<L/2,
\qquad
v_2(k)\equiv0\pmod2,
```

and set

```math
R=2L+k.
```

Assume that the first exact three-translate parent

```math
G=A\cup(A+R)\cup(A+2R)
```

is four-term-progression-free.

Define recursively

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n,
\qquad
R_n=2L_n+k_n,
```

```math
A_n=\{0\}\cup S_n,
```

```math
G_{n+1}
=
A_n\cup(A_n+R_n)\cup(A_n+2R_n),
```

```math
S_{n+1}=L_{n+1}+G_{n+1}.
```

Then every `G_n` and `S_n` is four-term-progression-free, every backbone reproduction is exact, and the construction gives an infinite exact factor-eight tail.

---

## 2. Enlarged top-layer regions

Exact rational vertex enumeration gives the same nine feasible four-layer patterns in both regions

```math
S\subseteq[L,7L/4),
\qquad
2L\le R\le5L/2,
```

and

```math
S\subseteq[L,15L/8),
\qquad
2L\le R\le9L/4.
```

These are exactly the nine patterns used by the existing top-layer reduction. Consequently, a new four-term progression in three translates can only arise from:

1. a three-term progression in the state whose missing completion is `R`; or
2. the half-separation point `R/2` lying in the state.

No additional layer pattern appears in either enlarged region.

---

## 3. Scheduled completion descent

For the scheduled successor offset

```math
k'=4k,
```

the target completion is

```math
2L'+k'=16L+4k.
```

Imposing this target directly in the rational layer equations leaves the unique pattern

```text
layers 012
base pattern 111.
```

This remains true in both regions

```math
S\subseteq[L,7L/4),
\qquad
0\le k/L\le1/2,
```

and

```math
S\subseteq[L,15L/8),
\qquad
0\le k/L\le1/4.
```

The child completion descends to the parent completion

```math
2L+(4k-3k)=2L+k=R.
```

Thus a completion obstruction at the scheduled successor would imply a completion obstruction at the already valid parent step.

---

## 4. Half-separation obstruction disappears

The scheduled successor has

```math
\frac{R'}2=L'+2k.
```

Relative to the child shell, this asks whether `2k` lies in the raw parent `G`.

Because

```math
0<2k<L
```

and the smallest positive point of `G` is `L`, one has

```math
2k\notin G.
```

Therefore the successor has no half-separation obstruction.

The same argument persists because

```math
\frac{k_{n+1}}{L_{n+1}}
=
\frac12\frac{k_n}{L_n}.
```

---

## 5. Invariant shell geometry

Write

```math
q_n=\frac{\max S_n}{L_n},
\qquad
r_n=\frac{k_n}{L_n}.
```

The exact recurrence gives

```math
q_{n+1}
=
1+\frac{q_n+4+2r_n}{8},
```

```math
r_{n+1}=\frac{r_n}{2}.
```

At entry,

```math
q_0<7/4,
\qquad
r_0<1/2.
```

Hence

```math
q_1
<
1+\frac{7/4+4+1}{8}
=
\frac{59}{32}
<
\frac{15}{8},
```

and

```math
r_1<1/4.
```

The region

```math
q<15/8,
\qquad
r<1/4
```

is invariant, since

```math
q'
<
1+\frac{15/8+4+1/2}{8}
=
\frac{115}{64}
<
\frac{15}{8},
```

and `r'<1/8<1/4`.

Thus the enlarged top-layer and scheduled-descent classifications apply at every generation.

---

## 6. Terminal charge

For entry size `N`, replay multiplicity `P`, and scale `L`, the exact factor-eight tail has

```math
\boxed{
\sum_{n\ge0}W_n
=
\frac{4P(N+1)}L.
}
```

The charge is independent of the valid offset `k`.

---

## 7. Complete half-scale basin fan at `S_10`

For the recorded depth-ten state,

```math
L_{10}=536870912,
\qquad
|S_{10}|=265719,
\qquad
P_{10}=1024.
```

Consider

```math
1\le k<L_{10}/2.
```

There are exactly

```text
178956970
```

values with even two-adic valuation.

The complete exact factor-eight classification gives `54999` completion-blocked offsets, all below `260796`. Direct reconstruction of `S_10` gives

```text
29569
```

half-separation-blocked offsets in the half-scale range, from

```text
150994944 through 230535804.
```

The two obstruction classes are disjoint. Therefore

```math
\boxed{
178956970-54999-29569
=
178872402
}
```

valid offsets enter infinite exact tails.

This enlarges the previously certified `11129810`-offset basin fan by a factor of approximately

```math
16.0715.
```

It certifies infinite summable tails for approximately `43.75%` of all valid positive exact factor-eight children of `S_10`.

Every one has terminal charge

```math
\boxed{
\frac{33215}{16384}.
}
```

---

## 8. Scope

This theorem controls a large exact child family. It does not classify:

1. valid exact offsets with `k\ge L_{10}/2`;
2. factor-two or factor-four cheap escape candidates from `S_10`;
3. the whole continuation tree.

The principal remaining problem is still whole-tree Bellman compensation.