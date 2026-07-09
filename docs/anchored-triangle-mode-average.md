# Anchored triangle mode average

## Status

Analytic test object.  This note constructs the anchored triangle average needed in the phase-comparison step.

The purpose is to test whether three pair-line modes through shared spectral vertices close as

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

The conclusion is cautious: the projected triangle average detects mode closure exactly, but the unprojected average can be polluted by off-mode Fourier mass or support structure.  Therefore this is a diagnostic and a possible lemma target, not yet a proof of automatic triangle closure.

## Pair-line projections

For an oriented spectral pair `a -> b`, let

```math
w_{ab}=a+b
```

and define

```math
H_{a,b}(t)=c_{a+t w_{ab}}c_{b-t w_{ab}}.
```

Use the normalized one-dimensional Fourier transform

```math
\widehat H_{a,b}(m)=E_{t\in F_p}H_{a,b}(t)e_p(-mt).
```

The pure mode projection onto `mu` is

```math
P_\mu H_{a,b}(t)=\widehat H_{a,b}(\mu)e_p(\mu t).
```

If `mu(a,b)` is the extracted stable mode, define

```math
H_{a,b}^{\sharp}(t)=P_{\mu(a,b)}H_{a,b}(t).
```

## Anchored triangle average

Fix an anchor vertex `o`.  For an active edge `a b` with `a o` and `b o` also active, define the projected anchored triangle average

```math
\mathcal T_o^{\sharp}(a,b)
=
E_{s\in F_p}
H_{a,b}^{\sharp}(s)
H_{b,o}^{\sharp}(s)
H_{o,a}^{\sharp}(s).
```

Substituting the pure projections gives

```math
\mathcal T_o^{\sharp}(a,b)
=
\widehat H_{a,b}(\mu(a,b))
\widehat H_{b,o}(\mu(b,o))
\widehat H_{o,a}(\mu(o,a))
E_s e_p((\mu(a,b)+\mu(b,o)+\mu(o,a))s).
```

By orthogonality,

```math
\mathcal T_o^{\sharp}(a,b)=0
```

unless

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

If the mode sum is zero, then

```math
\mathcal T_o^{\sharp}(a,b)
=
\widehat H_{a,b}(\mu(a,b))
\widehat H_{b,o}(\mu(b,o))
\widehat H_{o,a}(\mu(o,a)).
```

Thus the projected anchored triangle average detects exactly the zero-sum mode closure required by the coboundary-cleaning lemma.

## Unprojected triangle average

The corresponding unprojected average is

```math
\mathcal T_o(a,b)
=
E_s H_{a,b}(s)H_{b,o}(s)H_{o,a}(s).
```

Fourier expansion gives

```math
\mathcal T_o(a,b)
=
\sum_{m_1+m_2+m_3=0}
\widehat H_{a,b}(m_1)
\widehat H_{b,o}(m_2)
\widehat H_{o,a}(m_3).
```

Therefore the unprojected average is large when the three line spectra have substantial additive convolution at zero.  If each line spectrum is sharply concentrated near its extracted mode, then a large unprojected average forces approximately

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

But if the spectra are broad, the unprojected average may be carried by off-mode triples.  In that case it does not certify closure of the selected modes.

## Triangle closure lemma target

A useful lemma would be:

> Suppose for many anchored triples `(a,b,o)`, each line function `H_{a,b}`, `H_{b,o}`, and `H_{o,a}` has a stable dominant mode, and the unprojected triangle average has magnitude comparable to the product of those dominant mode magnitudes.  Then for many triples,
>
> ```math
> \mu(a,b)+\mu(b,o)+\mu(o,a)=0.
> ```

This is a standard Fourier-support statement once dominance is quantified.  The nontrivial part is proving that the relevant anchored triangle averages are large from the original shear-energy hypothesis.

## Relation to mode incoherence

If many individual pair-lines have biased modes but the anchored triangle averages are small, then the modes do not cohere into a vertex potential.  This gives a real branch:

```math
\text{many line biases but small triangle averages}
\Rightarrow
\text{incoherent line modes}.
```

Such incoherence should either:

1. cause cancellation when trying to aggregate line modes into global structure;
2. force the route back to a non-isotropic chirp label rather than an affine edge label;
3. or reveal support concentration where the off-mode terms live.

Thus failure of the anchored triangle average is not a contradiction.  It is a diagnostic that the affine coboundary route is not yet available.

## How this fits the proof architecture

The pair-lift route now has the following precise analytic sequence:

```math
\text{large shear contribution}
\Rightarrow
\text{many fixed-line mode biases}
\Rightarrow
\text{large anchored triangle averages}
\Rightarrow
\text{many zero-sum triangles}
\Rightarrow
\text{coboundary cleaning}
\Rightarrow
\text{quadraticity test for }\Phi.
```

The first implication is elementary after fixed-line extraction.  The third implication is elementary after mode dominance.  The missing analytic input is the second implication:

```math
\text{many line biases}
\Rightarrow
\text{large anchored triangle averages}
```

or else a structured explanation for its failure.

## Immediate proof task

Try to derive lower bounds for averages of

```math
|\mathcal T_o(a,b)|
```

from the original shear-energy distribution.  If no such lower bound follows, then the affine pair-lift route cannot be forced from shear energy alone; one must either use a higher-order sifting argument or enrich the labels to include quadratic line coefficients.
