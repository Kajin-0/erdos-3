# Product scale inheritance lemma

## Status

Proof-audit scale lemma.  This extends the bounded-product barrier to arbitrary product decompositions and shows that a critical-scale product obstruction must already contain a critical-scale factor.

## Uniform density gap for product factors

Fix a prime `p>4`.  Let `A subset F_p^b` be 4AP-free and nonempty.

Restrict `A` to any affine line in `F_p^b`.  The intersection with that line is a 4AP-free subset of `F_p`.  Therefore every line contains at most `r_4(p)` points of `A`.

Averaging over all parallel affine lines gives the uniform density bound

```math
|A|/p^b <= r_4(p)/p =: rho_0 < 1.
```

Thus every nontrivial 4AP-free factor has density at most `rho_0`, independent of its dimension.

## General product setup

Let

```math
A_j subset F_p^{b_j},
qquad j=1,...,k,
```

be nonempty 4AP-free factors with densities

```math
rho_j = |A_j|/p^{b_j}.
```

Form the product

```math
A = prod_{j=1}^k A_j subset F_p^N,
qquad
N=sum_j b_j,
```

with density

```math
alpha = prod_j rho_j.
```

The product `A` is 4AP-free, because any 4AP projects to a 4AP in every factor.

## Scale inheritance lemma

Fix `theta>0` and suppose that every factor satisfies a scale bound

```math
b_j <= C rho_j^{-theta}.
```

Then the whole product satisfies

```math
N <= C_{p,theta} C alpha^{-theta}.
```

### Proof

Set

```math
x_j = rho_j^{-theta}.
```

Since `rho_j <= rho_0 < 1`, we have

```math
x_j >= a := rho_0^{-theta} > 1.
```

Also

```math
prod_j x_j = alpha^{-theta}.
```

For each `j`, the product of the other `x_i` is at least `a^{k-1}`, hence

```math
x_j <= alpha^{-theta}/a^{k-1}.
```

Summing over `j`,

```math
sum_j x_j <= k a^{-(k-1)} alpha^{-theta}.
```

The quantity

```math
K_a := sup_{k>=1} k a^{-(k-1)}
```

is finite because `a>1`.  Therefore

```math
sum_j x_j <= K_a alpha^{-theta}.
```

Using `b_j <= C x_j`,

```math
N=sum_j b_j <= C sum_j x_j <= C K_a alpha^{-theta}.
```

This proves the claim.

## Contrapositive

If a product construction has dimension

```math
N > C K_a alpha^{-theta},
```

then at least one factor must violate

```math
b_j <= C rho_j^{-theta}.
```

Equivalently, a product cannot manufacture a dimension exponent worse than the worst exponent already present in one of its factors.

## Consequence for the reciprocal-sum finite-field target

The target scale is

```math
N ~ alpha^{-1+delta}.
```

Take

```math
theta = 1-delta.
```

If every product factor is already below this scale, then the product is below this scale as well, up to constants depending only on `p` and `delta`.

Therefore an unbounded product construction can threaten the finite-field target only if at least one of its factors is itself a high-dimensional obstruction at essentially the same exponent.

## Interpretation

This turns product constructions from a separate enemy into an inheritance problem.

Bounded products are harmless because they are logarithmic in `1/alpha`.  Unbounded products are dangerous only when one of the unbounded factors already contains the hard obstruction.

So the proof search can focus on irreducible or high-dimensional factors rather than direct products of small examples such as the `F_23` tensor enemy.

## Next research question

Can one define a useful notion of irreducible 4AP-free obstruction so that every high-dimensional pure four-balanced obstruction either factors into lower-dimensional pieces or yields a density increment/local trilinear obstruction?
