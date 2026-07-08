# Relative independence exponent calibration

## Status

Proof-audit calibration note.  This records the exact exponent needed from the high-rank quadratic-level AP hypergraph.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let `q:G -> F_p` be a high-rank quadratic polynomial.  For a level set

```math
V_t={x:q(x)=t},
```

let `H_q` be the internal 4AP hypergraph on `V_t`: vertices are points of `V_t`, and edges are nontrivial quadruples

```math
x,\quad x+d,\quad x+2d,\quad x+3d
```

lying in `V_t`.

Let

```math
\alpha(H_q)
```

denote the independence number of this hypergraph: the largest size of a subset `B subset V_t` containing no internal nontrivial 4AP.

## Independence bound implies recurrence threshold

Suppose one can prove a high-rank relative independence estimate of the form

```math
\alpha(H_q) <= C_p |V_t|/n^a
```

for some exponent `a>0`, uniformly over all sufficiently high-rank `q`.

Then any subset `B subset V_t` of relative density

```math
beta=|B|/|V_t|
```

contains an internal 4AP whenever

```math
beta > C_p/n^a.
```

Equivalently, recurrence is forced once

```math
n > (C_p/beta)^{1/a}.
```

Thus the relative recurrence exponent is

```math
theta_q = 1/a.
```

## Barrier threshold

To beat the logarithmic-barrier scale in the finite-field model, one needs

```math
theta_q < 1.
```

Since `theta_q=1/a`, this is equivalent to

```math
a>1.
```

Therefore the high-rank quadratic branch needs a relative independence estimate stronger than

```math
|V_t|/n.
```

The target is any estimate of the form

```math
\alpha(H_q) <= C_p |V_t|/n^{1+epsilon}
```

with `epsilon>0`.

## Relation to dyadic summability

If the finite-field model gave an exponent

```math
a=1+epsilon,
```

then dense subsets of high-rank quadratic levels would contain internal 4APs once

```math
n >= C beta^{-1/(1+epsilon)}.
```

This is the finite-field analogue of a summable logarithmic gain, because the exponent

```math
1/(1+epsilon)
```

is below `1`.

## Why a merely random-count heuristic is insufficient

The internal hypergraph has about

```math
p^{2n-3}
```

edges, and a random subset of relative density `beta` would contain about

```math
beta^4 p^{2n-3}
```

edges.

This suggests that very sparse random sets should already contain many internal 4APs.  But an independence theorem for arbitrary `B subset V_t` must rule out structured obstructions, not random behavior.

The needed result is therefore an extremal/quasirandom theorem, not merely an edge-count heuristic.

## Linear and low-rank escape routes

If `B` is large and internal-AP-free, the desired dichotomy is:

1. `B` has a linear or low-rank concentration, returning to the affine/low-rank density-increment branch; or
2. `B` is pseudorandom relative to the high-rank level set, in which case the internal AP counting lemma applies.

This means the high-rank recurrence theorem should probably be proved with a regularity/decomposition statement, not as a one-line spectral estimate.

## Updated target

The concrete high-rank target is:

> For fixed `p>4`, high-rank quadratic level sets have internal 4AP independence number
>
> ```math
> \alpha(H_q) <= C_p |V_t|/n^{1+epsilon}
> ```
>
> unless the independent set has a linear or low-rank density increment.

This is the exact exponent scale needed to make the high-rank branch relevant to the full proof program.

## Next research question

Can one prove even the weaker bound

```math
\alpha(H_q) <= C_p |V_t|/n
```

for high-rank quadratic levels?  If not, explicit examples near `|V_t|/n` would reveal the obstruction type that must be handled next.
