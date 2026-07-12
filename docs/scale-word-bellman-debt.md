# Scale-word Bellman debt identity

## Status

Elementary exact theorem. This note extends the exact-tail Bellman potential to arbitrary finite disjoint three-translate scale words, including contaminated steps.

The theorem is algebraic: it uses only

```math
N'=3(N+1),
\qquad
P'=2P,
\qquad
L'=cL.
```

It does not assert that a given scale word is geometrically realizable.

---

## 1. Reference potential

For every replay state, whether or not it already has a basin certificate, define the factor-eight reference potential

```math
\boxed{
\mathfrak B(N,P,L)
=
\frac{4P(N+1)}L.
}
```

The current weighted density is

```math
W(N,P,L)=\frac{PN}{L}.
```

Under one disjoint three-translate step with dyadic scale factor `c`,

```math
N'=3(N+1),
\qquad
P'=2P,
\qquad
L'=cL.
```

Therefore

```math
\boxed{
\frac{\mathfrak B(N',P',L')}{\mathfrak B(N,P,L)}
=
\frac{2(3N+4)}{c(N+1)}.
}
```

---

## 2. One-step Bellman defect

Define

```math
\mathfrak D_c
=
\mathfrak B(N,P,L)
-
W(N,P,L)
-
\mathfrak B(N',P',L').
```

Direct simplification gives

```math
\boxed{
\mathfrak D_c
=
\frac{P(3N+4)}L
\left(1-\frac8c\right).
}
```

Hence:

- `c=8`: `D_c=0`; the reference potential satisfies the exact Bellman identity;
- `c>8`: `D_c>0`; the step creates Bellman surplus;
- `c<8`: `D_c<0`; the step incurs Bellman debt.

For standard dyadic factors, only `c=2` and `c=4` create debt. Factor `8` is neutral, and every factor at least `16` creates surplus.

---

## 3. Telescoping identity along a path

For an `H`-step path, write

```math
(N_h,P_h,L_h),
\qquad
c_h=\frac{L_{h+1}}{L_h},
```

and let `D_h` be the one-step defect. Then

```math
\boxed{
\sum_{h=0}^{H-1}W_h
+
\mathfrak B_H
=
\mathfrak B_0
-
\sum_{h=0}^{H-1}\mathfrak D_h.
}
```

Thus the whole path problem reduces algebraically to controlling the cumulative negative defects of cheap steps.

---

## 4. Endpoint potential depends only on the scale product

Let

```math
C_H=\prod_{h=0}^{H-1}c_h.
```

The cardinality recurrence gives

```math
N_H
=
3^H\left(N_0+\frac32\right)-\frac32.
```

Since

```math
P_H=2^HP_0,
\qquad
L_H=C_HL_0,
```

one obtains

```math
\boxed{
\frac{\mathfrak B_H}{\mathfrak B_0}
=
\frac{2^H}{C_H}
\frac{3^H(N_0+\tfrac32)-\tfrac12}{N_0+1}.
}
```

Equivalently,

```math
\boxed{
\frac{\mathfrak B_H}{\mathfrak B_0}
=
\frac{2^{H-1}\bigl(3^H(2N_0+3)-1\bigr)}
{C_H(N_0+1)}.
}
```

The endpoint charge depends on the scale factors only through their product, not their order and not the contamination profile.

As `N_0` grows, endpoint contraction is governed by

```math
C_H>6^H.
```

---

## 5. Exact repayment blocks

### One factor four and one factor eight

For any two-step word with scale product

```math
C_2=4\cdot8=32,
```

```math
\frac{\mathfrak B_2}{\mathfrak B_0}
=
\boxed{
\frac{9N_0+13}{8(N_0+1)}
}
>1.
```

Thus one factor-eight step does not repay one factor-four step in endpoint potential.

### One factor four and two factor eights

For any three-step word with scale multiset

```math
\{4,8,8\},
```

```math
\frac{\mathfrak B_3}{\mathfrak B_0}
=
\boxed{
\frac{27N_0+40}{32(N_0+1)}.
}
```

This is less than `1` exactly when

```math
N_0>\frac85.
```

Therefore, for every integer state size

```math
\boxed{N_0\ge2,}
```

one factor-four debt is repaid by two factor-eight steps, regardless of their order inside the block.

### One factor two and three factor eights

For scale multiset

```math
\{2,8,8,8\},
```

the cumulative scale product is below the asymptotic threshold, so the endpoint potential expands for all sufficiently large states. Three factor-eight steps do not generally repay one factor-two step.

### One factor two and four factor eights

For scale multiset

```math
\{2,8,8,8,8\},
```

```math
\frac{\mathfrak B_5}{\mathfrak B_0}
=
\boxed{
\frac{243N_0+364}{256(N_0+1)}.
}
```

This is less than `1` exactly when

```math
N_0>\frac{108}{13}.
```

Therefore

```math
\boxed{N_0\ge9}
```

is sufficient for four factor-eight steps to repay one factor-two debt.

---

## 6. Interpretation of the recorded branch

The recorded cheap release at depth seven is a factor-four step. The complete exclusions at `S_7` and `S_8` force two subsequent factor-eight steps before another cheap step can occur on that branch.

The three-step scale multiset is therefore

```math
\{4,8,8\},
```

which contracts the Bellman endpoint potential independently of the order. The third consecutive factor-eight step creates additional contraction.

This explains the observed delayed repayment algebraically. The structural exclusion theorems supply the geometry; the Bellman identity supplies the exact accounting.

---

## 7. Remaining geometric problem

The algebraic whole-tree strategy is now explicit:

1. assign every state the reference potential `B=4P(N+1)/L`;
2. treat factor-eight basin paths by exact Bellman equality;
3. charge factor-two and factor-four steps as negative defects;
4. prove geometrically that cheap-step debt is followed by enough scale-eight or larger growth, or is offset by contamination export and overlap packing.

The unresolved theorem is a state-independent bound on the cumulative negative Bellman defect over every branch and, ultimately, over the entire continuation tree.
