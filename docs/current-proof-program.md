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

## 5. Regeneration and policy coordinates

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

The current finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

where:

```text
T = terminal-step harmonic mass
O = middle-fiber occurrence/provenance mass
E = normalized terminal residual error
G = certified regenerative continuation charge.
```

The exact witness used throughout the current finite frontier is

```math
\boxed{
\lambda=3,
\qquad
\gamma=\frac1{10}.
}
```

The continuation coordinate is necessary: `T+3O+E` alone prefers a policy retaining the canonical return. Favorable local priority changes are not greedily composable.

---

## 6. Full five-step policy subset lattice through S7

The delayed-step universe is

```text
{5,40,30,161,142}.
```

The exact finite family contains:

- all `32` delayed-step subsets on each of `S_1,...,S_7`;
- all `32` seed-delayed versions on `S_7`;
- reverse lexicographic deletion on `S_7`.

Every chosen-policy comparison is exported as

```math
\Delta O\,\lambda
+
\Delta G\,\gamma
\ge
-(\Delta T+\Delta E).
```

The resulting exact policy-ranking LP contains

```text
250 rational constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

The rational LP harness verifies

```math
\boxed{
(\lambda,\gamma)=\left(3,\frac1{10}\right)
}
```

against every row.

Representative selected policies are:

| state | selected policy |
|---:|---|
| `S_1` | `plain_none`, representative of a complete tie |
| `S_2` | `plain_5`, representative of an eight-policy tie |
| `S_3` | `plain_5_161_142`, unique |
| `S_4` | `plain_5_40`, modulo inactive-step ties |
| `S_5` | `plain_5_40`, modulo inactive-step ties |
| `S_6` | `plain_5_40`, modulo inactive-step ties |
| `S_7` | `seed_5_142`, unique |

The `S_7` winner is non-regenerative and has

```text
selected actions = 9347
terminal residual = 493
terminal step classes = 50
middle-fiber occurrences = 9297.
```

The previous finite winner `seed_5` is now the runner-up. The exact positive gap satisfies

```math
\frac3{2000}
<
C_{3,1/10}(\texttt{seed\_5})
-
C_{3,1/10}(\texttt{seed\_5\_142})
<
\frac{751}{500000}.
```

Thus the gap is approximately `0.0015010996`. This is the smallest positive slack in the 250-row system.

Primary references:

- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/two-coordinate-policy-family.md`.

This completes the explicit five-step subset lattice through `S_7`. It does not establish global optimality over arbitrary delayed steps or over all complete coordinated schedules.

---

## 7. Active theorem

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

The finite policy score now has a stable exact witness on a substantial deterministic family, but a retention theorem is still required before raw shell or path charges can enter a Bellman child sum.

The active bottleneck has two parts:

1. enlarge the delayed-step universe around `seed_5_142` with a deterministic exact neighborhood search;
2. prove a provenance-preserving retained-child quotient that bounds duplicate, containment, and cyclic reuse across generations.

---

## 8. Approved next targets

1. Compute exact one-step add/remove neighborhoods around `seed_5_142` using a deterministic candidate-step universe.
2. Add every new policy comparison to the exact policy LP and monitor the feasible cone.
3. Extract the first exact infeasible subsystem if the two-coordinate cone collapses.
4. Add the coordinate identified by that subsystem.
5. Prove a provenance-preserving retention quotient.
6. Export the first legitimate retained-child Bellman row.
7. Establish a policy-aware or minimax branching Carleson inequality.

---

## 9. Stop list

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
- the earlier `S_3` `{5,40}` policy remains optimal after family expansion;
- the earlier `S_7` `seed_5` policy remains optimal after subset-lattice expansion;
- the five-step lattice represents all possible delayed-step policies;
- policy-LP feasibility implies Bellman-LP feasibility;
- adding the recorded path charge is justified without retention;
- the tested policy family is globally optimal;
- one finite witness proves an all-policy theorem.

---

## 10. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Complete extended suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Transition frontier without the full five-step `S_7` lattice:

```bash
bash src/run_verify_transition_frontier.sh
```

Standalone full subset-lattice certificate:

```bash
python3 src/run_exact_python.py \
  src/verify_policy_subset_lattice_s1_s7.py \
  /tmp/policy_subset_lattice_s1_s7_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/two-coordinate-policy-family.md`;
- `docs/s7-cyclic-scc-output-load.md`;
- `docs/s7-regenerative-seed-policy-dependence.md`;
- `docs/branching-reserve-lp.md`.
