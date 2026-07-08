# Minimal critical dichotomy: borderline trilinear or genuine U3

## Status

Proof-audit reduction.  This note combines the sign-sensitive 4AP deficit with minimal critical hyperplane flatness.  It identifies the remaining obstruction after product examples are removed by minimality.

## Setup

Work in

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

Assume `A` is 4AP-free and `|G| >= 2 alpha^{-3}`.  Then the normalized 4AP count satisfies

```math
Lambda_4(1_A) <= alpha^4/2.
```

Therefore

```math
Lambda_4(1_A)-alpha^4 <= -alpha^4/2.
```

Expanding `1_A=alpha+f`, all one-`f` and two-`f` terms vanish.  Thus

```math
alpha sum_i T_i + Q <= -alpha^4/2,
```

where the `T_i` are the four trilinear balanced terms and

```math
Q=Lambda_4(f,f,f,f).
```

Hence the sign-sensitive alternative is:

```math
T_i <= -c alpha^3
```

for some `i`, or

```math
Q <= -c alpha^4.
```

## Minimal hyperplane-flat scale

For a minimal counterexample near the target scale

```math
n ~= C alpha^{-theta},
qquad theta=1-delta<1,
```

the hyperplane-flatness reduction gives

```math
||\widehat{1_A}||_{infty, nonzero}
lesssim alpha/n
~ alpha^{1+theta}
= alpha^{2-delta}.
```

This eliminates large product-type fiber increments, but it is not Fourier-uniform at the `alpha^2` scale.

## Branch 1: negative trilinear obstruction

A trilinear term has the form

```math
E_{x,d} f(L_1(x,d))f(L_2(x,d))f(L_3(x,d))
```

for three distinct 4AP forms.  Fourier expansion and Parseval give

```math
|T_i| <= alpha ||\widehat f||_{infty, nonzero}.
```

Therefore

```math
T_i <= -c alpha^3
```

forces

```math
||\widehat f||_{infty, nonzero} >= c' alpha^2.
```

Equivalently, it gives an affine hyperplane density increment of size about

```math
alpha^2.
```

At the target `theta=1-delta`, minimality only forbids increments larger than about

```math
alpha/n ~ alpha^{2-delta}.
```

Since

```math
alpha^2 << alpha^{2-delta}
```

for small `alpha`, this trilinear density increment is too small to contradict minimality when `delta>0`.

At the endpoint `theta=1`, these two scales match.  This is the logarithmic-barrier signature.

## Branch 2: pure four-balanced obstruction

If no negative trilinear branch occurs, then

```math
Q=Lambda_4(f,f,f,f) <= -c alpha^4.
```

By the generalized von Neumann inequality for 4APs,

```math
|Q| <= ||f||_{U^3}.
```

Therefore

```math
||f||_{U^3} >= c alpha^4.
```

Together with hyperplane flatness, the obstruction is not explained by a large linear/Fourier bias beyond the minimal critical scale.  It is a genuinely higher-order, quadratic-type obstruction.

## Resulting dichotomy

After passing to a minimal critical counterexample, the forced 4AP deficit leaves exactly two live cases:

1. **Borderline trilinear case.**  There is a hyperplane density increment of size about `alpha^2`, which is useful but still below the `alpha^{2-delta}` scale needed to contradict minimality.
2. **Genuine U3 case.**  There is a negative four-balanced term of size `alpha^4`, hence `||f||_{U^3} >= c alpha^4`, with no accompanying negative trilinear obstruction.

The `F_23` tensor example lives in the second branch before minimization, but is removed by obvious constant-size fiber increments.  A critical enemy would have to be a hyperplane-flat version of the second branch.

## Interpretation

This clarifies the remaining gap.  The proof cannot be completed by:

1. ruling out all pure four-balanced obstruction, because the `F_23` tensor family disproves that;
2. using raw minimality, because it only reaches `alpha^{2-delta}` Fourier scale;
3. using the trilinear branch alone, because it supplies only `alpha^2` increments.

A successful argument must gain the missing factor

```math
alpha^{-delta}
```

from either the trilinear branch, the pure `U^3` branch, or a mechanism converting pure `U^3` obstruction into a stronger structured increment.

## Next research question

Can the pure four-balanced branch

```math
Q <= -c alpha^4
```

under hyperplane flatness force a quadratic-structured density increment with strength exceeding the borderline `alpha^2` increment?
