# Research decision history and stop list

## Status and purpose

This document records how the project reached its current proof program and which earlier routes have already been tested, superseded, or disproved.

It is a navigation and decision document, not the primary source for theorem statements. For current mathematical claims, use:

1. `docs/current-proof-program.md`;
2. `docs/certainty-ledger.md`;
3. the dedicated proof note and verifier for the claim.

The purpose of this file is to prevent context loss and repeated work.

---

## 1. Computational construction phase

### PR #1: exact period-two threshold search

The first merged search layer exhaustively tested period-two digit systems in bases `11`, `12`, and `13` at size profiles exceeding the Walker base-55 density exponent

```math
\alpha_{55}=\frac{\log 21}{\log 55}\approx0.759737785.
```

No certified four-term-progression-free candidate above that threshold was found.

**Durable consequence:** do not repeat the same small-base period-two enumeration without a materially stronger model, search reduction, or theorem target.

### PR #2: stochastic period-two and period-three search

Witness-guided deletion and greedy rebuilding were tested for periodic digit systems. The best recorded candidate had

```math
\alpha=\frac{\log 6}{\log 11}\approx0.747221736,
```

below the Walker threshold.

**Durable consequence:** blind or lightly guided random deletion/rebuild is not an active research route.

### PR #3: literature audit and benchmark normalization

The literature and public-code audit established that ordinary modular digit-set branch-and-bound substantially overlaps Alexander Walker's public work. The repository then normalized the public base-11 and base-55 shifted Kempner benchmarks, reproduced their scores, and checked the radius-one and radius-two same-size substitution neighborhoods of the base-55 set.

The base-55 benchmark score is

```math
4.4397533693\ldots
```

under the repository's shifted convention. No four-term-progression-free same-size neighbor was found at substitution radius one or two.

**Durable consequence:** do not spend research time reimplementing ordinary Walker-style modular search or making small local substitutions around the base-55 benchmark.

### PR #4: pseudo-Boolean solver bridge

The repository completed a reproducible one-layer cyclic workflow:

```text
OPB generation
-> external PB/MaxSAT solver
-> assignment parsing
-> exact AP recertification
-> shifted harmonic scoring.
```

This remains usable infrastructure for finite extremizer experiments.

**Durable consequence:** any future solver result must pass exact AP certification and true harmonic scoring. Cardinality or a linear proxy alone is not evidence of improvement.

---

## 2. Finite-state language phase

### PR #5: exact DFA four-AP certifier

The project moved beyond one-layer digit sets to least-significant-digit-first deterministic finite automata. A finite product automaton tracks four language states, two arithmetic carries, and nontriviality, giving an exact four-AP certificate for a fixed DFA.

### PR #6: DFA growth and bounded harmonic triage

The digit-transition spectral radius and bounded shifted reciprocal sums were added as candidate-ranking tools.

For transition matrix `T`, the growth exponent is

```math
\alpha=\frac{\log\rho(T)}{\log b}.
```

The bounded reciprocal score is only a lower-bound triage quantity. It is not a full transfer-operator evaluation of an arbitrary regular language.

### PR #7: random small-DFA discovery

A random small-DFA generator was added with exact four-AP certification and bounded scoring. This was explicitly a discovery harness, not an optimality proof.

### PR #8: DFA minimization and canonicalization

Unreachable states are removed, equivalent states are minimized, and the result is canonically renamed and hashed. This prevents duplicate automaton presentations from appearing to be new languages.

### PR #9: certainty-ledger discipline

The certainty ledger was introduced to separate proved claims, finite computations, conjectures, corrections, and open bottlenecks. One important theorem recorded during this phase is that a fixed base-`b` automatic set with divergent reciprocal sum must have enough growth to force positive upper density, and hence arbitrarily long arithmetic progressions by Szemerédi's theorem.

**Durable consequence:** fixed finite automata and regular digit languages can be used to study finite extremizers and structure, but they cannot produce a divergent reciprocal-sum AP-free counterexample.

---

## 3. Transition to the active proof program

After the first nine PRs, the project moved from construction search to a direct proof program for the four-term-progression-free case.

For a block

```math
D\subseteq[N,2N),
```

