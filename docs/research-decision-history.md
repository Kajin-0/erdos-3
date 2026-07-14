# Research decision history and stop list

## Purpose

This document records why the current proof program has its present form and which earlier routes should not be restarted without a materially new hypothesis.

Current theorem status is authoritative in:

1. `docs/current-proof-program.md`;
2. `docs/certainty-ledger.md`;
3. the dedicated theorem note and verifier.

The full four-term Erdős reciprocal-sum problem remains open.

---

## 1. Construction-search phase

### Periodic digit systems

Exact period-two searches, stochastic period-two/period-three searches, and local substitutions around the base-55 Walker benchmark did not improve the known exponent.

**Decision:** do not repeat ordinary periodic digit-set search or small local substitution without a new structural model.

### Solver bridge

A reproducible OPB/MaxSAT workflow was completed with exact AP recertification and true shifted harmonic scoring.

**Decision:** solver output is evidence only after exact recertification; cardinality or proxy score is not enough.

### Finite automata

The repository developed an exact DFA four-AP certifier, spectral-radius growth scoring, harmonic triage, minimization, canonicalization, and hashing.

A fixed finite automaton with divergent reciprocal sum would have sufficient growth to force positive upper density and hence long progressions.

**Decision:** fixed regular languages remain useful finite extremizers, but cannot supply a divergent reciprocal-sum AP-free counterexample.

---

## 2. Direct recursive proof phase

Coordinated side-anchor deletion and the minimum-translation backbone produce the exact one-generation inequalities

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every recursive output must be resolved into dyadic shells.

**Decision:** occurrence multiplicity, exact numerical state, and distinct-label union are separate accounting layers. None may replace another without a packing theorem.

---

## 3. Exact benchmark and contaminated obstruction

The aligned-diamond construction proves persistence can grow like

```math
|S_h|^{\log_3 2}.
```

The exact scale-eight model is summable, but the contaminated chain

```math
4,8,4,4,8,4,8,8,8
```

has

```math
W_5/W_1=91/32>1.
```

**Decisions:**

- bounded or polylogarithmic identical-history persistence is false;
- universal local `3/4` contraction is false;
- fixed short-window contraction is false;
- universal two-generation recovery is false;
- pathwise recovery cannot substitute for a treewise theorem.

---

## 4. State-specific depth-ten completion

The repository proves

```math
N_{10,2}=N_{10,4}=0
```

for the recorded `S_10` state and certifies an infinite exact factor-eight tail from every valid positive exact child.

The exact target-demand calculation shows the factor-four residual closes with margin only

```math
5,
```

not the much larger coarse half-scale excess.

**Decisions:**

- the target interval is part of the reserve state;
- one state-specific barrier is not a whole-tree theorem;
- one exact fan is not a whole-tree theorem;
- further `S_10` prefix certification is finished work, not the bottleneck.

---

## 5. Replay and schedule semantics

Replay catalogs enumerate alternative outer separations. They are not simultaneous children.

Exhaustive `S_1` schedule analysis gives `1560` progression-labeled schedules, all with zero novel fiber support. On `S_2`, one schedule has positive novelty and another has zero novelty.

**Decisions:**

- replay siblings cannot be summed in one Bellman row;
- raw novel-fiber mass is schedule dependent;
- a deletion policy must be explicit whenever schedule-dependent features are used.

---

## 6. Forced-output phase

Root-forced progressions must be selected by every complete coordinated schedule. This gives positive parent-intrinsic forced-fork output through `S_7`.

However,

```math
F(S)=P\Psi(S)
```

has the wrong parent-minus-child sign on `S_1 -> S_2`.

**Decision:** forced-fork mass is a transition resource feeding packing or obstruction growth, not a standalone stored Bellman potential.

---

## 7. Raw simultaneous transition phase

The fixed lexicographic exporter now records complete raw output through `S_7`:

| state | occurrences | state classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 0 |
| `S_2` | 11 | 10 | 3 | 5 |
| `S_3` | 25 | 21 | 23 | 15 |
| `S_4` | 46 | 34 | 91 | 35 |
| `S_5` | 68 | 51 | 145 | 88 |
| `S_6` | 94 | 71 | 209 | 150 |
| `S_7` | 127 | 95 | 345 | 214 |

Maximum pointwise multiplicity grows

```text
2,3,7,11,12,13,16,
```

while harmonic-average multiplicity remains locally small.

**Decisions:**

- raw simultaneous generation is complete for the tested policy;
- exact-state quotienting does not solve containment or partial overlap;
- worst local multiplicity is not a stable universal packing constant;
- the missing object is a provenance-preserving retention theorem.

---

## 8. Terminal-fiber cycle phase

The terminal-to-fiber incidence graph contains

```math
61\longleftrightarrow303
```

at `S_3`, persisting through `S_6`. At `S_7`, the cyclic component is

```math
\{1,5,61,303,1597,8195,323640\}.
```

At the same depth, terminal-recursive overlap contains nonhistorical labels `5`, `49158`, and `323640`.

**Decisions:**

- no strict decreasing rank of terminal labels can orient every recursive incidence;
- tracking only the latest separation is inadequate;
- tracking the complete separation history is also inadequate;
- the natural finite state is component- and provenance-based.

---

## 9. SCC capacity phase

