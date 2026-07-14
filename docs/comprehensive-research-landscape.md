# Comprehensive research landscape for the four-term case

## Status and scope

This document is the strategic map of the repository's work on the four-term-progression-free case of Erdős Problem #3.

The ambient problem is:

> If \(A\subseteq\mathbb N\) and \(\sum_{n\in A}1/n=\infty\), must \(A\) contain arbitrarily long arithmetic progressions?

The repository studies the first unresolved finite-length case relevant to this program: whether every four-term-progression-free set has convergent reciprocal sum.

The full problem and the four-term case remain open.

This overview records:

1. the positive theorem spine currently supporting the proof program;
2. the exact finite and infinite constructions used as benchmarks and obstructions;
3. the principal failed proof principles and the strongest no-go statement known for each;
4. the mathematical models already explored;
5. the precise distinction between completed state-specific results and the missing whole-tree theorem;
6. the current roadmap ranked by logical leverage.

It is **repository-comprehensive**, not literature-comprehensive. It summarizes the mathematical territory explored and certified here. Novelty relative to the full external literature must still be established independently before publication.

Authoritative claim status remains in:

- `docs/certainty-ledger.md`;
- `docs/current-proof-program.md`;
- the dedicated theorem note and verifier for each result.

Chronological decisions remain in:

- `docs/research-decision-history.md`.

This document is organized by mathematical dependency rather than chronology.

---

# 1. Executive map

The project has passed through four conceptually distinct stages.

## Stage A: construction and search

The repository first explored modular digit sets, periodic digit systems, pseudo-Boolean search, and finite automata. These routes produced exact certification infrastructure and useful extremal benchmarks, but not a divergent-reciprocal-sum four-AP-free construction.

The principal conclusion was negative:

\[
\text{fixed finite-state digit models are useful finite extremizers, not a route to a counterexample.}
\]

## Stage B: recursive deletion and persistence

Coordinated side-anchor deletion and the minimum-translation backbone produced strong one-generation harmonic inequalities. Exact multiplicity fibers, shell resolution, and anchor-history compression isolated the remaining obstruction: identical recursive histories can persist with polynomial multiplicity.

This led to an explicit infinite scale-eight aligned-diamond family with persistence

\[
P_h=2^h=\frac12L_h^{1/3}.
\]

The exact uncontaminated equal-translate model is sharply summable, but contaminated backbones defeat local contraction.

## Stage C: debt, recovery, and structural transport

A contaminated path with scale word

\[
4,8,4,4,8,4,8,8,8
\]

showed that cheap factor-four replication can produce substantial temporary growth and that recovery is path-dependent.

The Bellman debt identity quantified the accounting:

\[
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
\]

The recorded depth-ten state was then closed structurally:

\[
N_{10,2}=N_{10,4}=0.
\]

The factor-four theorem replaced hundreds of millions of candidate checks by inherited obstruction, lifted completion support, complete direct rectangle support, and a four-ratio transport identity.

## Stage D: policy-aware whole-tree packing

The project then moved from selected paths and replay catalogs to the actual simultaneous deletion output. This exposed duplicates, containments, partial overlaps, terminal-recursive overlap, cyclic terminal-fiber components, and schedule dependence.

The current target is no longer a pathwise contraction statement. It is a policy-aware retained-child inequality of the form

\[
\Delta(S)
+
\sum_{S'\in\operatorname{Child}_\pi(S)}
\left(
\operatorname{Pack}(S')+\Phi_{\mathrm{obs}}(S')
\right)
\le
\operatorname{Pack}(S)+\Phi_{\mathrm{obs}}(S)
+\operatorname{controlled\ error}.
\]

The missing mathematical object is a **provenance-preserving retention quotient** converting raw overlapping simultaneous output into legitimate Bellman children.

---

# 2. The logical target

Let

\[
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j}.
\]

Up to absolute constants,

\[
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
\]

Therefore the four-term problem can be approached by proving that the dyadic densities of every four-AP-free set are summable.

The recursive program starts from a four-AP-free dyadic block

\[
D\subseteq[N,2N)
\]

and produces lower-scale four-AP-free outputs. One generation gives more harmonic output than the parent, up to the Roth-error term \(r_3(N)/N\). The difficulty is to control repeated numerical labels and overlapping descendants across all generations.

The required implication is not merely:

\[
\sup_{\gamma}\sum_{S\in\gamma}W(S)<\infty
\]

over individual paths \(\gamma\). A pathwise theorem can coexist with exponentially many paths.

The required object is treewise: after defining which simultaneous outputs count as retained children and how overlaps are packed, one needs a telescoping inequality whose total error is summable.

A successful closing theorem must therefore provide all of the following:

1. a complete simultaneous child semantics;
2. a retention or packing rule;
3. preservation of provenance under quotienting;
4. a potential or capacity covering internal recycling and outgoing recursive load;
5. controlled treatment of discarded or unresolved mass;
6. a summable global error term;
7. a deduction from the recursive inequality back to \(\sum_j\alpha_j<\infty\).

Any result omitting one of these links is a partial theorem, not a proof of the four-term case.

---

# 3. Claim-status convention

The repository uses the following categories.

## Theorem

A symbolic statement proved from explicit definitions and lemmas.

## Exact finite theorem

A complete finite classification, usually with exact integer or rational arithmetic and a recorded certificate.

## Exact infinite theorem

An infinite statement reduced to finite certification plus a symbolic induction, recurrence, or automaton argument.

## No-go theorem

