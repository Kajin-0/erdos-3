# Dilation triple failure mode

## Status

Proved obstruction to one attempted proof route.

## Claim

Divergent reciprocal sum, even with zero logarithmic density, does not by itself force exact triples

```math
d,2d,3d.
```

## Construction

Let `S` be a sparse infinite set of dyadic block indices with zero natural density, for example
`S={floor(m log m): m >= 2}`.  Let `A` consist of odd integers in the dyadic blocks
`[2^j,2^{j+1})` with `j in S`.

Each selected block contributes a fixed positive amount to `sum_{n in A} 1/n`, so the reciprocal
sum diverges.  Since `S` has zero natural density, the logarithmic density of `A` is zero.

But `A` has no exact triple `d,2d,3d`: if `d` is odd, then `2d` is even and is not in `A`; if `d`
is even, then `d` is not in `A`.

## Consequence

The long-range shadow route cannot rely on proving that divergent harmonic mass alone forces many
exact `(d,2d,3d)` tails.

A viable proof must couple dilation-tail analysis with local AP-rich/AP-poor structure, or use a
broader shifted-tail family rather than exact dilation triples alone.

## Caveat

This construction is not AP-free.  Selected blocks contain dense odd subsets and therefore contain
many arithmetic progressions.  The note rules out one isolated implication, not the full shadow
strategy.
