# Current proof program: policy-aware obstruction export and whole-tree packing

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Dyadic reduction and deletion genealogy

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

Coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-fiber resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every recursive output is resolved into standard dyadic shells. For `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

These statements control local moments. They do not by themselves control the full branching reciprocal mass.

---

## 2. Exact benchmark, contamination, and Bellman debt

The exact aligned recursion satisfies

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

In the uncontaminated equal-translate model, scale growth at least eight gives

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

The contaminated certified path has scale word

```text
4,8,4,4,8,4,8,8,8
```

through `S_10`, with

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Thus universal one-step, fixed-window, and universal two-generation contraction claims are false.

For constant exact scale factor `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right),
```

and the positive cheap-step debt is

```math
\Delta_c
=
\frac{P(3N+4)}L
\left(\frac8c-1\right).
```

Factors two and four create debt; factor eight is neutral.

---

## 3. Complete state-specific depth-ten barrier

Three-translate layer words reduce to `34` affine obstruction classes. The complete `S_10` factor-four domain partitions as

```math
33026376+137142200+177844250=348012826.
```

Inheritance removes the first block, lifted completion support removes the second, and direct rectangle transport removes the residual interval

```math
I_{10}=[97474324,613454687].
```

For target interval `I`, define

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At `S_10`, the available direct-support radius exceeds the exact target demand by only

```math
\boxed{5}.
```

Therefore

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

Every valid exact factor-eight child has a certified summable exact tail. This is a complete theorem for the recorded state, not a theorem for the entire deletion tree.

---

## 4. Raw simultaneous transition frontier

Replay siblings are alternative continuation choices, not simultaneous children. The fixed-policy raw exporter records one complete simultaneous occurrence family before any retention quotient.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

Maximum local occurrence multiplicities through `S_7` are

```text
2,3,7,11,12,13,16.
```

The harmonic-average multiplicity remains small, but this does not bound cross-generation reuse.

---

## 5. Schedule dependence and forced output

Novel middle-fiber mass is not parent-intrinsic. Every coordinated schedule on `S_1` has zero novelty, while `S_2` has both positive-novelty and zero-novelty complete schedules.

Root-forced progressions do give a schedule-independent lower bound

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D),
```

with positive certified values through `S_7`. However, `P\Psi` is not a standalone telescoping Bellman potential.

The role of forced output is therefore to supply unavoidable transition mass to a stronger packing or obstruction theorem, not to close the argument by itself.

---

## 6. Cyclic terminal-fiber obstruction

Draw an edge `q -> u` when terminal label `u` belongs to `Xi_q`. At `S_7`, the cyclic component is

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

For its internal adjacency matrix `A`, an exact Collatz-Wielandt witness gives

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

Hence no positive linear internal SCC capacity is nonexpanding or factor-two contractive without external credit.

The component emits `6,020` distinct novel labels. Even after numerical deduplication,

```math
\frac75
<
\frac{H(\bigcup_{q\in C}\Xi_q)}{H(C)}
<
\frac32.
```

Raw emitted support is additional recursive load, not automatic repayment.

---

## 7. Exact obstruction credit from novel labels

The seven cyclic source steps emit `63` shell occurrences representing `62` exact numerical states.

Local layer-collision and same-layer completion witnesses exclude:

| quantity | factor two | factor four |
|---|---:|---:|
| candidate domain | `950,202` | `4,986,696` |
| novel incremental invalidity | `140,352` | `398,745` |
| candidates remaining | `809,480` | `4,587,251` |

Thus novel labels create genuine future obstruction credit, but local support is far from complete.

On the `33` exact cyclic-source child states of size at most `50`, complete three-translate four-AP testing gives:

| quantity | factor two | factor four |
|---|---:|---:|
| candidate domain | `21,724` | `87,829` |
| exact invalid | `6,564` | `12,106` |
| exact valid | `15,160` | `75,723` |

Deterministic first witnesses span `33` of the `34` nonconstant affine classes for both factors. Complete one-generation affine testing is broad, but most small-state candidates remain valid.

---

## 8. Isolated canonical regeneration

The lexicographic `S_7` transition emits exactly one novel shell child

```math
X=\{16,21,26\}\subset[16,32)
```

such that

```math
X\xrightarrow[f=4]{R=1}S_1.
```

