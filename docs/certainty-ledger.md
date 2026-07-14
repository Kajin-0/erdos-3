# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The active dependency structure is in `docs/current-proof-program.md`.

Statuses marked **exact finite** are computational statements for recorded objects, not general asymptotic theorems.

---

## Foundational and exact-path ledger

| ID | Durable claim | Status |
|---|---|---|
| CL-001 | Dyadic reciprocal-sum divergence is equivalent up to constants to divergence of `sum_j |A intersect [2^j,2^{j+1})|/2^j`. | Standard; high certainty. |
| CL-002 | Coordinated deletion leaves a three-term-progression-free residual; the minimum-translation backbone is four-term-progression-free and contracts labels by at least one half. | Proved internally. |
| CL-003 | `H(B(D))+sum_x H(M_x) >= 3H(D)-2r_3(N)/N-1/N`, and `H(Q)+sum_q H(Xi_q)+H(B(D)) >= 2H(D)-r_3(N)/N-1/N`. | Proved internally. |
| CL-004 | Every child must be resolved into dyadic shells; for `p>=1`, `sum u^p <= 2^{1-p}a^p` over outputs of one parent label `a`. | Proved. |
| CL-005 | Center, anchor, predecessor, and antichain decompositions compress several repeated-label families. | Proved internally. |
| CL-006 | Aligned diamonds satisfy `|S_h|=(9*3^h-3)/2`, `P_h=2^h`, so persistence grows like `|S_h|^{log_3 2}`. | Recursive theorem plus finite verification. |
| CL-007 | There is a certified infinite exact scale-eight family with `L_h=8^{h+1}` and `P_h=(1/2)L_h^{1/3}`. | Exact computer-assisted theorem. |
| CL-008 | In the exact uncontaminated equal-translate model, `P_h alpha_h <= C_0(3/4)^h` and total weighted density is at most `4C_0`. | Elementary theorem. |
| CL-009 | The contaminated chain begins `4,8,4,4` and has `W_5/W_1=91/32>1`; universal local contraction is false. | Exact finite construction. |
| CL-010 | The chain through `S_7` disproves universal two-generation recovery and fixed six-step contraction. | Exact finite construction. |
| CL-011 | `N_{7,2}=N_{7,4}=0`. | Exact finite theorem. |
| CL-012 | `S_8` has `R_7=2097164`, size `29523`, persistence `256`. | Exact finite construction. |
| CL-013 | `N_{8,2}=N_{8,4}=0`. | Exact finite theorem. |
| CL-014 | `S_9` has `R_8=16777217`, size `88572`, persistence `512`. | Exact finite construction. |
| CL-015 | `N_{9,2}=N_{9,4}=0`. | Exact finite theorem. |
| CL-016 | `S_10` has `R_9=134217729`, `L_10=536870912`, size `265719`, persistence `1024`. | Exact finite construction. |
| CL-017 | In the certified exact-tail geometry, new progressions reduce to completion at `R` or the half-separation point. | Elementary theorem plus exact verification. |
| CL-018 | Scheduled completion targets descend through the recorded layer pattern. | Elementary theorem plus exact verification. |
| CL-019 | The explicit infinite exact tail from `S_10` has total charge `33215/16384`. | Exact infinite theorem with finite seed. |
| CL-020 | The original small-offset basin criterion produces exact scale-eight tails with charge `4P(N+1)/L`. | Elementary theorem. |
| CL-021 | The original `S_10` basin contains `11129810` offsets. | Exact finite classification. |
| CL-022 | For `c>6`, `B_c=cP(N+6/(c-2))/((c-6)L)`; at `c=8`, `B_8=4P(N+1)/L`. | Exact algebra. |
| CL-023 | `B-W-B' = P(3N+4)(1-8/c)/L`; factors `2,4` create debt, `8` is neutral. | Exact algebra. |
| CL-024 | Scale words parsable into the recorded repayment blocks are summable. | Sufficient theorem; realizability open. |
| CL-025 | Cheap replication consumes shell slack or imports prefix contamination according to the exact trichotomy. | Exact theorem. |
| CL-026 | The `S_10` candidate domains contain `33026376` factor-two and `348012826` factor-four candidates. | Exact finite certificate. |
| CL-027 | `S_10` has `408855759` valid positive exact factor-eight children. | Exact finite classification. |
| CL-028 | The half-scale basin gives `178872402` exact-tail offsets. | Exact theorem and computation. |
| CL-029 | The unmodified schedule handles `408767151` exact children. | Exact finite theorem. |
| CL-030 | Finite `+1` repairs handle the remaining `88608`; every valid exact factor-eight child has an infinite tail. | Exact finite theorem. |
| CL-031 | `N_{10,2}=0` by exact inheritance. | Exact embedding theorem. |
| CL-032 | The first `10000` new factor-four candidates have explicit witnesses; superseded by CL-037. | Prefix regression only. |
| CL-033 | The `80` nonconstant layer words reduce to `34` affine classes and obey an exact two-scale recurrence. | State-independent theorem. |
| CL-034 | Lifted completion support removes `137142200` candidates and leaves `177844250` residual candidates. | Exact finite theorem. |
| CL-035 | Direct rectangles transport at precisely ratios `1,2,3,4`; no positive cancellation ratios at least `5`. | State-independent theorem. |
| CL-036 | For `B_9={0} union S_9`, direct rectangle support is complete for `1<=U<=76583776`. | Exact finite theorem. |
| CL-037 | Inheritance, lifted completion, and rectangle transport exclude all `348012826` factor-four candidates; `N_{10,2}=N_{10,4}=0`. | Exact finite theorem. |

