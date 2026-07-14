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

### Backbone-anchor refinement

The exact source classification of the first failing transition is now complete. All `1015` recursively surviving roots continue through minimum-translation backbone occurrences; no middle-fiber root survives. The twelve minimum-anchor roots are exactly the twelve roots with no raw descendant output.

For each parent state `S`, `m=min(S)`, the full prospective translation gain is

```math
A(S)
=
\sum_{u>m}
\left(
\frac1{u-m}-\frac1u
\right).
```

Across the twelve parents,

```text
full translation reserve = 9.928706884742...
retained survivor gain    = 1.816777911848...
minimum-anchor release    = 0.364729899662...
```

Six parent states expand and six contract. Classes `77`, `68`, and `24` carry `87.7945%`–`87.7946%` of survivor gain. The correct local object is therefore a provenance-labeled anchor-survivor interval, not scalar minimum-anchor mass.

### Affine pivot pair-energy theorem

For an affine root state `S_r(P)={p-r:p in P}`, minimum translation at `a=min(P)` changes the common root reference from `r` to `a`. For pairwise root-disjoint children `S_a(Q_i)`, define

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

Exact pair bookkeeping gives

```math
\sum_i
\left(
H(S_a(Q_i))+J(Q_i)
\right)
\le
J(P).
```

Therefore every root pair is used at most once in an affine pivot forest. Cross-generation reuse is not the unresolved issue inside this model. The unresolved issues are entry into the affine regime and payment for the entering pair energy.

### Affine pair-token interpretation

In an affine state, `(u,p)` determines reference root `r=p-u` and therefore identifies one root pair `(r,p)` of weight `1/u`. First-appearance coarse-token mass is a sub-sum of entering pair energy. A recurrence of `(u,p)` is exact reuse of the same pair resource, not merely an inadequate signature.

Immediate provenance may distinguish histories, but it cannot manufacture another copy of root-pair capacity. Pair-resource accounting should therefore merge repeated `(u,p)` tokens and track the excess as pair-reuse mass.

### Exact fifth-frontier pair-energy row

The pair-energy potential was tested on the first previously failing retained transition. Every fourth and fifth recursive state is affine, every root and pair has multiplicity one, and

```math
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4^{\rm rec})
```

with ratio `0.578188259610...` and surplus `1157.391621834512...`.

This is the first exact retained-child Bellman row with a state-independent symbolic potential and no fitted coefficient. The fourth-to-fifth expansion is closed. The unresolved frontier moves to earlier generations, where root and pair reuse may still occur and affine coverage has not yet been certified.

### Pair-resource ownership certification

The fifth pair-energy row was strengthened from a numerical inequality to an exact token partition. All `107413` fifth current and latent resources are distinct members of the fourth latent pair universe. None uses a fourth current pair, and `264809` fourth resources remain unused.

The recorded transition therefore satisfies an exact set-valued conservation identity, not only a scalar bound. The open problem moves entirely to the earlier retained prefix where affine coverage and pair multiplicity have not yet been classified.

### Universal affine closure and pair containment

The finite affine observations were generalized symbolically. Terminal residuals, backbone shells, and middle-fiber shells of every affine parent are affine. In particular, a fixed-step middle fiber has values `t-t_0` in sponsor-root coordinates.

Every child current or latent pair is therefore already a parent pair resource. Union-valued pair capacity is nonincreasing for arbitrary simultaneous output and retained subfamilies, while occurrence-valued excess is exactly repeated pair-token mass.

This resolves the long-standing overlap/provenance bookkeeping bottleneck at the level of distinct resources. The active analytical bottleneck is now economical pair activation or a summable bound on the activated pair universe, not another retention rule.

### Third-to-fourth pair-resource contraction

The pair-resource test was moved one level earlier. All fourteen `R_3` recursive states are affine. Every `F_4` current or latent pair is contained in the parent resource universe. Pair multiplicity is at most two, and both occurrence and union potentials contract by more than `5000` units of exact pair mass.

The finite obstruction prefix is now restricted to `R_1 -> F_2` and `R_2 -> F_3`; the later transitions are closed.

