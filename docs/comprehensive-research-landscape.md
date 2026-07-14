# Comprehensive research landscape for the four-term case

## Status and scope

This document is the strategic map of the repository's work on the four-term-progression-free case of Erdős Problem #3.

The ambient problem is:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The repository studies the four-term case: whether every four-term-progression-free subset of the positive integers has convergent reciprocal sum.

This overview is **repository-comprehensive**, not literature-comprehensive. It records the mathematical territory explored here through claim `CL-065`: proved positive results, exact finite and infinite certificates, failed proof principles, model boundaries, and the current roadmap. External novelty and priority still require a separate literature audit before publication.

Authoritative sources remain:

- `docs/current-proof-program.md` for the active theorem chain;
- `docs/certainty-ledger.md` for atomic claim status;
- `docs/research-decision-history.md` for chronology and permanent stops;
- dedicated theorem notes, verifiers, and certificates for individual results.

This document is organized by mathematical dependency rather than commit history.

---

# 1. Executive assessment

The project has moved through four distinct stages.

## 1.1 Construction and search

The initial phase explored modular digit sets, periodic digit systems, pseudo-Boolean search, and finite automata. These routes produced exact certification infrastructure and useful finite benchmarks, but no divergent-reciprocal-sum four-AP-free construction.

The durable conclusion is:

```math
\text{fixed finite-state digit models are useful extremizers and certifiers, not the active proof route.}
```

## 1.2 Recursive deletion and persistence

Coordinated side-anchor deletion and the minimum-translation backbone produced strong one-generation harmonic inequalities. Exact middle-multiplicity fibers, shell resolution, and anchor-history compression isolated the surviving obstruction: identical recursive histories can persist with polynomial multiplicity.

