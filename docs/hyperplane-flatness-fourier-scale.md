# Hyperplane flatness and Fourier scale

## Status

Proof-audit scale check.  This note translates minimal criticality into Fourier uniformity and records the remaining exponent gap.

## Setup

Let `A subset F_p^n` have density

```math
alpha = |A|/p^n,
```

and write

```math
h=1_A.
```

For a nonzero frequency `xi in F_p^n`, let

```math
H_t = {x : xi dot x = t},
qquad t in F_p,
```

and define the fiber densities

```math
alpha_t = |A cap H_t|/|H_t|.
```

Then

```math
(1/p) sum_t alpha_t = alpha,
```

and

```math
\widehat h(xi) = (1/p) sum_t alpha_t e(-t/p).
```

Since the zero-frequency contribution cancels for `xi != 0`, this is also

```math
\widehat h(xi) = (1/p) sum_t (alpha_t-alpha)e(-t/p).
```

## Hyperplane flatness implies small Fourier coefficients

Assume the hyperplane-flatness condition

```math
alpha_t <= alpha(1+eta)
```

for every nonzero `xi` and every `t in F_p`.

Let

```math
delta_t = alpha_t-alpha.
```

Then `sum_t delta_t=0` and `delta_t <= alpha eta`.  Hence

```math
(1/p) sum_t |delta_t|
= 2(1/p) sum_t (delta_t)_+
<= 2 alpha eta.
```

Therefore

```math
|\widehat h(xi)| <= 2 alpha eta
```

for every `xi != 0`.

Thus

```math
||\widehat h||_{l^infty(xi != 0)} <= 2 alpha eta.
```

Conversely, if `|\widehat h(xi)|=beta`, then some affine hyperplane fiber for `xi` has density at least

```math
alpha + beta/2.
```

So affine-hyperplane density increments and nonzero Fourier coefficients are equivalent up to constants depending only on this normalization.

## Minimal critical flatness scale

For a minimal near-threshold counterexample to the target

```math
n >= C alpha^{-theta},
qquad theta<1,
```

the previous minimality calculation gives

```math
eta ~ 1/(theta n).
```

Therefore

```math
||\widehat h||_{infty, nonzero}
lesssim alpha/n.
```

At the critical scale

```math
n ~ alpha^{-theta},
```

this becomes

```math
||\widehat h||_{infty, nonzero}
lesssim alpha^{1+theta}.
```

## Comparison with trilinear obstruction scale

A negative trilinear obstruction of size

```math
|T_i| >= c alpha^3
```

forces a nonzero Fourier coefficient of size roughly

```math
||\widehat h||_{infty, nonzero} >= c' alpha^2.
```

This is the same `U^2`/Fourier extraction used for 3-point patterns.

The minimality-derived Fourier bound is

```math
alpha^{1+theta}.
```

Since `theta<1`,

```math
alpha^{1+theta} >> alpha^2
```

as `alpha -> 0`.  Thus hyperplane-flatness at the minimal critical scale is not strong enough by itself to rule out trilinear obstruction.

Equivalently, if `theta=1-delta`, then minimality gives the scale

```math
alpha^{2-delta},
```

which misses the desired `alpha^2` Fourier scale by a factor of

```math
alpha^{-delta}.
```

## Interpretation

This is an important near-miss.

Minimality kills product-type examples by forcing hyperplane flatness, but the resulting Fourier-uniformity scale is still slightly too weak for the desired exponent `theta<1`.

Therefore a proof cannot rely only on affine-hyperplane flatness.  It must use at least one additional ingredient:

1. stronger flatness on codimension larger than one;
2. the negative quartic 4AP identity;
3. a density increment that gains more than hyperplane Fourier extraction;
4. a structural classification of pure four-balanced obstructions.

## Next research question

Can minimality be iterated to codimension `r` subspaces to upgrade the Fourier bound from

```math
alpha/n
```

to the trilinear-relevant scale

```math
alpha^2,
```

without spending codimension comparable to `alpha^{-theta}`?
