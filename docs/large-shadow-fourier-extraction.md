# Large shadow implies weak Fourier concentration

## Status

Proof-audit bound.  This note records what the endpoint or skew shadow excess forces spectrally.  The conclusion is negative for the current route: the forced Fourier coefficient can be much too small to drive a useful density-increment argument.

## Setup

Let `A subset F_p`, let

```math
h=1_A,
qquad
alpha=E h=m/p,
```

and define

```math
beta = max_{r != 0} |\widehat h(r)|.
```

By Parseval,

```math
sum_{r in F_p} |\widehat h(r)|^2 = E h^2 = alpha,
```

so

```math
sum_{r != 0} |\widehat h(r)|^2 <= alpha.
```

## Endpoint shadow excess

From the Fourier shadow formulation,

```math
E - m^3/p
= p^2 sum_{r != 0} \widehat h(r)^2 \widehat h(-2r).
```

Therefore

```math
|E-m^3/p|
<= p^2 beta sum_{r != 0} |\widehat h(r)|^2
<= p^2 beta alpha.
```

Thus, if `E > m^3/p`, then

```math
beta >= (E-m^3/p)/(alpha p^2).
```

## Skew shadow excess

Similarly,

```math
I - m^3/p
= p^2 sum_{r != 0} \widehat h(2r)\widehat h(-3r)\widehat h(r).
```

Using Cauchy-Schwarz and the fact that multiplication by nonzero constants permutes frequencies,

```math
|I-m^3/p|
<= p^2 beta
   (sum_{r != 0}|\widehat h(2r)|^2)^{1/2}
   (sum_{r != 0}|\widehat h(-3r)|^2)^{1/2}
<= p^2 beta alpha.
```

Thus, if `I > m^3/p`, then

```math
beta >= (I-m^3/p)/(alpha p^2).
```

## Consequence at the product-enemy threshold

Let

```math
M=max(E,I).
```

If `M > m^3/p`, then

```math
beta >= (M-m^3/p)/(alpha p^2).
```

In the small-density side of the tensor obstruction search, one has

```math
m^3/p <= p,
```

and the product-enemy condition only forces

```math
M>p.
```

This yields at best

```math
beta >= (p-m^3/p)/(alpha p^2)
     = (1-alpha^3 p)/(alpha p)
     = (1-alpha^3 p)/m.
```

When `m << p^{2/3}`, this is only of order

```math
1/m.
```

## Interpretation

A large shadow does force nontrivial Fourier concentration, but the lower bound available exactly at the tensor obstruction threshold is weak.

This means that the implication

```math
E,I >= m^3/p
quad and quad
max(E,I)>p
```

is unlikely to be resolved by a naive large-Fourier-coefficient argument alone.

The obstruction seems to require either:

1. a sharper inequality using the simultaneous positivity of both cubic sums;
2. an argument using the negative quartic 4AP identity;
3. a structural/run-count argument across many directions;
4. an explicit larger-prime counterexample to the two-shadow domination conjecture.

## Next research question

Can simultaneous endpoint and skew nonnegative cubic biases, together with the forced negative quartic identity, produce a stronger Fourier concentration bound than either shadow alone?
