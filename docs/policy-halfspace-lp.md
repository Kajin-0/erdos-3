# Exact two-coordinate policy half-space LP

## Status

Exact finite feasibility theorem for the current deterministic policy family.

Each chosen-policy comparison has the form

```math
C_{\lambda,\gamma}(\pi_{\rm alt})
-
C_{\lambda,\gamma}(\pi_{\rm chosen})
\ge 0,
```

with

```math
C_{\lambda,\gamma}
=
T+\lambda O+E+\gamma G_{\rm regen}.
```

The comparison is exported as a linear constraint in the existing exact rational LP harness.

**Verifier:** `src/verify_policy_halfspace_lp.py`.

**Certificate:** `data/policy_halfspace_lp_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
7721d5c933fa04b3a2d9efec2ea29f1d0ebc540df6a602d78323bd390eb279d1
```

---

## 1. Constraint encoding

For an alternative policy `A` and chosen policy `P`, define

```math
\Delta T=T_A-T_P,
\qquad
\Delta O=O_A-O_P,
```

```math
\Delta E=E_A-E_P,
\qquad
\Delta G=G_A-G_P.
```

Then the ranking condition is

```math
\Delta O\,\lambda
+
\Delta G\,\gamma
\ge
-(\Delta T+\Delta E).
```

This is encoded directly as a two-feature row for `branching_reserve_lp.py`. The generated system contains

```text
60 exact rational constraints
2 nonnegative features: lambda, gamma
```

The canonical JSONL representation is `293,294` bytes with SHA-256

```text
6e2aa22f5214450062e3805c883687a9fee55ff87ed998d65802db46a07bd89b
```

The corresponding CPLEX-LP export is `348,333` bytes, `68` lines, with SHA-256

```text
62d24dd40f69e87d627d12b1a69645153903c2915895d44f6070cffe0d649667
```

---

## 2. Exact feasible witness

The exact weight vector

```math
\boxed{
\lambda=3,
\qquad
\gamma=\frac1{10}
}
```

satisfies all `60` constraints.

The zero-slack constraints are precisely:

```text
S1: lex <= q142
S1: lex <= q161
S1: lex <= q30
S1: lex <= q40
S1: lex <= step5
S1: lex <= step540
S1: lex <= step54030
S2: step5 <= step540
```

These are the expected policy ties.

The smallest strictly positive slack is the `S_1` lexicographic-versus-reverse comparison. The decisive `S_7` continuation constraint is

```text
S7: hybrid5 <= step540.
```

Its exact slack is positive at `gamma=1/10`; its rational numerator and denominator contain `6,939` and `6,940` digits respectively.

---

## 3. Scope

This result completes the finite policy-half-space export requested by the proof program. It proves that the current deterministic policy comparisons have a nonempty exact two-coordinate feasible region.

It does **not** convert the system into a whole-tree Bellman LP. The rows compare complete deletion policies on recorded parents; they do not yet encode retained simultaneous children. In particular, the following remain unresolved:

- provenance-preserving child retention;
- containment and partial-overlap capacity;
- repeated use of numerical support;
- schedule-independent control;
- and recursive justification of the path-charge coordinate.

The next useful LP experiment is to add further deterministic policy families until either the feasible cone remains stable or a smallest exact infeasible subsystem identifies the next missing coordinate.
