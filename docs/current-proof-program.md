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

and

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every recursive output is resolved into standard dyadic shells. These are local accounting statements, not a whole-tree reciprocal-mass theorem.

---

## 2. Exact benchmark and contaminated obstruction

The uncontaminated equal-translate model is summable:

```math
P_h\alpha_h\le C_0(3/4)^h.
```

The certified contaminated path reaches `S_10` with scale word

```text
4,8,4,4,8,4,8,8,8
```

and

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Universal local contraction, fixed short-window contraction, and universal two-generation recovery are false.

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

The exact transport closure margin is `5`. Every valid exact factor-eight child has a certified summable exact tail. This closes the recorded state, not the full deletion tree.

---

## 4. Raw simultaneous transition frontier

The lexicographic exporter records complete raw occurrence families before any retention quotient.

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

## 5. Cyclic output and retention obstruction

At `S_7`, the terminal-fiber graph contains

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

Its internal adjacency matrix satisfies

```math
\frac{23}{9}<\rho(A)<\frac83.
```

The component emits `6,020` distinct novel labels. Even after numerical deduplication, its output/input harmonic ratio exceeds `7/5`. Raw output is recursive load, not stored repayment.

Local and affine obstruction export is substantial but incomplete:

```text
140,352 of 950,202 factor-two candidates removed locally
398,745 of 4,986,696 factor-four candidates removed locally
```

On the `33` exact cyclic-source states of size at most `50`, complete one-generation four-AP testing still leaves

```text
15,160 of 21,724 factor-two candidates
75,723 of 87,829 factor-four candidates.
```

A provenance-preserving retention quotient remains missing.

---

## 6. Regeneration and policy dependence

Under lexicographic deletion, the isolated child

```math
X=\{16,21,26\}\subset[16,32)
```

satisfies

```math
X\xrightarrow[f=4]{R=1}S_1.
```

It is the unique exact factor-two/factor-four return from the `62` cyclic-source states to any canonical `S_1,...,S_10`. Its recorded path charge is

```math
G=\frac{36953}{4096}.
```

The seed-producing actions are not root-forced. Reverse lexicographic deletion avoids the return but creates a severe load explosion:

| coordinate | lexicographic | reverse lexicographic |
|---|---:|---:|
| terminal steps | `25` | `2,252` |
| middle-fiber shells | `124` | `2,374` |
| largest SCC | `7` | `286` |
| maximum label multiplicity | `15` | `160` |
| residual error | `15/256` | `165/2048` |

Avoiding a recognizable descendant is not a sufficient policy objective.

---

## 7. First occurrence-weight cone

For

