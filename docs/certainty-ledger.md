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
| CL-054 | Canonical regeneration is schedule-dependent on `S_7`. The lexicographic schedule has one exact return to `S_1`; a reverse-lexicographic complete coordinated schedule has no `{16,21,26}` seed shell and no factor-two/factor-four exact return to any `S_1,...,S_10`. The seed-producing centers are not root-forced. | Exact two-policy finite theorem. |
| CL-055 | Reverse lexicographic deletion avoids canonical regeneration but has over `75` times the lexicographic middle-fiber occurrence mass, over `744` times the duplicate mass, `2252` terminal steps, `2374` shells, and a `286`-label SCC. Avoiding regeneration is not a sufficient policy objective. | Exact two-policy finite theorem. |
| CL-056 | Delaying only the three unforced seed-producing `q=1` actions removes canonical regeneration while reducing shell count, occurrence mass, union mass, duplicate mass, harmonic-average multiplicity, and maximum multiplicity relative to lexicographic deletion. Terminal mass rises and residual error increases by exactly `1/4096`. | Exact finite Pareto-tradeoff theorem. |
| CL-057 | Exact policy-weight thresholds separate lexicographic and delayed-seed preferences: `2.384<lambda_*<2.385` for `T+lambda O+E`, `4.356<kappa_*<4.357` for `T+U+kappa D+E`, `0.021<gamma_*<0.022` when charging the lexicographic regenerative path, and `0.418<a_*<0.419` for `aT+O+E`. Unit terminal plus unit recursive-mass scores prefer lexicographic deletion. | Exact finite rational half-space theorem. |
| CL-058 | The score `C_lambda=T+lambda O+E` has a certified common policy subcone `477/200<lambda<260/63`. Every such weight ranks lexicographic below reverse lexicographic deletion on `S_1,...,S_7`, while ranking the delayed-seed policy below lexicographic deletion on `S_7`. The witness `lambda=3` gives the tested policy family `S_1,...,S_6` lexicographic and `S_7` delayed-seed. | Exact finite multi-state policy-ranking theorem. |
| CL-059 | The uniform policy that delays every step-5 action ties lexicographic deletion under `C_3=T+3O+E` on `S_1` and is strictly cheaper on every `S_2,...,S_7`. At `S_7` it still contains the isolated canonical return `{16,21,26}->S_1`. | Exact finite uniform-policy theorem. |
| CL-060 | A hybrid delaying step-5 and the three seed-producing `q=1` actions removes canonical regeneration but has higher raw `C_3` than the step-5 policy. For `C_{3,gamma}=T+3O+E+gamma G_regen`, the hybrid beats step-5 when `gamma>gamma_5`, where `0.057<gamma_5<0.058`; `gamma=1/16` is a valid witness for that pairwise comparison. | Exact finite continuation-weight theorem. |
| CL-061 | In the enlarged finite policy family, `C_{3,1/10}=T+3O+E+(1/10)G_regen` selects `step5/step540` on `S_2`, `step540` on `S_3,...,S_6`, and the non-regenerative `hybrid5` policy on `S_7`; reverse deletion is never selected. The active S7 constraint is `0.0837<gamma_540<0.0838`, so `gamma=1/16` fails and `gamma=1/10` succeeds. | Exact finite two-coordinate ranking theorem. |
| CL-062 | Delaying step `30` alone improves `C_3` relative to lexicographic deletion on every `S_2,...,S_7`, but adding the same delay after steps `5` and `40` reverses sign and worsens `C_3` on every `S_2,...,S_7`. Favorable local policy perturbations are not composable. | Exact finite interaction/no-greedy theorem. |
| CL-063 | The current policy comparisons export to `60` exact rational half-spaces in features `(lambda,gamma)`. The existing LP harness verifies `(3,1/10)` feasible. The only zero-slack rows are seven `S_1` ties and the `S_2` `step5/step540` tie; the active `S_7` continuation boundary is `hybrid5<=step540`. | Exact finite policy-LP feasibility theorem. |
| CL-064 | Expanding `S_1,...,S_6` to all `32` subsets of delayed steps `{5,40,30,161,142}` produces `198` exact policy half-spaces. `(lambda,gamma)=(3,1/10)` remains feasible. The unique `S_3` optimum changes to `delay_5_161_142`; `S_4,...,S_6` retain `delay_5_40` up to inactive `142/161` ties. The `S_7` side remains the current `13`-policy family and is not subset-exhaustive. | Exact finite subset-lattice policy-LP theorem. |
| CL-065 | Exhausting all `32` subsets of `{5,40,30,161,142}` on `S_7`, both with and without the seed-delay switch, plus reverse deletion, enlarges the exact policy LP to `250` constraints. `(lambda,gamma)=(3,1/10)` remains feasible. The unique `S_7` winner changes from `seed_5` to the non-regenerative `seed_5_142`; its exact advantage over `seed_5` lies between `3/2000` and `751/500000`. | Exact finite full five-step subset-lattice theorem through `S_7`. |
| CL-066 | A seed-delayed `S_7` policy with `37` delayed progression steps resolves to `9323` selected actions, residual size `517`, `28` terminal step classes, `9295` middle-fiber occurrences, and no canonical regeneration. In the exact one-toggle neighborhood given by its terminal-step set union delayed-step set (`59` candidates), it has no improving toggle, two zero-slack toggles, and minimum strict slack `384/111292259161`. Its exact score improves on `seed_5_142` by a value between `1915/1000` and `1916/1000`. | Exact finite terminal-step local-optimality theorem. |
| CL-067 | The raw transition of the 37-step local optimum has `131` shell occurrences, `87` exact state classes, `22` duplicate groups, `229` strict containments, `390` partial overlaps, maximum point multiplicity `18`, and an acyclic terminal-fiber incidence graph. Its recursive occurrence mass is between `254/1000` and `255/1000` of the lexicographic value. Relative to lexicographic deletion it removes the cyclic SCC and lowers harmonic load, but partial overlaps rise from `214` to `390` and maximum multiplicity from `16` to `18`. | Exact finite transition-profile and retention-obstruction theorem. |
| CL-068 | Exact-state quotienting with deterministic provenance representatives, followed by componentwise maximum-harmonic independent-set selection in the same-shell intersection graph, produces a unique `21`-state point-disjoint retained family from the local-optimum transition. The graph has `87` classes, `290` edges, `20` components, and largest component `13`; every component has a unique optimum. The retained family carries `11753` distinct labels and between `731/1000` and `732/1000` of the raw-union harmonic mass. | Exact finite one-generation provenance-preserving retained-child theorem. |

