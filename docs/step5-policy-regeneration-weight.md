# Step-5 policy and the missing regeneration coordinate

## Status

Exact finite policy-ranking theorem on the recorded states `S_1,...,S_7`.

Define

```math
C_3(\pi)=T_\pi+3O_\pi+E_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, and `E` is normalized terminal-residual error.

**Verifier:** `src/verify_step5_policy_regeneration_weight.py`.

**Certificate:** `data/step5_policy_regeneration_weight_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
4e64334bb09a12e0c1e764f59bbe5a6c71d477f631539cfcfceccc453cca7928
```

---

## 1. Uniform step-5 delay rule

Let `pi_5` be the complete coordinated schedule that delays every action with progression step `5` until after every other action, preserving lexicographic order inside both priority classes.

Exact recomputation gives

```math
C_3(\pi_5)=C_3(\pi_{\rm lex})
```

on `S_1`, and

```math
C_3(\pi_5)<C_3(\pi_{\rm lex})
```

on every `S_2,...,S_7`.

| state | selected | residual | terminal steps | fiber occurrences | score comparison |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 6 | 6 | 2 | 4 | tie |
| `S_2` | 25 | 14 | 7 | 18 | lower |
| `S_3` | 90 | 30 | 14 | 76 | lower |
| `S_4` | 302 | 61 | 22 | 280 | lower |
| `S_5` | 970 | 122 | 27 | 943 | lower |
| `S_6` | 3033 | 246 | 29 | 3004 | lower |
| `S_7` | 9348 | 492 | 41 | 9307 | lower |

Thus one uniform local priority rule improves the occurrence-weight score across the full recorded frontier.

---

## 2. The occurrence score still chooses regeneration

At `S_7`, `pi_5` retains exactly one canonical regeneration:

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1.
```

The step-5 policy schedule hash is

```text
2394f4eb375c0a9c61eb3ee1de27d48e1119807246ce78d90f8acff1c6062019
```

Now define the hybrid policy `pi_h` by delaying:

1. every step-5 action; and
2. the three unforced `q=1` seed-producing actions.

The hybrid has no canonical regeneration. However,

```math
C_3(\pi_h)-C_3(\pi_5)>0.
```

Therefore the raw score `T+3O+E` prefers a policy with a known long regenerative continuation over a non-regenerative alternative. The common occurrence-weight cone from CL-058 is real but incomplete.

---

## 3. Exact regeneration penalty

Let

```math
G=\frac{36953}{4096}
```

be the certified path charge of the isolated regenerative child, and refine the score to

```math
C_{3,\gamma}(\pi)
=
T_\pi+3O_\pi+E_\pi+\gamma G_\pi,
```

where `G_pi=G` when the recorded canonical seed is present and `0` when absent.

The hybrid beats the step-5 policy exactly when

```math
\gamma>\gamma_*,
```

with

```math
\boxed{
\frac{57}{1000}<\gamma_*<\frac{29}{500}
}.
```

Numerically,

```text
0.057 < gamma_* < 0.058.
```

The rational witness

```math
\boxed{\gamma=\frac1{16}}
```

makes the non-regenerative hybrid cheaper than both `pi_5` and lexicographic deletion at `S_7`.

---

## 4. Consequence

The first common policy score must include at least one continuation-sensitive coordinate. Terminal mass, occurrence mass, and terminal residual error do not distinguish a low one-generation score from a recursively expensive regenerative return.

This does not yet prove that the path charge can be inserted directly into a Bellman potential. The missing retention theorem must still establish:

- whether the regenerative shell is retained;
- how its provenance is counted;
- how repeated returns are charged;
- and how continuation charge interacts with containment and overlap.

The next exact target is to test the refined score on additional deterministic policies and determine whether one fixed pair `(lambda,gamma)` survives the larger policy half-space system.
