# Finite-state obstruction paper audit

## Status

Research-program audit.  This note evaluates an external proposal to pivot part of the Erdős reciprocal-sum AP project toward finite-state and digit-restricted model classes.

## Verdict

The proposal is directionally strong as a publishable side project, but it should not be presented as major progress toward the full fixed-`k >= 4` Erdős reciprocal-sum problem.

The best extraction is:

> finite-state / regular-language / automatic constructions cannot produce divergent reciprocal-sum AP-free counterexamples, and the existing repository machinery can make that obstruction theorem computationally checkable and benchmarked.

This is a credible paper direction if packaged with exact algorithms, certificates, and Walker benchmark data.

## Main correction: cross-block forcing is not universal

The proposal leans on the older ledger view that the remaining bottleneck is cross-block arithmetic forcing.  That is now superseded for fixed `k >= 4` by the dyadic summability equivalence.

For fixed `k >= 4`, the full reciprocal-sum problem for avoiding `k`-APs is equivalent to

```math
\sum_j r_k(2^j)/2^j < \infty.
```

The reverse construction isolates extremal blocks on one residue class of dyadic scales, preserving divergent reciprocal sum while eliminating cross-block APs.

Therefore cross-block forcing cannot be the missing universal ingredient for the unrestricted fixed-`k >= 4` problem.

A corrected cross-block target is only valid under additional structure, for example bounded-complexity digit rules, scale-varying automata, transducers, or finite-state dyadic block templates.

## Automatic-set theorem target

The automatic-set theorem is a good conceptual centerpiece:

> Let `A subset N` be base-`b` automatic.  If `sum_{n in A} 1/n` diverges, then `A` has positive upper density.  Consequently, by Szemerédi, `A` contains arithmetic progressions of every finite length.

The repository already records this as a proved ledger item, modulo standard regular-language growth and Szemerédi.

The proof route is:

1. Let `a_m` be the number of accepted canonical base-`b` words of length `m`.
2. The reciprocal sum is comparable to `sum_m a_m/b^m`.
3. The sequence `a_m` is controlled by the Perron spectral radius of the coaccessible transition graph.
4. If the spectral radius is less than `b`, the harmonic sum converges.
5. If the spectral radius equals `b`, deterministic `b`-digit structure forces a full branching component and positive upper density.
6. Szemerédi gives APs.

This theorem may be folklore, so the paper should not rely on novelty of this result alone.

## Algorithmic contribution

The repository has the right certification machinery for a computational-extremal paper.

The DFA 4AP certifier reads digits least-significant first and searches finite product/carry states for the two equations

```math
x_0-2x_1+x_2=0,
qquad
x_1-2x_2+x_3=0.
```

If no accepting zero-carry nontrivial state is reachable, the regular language is certified 4AP-free.

This can be upgraded into a formal theorem:

> For a zero-padding-closed DFA language over base `b`, containment of a nontrivial 4AP is decidable by a finite product/carry automaton.

This is likely the cleanest algorithmic theorem in the finite-state paper.

## Walker benchmark role

The Walker benchmark should be used as a certificate-grade computational benchmark, not as the main conceptual result.

The repository records Walker's base-55 shifted Kempner benchmark with score `4.43975` and verifies local rigidity under same-size substitutions:

```math
680
```

radius-1 neighbors checked and

```math
106590
```

radius-2 neighbors checked, with zero AP-free improving neighbors.

This is useful negative data, but it proves only local rigidity in one finite neighborhood.  It does not prove global optimality.

## PB / MaxSAT benchmark contribution

The PB / MaxSAT workflow is the natural computational spine:

1. generate cyclic AP-blocker OPB models;
2. solve externally;
3. parse assignments;
4. re-check cyclic `k`-AP-freeness;
5. compute shifted Kempner harmonic score;
6. compare against Walker's `4.43975` benchmark.

A negative result is publishable only if accompanied by solver-grade unsat/optimality certificates or independently checkable proof artifacts.

## Revised paper structure

A realistic paper should be framed as:

# Finite-State Barriers and Certified Digit Benchmarks for Erdős' Reciprocal-Sum Progression Problem

### Main Result 1

Automatic sets cannot be divergent reciprocal-sum AP-free counterexamples.

### Main Result 2

A finite product/carry automaton decides 4AP containment for zero-padding-closed DFA languages.

### Main Result 3

Certified Walker benchmark neighborhood: base 55, `k=4`, size 21, radius 1 and 2 same-size substitutions checked, no AP-free improving neighbors.

### Main Result 4

PB/MaxSAT benchmark pack for cyclic digit templates with independent rechecking and shifted harmonic scoring.

## What not to claim

Do not claim that this proves or nearly proves the full Erdős reciprocal-sum conjecture.

Do not claim that cross-block forcing is the universal missing ingredient for fixed `k >= 4`; the dyadic summability equivalence rules that out in full generality.

Do not claim Walker local rigidity as global optimality.

Do not claim novelty of the automatic-set theorem without checking the automata/regular-language literature.

## Highest-value next tasks

1. Write the automatic-set harmonic divergence theorem carefully, including canonical representations, leading-zero convention, and upper-density conclusion.
2. Formalize the DFA product/carry AP decision theorem.
3. Add a regular-language growth scorer using SCC spectral radii.
4. Generate certificate-grade small-DFA phase diagrams: number of states, base, spectral radius ratio, harmonic behavior, AP certificate.
5. Run PB/MaxSAT exact benchmark tables for small bases and selected Walker-scale profiles.
6. Treat scale-varying finite-state dyadic block rules as a separate model-class theorem, not as a universal cross-block theorem.
