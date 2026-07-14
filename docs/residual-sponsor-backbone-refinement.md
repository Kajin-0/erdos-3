# Residual-sponsor refinement of the minimum backbone

## Status

Symbolic refinement of coordinated side-anchor deletion for affine states.

The ordinary minimum-translation backbone contains translated copies of every parent root except the minimum. A completed deletion schedule already partitions the parent roots into:

1. a three-AP-free residual root set;
2. deleted sponsor roots.

This note proves that the backbone may be split along that partition without losing any point or harmonic mass. The translated residual part is terminal immediately. Only sponsor-root backbone points need remain recursively active.

The theorem is independent of the finite retained policy. Whether the refined split improves a particular maximum-harmonic retained quotient is a separate exact computation.

---

## 1. Affine setup

Let

```math
S_r(P)=\{p-r:p\in P\},
\qquad
r<\min P.
```

Run a complete coordinated side-anchor deletion schedule on `S_r(P)`. Let

```math
P=Q\sqcup\Sigma,
```

where:

- `Q` consists of roots whose current points remain in the terminal residual;
- `\Sigma` consists of roots whose current points are selected as sponsors and deleted.

Completeness of the schedule gives

```math
S_r(Q)
```

three-AP-free.

Because translation preserves arithmetic progressions,

```math
Q
```

itself is three-AP-free.

---

## 2. Ordinary backbone

Let

```math
a=\min P.
```

The ordinary minimum backbone is

```math
\mathcal B(S_r(P))
=
S_a(P\setminus\{a\}).
```

Its numerical support is

```math
\{p-a:p\in P,\ p>a\}.
```

---

## 3. Exact residual-sponsor split

Define

```math
\mathcal B_Q
=
S_a(Q\setminus\{a\}),
```

and

```math
\mathcal B_\Sigma
=
S_a(\Sigma\setminus\{a\}).
```

Then the root partition and injectivity of `p\mapsto p-a` give

```math
\boxed{
\mathcal B(S_r(P))
=
\mathcal B_Q
\sqcup
\mathcal B_\Sigma.
}
```

Therefore

```math
\boxed{
H(\mathcal B(S_r(P)))
=
H(\mathcal B_Q)
+
H(\mathcal B_\Sigma).
}
```

No support and no harmonic mass are lost.

---

## 4. The residual backbone is terminal

Since `Q` is three-AP-free, every translate and every subset of `Q` is three-AP-free. Hence

```math
\boxed{
\mathcal B_Q
\text{ is three-AP-free.}
}
```

After dyadic shelling, every shell of `\mathcal B_Q` remains three-AP-free and may be emitted as terminal output.

Thus roots that survived the parent deletion schedule never need to be carried recursively merely because they also occur in the minimum backbone.

---

## 5. Recursive root universe

The sponsor backbone has active roots in `\Sigma` and reference root `a`.

Every middle-fiber point also has sponsor-root provenance. For a fixed step `q`, its affine root set is a subset of the sponsor roots selected at that step. Since each parent point is deleted as sponsor at most once, the sponsor classes for distinct selected actions partition `\Sigma`.

Consequently:

```math
\boxed{
\text{every recursively continuing active root after the refined transition belongs to }\Sigma.
}
```

References may include:

- the minimum root `a`, which may lie in `Q` or `\Sigma`;
- an omitted sponsor root `t_0\in\Sigma` for a middle fiber.

But all active child root labels belong to the sponsor core `\Sigma`.

---

## 6. Refined one-generation inequality

The established exact local inequality is

```math
H(S_r(Q))
+
\sum_q H(\Xi_q)
+
H(\mathcal B(S_r(P)))
\ge
2H(S_r(P))
-
\frac{r_3(N)}N
-
\frac1N.
```

Using the exact backbone split gives

```math
\boxed{
H(S_r(Q))
+
H(\mathcal B_Q)
+
\sum_q H(\Xi_q)
+
H(\mathcal B_\Sigma)
\ge
2H(S_r(P))
-
\frac{r_3(N)}N
-
\frac1N.
}
```

The first two terms are terminal. The only potentially recursive terms are:

```math
\mathcal B_\Sigma
```

and the middle fibers.

Thus the same harmonic-production theorem may be rewritten with a strictly smaller recursive root universe and no change in the lower bound.

---

## 7. Pair-resource consequence

Under the ordinary backbone, recursive latent pair capacity can include pairs among all roots in `P\setminus\{a\}`.

Under the refined split, recursive latent pair capacity is restricted to sponsor roots:

```math
\boxed{
\text{recursive latent pairs}
\subseteq
\binom\Sigma2.
}
```

Recursive current pairs are of two forms:

1. sponsor-backbone pairs `(a,s)` with `s\in\Sigma`;
2. middle-fiber pairs `(t_0,t)` with `t_0,t\in\Sigma`.

Therefore the refined recursively active resource universe is contained in

```math
\{(a,s):s\in\Sigma\}
\cup
\binom\Sigma2.
```

If `a\in\Sigma`, this is simply a subset of `\binom\Sigma2`. If `a\in Q`, the only cross residual-sponsor resources are the sponsor-backbone star pairs `(a,s)`.

---

## 8. Why the refinement matters

The full latent pair energy

```math
J(P)
```

is generally too large to serve as an economical initial potential. The refinement replaces future latent capacity by

```math
J(\Sigma),
```

while terminalizing both:

- the original residual `S_r(Q)`;
- its translated backbone copy `S_a(Q\setminus\{a\})`.

This converts the activation problem into a sponsor-core problem:

```math
\boxed{
\text{bound pair energy of roots actually used to resolve three-APs, not all parent pairs.}
}
```

The sponsor core is schedule dependent. A final theorem may choose a deletion policy that balances:

- terminal residual mass;
- sponsor-core size and pair energy;
- middle-fiber structure;
- future completion or rectangle obstruction.

---

## 9. Compatibility with retention

The residual and sponsor backbone pieces have disjoint numerical support and together equal the original backbone support.

Therefore replacing one raw backbone occurrence by the two refined occurrences:

- preserves the raw support union;
- preserves raw harmonic occurrence mass;
- creates no new point overlap between the two pieces;
- permits the residual piece to be classified terminal before retained-child selection.

A retained quotient may then optimize over the refined states. It can reproduce the support of any previously selected backbone by choosing both pieces, while gaining the option to retain or discard them independently when conflicts with other outputs differ.

---

## 10. Open questions

The symbolic split does not itself prove that the sponsor core has summable pair energy.

The next exact and analytical questions are:

1. how much recursive point and pair mass is removed on the recorded frontiers?
2. does maximum-harmonic retention select both refined pieces or exploit the additional flexibility?
3. can `J(\Sigma)` be bounded by weighted selected-progression incidence?
4. does sponsor uniqueness imply a useful matching, forest, or energy inequality?
5. can policy selection minimize sponsor-core pair energy while preserving the local harmonic lower bound?
6. do large sponsor cores necessarily create completion, rectangle, or cheap-extension exclusion?

The refinement is useful only if one of these questions yields a state-independent transfer law.

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
