# Erdős Problem #3: harmonic arithmetic progressions

This repository develops partial progress on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The active program studies the four-term-progression-free case through a multiscale side-anchor deletion DAG.

## Current central results

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

run side-anchor deletion until a three-term-progression-free residual of size

```math
s\le r_3(N)
```

remains, and write

```math
K=|D|-s.
```

The selected progressions define an affine DAG. Two structural child families satisfy the exact balance

```math
\boxed{
\sum_v|\Delta_v|+\sum_j|\Theta_j|=2K.
}
```

After retaining at most one structural occurrence per parent element, at least `2K/3` structural occurrences remain.

### Raw occurrence recursion

For each selected progression with center `x` and step `q`, put `q` in the full middle child

```math
M_x=\{q_i:b_i=x\}.
```

Each `M_x` is four-term-progression-free, and

```math
\sum_xH(M_x)\ge\frac{2K}{N}.
```

Keeping every middle occurrence and at most one structural occurrence per parent gives a binary occurrence genealogy with

```math
\boxed{
\sum H(\text{children})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is the strongest raw occurrence theorem. It counts repeated numerical labels separately.

### Within-node multiplicity resolution

Let `Q` be the set of distinct selected middle steps. For each `q in Q`, let `X_q` be its selected centers and define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Then

```math
\boxed{
|Q|+\sum_q|\Xi_q|=K.
}
```

One copy of each distinct step is retained as terminal mass, and every additional copy becomes a lower-scale four-term-progression-free child. Adding the retained structural family gives

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
\sum H(\text{structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

### Half-contraction potential

Every retained output associated with parent label `a` is at most `a/2`, and every parent produces at most two outputs. Hence, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across all generations, if `mu(q)` is total terminal multiplicity, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Recursive depth is logarithmic.

## Shell interface

A child family generally lies in `[1,N)` rather than in one ratio-two block. Before reapplying the deletion theorem, each child is partitioned into standard dyadic shells

```math
[2^j,2^{j+1}).
```

Harmonic mass is additive across this partition. Claims about repeated terminal progressions must therefore be checked after shell decomposition, not only in the unshelled child set.

The original 31-element sibling-overlap example was only an algebraic precursor. The corrected 34-element construction in

```text
docs/dyadic-shell-compatible-sibling-sharpness.md
```

proves that the same terminal label can occur in both a middle-fiber shell and a spanning-component shell. Its verifier is

```text
src/verify_dyadic_shell_sibling_sharpness.py
```

## Global lifted-center resolution

Every recursive state has the form

```math
S=B-t,
\qquad B\subseteq D,
```

for the original root block `D`. A terminal step `q` in `S` therefore lifts to a three-term progression

```math
x-q,
\quad x,
\quad x+q
```

inside `D`.

Let `nu_q(x)` be the number of terminal occurrences of `q` lifting to center `x`, and let

```math
L(q)=\max_x\nu_q(x).
```

Define the nested center layers

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Translating each nonempty layer by its minimum gives lower-scale four-term-progression-free children `Omega_{q,k}` and the exact identity

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus all cross-state repetition occurring at different lifted centers is exported. The remaining multiplicity is

```math
\boxed{
L(q)=\text{the number of recursive states reusing one exact lifted }q\text{-progression}.
}
```

## Current bottleneck

The active target is now an exact-progression persistence theorem:

```math
\boxed{
\text{control how often one fixed lifted progression can survive through the recursive genealogy.}
}
```

The translated-gadget amplification shows that raw fixed-label multiplicity can be polynomially large, but those copies occur at different lifted centers and are handled by the global layer decomposition.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain and current gap.
- `docs/certainty-ledger.md` — claim status, confidence, and audit state.
- `docs/full-middle-binary-eight-thirds-recursion.md` — strongest raw occurrence theorem.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — within-node multiplicity resolution.
- `docs/half-contraction-multiscale-label-potential.md` — global label-moment potential.
- `docs/global-lifted-center-layer-resolution.md` — cross-state center-layer decomposition.
- `docs/dyadic-shell-compatible-sibling-sharpness.md` — shell-compatible two-layer sharpness.
- `docs/side-anchor-deletion-dag.md` — deletion-DAG construction.

All recent theorem-style claims are proved internally but await independent expert review.