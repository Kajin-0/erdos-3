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

The scale-eight base state

```math
S_1
=
64+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free and produces two copies of the terminal progression

```math
16,21,26
```

with step `5` and the same root anchor.

An alternating base-eight three-translate construction doubles the number of identical-history copies at every level. There are computer-certified four-term-progression-free blocks `S_h` with

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

The ambient scale is exact:

```math
\boxed{
S_h\subseteq[L_h,2L_h),
\qquad
L_h=8^{h+1}.
}
```

Therefore

```math
\boxed{
\text{persistence}
=
2^h
=
\frac12L_h^{1/3}.
}
```

The full infinite family is certified four-term-progression-free by a 34-state base-eight automaton and a 17,238-state product/carry search. Absolute, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false without additional hypotheses.

The certificate is reproduced by

```text
src/verify_scale_eight_aligned_diamond.py
```

and documented in

```text
docs/scale-eight-self-replicating-aligned-diamond.md
```

### Sharp exact-model theorems

The canonical equal-translate obstruction is now quantitatively classified.

If one exact replication step has

```math
S\subseteq[L,2L),
\qquad
A=\{0\}\cup S,
```

```math
G=A\cup(A+R)\cup(A+2R),
```

and is translated into a standard dyadic shell

```math
L'+G\subseteq[L',2L'),
```

then uncontaminated backbone reproduction requires `R>=2L`. Since `2R in G`, one has `L'>4L`; because `L'/L` is a power of two,

```math
\boxed{L'\ge8L.}
```

Also, four equal translate layers are impossible because `0,R,2R,3R` would be a four-term progression. Thus three layers are maximal. Since the occurrence genealogy is binary, two persistent children are maximal. The canonical architecture therefore has the extremal one-step efficiency

```math
\boxed{
\rho_{\mathrm{exact}}
=
\frac{2\cdot3}{8}
=
\frac34.
}
```

After `h` exact generations,

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

The exact cardinality recurrence is

```math
n_{h+1}=3(n_h+1),
```

so every exact equal-translate genealogy satisfies

```math
\boxed{
P_h\alpha_h
\le
C_0P_h^{\log_2 3-2}
}
```

and

```math
\boxed{
\sum_hP_h\alpha_h
\le
4C_0,
\qquad
C_0=\frac{n_0+3/2}{L_0}.
}
```

The scale-eight family attains the exponents `1/3` and `2-log_2(3)`.

## Current bottleneck

The remaining theorem must control persistence outside the exact equal-translate model.

The exact obstruction already has summable multiplicity-weighted density, so any unresolved mechanism must involve at least one genuinely different feature:

1. overlapping or only partially resolved translate layers;
2. several parent states feeding one terminal history;
3. nonuniform branching or child counts;
4. approximate rather than exact recurrence;
5. persistence distributed across multiple dyadic shells;
6. many genealogies whose charges cannot be separated.

The active target is therefore

```math
\boxed{
\text{decompose general persistence into exact or near-exact genealogies plus a quantitatively cheaper error class.}
}
```

A useful next theorem would define a general local efficiency ratio and prove that every segment either stays structurally close to the exact `3/4` architecture or contracts by a uniformly stronger factor.

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
- `docs/research-decision-history.md` — audited PR history, superseded routes, permanent stop list, and documentation protocol.
- `docs/minimum-translation-backbone-recursion.md` — raw factor `3` and hybrid factor `2`.
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md` — exact within-state middle multiplicity fibers.
- `docs/global-lifted-center-layer-resolution.md` — different-center compression.
- `docs/state-anchor-layer-and-antichain-budget.md` — different-anchor compression and same-anchor budget.
- `docs/predecessor-anchor-layer-resolution.md` — predecessor and anchor-history compression.
- `docs/self-replicating-aligned-diamond.md` — original arbitrary-depth persistence construction.
- `docs/scale-eight-self-replicating-aligned-diamond.md` — exact scale-eight refinement and density benchmark.
- `docs/three-translate-dyadic-scale-barrier.md` — sharp `L' >= 8L` theorem for exact replication.
- `docs/exact-three-translate-weighted-density-theorem.md` — sharp weighted-density decay and summability in the exact model.
- `src/verify_scale_eight_aligned_diamond.py` — infinite-family automaton certificate.
- `src/verify_self_replicating_aligned_diamond_depth2.py` — original depth-two verifier.
- `docs/half-contraction-multiscale-label-potential.md` — all-generation moment potential.
- `docs/side-anchor-deletion-dag.md` — supporting affine deletion DAG.

All recent theorem-style claims are proved internally but await independent expert review.