Collapsing strongly connected components gives an acyclic condensation graph. For component `C`, define harmonic vertex mass `V(C)` and internal target mass `T(C)`.

For the two-label component through `S_6`,

```math
T(C)=V(C).
```

At `S_7`,

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

**Decision:** harmonic vertex mass alone is not sufficient SCC capacity.

The stronger linear-capacity test uses the internal adjacency matrix `A`. For the seven-label `S_7` component, the exact witness

```math
w=(43,59,31,31,14,10,26)^T
```

satisfies

```math
9Aw-23w>0,
\qquad
8w-3Aw>0.
```

Hence

```math
\frac{23}{9}<\rho(A)<\frac83.
```

**Decision:** no positive linear internal SCC capacity can be nonexpanding or factor-two contractive on the recorded `S_7` component. Any viable proof must use external obstruction export, nonlinear capacity, or multi-generation amortization.

---

## 10. Retained propagation and root-lineage transfer phase

The retained quotient was propagated through five recorded levels. Static current-generation features produced exact finite witnesses, including `H+74R` through generation four, but generation five has

```math
R_4=R_5=0
```

while recursive harmonic mass expands by a factor between `1.329813` and `1.329814`. No finite coefficient in `H+kR` repairs that transition.

The first failing transition was then tested under all-lexicographic deletion, all-reverse deletion, and each single-parent lexicographic-to-reverse flip. All fourteen tested policies expand under every maximum-harmonic retention tie. The best tested policy, `reverse_parent_82`, lowers the ratio to `1.197375982982...` but does not contract.

At the baseline transition all root provenance is unique. The exact lineage identity is

```math
H_5^{\mathrm{rec}}-H_4^{\mathrm{rec}}
=G_{4\to5}-L_{4\to5},
```

with

```text
surviving-lineage scale gain = 1.816777911848...
exiting parent release       = 1.310139720502...
net recursive increase       = 0.506638191346...
```

Of `1717` fourth recursive roots, `1015` survive and `702` exit; `17` terminalize and `685` disappear from the retained family. No root splits between recursive and terminal output.

**Decisions:**

- current-generation multiplicity is not persistent reserve;
- finite feature-LP witnesses are diagnostics, not theorem candidates without a transfer law;
- nearby deletion-policy changes do not remove the first failing expansion, although policy remains quantitatively important;
- the missing resource is cumulative ancestor-path scale capacity plus terminal/drop/obstruction release;
- generation six is blocked until a state-independent transfer lemma is proposed;
- a new feature is admissible only with a transition recurrence, bounded-reuse interpretation, and telescoping role.

---

## 11. Permanent stop list

Do not restart these routes without explicitly identifying which obstruction is avoided:

1. ordinary Walker-style modular digit search;
2. blind stochastic periodic deletion/rebuild;
3. small substitutions around the base-55 benchmark;
4. a fixed finite-automaton counterexample;
5. density exponent or cardinality as the final objective;
6. recursive deletion without shell resolution;
7. bounded or polylogarithmic persistence;
8. universal local `3/4` contraction;
9. fixed short-window contraction;
10. universal two-generation recovery;
11. pathwise summability as a whole-tree proof;
12. replay siblings as simultaneous children;
13. density, raw contamination, and shell slack as a complete reserve;
14. rectangle radius without target demand;
15. raw novelty as schedule independent;
16. `P Psi` as a standalone Bellman potential;
17. raw occurrences copied into an LP child list;
18. exact-state quotienting as an overlap theorem;
19. a uniform maximum-overlap constant inferred from the recorded path;
20. a strict decreasing terminal-label rank;
21. latest- or historical-separation-only state;
22. unit harmonic SCC capacity;
23. positive linear SCC contraction with factor at most two at `S_7`;
24. further `S_10` prefix certification;
25. the rejected depth-ten anchor reduction;
26. current-generation multiplicity as persistent reserve;
27. another feature-fit/one-more-generation loop without a transfer lemma;
28. generation-six propagation without a predeclared conceptual test.

---

## 12. Active closing target

The active target is a cumulative root-lineage reserve-transfer theorem:

```math
H_{g+1}^{\mathrm{rec}}
+A_{g+1}
+T_{g+1}^{\mathrm{first}}
\le
H_g^{\mathrm{rec}}
+A_g
+\Phi_{\mathrm{obs},g}
+\varepsilon_g.
```

Here `A_g` must be a state-independent ancestor-path capacity, `T^{first}` is newly terminal first-appearance credit, and `Phi_obs` records completion, rectangle, or cheap-extension exclusion created when capacity is released.

The next exact work is to:

1. classify survivor scale gain by parent state, source type, shell, and immediate provenance;
2. attach the `17` terminalized roots injectively to first-appearance `(u,p,i)` tokens;
3. determine what completion, rectangle, or future-extension exclusion is created by the `685` dropped lineages;
4. formulate a transfer lemma before propagating another generation.

No current theorem closes this gap. Generation six and further feature fitting are explicitly deferred.

---

## 13. Documentation protocol

Every substantive theorem, counterexample, or finite certificate should update:

1. a dedicated note;
2. a verifier and recorded certificate;
3. `docs/certainty-ledger.md`;
4. `docs/current-proof-program.md` when the dependency graph changes;
5. this decision history when a route opens or closes.

Counterexamples to proposed lemmas remain part of the permanent progress record.