The aligned-diamond construction gives

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp |S_h|^{\log_3 2}.
```

An exact scale-eight refinement satisfies

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

## 1.3 Debt, recovery, and structural transport

The exact uncontaminated equal-translate model is sharply summable, but contaminated backbones defeat local contraction. A certified path has scale word

```text
4,8,4,4,8,4,8,8,8
```

and disproves universal one-step contraction, fixed four- and six-generation contraction, and universal two-generation recovery.

The exact Bellman debt created by a scale factor `c` is

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

The recorded depth-ten state is completely closed against cheap continuations:

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The factor-four proof replaces direct enumeration of `348012826` candidates by inherited obstruction, lifted completion support, complete direct rectangle support, and four-ratio transport.

## 1.4 Policy-aware whole-tree packing

The project then moved from selected paths and replay catalogs to the actual simultaneous deletion output. This exposed duplicate states, strict containments, partial overlaps, terminal-recursive overlap, cyclic terminal-fiber components, schedule dependence, and regeneration.

The current objective is a policy-aware retained-child inequality of the schematic form

```math
\Delta(S)
+
\sum_{S'\in\mathrm{Child}_\pi(S)}
\left(
\mathrm{Pack}(S')+\Phi_{\rm obs}(S')
\right)
\le
\mathrm{Pack}(S)+\Phi_{\rm obs}(S)
+
\mathrm{controlled\ error}.
```

The decisive missing object is a **provenance-preserving retention quotient** converting raw overlapping simultaneous output into legitimate Bellman children.

---

# 2. Logical target and required bridge

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

reciprocal divergence is equivalent up to constants to

```math
\sum_j\alpha_j=\infty.
```

Thus the four-term case would follow from summability of the dyadic densities of every four-AP-free set.

The recursive program starts from a four-AP-free dyadic block

```math
D\subseteq[N,2N)
```

and generates lower-scale four-AP-free outputs. One generation produces more harmonic output than the parent, up to a Roth-error term. The hard problem is global: numerical labels repeat, descendants overlap, and many outputs coexist.

The needed conclusion is not merely pathwise:

```math
\sup_\gamma\sum_{S\in\gamma}W(S)<\infty.
```

Exponentially many individually summable paths can still have divergent total mass. The required theorem must be treewise and must provide:

1. exact simultaneous child semantics;
2. a retention and packing rule;
3. preservation of provenance under quotienting;
4. control of duplicate, containment, and partial overlap;
5. capacity for cyclic internal recycling and outgoing recursive load;
6. prevention of repeated payment by the same provenance across generations;
7. a globally summable error term;
8. a final deduction to `sum_j alpha_j < infinity`.

Any result missing one of these links is partial progress, not a proof of the four-term case.

---

# 3. Claim-status convention

The repository distinguishes:

- **Theorem** — symbolic proof from explicit definitions and lemmas.
- **Exact finite theorem** — complete finite classification with exact arithmetic and a recorded certificate.
- **Exact infinite theorem** — finite certification plus a symbolic induction, recurrence, or automaton argument.
- **No-go theorem** — exact counterexample, sign obstruction, spectral obstruction, or infeasibility certificate.
- **Experimental evidence** — sampling, heuristic search, or incomplete enumeration.
- **Conjecture** — proposed statement not yet proved.
- **Superseded** — a claim or route replaced or invalidated by a stronger result.

See `docs/certainty-ledger.md` for authoritative status.

---

# 4. Positive theorem spine

## 4.1 Coordinated deletion and backbone inequalities

For a four-AP-free block `D subseteq [N,2N)`, coordinated side-anchor deletion leaves a three-AP-free residual of size at most `r_3(N)`. The minimum-translation backbone and selected middle fibers satisfy

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N.
```

After exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

These are strong one-generation production inequalities. They do not control repeated descendants globally.

Primary references:

- `docs/minimum-translation-backbone-recursion.md`;
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md`;
- `docs/side-anchor-deletion-dag.md`.

## 4.2 Mandatory dyadic shell resolution

Every lower-scale output must be resolved into standard dyadic shells. For each parent label `a`, there are at most two retained outputs, each at most `a/2`. Hence, for every `p >= 1`,

```math
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
```

This gives logarithmic depth and positive-moment control. It does not control reciprocal mass.

Primary reference:

- `docs/half-contraction-multiscale-label-potential.md`.

## 4.3 Multiplicity compression by geometry and history

Repeated terminal labels are compressed through:

1. lifted-center difference layers;
2. root-anchor difference layers;
3. predecessor-anchor difference layers;
4. complete-anchor-history antichain bounds.

For fixed complete anchor history,

```math
\lambda_{x,q}(t)(a-t)\le a.
```

The residual obstruction consists of identical local progressions produced by state occurrences with the same complete anchor history.

Primary references:

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`.

## 4.4 Aligned-diamond persistence obstruction

The aligned-diamond recursion satisfies

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so persistence grows polynomially in state size:

```math
P_h\asymp |S_h|^{\log_3 2}.
```

This rules out bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds without additional hypotheses.

## 4.5 Exact scale-eight infinite family

There is an explicit infinite four-AP-free family with

```math
L_h=8^{h+1},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton and a 17,238-state product/carry search certify four-AP-freeness of the full infinite language.

Primary references:

- `docs/scale-eight-self-replicating-aligned-diamond.md`;
- `src/verify_scale_eight_aligned_diamond.py`.

## 4.6 Sharp exact equal-translate theorem

In the uncontaminated equal-translate model, exact reproduction requires

```math
L'\ge8L.
```

Three translate layers are maximal because four layers contain `0,R,2R,3R`. Two persistent children are maximal because the genealogy is binary. The exact one-step efficiency is

```math
\rho_{\rm exact}=\frac{2\cdot3}{8}=\frac34.
```

Consequently,

```math
P_h\alpha_h\le C_0\left(\frac34\right)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

The exact model is sharply classified and summable.

Primary references:

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

## 4.7 Contaminated replication and Bellman debt

The contaminated chain begins

```text
4,8,4,4
```

and has

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

An extended branch reaches

```text
4,8,4,4,8,4,8,8,8.
```

For constant exact scale factor `c > 6`, the future-cost function is

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right).
```

At `c=8`,

```math
\mathfrak B_8=\frac{4P(N+1)}L.
```

The exact debt identity is

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

Factors `2` and `4` create debt, factor `8` is neutral, and factors at least `16` create surplus. This is accounting, not yet a repayment theorem.

## 4.8 Complete depth-ten cheap-extension closure

For the recorded state `S_10`,

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The exact factor-four domain has `348012826` layer-disjoint candidates and is partitioned as

```math
33026376+137142200+177844250=348012826.
```

The three classes are removed by:

1. inherited depth-nine obstruction;
2. lifted depth-nine completion support;
3. complete direct rectangle support in `B_9={0} union S_9` and four-ratio transport.

The direct rectangle-support theorem proves

```math
[1,76583776]\subseteq\mathcal R(B_9).
```

A base rectangle with effective separation `U` transports through the next replication at precisely

```math
k=1,2,3,4,
```

covering targets

```math
T=kR_9\pm U.
```

The resulting windows cover the entire residual interval. No cancellation channel exists for `k >= 5`.

This is the strongest example in the repository of replacing enormous enumeration by a reusable structural theorem.

Primary references:

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `docs/four-ratio-rectangle-transport-and-residual-profile.md`;
- `docs/three-translate-obstruction-coverage-recurrence.md`;
- `src/run_verify_s10_factor4_rectangle_closure.sh`.

## 4.9 Complete exact factor-eight fan from `S_10`

Every valid positive exact factor-eight child of `S_10` has an explicit infinite exact four-AP-free continuation. The complete fan contains

```math
408855759
```

valid children. Standard schedules handle nearly all of them; the remaining failures are repaired by one `+1` perturbation at the second or third step. Every tail has total charge

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

This classifies one exact fan, not all contaminated descendants.

Primary reference:

- `docs/complete-exact-child-tail-fan.md`.

## 4.10 Raw simultaneous transition frontier

For a fixed lexicographic deletion policy, complete raw simultaneous output is exported through `S_7` with exact state classes, provenance, duplicates, containments, partial overlaps, terminal-recursive overlap, and harmonic ledgers.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

These are raw simultaneous occurrences, not retained Bellman children.

Primary references:

- `docs/simultaneous-deletion-transition-exporter.md`;
- `docs/simultaneous-transition-frontier-s5.md`;
- `docs/simultaneous-transition-frontier-s7.md`.

## 4.11 Policy-aware exact finite cone through `S_7`

Deletion policy changes terminal mass, recursive occurrence load, duplication, residual error, SCC structure, and long-range regeneration.

The current finite score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi.
```

