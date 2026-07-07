# Dyadic summability equivalence for fixed k >= 4

## Status

Proved structural reduction.

## Claim

For every fixed `k >= 4`, the reciprocal-sum Erdős problem for avoiding `k`-term arithmetic
progressions is equivalent to the dyadic summability condition

```math
\sum_{j\ge 1}\frac{r_k(2^j)}{2^j}<\infty,
```

where `r_k(N)` is the largest size of a `k`-AP-free subset of `[1,N]`.

The forward direction was already the standard dyadic-block reduction.  The reverse direction is the
important point: if the dyadic sum diverges, then one can build a global `k`-AP-free set with
divergent reciprocal sum.

## Standard sufficient direction

Let `A_j=A cap [2^j,2^{j+1})`.  If `A` is `k`-AP-free, then

```math
|A_j| \le r_k(2^j)
```

up to harmless translation/length constants, and therefore

```math
\sum_{n\in A_j}\frac1n \le \frac{|A_j|}{2^j}\lesssim \frac{r_k(2^j)}{2^j}.
```

Thus dyadic summability implies every `k`-AP-free set has convergent reciprocal sum.

## Reverse construction for k >= 4

Assume

```math
\sum_j \frac{r_k(2^j)}{2^j}=\infty.
```

Choose an integer `M=M(k)` large enough that

```math
2^M>k-1
```

and

```math
2^{-M+1}<\frac{k-3}{k-2}.
```

At least one residue class modulo `M` has divergent subseries

```math
\sum_{j\equiv r\pmod M}\frac{r_k(2^j)}{2^j}=\infty.
```

For each such `j`, place a translated extremal `k`-AP-free subset of length `2^j` inside the dyadic
block `[2^j,2^{j+1})`.  Let `A` be the union over `j congruent r mod M`.

Then

```math
\sum_{n\in A}\frac1n=\infty.
```

It remains to check that `A` is globally `k`-AP-free.

Suppose a `k`-AP

```math
x_0,x_1,\ldots,x_{k-1}
```

lies in `A`.  The final `k-1` terms satisfy

```math
\frac{x_{k-1}}{x_1}\le k-1.
```

Since occupied dyadic blocks are separated by a factor greater than `k-1`, the final `k-1` terms
must all lie in the same occupied dyadic block `[2^j,2^{j+1})`.

Then

```math
(k-2)d=x_{k-1}-x_1<2^j,
```

so

```math
x_0=x_1-d \ge 2^j-\frac{2^j}{k-2}=\frac{k-3}{k-2}2^j.
```

By the choice of `M`, the previous occupied dyadic block is below this range.  Hence `x_0` is either
in the same occupied block or in an empty block.  Since `x_0 in A`, it must be in the same occupied
block.  The whole `k`-AP is therefore internal to one block, contradicting the block's construction.

So `A` is globally `k`-AP-free and has divergent reciprocal sum.

## Consequence

For fixed `k >= 4`, cross-block constraints cannot improve the problem in full generality.  If the
blockwise dyadic extremal densities are not summable, the above construction isolates extremal blocks
on one residue class of dyadic scales and eliminates cross-block APs without losing divergence.

Thus, for `k >= 4`, solving the reciprocal-sum Erdős problem for fixed `k` is essentially equivalent
to proving dyadic summability of `r_k(2^j)/2^j`.

## Research implication

The previous cross-block-shadow program is useful for understanding constraints in natural or dense
multi-scale constructions, but it cannot be the missing universal ingredient for the full fixed-`k`
problem.  The central bottleneck returns to improving extremal bounds for `r_k(N)` enough to make the
dyadic series summable.