### Residual-sponsor backbone refinement

The first workflow attempt did not test the mathematics: it imported a nonexistent module, and an unsafe named `git add -A` pathspec masked that exception. After the repository-wide workflow hardening pass, the original error was preserved and the probe was rewritten against the certified lexicographic propagation APIs.

The corrected exact test partitions only the already-existing translated minimum backbone. It inserts no unshifted residual output and preserves raw support, point occurrences, and harmonic occurrence mass exactly. Under the same retained quotient, the residual-root shells are terminal, recursive points fall by `151`, recursive mass falls by `0.168809631114...`, and union pair-resource mass falls by `404.536054734914...`.

This closes the finite question of whether the symbolic residual-sponsor split is useful on the recorded failing transition. It is strongly favorable. The remaining analytical target is a state-independent sponsor-core activation bound.

### Terminal-parent stopping correction

The first retained family was historically propagated wholesale, but exact classification shows six of its twenty-one states are already three-AP-free. A terminal parent selects no action, has no middle fiber, and can emit only terminal translated-backbone shells. Propagating it is semantically invalid as recursive continuation.

The independent correction certificate gives:

```text
F1 terminal:  6 states,    52 points, mass 0.127088543982...
F1 recursive: 15 states, 11701 points, mass 0.158733022746...
```

Stopping those parents changes the maximum-harmonic second optimum. Ordinary corrected recursive mass is `0.416597543898...`; residual-sponsor refinement lowers it to `0.322355467082...`. The historical `0.937...` ratio is not a recursive contraction theorem.

### Full-color branching correction

The middle role need not discard two valuation colors. Emitting all three classes `v_2-v_3 mod 3` preserves every middle incidence while every color child remains four-AP-free with disjoint first three dilates. Together with parity-selected side children, every three-AP has exactly two memberships and total child mass is exactly `2 L(B)`, giving raw branching factor `4` up to Roth error.

An exhaustive regression checked all `2233` four-AP-free subsets of `[1,12]`, including `3174` three-AP occurrences.

### Sponsor transport and edge capacity

Every activated sponsor pair has a monotone deletion-rank transport to a direct edge, backward obstruction, or residual target. Full-color branching supplies an exact three-edge dictionary: side `d`, doubled side `2d`, and middle `d` carry the two adjacent and one outer pair edge of each progression. Completed in-parent distinct targets therefore have exact child-located capacity.

The unresolved terms are transport collisions, parent-external ambient completions, genuine ambient holes, and reuse of edge capacity across retained branches.

### Full-edge collision and unbounded reuse

Full-edge branching closes the local edge-production coefficient: occurrence
mass has factor `5`, and current pair-union mass has factor at least `5/2`.
Mandatory shelling makes every latent-pair lineage finite because normalized
gap `D/M` at least doubles.

Cross-branch reuse is nevertheless unbounded. A parametric three-layer family
produces arbitrarily many recursive side shells sharing one root progression.
The `m=4` certificate gives four copies of all three common latent pairs in one
transition.

Fixing one transported parent witness reveals the exact collision geometry:
all preimage child witnesses are three affine translates of their reference
set. The correct reserve is therefore weighted three-translate exposure, not
a uniform overlap constant.

### Scale-critical three-AP transfer

Completion transport preserves three-AP load after the exact type weights
`1/2,1,2`. Dyadic shell scale then allocates one first preimage of each type
with fractions `1/2,1/4,1/4` of one parent target. The exponent-one
scale-weighted row is exactly critical; all higher scale moments contract
before collision excess.

Unbounded collision multiplicity is converted to a lower-scale four-AP-free
reference-difference set. Each extra branch has an exact completion rectangle
and aspect ratio. The unresolved object is no longer pair activation itself,
but reuse of reference-gap and rectangle tokens across different repeated root
configurations.

**Decisions:**