The repository exhausts all `32` subsets of delayed steps

```text
{5,40,30,161,142}
```

on `S_1,...,S_7`; on `S_7` it tests both seed-delay states and reverse deletion. The exact rational LP contains `250` constraints. The witness

```math
(\lambda,\gamma)=\left(3,\frac1{10}\right)
```

remains feasible.

Policy selection is not stable under family enlargement:

- the unique `S_3` winner changes to `delay_5_161_142`;
- the unique `S_7` winner changes from `seed_5` to the non-regenerative `seed_5_142`.

The five-step subset lattice is exhaustive only for this delayed-step universe. It is not exhaustive over arbitrary progression steps or all complete schedules.

Most importantly, policy-ranking feasibility is not branching Bellman feasibility because retained simultaneous children remain undefined.

Primary references:

- `docs/policy-occurrence-cone-s1-s7.md`;
- `docs/two-coordinate-policy-family.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-subset-lattice-s1-s7.md`.

---

# 5. Explored model space

| Model | Status | Main conclusion |
|---|---|---|
| One-layer modular digit sets | explored and benchmarked | ordinary Walker-style search is not the active route |
| Periodic digit systems | exact small-base and stochastic searches | naive periodic extension did not improve the benchmark |
| Pseudo-Boolean/MaxSAT templates | infrastructure complete | solver output requires exact recertification and true harmonic scoring |
| Fixed finite automata | exact 4-AP certifier and growth tools | useful finite extremizers; not a direct divergent counterexample route |
| One-generation deletion recursion | strong exact inequalities | creates harmonic gain but not global packing |
| Exact equal-translate replication | sharply classified | scale 8 is minimal and the model is summable |
| Contaminated selected paths | extensive exact constructions | local and fixed-window contraction fail |
| State-specific obstruction closure | completed through `S_10` | completion and rectangles can repay cheap debt completely |
| Replay catalogs | exact finite catalogs | replay siblings are alternative choices, not simultaneous children |
| Raw simultaneous deletion output | exported through `S_7` | provenance, overlap, and cyclic structure are essential |
| Finite policy optimization | full five-step subset lattice through `S_7` | a stable two-coordinate witness exists, but winners change under enlargement |
| Retained-child packing | open | decisive missing theorem |

