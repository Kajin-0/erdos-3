# Shadow disjointness inequality

## Status

Proof-audit inequality.  This note derives the first universal constraint on the two shadow counts `E` and `I` for a one-dimensional 4AP-free base set.

## Setup

Let `A subset F_p` be 4AP-free.  Write

```math
m=|A|.
```

For each `(x,d) in F_p^2`, define the four membership bits

```math
b_j = 1_A(x+jd),
qquad j=0,1,2,3.
```

The four missing-slot shadow events are

```math
S_i(x,d)=1
```

when all `b_j=1` for `j != i`.

Summing over `(x,d)`, the endpoint shadows have total count `E` twice and the interior shadows have total count `I` twice:

```math
sum_i sum_{x,d} S_i(x,d) = 2E+2I.
```

## Pointwise disjointness for nonzero difference

If `d != 0`, then 4AP-freeness says the four bits cannot all equal `1`.

For a fixed `(x,d)` with `d != 0`, at most one of the four events `S_i(x,d)` can occur.  Indeed, if two distinct missing-slot events occur, then all four positions are occupied, giving a nontrivial 4AP in `A`.

Therefore

```math
sum_i S_i(x,d) <= 1
```

for every `d != 0`.

There are `p(p-1)` pairs `(x,d)` with `d != 0`, so the total nontrivial contribution is at most

```math
p(p-1).
```

## Trivial-difference contribution

For `d=0`, all four positions are equal.  If `x in A`, then all four missing-slot events occur.  If `x notin A`, none occur.

Thus the `d=0` contribution to the total shadow sum is exactly

```math
4m.
```

## Universal inequality

Combining the nonzero and zero difference contributions gives

```math
2E+2I <= p(p-1)+4m.
```

Equivalently,

```math
E+I <= (p(p-1)+4m)/2.
```

## Consequence under random-scale lower bounds

The pure tensor enemy criterion requires

```math
E >= m^3/p,
qquad
I >= m^3/p.
```

Substituting into the disjointness inequality gives

```math
4m^3/p <= p(p-1)+4m.
```

Equivalently,

```math
m^3 <= (p^3-p^2+4mp)/4.
```

In density form, with `alpha=m/p`, this says roughly

```math
alpha^3 <= 1/4 + O(1/p).
```

Hence a pure tensor enemy cannot have density much larger than

```math
4^{-1/3} = 0.629960...
```

## Interpretation

This inequality is useful but not decisive.  It only rules out high-density product enemies.  The main reciprocal-sum-relevant regime is small density, where this inequality gives no serious obstruction.

Still, the pointwise disjointness is a structural fact that any stronger proof of the two-shadow domination conjecture should exploit.

## Next research question

Can pointwise disjointness of the four missing-slot shadow events be combined with additive structure of the endpoint shadow `E` and skew shadow `I` to prove the stronger domination claim

```math
E,I >= m^3/p
quad => quad
E,I <= p?
```