coordinated side-anchor deletion leaves a three-term-progression-free residual of size at most `r_3(N)`. The deleted occurrences generate lower-scale middle-step children, while translation by the minimum generates the backbone

```math
\mathcal B(D)=\{d-\min D:d\in D,\ d>\min D\}.
```

The strongest multiplicity-resolving one-generation inequality currently recorded is

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every retained child associated with a parent label `a` has label at most `a/2`, and each parent generates at most two retained outputs. Thus, for every `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

Subsequent center, root-anchor, predecessor-anchor, and complete-history decompositions resolve many forms of repeated terminal output.

---

## 4. The aligned-diamond obstruction

The project then found a sharp obstruction to all cardinality-only persistence arguments.

There are four-term-progression-free recursive states `S_h` producing

```math
2^h
```

terminal copies of the same local progression with the same complete anchor history, while

```math
|S_h|=\frac{9\cdot3^h-3}{2}.
```

Therefore

```math
\text{identical-history persistence}
\asymp
|S_h|^{\log_3 2}.
```

The explicit depth-two state has `39` points and produces four identical-history copies; it is checked by `src/verify_self_replicating_aligned_diamond_depth2.py`.

**Durable consequence:** the following targets are false without additional hypotheses:

1. bounded identical-history persistence;
2. logarithmic or polylogarithmic persistence;
3. a bound `O(|D|^theta)` for `theta<log_3 2`;
4. a theorem forbidding aligned replication from four-AP-freeness alone.

The construction is sparse in its ambient interval, so it is not a divergent reciprocal-sum counterexample.

---

## 5. Permanent stop list

Do not restart any of the following as an active route unless a new hypothesis, invariant, or model materially changes the problem.

1. Naive modular digit-set branch-and-bound duplicating Walker's search class.
2. Blind stochastic period-two or period-three deletion/rebuild.
3. Radius-one or radius-two substitutions around the Walker base-55 set.
4. A fixed finite-automaton or regular-language counterexample construction.
5. Treating density exponent, cardinality, or a linear harmonic proxy as the final objective.
6. Recursive arguments that reapply deletion before standard dyadic shell resolution.
7. Universal one-copy-per-anchor or one-copy-per-history claims.
8. Bounded, logarithmic, or polylogarithmic identical-history persistence.
9. Subpower persistence below exponent `log_3 2` in terms of parent cardinality.
10. Any closing argument that ignores the ambient scale required to realize repeated aligned diamonds.

A route may be reopened only if the new proposal explicitly identifies which prior obstruction it avoids.

---

## 6. Active closing target

The current bottleneck is density-sensitive aligned replication.

The required theorem must show that blocks carrying substantial reciprocal mass cannot sustain aligned-diamond replication efficiently across scales.

Useful quantitative formulations include:

1. an ambient-scale lower bound for `h` replication levels;
2. a tradeoff between persistence `P` and dyadic density `|D|/N`;
3. a potential coupling reciprocal mass to the replication law
   ```math
   |S_h|\asymp3^h,
   \qquad
   P_h=2^h;
   ```
4. a classification of constructions approaching minimum scale growth;
5. a proof that nonsummable dyadic density is incompatible with indefinite efficient replication.

A natural extremal quantity for experiments and theorem design is

```math
\Phi(P)
=
\sup
\left\{
P\frac{|D|}{N}:
D\subseteq[N,2N)
\text{ is four-AP-free and supports persistence at least }P
\right\}.
```

Decay of `Phi(P)`, or an aggregate Carleson-type analogue, would directly connect persistence control to reciprocal-mass summability.

---

## 7. Documentation protocol

Every substantial future result should be classified as one of:

- proved in the repository;
- computationally certified;
- heuristically supported;
- conjectural;
- false or superseded;
- open bottleneck.

A substantive theorem, counterexample, or finite certificate should normally update:

1. a dedicated proof or experiment note;
2. `docs/certainty-ledger.md`;
3. `docs/current-proof-program.md` when the dependency graph changes;
4. a verifier and reproducible data when the claim is finite;
5. the README only when the project-level summary changes.

Counterexamples to proposed lemmas must be documented, because eliminating a false closing route is part of the progress record.
