# Two-shadow reduction for one-dimensional tensor bases

## Status

Proof-audit simplification.  This note reduces the four missing-slot shadow counts for one-dimensional tensor bases to two parameters.

## Setup

Let `A subset F_p`, and let

```math
h = 1_A,
qquad
m = |A|,
qquad
alpha = m/p.
```

For `i in {0,1,2,3}`, define

```math
N_i
= # { (x,d) in F_p^2 : x+jd in A \text{ for every } j != i }.
```

These are the four missing-slot three-shadows of the 4AP hypergraph.

## Endpoint shadows

The endpoint shadows are equal:

```math
N_0 = N_3.
```

Indeed, missing the first slot gives the count of triples

```math
x+d, x+2d, x+3d in A,
```

which after shifting is the ordinary 3AP count

```math
E := # { (y,d) : y,y+d,y+2d in A }.
```

Missing the last slot gives the same count directly.  Thus

```math
N_0=N_3=E.
```

## Interior shadows

The interior shadows are equal:

```math
N_1 = N_2.
```

This follows by reversing the 4AP direction.  Missing the second position corresponds to the pattern

```math
x, x+2d, x+3d in A,
```

while missing the third corresponds to

```math
x, x+d, x+3d in A.
```

The change of variables

```math
(x,d) -> (x+3d,-d)
```

interchanges these two patterns.

Write their common value as

```math
I := N_1=N_2.
```

This is a skew three-point pattern count, not generally an ordinary 3AP count.

## Normalized ratios

For a 4AP-free base set, the full 4AP count is only the trivial contribution:

```math
lambda_4 = m/p^2.
```

Thus

```math
a = lambda_4/alpha^4 = p^2/m^3.
```

The two shadow ratios are

```math
r_E = pE/m^3,
qquad
r_I = pI/m^3.
```

The tensor-power four-balanced term satisfies

```math
Q_n/alpha^{4n}
= a^n - 2 r_E^n - 2 r_I^n + 3.
```

The trilinear terms satisfy

```math
T_{0,n}=T_{3,n}=alpha^{3n}(r_E^n-1),
```

and

```math
T_{1,n}=T_{2,n}=alpha^{3n}(r_I^n-1).
```

## Pure tensor enemy criterion in two parameters

A one-dimensional tensor base would produce an asymptotic pure four-balanced enemy exactly if

```math
r_E >= 1,
qquad
r_I >= 1,
```

and

```math
max(r_E,r_I) > max(a,1).
```

Equivalently, in raw counts,

```math
E >= m^3/p,
qquad
I >= m^3/p,
```

and

```math
max(E,I) > max(p,m^3/p).
```

## Candidate two-shadow domination conjecture

A sharpened product-obstruction conjecture is:

> If `A subset F_p` is 4AP-free and both `E` and `I` are at least their random scale `m^3/p`, then both are at most `p`.

In symbols:

```math
E >= m^3/p,
qquad
I >= m^3/p
```

should imply

```math
E <= p,
qquad
I <= p.
```

This is not proved here.

## Why this matters

The one-dimensional product obstruction search has now been reduced from four shadow counts to two:

1. the ordinary 3AP count `E` inside `A`;
2. the skew triple count `I` inside `A`.

If the two-shadow domination conjecture holds, then direct tensor powers cannot produce the asymptotic pure four-balanced enemy.

## Next research question

Can one prove the two-shadow domination conjecture, or find a 4AP-free set in some `F_p` with

```math
E,I >= m^3/p
```

and

```math
max(E,I)>p?
```
