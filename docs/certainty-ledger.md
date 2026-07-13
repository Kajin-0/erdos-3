# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The active dependency structure is in `docs/current-proof-program.md`.

Statuses marked **exact finite** are computational statements for the recorded objects, not general asymptotic theorems.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard. **Certainty:** high.

For

```math
\alpha_j=\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

divergence of `sum_{n in A}1/n` is equivalent up to constants to `sum_j alpha_j=infinity`.

---

## CL-002: Coordinated deletion and minimum-translation backbone

**Status:** proved in repository. **Certainty:** medium-high internally.

Coordinated deletion leaves a three-term-progression-free residual of size at most `r_3(N)`. The minimum-translation backbone is four-term-progression-free, has size `|D|-1`, lies below `N`, and contracts labels by at least one half.

---

## CL-003: One-generation harmonic inequalities

**Status:** proved in repository. **Certainty:** medium-high internally.

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

---

## CL-004: Shell resolution and positive moments

**Status:** proved. **Certainty:** high for shelling.

Every recursive output must be resolved into standard dyadic shells. For `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

---

## CL-005: Center, anchor, predecessor, and antichain compression

**Status:** proved in repository. **Certainty:** medium-high internally.

Repeated labels at different centers or anchors are exported by translated layers. Fixed complete anchor histories obey the recorded antichain bounds.

---

## CL-006: Self-replicating aligned diamonds

**Status:** recursive theorem with finite verification. **Certainty:** medium-high.

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
\qquad
P_h\asymp|S_h|^{\log_3 2}.
```

---

## CL-007: Infinite exact scale-eight family

**Status:** exact computer-assisted construction. **Certainty:** high for the certificate.

```math
L_h=8^{h+1},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A finite automaton and exact carry search certify no nontrivial four-term progression in the union.

---

## CL-008: Sharp exact-model classification

**Status:** elementary theorem. **Certainty:** high internally.

Exact uncontaminated equal-translate reproduction requires `L'>=8L`, and

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

---

## CL-009: Finite contaminated depth-five burst

**Status:** exact finite construction. **Certainty:** high.

The initial scale factors are `4,8,4,4`, and

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Universal local contraction and contraction over every four-step window are false.

---

## CL-010: Path-dependent recovery

**Status:** exact finite construction. **Certainty:** high.

The chain extends through `S_7` with scale word `4,8,4,4,8,4`. Universal two-generation recovery and contraction over every six-step window are false.

---

## CL-011: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite theorem. **Certainty:** high.

```math
N_{7,2}=N_{7,4}=0.
```

---

## CL-012: Exact depth-eight continuation

**Status:** exact finite construction. **Certainty:** high.

```math
R_7=2097164,
\qquad
|S_8|=29523,
\qquad
P_8=256.
```

---

## CL-013: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite theorem. **Certainty:** high.

```math
N_{8,2}=N_{8,4}=0.
```

---

## CL-014: Exact depth-nine continuation

**Status:** exact finite construction. **Certainty:** high.

```math
R_8=16777217,
\qquad
|S_9|=88572,
\qquad
P_9=512.
```

---

## CL-015: Complete cheap-extension exclusion from `S_9`

**Status:** exact finite theorem. **Certainty:** high.

```math
N_{9,2}=N_{9,4}=0.
```

The factor-four domain is exhausted by completion and recursive rectangle witnesses plus seven explicit terminal witnesses.

---

## CL-016: Exact depth-ten continuation

**Status:** exact finite construction. **Certainty:** high.

```math
R_9=134217729,
\quad
L_{10}=536870912,
\quad
|S_{10}|=265719,
\quad
P_{10}=1024.
```

The finite scale word is `4,8,4,4,8,4,8,8,8`.

---

## CL-017: Exact-tail top-layer reduction

**Status:** elementary theorem with exact verification. **Certainty:** high internally.

In every certified exact-tail geometry used through CL-030, each new four-term progression comes from either a completion at `R` or the half-separation point `R/2` inside the state.