---

## Whole-tree reserve and transition ledger

| ID | Durable claim | Status |
|---|---|---|
| CL-038 | For target interval `I`, `q_S(I)=max_{T in I} min_{1<=k<=4}|T-kS|`. At the `S_10` residual the exact closure margin is `5`, not the coarse overlap excess `9474912`. | Elementary interval theorem plus exact finite application. |
| CL-039 | Replay siblings are alternative continuations, not simultaneous Bellman children. `S_1` has four factor-four replay siblings and `S_2` has `203` factor-eight replay siblings. | Exact semantic and finite catalog result. |
| CL-040 | `S_1` has `120` reachable states, `1560` progression-labeled schedules, and `930` sponsor sequences; every schedule has zero novel fiber mass outside the backbone. | Exact finite exhaustion. |
| CL-041 | Novel fiber mass is schedule dependent on `S_2`; one valid schedule has positive novelty and another has zero, so `min_sigma N_sigma(S_2)=0`. | Exact finite witnesses. |
| CL-042 | Every root-forced progression must be selected, giving `sum_q H(Xi_q^sigma)>=Psi(D)`; positive lower bounds are certified through `S_7`. | General combinatorial lemma plus exact finite values. |
| CL-043 | `F(S)=P Psi(S)` is not a standalone Bellman potential: on `S_1 -> S_2`, `F(S_1)-F(S_2)<0` while factor-four debt is `5/4`. | Exact finite no-go theorem. |
| CL-044 | The raw simultaneous transition exporter is certified through `S_7`; the `S_7` payload has `127` occurrences, `95` state classes, `20` duplicate classes, `345` containments, and `214` partial overlaps. | Exact fixed-policy infrastructure. |
| CL-045 | `sum_i H(C_i)=sum_u m(u)/u <= M H(union_i C_i)`. Maximum local multiplicities through `S_7` are `2,3,7,11,12,13,16`; harmonic-average multiplicity stays small but does not control cross-generation reuse. | Elementary identity plus exact finite spectra. |
| CL-046 | The terminal-fiber incidence graph is cyclic. It contains `61 <-> 303` at `S_3`; at `S_7` the cyclic component is `{1,5,61,303,1597,8195,323640}`. | Exact fixed-policy finite theorem. |
| CL-047 | Historical-separation-only state fails at `S_7`: terminal-recursive overlap also contains `5,49158,323640`. | Exact fixed-policy obstruction. |
| CL-048 | Unit harmonic SCC capacity fails. For the `S_7` component, `T(C)-V(C)=43727503229099/1043823972523464>0`. | Exact finite quotient and no-go theorem. |
| CL-049 | The `S_7` internal SCC adjacency satisfies `23/9 < rho(A) < 8/3`; no positive linear internal capacity can be nonexpanding or factor-two contractive without external credit. | Exact finite Collatz-Wielandt theorem. |
| CL-050 | The `S_7` cyclic component emits `6020` distinct novel labels. Even after numerical deduplication, total emitted support has output/input harmonic ratio greater than `7/5`; raw output union is additional recursive load, not repayment. | Exact fixed-policy finite theorem. |
| CL-051 | Across `62` exact shell children sourced by the `S_7` cyclic component, novel labels create local collision/completion invalidity for `140352/950202` factor-two and `398745/4986696` factor-four replay candidates. Most candidates remain. | Exact fixed-policy finite theorem. |
| CL-052 | On the `33` exact cyclic-source child states of size at most `50`, complete three-translate four-AP testing leaves `15160/21724` factor-two and `75723/87829` factor-four candidates valid. Deterministic first witnesses span `33` of the `34` nonconstant affine classes; class `22` is absent only from the first-witness histogram. | Exact fixed-policy finite theorem. |
| CL-053 | The novel child `{16,21,26}` at scale `16` is the unique factor-two/factor-four exact return from the `62` cyclic-source states to any canonical `S_1,...,S_10`: factor four with `R=1` gives `S_1` exactly. It is disjoint from all other `126` recursive shells and all terminal outputs of the raw `S_7` transition. | Exact fixed-policy path, uniqueness, and isolation theorem. |
| CL-054 | Canonical regeneration is schedule-dependent on `S_7`. The lexicographic schedule has one exact return to `S_1`; a reverse-lexicographic complete schedule has no seed shell and no factor-two/factor-four exact return to any `S_1,...,S_10`. | Exact two-policy finite theorem. |
| CL-055 | Reverse lexicographic deletion avoids canonical regeneration but has over `75` times the lexicographic middle-fiber occurrence mass, over `744` times the duplicate mass, `2252` terminal steps, `2374` shells, and a `286`-label SCC. | Exact two-policy finite theorem. |
| CL-056 | Delaying only the three unforced seed-producing `q=1` actions removes canonical regeneration while reducing shell count, occurrence mass, union mass, duplicate mass, harmonic-average multiplicity, and maximum multiplicity relative to lexicographic deletion. Terminal mass rises and residual error increases by exactly `1/4096`. | Exact finite Pareto-tradeoff theorem. |
| CL-057 | Exact policy-weight thresholds separate lexicographic and delayed-seed preferences: `2.384<lambda_*<2.385`, `4.356<kappa_*<4.357`, `0.021<gamma_*<0.022`, and `0.418<a_*<0.419` for the recorded score families. | Exact finite rational half-space theorem. |
| CL-058 | `C_lambda=T+lambda O+E` has a common tested subcone `477/200<lambda<260/63`; `lambda=3` ranks lexicographic below reverse through `S_7` and delayed seed below lexicographic at `S_7`. | Exact finite multi-state policy-ranking theorem. |
| CL-059 | Delaying every step-5 action ties lexicographic under `C_3` on `S_1` and is strictly cheaper on `S_2,...,S_7`, but retains the canonical return. | Exact finite uniform-policy theorem. |
| CL-060 | Adding the seed delay removes regeneration; under `C_{3,gamma}`, it beats step-5 when `0.057<gamma_5<0.058`. | Exact finite continuation-weight theorem. |
| CL-061 | In the enlarged finite family, `C_{3,1/10}` selects step-5/40 variants through `S_6` and the non-regenerative hybrid at `S_7`; `gamma=1/16` fails and `gamma=1/10` succeeds. | Exact finite two-coordinate ranking theorem. |
| CL-062 | Delaying step `30` helps alone but hurts after steps `5` and `40`; favorable local policy perturbations are not composable. | Exact finite interaction/no-greedy theorem. |
| CL-063 | The first policy comparison exports `60` exact rational half-spaces and verifies `(lambda,gamma)=(3,1/10)` feasible. | Exact finite policy-LP theorem. |
| CL-064 | All `32` subsets of `{5,40,30,161,142}` on `S_1,...,S_6` produce `198` exact half-spaces. The witness remains feasible and the unique `S_3` optimum becomes `delay_5_161_142`. | Exact finite subset-lattice theorem. |
| CL-065 | Exhausting those subsets on `S_7` with and without seed delay, plus reverse deletion, gives `250` constraints. The unique `S_7` winner is non-regenerative `seed_5_142`. | Exact finite full five-step subset-lattice theorem. |
| CL-066 | A seed-delayed 37-step `S_7` policy has `9323` selected actions, residual `517`, `28` terminal classes, `9295` middle-fiber occurrences, and no canonical regeneration. It has no improving move in its exact 59-toggle neighborhood. | Exact finite local-optimality theorem. |
| CL-067 | The 37-step policy raw transition has `131` shells, `87` exact classes, `22` duplicate groups, `229` containments, `390` partial overlaps, maximum point multiplicity `18`, and no cyclic terminal-fiber SCC. | Exact finite transition-profile theorem. |
| CL-068 | Exact-state quotienting plus componentwise maximum-harmonic same-shell conflict selection produces a unique `21`-state, `11753`-label point-disjoint retained family carrying `73.1%`–`73.2%` of raw-union harmonic mass. | Exact finite one-generation retained-child theorem. |
| CL-069 | Propagating the 21 retained states and reapplying the quotient produces a unique `27`-state, `7925`-label point-disjoint family. Root provenance multiplicity is at most three, but total retained mass expands by `6.828`–`6.829`. | Exact finite second-generation provenance theorem. |
| CL-070 | Every floor-log contraction at least eight carries repeated root provenance. Repeated roots carry `7.6%`–`7.7%` of root occurrence mass but produce `94.8%`–`94.9%` of descendant mass. Unit depth/log charges fail by factors greater than `77`. | Exact finite provenance-times-scale theorem. |
| CL-071 | The 27 second-generation retained states split into 13 terminal states with 43 labels and 14 recursive states with 7882 labels. Terminal states carry `86.2%`–`86.3%` of second retained mass. Recursive mass is `93.7%`–`93.8%` of first retained mass, giving `6.2%`–`6.3%` contraction. | Exact finite terminal decomposition and recursive-contraction theorem. |
| CL-072 | The 13 terminal states admit an exact identity export anchored to the certified retained-family and 7925-point provenance hashes. Their 43 numerical labels are pairwise unique, disjoint from recursive retained labels, and their 43 `(u,p)` point tokens are unique within the recorded family. | Exact finite terminal-sink identity theorem. |
| CL-073 | For any fixed terminal-token map on a finite or locally finite rooted tree, assigning each token to its first node in a deterministic total order gives pairwise disjoint first-appearance ledgers whose weighted sum equals the weighted global token union. | Elementary whole-tree accounting lemma; token soundness and union bound remain open. |
| CL-074 | Propagating only the 14 recursive second-generation states and reapplying the same global retained quotient produces a unique point-disjoint third family with 32 states and 4899 points: 18 terminal states with 110 points and 14 recursive states with 4789 points. Recursive third-generation mass is `2.011553`–`2.011554` times second-generation recursive mass and `1.886248`–`1.886249` times first retained mass. The `31/500` two-generation Bellman credit therefore does not iterate under this fixed policy and quotient. | Exact finite third-generation recursive-expansion and Bellman no-go theorem. |
| CL-075 | The 43 second-generation terminal `(u,p)` tokens have no collision with first-generation raw or retained tokens, but `(60,1354490)` recurs as a third-generation terminal sink. Both occurrences are step-5 middle fibers; immediate provenance differs (`2810` versus `440`) and separates the collision. Numerical identity is much coarser: 28 labels and seven complete terminal numerical states recur. | Exact finite cross-generation token-collision and signature-refinement theorem. |
| CL-076 | With current harmonic mass coefficient fixed to one, an exact 11-feature screen finds four feasible standalone nonnegative corrections. In particular, `Phi_rep=H+2R`, where `R` is descendant harmonic mass on points whose root provenance repeats within the retained generation, contracts by `27.4704%`-`27.4705%` and then `6.0556%`-`6.0557%`. Independently, `Phi_tail=H+4T`, where `T` is descendant mass with immediate-provenance depth drop at least four, contracts on both transitions and has second-transition margin `0.1313%`-`0.1314%`. | Exact finite three-generation retained-potential theorem. |
| CL-077 | Propagating the 14 third-generation recursive states and reapplying the same quotient produces a unique point-disjoint fourth family with 23 states and 1794 points, split into 11 terminal states with 77 points and 12 recursive states with 1717 points. `H4_rec/H3_rec` is `2.849279`-`2.849280`. The CL-076 candidates fail: `H+2R` expands by `2.711908`-`2.711909` because repeated-root reserve vanishes, and `H+4T` expands by `9.636610`-`9.636611` because the immediate depth-four tail regenerates. Seven `(u,p)` terminal collisions occur, but no `(u,p,i)` collision is recorded through generation four. | Exact finite fourth-generation potential no-go and refined-token survival theorem. |