- current-generation multiplicity is not persistent reserve;
- finite feature-LP witnesses are diagnostics, not theorem candidates without a transfer law;
- nearby deletion-policy changes do not remove the first failing expansion, although policy remains quantitatively important;
- the missing resource is cumulative ancestor-path scale capacity plus terminal/drop/obstruction release;
- the baseline failing survivor family is backbone-only, and scalar minimum-anchor release is not sufficient payment for enabled translation intervals;
- affine pivot forests admit an exact pair-energy Bellman potential, so root-pair reuse is controlled once affine coordinates and root-disjoint children are established;
- the new bottleneck is the entering pair energy and an affine-entry theorem, not another local reuse coefficient;
- `(u,p)` is the capacity-level token in the affine regime; `(u,p,i)` is history metadata unless a separate resource is proved;
- the fourth-to-fifth retained expansion is closed by pair energy and is no longer an open obstruction;
- pair energy, not scalar translation reserve, is the principal cumulative affine potential;
- generation six is unnecessary until earlier-generation affine entry and pair reuse are resolved;
- the fifth-frontier pair row has exact token ownership and no repeated payment; future work should reuse this resource schema rather than fit scalar surrogates;
- affine entry is automatic from the initial state under terminal, backbone, and middle-fiber output;
- union-valued pair containment resolves duplicate, containment, partial-overlap, and cross-generation payment semantics;
- the active theorem is economical pair activation, not another retained-child quotient or affine-purification lemma;
- `R_3 -> F_4` is closed in both occurrence and union pair-resource conventions; only the first two retained transitions remain as finite diagnostics;
- generation six is blocked until a state-independent transfer lemma is proposed;
- a new feature is admissible only with a transition recurrence, bounded-reuse interpretation, and telescoping role.
- terminal parents must stop immediately and may never be reintroduced as recursive production;
- the historical second-to-fifth chain is an exact diagnostic, not the terminal-stopped recursive tree;
- all three middle valuation colors are retained; choosing one color discards valid production without reducing per-progression multiplicity;
- completed in-parent pair targets use explicit full-color edge capacity rather than prepaid full latent pair energy;
- parent-external ambient roots and genuine ambient holes are different obstruction classes and must not be conflated;
- recursive latent-pair multiplicity has no universal finite bound;
- pairwise latent-pair disjointness is false even after mandatory dyadic shelling;
- dyadic gap growth proves pathwise termination but does not control branch count;
- every fixed-witness collision fiber must be accounted for as three affine translates of a reference set;
- the active reserve is weighted three-translate exposure, not scalar overlap multiplicity;
- the three full-edge types are allocated by shell-scaled capacities `1/2,1/4,1/4`, not by spending parent three-AP load three times;
- collision multiplicity transfers to lower-scale reference differences and explicit rectangle-aspect tokens;
- the remaining scalar obstruction is the critical excess `Y(P)`, not the local branching coefficient;
- higher scale moments contract before collisions but do not by themselves prove reciprocal summability;

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
29. a universal finite recursive latent-pair overlap constant;
30. pairwise recursive-shell latent-pair disjointness;
31. dyadic gap monotonicity without a cross-branch exposure charge.

---

## 12. Active closing target

The active scalar row is

```math
\Psi_1(\text{child witnesses})
\le
N\mathcal L_3(P)
+
Y(P),
```

where first appearances are paid by exact role capacities `1/2,1/4,1/4` and
`Y(P)` is the scale-critical collision excess.

Every term of `Y(P)` has two exact exports:

```text
lower-scale four-AP-free reference-difference reserve;
completion rectangle with aspect ratio delta/D.
```

The immediate task is a first-appearance theorem for those exported tokens,
including unused shell slack, terminal release, and ambient
external-completion/genuine-hole separation. CL-087 must be audited before its
finite values are used. Corrected-third-frontier and generation-six
propagation remain blocked.

---

## 13. Documentation protocol

Every substantive theorem, counterexample, or finite certificate should update:

1. a dedicated note;
2. a verifier and recorded certificate;
3. `docs/certainty-ledger.md`;
4. `docs/current-proof-program.md` when the dependency graph changes;
5. this decision history when a route opens or closes.

Counterexamples to proposed lemmas remain part of the permanent progress record.
