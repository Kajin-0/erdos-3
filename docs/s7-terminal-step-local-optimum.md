# Exact S7 terminal-step local optimum

## Status

Exact finite one-toggle local-optimality theorem for the policy score

```math
C_{3,1/10}(\pi)
=
T_\pi+3O_\pi+E_\pi+\frac1{10}G_\pi.
```

The candidate was found by deterministic coordinate screening. The theorem below does not rely on the screening arithmetic: the final schedule and every neighbor are independently recomputed with exact rational arithmetic.

**Verifier:** `src/verify_s7_terminal_step_local_optimum.py`.

**Certificate:** `data/s7_terminal_step_local_optimum_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
8bd93afd6ed9bcd856ff23b5eb671b2963d5aa8b8e47df19f726b38760085211
```

---

## 1. Certified policy

The policy uses the seed delay and delays the following `37` progression steps:

```text
4,5,6,19,62,71,81,141,142,161,162,365,384,400,
1526,1592,1962,5946,8190,9773,9792,10157,42638,
42643,49158,50838,87530,93471,103249,103268,103633,
135162,142634,228638,230159,333413,333797
```

Complete coordinated resolution gives:

```text
selected actions = 9323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9295
canonical regeneration = false.
```

The exact schedule SHA-256 is

```text
2a4df51cdf4c33263ff09fee2b39f3bd0e74277de2d6d2fa2904752ae14f2267.
```

---

## 2. Exact neighborhood

The deterministic one-toggle neighborhood is defined by

```math
\mathcal Q
=
\{
\text{terminal steps of the resolved policy}
\}
\cup
\{
\text{currently delayed steps}
\}.
```

It contains `59` distinct step labels. For each `q in Q`, the verifier toggles whether `q` is delayed, resolves the complete schedule again, and recomputes `C_{3,1/10}` exactly.

The result is:

```text
strictly improving toggles = 0
zero-slack toggles = 384, 323640
strictly worsening toggles = 57.
```

The smallest strict positive slack occurs at toggle `333432` and equals

```math
\boxed{
\frac{384}{111292259161}
}
```

which is approximately

```text
3.4503747421e-9.
```

Thus the certificate is numerically close at one boundary but exact: the numerator is positive.

The complete exact neighbor ranking has SHA-256

```text
46e29b7e6c688b1d58bfcd066507df04f86318d9cf9f3b0780988feb838515e7.
```

---

## 3. Improvement over the five-step-lattice winner

The previous certified finite winner was `seed_5_142`. The new local optimum satisfies

```math
\frac{1915}{1000}
<
C_{3,1/10}(\texttt{seed\_5\_142})
-
C_{3,1/10}(\pi_*)
<
\frac{1916}{1000}.
```

The exact improvement is therefore approximately

```text
1.9150599135.
```

Its exact fraction has SHA-256

```text
1a640959e7851f94963570ed1371d3242dd32719d5748afebf48a461e0b19e8b.
```

The policy also reduces the number of terminal step classes from `50` for `seed_5_142` to `28`, while keeping canonical regeneration absent.

---

## 4. Scope

This proves local optimality only for the explicitly defined `59` one-toggle neighborhood. It does not prove:

- global optimality over all delayed-step sets;
- local optimality against steps outside the terminal/delayed union;
- optimality over arbitrary complete coordinated schedules;
- validity of the continuation charge in a Bellman child sum;
- or a provenance-preserving retention quotient.

The next finite search can enlarge the candidate-step universe around this exact fixed point. The structural target remains a retained-child theorem controlling duplicates, containments, cyclic reuse, and continuation charge across generations.