Primary latest references:

- `docs/fourth-generation-provenance-reserve-frontier.md`;
- `src/verify_fourth_generation_potential_frontier.py`;
- `docs/generation-aware-retained-potentials.md`;
- `src/verify_generation_aware_retained_potentials.py`;
- `docs/third-generation-recursive-frontier.md`;
- `docs/two-generation-recursive-bellman-row.md`;
- `docs/retained-terminal-sink-identity-ledger.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-recursive-split.md`;
- `docs/retained-provenance-scale-profile.md`;
- `src/verify_third_generation_recursive_frontier.py`;
- `src/export_retained_terminal_sink_ledger.py`.

---

# Prohibited inferences

Do not use without materially new hypotheses:

1. universal local or fixed-window contraction;
2. replay siblings as simultaneous children;
3. pathwise summability as whole-tree summability;
4. raw novelty as schedule independent;
5. `P Psi` as a standalone Bellman potential;
6. raw occurrences copied directly into a Bellman child sum;
7. exact-state quotienting alone as a containment theorem;
8. a uniform overlap constant or decreasing terminal-label rank;
9. unit harmonic or factor-two linear SCC capacity;
10. raw numerical union as stored repayment;
11. local affine obstruction coverage as complete repayment;
12. absence from a first-witness histogram as absence from all witnesses;
13. all small surviving states as negligible errors;
14. one regenerative path as whole-tree divergence;
15. regeneration as parent-intrinsic;
16. one finite policy witness as an all-policy theorem;
17. avoidance of regeneration as sufficient optimization;
18. raw occurrence or label count without harmonic/provenance weights;
19. one finite weight cone as global validation;
20. greedy composition of favorable policy delays;
21. one-toggle local optimality as global policy optimality;
22. lower raw harmonic occurrence mass as Bellman contraction;
23. one-generation retention as a bound on indefinite reuse;
24. maximum provenance multiplicity three as contraction;
25. unit depth/log charge as repayment for total retained mass;
26. the full `6.828`–`6.829` ratio as recursive load;
27. discarding terminal mass instead of charging it once;
28. within-family terminal-token uniqueness as global uniqueness;
29. `(u,p)` as a collision-sound cross-generation terminal token;
30. source type and source step as sufficient collision refinement;
31. first-appearance deduplication as a bound on token-union mass;
32. the `6.2%`–`6.3%` recursive contraction or `31/500` credit as an iterating invariant;
33. the third-generation expansion as universal over all policies or quotients;
34. immediate provenance as globally sufficient after one finite collision test;
35. `H+2R` or `H+4T` as a universal Bellman potential after two finite transitions;
36. `H+2R` or `H+4T` as an iterating potential after the fourth-generation failure;
37. maximum-harmonic local retention as globally optimal;
38. policy-LP feasibility as branching Bellman-LP feasibility;
39. the tested policy family as globally optimal;
40. random sampling as a finite certificate;
41. the rejected depth-ten anchor reduction.

