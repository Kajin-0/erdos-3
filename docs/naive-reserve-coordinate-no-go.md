# No-go theorem for naive reserve coordinates

## Status

Exact finite algebraic consequence of the certified transition

```math
S_6\longrightarrow S_7.
```

This note rules out a natural three-coordinate reserve family before any large
linear-program search is attempted.

**Verifier:** `src/verify_naive_reserve_no_go.py`.

**Certificate:** `data/naive_reserve_no_go_certificate_2026-07-13.txt`.

---

## 1. Candidate coordinates

For a recorded state

```math
S_h\subseteq[L_h,2L_h),
```

with persistence lower bound `P_h`, define:

### Multiplicity-weighted density

```math
W_h
=
P_h\frac{|S_h|}{L_h}.
```

### Right-shell slack

```math
Q_h
=
P_h\frac{2L_h-1-\max S_h}{L_h}.
```

This measures the unused integer width at the right side of the current dyadic
shell in the same `P/L` normalization as the Bellman accounting.

### Incoming contamination mass

Let `kappa_h` be the number of additional points in the backbone shell of the
step that created `S_h`. Define

```math
C_h
=
P_h\frac{\kappa_h}{L_h}.
```

A naive linear reserve would be

```math
\Phi_h
=
aW_h+bQ_h+cC_h,
\qquad
a,b,c\ge0.
```

All three coordinates are nonnegative and superficially plausible:

1. `W_h` measures current weighted mass;
2. `Q_h` measures geometric room before the shell boundary;
3. `C_h` measures raw contamination that might later create obstructions.

The recorded factor-four transition from `S_6` to `S_7` disproves this entire
nonnegative linear family.

---

## 2. Certified transition data

The parent state has

```math
L_6=262144,
\qquad
|S_6|=3279,
\qquad
P_6=64,
\qquad
\max S_6=512764.
```

The child state has

```math
L_7=1048576,
\qquad
|S_7|=9840,
\qquad
P_7=128,
\qquad
\max S_7=2021668.
```

The transition uses scale factor

```math
c=4
```

and introduces exactly two contaminating backbone points.

The factor-four Bellman debt is

```math
\Delta_4(S_6)
=
\frac{P_6(3|S_6|+4)}{L_6}
=
\boxed{\frac{9841}{4096}}.
```

This is the amount that a reserve drop must pay before any controlled error is
allowed.

---

## 3. Every naive coordinate moves in the wrong direction

### Weighted density

```math
W_6
=
\frac{3279}{4096},
```

while

```math
W_7
=
\frac{615}{512}
=
\frac{4920}{4096}.
```

Therefore

```math
\boxed{
W_6-W_7
=
-\frac{1641}{4096}<0.
}
```

### Right-shell slack

For `S_6`, the unused shell width is

```math
2L_6-1-\max S_6
=
11523,
```

so

```math
Q_6
=
\frac{11523}{4096}.
```

For `S_7`, the unused shell width is

```math
2L_7-1-\max S_7
=
75483,
```

so

```math
Q_7
=
\frac{75483}{8192}.
```

Hence

```math
\boxed{
Q_6-Q_7
=
-\frac{52437}{8192}<0.
}
```

The child has substantially more geometric slack in Bellman normalization.
Thus raw shell room is not debt repayment.

### Incoming contamination mass

The exact factor-eight step into `S_6` has no contamination, while the
factor-four step into `S_7` has two contaminating points. Therefore

```math
C_6=0,
```

and

```math
C_7
=
128\frac{2}{1048576}
=
\frac1{4096}.
```

Thus

```math
\boxed{
C_6-C_7
=
-\frac1{4096}<0.
}
```

Raw contamination count also increases rather than being consumed.

---

## 4. Exact no-go conclusion

For arbitrary nonnegative coefficients `a,b,c`,

```math
\Phi_6-\Phi_7
=
a(W_6-W_7)
+b(Q_6-Q_7)
+c(C_6-C_7).
```

Substituting the exact differences gives

```math
\Phi_6-\Phi_7
=
-\frac{1641}{4096}a
-\frac{52437}{8192}b
-\frac1{4096}c
\le0.
```

But the factor-four Bellman inequality without error would require

```math
\Phi_6-\Phi_7
\ge
\frac{9841}{4096}>0.
```

These statements are incompatible. Therefore:

```math
\boxed{
\text{No nonnegative linear combination of }W,Q,C
\text{ can pay the recorded }S_6\to S_7\text{ debt.}
}
```

The obstruction is stronger than LP infeasibility detected numerically. It is
an exact one-row sign certificate.

---

## 5. Interpretation

The result rules out three tempting shortcuts:

1. **weighted mass alone:** the cheap factor-four step increases it;
2. **dyadic fit slack alone:** the child gains shell room instead of consuming
   it;
3. **raw contamination count alone:** cheap replication can create more
   contamination before that contamination becomes arithmetically useful.

The required potential must distinguish *unstructured contamination* from
*obstruction capacity*. Merely counting extra points cannot measure whether
they support completion fibers, direct rectangles, or future exclusion
windows.

This supports the target coordinates introduced in
`docs/transport-interval-capacity.md`:

1. direct rectangle-support radius;
2. target interval demand;
3. endpoint closure margin;
4. affine obstruction coverage by class;
5. overlap and imported-prefix packing data.

The depth-ten closure illustrates the distinction sharply. A large rectangle
support interval can eliminate all cheap continuations even when the final
endpoint margin is only five. That information is invisible to `W`, `Q`, and
`C`.

---

## 6. Consequence for LP design

The branching-reserve LP should not begin with the feature family

```text
weighted_density
right_shell_slack
incoming_contamination_mass
```

alone. Any feasibility solver would correctly reject it, but the exact sign
certificate already explains why.

These coordinates may remain as auxiliary terms if a stronger obstruction
coordinate is present. The next candidate basis should include at least one
feature that decreases across `S_6 -> S_7` despite the increase in raw mass,
slack, and contamination. Plausible candidates are:

1. uncovered cheap-separation capacity;
2. deficit between direct-support radius and target interval demand;
3. weighted count of zero obstruction classes;
4. completion-fiber deficit;
5. a packing-adjusted imported-prefix reserve.

The next finite-state experiment should therefore compute obstruction-aware
features for every sibling in the exact replay catalog, then test whether one
of those features supplies a positive drop on the certified factor-four step.

---

## 7. Reproduction

Run

```bash
python3 src/verify_naive_reserve_no_go.py \
  /tmp/naive_reserve_no_go_certificate.txt
```

The recorded certificate has SHA-256

```text
67a8f08bdaacb838a364079c9fe9e03f7fcf3ae8325ba4aee970c997791664b8
```

and records the exact debt and coordinate differences used above.
