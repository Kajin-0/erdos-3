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

Every recursive output is resolved into standard dyadic shells. These statements control local moments, not the full branching reciprocal mass.

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

and satisfies

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

Local and affine obstruction export is real but incomplete:

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

## 7. Targeted delayed-seed policy

Delay only the three unforced lexicographic `q=1` actions that produce the regenerative seed. The delayed actions become stale.

| coordinate | lexicographic | delayed-seed |
|---|---:|---:|
| terminal steps | `25` | `31` |
| middle-fiber shells | `124` | `123` |
| maximum multiplicity | `15` | `14` |
| residual error | `240/4096` | `241/4096` |

Occurrence mass falls by about `7.3%`, duplicate mass by about `30.3%`, and residual error rises by exactly `1/4096`. Terminal-step mass rises.

For

```math
C_\lambda(\pi)=T_\pi+\lambda O_\pi+E_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, and `E` is normalized residual error, the delayed policy beats lexicographic deletion at `S_7` exactly when

```math
\lambda>\lambda_*,
\qquad
\frac{298}{125}<\lambda_*<\frac{477}{200}.
```

---

## 8. First common policy-weight cone

The same score has now been tested on the recorded lexicographic and reverse schedules through `S_6`.

On `S_1`, reverse deletion has lower occurrence mass but higher terminal mass. Exact arithmetic gives

```math
C_\lambda(\mathrm{reverse})
>
C_\lambda(\mathrm{lex})
\quad\Longleftrightarrow\quad
\lambda<\frac{260}{63}.
```

At `lambda=3`, the exact `S_1` score gap is

```math
\frac{71}{624}>0.
```

On every `S_2,...,S_6`, reverse deletion has larger terminal mass, larger occurrence mass, and no smaller residual error, so lexicographic deletion is cheaper for every nonnegative `lambda`.

Combining these inequalities with the `S_7` delayed-policy threshold gives the certified nonempty subcone

```math
\boxed{
\frac{477}{200}<\lambda<\frac{260}{63}
}.
```

The rational witness

```math
\boxed{\lambda=3}
```

selects the tested policy family

```text
S1-S6: lexicographic
S7:    delayed-seed
```

and rejects reverse lexicographic deletion on every `S_1,...,S_7` comparison.

This is an exact finite policy-ranking theorem. It does not prove that `C_lambda` is a retained-child Bellman potential or globally optimal over all complete schedules.

**Primary reference:** `docs/policy-occurrence-cone-s1-s7.md`.

---

## 9. Active theorem

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

A closing route must either:

1. construct a global coordinated policy with controlled complete child cost; or
2. prove a schedule-independent lower-envelope inequality over all complete policies.

The state must include provenance overlap, SCC recycling, obstruction coverage, regenerative continuation cost, and residual error.

---

## 10. Approved next targets

1. Generate additional deterministic local policies on `S_1,...,S_7`.
2. Convert every comparison into an exact rational half-space.
3. Intersect the half-spaces in the exact branching-reserve LP harness.
4. Extract the first infeasible subsystem if the common cone collapses.
5. Add the missing coordinate identified by that subsystem.
6. Prove a provenance-preserving retention quotient before treating raw shells as Bellman children.
7. Establish a policy-aware or minimax branching Carleson inequality.

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
- the delayed-seed Pareto improvement is already a whole-tree contraction;
- one finite weight interval validates the raw score globally;
- the tested policy family is globally optimal;
- one policy witness proves an all-policy theorem.

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
- `docs/branching-reserve-lp.md`.