---

# Open bottleneck OB-001: exact four-generation feature LP

The adversarial retained construction now has:

- legitimate point-disjoint retained families through generation four;
- exact terminal/recursive partitions at generations two, three, and four;
- recursive mass ratios below one, above two, and above 2.84 on successive transitions;
- a complete first-appearance terminal ledger;
- failure of `(u,p)` and finite survival of `(u,p,i)`;
- two exact three-generation reserve witnesses;
- and an exact fourth-generation failure of both witnesses.

The next theorem is an exact nonnegative feature-feasibility problem. Export the three recursive transitions into a common rational matrix with current harmonic coefficient fixed to one. Test whether any nonnegative combination of the existing provenance, multiplicity, and depth features makes all three rows nonpositive.

If feasible, record a sparse rational witness. If infeasible, extract the smallest exact Farkas or dual obstruction before introducing cumulative provenance, ancestor-path, terminal-release, or affine-obstruction coordinates.

The whole-tree target remains

```math
\Delta(S)
+
\mathrm{TermSink}_{\mathrm{first}}(S)
+
\sum_{S'\in\mathrm{RecChild}_\pi(S)}
\mathrm{RecPack}(S')
\le
\mathrm{RecPack}(S)
+
\Phi_{\mathrm{obs}}(S)
+
\mathrm{controlled\ error}.
```