An exact counterexample, infeasible system, sign obstruction, spectral obstruction, or other proof that a proposed principle cannot hold in its stated form.

## Experimental evidence

Sampling, numerical ranking, heuristic search, or incomplete enumeration. Such evidence may motivate a theorem but is not used as one.

## Conjecture

A proposed general statement not yet proved.

## Superseded

A statement or route that was useful historically but has been replaced by a stronger result or invalidated by an exact counterexample.

The strongest current claims are indexed in `docs/certainty-ledger.md`.

---

# 4. Positive theorem spine

This section gives the shortest dependency chain from the dyadic reduction to the active whole-tree target.

## 4.1 Coordinated deletion and the minimum-translation backbone

Run coordinated side-anchor deletion on

\[
D\subseteq[N,2N)
\]

until the residual is three-term-progression-free. If \(s\) points remain, then

\[
s\le r_3(N).
\]

Writing \(K=|D|-s\), the minimum-translation backbone and selected middle fibers satisfy

\[
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N.
\]

After exact resolution of repeated middle steps,

\[
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
\]

These inequalities establish strong one-generation production. They do not by themselves control repeated labels or overlapping descendants.

Primary references:

- `docs/minimum-translation-backbone-recursion.md`;
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md`;
- `docs/side-anchor-deletion-dag.md`.

## 4.2 Mandatory shell resolution

Every lower-scale output must be resolved into standard dyadic shells. For a parent label \(a\), there are at most two retained outputs and each is at most \(a/2\). Hence, for every \(p\ge1\),

\[
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
\]

This gives logarithmic recursive depth and positive-moment control. It does not control reciprocal mass, where \(p=-1\).

Ignoring shell resolution is a permanent invalid route.

Primary reference:

- `docs/half-contraction-multiscale-label-potential.md`.

## 4.3 Center, anchor, predecessor, and antichain compression

Repeated terminal labels are progressively compressed by:

1. lifted-center difference layers;
2. root-anchor difference layers;
3. predecessor-anchor difference layers;
4. complete anchor-history antichain bounds.

For fixed complete anchor history,

\[
\lambda_{x,q}(t)(a-t)\le a.
\]

These reductions remove large classes of accidental multiplicity. The final unresolved residue consists of identical local progressions generated by state occurrences with the same complete anchor history.

Primary references:

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`.

## 4.4 Self-replicating aligned diamonds

The residual multiplicity can grow polynomially. The aligned-diamond recursion satisfies

\[
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
\]

so

\[
P_h\asymp |S_h|^{\log_3 2}.
\]

This disproves bounded, logarithmic, polylogarithmic, and sufficiently small subpower bounds on identical-history persistence without further hypotheses.

Primary references:

- `docs/self-replicating-aligned-diamond.md`;
- `src/verify_self_replicating_aligned_diamond_depth2.py`.

## 4.5 Exact scale-eight family

There is an explicit infinite four-AP-free family with

\[
L_h=8^{h+1},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
\]

A 34-state base-eight automaton and a 17,238-state product/carry search certify four-AP-freeness of the full infinite language.

This is an exact infinite theorem and a sharp benchmark for persistence.

Primary references:

- `docs/scale-eight-self-replicating-aligned-diamond.md`;
- `src/verify_scale_eight_aligned_diamond.py`.

## 4.6 Sharp exact equal-translate classification

In the uncontaminated equal-translate model, exact reproduction requires dyadic scale expansion at least \(8\):

\[
L'\ge8L.
\]

Three translate layers are maximal because four equal layers would contain

\[
0,R,2R,3R.
\]

Two persistent children are maximal because the genealogy is binary. Therefore the exact one-step efficiency is

\[
\rho_{\mathrm{exact}}=\frac{2\cdot3}{8}=\frac34.
\]

The exact model obeys

\[
P_h\alpha_h\le C_0\left(\frac34\right)^h
\]

and

\[
\sum_hP_h\alpha_h\le4C_0.
\]

Thus the exact model is completely summable and sharply classified.

Primary references:

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

## 4.7 Contaminated replication and Bellman debt

Exact reproduction is not the only way persistence continues. A relevant backbone shell may contain a replayable copy of the previous state plus extra points.

The certified contaminated chain begins with scale factors

\[
4,8,4,4
\]

and satisfies

\[
\frac{W_5}{W_1}=\frac{91}{32}>1.
\]

An extended branch has scale word

\[
4,8,4,4,8,4,8,8,8.
\]

The exact Bellman future-cost function for constant scale factor \(c>6\) is

\[
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right).
\]

At \(c=8\),

\[
\mathfrak B_8=\frac{4P(N+1)}L.
\]

The debt generated by a step of scale factor \(c\) is

\[
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
\]

Thus factors \(2\) and \(4\) create debt, factor \(8\) is neutral, and factors at least \(16\) create surplus.

This is exact accounting. It does not prove that geometric constraints force repayment.

Primary references:

- `docs/contaminated-backbone-depth-five-chain.md`;
- `docs/current-proof-program.md`;
- the depth-seven through depth-ten chain notes.

## 4.8 Complete depth-ten cheap-extension closure

For the recorded depth-ten state,

\[
N_{10,2}=N_{10,4}=0.
\]

The complete factor-four domain contains

\[
348{,}012{,}826
\]

layer-disjoint candidates. It is partitioned exactly into:

\[
33{,}026{,}376
+
137{,}142{,}200
+
177{,}844{,}250.
\]

The three classes are removed by:

