# Erdős Problem #3: harmonic arithmetic progressions

This repository develops partial progress on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The active project studies the four-term-progression-free case.

## Current shortest recursion

Fix a four-term-progression-free block

```math
D\subseteq[N,2N).
```

Run coordinated side-anchor deletion until a three-term-progression-free residual of size

```math
s\le r_3(N)
```

remains, and put

```math
K=|D|-s.
```

### Minimum-translation backbone

Let

```math
m=\min D
```

and define

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}.
```

Then

```math
\mathcal B(D)\subseteq[1,N),
```

`B(D)` is four-term-progression-free, and

```math
|\mathcal B(D)|=|D|-1.
```

Each backbone label associated with parent `d` satisfies

```math
d-m\le d/2.
```

### Raw full-middle factor three

Every selected progression contributes one middle-step occurrence `q<=N/2`. Keeping every middle occurrence and the backbone child gives a binary occurrence genealogy satisfying

```math
\boxed{
H(\mathcal B(D))
+
\sum_xH(M_x)
\ge
3H(D)
-
2\frac{r_3(N)}N
-
\frac1N.
}
```

This is the strongest raw occurrence theorem. Equal numerical labels are counted repeatedly.

### Multiplicity-resolving factor two

Let `Q` be the set of distinct selected steps. For every `q in Q`, translate the other selected centers by the minimum center to obtain a lower-scale four-term-progression-free child `Xi_q`. Then

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

One copy of each distinct step becomes terminal harmonic mass, and every additional copy becomes a recursive child. Combining this exact resolution with the backbone gives

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
H(\mathcal B(D))
\ge
2H(D)
-
\frac{r_3(N)}N
-
\frac1N.
}
```

The genealogy remains binary.

## Half-contraction potential

Every retained output associated with parent label `a` is at most `a/2`, and every parent creates at most two outputs. Hence, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across all generations,

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p,
}
```

where `mu(q)` is total terminal multiplicity. Recursive depth is logarithmic.

## Multiplicity compression

Every recursive state has the form

```math
S=B-t,
\qquad
B\subseteq D_{\mathrm{root}},
\qquad
t\in\{0\}\cup D_{\mathrm{root}}.
```

### Different lifted centers

For fixed terminal step `q`, group occurrences by their lifted center `x` in the root block. Nested center layers export every repeated copy occurring at a different center to lower-scale four-term-progression-free difference children.

### Different root anchors

For one exact lifted progression, group copies by the root translation anchor `t`. Nested anchor layers export every repeated copy occurring with a different anchor.

The remaining copies have the same:

- terminal step;
- lifted center;
- root sponsor;
- root translation anchor;
- local sponsor label.

### Same-anchor antichain budget

Let

```math
a=x-\sigma(q)q
```

be the root sponsor. In a state anchored at `t`, the local sponsor label is

```math
s=a-t.
```

Copies with the same anchor all have label `s` and form an antichain in the half-contracting occurrence tree. Therefore

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

Equivalently,

```math
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{a-t}\right\rfloor.
```

High same-anchor multiplicity can occur only when `t` lies very close to `a`.

## Sharp aligned diamond

A 12-point four-term-progression-free block shows that the same local progression can occur in both

1. a middle multiplicity-fiber child;
2. the minimum-translation backbone child;

with the same root anchor.

The duplicated progression is

```math
16,21,26
```

with terminal step `5`. Thus a universal one-copy-per-anchor theorem is false. One parent can create two aligned copies, and this local bound is sharp.

See:

- `docs/minimum-backbone-aligned-diamond-counterexample.md`
- `src/verify_minimum_backbone_aligned_diamond.py`

## Current bottleneck

The unresolved object is now precise:

```math
\boxed{
\text{one identical local progression repeated across incomparable recursive states with the same anchor.}
}
```

The next target is predecessor-anchor convergence. A closing theorem must either

1. export convergence diamonds to additional lower-scale difference structure;
2. show that repeated aligned convergence forces a forbidden affine configuration;
3. construct a density-sensitive potential that controls the residual same-anchor multiplicity.

## Supporting deletion-DAG theory

The deletion-DAG merge and spanning-component results remain valid and useful for overlap geometry:

```math
\sum_v|\Delta_v|=K-s+\rho,
```

```math
\sum_j|\Theta_j|=K+s-\rho,
```

and

```math
\sum_v|\Delta_v|+
\sum_j|\Theta_j|=2K.
```

They are no longer needed for the strongest one-generation constants, but remain possible ingredients in a convergence-diamond theorem.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain and current gap.
- `docs/certainty-ledger.md` — claim status, confidence, and audit state.
- `docs/minimum-translation-backbone-recursion.md` — raw factor `3` and hybrid factor `2`.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — exact within-state middle multiplicity fibers.
- `docs/global-lifted-center-layer-resolution.md` — different-center compression.
- `docs/state-anchor-layer-and-antichain-budget.md` — different-anchor compression and same-anchor budget.
- `docs/half-contraction-multiscale-label-potential.md` — all-generation moment potential.
- `docs/minimum-backbone-aligned-diamond-counterexample.md` — sharp same-anchor sibling event.
- `docs/side-anchor-deletion-dag.md` — supporting affine deletion DAG.

All recent theorem-style claims are proved internally but await independent expert review.