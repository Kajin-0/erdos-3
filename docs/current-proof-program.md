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

## 4. Raw transition and retention obstruction

The lexicographic raw transition frontier is certified through `S_7`.

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

At `S_7`, the terminal-fiber graph contains

```math
C=\{1,5,61,303,1597,8195,323640\},
```

with

```math
\frac{23}{9}<\rho(A)<\frac83.
```

The component emits `6,020` distinct novel labels, and its numerically deduplicated output/input harmonic ratio exceeds `7/5`. Local and affine obstruction export is substantial but incomplete. A provenance-preserving retention quotient remains missing.

---

## 5. Regeneration and policy dependence

Under lexicographic deletion, the isolated child

```math
X=\{16,21,26\}\subset[16,32)
```

satisfies

```math
X\xrightarrow[f=4]{R=1}S_1.
```

Its recorded continuation charge is

```math
G=\frac{36953}{4096}.
```

The seed-producing actions are not root-forced. Reverse lexicographic deletion avoids the return but creates severe terminal, cyclic, and duplicate load. Avoiding a recognizable descendant is not a sufficient policy objective.

---

## 6. Occurrence and continuation coordinates

For

```math
C_\lambda(\pi)=T_\pi+\lambda O_\pi+E_\pi,
```

the tested lexicographic, reverse, and delayed-seed policies admit the common subcone

```math
\boxed{
\frac{477}{200}<\lambda<\frac{260}{63}
}.
```

The witness `lambda=3` is exact.

A uniform policy `pi_5` delaying all step-5 actions ties lexicographic deletion on `S_1` and lowers `C_3` on every `S_2,...,S_7`, but retains the canonical return. Therefore occurrence cost alone is insufficient.

Introduce

```math
C_{3,\gamma}(\pi)
=
T_\pi+3O_\pi+E_\pi+\gamma G_\pi.
```

The pairwise `pi_5` versus non-regenerative hybrid comparison has threshold

```math
0.057<\gamma_5<0.058,
```

but that threshold is not stable under policy-family enlargement.

---

## 7. Current finite policy family

The enlarged family contains:

```text
lexicographic
reverse lexicographic
single-step delays 30, 40, 142, 161
step5
step540
step54030
S7 seed-delayed hybrids of cumulative policies.
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

The stronger regenerative `step540` policy raises the active continuation threshold to

```math
\frac{837}{10000}
<
\gamma_{540}
<
\frac{419}{5000}.
```

Thus `gamma=1/16` fails after family enlargement, while `gamma=1/10` succeeds.

Delaying step `30` alone improves `C_3` on `S_2,...,S_7`, but adding the same delay after steps `5` and `40` worsens `C_3` on every one of those states. Favorable local policy changes are not greedily composable.

Primary references:

- `docs/two-coordinate-policy-family.md`;
- `docs/step5-policy-regeneration-weight.md`;
- `docs/policy-occurrence-cone-s1-s7.md`.

---

## 8. Exact policy half-space LP

Every current chosen-policy comparison is exported as

```math
\Delta O\,\lambda
+
\Delta G\,\gamma
\ge
-(\Delta T+\Delta E).
```

The exact finite system contains

```text
60 constraints
2 features: lambda, gamma.
```

The existing rational LP harness verifies

```math
(\lambda,\gamma)=\left(3,\frac1{10}\right)
```

exactly. The only zero-slack constraints are the expected `S_1` policy ties and the `S_2` `step5/step540` tie. The active `S_7` continuation boundary is `hybrid5 <= step540`.

This completes the finite policy-ranking LP export. It is **not** the branching Bellman LP because the rows compare complete policies on recorded parents and do not yet encode retained simultaneous children.

**Primary reference:** `docs/policy-halfspace-lp.md`.

---

## 9. Active theorem

The required whole-tree object remains

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

The finite policy score currently needs at least

```text
terminal mass
recursive occurrence/provenance load
terminal residual error
regenerative continuation charge.
```

A retention theorem is still required before raw shell or path charges can enter a Bellman child sum.

---

## 10. Approved next targets

1. Add further deterministic priority families to the exact policy LP.
2. Extract the first exact infeasible subsystem if the two-coordinate cone collapses.
3. Add the coordinate identified by that subsystem.
4. Prove a provenance-preserving retention quotient.
5. Export the first legitimate retained-child Bellman row.
6. Establish a policy-aware or minimax branching Carleson inequality.

---

## 11. Stop list

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
- policy-LP feasibility implies Bellman-LP feasibility;
- adding the recorded path charge is justified without retention;
- the tested policy family is globally optimal;
- one finite witness proves an all-policy theorem.

---

## 12. Reproduction

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
- `docs/policy-halfspace-lp.md`;
- `docs/branching-reserve-lp.md`.
