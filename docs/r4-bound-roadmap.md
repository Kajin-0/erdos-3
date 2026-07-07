# r_4(N) bound roadmap

## Status

Working roadmap after the dyadic-summability equivalence.

## Central target

For `k=4`, the reciprocal-sum Erdős problem is reduced to proving

```math
\sum_{j\ge 1}\frac{r_4(2^j)}{2^j}<\infty.
```

A simple sufficient condition is

```math
r_4(N) \ll \frac{N}{(\log N)^{1+\epsilon}}
```

for some `epsilon > 0`.

## Current published upper-bound type

Green--Tao, *New bounds for Szemerédi's theorem, III: A polylogarithmic bound for r_4(N)*,
prove a bound of the form

```math
r_4(N) \ll N(\log N)^{-c}
```

for some absolute `c>0`.

Along dyadic scales this gives

```math
\frac{r_4(2^j)}{2^j} \ll j^{-c}.
```

This proves dyadic summability only if the exponent satisfies `c>1`.  The known result gives a
positive exponent but does not, as stated, provide the required `c>1` threshold.

## Exact bottleneck

The fixed-`k=4` reciprocal-sum problem becomes the quantitative question:

```math
\text{Can the logarithmic exponent in } r_4(N)\ll N(\log N)^{-c}\text{ be pushed past }1?
```

or, more flexibly, can one prove any estimate whose dyadic specialization is summable?

## Proof components to inspect

The next mathematical work should decompose the Green--Tao mechanism into:

1. the inverse theorem / structure theorem input;
2. the density-increment size;
3. the scale loss per increment;
4. the number of iterations before density exceeds 1;
5. the resulting final logarithmic exponent.

The relevant obstruction is not construction search or cross-block shadows.  It is the quantitative
strength of the density-increment iteration for 4-term APs.

## Consequence for the repository

Computational searches remain useful for finite benchmark exploration, but the shortest route toward
the full problem is now a proof audit of the `r_4(N)` density-increment exponent.
