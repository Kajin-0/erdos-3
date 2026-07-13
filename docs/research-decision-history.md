# Research decision history and stop list

## Status and purpose

This document records how the project reached its current proof program and which earlier routes have already been tested, superseded, or disproved.

It is a navigation and decision document, not the primary theorem source. For current claims use:

1. `docs/current-proof-program.md`;
2. `docs/certainty-ledger.md`;
3. the dedicated note and verifier for the claim.

The purpose is to prevent context loss and repeated work.

---

## 1. Construction-search phase

### PR #1: exact period-two threshold search

Period-two digit systems in bases `11`, `12`, and `13` were exhaustively tested at size profiles above the Walker base-55 density exponent

```math
\alpha_{55}=\frac{\log21}{\log55}.
```

No certified four-term-progression-free candidate above that threshold was found.

**Decision:** do not repeat the same small-base period-two enumeration without a materially stronger model or theorem target.

### PR #2: stochastic period-two and period-three search

Witness-guided deletion and greedy rebuilding were tested. The best recorded exponent was

```math
\frac{\log6}{\log11},
```

below the Walker threshold.

**Decision:** blind or lightly guided random deletion/rebuild is not an active route.

### PR #3: literature audit and benchmark normalization

The repository reproduced public shifted Kempner benchmarks and checked same-size substitution neighborhoods of the base-55 set. No four-term-progression-free neighbor was found at substitution radius one or two.

**Decision:** do not reimplement ordinary Walker-style modular search or small local substitutions around the base-55 benchmark.

### PR #4: pseudo-Boolean solver bridge

A reproducible finite workflow was completed:

```text
OPB generation
-> external PB/MaxSAT solver
-> assignment parsing
-> exact AP recertification
-> shifted harmonic scoring.
```

**Decision:** any solver result must pass exact AP certification and true harmonic scoring. Cardinality or a linear proxy alone is not evidence of improvement.

---

## 2. Finite-state language phase

### PRs #5–#8: DFA certification and canonical search

The project developed:

- an exact least-significant-digit-first DFA four-AP certifier;
- spectral-radius growth scoring;
- bounded harmonic triage;
- random small-DFA discovery;
- DFA minimization, canonicalization, and hashing.

The growth exponent is

```math
\alpha=\frac{\log\rho(T)}{\log b}.
```

Bounded reciprocal scoring is a triage quantity, not a full transfer-operator evaluation.

### PR #9: certainty-ledger discipline

A fixed base-`b` automatic set with divergent reciprocal sum has enough growth to force positive upper density and hence arbitrarily long arithmetic progressions by Szemerédi's theorem.

**Decision:** fixed finite automata and regular digit languages remain useful for finite extremizers, but cannot produce a divergent reciprocal-sum AP-free counterexample.

---

## 3. Transition to the direct proof program

For

```math
D\subseteq[N,2N),
```

coordinated side-anchor deletion leaves a three-term-progression-free residual. Deleted occurrences generate middle-step children, while translation by the minimum generates

```math
\mathcal B(D)=\{d-\min D:d\in D,\ d>\min D\}.
```

The strongest multiplicity-resolving one-generation inequality is

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Each retained child label is at most half its parent label, and for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

**Decision:** recursive output must always be distinguished at three levels:

1. occurrence multiplicity;
2. exact numerical state;
3. distinct numerical-label union.

No level may replace another without a packing theorem.

---

## 4. Aligned-diamond obstruction

There are four-term-progression-free recursive states with

```math
P_h=2^h,
```

while

```math
|S_h|=\frac{9\cdot3^h-3}{2}.
```

Thus identical-history persistence grows like

```math
|S_h|^{\log_3 2}.
```

**Decision:** bounded, logarithmic, polylogarithmic, and subpower persistence below exponent `log_3 2` are false without additional hypotheses.

The construction is sparse in its ambient interval, so it is not a reciprocal-sum counterexample.

---

## 5. Exact and contaminated continuation phase

