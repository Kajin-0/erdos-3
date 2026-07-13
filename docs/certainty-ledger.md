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

## CL-038: Exact target-demand transport reserve

**Status:** elementary interval theorem plus exact finite application. **Certainty:** high.

For target interval `I`,

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At the `S_10` residual, `q_S(I)=76583771`, so the closure margin is exactly `5`. The larger overlap excess `9474912` is not the target reserve.

---

## CL-039: Replay siblings are not simultaneous children

**Status:** exact semantic and finite catalog result. **Certainty:** high.

`S_1` has four factor-four replay siblings and `S_2` has `203` factor-eight replay siblings, but these are alternative continuations and cannot be summed as one simultaneous Bellman child family.

---

## CL-040: Exhaustive coordinated schedule theorem on `S_1`

**Status:** exact finite exhaustion. **Certainty:** high.

There are `120` reachable states, `1560` progression-labeled schedules, and `930` sponsor sequences. Every schedule has all middle-fiber support inside the backbone and zero novel fiber mass.

---

## CL-041: Novel fiber mass is schedule dependent on `S_2`

**Status:** exact finite witnesses. **Certainty:** high.

The lexicographic schedule has positive novel mass, while another valid schedule has zero novelty. Therefore

```math
\min_\sigma\mathcal N_\sigma(S_2)=0.
```

Raw novelty is not parent-intrinsic.

---

## CL-042: Root-forced fork lemma and reserve

**Status:** general combinatorial lemma plus exact finite values. **Certainty:** high internally.

A root-forced progression must be selected by every complete coordinated schedule. Hence

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
```

Positive lower bounds are certified through `S_7`.

---

## CL-043: Forced-fork reserve is not a standalone Bellman potential

**Status:** exact finite no-go theorem. **Certainty:** high.

For `F(S)=P Psi(S)`, the factor-four transition `S_1 -> S_2` has `F(S_1)-F(S_2)<0` while debt is `5/4`.

---

## CL-044: Raw simultaneous transition exporter

**Status:** exact fixed-policy infrastructure. **Certainty:** high for the payloads.

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

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
\le
M H\left(\bigcup_iC_i\right).
```

The exact maximum multiplicities through `S_7` are

```text
2,3,7,11,12,13,16.
```

The harmonic-average multiplicity remains below `8/5`, `11/10`, or `9/8`. This does not prove bounded cross-generation reuse.

---

## CL-046: Terminal-fiber incidence graph is cyclic

**Status:** exact fixed-policy finite theorem. **Certainty:** high.

The graph with edge `q -> u` when `u in Q intersect Xi_q` contains `61 <-> 303` at `S_3`. At `S_7`, the cyclic component is

```math
\{1,5,61,303,1597,8195,323640\}.
```

A strict decreasing terminal-label rank is impossible.

---

## CL-047: Historical-separation-only state fails at `S_7`

**Status:** exact fixed-policy obstruction. **Certainty:** high.

At `S_7`, terminal-recursive overlap contains `5,49158,323640` in addition to historical separations. Tracking only the latest separation or separation history is inadequate.

---

## CL-048: SCC quotient and unit harmonic capacity no-go

**Status:** exact finite quotient and no-go theorem. **Certainty:** high.

For component `C`, let

```math
V(C)=\sum_{u\in C}\frac1u,
\qquad
T(C)=\sum_{(q,u)\text{ internal edge}}\frac1u.
```

For `{61,303}` through `S_6`, `T(C)=V(C)`. At `S_7`,

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

Harmonic vertex mass alone is insufficient component capacity.

---

## CL-049: Exact SCC spectral-growth obstruction

**Status:** exact finite theorem using Collatz-Wielandt. **Certainty:** high.

For the two-label component through `S_6`, the internal adjacency matrix squares to the identity and has spectral radius `1`.

For the seven-label `S_7` component, the positive integer vector

```math
w=(43,59,31,31,14,10,26)^T
```

satisfies

```math
9Aw-23w>0,
\qquad
8w-3Aw>0.
```

Therefore

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

No positive linear internal SCC capacity can be nonexpanding or factor-two contractive on this recorded component without external obstruction export.

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
11. exact-state quotienting as a containment solution;
12. a uniform maximum-overlap constant;
13. a strict decreasing terminal-label rank;
14. latest- or historical-separation-only state;
15. unit harmonic SCC capacity;
16. any positive linear SCC capacity with contraction factor at most two on the recorded `S_7` component;
17. random sampling as a finite certificate;
18. the rejected depth-ten anchor reduction.

---

# Open bottleneck OB-001: Cyclic-component retention and bounded reuse

The state-specific cheap-extension problem at `S_10` is closed. Raw simultaneous transition generation is certified through `S_7`.

The unresolved theorem must control:

1. exact duplicate multiplicity;
2. strict containment;
3. partial overlap;
4. terminal-recursive overlap;
5. cyclic SCC internal recycling and spectral growth;
6. imported-label matching across generations;
7. repeated use of inherited and compound labels;
8. controlled error from discarded mass.

The target is

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

The next finite experiment must quantify export from the high-growth cyclic SCC into nonterminal fibers, affine obstruction classes, completion support, or rectangle coverage. No current theorem closes this gap.
