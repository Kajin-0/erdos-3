# Pair-lift coboundary cleaning

## Status

Concrete graph lemma.  This note isolates the next elementary combinatorial component of the pair-lift mode cocycle route.

Once line modes are lifted to antisymmetric edge labels

```math
\mu(a,b)=-\mu(b,a),
```

the first compatibility problem is no longer quadratic.  It is ordinary graph cohomology:

```math
\text{when is }\mu\text{ a coboundary }\Phi(a)-\Phi(b)?
```

The exact answer is simple; the robust sparse version is the needed graph-cleaning lemma.

## Exact coboundary criterion

Let `Gamma=(V,E)` be a connected undirected graph, and orient every edge both ways.  Let

```math
\mu:E^{or}\to F_p
```

satisfy

```math
\mu(b,a)=-\mu(a,b).
```

Then the following are equivalent.

1. There exists a potential

```math
\Phi:V\to F_p
```

such that

```math
\mu(a,b)=\Phi(a)-\Phi(b)
```

for every oriented edge `a -> b`.

2. Every oriented cycle has zero label-sum:

```math
\sum_{i=1}^k\mu(x_i,x_{i+1})=0,
\qquad x_{k+1}=x_1.
```

## Proof

If `mu=delta Phi`, then every cycle telescopes:

```math
\sum_i(\Phi(x_i)-\Phi(x_{i+1}))=0.
```

Conversely, fix a root `o`.  For each vertex `x`, choose a path

```math
o=x_0,x_1,\dots,x_k=x.
```

Define

```math
\Phi(x)=\sum_{i=0}^{k-1}\mu(x_i,x_{i+1}).
```

The zero-cycle condition makes this path-independent.  Then for any edge `a -> b`, comparing a root-to-`a` path followed by `a -> b` with a root-to-`b` path gives

```math
\Phi(b)=\Phi(a)+\mu(a,b).
```

Depending on orientation convention this is equivalent to

```math
\mu(a,b)=\Phi(b)-\Phi(a)
```

or, after replacing `Phi` by `-Phi`, to the convention used above.

Thus exact cocycle closure is exactly exact coboundary structure.

## Robust triangle cleaning lemma: dense-root form

The exact criterion uses all cycles.  For extraction, a triangle-root variant is more useful.

Let `Gamma=(V,E)` be a graph with antisymmetric edge labels `mu`.  Suppose there exists a vertex `o` such that many edges `a b` have both `o a` and `o b` present and satisfy the triangle identity

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

Define a potential on the neighborhood of `o` by

```math
\Phi_o(x)=\mu(x,o).
```

Then on every edge `a b` satisfying the above triangle identity,

```math
\mu(a,b)=\Phi_o(a)-\Phi_o(b).
```

Therefore, if one can find a popular root `o` for which a positive fraction of the edge weight lies in zero-sum triangles through `o`, one immediately obtains a large subgraph on which `mu` is a coboundary.

This is the simplest graph-cleaning mechanism.

## Weighted averaging principle

Suppose the active pair graph has a positive total weight of zero-sum triangles:

```math
\sum_{a,b,c}\omega_{ab}\omega_{bc}\omega_{ca}
1_{\mu(a,b)+\mu(b,c)+\mu(c,a)=0}
\ge \tau\, T_{\mathrm{tri}}.
```

Then by averaging there exists a root `o` such that the zero-sum triangles through `o` carry at least a `tau` fraction of the triangle weight incident to `o`.

If the graph has already been cleaned to avoid very uneven triangle distribution, this yields a large edge set on which

```math
\mu(a,b)=\Phi_o(a)-\Phi_o(b).
```

This is the graph-theoretic core of the sparse cocycle cleaning step.

## Why prior graph cleaning is still necessary

The dense-root argument can fail if zero-sum triangles are concentrated around a tiny exceptional vertex set.  In the main proof, such concentration is not just a nuisance; it may be useful because it indicates additive/low-rank structure in the spectral cloud.

Therefore the intended dichotomy is:

1. **concentrated triangle branch:** zero-sum compatibility concentrates in a small or low-rank part of the active graph, potentially giving a density increment or low-rank spectral structure;
2. **spread triangle branch:** after cleaning, a popular root produces a large coboundary subgraph.

This matches the BSG philosophy: either energy concentrates structurally, or popularization yields a cleaned structured object.

## From coboundary to quadratic potential

The coboundary conclusion gives

```math
\mu(a,b)=\Phi(a)-\Phi(b)
```

on a large active subgraph.  But the quadratic isotropic model predicts more:

```math
\Phi(x)=2Q_q(x).
```

Thus the next layer is to test whether the recovered potential has quadratic second differences.

For many additive parallelograms

```math
x,\quad x+h,\quad x+k,\quad x+h+k
```

inside the cleaned spectral cloud, a quadratic potential should satisfy

```math
\Phi(x+h+k)-\Phi(x+h)-\Phi(x+k)+\Phi(x)=B_q(h,k),
```

with the right-hand side bilinear in `(h,k)`.

Equivalently, third additive differences should vanish:

```math
\Delta_a\Delta_b\Delta_c\Phi(x)=0.
```

on a large structured subset.

## Candidate two-stage lemma

The pair-lift compatibility route should therefore be split into two lemmas.

### Lemma A: sparse cocycle cleaning

If the lifted mode labels `mu` satisfy many zero-sum cycle identities and no compatibility concentration already gives a low-rank/increment branch, then after graph cleaning there is a large subgraph and a potential `Phi` with

```math
\mu(a,b)=\Phi(a)-\Phi(b)
```

on most active edges.

### Lemma B: quadraticity of the potential

If this potential arises from line modes of the factorized pair functions

```math
H_{a,b}(t)=c_{a+t(a+b)}c_{b-t(a+b)},
```

and the active graph has enough additive parallelograms, then either `Phi` agrees with a quadratic phase on a large structured subset or the failures reveal low-rank/additive concentration.

## Immediate proof task

Prove Lemma A in a precise weighted graph model first.  It is independent of Fourier analysis.

Then identify which zero-sum triangles are actually forced by the shear extraction.  If the extraction only gives line-mode biases but not triangle identities, an additional phase-comparison step is needed before Lemma A can be applied.