1. inherited lower-interval obstruction from \(S_9\);
2. lifted depth-nine completion support;
3. complete direct rectangle support in \(B_9=\{0\}\cup S_9\) and four-ratio transport.

The direct rectangle-support theorem proves

\[
[1,76{,}583{,}776]\subseteq\mathcal R(B_9).
\]

If a base rectangle has effective separation \(U\), exact layer-word cancellation transports it through the next replication at precisely

\[
k=1,2,3,4,
\]

covering separations

\[
T=kR_9\pm U.
\]

The resulting four windows cover the complete residual interval. No cancellation channel exists for \(k\ge5\).

This is the strongest example in the repository of replacing enormous enumeration by a reusable structural mechanism.

Primary references:

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `docs/four-ratio-rectangle-transport-and-residual-profile.md`;
- `docs/three-translate-obstruction-coverage-recurrence.md`;
- `src/run_verify_s10_factor4_rectangle_closure.sh`.

## 4.9 Complete exact factor-eight fan from \(S_{10}\)

Every valid positive exact factor-eight child of \(S_{10}\) has an explicit infinite exact four-AP-free continuation. The complete fan contains

\[
408{,}855{,}759
\]

valid children.

Most follow the standard offset recurrence. The remaining scheduled failures are repaired by a single \(+1\) perturbation at the second or third step. Every tail has total charge

\[
\sum_{n\ge0}W_{10+n}
=
\frac{33215}{16384}.
\]

This completely classifies the exact factor-eight future from one recorded state. It does not control arbitrary contaminated descendants.

Primary reference:

- `docs/complete-exact-child-tail-fan.md`.

## 4.10 Raw simultaneous transition export

The project now exports complete raw output for a fixed deletion policy through \(S_7\). The data include:

- every occurrence;
- exact numerical state classes;
- provenance;
- duplicate classes;
- containments;
- partial overlaps;
- terminal-recursive overlap;
- terminal-fiber incidence;
- exact harmonic ledgers.

The frontier is:

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| \(S_1\) | 5 | 4 | 1 | 1 | 0 |
| \(S_2\) | 11 | 10 | 1 | 3 | 5 |
| \(S_3\) | 25 | 21 | 3 | 23 | 15 |
| \(S_4\) | 46 | 34 | 7 | 91 | 35 |
| \(S_5\) | 68 | 51 | 11 | 145 | 88 |
| \(S_6\) | 94 | 71 | 15 | 209 | 150 |
| \(S_7\) | 127 | 95 | 20 | 345 | 214 |

These are raw simultaneous occurrences, not retained Bellman children.

Primary references:

- `docs/simultaneous-deletion-transition-exporter.md`;
- `docs/simultaneous-transition-frontier-s5.md`;
- `docs/simultaneous-transition-frontier-s7.md`;
- `src/export_simultaneous_deletion_transition.py`.

## 4.11 Policy-aware finite cone

Deletion policy changes novelty, duplication, cyclic load, and long-range regeneration.

A finite policy score has been developed:

\[
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
\]

where:

- \(T_\pi\) is terminal mass;
- \(O_\pi\) is recursive occurrence/provenance load;
- \(E_\pi\) is residual error;
- \(G_\pi\) is known regenerative continuation charge.

After exhaustive expansion over all 32 subsets of delayed actions

\[
\{5,40,30,161,142\}
\]

on \(S_1,\ldots,S_6\), the exact rational half-space system contains 198 constraints. The witness

\[
(\lambda,\gamma)=\left(3,\frac1{10}\right)
\]

remains feasible.

This is a finite policy-ranking theorem. It is not yet a branching Bellman theorem because the retained simultaneous children are undefined.

Primary references:

- `docs/policy-occurrence-cone-s1-s7.md`;
- `docs/two-coordinate-policy-family.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/expanded-policy-subset-lp.md`.

---

# 5. Model-space map

The repository has explored several mathematically distinct model classes. They should not be conflated.

| Model | What is controlled | Status | Main lesson |
|---|---|---|---|
| One-layer modular digit sets | fixed-base digit restriction | explored and benchmarked | ordinary Walker-style search is not the active proof route |
| Periodic digit systems | finite-period digit rules | exact small-base and stochastic searches | no improvement from naive periodic extension |
| Pseudo-Boolean/MaxSAT search | finite modular templates | infrastructure complete | solver output requires exact recertification and true harmonic scoring |
| Fixed finite automata | regular digit languages | exact 4-AP certifier and growth tools | useful finite extremizers; fixed automata cannot yield the desired sparse divergent counterexample |
| One-generation deletion recursion | one parent block and its outputs | strong exact inequalities | creates harmonic gain but not global packing |
| Exact equal-translate replication | uncontaminated recursive state | sharply classified | scale 8 is minimal and weighted density is summable |
| Contaminated selected paths | one replayable branch | extensive exact constructions | local contraction and bounded-window recovery fail |
| State-specific obstruction closure | one recorded state | closed through \(S_{10}\) | completion and rectangle structure can repay cheap debt completely |
| Replay catalogs | alternative outer separations | exact finite catalogs | alternatives are not simultaneous children |
| Raw simultaneous deletion output | one complete deletion schedule | exported through \(S_7\) | duplication, containment, partial overlap, cycles, and provenance are essential |
| Policy optimization | finite family of deletion schedules | active exact LP ranking | a stable surrogate exists, but selected policies change under family enlargement |
| Retained-child packing | true Bellman children | open | decisive missing theorem |

The active route is the final row. Earlier models remain benchmarks, counterexamples, or infrastructure.