Earlier models remain benchmarks, counterexamples, or infrastructure. The active route is retained-child packing.

---

# 6. Negative results and permanent lessons

The following failures materially constrain any future proof. Each is mathematical progress.

| Proposed route | Exact obstruction or result | Durable consequence |
|---|---|---|
| ordinary modular digit search | no improvement in tested periodic and local-substitution regimes | do not restart without a new structural model |
| fixed finite-automaton counterexample | sufficient regular-language growth would force positive-density behavior | use automata as certifiers or quotients, not as the direct counterexample ansatz |
| bounded or polylogarithmic persistence | aligned diamonds have `P_h asymp |S_h|^{log_3 2}` | any global theorem must be density-sensitive |
| universal one-step `3/4` contraction | contaminated factor-four burst gives `W_5/W_1=91/32` | allow debt and delayed repayment |
| fixed four- or six-step contraction | certified contaminated paths violate both | no fixed short-memory scale-word theorem is justified |
| universal two-generation recovery | factor-eight recovery can be followed by another factor-four release | recovery is state dependent |
| pathwise summability | simultaneous branching and overlap remain | a treewise packing theorem is necessary |
| replay siblings as Bellman children | replay choices are alternatives, not coexisting outputs | only simultaneous retained output belongs in one row |
| raw novelty as an intrinsic reserve | `S_2` has positive- and zero-novelty schedules | schedule-dependent features require an explicit policy or minimax theorem |
| density, slack, and raw contamination as complete reserve | the naive cone fails on `S_6 -> S_7` | additional structural coordinates are necessary |
| rectangle radius without target demand | exact `S_10` closure margin is only `5` | obstruction support must be demand-aware |
| `P Psi` as stored potential | wrong parent-minus-child sign on `S_1 -> S_2` | forced-fork mass is a transition resource, not a standalone potential |
| exact-state quotienting | strict containment and partial overlap persist | numerical equality does not solve packing |
| a uniform local overlap constant | pointwise multiplicity grows `2,3,7,11,12,13,16` | cross-generation provenance reuse must be controlled |
| strict decreasing terminal-label rank | `61 <-> 303` and a seven-label `S_7` SCC | component state is necessary |
| separation-history-only state | nonhistorical overlap labels appear at `S_7` | provenance exceeds outer-separation history |
| unit harmonic SCC capacity | internal target mass exceeds vertex mass at `S_7` | internal recycling needs external or nonlinear credit |
| positive linear SCC contraction by factor two | `23/9 < rho(A) < 8/3` | no positive linear internal capacity can contract by factor two |
| avoid regeneration at all costs | reverse deletion avoids the seed but explodes output and SCC load | policy must balance immediate and future costs |
| occurrence cost alone | step-5 delay improves local score but keeps canonical regeneration | continuation-sensitive coordinates are required |
| greedy composition of favorable delays | delaying step `30` alone helps; adding it after `5,40` hurts everywhere tested | policy interactions are genuinely nonadditive |
| finite-family winner as theorem | winners change at `S_3` and `S_7` under enlargement | monitor the feasible cone, not one selected policy |
| policy half-space feasibility as Bellman feasibility | retained children are undefined | the LP is diagnostic until a retention theorem exports legitimate rows |
| depth-ten anchor reduction | audit found an uncovered gap | use the replacement completion-and-rectangle proof only |
| further direct `S_10` prefix certification | complete structural closure now exists | state-specific enumeration is finished work |

Primary details are distributed across `docs/research-decision-history.md`, `docs/certainty-ledger.md`, and the dedicated no-go notes.

---

# 7. The depth-ten theorem as a model of productive progress

The initial factor-four problem at `S_10` was posed as a search over hundreds of millions of separations. That formulation was finite but low leverage.

The successful reformulation was structural:

1. embed the completed `S_9` obstruction into the lower interval;
2. lift depth-nine completion coordinates through the three-copy geometry;
3. prove complete direct rectangle support for `B_9`;
4. express every residual target as
   ```math
   T=kR_9\pm U,
   \qquad 1\le k\le4;
   ```
5. apply the four-ratio cancellation theorem.

The reusable mechanism is

```math
\text{cheap replication}
\longrightarrow
\text{inherited completion and rectangle structure}
\longrightarrow
\text{coverage of future cheap-separation demand}.
```

