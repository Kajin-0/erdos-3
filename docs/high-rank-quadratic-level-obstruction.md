# High-rank quadratic level obstruction

## Status

Proof-audit obstruction note.  This note stress-tests the high-rank branch of the quadratic-correlation route.  A density increment on a high-rank quadratic level set is not the same as an affine-subspace density increment; internal 4APs in a quadratic level set obey additional isotropic-direction constraints.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let

```math
q:G -> F_p
```

be a quadratic polynomial with high-rank homogeneous quadratic part `q_2`.

For a level

```math
V_t={x in G:q(x)=t},
```

suppose the pure `U^3` branch has produced a density increment

```math
|A cap V_t|/|V_t| >= alpha+rho.
```

The question is whether this implies a useful 4AP recurrence statement.

## 4APs inside one quadratic level set

Consider a 4AP

```math
x,
quad x+d,
quad x+2d,
quad x+3d.
```

The map

```math
i -> q(x+id)
```

is a polynomial in `i` of degree at most `2`.

If all four points lie in the same level set `V_t`, then this degree-2 polynomial takes the same value at `i=0,1,2,3`.  Since `p>4`, it must be constant.

Therefore internal 4APs in `V_t` are exactly those pairs `(x,d)` satisfying:

```math
q(x)=t,
```

```math
q_2(d)=0,
```

and

```math
q(x+d)-q(x)=0.
```

The second condition says that the common difference is isotropic for the quadratic part.  The third is a derivative/orthogonality condition depending on `x` and `d`.

## Counting scale for high rank

For a high-rank nondegenerate quadratic form, the isotropic cone

```math
{d:q_2(d)=0}
```

has size about

```math
p^{n-1}.
```

For each nonzero isotropic `d`, the condition

```math
q(x+d)-q(x)=0
```

is essentially one nontrivial affine-linear condition on `x`, and `q(x)=t` is one quadratic condition.

Thus the expected number of internal 4AP parameter pairs `(x,d)` in `V_t` is on the scale

```math
p^{2n-3}
```

up to constants depending on `p` and rank-error terms.

Equivalently, among all pairs `(x,d) in G^2`, internal 4APs in a fixed high-rank level set have density about

```math
p^{-3}.
```

This is a positive constant-density algebraic AP hypergraph when `p` is fixed, but it is not the full affine AP hypergraph.

## Why this is not an immediate proof

A density increment on `V_t` gives a set

```math
A_t=A cap V_t
```

with density about `alpha+rho` relative to `V_t`.

To force a 4AP in `A_t`, one needs a relative recurrence theorem for the algebraic AP hypergraph

```math
q(x)=t,
qquad
q_2(d)=0,
qquad
q(x+d)=q(x).
```

This is a different object from ordinary affine-subspace recurrence.

The naive random heuristic would predict about

```math
(alpha+rho)^4 p^{2n-3}
```

internal 4APs, but turning this into a theorem for arbitrary `A_t subset V_t` requires pseudorandomness/mixing of the induced algebraic hypergraph and quantitative control of structured obstructions.

## Affine-subspace fallback is too expensive

High-rank quadratic level sets contain many large totally isotropic affine subspaces, but their codimension is typically proportional to `n` rather than `O(1)`.

Passing to such an affine subspace would therefore spend codimension on the order of

```math
n/2
```

in the nondegenerate case.

That is not compatible with the fine density-increment bookkeeping needed for the reciprocal-sum target.

Thus the high-rank branch cannot be handled by simply finding large affine subspaces inside `V_t` and applying the existing induction.

## Interpretation

The high-rank quadratic branch is not automatically good or bad.  It shifts the problem to a relative Szemeredi-type theorem on a high-rank quadratic-level AP hypergraph.

A successful high-rank argument would need to prove something like:

> If `q` has sufficiently high rank and `A subset V_t` has density `alpha+rho` relative to `V_t`, with the ambient set hyperplane-flat, then `A` contains a nontrivial 4AP unless `rho` is below a precisely controlled threshold.

This would be a direct recurrence/counting theorem, not a standard affine density-increment step.

## Updated bottleneck

The high-rank branch requires one of two new ingredients:

1. a relative counting lemma for the algebraic AP hypergraph inside high-rank quadratic level sets; or
2. a proof that the sign condition `Q<0` cannot concentrate on such high-rank level sets without creating an affine density increment elsewhere.

## Next research question

Can the internal 4AP hypergraph of a high-rank quadratic level set be shown to be sufficiently pseudorandom for sparse relative density `alpha` at the critical scale

```math
n ~ alpha^{-1+delta}?
```