Primary references for CL-050 through CL-068:

- `docs/s7-cyclic-scc-output-load.md`;
- `docs/s7-cyclic-scc-local-completion-credit.md`;
- `docs/s7-cyclic-scc-small-state-affine-frontier.md`;
- `docs/s7-cyclic-output-seed-regeneration.md`;
- `docs/s7-regenerative-seed-policy-dependence.md`;
- `docs/s7-policy-transition-tradeoff.md`;
- `docs/s7-delayed-seed-policy.md`;
- `docs/s7-policy-weight-regions.md`;
- `docs/policy-occurrence-cone-s1-s7.md`;
- `docs/step5-policy-regeneration-weight.md`;
- `docs/two-coordinate-policy-family.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/s7-provenance-retained-quotient.md`;
- `src/verify_policy_occurrence_cone_s1_s7.py`;
- `src/verify_step5_policy_regeneration_weight.py`;
- `src/verify_two_coordinate_policy_family.py`;
- `src/verify_policy_halfspace_lp.py`;
- `src/verify_expanded_policy_subset_lp.py`;
- `src/verify_policy_subset_lattice_s1_s7.py`;
- `src/verify_s7_terminal_step_local_optimum.py`;
- `src/verify_s7_local_optimum_transition_profile.py`;
- `src/verify_s7_provenance_retained_quotient.py`.

