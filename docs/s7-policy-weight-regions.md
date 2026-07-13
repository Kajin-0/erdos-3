# Exact weight regions for the `S_7` delayed-seed policy

## Status

Exact finite comparison of the lexicographic and delayed-seed complete
coordinated schedules on `S_7`.

The delayed policy reduces recursive occurrence, union, duplicate, and average
multiplicity, but increases terminal-step mass and terminal-residual error. This
note gives the exact coefficient thresholds at which a linear policy score
changes preference.

These thresholds constrain candidate policy objectives. They do not prove that
the raw coordinates are valid retained-child Bellman potentials.

**Verifier:** `src/verify_s7_policy_weight_regions.py`.

**Certificate:** `data/s7_policy_weight_regions_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
97f45313494b16f022f47f87ef1c788962011c76c349dc88faef1ba8e1838693
```

---

## 1. Notation

Let

```math
T=\text{terminal-step harmonic mass},
```

```math
O=\text{middle-fiber occurrence mass},
```

```math
U=\text{distinct middle-fiber union mass},
```

```math
D=O-U=\text{duplicate mass},
```

and let `E` be the normalized terminal-residual error.

Write `L` for the lexicographic policy and `P` for the delayed-seed policy. The
exact certified signs are

```math
T_P-T_L>0,
\qquad
E_P-E_L=\frac1{4096}>0,
```

while

```math
O_L-O_P>0,
\qquad
U_L-U_P>0,
\qquad
D_L-D_P>0.
```

The full exact fractions for the three harmonic reductions contain thousands
of digits. The certificate records canonical numerator/denominator hashes and
digit counts; all comparisons are performed with exact rational arithmetic.

---

## 2. Occurrence-mass weight

Consider

```math
C_\lambda(\pi)=T_\pi+\lambda O_\pi+E_\pi.
```

The delayed policy is cheaper exactly when

```math
\lambda>
\lambda_*
=
\frac{(T_P-T_L)+(E_P-E_L)}{O_L-O_P}.
```

The exact threshold satisfies

```math
\boxed{
\frac{298}{125}
<
\lambda_*
<
\frac{477}{200}
}
```

or numerically

```text
2.384 < lambda_* < 2.385.
```

Thus the unit-weight score

```math
T+O+E
```

still prefers lexicographic deletion. A weight `lambda=3` prefers the delayed
policy.

---

## 3. Duplicate-mass weight

Because

```math
O=U+D,
```

one can instead score

```math
C_\kappa(\pi)=T_\pi+U_\pi+\kappa D_\pi+E_\pi.
```

The delayed policy is cheaper exactly when

```math
\kappa>
\kappa_*
=
\frac{(T_P-T_L)+(E_P-E_L)-(U_L-U_P)}{D_L-D_P}.
```

Exact arithmetic gives

```math
\boxed{
\frac{1089}{250}
<
\kappa_*
<
\frac{4357}{1000}
}
```

or

```text
4.356 < kappa_* < 4.357.
```

Therefore `T+U+D+E=T+O+E` prefers lexicographic deletion, while

```math
T+U+5D+E
```

prefers the delayed policy.

This quantifies how strongly provenance reuse must be penalized before the
30-percent duplicate-mass reduction dominates the terminal penalty.

---

## 4. Regenerative continuation weight

Let

```math
G=\frac{36953}{4096}
```

be the certified path charge of the isolated lexicographic regenerative seed.
For the score

```math
C_\gamma(\pi)=T_\pi+O_\pi+E_\pi+\gamma G_\pi,
```

with `G_L=G` and `G_P=0`, the delayed policy is cheaper exactly when

```math
\gamma>
\gamma_*
=
\frac{(T_P-T_L)+(E_P-E_L)-(O_L-O_P)}{G}.
```

The exact threshold satisfies

```math
\boxed{
\frac{21}{1000}
<
\gamma_*
<
\frac{11}{500}
}
```

or

```text
0.021 < gamma_* < 0.022.
```

A coefficient `gamma=1/32` is sufficient to reverse the unit occurrence-score
ranking.

This does not establish that the complete path charge may be added to a
simultaneous-child potential. That requires the retention and provenance
packing theorem still missing from the program.

---

## 5. Terminal-mass weight

For

```math
C_a(\pi)=aT_\pi+O_\pi+E_\pi,
```

the delayed policy is cheaper exactly when

```math
a<a_*
=
\frac{(O_L-O_P)-(E_P-E_L)}{T_P-T_L}.
```

The exact threshold is

```math
\boxed{
\frac{209}{500}
<
a_*
<
\frac{419}{1000}
}
```

or

```text
0.418 < a_* < 0.419.
```

Thus a score that values terminal mass comparably to recursive occurrence mass
prefers lexicographic deletion. The delayed policy wins only when terminal mass
is given substantially lower weight or recursive/provenance costs are given
substantially higher weight.

---

## 6. Exact sign checks

The certificate records exact hashes for five representative score
differences, using the convention

```text
delayed score minus lexicographic score.
```

| score | sign | preferred policy |
|---|---:|---|
| `T+O+E` | positive | lexicographic |
| `T+U+E` | positive | lexicographic |
| `T+U+5D+E` | negative | delayed-seed |
| `T+3O+E` | negative | delayed-seed |
| `T+O+E+(1/32)G_lex` | negative | delayed-seed |

The thresholds and examples are exact rational results, not floating-point
fits.

---

## 7. Consequence

The delayed policy is a genuine Pareto improvement on several recursive-load
coordinates, but no coefficient-free conclusion follows. The policy ranking
changes according to how the proof values:

1. terminal output;
2. recursive occurrence mass;
3. distinct numerical support;
4. provenance duplication;
5. regenerative continuation cost;
6. terminal residual error.

Any proposed policy potential must land in a weight region compatible with
these exact inequalities. In particular, assigning all raw harmonic masses
unit weight selects the lexicographic policy, not the delayed policy.

---

## 8. Scope and next target

These are necessary finite constraints on a candidate policy score. They are
not sufficient conditions for a whole-tree Bellman inequality.

The next exact task is to compute the same coordinate differences for
additional certified states and policies. Their half-spaces can then be
intersected in the rational LP harness. Either:

- a nonempty common weight cone emerges, suggesting a constructive policy
  objective; or
- the first exact infeasible subsystem identifies which coordinate is still
  missing.