---

# 6. Negative theorem catalogue

The following failures materially constrain any future proof. They are mathematical progress and should not be discarded.

## 6.1 Ordinary modular and periodic search does not supply the needed result

### Proposed principle

Improve known lower constructions by ordinary modular digit search, periodic digit systems, or local substitutions near a strong benchmark.

### Why it was plausible

Digit restrictions naturally produce progression-free sets and permit exact automaton certification.

### What was found

Exact period-two searches, stochastic period-two/period-three searches, and local substitutions did not improve the relevant benchmark. A pseudo-Boolean pipeline was built, but no structural breakthrough emerged from the tested one-layer templates.

### Consequence

Do not restart ordinary modular or small-period search without a genuinely new model class or theorem target.

Primary references:

- early PR notes;
- `docs/research-decision-history.md`.

## 6.2 A fixed finite automaton is not a counterexample route

### Proposed principle

Search for a fixed regular digit language that is four-AP-free and has divergent reciprocal sum.

### Obstruction

A fixed finite automaton with enough growth for divergent reciprocal mass would have growth exponent forcing positive upper density, which is incompatible with long-progression avoidance.

### What remains useful

Finite automata remain effective for:

- exact 4-AP certification;
- finite extremizers;
- automatic infinite benchmark families;
- carry-state analysis.

### Consequence

Use automata as certifiers or finite-state quotients, not as a direct sparse counterexample ansatz.

## 6.3 Bounded or polylogarithmic persistence is false

### Proposed principle

Identical recursive histories occur only boundedly or polylogarithmically many times.

### Counterexample

The aligned-diamond family has

\[
P_h=2^h
\]

and

\[
|S_h|\asymp3^h,
\]

so

\[
P_h\asymp|S_h|^{\log_3 2}.
\]

### Consequence

Any global theorem must be density-sensitive. Cardinality-only multiplicity bounds below exponent \(\log_3 2\) are false.

## 6.4 Universal one-step \(3/4\) contraction is false

### Proposed principle

The exact-model efficiency

\[
\frac34
\]

continues to hold for contaminated backbones.

### Counterexample

The depth-five chain with factors

\[
4,8,4,4
\]

has

\[
W_5/W_1=91/32>1.
\]

### Consequence

The exact barrier theorem cannot be applied to mere containment of a replayable state. The proof must allow cheap debt and delayed repayment.

## 6.5 Fixed short-window contraction is false

### Proposed principles

Every four-generation or six-generation window contracts, or exact recovery forces contraction within two generations.

### Counterexamples

The contaminated chain disproves four-step contraction. The extended branch through \(S_7\) disproves universal two-generation recovery and six-step contraction.

### Consequence

No fixed short-memory scale-word rule is currently justified. The state must record structural debt, not only recent scale factors.

## 6.6 Pathwise recovery is not a whole-tree theorem

### Proposed principle

If every selected continuation path has finite total charge, the full recursion is controlled.

### Obstruction

The deletion process generates simultaneous overlapping outputs. Exponentially many individually summable paths can have divergent total mass.

### Consequence

The proof must define retained simultaneous children and a treewise packing inequality.

## 6.7 Replay siblings are not simultaneous Bellman children

### Proposed principle

Put every outer replay option into one Bellman child list.

### Obstruction

Replay siblings are alternative choices of outer separation, not outputs generated together by one deletion schedule.

### Consequence

A Bellman row may contain only outputs that coexist under the same complete schedule and retention rule.

Primary reference:

- `docs/replay-transition-catalog.md`.

## 6.8 Raw novelty is not schedule independent

### Proposed principle

Novel fiber support is an intrinsic parent quantity.

### Counterexample

At \(S_2\), one valid complete schedule has positive novelty and another has zero novelty.

### Consequence

Any schedule-dependent feature requires an explicit policy or a minimax statement.

Primary references:

- `docs/s2-novel-fiber-reference.md`;
- `docs/s2-zero-novelty-schedule.md`.

## 6.9 Density, shell slack, and raw contamination are not a complete reserve

### Proposed principle

A low-dimensional potential based only on weighted density, right-shell slack, and imported contamination pays every cheap transition.

### Counterexample

The recorded \(S_6\to S_7\) transition violates the naive reserve cone.

### Consequence

The reserve must include additional structural information such as provenance, obstruction coverage, cyclic capacity, regeneration, or multi-generation amortization.

Primary reference:

- `docs/naive-reserve-coordinate-no-go.md`.

## 6.10 Rectangle radius without target demand is insufficient

### Proposed principle

A large interval of rectangle support alone measures repayment capacity.

### Obstruction

Only the intersection of support with the actual target interval matters. At \(S_{10}\), the exact closure margin is 5, far smaller than the coarse overlap excess.

### Consequence

The target interval is part of the reserve state. Support must be demand-aware.

Primary reference:

- `docs/transport-interval-capacity.md`.

## 6.11 \(P\Psi(S)\) is not a standalone Bellman potential

### Proposed principle

The schedule-independent forced-fork output

\[
F(S)=P\Psi(S)
\]

stores enough value to pay cheap debt.

### Counterexample

On \(S_1\to S_2\),

\[
F(S_1)-F(S_2)<0
\]

while the factor-four debt is positive:

\[
D(S_1)=\frac54.
\]

No nonnegative scalar multiple of \(F\) can satisfy a standalone telescoping inequality.

### What remains valid

Forced-fork output is genuine unavoidable structure and may feed a packing, obstruction-growth, or transition-credit theorem.