---

## CL-018: Completion descent

**Status:** elementary theorem with exact verification. **Certainty:** high internally.

For `R=2L+k`, scheduled child completion targets descend through the recorded layer pattern, and `4k` descends to the preceding separation.

---

## CL-019: Explicit infinite exact tail from `S_10`

**Status:** exact infinite theorem with finite seed certificate. **Certainty:** high internally.

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

---

## CL-020: Original exact-tail basin criterion

**Status:** elementary theorem. **Certainty:** high internally.

The original small-offset criterion produces infinite exact scale-eight tails with charge `4P(N+1)/L`.

---

## CL-021: Original depth-ten basin fan

**Status:** exact finite classification. **Certainty:** high.

The original basin contains `11129810` certified offsets from `S_10`.

---

## CL-022: Exact-tail Bellman potential

**Status:** elementary algebraic theorem. **Certainty:** high.

For `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right).
```

At `c=8`, `B_8=4P(N+1)/L`.

---

## CL-023: Scale-word Bellman debt identity

**Status:** elementary exact theorem. **Certainty:** high.

```math
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
```

Factors `2` and `4` create positive cheap-step debt, `8` is neutral, and larger factors create surplus.

---

## CL-024: Cheap-debt repayment parsing

**Status:** elementary sufficient theorem. **Certainty:** high.

A scale word parsable into the recorded repayment blocks has summable weighted density. Universal geometric realizability remains open.

---

## CL-025: Cheap-step slack and contamination trichotomy

**Status:** elementary exact theorem. **Certainty:** high.

For `T=2L-max S`,

```math
T'=T+(c-2)L-2R.
```

Factor-two and factor-four debt is accompanied by strict slack consumption or imported-prefix contamination.

---

## CL-026: Exact `S_10` candidate domains

**Status:** exact finite domain certificate. **Certainty:** high.

Factor two has `33026376` layer-disjoint candidates. Factor four has `348012826` candidates.

---

## CL-027: Complete exact factor-eight classification from `S_10`

**Status:** exact finite classification. **Certainty:** high.

There are

```math
408855759
```

valid positive exact factor-eight children.

---

## CL-028: Half-scale exact-tail basin

**Status:** elementary infinite theorem with exact verification. **Certainty:** high internally.

A valid exact child in the half-scale region enters an infinite scheduled exact tail. At `S_10`, this gives `178872402` offsets.

---

## CL-029: Full-fitting scheduled basin from `S_10`

**Status:** exact finite obstruction classification plus induction. **Certainty:** high internally.

The unmodified schedule gives infinite tails for `408767151` valid exact children.

---

## CL-030: Complete exact-child infinite-tail fan from `S_10`

**Status:** exact finite repair classification plus induction. **Certainty:** high internally.

Finite `+1` repairs cover the remaining `88608` children. Every valid exact factor-eight child has a certified infinite tail of charge `33215/16384`.

---

## CL-031: Complete factor-two inheritance exclusion from `S_10`

**Status:** exact embedding theorem. **Certainty:** high.

```math
\boxed{N_{10,2}=0.}
```

---

## CL-032: First 10000 genuinely new `S_10` factor-four candidates

**Status:** exact finite prefix regression. **Certainty:** high for the prefix only.

The first `10000` candidates above the inherited cutoff have explicit witnesses. CL-037 supersedes this as a frontier.

---

## CL-033: Exact 34-class obstruction recurrence

**Status:** elementary state-independent theorem with exact symbolic verification. **Certainty:** high internally.

The `80` nonconstant raw layer words reduce to `34` classes, and the affine spectrum closes under the exact two-scale recurrence.

---

## CL-034: Lifted `S_9` completion reduction at `S_10`

**Status:** exact finite structural-witness theorem. **Certainty:** high.

Lifted completion support removes `137142200` candidates and leaves the exact residual of `177844250` candidates on `[97474324,613454687]`.

---

## CL-035: Exact four-ratio rectangle transport

**Status:** elementary state-independent theorem. **Certainty:** high internally.

