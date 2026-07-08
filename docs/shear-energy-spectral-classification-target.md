# Shear-energy spectral classification target

## Status

Proof-audit target.  This note records why marginal Fourier flatness is not enough to close the pair-incidence shear formulation, and isolates the next classification problem.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
a=1_A,
\qquad \alpha=E_G a.
```

Define

```math
P(x,d)=a(x)a(x+d),
\qquad
S(x,d)=(x+2d,d).
```

If `A` is 4AP-free, then

```math
\langle P,P\circ S\rangle=0
```

up to the negligible zero-difference contribution.

The random main term is `alpha^4`, so the nontrivial spectral contribution must cancel a quantity of size about `alpha^4`.

## Endpoint factorization

The Fourier transform of `P` factors as

```math
\widehat P(\xi,\eta)=\widehat a(\xi-\eta)\widehat a(\eta),
```

up to sign convention.

Thus the shear correlation is

```math
\langle P,P\circ S\rangle
=\sum_{\xi,\eta}
\widehat a(\xi-\eta)\widehat a(\eta)
\overline{\widehat a(3\xi-\eta)\widehat a(\eta-2\xi)}.
```

The all-zero term contributes `alpha^4`.  In a 4AP-free set, all other terms must contribute approximately `-alpha^4`.

## Marginal flatness only controls one shadow

The pair-density function is

```math
p_d=E_x P(x,d).
```

Pair-density variance is

```math
E_d |p_d-alpha^2|^2
=\sum_{\eta\ne0}|\widehat a(\eta)|^4.
```

Thus marginal flatness controls the one-dimensional shadow of the spectrum given by fourth moments of individual Fourier coefficients.

It does not control the phase-sensitive shear energy

```math
\sum_{\xi,\eta}
\widehat a(\xi-\eta)\widehat a(\eta)
\overline{\widehat a(3\xi-\eta)\widehat a(\eta-2\xi)}.
```

The latter may be large because of many small coefficients arranged coherently across the shear relation.

## The actual hard spectral object

Let

```math
c_\zeta=\widehat a(\zeta).
```

The nontrivial shear energy is a quartic sum over frequency quadruples

```math
(\xi-\eta,\ \eta,\ 3\xi-\eta,\ \eta-2\xi).
```

These four frequencies satisfy the 4AP Fourier constraints.  The problem is not only the magnitudes `|c_zeta|`; it is the phase alignment of products

```math
c_{\xi-\eta}c_\eta\overline{c_{3\xi-\eta}c_{\eta-2\xi}}.
```

Therefore a large negative nontrivial contribution means:

1. many frequency quadruples participate; and
2. their phases align strongly enough to cancel the `alpha^4` main term.

This is a spectral additive-combinatorial structure statement.

## Why a simple inequality is unlikely

Suppose all nonzero Fourier coefficients obey

```math
|\widehat a(\zeta)|\le M
```

with `M` near the hyperplane-flatness threshold.  Also suppose

```math
\sum_{\zeta\ne0}|\widehat a(\zeta)|^4
```

is small.  These two facts still do not preclude a large quartic shear sum, because the sum ranges over pairs `(xi,eta)` and can accumulate many small terms.

Thus the next step cannot simply be: marginal flatness implies positive 4AP count.  One must either classify the spectral support/phase alignment or recover a density increment from it.

## Candidate classification principle

A possible theorem to seek is:

> If the nontrivial shear contribution has magnitude at least `c alpha^4`, while
>
> ```math
> \|\widehat a\|_{\infty,\zeta\ne0}\le alpha^{2-epsilon}
> ```
>
> and
>
> ```math
> \sum_{\zeta\ne0}|\widehat a(\zeta)|^4\ll alpha^{5-2epsilon},
> ```
>
> then the Fourier mass of `a` has organized phase alignment on a quadratic factor, or else `a` has a structured density increment not visible to first-order Fourier analysis.

This would convert the shear formulation into the low-rank/high-rank quadratic split already being developed.

## Dyadic pigeonholing version

A more concrete first step is to dyadically decompose frequencies by magnitude.  If the shear contribution is at least `c alpha^4`, then there is a scale `lambda` and a set

```math
\Omega_\lambda=\{\zeta: |\widehat a(\zeta)|\sim \lambda\}
```

such that the restricted shear sum over quadruples in `Omega_lambda` is still large after logarithmic losses.

Then `Omega_lambda` must have many solutions to the shear/Fourier quadruple relation.  Ignoring phases, this suggests high additive energy in a spectral set.  Keeping phases, it suggests an approximate quadratic phase relation.

## Possible tools

This target is closer to additive-combinatorial energy classification than to a black-box inverse theorem.  Plausible tools include:

1. Balog--Szemeredi--Gowers type extraction on the spectral support;
2. phase-alignment refinement after energy extraction;
3. conversion of an additive spectral model into a physical-space density increment;
4. high-rank quadratic factor classification when no low-rank increment appears.

## Relation to previous branches

- If the spectral support has a large atom, we are back in the trilinear/Fourier increment branch.
- If the spectral support has low-rank organization, we are in the low-rank quadratic increment branch.
- If the spectral support has only high-rank quadratic organization, the proof must move to the high-rank relative-host recurrence branch.

Thus this note supplies a bridge from the physical-space pair-fiber formulation to the existing quadratic rank split.

## Next research question

Can a large nontrivial shear sum be converted, by dyadic spectral pigeonholing and additive-energy extraction, into either:

```math
\|\widehat a\|_\infty\ge alpha^{2-epsilon},
```

or a low-rank/high-rank quadratic factor carrying the obstruction?