Indeed,

```math
G_1(X)
=
\{0,1,2,16,17,18,21,22,23,26,27,28\},
```

which is the canonical base pattern. The return then follows the certified path through `S_10` and its exact tail.

This regeneration is unique among all `62` cyclic-source exact states under factor-two and factor-four tests. The occurrence is also numerically isolated from every other recursive shell and terminal output in the raw lexicographic `S_7` transition.

Its normalized path charge, assigning seed persistence one, is

```math
\frac{36953}{4096}.
```

---

## 9. Exact policy dependence of regeneration

The isolated regeneration is not forced by the parent state.

The `S_7` parent has `298,606` initial coordinated actions and `30` root-forced actions. For `q=1`, the forced centers are

```math
1687866,
\quad
1781342,
\quad
1918030.
```

The lexicographic seed-producing centers

```math
1354065,
\quad
1354070,
\quad
1354075
```

are not root-forced.

More decisively, a reverse-lexicographic complete coordinated schedule has:

```text
9,180 selected actions
660-point terminal residual
2,374 middle-fiber shells
0 seed shells
0 factor-two/factor-four exact returns to S1,...,S10.
```

The lexicographic schedule has one canonical regeneration; the reverse schedule has none. Therefore

```math
\boxed{
\text{canonical regeneration is schedule-dependent on }S_7.
}
```

A parent-only potential may not assign unavoidable canonical-return cost to `S_7` from the lexicographic witness alone.

---

## 10. Active theorem: policy-aware whole-tree cost

The target remains a branching inequality

```math
\boxed{
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
\operatorname{controlled\ error},
}
```

but the child family and transition features must now carry an explicit deletion policy `pi`, unless a schedule-independent lower envelope is proved.

A valid closing route must do one of two things:

1. construct a global coordinated policy whose complete simultaneous child cost contracts treewise; or
2. prove a schedule-independent lower-envelope inequality over all complete policies.

The state must account for:

- duplicate, containment, and partial-overlap provenance;
- terminal-fiber SCC recycling;
- obstruction and completion coverage;
- regenerative and near-regenerative continuation cost;
- terminal residual error;
- bounded cross-generation reuse.

---

## 11. Approved next targets

1. Compute the complete common feature vector for lexicographic and reverse-lexicographic `S_7` transitions.
2. Compare total middle-fiber mass, overlap load, SCC spectrum, affine coverage, regeneration cost, and residual error in Bellman units.
3. Search for a constructive policy objective minimizing certified future cost rather than raw shell count.
4. Classify near-regenerations up to translation, scale, and bounded defects.
5. Prove a retention rule preserving provenance while merging exact numerical states.
6. Establish a policy-aware or minimax branching Carleson inequality.
7. Feed only proved retained-child rows into the exact rational LP harness.

---

## 12. Prohibited inferences

Do not use without materially new hypotheses:

1. universal local or fixed-window contraction;
2. pathwise summability as a whole-tree theorem;
3. replay siblings as simultaneous children;
4. raw novelty as schedule independent;
5. radius without target demand;
6. `P\Psi` as a standalone Bellman potential;
7. exact-state quotienting as a containment solution;
8. a uniform maximum-overlap constant;
9. a strict decreasing terminal-label rank;
10. latest-separation-only state;
11. unit or factor-two-contracting positive linear SCC capacity;
12. numerical output union as stored repayment;
13. local or complete one-generation affine coverage as sufficient repayment;
14. all small survivors as negligible error;
15. canonical regeneration as a parent-intrinsic feature of `S_7`;
16. one policy witness as a schedule-independent theorem;
17. the rejected depth-ten anchor reduction.

---

## 13. Reproduction

Run the complete lightweight suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Run only the transition frontier:

```bash
bash src/run_verify_transition_frontier.sh
```

Key current documents:

- `docs/certainty-ledger.md`;
- `docs/branching-reserve-lp.md`;
- `docs/s7-cyclic-scc-output-load.md`;
- `docs/s7-cyclic-scc-local-completion-credit.md`;
- `docs/s7-cyclic-scc-small-state-affine-frontier.md`;
- `docs/s7-cyclic-output-seed-regeneration.md`;
- `docs/s7-regenerative-seed-policy-dependence.md`;
- `docs/research-decision-history.md`.
