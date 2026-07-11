# Erdős Problem #3: harmonic arithmetic progressions

This repository develops a partial-progress attack on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open.

The active program studies four-term-progression-free sets using a multiscale side-anchor deletion DAG. Two complementary theorems are now central:

- a binary lower-scale occurrence recursion with harmonic factor `8/3`;
- a binary multiplicity-resolving recursion with factor `5/3`, which keeps one distinct copy of every middle step and converts repeated copies into lower-scale four-term-progression-free center-difference children.

The remaining gap is repetition across different parent states together with rapid scale contraction.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain and current gap.
- `docs/certainty-ledger.md` — status, confidence, and audit state of the main claims.
- `docs/full-middle-binary-eight-thirds-recursion.md` — strongest raw occurrence theorem.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — current multiplicity-resolution theorem.
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

## Central gap

The remaining unresolved issue is no longer within-node repetition. It is repetition across different recursive states:

```math
\boxed{
\text{cross-state multiplicity}
\quad+
\text{scale contraction}
\quad+
\text{genealogical overlap}.
}
```

The approved closing targets are:

1. group equal terminal steps across sibling or same-depth states and export repeated copies to lower-scale fibers;
2. construct a potential that counts each terminal numerical label once;
3. prove a bounded-energy or bounded-multiplicity theorem for equal labels across states;
4. prove a stopping theorem for repeated rapid contraction.

## Research discipline

- Recent theorem-style lemmas are proved in the repository but await independent expert review.
- Occurrence mass and distinct mass must always be reported separately.
- New proof language should be added only when it proves or falsifies an explicit closing target.
- Counterexamples and superseded routes remain documented so false approaches are not revived.

## Earlier computational program

The PB/MaxSAT, modular digit-set, shifted Kempner, and DFA tools remain useful for finite extremizer exploration and reproducible computation. They are supporting or legacy work rather than the active route to the full problem.

No recent deletion-DAG theorem has yet received independent expert review. The full Erdős problem remains unresolved.
