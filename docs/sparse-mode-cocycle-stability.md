# Sparse mode cocycle stability

## Status

Extraction target and barrier note.  This note refines the line-mode compatibility problem into a sparse cocycle-stability problem.

The previous compatibility equations identify what a true quadratic model predicts:

```math
m(w,r)\approx 2B(w,r).
```

However, in the actual shear extraction, `m(w,r)` is not observed everywhere.  It is observed only on an active weighted incidence set of pairs `(w,r)` where the line function

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}
```

has enough mass and enough shift-autocorrelation.  Therefore ordinary bilinear reconstruction is not immediately applicable.

The real task is:

```math
\text{sparse many local compatibilities}
\Rightarrow
\text{large cleaned subgraph with bilinear mode field}.
```

## Active incidence graph

Let

```math
\mathcal I\subseteq \{(w,r): w\ne0,\ r\in G/\langle w\rangle\}
```

be the family of line fibers produced by fixed-`w` extraction.

Attach a weight

```math
\omega(w,r)\approx E(H_{w,r})
```

or the extracted negative/autocorrelation mass, and a mode value

```math
m(w,r)\in F_p.
```

The compatibility extraction should not require every pair `(w,r)`.  It should work with a positive-weight incidence set `mathcal I`.

## Mandatory exact symmetries

Before attempting any additive reconstruction, clean `mathcal I` so that it is approximately closed under the two exact symmetries.

### Representative gauge

For all `s in F_p`,

```math
(w,r)\sim(w,r+sw)
```

and

```math
m(w,r+sw)=m(w,r).
```

Thus the true domain is a quotient.  Any extraction should choose canonical representatives or work intrinsically on `G/<w>`.

### Reversal

The reversal map is

```math
R(w,r)=(w,w-r),
```

and true modes satisfy

```math
m(R(w,r))=-m(w,r).
```

If extracted modes fail this symmetry on a large fraction of weighted fibers, then the line-mode extraction is not coherent enough to imply a quadratic phase.  That failure should be treated as a noise branch, not as structure.

## Local bilinear tests

A bilinear model predicts

```math
m(w,r)=2B(w,r).
```

Therefore the following local tests are necessary.

### Base additivity at fixed direction

For fixed `w`, if `r_1,r_2,r_1+r_2` are all active modulo `<w>`, then

```math
m(w,r_1+r_2)=m(w,r_1)+m(w,r_2).
```

This is a one-direction linearity test.

### Direction additivity at fixed base

If `w_1,w_2,w_1+w_2` are active with a common compatible base `r`, then

```math
m(w_1+w_2,r)=m(w_1,r)+m(w_2,r).
```

This is harder because the quotient gauges change with the direction.

### Rectangle/cocycle identity

The most invariant local test is the rectangle identity:

```math
m(w_1,r_1)+m(w_2,r_2)
-m(w_1,r_2)-m(w_2,r_1)=0
```

whenever all four incidences are active and the quotient representatives are compatible.

For a bilinear form this identity is automatic after interpreting representatives correctly.  A large supply of such identities is the natural input for a BSG-type cocycle-stability theorem.

## Why graph cleaning is required

Sparse local identities can be misleading.  A mode field may look bilinear on many isolated rectangles without containing a large bilinear component.

Thus the extraction needs a graph-cleaning step:

1. discard low-weight or low-degree fibers;
2. pass to popular directions `W` and popular base classes `R_w`;
3. keep only incidences participating in many compatible rectangles;
4. then attempt bilinear reconstruction on the cleaned subgraph.

This is the analogue of the popular-differences step in Balog--Szemeredi--Gowers arguments.

## Candidate sparse cocycle-stability lemma

A useful lemma would be:

> Let `mathcal I` be a weighted incidence set of pairs `(w,r)` with mode values `m(w,r)`.  Suppose:
>
> 1. `mathcal I` has positive weighted density in the shear-extracted family;
> 2. `m` satisfies representative invariance and reversal symmetry on most of the weight;
> 3. a positive proportion of compatible rectangles in `mathcal I` satisfy the cocycle identity;
> 4. the projection to directions and base classes has no low-rank concentration already yielding an increment.
>
> Then there is a large cleaned sub-incidence set `mathcal I'` and a bilinear form `B` such that
>
> ```math
> m(w,r)=2B(w,r)
> ```
>
> for most `(w,r) in mathcal I'`, up to the extracted mode uncertainty.

This is the precise replacement for a vague statement that modes are compatible.

## Relation to BSG

The lemma is BSG-like in three ways:

1. the input is many local algebraic relations, not a global homomorphism;
2. the conclusion is obtained only after passing to a popular cleaned subset;
3. failure of the conclusion should expose concentration or nonrandom structure, which in the main proof would become a density increment branch.

The closest formal analogy is not ordinary additive energy of a set, but stability of an approximate bilinear cocycle on a sparse graph.

## How this connects back to the shear sum

The chain now becomes:

```math
\text{large shear contribution}
\Rightarrow
\text{many line-mode biases}
\Rightarrow
\text{weighted sparse mode field }m(w,r)
\Rightarrow
\text{many local cocycle identities}
\Rightarrow
\text{bilinear }B
\Rightarrow
\text{quadratic phase/cocycle or low-rank increment}.
```

The first implication is analytic and already mostly elementary.  The middle implication is combinatorial and currently the main missing lemma.

## Immediate proof task

Define compatible rectangles intrinsically, without choosing inconsistent quotient representatives.

A clean approach is to lift `(w,r)` to actual paired points

```math
(a,b)=(r+tw,w-r-tw),
\qquad a+b=w,
```

and express mode values as functions of unordered spectral pairs `{a,b}`.  The rectangle identities should then be written in terms of four or six spectral points rather than quotient representatives.

This may remove gauge ambiguity and reveal the correct cocycle complex.
