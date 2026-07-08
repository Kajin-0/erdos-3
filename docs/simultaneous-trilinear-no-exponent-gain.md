# Simultaneous trilinear signs do not give an exponent gain

## Status

Proof-audit negative result.  This note checks whether the combined signed identity can improve the trilinear branch merely by having several trilinear terms available at once.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let

```math
A subset G,
qquad
alpha=|A|/|G|,
qquad
f=1_A-alpha.
```

For a 4AP-free set with `|G| >= 2 alpha^{-3}`, the signed expansion gives

```math
alpha \sum_{i=0}^3 T_i + Q <= -c alpha^4,
```

where `T_i` are the four trilinear balanced terms and

```math
Q=Lambda_4(f,f,f,f).
```

## If Q is not responsible

Suppose the four-balanced term is not already responsible for the deficit, for instance

```math
Q > -c_0 alpha^4.
```

Then

```math
alpha \sum_i T_i <= -c_1 alpha^4,
```

so

```math
\sum_i T_i <= -c_1 alpha^3.
```

Since there are only four trilinear terms, at least one satisfies

```math
T_i <= -c_2 alpha^3.
```

This recovers the usual trilinear branch but only up to constants.

## Multiple trilinear terms do not improve the exponent

For each `i`, Fourier expansion and Parseval give

```math
|T_i| <= alpha ||\widehat f||_{infty, nonzero}
```

up to constants depending only on `p`.

Consequently, even if several trilinear terms are negative at scale `alpha^3`, the conclusion remains only

```math
||\widehat f||_{infty, nonzero} >= c alpha^2.
```

At most, simultaneous negativity gives a constant-factor improvement in the lower bound.  It cannot change the exponent from `alpha^2` to `alpha^{2-epsilon}` because the number of terms is fixed.

## Energy-increment viewpoint

One might hope that several negative trilinear terms force several independent large Fourier coefficients.  But there are only four trilinear forms, and the Fourier supports may overlap.  Even in the best case, a bounded number of coefficients of size about `alpha^2` gives Fourier energy only on the scale

```math
O(alpha^4),
```

which is far below the ambient variance scale

```math
E f^2 = alpha(1-alpha) ~ alpha.
```

Thus a bounded family of trilinear signs cannot by itself create a strong energy increment.

## Consequence

The combined signed identity

```math
alpha \sum_i T_i + Q <= -c alpha^4
```

only gives the existing dichotomy:

1. some `T_i <= -c alpha^3`, producing a borderline `alpha^2` Fourier increment; or
2. `Q <= -c alpha^4`, producing the pure `U^3` branch.

There is no third exponent-improving conclusion from the finite sum of trilinear terms alone.

## What would be needed

To beat the logarithmic barrier, one must exploit structure not captured by this finite trilinear averaging step, such as:

1. an interaction inequality coupling the signs of the `T_i` with `Q`;
2. a one-sided recurrence theorem for `Q<0`;
3. a high-rank quadratic counting lemma;
4. an entropy or regularity mechanism that turns many small local biases into one stronger increment;
5. a non-iterative contradiction.

## Updated next research question

Can the pure four-balanced sign

```math
Q <= -c alpha^4
```

be upgraded into a one-sided structural statement stronger than the generic `U^3` inverse theorem?
