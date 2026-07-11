# Erdős Problem #3: harmonic arithmetic progressions

This repository develops a partial-progress attack on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open.

The active program studies four-term-progression-free sets using a multiscale side-anchor deletion DAG. Three complementary results are now central:

- a binary lower-scale occurrence recursion with harmonic factor `8/3`;
- a binary multiplicity-resolving recursion with factor `5/3`, which keeps one distinct copy of every middle step and converts repeated copies into lower-scale center-difference children;
- a half-contraction theorem giving a conserved linear-label potential and contracting higher label moments across all generations.

The remaining gap is concentration of cross-state multiplicity near the smallest labels.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain and current gap.
- `docs/certainty-ledger.md` — status, confidence, and audit state of the main claims.
- `docs/full-middle-binary-eight-thirds-recursion.md` — strongest raw occurrence theorem.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — within-node multiplicity resolution.
- `docs/half-contraction-multiscale-label-potential.md` — global all-generation label-moment potential.
- `docs/spanning-forest-binary-four-thirds-recursion.md` — structural balance used by both recursions.
- `docs/deletion-dag-merge-difference-recursion.md` — indegree excess and merge-difference children.
- `docs/side-anchor-deletion-dag.md` — affine deletion-DAG construction.

## One-block setup

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

run side-anchor deletion until a three-term-progression-free residual of size

```math
s\le r_3(N)
```

remains. Put

```math
K=|D|-s.
```

The selected progressions define an acyclic graph in which every deleted sponsor points to the two surviving points of its selected three-term progression.

## Structural children

If `rho` is the number of indegree-zero vertices, translating incoming sponsors at each target gives lower-scale four-term-progression-free children `Delta_v` with

```math
\sum_v|\Delta_v|=K-s+\rho.
```

Choosing one incoming edge for each nonroot DAG vertex gives a spanning forest. Translating each forest component by its smallest element gives lower-scale four-term-progression-free children `Theta_j` with

```math
\sum_j|\Theta_j|=K+s-\rho.
```

Therefore

```math
\boxed{
\sum_v|\Delta_v|+\sum_j|\Theta_j|=2K.
}
```

Retaining at most one structural occurrence per parent element preserves at least `2K/3` structural occurrences and harmonic mass at least

```math
\frac{2K}{3N}.
```

## Raw full-middle recursion

For every selected progression centered at `x` with common difference `q`, place `q` in

```math
M_x=\{q_i:b_i=x\}.
```

Each `M_x` is four-term-progression-free. Every selected step satisfies `q<=N/2`, so

```math
\sum_xH(M_x)\ge\frac{2K}{N}.
```

Keeping every middle occurrence and at most one structural occurrence per parent gives a binary genealogy satisfying

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is the strongest raw occurrence bound. It counts repeated numerical labels separately.

## Middle multiplicity resolution

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the distinct selected steps. For each `q in Q`, let

```math
X_q=\{b_i:q_i=q\}
```

be its set of centers, and define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Each `Xi_q` is four-term-progression-free and lies in `[1,N)`. The exact multiplicity identity is

```math
\boxed{
|Q|+\sum_{q\in Q}|\Xi_q|=K.
}
```

Thus one copy of each distinct step is retained as terminal distinct harmonic mass, while every additional occurrence becomes a lower-scale recursive child.

Combining this with the thinned structural family gives a binary hybrid inequality:

```math
\boxed{
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
\sum H(\text{retained structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

This factor is smaller than `8/3`, but it resolves all middle-label multiplicity within one parent node.

## Half-contraction and global label potential

The coordinated side-anchor orientation depends only on the step `q`. For two selected progressions with the same `q`, the difference of their centers equals the difference of their sponsors. Consequently every multiplicity-fiber label associated with sponsor `a` is at most `a/2`.

The retained structural labels and terminal representative steps are also at most half their associated parent label. Therefore every parent produces at most two outputs, each at most half the parent.

For every real `p>=1`, the outputs of one parent `a` satisfy

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the full recursive tree, if `mu(q)` is the total multiplicity of terminal numerical label `q`, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root occurrence}}a^p
\qquad(p\ge1).
}
```

In particular,

```math
\boxed{
\sum_q\mu(q)q
\le
\sum_a a.
}
```

Every recursive path has length at most `floor(log_2 a_0)` when it starts at label `a_0`.

This is the first bounded all-generation potential controlling cross-state terminal multiplicity. It rules out uncontrolled repetition at moderate and large labels, but does not yet control repetition concentrated near label `1`.

## Central gap

The unresolved regime is now

```math
\boxed{
\text{small-label concentration}
\quad+
\text{cross-state multiplicity}
\quad+
\text{genealogical overlap}.
}
```

The approved closing targets are:

1. prove that excessive multiplicity at the bottom scales forces additional distinct labels;
2. construct a potential that combines reciprocal weight with the positive-moment bounds;
3. prove an additive-energy bound for repeated small terminal labels across states;
4. computationally search for multigeneration examples concentrating terminal mass near `1`.

## Research discipline

- Recent theorem-style lemmas are proved in the repository but await independent expert review.
- Occurrence mass and distinct mass must always be reported separately.
- New proof language should be added only when it proves or falsifies an explicit closing target.
- Counterexamples and superseded routes remain documented so false approaches are not revived.

## Earlier computational program

The PB/MaxSAT, modular digit-set, shifted Kempner, and DFA tools remain useful for finite extremizer exploration and reproducible computation. They are supporting or legacy work rather than the active route to the full problem.

No recent deletion-DAG theorem has yet received independent expert review. The full Erdős problem remains unresolved.