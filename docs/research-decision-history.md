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

## 5. Contaminated continuation and reserve phase

### PR #10: recursive deletion route

The repository consolidated coordinated side-anchor deletion, the minimum-translation backbone, exact middle multiplicity fibers, standard dyadic shell resolution, and binary genealogy accounting into the active recursive program.

**Durable consequence:** recursive output must always be distinguished at three levels:

1. occurrence multiplicity;
2. exact-state equivalence;
3. distinct numerical-label union.

No one level may be substituted for another without an explicit packing theorem.

### PR #11: exact scale-eight family

The exact equal-translate model was classified sharply. Uncontaminated reproduction requires scale growth at least `8`, its weighted density contracts by the exact factor `3/4`, and the resulting infinite family is summable despite unbounded identical-history multiplicity.

**Durable consequence:** exact aligned replication is no longer the bottleneck. Any unresolved obstruction must use contamination, overlap, imported copies, or branching interactions absent from the exact model.

### PR #12: contaminated-backbone chain

A certified finite chain with scale word beginning

```math
4,8,4,4
```

showed that contaminated replay can increase multiplicity-weighted density and defeat one-step, four-generation, six-generation, and universal two-generation recovery claims. The recorded genealogy was subsequently extended through `S_10` with scale word

```math
4,8,4,4,8,4,8,8,8.
```

The state-specific depth-ten analysis then proved

```math
N_{10,2}=N_{10,4}=0,
```

while every valid exact factor-eight child enters a certified summable exact tail.

**Durable consequence:** one distinguished path, one barrier state, or one complete exact fan is not a whole-tree theorem.

### PR #13: transport capacity and deletion-DAG reserve diagnostics

This phase introduced the first exact infrastructure and finite obstructions for a whole-tree reserve.

#### Exact transport demand

For four-ratio rectangle transport, define

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

The integer transport windows coalesce exactly when

```math
2U+1\ge S.
```

For the recorded `S_10` residual, the available rectangle radius exceeds the exact target demand by only

```math
5,
```

even though it exceeds the coarse half-scale overlap threshold by `9,474,912`.

**Durable consequence:** normalized radius alone is not a faithful reserve coordinate. The admissible target interval must be part of the state.

#### Naive reserve no-go

For the certified factor-four transition `S_6 -> S_7`, Bellman debt is positive while parent-minus-child changes in weighted density, right-shell slack, and raw contamination mass are all negative. Therefore no nonnegative linear combination of those three coordinates can pay even this single transition.

**Durable consequence:** a valid reserve must contain obstruction-aware and overlap-aware information, not merely mass, slack, or contamination count.

#### Replay siblings versus simultaneous children

The restricted replay model already has several valid alternative continuations:

```text
S1 factor 4: 4 valid separations;
S2 factor 8: 203 valid separations.
```

These are alternative continuation siblings. They are not automatically simultaneous deletion-DAG children and cannot be summed in one Bellman row without a retention/packing theorem.

#### Exact `S_1` simultaneous-child obstruction

For one complete `S_1` deletion resolution, all middle-fiber labels are already contained in the simultaneous minimum-translation backbone. Exhausting all coordinated progression-labeled schedules gives

```text
120 reachable vertex sets;
1,560 complete schedules;
930 sponsor sequences;
```

and every schedule satisfies

```math
\bigcup_q\Xi_q\subseteq\mathcal B(S_1).
```

Thus the novel-fiber mass

```math
\mathcal N(D)
=
H\left(
\left(\bigcup_q\Xi_q\right)
\setminus\mathcal B(D)
\right)
```

vanishes for every coordinated schedule on `S_1`.

#### First positive novel-fiber reference

Under the deterministic coordinated rule on `S_2`, the novel support is

```math
\{1,16,21,26,62,77,123,138\}
```

with exact positive harmonic mass

```math
\mathcal N(S_2)
=
\frac{239396453}{200655312}.
```

The fibers also overlap each other before the backbone is included.

**Durable consequence:** novel-fiber mass is nontrivial but is not yet known to be schedule-independent, monotone, or sufficient for a Bellman reserve.

---

## 6. Permanent stop list

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
11. Universal one-step `3/4` contraction for contaminated backbones.
12. Universal strict contraction at every non-exact step.
13. Contraction over every fixed four- or six-generation window.
14. Universal two-generation recovery after an exact factor-eight step.
15. Treating pathwise summability as sufficient for the branching deletion tree.
16. Treating alternative valid replay separations as simultaneous Bellman children.
17. A reserve built only from weighted density, raw contamination count, and geometric shell slack.
18. A reserve using rectangle radius without the target interval it is required to cover.
19. Assuming middle multiplicity fibers add distinct support beyond the backbone.
20. Additional contiguous `S_10` prefix certification after complete factor-two/factor-four closure.

A route may be reopened only if the new proposal explicitly identifies which prior obstruction it avoids.

---

## 7. Active closing target

The current bottleneck is a whole-tree contamination reserve and overlap-packing theorem.

A pathwise estimate is insufficient: exponentially many paths can each have finite charge while the full continuation tree diverges. The required object is a nonnegative potential `Phi` in Bellman units satisfying an inequality of the form

```math
W(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(\mathfrak B(S')+\Phi(S')\right)
\le
\mathfrak B(S)+\Phi(S)
+
\operatorname{controlled\ error}.
```

The next finite question is now sharply defined on `S_2`:

```math
\min_\sigma\mathcal N_\sigma(S_2),
\qquad
\max_\sigma\mathcal N_\sigma(S_2),
```

where `sigma` ranges over coordinated progression-labeled deletion schedules.

- A positive minimum would establish schedule-independent obstruction export at the first descendant.
- A zero minimum would exhibit an exact schedule that erases the apparent reserve.
- Either outcome constrains the state variables required by a whole-tree potential.

The larger theorem must also account for:

1. complete simultaneous child aggregates rather than alternative replay choices;
2. exact duplicate states and strict child containment;
3. imported-prefix provenance;
4. within-middle overlap;
5. target-specific rectangle demand;
6. bounded overlap or Carleson packing across different parents;
7. exact Bellman debt from factor-two and factor-four steps.

Useful computational infrastructure now includes:

- `src/branching_reserve_lp.py` for exact-rational LP export and verification;
- `src/export_replay_transition_catalog.py` for alternative replay catalogs;
- `src/verify_s1_deletion_dag_adapter.py` for a complete simultaneous child ledger;
- `src/verify_s1_all_deletion_schedules.py` for exhaustive base-state schedule analysis;
- `src/verify_s2_novel_fiber_reference.py` for the first positive novel-fiber reference;
- `.github/workflows/lightweight-proof-checks.yml` for automatic certificate regeneration.

---

## 8. Documentation protocol

Every substantial future result should be classified as one of:

- proved in the repository;
- computationally certified;
- heuristically supported;
- conjectural;
- false or superseded;
- open bottleneck.

A substantive theorem, counterexample, or finite certificate should update:

1. a dedicated proof or experiment note;
2. `docs/certainty-ledger.md`;
3. `docs/current-proof-program.md` when the dependency graph changes;
4. a verifier and reproducible data when the claim is finite;
5. the README only when the project-level summary changes.

Counterexamples to proposed lemmas must be documented, because eliminating a false closing route is part of the progress record.