This is a concrete form of debt repayment. A future general theorem should measure not raw obstruction volume, but normalized coverage of the next admissible target interval.

The limitation remains state dependence: no theorem yet proves that every contaminated branch develops an `S_10`-type coverage reserve.

---

# 8. Current obstruction anatomy

## 8.1 Raw simultaneous output overlaps

A complete deletion schedule emits recursive shells and terminal outputs that may be identical, nested, partially overlapping, terminal-recursive overlapping, or cyclically related. Summing occurrences double counts support and provenance.

## 8.2 Provenance cannot be discarded

Numerically identical states may carry different histories and future obligations. Distinct states may share large support. A valid quotient must identify what has already been paid for and prevent the same ancestor resource from being charged repeatedly.

## 8.3 Terminal-fiber incidence is cyclic

At `S_7`, the principal cyclic component is

```math
\{1,5,61,303,1597,8195,323640\},
```

with

```math
\frac{23}{9}<\rho(A)<\frac83.
```

No scalar decreasing rank or positive linear factor-two capacity can control its internal recycling.

## 8.4 Policy changes the transition

The schedule affects terminal mass, recursive occurrences, duplicates, residual error, SCC structure, canonical regeneration, and future obstruction structure. A final theorem may specify a constructive policy, prove a minimax policy exists, or dominate all policies with a stronger potential.

## 8.5 The retention theorem comes before the final LP

The exact LP harness accepts only legitimate retained-child rows. A valid retention contract must specify:

1. whether the potential is occurrence-, support-, state-, provenance-, or component-valued;
2. duplicate merging;
3. provenance multiplicity;
4. containment charging;
5. partial-overlap charging;
6. terminal-recursive overlap;
7. SCC representation;
8. internal recycling;
9. cross-generation matching of imported labels;
10. prevention of repeated payment;
11. controlled error for discarded mass;
12. completeness of the emitted child family.

Without this contract, an exactly feasible LP can encode the wrong inequality.

Primary reference:

- `docs/branching-reserve-lp.md`.

---

# 9. Current active theorem

The target is a policy-aware branching inequality

```math
\Delta(S)
+
\sum_{S'\in\mathrm{Child}_\pi(S)}
\left(
\mathrm{Pack}(S')+\Phi_{\rm obs}(S')
\right)
\le
\mathrm{Pack}(S)+\Phi_{\rm obs}(S)
+
\mathrm{controlled\ error}.
```

Here:

- `Delta(S)` is Bellman debt from cheap replication;
- `Child_pi(S)` is the complete retained simultaneous family under policy `pi`;
- `Pack` controls support and provenance reuse;
- `Phi_obs` stores demand-aware completion, rectangle, or related obstruction capacity;
- the error must be globally summable.

The theorem must survive duplicate states, containments, partial overlaps, cyclic incidence, policy-dependent regeneration, and cross-generation reuse. A one-state or one-path statement is insufficient.

---

# 10. Roadmap ranked by logical leverage

## Tier I: decisive

### I.1 Provenance-preserving retention quotient

Define a canonical or policy-dependent map from raw simultaneous output to retained children and prove:

- support completeness;
- no unaccounted recursive output;
- bounded or explicitly charged overlap;
- preservation of required provenance;
- prevention of repeated payment.

### I.2 First legitimate retained-child Bellman row

Construct one exact row, beginning with `S_1` or `S_2`, from the proved retention quotient. The children must come from mathematics, not from a fitted surrogate.

### I.3 State-independent branching Carleson inequality

Prove a general policy-aware inequality controlling all retained children. This is the central major theorem of the current architecture.

### I.4 Deduction to dyadic density summability

Show that the branching inequality telescopes with summable Roth error and yields

```math
\sum_j\alpha_j<\infty.
```

This would resolve the four-term reciprocal-sum case.

## Tier II: enabling

1. **Demand-aware obstruction recurrence:** normalize completion and rectangle coverage against the next target interval and prove its transition law.
2. **External-export theorem for high-growth SCCs:** show that internal recycling forces outgoing obstruction, terminal, or condensation capacity.
3. **Bounded provenance reuse:** prevent the same imported label, pair, rectangle, or completion witness from paying indefinitely.
4. **Multi-generation amortization:** use a stopping-time block inequality if one-step retention cannot contract.
5. **Finite-state or symbolic quotient:** compress policy-aware component/provenance states into a finite or spectrally controlled system.

