# r4 replacement architecture spec

## Status

Open research specification.  This file records quantitative requirements for any mechanism intended to replace the current Green--Tao Theorem 3.1 localization/refinement architecture.

## Baseline from GT31

Inside the GT31 absolute-error framework, applying the recurrence theorem to a 4AP-free set of density `alpha` forces the choice

```math
eta ~ alpha^4.
```

If the zero-step thickness has form

```math
P(r=0) << exp(C eta^{-gamma})/p,
```

then the method yields

```math
r_4(N) << N(log N)^(-1/(4 gamma)).
```

The reciprocal-sum target requires

```math
gamma < 1/4.
```

The extracted GT31 parameter rows show a much larger effective exponent because the proof uses polynomially many refinements and exponential radius/thickness losses.

## Required replacement theorem

A successful replacement recurrence theorem should retain the two useful features of GT31:

```math
E f(a) = E_x f(x) + O(eta),
```

and

```math
Lambda_{a,r}(f) >= (E f(a))^4 - O(eta),
```

but replace the zero-step thickness with

```math
P(r=0) << exp(C eta^{-gamma})/p
```

for some

```math
gamma < 1/4.
```

This would imply the `k=4` reciprocal-sum case.

## Equivalent density-dependent target

Since `eta ~ alpha^4`, the same target can be stated directly in density language:

```math
P(r=0) << exp(C alpha^{-1+delta})/p
```

for some `delta>0`, while retaining recurrence error below a fixed fraction of `alpha^4`.

This gives

```math
p >> exp(C alpha^{-1+delta}),
```

or equivalently

```math
r_4(N) << N(log N)^(-1/(1-delta)),
```

which is summable on dyadic scales.

## What must be avoided

The replacement must avoid the GT31 loss pattern

```math
polynomially many refinement steps
+ exponential radius shrinkage per refinement
+ final Bohr-thickness conversion.
```

In a schematic iterative model, if there are

```math
T(eta) ~ eta^{-a}
```

refinement steps and each step costs thickness roughly

```math
exp(C eta^{-b}),
```

then the final cost has exponent at least about

```math
gamma >= a+b.
```

To reach the target one would need

```math
a+b < 1/4,
```

which is incompatible with the visible GT31 hierarchy.

## Candidate architecture classes

### 1. One-shot recurrence

Avoid iterative localization entirely.  Prove a global recurrence theorem with zero-step thickness below the `eta^{-1/4}` threshold.

### 2. Low-loss localization

Use a localization object whose thickness degrades polynomially or subexponentially under refinement, instead of via repeated Bohr-radius shrinkage.

### 3. Entropy/information-energy framework

Replace atom refinement by an information increment where complexity grows additively and the final sampling distribution retains much larger support.

### 4. Finite-vector-space model first

Attempt the analogous recurrence problem over vector spaces, where subspace codimension may replace Bohr radius.  This could isolate whether the obstruction is genuinely arithmetic or mainly caused by cyclic-group localization losses.

### 5. Direct counting/transference

Bypass recurrence sampling variables `a,r` and prove directly that density alpha in `[N]` forces a 4AP once `N >= exp(C alpha^{-1+delta})`.

## Failure criterion for proposed approaches

Any proposed replacement architecture that still has:

```math
T(eta) >= eta^{-c}
```

iterations and

```math
exp(C eta^{-c'})
```

thickness loss per iteration must explicitly show

```math
c+c' < 1/4.
```

Otherwise it cannot reach the reciprocal-sum threshold through the GT31-style cost chain.

## Next work item

Pick one architecture class and attempt a toy theorem with full parameter accounting.  The finite-vector-space model is the cleanest first sandbox because codimension can be tracked more transparently than Bohr radius.
