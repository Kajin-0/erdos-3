# Expanded policy subset-lattice LP

## Status

Exact finite feasibility theorem for all `32` delay subsets of

```text
{5,40,30,161,142}
```

on each of `S_1,...,S_6`, together with the current `13`-policy `S_7` family.

The score remains

```math
C_{\lambda,\gamma}
=
T+\lambda O+E+\gamma G_{\rm regen}.
```

**Verifier:** `src/verify_expanded_policy_subset_lp.py`.

**Certificate:** `data/expanded_policy_subset_lp_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
296e171145d54aed0425ffd14ea2065096106112c45094f0044e5962e3fe1829
```

---

## 1. Expanded exact system

For `S_1` through `S_6`, every subset of the five candidate delayed steps is resolved as a complete coordinated schedule. The `S_7` side retains the previously certified family containing lexicographic, reverse, cumulative-step, and seed-delayed hybrid policies.

The expanded policy-ranking LP contains

```text
198 exact rational constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

The canonical JSONL representation is `417,334` bytes with SHA-256

```text
9181fd97362560cdb10001063df140b88465740f025620c3d2c4c92650d2d79f
```

The CPLEX-LP export is `464,574` bytes, `206` lines, with SHA-256

```text
e1b0a00c2472110c9133cc79a844256211b5e0ed0e27c04acfc8f2a236026936
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

satisfies every one of the `198` inequalities.

The selected policies are:

| state | selected policy |
|---:|---|
| `S_1` | `delay_none` |
| `S_2` | `delay_5` |
| `S_3` | `delay_5_161_142` |
| `S_4` | `delay_5_40` |
| `S_5` | `delay_5_40` |
| `S_6` | `delay_5_40` |
| `S_7` | non-regenerative `hybrid5` |

The chosen name represents one member of a tie when multiple subsets generate the same score and transition coordinates.

---

## 3. The `S_3` policy changes

The smaller policy family selected `delay_5_40` on `S_3`. Full subset enumeration finds the unique better policy

```text
delay_5_161_142.
```

Its nearest competitor is `delay_5_40`. The exact positive score gap has SHA-256

```text
f63047846da4fbe9897d75156ec8ec2386709bc6a64d40c9305e7a03f7e2358c
```

and equals approximately

```text
0.0226102848.
```

Thus the fixed witness remains feasible, but the policy selected by that witness is sensitive to family expansion.

---

## 4. Interpretation

This is stronger than the earlier `60`-row policy LP because it exhausts the complete five-step subset lattice on six recorded states. It shows that the two-coordinate witness survives a substantial adversarial family expansion.

It still does not establish:

- global optimality over all complete schedules;
- stability under arbitrary delayed-step sets;
- a retention quotient for simultaneous raw children;
- or a whole-tree Bellman inequality.

The next finite test should expand `S_7` using a tractable policy-search method rather than exact enumeration of every subset, whose exact rational recomputation becomes expensive. The structural target remains a provenance-preserving retained-child theorem.