A direct rectangle at effective separation `U` transports through one replication at precisely the integer ratios `1,2,3,4`. There are no positive integer cancellation ratios at least `5`.

---

## CL-036: Complete direct rectangle support of `B_9`

**Status:** exact finite computer-assisted theorem. **Certainty:** high internally.

For `B_9={0} union S_9`,

```math
\mathcal F_{B_9}(U,-U;0)>0
\quad
\text{for }1\le U\le76583776.
```

The certificate contains `76581484` structural values, `2285` deterministic terminal witnesses, and `7` stored large-fiber witnesses.

---

## CL-037: Complete factor-four exclusion from `S_10`

**Status:** exact finite theorem plus elementary transport. **Certainty:** high internally.

```math
33026376+137142200+177844250=348012826,
```

and the blocks are excluded by inheritance, lifted completion support, and direct rectangle transport. Therefore

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

---

## CL-038: Exact target-demand transport reserve

**Status:** elementary interval theorem plus exact finite application. **Certainty:** high.

For four centers `S,2S,3S,4S`, integer windows coalesce exactly when

```math
2U+1\ge S.
```

For target interval `I`,

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At the `S_10` residual, `q_S(I)=76583771`, so the closure margin is exactly `5`. The larger overlap excess `9474912` is not the target reserve.

---

## CL-039: Replay siblings are not simultaneous children

**Status:** exact semantic and finite catalog result. **Certainty:** high.

The replay catalog enumerates alternative outer separation choices. `S_1` has four factor-four replay siblings and `S_2` has `203` factor-eight replay siblings, but these alternatives cannot be summed as one simultaneous Bellman child family.

---

## CL-040: Exhaustive coordinated schedule theorem on `S_1`

**Status:** exact finite exhaustion. **Certainty:** high.

There are `120` reachable states, `1560` progression-labeled schedules, and `930` sponsor sequences. Every schedule has all middle-fiber support inside the minimum-translation backbone and therefore zero novel fiber mass.

---

## CL-041: Novel fiber mass is schedule dependent on `S_2`

**Status:** exact finite witnesses. **Certainty:** high.

The lexicographic schedule has novel mass

```math
\frac{239396453}{200655312}>0,
```

while another valid schedule has zero novelty. Therefore

```math
\min_\sigma\mathcal N_\sigma(S_2)=0.
```

Raw novelty is not a parent-only reserve.

---

## CL-042: Root-forced fork lemma and reserve

**Status:** general combinatorial lemma plus exact finite values. **Certainty:** high internally.

A root-forced progression must be selected by every complete coordinated schedule. This gives

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
```

Positive lower bounds are certified through `S_7`: `1/21,1/18,1/51,1/200,1/624,1/4321,1/14046`.

---

## CL-043: Forced-fork reserve is not a standalone Bellman potential

**Status:** exact finite no-go theorem. **Certainty:** high.

For `F(S)=P Psi(S)`, the factor-four transition `S_1 -> S_2` has

```math
F(S_1)-F(S_2)<0
```

while its debt is `5/4`. No nonnegative multiple of `P Psi` is a standalone stored potential.

---

## CL-044: Raw simultaneous transition exporter

**Status:** exact fixed-policy infrastructure. **Certainty:** high for the payloads.

The lexicographic exporter records the complete raw simultaneous occurrence family with schedule, shell resolution, provenance, exact duplicates, containments, and partial overlap.

The exact frontier through `S_7` is:

| parent | raw occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

The payload is before any retention quotient and is not a Bellman child list.

---

## CL-045: Exact local occurrence-multiplicity packing

**Status:** elementary identity plus exact finite spectra. **Certainty:** high.

For raw recursive occurrences `C_i`,

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
\le
M H\left(\bigcup_iC_i\right),
```

where `M=max m(u)`. The exact maxima through `S_7` are

```text
2,3,7,11,12,13,16.
```

The harmonic-average multiplicity is bounded by

```text
8/5,11/10,11/10,9/8,9/8,9/8,9/8.
```

