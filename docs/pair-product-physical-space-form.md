# Pair-product physical-space form of the pure U3 obstruction

## Status

Proof-audit identity and new probe.  This note rewrites the pure four-balanced obstruction in physical space.  The goal is to test whether `Q<0` can be treated as translation-instability of pair products, rather than only as a generic `U^3` inverse-theorem input.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
A \subset G,
\qquad
\alpha=|A|/|G|,
\qquad
f=1_A-\alpha.
```

The pure four-balanced term is

```math
Q=\Lambda_4(f,f,f,f)
 = E_{x,d} f(x)f(x+d)f(x+2d)f(x+3d).
```

The pure branch begins when

```math
Q \le -c\alpha^4.
```

## Pair-product identity

For each direction `d`, define the adjacent-pair product

```math
g_d(x)=f(x)f(x+d).
```

Then

```math
Q=E_d E_x g_d(x)g_d(x+2d).
```

Equivalently,

```math
Q=E_d \langle g_d,\tau_{2d}g_d\rangle,
```

where

```math
(\tau_h g)(x)=g(x+h).
```

Thus `Q<0` says that, on average over directions `d`, the adjacent-pair product `g_d` is anti-correlated with its `2d` translate.

## Centered pair-product form

Let

```math
\mu_d=E_x g_d(x)=E_x f(x)f(x+d).
```

Then

```math
\langle g_d,\tau_{2d}g_d\rangle
=\mu_d^2+\langle g_d-\mu_d,\tau_{2d}(g_d-\mu_d)\rangle.
```

Since `mu_d^2>=0`, the pure obstruction implies

```math
E_d \langle g_d-\mu_d,\tau_{2d}(g_d-\mu_d)\rangle
\le -c\alpha^4.
```

So the obstruction is genuinely a centered translation-instability statement for pair products.

## Difference-direction interpretation

For the original indicator, 4AP-freeness says that for every nonzero `d`,

```math
1_A(x)1_A(x+d)1_A(x+2d)1_A(x+3d)=0
```

for all `x`, or equivalently

```math
A\cap(A-d)\cap(A-2d)\cap(A-3d)=\emptyset.
```

The balanced identity above says that after subtracting density, this absence appears as systematic anti-correlation between adjacent-pair profiles at separation `2d`.

## Fourier comparison

For a fixed `d`, Fourier expansion gives

```math
\langle g_d,\tau_{2d}g_d\rangle
=\sum_\xi |\widehat{g_d}(\xi)|^2 e_p(2d\cdot\xi)
```

up to the sign convention of the Fourier transform.

A negative value does not force one large Fourier coefficient of `f`.  It may instead reflect many medium spectral components of the pair product `g_d` sitting on phases with negative real part.

This is the physical-space opening: the obstruction may be spread across many directions and many medium coefficients, so a one-coefficient extraction can lose the exponent gain.

## Almost-periodicity probe

A physical-space route would try to prove a dichotomy:

1. if many pair products `g_d` are sufficiently stable under the shifts `2d`, then `Q` cannot be negative enough and 4APs are forced; or
2. the failure of stability across many `d` produces a density increment larger than the direct Fourier `alpha^2` scale.

The desired increment threshold is

```math
\alpha^{2-\epsilon}
```

for some `epsilon>0`.

## Sifting probe

The same identity suggests a difference-direction sifting problem.

Define a direction `d` to be pair-unstable if

```math
\langle g_d-\mu_d,\tau_{2d}(g_d-\mu_d)\rangle
\le -\kappa\alpha^4.
```

Since the average over `d` is negative in the pure branch, there must be a nontrivial weighted family of such unstable directions.

The next question is whether this family can be used to construct a structured increment.  Possible mechanisms:

1. many unstable directions share a common linear or quadratic bias;
2. the unstable directions have additive structure and can be sifted;
3. translation instability of `g_d` gives a physical-space almost-periodicity failure that yields a large set of useful translates;
4. the direction family interacts with hyperplane-flatness to force a contradiction.

## Why this may beat the direct U3 route

The generic `U^3` route compresses the entire obstruction into one quadratic-correlation conclusion.  That loses the information that `Q` is an average of directional pair-product anti-correlations.

The physical-space route keeps the direction parameter `d` alive.  If many weak directional instabilities can be aggregated before passing to Fourier/quadratic structure, the resulting increment may exceed the direct `alpha^2` barrier.

## Immediate next research question

Can one prove a deterministic lemma of the form:

> If `E_d <g_d-mu_d, tau_{2d}(g_d-mu_d)> <= -c alpha^4` and `A` is hyperplane-flat, then either `A` has an affine density increment of size `alpha^{2-epsilon}`, or the unstable direction set has high-rank quadratic structure suitable for the relative-host branch?

This is the first concrete physical-space/sifting target.
