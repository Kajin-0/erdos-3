# Full `S_7` delay-subset policy LP

## Status

Exact finite policy-ranking theorem for all `32` subsets of

```text
{5,40,30,161,142}
```

on each of `S_1,...,S_6`, and all `64` policies on `S_7` obtained by pairing every subset with both seed-delay modes.

The score is

```math
C_{\lambda,\gamma}
=
T+\lambda O+E+\gamma G_{\rm regen}.
```

**Verifier:** `src/verify_full_s7_policy_subset_lp.py`.

**Certificate:** `data/full_s7_policy_subset_lp_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
36b93f5c52e55b7e0a182be0476881c4cd13bfbf17690261fa58c071509783c3
```

---

## 1. Exact family

The verifier caches each state's initial three-term progressions once, then resolves every policy as a complete coordinated schedule. This is important at `S_7`, where the initial state has `298,606` progression actions.

The exact policy-ranking LP contains

```text
249 rational constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

Its canonical JSONL representation has SHA-256

```text
c8986841eb8e936848d26ef769e6314052987b42a59a0f6430dfcf2bc01b4f4d
```

and the CPLEX-LP export has SHA-256

```text
45c1f50bbac2b9d50a6b3d5dd99ff874f24ef965e046e476567fa2d9b3375985.
```

---

## 2. The witness survives

The exact weight vector

```math
\boxed{
\lambda=3,
\qquad
\gamma=\frac1{10}
}
```

satisfies all `249` inequalities.

The selected representative policies are:

| state | selected policy |
|---:|---|
| `S_1` | `delay_none` |
| `S_2` | `delay_5` |
| `S_3` | `delay_5_161_142` |
| `S_4` | `delay_5_40` |
| `S_5` | `delay_5_40` |
| `S_6` | `delay_5_40` |
| `S_7` | `seed_delay_5_142` |

The first six rows preserve the previously certified subset-lattice choices. The `S_7` optimum changes.

---

## 3. New `S_7` optimum

The full `S_7` family has a unique minimum:

```text
seed_delay_5_142
```

This policy delays all step-5 and step-142 actions and also delays the three seed-producing step-1 actions. It is non-regenerative on the recorded canonical-return test.

Its transition metrics are

```text
selected actions = 9,347
residual points = 493
terminal steps = 50
middle-fiber occurrences = 9,297
canonical regeneration = false.
```

The nearest competitor is the earlier non-regenerative `seed_delay_5` policy. The exact positive gap is the strict minimum LP slack:

```text
S7:seed_delay_5_142 <= seed_delay_5
```

with SHA-256

```text
94b80ff019f4ba5a4e740db7a11dfb5be412dae92c5ad6a3f863692ce5018d38
```

and numerical value approximately

```text
0.001501099630423487.
```

The margin is small. The policy choice remains sensitive to family enlargement.

---

## 4. Interpretation

The two-coordinate witness survives exact enumeration of the complete five-step subset lattice on all seven recorded states. This removes the previous qualification that `S_7` was represented only by a 13-policy hand-selected family.

It still does not establish:

- optimality over arbitrary priority functions or all complete schedules;
- that the recorded continuation charge is a legitimate retained-child potential;
- a provenance-preserving quotient for overlapping raw shells;
- or a whole-tree Bellman inequality.

The next structural target remains the retention problem. Further policy search is useful only if it probes priority rules outside this five-step subset family or produces a conflicting half-space that identifies a missing coordinate.
