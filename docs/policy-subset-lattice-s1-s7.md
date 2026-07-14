# Policy subset-lattice LP through S7

## Status

Exact finite policy-ranking theorem for all `32` subsets of delayed steps

```text
{5,40,30,161,142}
```

on each of `S_1,...,S_6`, and all `32` subsets on `S_7` both with and without the three-action seed delay. Reverse lexicographic deletion is also retained as an `S_7` alternative.

The score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

with exact witness

```math
\boxed{\lambda=3,\qquad \gamma=\frac1{10}}.
```

**Verifier:** `src/verify_policy_subset_lattice_s1_s7.py`.

**Certificate:** `data/policy_subset_lattice_s1_s7_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
85667125996eb7d3f33d6bdf6ddd78ad1cefbad8c229d57402711e20d17a2287
```

---

## 1. Exact finite family

The policy family contains:

- `32` plain delayed-step subsets on each of `S_1,...,S_7`;
- `32` seed-delayed versions on `S_7`;
- reverse lexicographic deletion on `S_7`.

The resulting exact policy-ranking LP has

```text
250 rational half-space constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

The canonical JSONL representation has SHA-256

```text
e439db76aef083e35239386c040d9fca934508d53a383836f4c78efa74ea85af
```

and the CPLEX-LP export has SHA-256

```text
f3775bccfcfea11783e9777fa5b402f6f86b4d58b431b700509373cd35ef8f70.
```

---

## 2. Selected policies

At `(lambda,gamma)=(3,1/10)`, representative selected policies are:

| state | selected policy |
|---:|---|
| `S_1` | `plain_none`, representative of a complete tie |
| `S_2` | `plain_5`, representative of an eight-policy tie |
| `S_3` | `plain_5_161_142`, unique |
| `S_4` | `plain_5_40`, modulo inactive-step ties |
| `S_5` | `plain_5_40`, modulo inactive-step ties |
| `S_6` | `plain_5_40`, modulo inactive-step ties |
| `S_7` | `seed_5_142`, unique |

The `S_7` policy delays every step-5 and step-142 action and delays the three unforced seed-producing step-1 actions. It has

```text
selected actions = 9347
terminal residual = 493
terminal step classes = 50
middle-fiber occurrences = 9297
canonical regeneration = false.
```

---

## 3. The S7 winner changes

The previous finite family selected `seed_5`, also called `hybrid5`. Exhausting the five-step subset lattice on `S_7` finds the uniquely cheaper non-regenerative policy

```text
seed_5_142.
```

Its runner-up is `seed_5`. The exact positive score gap satisfies

```math
\frac3{2000}
<
C_{3,1/10}(\texttt{seed\_5})
-
C_{3,1/10}(\texttt{seed\_5\_142})
<
\frac{751}{500000},
```

so the gap is approximately

```text
0.0015010996.
```

The exact gap has SHA-256

```text
94b80ff019f4ba5a4e740db7a11dfb5be412dae92c5ad6a3f863692ce5018d38.
```

This is the smallest positive slack in the full 250-row system.

---

## 4. Interpretation

The fixed two-coordinate witness survives complete enumeration of this explicit policy lattice on all recorded states through `S_7`. It is materially stronger than the earlier 198-row result because the `S_7` side is now exhaustive for the selected five delayed steps and the seed-delay switch.

It still does not establish:

- optimality over arbitrary delayed progression steps;
- optimality over all complete coordinated schedules;
- validity of the recorded continuation charge without a retention theorem;
- a provenance-preserving simultaneous-child quotient;
- or a whole-tree Bellman inequality.

The next finite policy search should enlarge the delayed-step universe by an exact deterministic neighborhood test around `seed_5_142`. The structural theorem target remains a provenance-preserving retained-child inequality.