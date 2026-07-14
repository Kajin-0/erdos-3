# Two-generation recursive Bellman row

## Status

Exact finite Bellman inequality for the certified `S_7` local-optimum transition, its retained-child quotient, and the first propagated retained generation.

The terminal and recursive outputs are separated. Terminal sink mass is carried in a first-appearance coordinate rather than treated as recursive load.

**Verifier:** `src/verify_two_generation_recursive_bellman_row.py`.

**Certificate:** `data/two_generation_recursive_bellman_row_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
7da70d79f271080a66d3f8ed1aa517d95bf321eb5d618822440fefdfa8504e14
```

---

## 1. Source masses

Let

```math
H_1
=
\text{harmonic mass of the 21 first-generation retained states},
```

and split the second retained generation as

```math
H_2=H_2^{\rm term}+H_2^{\rm rec}.
```

The source masses are anchored by their exact fraction hashes:

```text
H1:
29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446

H2 terminal:
b9c790f6e8be18382848adb9e66fecc01ad26ee0e2ca77e31f93326fb5d1765e

H2 recursive:
539dfbe1e345d4e6f1e0ed1c08cfedd1eba8c3f9d195fc078ae9ac0d5e391775
```

The exact recursive ratio obeys

```math
\frac{937}{1000}
<
\frac{H_2^{\rm rec}}{H_1}
<
\frac{469}{500}.
```

Equivalently,

```math
\frac{31}{500}
<
\frac{H_1-H_2^{\rm rec}}{H_1}
<
\frac{63}{1000}.
```

---

## 2. Strict recursive Bellman row

The upper bound gives

```math
H_2^{\rm rec}<\frac{469}{500}H_1.
```

Therefore

```math
\boxed{
\frac{31}{500}H_1+H_2^{\rm rec}<H_1.
}
```

This is the first strict rational Bellman contraction row for the genuinely recursive retained output of the adversarial transition.

The certified contraction credit is at least

```math
\boxed{\frac{31}{500}H_1.}
```

---

## 3. Terminal-augmented form

Let `TermSink_first` denote the first-appearance charge of the terminal output token union. Adding the same terminal coordinate to both sides preserves the strict inequality:

```math
\boxed{
\frac{31}{500}H_1
+
H_2^{\rm rec}
+
\operatorname{TermSink}_{\rm first}
<
H_1
+
\operatorname{TermSink}_{\rm first}.
}
```

This form is intentionally explicit:

- terminal sink mass is not discarded;
- terminal sink mass is not counted as a recursive child;
- recursive contraction and terminal accounting are separate proof obligations;
- the first-appearance lemma prevents duplicate terminal-token charges once a collision-sound token map is fixed.

---

## 4. Scope

The row is exact for:

```text
parent state = certified S7 local-optimum transition
first retention = exact duplicate quotient plus maximum-harmonic conflict selection
child policy = lexicographic coordinated deletion
second retention = the same global quotient rule.
```

It does not establish:

- universal contraction over all parent states;
- contraction under every schedule or retention rule;
- global soundness of the `(u,p)` terminal token;
- a bound on the global terminal-token union;
- or a complete whole-tree Bellman inequality.

The next computational test is to propagate only the 14 recursive states, apply the quotient a third time, and measure both recursive contraction and recreation of the 43 recorded terminal sink tokens.

---

## 5. Reproduction

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The runner verifies both the terminal identity ledger and this strict Bellman row. It is invoked only by the manually triggered extended workflow, not by push-gating lightweight CI.