Primary references:

- `docs/forced-fork-reserve-s1-s7.md`;
- `docs/forced-fork-bellman-no-go.md`.

## 6.12 Exact-state quotienting is not an overlap theorem

### Proposed principle

Merge numerically identical states and sum the distinct classes.

### Obstruction

Raw outputs also exhibit strict containment, partial overlap, and terminal-recursive overlap. Exact equality does not resolve shared support or repeated provenance.

### Consequence

Retention must operate on a richer state carrying provenance and overlap relations.

## 6.13 A uniform local multiplicity constant is not justified

### Proposed principle

Use the maximum pointwise multiplicity observed on the recorded branch as a global packing constant.

### Obstruction

Maximum local multiplicity grows through the tested states:

\[
2,3,7,11,12,13,16.
\]

The harmonic-average multiplicity is smaller, but cross-generation reuse remains uncontrolled.

### Consequence

A valid packing theorem must prevent repeated payment by the same provenance across generations; one-generation multiplicity statistics are insufficient.

Primary reference:

- `docs/recursive-occurrence-multiplicity.md`.

## 6.14 Strict decreasing terminal-label rank is false

### Proposed principle

Orient every recursive terminal-fiber edge by a strictly decreasing numerical rank.

### Counterexample

The terminal-fiber incidence graph contains

\[
61\longleftrightarrow303
\]

at \(S_3\), and a seven-label cyclic component at \(S_7\).

### Consequence

The natural finite object is an SCC quotient, not a scalar decreasing label rank.

Primary reference:

- `docs/terminal-fiber-incidence-graph.md`.

## 6.15 Latest- or complete-separation-history state is insufficient

### Proposed principle

Classify recursive outputs only by recent or complete historical outer separations.

### Counterexample

At \(S_7\), terminal-recursive overlap contains labels not captured by that history-only description, including \(5\), \(49158\), and \(323640\).

### Consequence

State must include provenance or component structure beyond outer-separation history.

## 6.16 Unit harmonic SCC capacity fails

### Proposed principle

For each terminal-fiber SCC \(C\), use harmonic vertex mass

\[
V(C)=\sum_{u\in C}\frac1u
\]

as its complete internal capacity.

### Counterexample

At \(S_7\),

\[
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0,
\]

where \(T(C)\) is internal target mass.

### Consequence

Internal recycling exceeds unit harmonic capacity. External export, nonlinear capacity, or amortization is necessary.

Primary reference:

- `docs/terminal-fiber-scc-quotient.md`.

## 6.17 Positive linear SCC contraction by factor two is impossible

### Proposed principle

Find positive weights \(w\) with

\[
Aw\le2w
\]

for the internal adjacency matrix of the \(S_7\) cyclic component.

### No-go theorem

The exact Collatz-Wielandt witnesses give

\[
\frac{23}{9}<\rho(A)<\frac83.
\]

Since \(23/9>2\), no positive linear internal capacity can be nonexpanding or factor-two contractive.

### Consequence

The proof must use one or more of:

- external obstruction export;
- nonlinear capacity;
- multi-generation amortization;
- policy avoidance or controlled regeneration;
- a larger state space.

Primary reference:

- `docs/terminal-fiber-scc-spectral-growth.md`.

## 6.18 Avoiding canonical regeneration is not a sufficient policy

### Proposed principle

Choose a deletion schedule that avoids the isolated child

\[
\{16,21,26\}
\]

which regenerates \(S_1\).

### Counterexample

Reverse lexicographic deletion avoids the return but creates more than 75 times the lexicographic middle-fiber occurrence mass, more than 744 times the duplicate mass, thousands of terminal steps and shells, and a much larger SCC.

### Consequence

Policy optimization must balance immediate output, duplication, residual error, cyclic load, and future regeneration.

Primary reference:

- `docs/s7-regenerative-seed-policy-dependence.md`.

## 6.19 Occurrence cost alone is insufficient

### Proposed principle

Rank policies only by

\[
C_\lambda=T+\lambda O+E.
\]

### Counterexample

The uniform step-5-delayed policy improves the score through \(S_7\) but retains the canonical regenerative return.

### Consequence

Continuation-sensitive coordinates are necessary. The current finite score adds \(G_{\mathrm{regen}}\).

Primary reference:

- `docs/step5-policy-regeneration-weight.md`.

## 6.20 Favorable local policy changes are not greedily composable

### Proposed principle

If delaying action \(a\) improves the score and delaying action \(b\) improves the score, then delaying both improves it further.

### Counterexample

Delaying step 30 alone improves \(C_3\) on \(S_2,\ldots,S_7\), but adding the same delay after steps 5 and 40 worsens \(C_3\) on every one of those states.

### Consequence

Policy search has genuine interaction terms. Greedy local improvement is invalid.

Primary reference:

- `docs/two-coordinate-policy-family.md`.

## 6.21 Policy-ranking feasibility is not Bellman feasibility

### Proposed principle

A common weight vector selecting favorable policies across finite states proves a whole-tree potential.

### Obstruction

The policy LP compares schedules using surrogate coordinates. It does not define the retained simultaneous children, resolve overlaps, or prove a telescoping inequality.

### Consequence

The current 198-half-space feasibility theorem is diagnostic infrastructure. It becomes proof-relevant only after a retention contract exports legitimate Bellman rows.

Primary references:

- `docs/policy-halfspace-lp.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/branching-reserve-lp.md`.

## 6.22 Finite policy optima are not stable under family enlargement

