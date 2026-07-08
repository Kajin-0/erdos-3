# Fixed-w line-mode extraction

## Status

Proof-audit lemma.  This note proves the elementary fixed-`w` extraction behind the phase-sensitive flat-cloud branch, with explicit Fourier normalization.

It also records a correction: a fixed-shift autocorrelation detects **line-mode bias** of `H_{w,r}`.  A full nondegenerate quadratic chirp on a complete line has essentially flat one-dimensional Fourier mass and gives little or no fixed-shift autocorrelation.  Therefore quadratic structure must enter through compatibility across many `(w,r)`, support truncation, or degeneration such as isotropic directions.

## Normalization

Let `p>4` and let

```math
H:F_p\to C.
```

Use the normalized one-dimensional Fourier transform

```math
\widehat H(m)=E_{t\in F_p}H(t)e_p(-mt),
```

so that

```math
H(t)=\sum_{m\in F_p}\widehat H(m)e_p(mt)
```

and

```math
E_t|H(t)|^2=\sum_m|\widehat H(m)|^2.
```

Define the shift-2 autocorrelation

```math
C_2(H)=E_t H(t)\overline{H(t+2)}.
```

Then

```math
C_2(H)=\sum_m |\widehat H(m)|^2 e_p(-2m).
```

Taking real parts,

```math
\operatorname{Re} C_2(H)
=\sum_m |\widehat H(m)|^2\cos(4\pi m/p).
```

## Fixed-line extraction lemma

Let

```math
E(H)=E_t|H(t)|^2.
```

Suppose

```math
\operatorname{Re} C_2(H)\le -\gamma E(H)
```

for some `0<gamma<=1`.

Define the negative-mode set

```math
M_\gamma^-=\{m\in F_p:\cos(4\pi m/p)\le -\gamma/2\}.
```

Then

```math
\sum_{m\in M_\gamma^-}|\widehat H(m)|^2
\ge
\frac{\gamma/2}{1-\gamma/2}E(H)
\ge
\frac{\gamma}{2}E(H)
```

up to the harmless monotone constant convention.

Thus large negative fixed-shift autocorrelation forces a positive fraction of the `L^2` Fourier mass of `H` onto modes whose shift character has negative real part.

More generally, if

```math
|C_2(H)|\ge \gamma E(H),
```

then after rotating by a phase `omega` with `|omega|=1`, a positive fraction of the spectral mass lies on modes satisfying

```math
\operatorname{Re}(\omega e_p(-2m))\ge \gamma/2.
```

## Proof

The identity for `C_2(H)` follows from Fourier inversion:

```math
H(t)=\sum_m\widehat H(m)e_p(mt),
\qquad
\overline{H(t+2)}=\sum_n\overline{\widehat H(n)}e_p(-nt-2n).
```

Averaging over `t` keeps only `m=n`, giving

```math
C_2(H)=\sum_m|\widehat H(m)|^2e_p(-2m).
```

For the mass bound, write

```math
\mu(m)=|\widehat H(m)|^2/E(H).
```

Then `mu` is a probability measure if `E(H)>0`, and

```math
E_\mu\cos(4\pi m/p)\le -\gamma.
```

If `x=\mu(M_\gamma^-)`, then the average is bounded below by

```math
-x-(1-x)\gamma/2.
```

For this to be at most `-gamma`, one needs

```math
x\ge \frac{\gamma/2}{1-\gamma/2}.
```

This proves the claim.

## Application to shear fibers

For the shear form, define

```math
h_w(u)=c_uc_{w-u}.
```

Choose representatives `r` for `G/<w>` and set

```math
H_{w,r}(t)=h_w(r+tw).
```

Then

```math
\sum_u h_w(u)\overline{h_w(u+2w)}
=
\sum_{r\in G/<w>}\sum_{t\in F_p}H_{w,r}(t)\overline{H_{w,r}(t+2)}.
```

With normalized line averages this is

```math
p\sum_r C_2(H_{w,r}).
```

Therefore, if a fixed `w` contributes large negative real autocorrelation relative to its line energies, then many line functions `H_{w,r}` have nontrivial mass on negative shift modes.

A quantitative averaged statement is obtained by applying the previous lemma after pigeonholing lines by the ratio

```math
-\operatorname{Re}C_2(H_{w,r})/E(H_{w,r}).
```

## What this does and does not prove

This lemma proves only a fixed-line spectral extraction:

```math
\text{large fixed-shift autocorrelation}
\Rightarrow
\text{line-mode bias of }H_{w,r}.
```

It does **not** by itself prove a global quadratic-chirp model for the original coefficients `c_xi`.

The reason is important.  If

```math
c_\xi\approx A(\xi)e_p(q(\xi))
```

with `q` genuinely quadratic, then

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}
```

has phase

```math
q(r+tw)+q(w-r-tw)
=C(w,r)+2Q_q(w)t^2+B_q(w,2r-w)t.
```

If `Q_q(w)\ne0` and the line support is complete with nearly constant amplitude, this is a nondegenerate quadratic chirp in `t`.  Its one-dimensional Fourier mass is typically spread rather than concentrated at one mode, and its fixed shift-2 autocorrelation averages to zero.

Thus a large fixed-shift autocorrelation is more consistent with one of the following:

1. **degenerate directions**, where `Q_q(w)=0`, so the chirp becomes affine along the `w`-line;
2. **incomplete or structured support**, where cancellation of the chirp derivative is blocked;
3. **mode compatibility across many lines**, forcing a global quadratic/cocycle relation indirectly;
4. **low-rank concentration**, where many relevant `w` lie in a structured isotropic set.

## Compatibility problem

The next problem is not fixed-line extraction.  That part is elementary.

The real problem is compatibility: if for many `(w,r)` there is substantial Fourier mass near modes

```math
m=m(w,r),
```

what constraints are imposed by

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}?
```

A quadratic model predicts that the extracted affine mode should behave like

```math
m(w,r)\approx B_q(w,2r-w)
```

on directions where the quadratic `t^2` term is absent or suppressed, while nonzero quadratic terms should appear through systematic variation of autocorrelations across shifts or through support truncation.

## Updated extraction target

The phase-sensitive flat-cloud route should now be stated as:

```math
\text{large shear contribution}
\Rightarrow
\text{many biased line modes }m(w,r)
\Rightarrow
\text{compatibility of }m(w,r)
\Rightarrow
\text{low-rank/quadratic structure or increment}.
```

The first implication is elementary and now normalized.  The second implication is the genuine research obstacle.
