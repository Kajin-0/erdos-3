# Bounded-product scale barrier

## Status

Proof-audit scale lemma.  This note isolates why the `F_23` product enemy does not threaten the finite-field route to the reciprocal-sum problem.

## Fixed base tensor products

Let `A subset F_p^b` be a nonempty 4AP-free set with density

```math
rho = |A|/p^b,
qquad
0<rho<1.
```

For `n>=1`, form the tensor power

```math
B_n=A^n subset F_p^{bn}.
```

Then `B_n` is 4AP-free: a 4AP in `B_n` projects to a 4AP in each factor, so the common difference is zero in every coordinate block.

The density is

```math
alpha_n = rho^n.
```

The ambient dimension is

```math
N_n = bn.
```

Therefore

```math
N_n = (b/log(1/rho)) log(1/alpha_n).
```

Thus every fixed-base tensor construction has dimension logarithmic in inverse density:

```math
N_n ~ log(1/alpha_n).
```

## Bounded-block products

More generally, suppose `B` is fixed and a product construction is assembled from blocks

```math
A_j subset F_p^{b_j},
qquad
1 <= b_j <= B,
```

where each `A_j` is 4AP-free and nonempty.

Let

```math
rho_j = |A_j|/p^{b_j},
qquad
alpha = prod_j rho_j,
qquad
N = sum_j b_j.
```

Since there are only finitely many possible nonempty 4AP-free subsets in dimensions `1,...,B`, define

```math
rho_* = max rho_j < 1
```

where the maximum ranges over all proper 4AP-free block choices of dimension at most `B`.

Then

```math
alpha <= rho_*^{N/B},
```

so

```math
N <= (B/log(1/rho_*)) log(1/alpha).
```

Hence every bounded-block product construction also has only logarithmic dimension in inverse density.

## Comparison with the desired forcing scale

The finite-field route toward the reciprocal-sum problem asks for a theorem of the form:

```math
n >= C alpha^{-1+delta}
```

forcing a 4AP in every density-`alpha` subset of `F_p^n`.

But for any fixed `delta>0`,

```math
log(1/alpha) = o(alpha^{-1+delta})
```

as `alpha -> 0`.

Therefore bounded-block product examples, including the `F_23` pure four-balanced tensor enemy, live far below the target forcing scale.

## What the F23 example does and does not prove

The `F_23` example proves that direct tensor products can have

```math
Q_n<0,
qquad
T_{i,n}>0 \quad\text{for all }i.
```

So negative four-balanced obstruction does not automatically imply negative trilinear obstruction, even asymptotically.

But because it is a bounded-block tensor product, its dimension satisfies

```math
n ~ log(1/alpha_n),
```

not

```math
n ~ alpha_n^{-1+delta}.
```

Thus it does not contradict the finite-field target.

## Updated live route

The proof search should no longer try to prove a universal statement of the form:

```math
Q<0 => some T_i<0.
```

That statement is false for tensor powers of the `F_23` base example.

A viable replacement must be scale-sensitive:

```math
Q<0
```

plus ambient dimension near or above

```math
alpha^{-1+delta}
```

should force one of:

1. negative trilinear obstruction after localization;
2. a large density increment;
3. a direct contradiction to 4AP-freeness;
4. structural classification showing the obstruction is bounded-product/logarithmic-scale.

## Next research question

Can every pure four-balanced obstruction be decomposed into a bounded-product component plus an error, or can one build a genuinely high-dimensional pure four-balanced obstruction with

```math
n comparable to alpha^{-1+delta}?
```
