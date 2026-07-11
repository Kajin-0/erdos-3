# Erdős Problem #3: harmonic arithmetic progressions

This repository develops partial progress on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The active project studies the four-term-progression-free case.

## Strongest one-generation recursion

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

Let

```math
m=\min D
```

and define the minimum-translation backbone

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}.
```

Then `B(D)` is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and every associated output satisfies

```math
d-m\le d/2.
```

### Raw occurrence factor three

Keeping every selected middle occurrence and the backbone gives a binary genealogy with

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

Equal numerical labels are counted repeatedly.

### Multiplicity-resolving factor two

Let `Q` be the set of distinct selected middle steps. Repeated copies of each `q in Q` are converted exactly into lower-scale center-difference children `Xi_q` satisfying

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

Combining these fibers with the backbone gives

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
\sum_{a\text{ root}}a^p.
}
```

Recursive depth is logarithmic.

## Exact multiplicity compression

Every recursive state has the form

```math
S=B-t,
\qquad
B\subseteq D_{\mathrm{root}},
\qquad
t\in\{0\}\cup D_{\mathrm{root}}.
```

Repeated terminal copies are compressed in stages:

1. Different lifted centers are exported by center-difference layers.
2. For one exact lifted progression, different root anchors are exported by anchor-difference layers.
3. Different predecessor anchors are exported by predecessor-difference layers.
4. Same-anchor copies obey the antichain budget
   ```math
   \lambda_{x,q}(t)(a-t)\le a.
   ```

After iterating through the anchor history, the residual consists of identical local progressions produced by state occurrences with the same complete anchor history.

## Self-replicating aligned diamonds

That final residual can grow polynomially.

The base state

```math
S_1
=
32+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free and produces two copies of the terminal progression

```math
16,21,26
```

with step `5` and the same root anchor.

A recursive three-translate construction doubles the number of identical-history copies at every level. There are four-term-progression-free blocks `S_h` with

```math
\boxed{
\text{identical-history terminal multiplicity}=2^h
}
```

and

```math
\boxed{
|S_h|
=
\frac{9\cdot3^h-3}{2}.
}
```

Therefore

```math
\boxed{
\text{persistence}
\asymp
|S_h|^{\log_3 2}.
}
```

Absolute, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false without additional hypotheses.

The depth-two 39-point instance produces four terminal copies with the same complete anchor history. It is verified by

```text
src/verify_self_replicating_aligned_diamond_depth2.py
```

## Current bottleneck

The remaining theorem must be density-sensitive.

The self-replicating construction is sparse in its ambient interval, so it does not yield a divergent reciprocal-sum counterexample. The active target is now

```math
\boxed{
\text{prove that blocks carrying substantial reciprocal mass cannot sustain aligned-diamond replication efficiently across scales.}
}
```

Useful forms would include:

1. a tradeoff between persistence multiplicity and block density;
2. a lower bound on ambient scale required for `h` replication levels;
3. a potential coupling reciprocal mass to the `3`-for-`2` size growth of the gadget;
4. a theorem showing that near-extremal replication consumes a summable amount of dyadic density.

## Supporting deletion-DAG theory

The deletion-DAG merge and spanning-component identities remain valid:

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

They are no longer needed for the strongest one-generation constants, but remain possible ingredients in a density-sensitive replication theorem.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain and current gap.
- `docs/certainty-ledger.md` — claim status, confidence, and audit state.
- `docs/minimum-translation-backbone-recursion.md` — raw factor `3` and hybrid factor `2`.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — exact within-state middle multiplicity fibers.
- `docs/global-lifted-center-layer-resolution.md` — different-center compression.
- `docs/state-anchor-layer-and-antichain-budget.md` — different-anchor compression and same-anchor budget.
- `docs/predecessor-anchor-layer-resolution.md` — predecessor and anchor-history compression.
- `docs/self-replicating-aligned-diamond.md` — arbitrary-depth persistence construction.
- `src/verify_self_replicating_aligned_diamond_depth2.py` — depth-two verifier.
- `docs/half-contraction-multiscale-label-potential.md` — all-generation moment potential.
- `docs/side-anchor-deletion-dag.md` — supporting affine deletion DAG.

All recent theorem-style claims are proved internally but await independent expert review.