### PR #10: recursive deletion route

Coordinated deletion, the backbone, exact middle fibers, dyadic shell resolution, and binary genealogy accounting were consolidated.

### PR #11: exact scale-eight family

The uncontaminated equal-translate model was classified sharply. It requires scale growth at least `8`, contracts weighted density by `3/4`, and is summable.

**Decision:** exact aligned replication is no longer the bottleneck. The unresolved obstruction must use contamination, overlap, imported copies, or branching interactions.

### PR #12: contaminated-backbone chain

A certified chain with scale word

```math
4,8,4,4,8,4,8,8,8
```

through `S_10` disproved universal one-step contraction, fixed short-window contraction, and universal two-generation recovery.

The state-specific depth-ten theorem proved

```math
N_{10,2}=N_{10,4}=0,
```

while every valid exact factor-eight child enters a certified summable tail.

**Decision:** one path, one barrier state, or one complete exact fan is not a whole-tree theorem.

---

## 6. Whole-tree reserve phase

### PR #13: transport capacity and deletion-DAG diagnostics

#### Exact target demand

For four-ratio transport,

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At the `S_10` residual, the available rectangle radius exceeds exact demand by only

```math
5,
```

although it exceeds the coarse half-scale threshold by `9,474,912`.

**Decision:** radius alone is not a faithful reserve coordinate. The target interval must be part of the state.

#### Naive reserve no-go

On the recorded factor-four transition `S_6 -> S_7`, Bellman debt is positive while parent-minus-child changes in weighted density, right-shell slack, and raw contamination mass are all negative.

**Decision:** a valid reserve must contain obstruction-aware and overlap-aware information.

#### Replay siblings versus simultaneous children

The restricted replay model has alternative continuation siblings:

```text
S1 factor 4: 4
S2 factor 8: 203.
```

They are not simultaneous deletion-DAG children and cannot be summed in one Bellman row.

---

## 7. Schedule and forced-output decisions

### Exhaustive `S_1` schedules

There are

```text
120 reachable states
1560 progression-labeled schedules
930 sponsor sequences.
```

Every schedule satisfies

```math
\bigcup_q\Xi_q\subseteq\mathcal B(S_1).
```

Thus novel-fiber mass is zero for every coordinated `S_1` schedule.

### `S_2` schedule dependence

The lexicographic `S_2` schedule has novel mass

```math
\frac{239396453}{200655312}>0,
```

but another valid schedule has zero novelty.

**Decision:** raw novel-fiber mass is not a parent-only reserve.

### Root-forced forks