## Tier III: diagnostic finite work

1. enlarge the candidate delayed-step universe around the current `S_7` winner `seed_5_142` with exact deterministic add/remove neighborhoods;
2. add every comparison to the rational LP and monitor the feasible cone;
3. extract the smallest exact infeasible subsystem whenever a potential fails;
4. prototype retention definitions on `S_1` and `S_2`;
5. track completion and rectangle export by provenance;
6. test nonlinear or component-valued capacities forced by the `S_7` spectral no-go theorem.

## Tier IV: low leverage

Do not prioritize these unless they test a precise general conjecture:

- extending one distinguished contaminated path;
- certifying another candidate prefix;
- adding isolated policy comparisons;
- enlarging policy families without monitoring theorem-level stability;
- improving constants that do not enter a telescoping inequality;
- counting more exact tails from the completed `S_10` fan;
- searching for another local contraction window;
- adding coordinates without an exact no-go subsystem requiring them.

---

# 11. Decision gates for future work

A new result should normally pass at least one gate.

## Gate A: generality

It applies to a class of states or transitions, not only one numerical state.

## Gate B: telescoping relevance

It enters a retained-child inequality, packing theorem, or globally summable error estimate.

## Gate C: structural compression

It replaces a large finite catalog by a symbolic classification, transport identity, recurrence, or automaton.

## Gate D: obstruction removal

It closes a named bottleneck or proves a proposed route impossible.

## Gate E: connection to the original problem

It closes a missing implication between recursive deletion and dyadic reciprocal-mass summability.

A finite computation passing none of these gates is exploratory evidence, not a priority theorem.

---

# 12. Dependency graph

```text
Dyadic reciprocal-sum reduction
    |
Coordinated deletion and backbone inequalities
    |
Exact middle multiplicity fibers
    |
Mandatory shell resolution
    |
Center / anchor / predecessor compression
    |
Aligned-diamond persistence obstruction
    |
Exact scale-eight benchmark and exact-model summability
    |
Contaminated cheap-debt counterexamples
    |
Bellman debt accounting
    |
Completion and rectangle repayment mechanisms
    |
Complete S10 cheap-extension closure
    |
Raw simultaneous transition semantics
    |
Policy dependence and cyclic-component analysis
    |
Provenance-preserving retention quotient          [OPEN]
    |
Legitimate retained-child Bellman rows            [OPEN]
    |
Policy-aware branching Carleson inequality        [OPEN]
    |
Whole-tree summability with controlled error      [OPEN]
    |
Four-term reciprocal-sum theorem                  [OPEN]
```

Major failed shortcuts are:

```text
Exact 3/4 contraction
    X contaminated factor-four burst

Fixed short-window recovery
    X path-dependent delayed release

Pathwise summability
    X simultaneous branching and overlap

Replay catalog as Bellman tree
    X replay choices are alternatives

Raw novelty reserve
    X schedule minimum zero

P Psi stored potential
    X wrong sign on S1 -> S2

Scalar terminal rank
    X terminal-fiber cycles

Unit SCC capacity
    X S7 internal excess

Positive linear factor-two SCC contraction
    X rho(A) > 23/9

Avoid regeneration at all costs
    X reverse-policy explosion

Greedy policy improvement
    X noncomposable delays

Finite policy LP feasibility
    X retained children undefined
```

---

# 13. Publication-value map

## 13.1 Exact construction and scale-barrier paper

A coherent focused paper can be built around:

- the infinite scale-eight aligned-diamond family;
- exact automaton/carry certification;
- persistence `P_h=(1/2)L_h^{1/3}`;
- the sharp `L' >= 8L` barrier;
- exact-model summability;
- contaminated counterexamples to naive local generalization.

## 13.2 Structural repayment and depth-ten closure paper

A second focused narrative can be built around:

- contaminated debt and delayed recovery;
- lifted completion support;
- complete direct rectangle support;
- four-ratio transport;
- complete `S_10` cheap-extension closure;
- the complete exact factor-eight fan.

Its broader significance increases if the transport mechanism can be stated for a state-independent class.

## 13.3 Future major paper

The major target is:

> A policy-aware retention and branching-packing theorem for the recursive deletion tree, yielding summability of four-AP-free dyadic density.