### Proposed principle

The best policy in a small tested family is structurally canonical.

### Counterexample

After subset-lattice expansion, the unique \(S_3\) optimum changed from delaying \(\{5,40\}\) to delaying

\[
\{5,161,142\}.
\]

### Consequence

Do not promote a finite-family winner to a theorem. Monitor the feasible cone and the structural coordinates, not only the selected policy.

## 6.23 The rejected depth-ten anchor reduction is invalid

### Proposed principle

A proposed anchor-based reduction eliminates the entire \(S_{10}\) factor-four domain.

### Audit result

The reduction had an uncovered logical gap and was explicitly withdrawn.

### Replacement

The valid theorem uses:

- inherited lower-interval obstruction;
- lifted completion support;
- direct rectangle support;
- four-ratio transport;
- explicit terminal witnesses.

### Consequence

The complete \(S_{10}\) result is sound only through the replacement proof architecture.

---

# 7. The depth-ten case as a model for future progress

The \(S_{10}\) theorem is strategically important not because it closes one large finite state, but because it illustrates the desired research pattern.

## 7.1 The unproductive formulation

The initial formulation was:

> Check hundreds of millions of candidate separations and find one four-AP witness for each.

That is finite but mathematically low leverage.

## 7.2 The structural reformulation

The domain was partitioned by inherited and lifted structure.

First, an embedded copy of \(S_9\) excludes the lower interval.

Second, depth-nine completion coordinates lift through the three-copy geometry and remove a large class of new candidates.

Third, the remaining candidates are represented as

\[
T=kR_9\pm U,
\qquad
1\le k\le4,
\]

where \(U\) lies in the complete direct rectangle-support interval of \(B_9\).

The four-ratio cancellation theorem then eliminates the residual interval.

## 7.3 General lesson

The reusable mechanism is:

\[
\text{cheap replication}
\longrightarrow
\text{inherited completion and rectangle structure}
\longrightarrow
\text{coverage of future cheap-separation demand}.
\]

This is a concrete realization of debt repayment.

A future general theorem should identify a normalized reserve measuring not merely the amount of completion or rectangle support, but its coverage of the next admissible target interval.

## 7.4 Limitation

The theorem is state-specific. It does not prove that every contaminated state eventually develops complete support or enters an \(S_{10}\)-type basin.

The open problem is to derive a recurrence, packing principle, or finite-state quotient that makes this repayment mechanism uniform across the retained branching tree.

---

# 8. Current obstruction anatomy

The active obstruction is no longer poorly understood multiplicity. It has a specific architecture.

## 8.1 Simultaneous output is overlapping

A complete deletion schedule produces multiple recursive shells and terminal outputs at once. Their supports may be:

- identical;
- strictly contained;
- partially overlapping;
- terminal-recursive overlapping;
- internally cyclic through terminal-fiber incidence.

Summing raw occurrences double counts support and provenance.

## 8.2 Provenance cannot be discarded

Two numerically identical states may represent different histories and future obligations. Conversely, distinct states may share large portions of their support.

A quotient must know what resource has already been paid for and prevent the same ancestor mass from being charged repeatedly across generations.

## 8.3 Terminal-fiber incidence is cyclic

The SCC structure prevents a scalar descending-rank proof. Internal linear growth can exceed factor two. Therefore a retained state likely needs component-level capacity plus external export.

## 8.4 Policy changes the transition

The deletion schedule affects:

- terminal mass;
- recursive occurrences;
- duplicate load;
- partial overlap;
- SCC structure;
- residual error;
- canonical regeneration;
- future obstruction structure.

A valid theorem may be:

1. constructive: specify one admissible policy;
2. minimax: show some policy always satisfies the inequality;
3. potential-based: dominate all policies;
4. dynamic: choose policy from a finite or compact state.

The current evidence favors an explicit policy-aware or minimax formulation.

## 8.5 Local output can be expansive

The \(S_7\) cyclic component has internal spectral radius greater than \(23/9\) and emits thousands of novel labels. Local recursive output is not itself repayment.

The missing credit must come from:

- obstruction coverage generated downstream;
- outgoing component capacity;
- terminal mass;
- eventual scale expansion;
- limited provenance reuse;
- or a nonlinear/multi-generation reserve.

## 8.6 The retention theorem is prior to the final LP

The LP harness is intentionally exact, but it accepts only legitimate retained-child rows. It cannot determine the retention rule.

A valid retention contract must specify:

1. the type of potential: occurrence-, support-, state-, provenance-, or component-valued;
2. duplicate merging;
3. preservation of provenance multiplicity;
4. containment charging;
5. partial-overlap charging;
6. terminal-recursive overlap;
7. SCC representation;
8. internal recycling;
9. cross-generation matching of imported labels;
10. prevention of repeated payment;
11. controlled error for discarded mass;
12. completeness of the emitted child family.

Without this contract, an exactly feasible LP may encode the wrong theorem.

Primary reference:

- `docs/branching-reserve-lp.md`.

---

# 9. Current active theorem

The desired inequality is schematically

