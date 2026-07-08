# Pair-shift Fourier factorization

## Status

Proof-audit identity.  This note reformulates the uniform pair-fiber branch as a sheared-correlation problem on `G x G` and records the special Fourier factorization forced by the fact that all pair-fibers come from one set `A`.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
A\subset G,
\qquad
a=1_A,
\qquad
\alpha=E_G a.
```

Define the pair-incidence function on `G x G` by

```math
P(x,d)=a(x)a(x+d).
```

Thus the `d`-fiber of `P` is the pair-fiber

```math
B_d=A\cap(A-d).
```

Let the shear map be

```math
S(x,d)=(x+2d,d).
```

## 4AP-freeness as shear-disjointness

The condition that `A` is 4AP-free is exactly

```math
P(x,d)P(S(x,d))=0
```

for every `x` and every nonzero `d`.

Equivalently, ignoring the negligible zero direction in the finite-field asymptotic,

```math
\langle P,P\circ S\rangle_{G\times G}=0.
```

The trivial random expectation at density `alpha` would be about `alpha^4`, so this is the same missing-mass phenomenon as the 4AP count.

## Fourier factorization of P

With normalized Fourier transform on `G x G`, write frequencies as `(xi,eta)`.  Changing variables `y=x+d`, one gets

```math
\widehat P(\xi,\eta)
=\widehat a(\xi-\eta)\widehat a(\eta),
```

up to the harmless sign convention of the Fourier transform.

This is the key constraint distinguishing genuine pair-fiber families from arbitrary sparse subsets of `G x G`.

An arbitrary function `P` of density `alpha^2` can avoid its shear translate without forcing useful structure.  The genuine pair-incidence function has rank-one Fourier factorization in the two endpoints of an edge.

## Sheared spectral identity

The map `S` is linear with matrix

```math
(x,d)\mapsto(x+2d,d).
```

On frequencies, it acts by the inverse transpose.  Thus

```math
\widehat{P\circ S}(\xi,\eta)=\widehat P(\xi,\eta-2\xi)
```

up to sign convention.

Therefore

```math
\langle P,P\circ S\rangle
=\sum_{\xi,\eta}\widehat P(\xi,\eta)\overline{\widehat P(\xi,\eta-2\xi)}.
```

Using the factorization of `P`, this becomes

```math
0
=\sum_{\xi,\eta}
\widehat a(\xi-\eta)\widehat a(\eta)
\overline{\widehat a(3\xi-\eta)\widehat a(\eta-2\xi)}.
```

This is just the usual Fourier expression for the 4AP count, but written as a shear-correlation of a pair-incidence function.

## What pair-density flatness controls

The pair-density function is

```math
p_d=E_xP(x,d).
```

Its Fourier transform in `d` is

```math
\widehat p(\eta)=|\widehat a(\eta)|^2.
```

Thus the pair-density variance dichotomy controls only the vertical marginal spectrum

```math
\sum_{\eta\ne0}|\widehat a(\eta)|^4.
```

In the hard branch, this marginal spectrum is too small to expose the desired linear increment.

## What remains uncontrolled

The sheared correlation

```math
\sum_{\xi,\eta}\widehat P(\xi,\eta)\overline{\widehat P(\xi,\eta-2\xi)}
```

can still cancel the trivial `alpha^4` contribution through spectral mass not visible in the pair-density marginal.

Thus the hard branch can be described as:

1. marginal Fourier spectra are flat enough to avoid a linear increment;
2. nevertheless the sheared correlation of the pair-incidence function cancels the `alpha^4` random main term;
3. the only available structure is the endpoint factorization

```math
\widehat P(\xi,\eta)=\widehat a(\xi-\eta)\widehat a(\eta).
```

## Why this matters

This isolates the next obstruction more precisely than the generic `U^3` statement.

The problem is not merely that `a` has large quadratic uniformity.  It is that the endpoint-factorized pair-incidence function `P` has anomalously large negative correlation with a fixed shear, while its obvious marginals are flat.

A physical-space or sifting argument should try to exploit the endpoint factorization before collapsing the problem into a generic inverse theorem.

## Candidate next lemma

A possible lemma to seek is:

> Let `P(x,d)=a(x)a(x+d)` with `a=1_A`.  Suppose the vertical marginal `p_d=E_xP(x,d)` is `L^2`-flat and the start marginal `E_dP(x,d)=alpha a(x)` is hyperplane-flat through `a`.  If
>
> ```math
> \langle P,P\circ S\rangle=0,
> ```
>
> then either `a` has a Fourier coefficient of size `alpha^{2-epsilon}` or the sheared spectral cancellation is concentrated on a quadratic phase/factor.

This would connect the physical-space pair-fiber branch to the existing low-rank/high-rank quadratic split.

## Next research question

Can the sheared correlation identity be bounded below using only endpoint factorization plus marginal flatness?  If not, can one classify the extremizers that make the sheared correlation cancel the `alpha^4` main term while keeping all linear marginals flat?