```math
C_\lambda(\pi)=T_\pi+\lambda O_\pi+E_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, and `E` is normalized terminal-residual error, the targeted delayed-seed policy beats lexicographic deletion at `S_7` exactly when

```math
\lambda>\lambda_*;
\qquad
\frac{298}{125}<\lambda_*<\frac{477}{200}.
```

On `S_1`, lexicographic deletion beats reverse deletion exactly when

```math
\lambda<\frac{260}{63}.
```

On every `S_2,...,S_6`, reverse deletion has larger terminal mass, larger occurrence mass, and no smaller residual error.

Therefore the tested family has the nonempty common subcone

```math
\boxed{
\frac{477}{200}<\lambda<\frac{260}{63}
}.
```

The exact witness is

```math
\boxed{\lambda=3}.
```

**Primary reference:** `docs/policy-occurrence-cone-s1-s7.md`.

---

## 8. Uniform step-5 policy exposes continuation cost

Let `pi_5` delay every progression-step-5 action and preserve lexicographic order otherwise.

Exact recomputation gives

```math
C_3(\pi_5)=C_3(\pi_{\rm lex})
```

on `S_1`, and

```math
C_3(\pi_5)<C_3(\pi_{\rm lex})
```

on every `S_2,...,S_7`.

At `S_7`, `pi_5` retains the isolated canonical return. A hybrid delaying both step `5` and the three seed-producing `q=1` actions removes regeneration but has higher raw `C_3`.

Introduce

```math
C_{3,\gamma}(\pi)
=
T_\pi+3O_\pi+E_\pi+\gamma G_\pi.
```

In the pairwise `pi_5` versus hybrid comparison, the hybrid wins once

```math
\gamma>\gamma_5,
\qquad
\frac{57}{1000}<\gamma_5<\frac{29}{500}.
```

The witness `gamma=1/16` is valid only for that pairwise comparison.

**Primary reference:** `docs/step5-policy-regeneration-weight.md`.

---

## 9. Two-coordinate finite policy family

The policy family was enlarged to include:

```text
lexicographic
reverse lexicographic
single-step delays 30, 40, 142, 161
step5
step540
step54030
S7 seed-delayed hybrids of the cumulative policies.
```

At

```math
\boxed{
\lambda=3,
\qquad
\gamma=\frac1{10},
}
```

the exact winners are:

| state | winner |
|---:|---|
| `S_1` | all tested non-reverse policies tie |
| `S_2` | `step5`, `step540` tie |
| `S_3` | `step540` |
| `S_4` | `step540` |
| `S_5` | `step540` |
| `S_6` | `step540` |
| `S_7` | non-regenerative `hybrid5` |

The stronger regenerative `step540` policy tightens the continuation constraint. The hybrid beats it exactly when

```math
\gamma>\gamma_{540},
\qquad
\frac{837}{10000}<\gamma_{540}<\frac{419}{5000}.
```

Thus

```text
gamma = 1/16 fails
gamma = 1/10 succeeds.
```

This is the first stable finite two-coordinate witness for the present policy family.

**Primary reference:** `docs/two-coordinate-policy-family.md`.

---

## 10. Policy improvements are not composable

Delaying step `30` alone improves `C_3` relative to lexicographic deletion on every `S_2,...,S_7`.

After steps `5` and `40` are already delayed, the same modification reverses sign:

```math
C_3(\pi_{5,40,30})
>
C_3(\pi_{5,40})
```

on every `S_2,...,S_7`.

Therefore independently favorable local policy moves cannot be greedily combined. The policy objective is interaction-sensitive, and every candidate priority set must be recomputed as a complete schedule or controlled by a new structural theorem.

---

## 11. Active theorem

The required object remains policy-aware:

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

The current finite policy score needs at least

```text
terminal mass
recursive occurrence/provenance load
terminal residual error
regenerative continuation charge.
```

A retention theorem is still required before raw shell or path charges can enter a Bellman child sum.

---

## 12. Approved next targets

1. Export all current policy comparisons as exact rational half-spaces in `(lambda,gamma)`.
2. Intersect them in the branching-reserve LP harness.
3. Add additional deterministic priority families and update the feasible cone.
4. Extract the first exact infeasible subsystem if the two-coordinate cone collapses.
5. Add the coordinate identified by that subsystem.
6. Prove a provenance-preserving retention quotient.
7. Establish a policy-aware or minimax branching Carleson inequality.

---

## 13. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- raw novelty is schedule-independent;
- one-generation affine coverage repays cyclic output;
- canonical regeneration is forced by `S_7`;
- avoiding regeneration makes a policy cheaper;
- raw occurrence or distinct-label count ranks policies correctly;
- a nonempty occurrence-weight cone makes continuation cost unnecessary;
- `gamma=1/16` survives enlarged policy families;
- locally favorable policy moves compose greedily;
- adding the recorded path charge is justified without retention;
- the tested policy family is globally optimal;
- one finite witness proves an all-policy theorem.

---

## 14. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Complete extended suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Transition and policy frontier only:

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
- `docs/s7-delayed-seed-policy.md`;
- `docs/s7-policy-weight-regions.md`;
- `docs/policy-occurrence-cone-s1-s7.md`;
- `docs/step5-policy-regeneration-weight.md`;
- `docs/two-coordinate-policy-family.md`;
- `docs/branching-reserve-lp.md`.