\[
\Delta(S)
+
\sum_{S'\in\operatorname{Child}_\pi(S)}
\left(
\operatorname{Pack}(S')+
\Phi_{\mathrm{obs}}(S')
\right)
\le
\operatorname{Pack}(S)+
\Phi_{\mathrm{obs}}(S)+
\operatorname{controlled\ error}.
\]

Here:

- \(\Delta(S)\) is the Bellman debt created by cheap replication;
- \(\operatorname{Child}_\pi(S)\) is the complete retained simultaneous family under policy \(\pi\);
- \(\operatorname{Pack}\) controls support and provenance reuse;
- \(\Phi_{\mathrm{obs}}\) stores obstruction-export capacity, such as completion or rectangle coverage;
- the error must be globally summable.

The theorem must survive:

- duplicate states;
- strict containments;
- partial overlaps;
- cyclic terminal-fiber incidence;
- policy-dependent regeneration;
- cross-generation reuse.

A one-state or one-path inequality is not sufficient.

---

# 10. Candidate theorem hierarchy

Open targets should be ranked by logical value rather than ease of computation.

## Tier I: decisive theorems

### I.1 Provenance-preserving retention quotient

Define a canonical or policy-dependent map from the raw simultaneous payload to retained children and prove:

- support completeness;
- no unaccounted recursive output;
- bounded or explicitly charged overlap;
- preservation of necessary provenance;
- prevention of repeated payment.

This is the immediate decisive target.

### I.2 First legitimate retained-child Bellman row

Construct and verify one exact row, preferably first for \(S_1\) or \(S_2\), using the proved retention quotient.

The row must be mathematical, not merely a fitted score comparison.

### I.3 General policy-aware branching Carleson inequality

Prove a state-independent inequality controlling all retained children. This would be the central major theorem of the current architecture.

### I.4 Global deduction to dyadic density summability

Show that the branching inequality telescopes with summable Roth error and yields

\[
\sum_j\alpha_j<\infty.
\]

This would resolve the four-term reciprocal-sum case.

## Tier II: enabling theorems

### II.1 Demand-aware obstruction reserve recurrence

Define normalized completion and rectangle-support reserves and prove how they transform under replication and shell resolution.

The reserve must measure coverage of the next target interval, not raw support size alone.

### II.2 External export theorem for high-growth SCCs

Show that internal SCC growth forces sufficient outgoing obstruction, terminal, or condensation-component capacity.

This is a likely route around the spectral no-go theorem.

### II.3 Bounded provenance reuse

Prove that the same imported label, ancestor pair, rectangle, or completion witness cannot be used to pay arbitrarily many later transitions.

### II.4 Multi-generation amortization

If one-step retention is impossible, prove a block inequality over a variable stopping time determined by regeneration or obstruction thresholds.

### II.5 Finite-state or symbolic quotient

Compress the relevant policy-aware component/provenance state into a finite or spectrally controlled system.

## Tier III: diagnostic finite work

These computations are useful only when tied to a proposed theorem.

### III.1 Expand the \(S_7\) policy family

Use exact or certifiable search to test whether the two-coordinate feasible cone survives.

### III.2 Extract minimal infeasible subsystems

When a candidate potential fails, record the smallest exact transition set proving failure. Use it to identify a missing coordinate.

### III.3 Prototype retention on \(S_1\) and \(S_2\)

Small states are the correct laboratory for definitions of duplicate, containment, and partial-overlap charging.

### III.4 Track obstruction export by provenance

Measure which parent pairs, differences, completions, and rectangles produce future coverage.

### III.5 Test nonlinear or component-valued capacities

The \(S_7\) spectral obstruction rules out overly simple positive linear internal capacities.

## Tier IV: low-leverage work

Do not prioritize the following unless they test a precise general conjecture:

- extending one distinguished contaminated path;
- certifying another finite prefix of candidate separations;
- adding isolated policy comparisons;
- increasing policy-family size without monitoring theorem-level stability;
- improving constants that do not enter a telescoping inequality;
- counting more exact tails from already classified \(S_{10}\);
- searching for a new local contraction window;
- adding state coordinates without an exact no-go subsystem requiring them.

---

# 11. Decision gates for future work

A new result should normally satisfy at least one of the following.

## Gate A: generality

It applies to an entire class of states or transitions, not only one numerical state.

## Gate B: telescoping relevance

It enters a retained-child inequality, a packing theorem, or a globally summable error estimate.

## Gate C: structural compression

It replaces a large finite catalog by a finite symbolic classification, transport identity, recurrence, or automaton.

## Gate D: obstruction removal

It eliminates a specific open bottleneck or proves a proposed route impossible.

## Gate E: connection to the root problem

It closes a missing implication between the deletion recursion and dyadic reciprocal-mass summability.

A finite computation failing all five gates should be treated as exploratory evidence, not as a priority result.

---

# 12. Dependency graph

The positive dependency spine is:

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
Exact scale-eight benchmark and sharp exact-model theorem
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
    X depth-seven path dependence

Pathwise summability
    X simultaneous branching and overlap

Replay catalog as Bellman tree
    X replay siblings are alternatives

Raw novelty reserve
    X schedule minimum zero

P Psi stored potential
    X wrong sign on S1 -> S2

Scalar terminal rank
    X terminal-fiber cycles

Unit SCC harmonic capacity
    X S7 internal excess

Positive linear factor-two SCC contraction
    X rho(A) > 23/9

Avoid regeneration at all costs
    X reverse-policy explosion

Greedy policy improvement
    X noncomposable delays

Policy half-space feasibility
    X retained children undefined
```

---

# 13. Publication-value map

The repository now contains at least two distinct paper-level narratives.

## 13.1 Exact construction and scale-barrier paper

Core results:

- infinite scale-eight aligned-diamond family;
- exact automaton/carry certification;
- persistence \(P_h=\frac12L_h^{1/3}\);
- sharp \(L'\ge8L\) exact barrier;
- summability of the exact equal-translate model;
- contaminated counterexamples to naive local generalization.

This is a coherent focused contribution independent of the unresolved whole-tree theorem.

## 13.2 Structural repayment and depth-ten closure paper

Core results:

- contaminated debt and delayed recovery;
- exact completion-support lifting;
- direct rectangle-support theorem;
- four-ratio transport;
- complete \(S_{10}\) factor-two/factor-four closure;
- complete exact factor-eight fan.

Its broader significance depends on how much of the transport mechanism can be stated state-independently.

## 13.3 Future major paper

The major target would be:

> A policy-aware retention and branching-packing theorem for the recursive deletion tree, yielding summability of four-AP-free dyadic density.

This paper does not yet exist because the retention quotient and whole-tree inequality remain open.

---

# 14. Recommended immediate program

The recommended order is:

## Step 1: freeze state-specific \(S_{10}\) work

Treat \(N_{10,2}=N_{10,4}=0\) and the exact fan as completed. Reopen only to test a general reserve recurrence.

## Step 2: define the retention object on the smallest nontrivial states

Start with \(S_1\) and \(S_2\). Give exact definitions for:

- support ownership;
- provenance ownership;
- duplicate merging;
- containment;
- partial overlap;
- terminal-recursive overlap;
- discarded mass.

The definition should emit a finite retained family and a proof of completeness.

## Step 3: export the first real Bellman row

Use `src/branching_reserve_lp.py` only after the retention theorem determines the children.

If the current feature set fails, extract the exact minimal infeasible subsystem.

## Step 4: add one structurally motivated coordinate at a time

Candidate coordinates include:

- demand-aware completion deficit;
- demand-aware rectangle deficit;
- outgoing SCC capacity;
- imported-provenance reuse capacity;
- regeneration charge;
- nonlinear internal component capacity.

No coordinate should be added solely because it improves a finite fit.

## Step 5: test on \(S_3\) through \(S_7\)

The goal is not to fit all states at any cost. It is to determine whether one state-independent retention and reserve theorem survives increasing complexity.

## Step 6: prove a general inequality or stop

If the feature dimension grows without stabilization or the retention rule becomes state-specific, treat that as evidence that the architecture needs a deeper reformulation.

---

# 15. Permanent stop list

Do not restart the following without a materially new hypothesis that explicitly avoids the recorded obstruction.

1. ordinary Walker-style modular digit search;
2. blind stochastic periodic deletion/rebuild;
3. small substitutions around the base-55 benchmark;
4. a fixed finite-automaton counterexample;
5. density exponent or cardinality as the final objective;
6. recursive deletion without shell resolution;
7. bounded or polylogarithmic identical-history persistence;
8. a universal one-step \(3/4\) contraction theorem;
9. fixed four- or six-generation contraction;
10. universal two-generation recovery;
11. pathwise summability as a whole-tree proof;
12. replay siblings as simultaneous children;
13. density, shell slack, and raw contamination as a complete reserve;
14. rectangle radius without target demand;
15. raw novelty as a schedule-independent quantity;
16. \(P\Psi\) as a standalone stored Bellman potential;
17. raw occurrences copied directly into a Bellman child list;
18. exact-state quotienting as an overlap theorem;
19. a uniform maximum-overlap constant inferred from the recorded path;
20. a strict decreasing terminal-label rank;
21. latest- or complete-separation-history-only state;
22. unit harmonic SCC capacity;
23. positive linear SCC contraction by factor two at \(S_7\);
24. avoiding canonical regeneration as the sole policy objective;
25. occurrence cost without continuation charge;
26. greedy composition of locally favorable policy delays;
27. treating a finite-family policy winner as globally optimal;
28. treating policy-half-space feasibility as Bellman feasibility;
29. further direct \(S_{10}\) candidate-prefix certification;
30. the rejected depth-ten anchor reduction.

---

# 16. Maintenance protocol

Update this document only when the strategic landscape changes.

A result belongs here if it:

- proves or disproves a general principle;
- opens or closes a model class;
- changes the dependency graph;
- changes the active theorem;
- creates a new permanent stop;
- replaces brute force by structural compression;
- changes publication readiness.

Routine finite certificates should update their dedicated note and `docs/certainty-ledger.md`, but not necessarily this overview.

Every strategic update should preserve:

1. exact statement;
2. status category;
3. hypotheses;
4. strongest consequence;
5. explicit non-consequence;
6. primary theorem note;
7. verifier and certificate where applicable;
8. effect on the roadmap.

---

# 17. Current bottom line

The repository has established a substantial body of exact mathematics:

- strong one-generation harmonic recursion;
- exact multiplicity resolution;
- sharp persistence benchmarks;
- an infinite automatic scale-eight family;
- a complete exact-model summability theorem;
- contaminated counterexamples to local contraction;
- exact Bellman debt accounting;
- a complete structural closure of the depth-ten cheap-extension domain;
- a complete exact-tail fan;
- raw simultaneous transition semantics through \(S_7\);
- exact cyclic-component and policy no-go theorems;
- a stable finite two-coordinate policy cone under substantial family expansion.

The project has also sharply isolated the missing theorem.

The decisive open problem is not another candidate search, another selected path, or another policy ranking. It is:

\[
\boxed{
\text{construct a provenance-preserving retained-child packing theorem}
}
\]

and use it to prove a policy-aware branching Bellman or Carleson inequality.

That is the shortest currently credible route from the repository's positive results to a major theorem on the four-term reciprocal-sum problem.
