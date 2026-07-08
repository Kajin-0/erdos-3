# Relative U3 lower-bound calibration

## Status

Proof-audit calibration.  This note isolates the first missing implication needed to use Prendiville's relative `U^3` inverse theorem in the high-rank quadratic-level branch.

Prendiville supplies:

```math
\text{large relative }U^3
\Rightarrow
\text{relative quadratic correlation or low-rank escape}.
```

The missing input is:

```math
\text{internal 4AP-free inside a high-rank quadratic level set}
\Rightarrow
\text{large relative }U^3.
```

## Setup

Let

```math
V=\{x\in F_p^n:q(x)=t\}
```

be a high-rank quadratic level set, and let

```math
B\subset V,
\qquad
|B|/|V|=\beta.
```

Let

```math
b=1_B,
\qquad
v=1_V,
\qquad
f=b-\beta v.
```

The internal 4AP count is

```math
\Lambda_V(b)
=E_{x,d} b(x)b(x+d)b(x+2d)b(x+3d),
```

where the support condition automatically restricts all four points to `V`.

If `B` has no nontrivial internal 4AP, then, ignoring the negligible zero-difference contribution,

```math
\Lambda_V(b)=0.
```

## Expected main term

For a high-rank quadratic level set, the host internal 4AP count should satisfy

```math
\Lambda_V(v)\approx p^{-3}
```

in normalized ambient measure, because the conditions for an internal 4AP are roughly

```math
q(x)=t,
\qquad
Q(d)=0,
\qquad
B_q(x,d)+\ell(d)=0.
```

Thus a random subset of `V` of relative density `beta` should have count

```math
\Lambda_V(b)\approx \beta^4\Lambda_V(v).
```

If `B` is internally 4AP-free, the error terms in the expansion around `beta v` must cancel a main term of size

```math
\beta^4\Lambda_V(v).
```

## Relative generalized von Neumann requirement

To derive a relative `U^3` lower bound, one needs a counting lemma of the form

```math
|\Lambda_V(b)-\beta^4\Lambda_V(v)|
\le C_p \|f\|_{U^3(V,\mathrm{rel})}\Lambda_V(v)
```

or more generally the same estimate with the appropriate relative `U^3` norm and normalization.

If such a lemma holds, then internal 4AP-freeness gives

```math
\|f\|_{U^3(V,\mathrm{rel})}\gtrsim_p \beta^4.
```

So the natural first calibration is

```math
\delta(\beta)\sim \beta^4.
```

## Consequence for Prendiville

If Prendiville's inverse theorem gives correlation

```math
\delta^{C_p}|V|,
```

then the resulting correlation scale is approximately

```math
\beta^{4C_p}|V|.
```

A direct increment of comparable size has exponent

```math
4C_p.
```

To fit the existing minimality strategy, one would need

```math
4C_p<2,
```

that is

```math
C_p<1/2.
```

This is unlikely for a generic inverse theorem.  Therefore the naive relative generalized-von-Neumann route probably does not produce the desired `beta^{2-epsilon}` increment by itself.

## Interpretation

This does not make Prendiville irrelevant.  It means its role is unlikely to be:

```math
\beta^4\text{ relative }U^3
\Rightarrow
\beta^{<2}\text{ increment}
```

via a black-box inverse theorem.

The more plausible uses are:

1. **Non-iterative high-rank recurrence.**  Use the relative quadratic correlation plus high-rank host geometry to prove that an internally 4AP-free `B` must have

```math
\beta\le C_p n^{-1-\epsilon_h}.
```

2. **System-specific stronger norm forcing.**  Exploit pair-fiber/shear structure to prove a relative `U^3` lower bound stronger than `beta^4`, perhaps closer to `beta^{2-\epsilon}`.

3. **Structured escape.**  Use the low-rank alternative to land exactly in the logarithmic-rank escape branch, avoiding destructive localization.

## Updated bottleneck

The bottleneck is not just Prendiville's inverse theorem.  It is the first and last steps around it:

```math
\text{internal 4AP-free}
\Rightarrow
\text{relative }U^3\text{ mass stronger than naive }\beta^4?
```

and

```math
\text{relative quadratic correlation at scale }\beta^{4C_p}
\Rightarrow
\text{non-iterative recurrence or stronger increment?}
```

## Relation to pair-fiber/shear route

This calibration strengthens the case for the pair-fiber/shear-energy route.

The pure global obstruction already had the same weakness:

```math
Q\le -c\alpha^4
\Rightarrow
\|f\|_{U^3}\gtrsim \alpha^4,
```

which is too weak for a generic inverse theorem.

The pair-fiber and spectral-shear analyses try to avoid compressing the obstruction to a single `U^3` number.  They preserve directional/fiber information that may yield a stronger-than-`beta^4` structural conclusion.

## Immediate proof task

Prove or disprove the following strengthened relative counting statement:

> If `B subset V` is internally 4AP-free, `V` is a high-rank quadratic level set, and `B` has no low-rank/linear density increment, then the deviation from random is not merely detected at scale `beta^4`; it forces pair-fiber or shear-energy structure corresponding to an effective increment at scale `beta^{2-epsilon}`.

If this strengthened statement is false, the high-rank route probably needs a direct extremal/relative-independence theorem rather than an inverse-theorem iteration.
