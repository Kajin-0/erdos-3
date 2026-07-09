# Line autocorrelation dichotomy

## Status

One-dimensional reduction.  This note formulates the line-level dichotomy needed before the non-isotropic chirp-label branch can be globalized.

The main point is that a large fixed-shift autocorrelation of a line function is exactly an ordinary Fourier bias of its spectral measure.  It does not by itself identify whether the line function is affine, quadratic-chirped, or supported on a structured subset.

## Basic identity

Let

```math
H:F_p\to C
```

and define

```math
C_2(H)=E_t H(t)\overline{H(t+2)}.
```

With normalized Fourier transform

```math
\widehat H(m)=E_tH(t)e_p(-mt),
```

one has

```math
C_2(H)=\sum_m |\widehat H(m)|^2e_p(-2m).
```

Thus large `C_2(H)` means the Fourier-energy measure

```math
\nu_H(m)=|\widehat H(m)|^2
```

has nontrivial bias against the character

```math
m\mapsto e_p(-2m).
```

It is a statement about the ordinary frequency distribution of `H`, not directly about quadratic structure.

## Demodulation by a quadratic chirp

Suppose we write

```math
H(t)=R(t)e_p(A t^2+M t).
```

Then

```math
H(t)\overline{H(t+2)}
=
R(t)\overline{R(t+2)}e_p(-4At-4A-2M).
```

Therefore

```math
C_2(H)=e_p(-4A-2M)E_t R(t)\overline{R(t+2)}e_p(-4At).
```

So a nonzero quadratic coefficient `A` can contribute to fixed-shift autocorrelation only through an ordinary Fourier coefficient of the amplitude autocorrelation

```math
R(t)\overline{R(t+2)}
```

at frequency `4A`.

If `R` is constant on the full line, this average vanishes for `A\ne0`.

## Consequence

Fixed-shift autocorrelation cannot by itself distinguish the following cases:

1. **Affine line mode.**  `H` has ordinary Fourier mass at one or more modes.
2. **Quadratic chirp with structured support.**  After demodulating by `e_p(A t^2+M t)`, the residual `R` has support/amplitude autocorrelation with frequency `4A`.
3. **Pure support artifact.**  The observed ordinary mode comes mostly from irregular support or amplitude, with no stable quadratic phase.

Thus a line-level dichotomy must include support/amplitude structure explicitly.

## Candidate line dichotomy

A useful line lemma would be:

> Let `H:F_p -> C` satisfy
>
> ```math
> |C_2(H)|\ge \gamma E_t|H(t)|^2.
> ```
>
> Then at least one of the following holds:
>
> 1. **Affine branch:** `H` has a large ordinary Fourier coefficient on a mode set selected by the fixed-shift phase.
> 2. **Chirp-support branch:** there exist `A,M` such that the demodulated function
>
> ```math
> R_{A,M}(t)=H(t)e_p(-At^2-Mt)
> ```
>
> has structured shift autocorrelation
>
> ```math
> |E_t R_{A,M}(t)\overline{R_{A,M}(t+2)}e_p(-4At)|
> ```
>
> of comparable size.
> 3. **No stable chirp branch:** no small family of chirp demodulations explains the autocorrelation; the line should be treated as an affine/support artifact rather than a quadratic phase signal.

The first branch is already guaranteed in the weak sense by the Fourier identity.  The point of the lemma is to decide when the observed affine bias can be interpreted as the derivative of a quadratic chirp rather than as arbitrary support oscillation.

## Stronger test using multiple shifts

A single shift cannot recover `A` stably.  For a chirp

```math
H(t)=R(t)e_p(A t^2+M t),
```

the shift-`h` autocorrelation is

```math
C_h(H)=E_tH(t)\overline{H(t+h)}
=e_p(-Ah^2-Mh)E_tR(t)\overline{R(t+h)}e_p(-2Ah t).
```

If `R` is regular enough, the derivative frequency varies linearly with `h`:

```math
\text{observed frequency at shift }h\approx 2Ah.
```

Thus a more robust non-isotropic chirp extraction should use several shifts `h`, not just `h=2`.

A line-level chirp test is therefore:

```math
m_h\approx 2Ah+M_h^{\mathrm{support}},
```

where the support term should be absent or controlled in the chirp branch.

## Relevance to shear

The original 4AP shear identity supplies only the shift `h=2` along each shear orbit.  Therefore it gives too little line-level data to distinguish a true quadratic chirp from support-induced affine bias.

To access multiple shifts, one would need either:

1. additional progression identities beyond the original 4AP shear map;
2. a sifting/iteration that creates effective shift variation inside the active support;
3. a physical-space pair-fiber argument that directly controls support irregularity;
4. an auxiliary higher-order Fourier statistic.

This is an important limitation of the current Fourier-only route.

## Updated interpretation of fixed-line extraction

The fixed-line extraction should be treated as producing a derivative label, not a chirp label:

```math
m_{\mathrm{obs}}(a,b)
\approx -4A(a+b)-2M(a,b)+\text{support contribution}.
```

Without controlling support contribution, one cannot solve for `(A,M)`.

Therefore the non-isotropic chirp-label branch cannot be launched from the fixed-shift shear identity alone unless we add a support-regularity or multi-shift input.

## Architectural consequence

The phase-sensitive route now has a sharper trichotomy:

```math
\text{fixed-line autocorrelation}
\Rightarrow
\begin{cases}
\text{affine observed mode branch},\\
\text{chirp derivative branch with support control},\\
\text{support artifact / sifting branch}.
\end{cases}
```

The non-isotropic global chirp reconstruction is conditional on first separating the second branch from the third.

## Immediate next proof task

The Fourier route alone appears underdetermined.  The next more promising step is to formulate a physical-space pair-fiber sifting lemma that can control support irregularity directly.

This aligns with the earlier conclusion that pair-fiber/sifting input is likely necessary before the shear-BSG/chirp machinery can produce exponent gain.