Worst-case local multiplicity is not uniformly stable. Local harmonic-average control does not prove bounded cross-generation provenance reuse.

---

## CL-046: Terminal-fiber incidence graph is cyclic

**Status:** exact fixed-policy finite theorem. **Certainty:** high.

Draw an edge `q -> u` when `q` and `u` are terminal steps and `u in Xi_q`. The graph is acyclic at `S_1,S_2`, but contains the cycle

```math
61\longleftrightarrow303
```

at `S_3`, persisting through `S_6`. At `S_7`, the cyclic component is

```math
\{1,5,61,303,1597,8195,323640\}.
```

Any retention potential based on a strict decreasing rank of terminal labels is false on the recorded genealogy.

---

## CL-047: Historical-separation-only state fails at `S_7`

**Status:** exact fixed-policy finite obstruction. **Certainty:** high.

Through `S_6`, terminal-recursive overlap equals the base step plus historical replication separations. At `S_7`, additional labels `5,49158,323640` occur. A state tracking only the latest separation or the list of historical separations is inadequate.

---

## CL-048: SCC quotient and unit harmonic capacity no-go

**Status:** exact finite quotient and no-go theorem. **Certainty:** high.

Collapsing terminal-fiber strongly connected components yields an acyclic condensation graph. For a cyclic component `C`, define

```math
V(C)=\sum_{u\in C}\frac1u
```

and internal target mass

```math
T(C)=\sum_{(q,u)\text{ internal edge}}\frac1u.
```

For `C={61,303}` through `S_6`, `T(C)=V(C)`. At `S_7`, the seven-label component satisfies

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

Thus SCC capacity equal only to harmonic vertex mass fails at `S_7`. Internal edge capacity, provenance capacity, nonlinear potential, or obstruction export is required.

---

# Superseded, false, or prohibited inferences

Do not use without materially new hypotheses:

1. universal local `3/4` contraction in contaminated states;
2. contraction over every fixed short window;
3. universal two-generation recovery;
4. extrapolating one path or one exact tail fan to the whole tree;
5. treating replay siblings as simultaneous children;
6. treating pathwise summability as sufficient;
7. treating `nu(B)/S>1/2` as a complete target reserve;
8. treating novel fiber mass as schedule independent;
9. treating `P Psi` as a standalone Bellman potential;
10. copying raw simultaneous occurrences directly into an LP child sum;
11. merging provenance-distinct exact duplicates without a convention;
12. assuming a uniform maximum-overlap constant from the recorded path;
13. treating exact-state quotienting as a solution to containment or partial overlap;
14. assigning a strict decreasing rank to terminal-fiber labels;
15. tracking only the latest or historical separations;
16. assigning each SCC only its harmonic vertex mass as capacity;
17. random sampling as a finite certificate;
18. the rejected depth-ten anchor reduction.

---

# Open bottleneck OB-001: Cyclic-component retention and bounded reuse

The state-specific cheap-extension problem at `S_10` is closed. Raw simultaneous transition generation is certified through `S_7`.

The unresolved theorem must convert the raw occurrence family into a complete retained child family while controlling:

1. exact duplicate multiplicity;
2. strict containment;
3. partial overlap;
4. terminal-recursive overlap;
5. cyclic SCC internal recycling;
6. imported-label matching across generations;
7. repeated use of inherited and compound labels;
8. controlled error from discarded mass.

The target whole-tree inequality is

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

Approved next targets:

1. attach explicit internal capacity vectors to the certified SCC quotients;
2. test whether internal recycling plus outgoing capacity is paid by incoming capacity plus obstruction export;
3. preserve provenance while merging exact numerical state classes;
4. connect cyclic-component output to affine obstruction and rectangle coverage;
5. feed a proved retention convention into the exact rational LP harness;
6. extract the smallest exact failing transition for each candidate convention;
7. establish the branching Carleson inequality for all pre-basin states.

No current theorem closes this gap. The full Erdős problem remains unresolved.