A root-forced progression must be selected in every complete coordinated schedule. This gives a positive parent-intrinsic lower bound

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D)
```

through the recorded `S_7`.

However, `P Psi` increases across `S_1 -> S_2` while that factor-four step has positive debt.

**Decision:** forced-fork output is a transition resource, not a standalone telescoping potential.

---

## 8. Raw transition and overlap phase

### Complete fixed-policy raw exporter

The repository now exports every raw simultaneous occurrence from one complete lexicographic schedule, including:

- shell resolution;
- point-level provenance;
- exact duplicate classes;
- strict containment;
- partial overlap;
- terminal-recursive overlap;
- exact occurrence and union masses.

The certified frontier is:

| state | occurrences | state classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 0 |
| `S_2` | 11 | 10 | 3 | 5 |
| `S_3` | 25 | 21 | 23 | 15 |
| `S_4` | 46 | 34 | 91 | 35 |
| `S_5` | 68 | 51 | 145 | 88 |
| `S_6` | 94 | 71 | 209 | 150 |
| `S_7` | 127 | 95 | 345 | 214 |

**Decision:** raw simultaneous generation is complete for the tested policy. The missing layer is retention and bounded reuse.

### Pointwise multiplicity

The exact maximum multiplicities through `S_7` are

```text
2,3,7,11,12,13,16,
```

while harmonic-average multiplicity remains below the certified small constants `8/5`, `11/10`, or `9/8`.

**Decision:** worst local multiplicity is unstable. A useful packing theorem must be provenance-sensitive and harmonically weighted.

---

## 9. Terminal-fiber cycle phase

### Incidence graph

Draw an edge

```math
q\to u
```

when `q` and `u` are terminal labels and `u in Xi_q`.

The graph contains

```math
61\leftrightarrow303
```

at `S_3`, persisting through `S_6`. At `S_7`, the cyclic component becomes

```math
\{1,5,61,303,1597,8195,323640\}.
```

**Decision:** no strict decreasing rank of terminal labels can orient every recursive incidence.

### Historical-separation state failure

Through `S_6`, terminal-recursive overlap equals the base step plus historical separations. At `S_7`, additional labels `5`, `49158`, and `323640` appear.

**Decision:** neither the latest separation nor the separation history is a sufficient overlap state.

### SCC quotient and capacity no-go

Collapsing strongly connected components gives an acyclic condensation graph. For a component `C`, define harmonic vertex capacity `V(C)` and internal target mass `T(C)`.

For `C={61,303}` through `S_6`,

```math
T(C)=V(C).
```

At `S_7`,

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

**Decision:** SCC condensation solves ordering but not recycling. Unit harmonic vertex mass is not sufficient component capacity.

---

## 10. Permanent stop list

Do not restart any of the following without a materially new hypothesis, invariant, or model:

1. ordinary Walker-style modular digit-set search;
2. blind stochastic periodic deletion/rebuild;
3. small substitutions around the base-55 benchmark;
4. a fixed finite-automaton counterexample route;
5. density exponent or cardinality as the final objective;
6. recursive deletion before dyadic shell resolution;
7. bounded or polylogarithmic identical-history persistence;
8. persistence below exponent `log_3 2` from cardinality alone;
9. universal local `3/4` contraction in contaminated states;
10. fixed four- or six-generation contraction;
11. universal two-generation recovery;
12. pathwise summability as a whole-tree proof;
13. replay siblings as simultaneous Bellman children;
14. a reserve using only density, raw contamination, and shell slack;
15. rectangle radius without target demand;
16. raw novelty as schedule independent;
17. `P Psi` as a standalone Bellman potential;
18. copying raw occurrences into an LP child list;
19. exact-state quotienting as a solution to containment or partial overlap;
20. a uniform maximum-overlap constant inferred from the recorded path;
21. a strict decreasing terminal-label rank;
22. tracking only latest or historical separations;
23. assigning each SCC only harmonic vertex mass;
24. additional `S_10` prefix certification after complete closure;
25. the rejected depth-ten anchor reduction.

A route may be reopened only if the proposal explicitly identifies which prior obstruction it avoids.

---

## 11. Active closing target

The current bottleneck is a cyclic-component retention and whole-tree packing theorem.

The required object is a nonnegative potential satisfying

```math
\Delta(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(
\operatorname{Pack}(S')+
\Phi_{\rm obs}(S')
\right)
\le
\operatorname{Pack}(S)+
\Phi_{\rm obs}(S)+
\operatorname{controlled\ error}.
```

The next finite experiment must attach explicit internal capacity vectors to terminal-fiber SCCs and test whether

```math
\text{internal recycling}
+
\text{outgoing capacity}
\le
\text{incoming capacity}
+
\text{obstruction export}
```

holds on the certified `S_1` through `S_7` transitions.

The state must also account for:

1. provenance-distinct exact duplicates;
2. strict containment and partial overlap;
3. terminal-recursive overlap;
4. cyclic internal edge multiplicity;
5. affine obstruction and rectangle coverage;
6. target-specific completion and transport deficits;
7. exact Bellman debt.

No current theorem closes this gap.

---

## 12. Documentation protocol

Every substantial result must be classified as:

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
5. this decision history when a route is opened or closed.

Counterexamples to proposed lemmas must remain documented. Eliminating a false closing route is part of the progress record.
