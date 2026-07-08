# Counterintuitive architecture probes

## Status

Research-program control note.  This note records several high-risk or nonstandard directions that may prevent the project from overfitting to the wrong abstraction.

The central warning is:

> Do not keep treating the missing step as merely a better generic `U^3` inverse theorem or a slightly larger Fourier coefficient.

The main proof target remains dyadic summability of `r_4(2^j)/2^j`.  These probes are useful only if they can produce a mechanism stronger than the current `alpha^2` logarithmic-barrier increment.

## Probe 1: physical-space almost-periodicity

The Roth `k=3` breakthroughs suggest that a logarithmic barrier may be broken by replacing destructive Fourier/localization iterations with physical-space smoothing and almost-periodicity.

For the current `k=4` branch, the question is whether the pure four-balanced obstruction

```math
Q=Lambda_4(f,f,f,f) <= -c alpha^4
```

can be reinterpreted as failure of almost-periodicity for a structured multilinear convolution, rather than as only a generic `U^3` inverse-theorem input.

A possible target is to identify a convolutional object `C_A` built from `1_A` such that:

1. if `C_A` has strong almost-periodicity, then 4APs are forced; but
2. if almost-periodicity fails, the failure produces many medium-scale local biases that can be aggregated into a stronger-than-`alpha^2` increment.

The key desired output is not one large Fourier coefficient.  It is a mechanism that converts many weak translation instabilities into an effective density increment larger than the logarithmic-barrier scale.

## Probe 2: finite-field first

The finite-field model should remain the primary sandbox:

```math
A subset F_p^n,
qquad |A|=alpha p^n,
qquad A \text{ 4AP-free}.
```

The target is to force a 4AP when

```math
n >= C alpha^{-1+delta}.
```

This removes Bohr-radius bookkeeping and replaces it with codimension bookkeeping.  If the obstruction still persists in `F_p^n`, then it is genuinely `4AP/U^3` structural.  If it disappears, then the integer obstruction is likely tied to cyclic localization losses.

## Probe 3: sifting / bootstrapping formulation

The `k=3` breakthrough literature suggests that the decisive move may be a sifting or bootstrapping architecture rather than a sharper inverse theorem.

For `k=4`, translate 4AP-freeness into restrictions on difference directions:

```math
A \cap (A-d) \cap (A-2d) \cap (A-3d)=emptyset
```

for every nonzero `d`.

Potential sifting questions:

1. Which difference directions are popular for two-term or three-term partial configurations?
2. Can bad difference directions be discarded while preserving enough mass or convolutional energy?
3. Can many medium-sized directional biases be combined into an increment of size `alpha^{2-epsilon}`?
4. Can the signed deficit

```math
alpha sum_i T_i + Q <= -c alpha^4
```

be interpreted as a failure of a difference-direction pseudorandomness condition?

This probe is valuable because the direct trilinear extraction gives only an `alpha^2` Fourier increment.

## Probe 4: relative high-rank host

The current high-rank branch studies quadratic level sets

```math
V_t={x:q(x)=t}
```

and internal 4APs inside `V_t`.

The host is not an affine space; it is a structured sparse algebraic host.  The right model may therefore be a relative Szemeredi / sparse hypergraph problem.

Target:

```math
B subset V_t,\qquad |B|/|V_t|=beta
```

should imply either

```math
beta <= C_p n^{-1-epsilon_h}
```

or a structured density increment of size at least

```math
c_p beta^{2-epsilon_F}
```

on a linear/low-rank factor of codimension `O_p(log(1/beta))`.

Any relative counting theorem here must explicitly identify the pseudorandomness norm of the internal AP hypergraph and the rank threshold needed to satisfy it.

## Probe 5: containers as diagnostics

Hypergraph containers probably do not directly prove the desired `r_4` estimate.  Their more useful role is diagnostic:

> Are near-extremal 4AP-free sets compressible into a small family of structured templates?

For the finite-field 4AP hypergraph, estimate codegrees

```math
Delta_1,
Delta_2,
Delta_3
```

and test whether container hypotheses say anything meaningful at densities near

```math
alpha ~ n^{-1-epsilon}.
```

A useful output would be a structural classification of near-extremizers, not merely a weaker counting bound.

## Probe 6: algebraic/tensor certificates

Slice-rank and polynomial-method ideas are not obviously suited to 4APs, but they suggest a high-risk alternative to density increment:

> Certify that a 4AP-free support pattern forces an impossible low-rank algebraic object.

In `F_p^n`, absence of 4APs means avoiding support on tuples

```math
(x, x+d, x+2d, x+3d).
```

The probe is to ask whether the associated tensor, possibly after conditioning on high-rank quadratic levels, admits a rank obstruction at the target density.

This should be treated as high-risk/high-upside, not as the default route.

## Probe 7: true-complexity and flag-property checks

Every derived counting problem must be checked separately.  Do not assume full `U^3` complexity just because ordinary 4APs require it.

For each derived configuration, record:

1. the exact linear forms;
2. Cauchy--Schwarz complexity;
3. true complexity;
4. whether any arithmetic regularity/counting lemma requires a flag property;
5. whether conditioning on algebraic constraints such as `q(x)=t` changes the validity of the counting step.

This is a proof-safety requirement.  A false high-rank counting lemma is one of the easiest ways to create an invalid proof.

## Prioritization

The immediate order is:

1. keep Green--Tao III exponent extraction as the baseline audit;
2. in parallel, start a finite-field physical-space/sifting probe for the signed deficit;
3. before proving any high-rank quadratic-level recurrence theorem, run the true-complexity/flag-property checklist;
4. use containers and tensor methods only as obstruction-classification probes unless they produce a concrete quantitative gain.

## Next research question

Can `Q <= -c alpha^4` be written as a failure of translation-stability for an explicit physical-space convolutional object, and can that failure produce an increment of size `alpha^{2-epsilon}` rather than the direct Fourier `alpha^2` increment?