This result does not yet exist because the retention quotient and whole-tree inequality remain open.

---

# 14. Recommended immediate program

1. **Freeze state-specific `S_10` work.** Reopen it only to test a general reserve recurrence.
2. **Define retention on `S_1` and `S_2`.** Specify support ownership, provenance ownership, duplicate merging, containment, partial overlap, terminal-recursive overlap, and discarded mass.
3. **Export the first real Bellman row.** Use `src/branching_reserve_lp.py` only after the theorem determines the children.
4. **Add one structurally motivated coordinate at a time.** Candidate features include demand-aware completion deficit, rectangle deficit, outgoing SCC capacity, provenance reuse capacity, regeneration charge, and nonlinear internal capacity.
5. **Test one definition through `S_3,...,S_7`.** The objective is a stable theorem, not a fit at any cost.
6. **Stop or reformulate if the state dimension does not stabilize.** An indefinitely expanding feature list is evidence that the architecture is missing a deeper invariant.

---

# 15. Permanent stop list

Do not restart these routes without a materially new hypothesis that explicitly avoids the recorded obstruction:

1. ordinary Walker-style modular digit search;
2. blind stochastic periodic deletion/rebuild;
3. small substitutions around the base-55 benchmark;
4. a fixed finite-automaton counterexample;
5. density exponent or cardinality as the final objective;
6. recursive deletion without shell resolution;
7. bounded or polylogarithmic persistence;
8. universal one-step `3/4` contraction;
9. fixed four- or six-generation contraction;
10. universal two-generation recovery;
11. pathwise summability as a whole-tree proof;
12. replay siblings as simultaneous children;
13. density, shell slack, and raw contamination as a complete reserve;
14. rectangle radius without target demand;
15. raw novelty as schedule independent;
16. `P Psi` as a standalone stored potential;
17. raw occurrences copied directly into a Bellman child list;
18. exact-state quotienting as an overlap theorem;
19. a uniform overlap constant inferred from the recorded path;
20. a strict decreasing terminal-label rank;
21. latest- or full-separation-history-only state;
22. unit harmonic SCC capacity;
23. positive linear factor-two SCC contraction at `S_7`;
24. avoiding canonical regeneration as the sole policy objective;
25. occurrence cost without continuation charge;
26. greedy composition of favorable policy delays;
27. treating a five-step subset-lattice winner as globally optimal;
28. treating the tested five-step universe as exhaustive over all schedules;
29. treating policy-half-space feasibility as Bellman feasibility;
30. further direct `S_10` candidate-prefix certification;
31. the rejected depth-ten anchor reduction.

---

# 16. Maintenance protocol

Update this document only when the strategic landscape changes. A result belongs here if it:

- proves or disproves a general principle;
- opens or closes a model class;
- changes the dependency graph;
- changes the active theorem;
- creates a new permanent stop;
- replaces brute force by structural compression;
- changes publication readiness.

Routine finite certificates should update their dedicated note and `docs/certainty-ledger.md`, but not necessarily this overview.

Every strategic update should record:

1. exact statement;
2. status category;
3. hypotheses;
4. strongest consequence;
5. explicit non-consequence;
6. primary theorem note;
7. verifier and certificate, where applicable;
8. effect on the roadmap.

---

# 17. Current bottom line

The repository now contains a substantial body of exact mathematics:

- strong one-generation harmonic recursion;
- exact multiplicity resolution;
- sharp persistence benchmarks;
- an infinite automatic scale-eight family;
- a complete exact-model summability theorem;
- contaminated counterexamples to local contraction;
- exact Bellman debt accounting;
- complete structural closure of the depth-ten cheap-extension domain;
- a complete exact-tail fan;
- raw simultaneous transition semantics through `S_7`;
- exact cyclic-component and policy no-go theorems;
- a stable two-coordinate policy witness across a 250-constraint full five-step subset lattice through `S_7`.

The decisive open problem is not another candidate search, another selected path, or another finite policy ranking. It is

```math
\boxed{
\text{construct a provenance-preserving retained-child packing theorem}
}
```

and use it to prove a policy-aware branching Bellman or Carleson inequality.

That is the shortest currently credible route from the repository's positive results to a major theorem on the four-term reciprocal-sum problem.
