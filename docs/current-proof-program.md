# Current proof program: policy-aware whole-tree packing

## Status

This is the authoritative overview of the active program for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Exact theorem status is tracked in `docs/certainty-ledger.md`.

---

## 1. Foundation

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

reciprocal divergence is equivalent up to constants to `sum_j alpha_j=infinity`.

Coordinated side-anchor deletion and the minimum-translation backbone give

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

Every recursive output is resolved into standard dyadic shells. These results control local moments, not the full branching reciprocal mass.

---

## 2. Exact benchmark and contaminated obstruction

The uncontaminated equal-translate model is summable:

```math
P_h\alpha_h\le C_0(3/4)^h.
```

The certified contaminated path has scale word

```text
4,8,4,4,8,4,8,8,8
```

through `S_10`, and `W_5/W_1=91/32>1`. Universal local and fixed-window contraction claims are false.

For exact scale factor `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right),
```

with cheap-step debt

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

---

## 3. Finished state-specific theorem

At `S_10`, inheritance, lifted completion support, and direct rectangle transport exclude every factor-two and factor-four candidate:

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The exact transport closure margin is only `5`. Every valid exact factor-eight child has a certified summable exact tail. This closes the recorded state, not the full deletion tree.

---

## 4. Raw simultaneous transition frontier

The fixed lexicographic exporter records complete raw occurrence families before a retention quotient.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

Replay siblings are alternative choices, not simultaneous Bellman children.

---

## 5. Cyclic output obstruction

At `S_7`, the terminal-fiber graph contains the cyclic component

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

Its internal adjacency matrix satisfies

```math
\frac{23}{9}<\rho(A)<\frac83.
```

The component emits `6,020` distinct novel labels. Even after numerical deduplication, its output/input harmonic ratio exceeds `7/5`. Raw output is recursive load, not stored repayment.

---

## 6. Obstruction credit is real but incomplete

Across the `62` exact cyclic-source shell states, novel labels create local collision/completion invalidity for

```text
140,352 of 950,202 factor-two candidates
398,745 of 4,986,696 factor-four candidates.
```

On the `33` exact states of size at most `50`, complete three-translate four-AP testing still leaves

```text
15,160 of 21,724 factor-two candidates
75,723 of 87,829 factor-four candidates.
```

Deterministic first witnesses span `33` of the `34` nonconstant affine classes. Complete one-generation affine testing is broad but insufficient.

---

## 7. Isolated canonical regeneration

Under lexicographic deletion, the novel isolated child

```math
X=\{16,21,26\}\subset[16,32)
```

satisfies

```math
X\xrightarrow[f=4]{R=1}S_1.
```

It is the unique exact factor-two/factor-four return from the `62` cyclic-source states to any canonical `S_1,...,S_10`, and it is disjoint from every other raw recursive shell and terminal output in the lexicographic `S_7` transition.

Its certified path charge, assigning seed persistence one, is `36953/4096`.

---

## 8. Regeneration is policy-dependent

The seed-producing `q=1` centers are not root-forced. A reverse-lexicographic complete coordinated schedule has

```text
0 seed shells
0 exact factor-two/factor-four returns to S1,...,S10.
```

Therefore canonical regeneration is not a parent-intrinsic feature of `S_7`.

---

## 9. Avoiding regeneration is not a sufficient policy objective

The reverse policy avoids the canonical return but has a much larger raw transition:

| coordinate | lexicographic | reverse lexicographic |
|---|---:|---:|
| terminal steps | `25` | `2,252` |
| middle-fiber shells | `124` | `2,374` |
| largest SCC | `7` | `286` |
| maximum label multiplicity | `15` | `160` |
| residual error | `15/256` | `165/2048` |

Exact harmonic comparisons give

```math
75
<
\frac{M_{\rm occ}^{\rm rev}}{M_{\rm occ}^{\rm lex}}
<
76,
```

and

```math
744
<
\frac{M_{\rm dup}^{\rm rev}}{M_{\rm dup}^{\rm lex}}
<
745.
```

Thus a policy must be scored by complete transition cost, not by canonical-return count or raw label count.

---

## 10. Active theorem

The required object is now explicitly policy-aware:

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
\operatorname{controlled\ error}.
}
```

A closing route must either:

1. construct a global coordinated policy `pi` with controlled complete child cost; or
2. prove a schedule-independent lower-envelope inequality over all complete policies.

The state must include provenance overlap, SCC recycling, obstruction coverage, regenerative continuation cost, and residual error.

---

## 11. Approved next targets

1. Define exact Bellman-unit policy coordinates constrained by the lex/reverse tradeoff.
2. Reject any coordinate system that ranks the reverse transition below lexicographic despite its exact load explosion.
3. Compare additional deterministic policies on `S_1` through `S_7`.
4. Search for a stable constructive policy objective.
5. Prove a provenance-preserving retention quotient.
6. Establish a policy-aware or minimax branching Carleson inequality.
7. Feed only proved retained-child rows into the exact rational LP harness.

---

## 12. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- raw novelty is schedule-independent;
- one-generation affine coverage repays cyclic output;
- canonical regeneration is forced by `S_7`;
- avoiding regeneration makes a policy cheaper;
- raw occurrence count ranks policies correctly;
- one policy witness proves an all-policy theorem.

---

## 13. Reproduction

```bash
bash src/run_verify_transport_reserve.sh
```

Transition-only suite:

```bash
bash src/run_verify_transition_frontier.sh
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/s7-cyclic-scc-output-load.md`;
- `docs/s7-cyclic-scc-local-completion-credit.md`;
- `docs/s7-cyclic-scc-small-state-affine-frontier.md`;
- `docs/s7-cyclic-output-seed-regeneration.md`;
- `docs/s7-regenerative-seed-policy-dependence.md`;
- `docs/s7-policy-transition-tradeoff.md`;
- `docs/branching-reserve-lp.md`.