---

# Prohibited inferences

Do not use without materially new hypotheses:

1. universal local `3/4` contraction;
2. fixed short-window contraction;
3. universal two-generation recovery;
4. extrapolating one path or one exact fan to the whole tree;
5. replay siblings as simultaneous children;
6. pathwise summability as sufficient;
7. rectangle radius without target demand;
8. raw novelty as schedule independent;
9. `P Psi` as a standalone Bellman potential;
10. raw occurrences copied directly into an LP child sum;
11. exact-state quotienting as a containment solution by itself;
12. a uniform maximum-overlap constant;
13. a strict decreasing terminal-label rank;
14. latest- or historical-separation-only state;
15. unit harmonic SCC capacity;
16. any positive linear SCC capacity with contraction factor at most two on the recorded `S_7` component;
17. treating the numerical union of cyclic output as unit-weight stored capacity;
18. treating layer collisions and same-layer completions as sufficient repayment for the `S_7` cyclic output;
19. treating complete one-generation affine testing as sufficient repayment on small cyclic-output children;
20. interpreting absence from the deterministic first-witness histogram as absence from all witnesses;
21. treating all small surviving states as negligible terminal errors;
22. inferring whole-tree divergence from the isolated regenerative path;
23. treating lexicographic regeneration as parent-intrinsic or schedule-independent;
24. using one policy witness as a minimax or all-policy theorem;
25. treating avoidance of canonical regeneration as sufficient policy optimization;
26. ranking policies by raw occurrence count or distinct-label count without harmonic and provenance weights;
27. treating the delayed-seed Pareto tradeoff as a completed Bellman contraction;
28. treating one finite weight threshold or common cone as global validation of its raw coordinate;
29. treating `T+3O+E` as sufficient after it chooses a known regenerative schedule;
30. assuming `gamma=1/16` survives enlargement of the policy family;
31. greedily composing individually favorable policy delays;
32. treating the earlier `S_3` `delay_5_40` choice as optimal after subset-lattice expansion;
33. treating the earlier `S_7` `seed_5` or `seed_5_142` choice as optimal after neighborhood expansion;
34. treating one-toggle local optimality as global policy optimality;
35. treating the 59-toggle neighborhood as exhaustive over arbitrary delayed progression steps;
36. inferring disjoint retained children from acyclic terminal-fiber incidence;
37. inferring Bellman contraction from lower raw harmonic occurrence mass;
38. treating one-generation point-disjoint retention as a bound on cross-generation provenance reuse;
39. treating maximum-harmonic local retention as globally Bellman-optimal;
40. treating policy-half-space LP feasibility as branching Bellman-LP feasibility;
41. inserting the recorded path charge directly into a Bellman child sum without a cross-generation packing theorem;
42. treating the tested policy family as globally optimal over all complete schedules;
43. random sampling as a finite certificate;
44. the rejected depth-ten anchor reduction.

---

# Open bottleneck OB-001: Cross-generation provenance packing

Within-generation retention is now solved for the adversarial local-optimum `S_7` transition: the certified quotient is exact, point-disjoint, maximum-harmonic componentwise, and carries explicit representative provenance.

The next task is to propagate the `21` retained states, apply the same quotient where tractable, and build the provenance-reuse graph from parent and sponsor labels to retained descendant representatives. A valid theorem must bound repeated reuse across generations, or identify the smallest exact reuse cycle that requires another packing coordinate.

The target remains

```math
\Delta(S)
+
\sum_{S'\in\operatorname{Child}_\pi(S)}
\left(
\operatorname{Pack}(S')+
\Phi_{\rm obs}(S')
\right)
\le
\operatorname{Pack}(S)+
\Phi_{\rm obs}(S)+
\operatorname{controlled\ error}.
```
