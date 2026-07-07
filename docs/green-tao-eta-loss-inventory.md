# Green--Tao eta-loss inventory

## Status

Working proof-audit note.  This records where the hidden `eta^{-O(1)}` cost in Green--Tao Theorem 3.1 should be traced.  It does not claim an improvement.

## Correction: thickness sign

The useful thickness form is

```math
P(r=0) << exp(eta^{-O(1)})/p,
```

not a negative exponential.  This is the form needed to recover a polylogarithmic bound.  The gamma diagnostic is unchanged.

## Source facts from the paper

Green--Tao Part III proves Theorem 3.1, which supplies random variables `a,r` satisfying:

```math
E f(a)=E_x f(x)+O(eta),
```

```math
Lambda_{a,r}(f)>= (E f(a))^4-O(eta),
```

and

```math
P(r=0)<< exp(eta^{-O(1)})/p.
```

The paper says the thickness condition is crucial to the quantitative bound, and that the proof uses non-independent random variables, factor-like decomposition, and regular probability distributions to smooth Bohr-set boundary issues.

## Immediate cost chain

For a 4AP-free set `A` of density `alpha`, applying Theorem 3.1 to `f=1_A` gives the schematic inequality

```math
alpha^4 <= O(eta) + P(r=0).
```

Taking `eta ~ alpha^4` reduces the problem to the thickness estimate.  If the hidden estimate is made explicit as

```math
P(r=0)<< exp(C eta^{-gamma})/p,
```

then the argument yields

```math
p >> exp(C alpha^{-4 gamma})
```

and hence

```math
r_4(N)<< N(log N)^{-1/(4 gamma)}.
```

The reciprocal-sum threshold requires `gamma < 1/4`.

## Candidate eta-loss sources

### 1. Repeated Cauchy--Schwarz

The paper explicitly uses probabilistic Cauchy--Schwarz as a device that eliminates one factor at the cost of duplicating another factor and worsening a lower bound from `eta` to `eta^2`.

Every repeated Cauchy--Schwarz step can square the effective parameter.  A chain of such steps can quickly turn a desired `eta`-scale statement into a much worse polynomial dependence.

### 2. Popularity losses

The popularity principle converts an average lower bound into a positive-probability pointwise event.  This typically costs a factor polynomial in `eta`.

### 3. Factor refinement / atom decomposition

The paper compares the framework to factor decompositions into smaller atoms such as Bohr sets.  Each refinement can increase complexity and reduce local thickness.

### 4. Regular probability distributions

The paper introduces regular probability distributions to avoid Bohr-set boundary irregularity.  This may smooth the argument but still contributes to parameter loss through dimension/radius bookkeeping.

### 5. Zero-step thickness

The final bottleneck is the quantitative upper bound for `r=0`.  The reciprocal-sum route needs this thickness cost to behave effectively better than

```math
exp(C eta^{-1/4})/p.
```

## Audit target

Extract from the proof of Theorem 3.1 a chain of the form

```math
eta -> eta^{a_1} -> eta^{a_2} -> ... -> exp(eta^{-gamma})/p.
```

The key question is whether the final exponent `gamma` is structurally forced to be `>=1/4`, or whether one of the loss-producing steps is quantitatively wasteful.

## Practical next step

Make a line-by-line table of Theorem 3.1's proof with columns:

1. lemma/proposition used;
2. input parameter;
3. output parameter;
4. type of loss: squaring, polynomial, exponential, dimension, radius, regularization;
5. contribution to final `gamma`.

Only after this table exists should the repository attempt a proposed improvement.
