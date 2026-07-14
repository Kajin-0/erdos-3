# Type-weighted three-AP transport row

## Status

State-independent one-generation transfer theorem for oriented full-edge child
shells of one fixed completion type.

The theorem gives an exact first-appearance plus collision decomposition for
weighted child three-AP load. It does not yet sum the three completion types
into one contracting scalar potential.

---

## 1. Weighted three-AP load

For a finite four-AP-free root set `P`, define

```math
\mathcal L_3(P)
=
\sum_{Q\in\operatorname{AP}_3(P)}
\frac1{d(Q)},
```

where `d(Q)` is the common difference of the three-AP `Q`.

For a family of child occurrences, the load is occurrence-valued: the same
physical root progression carried by two child shells is counted twice.

---

## 2. Completion transport

Fix one child type

```text
side;
middle;
doubled side.
```

Let a child shell have reference `r`, root subset `P_C`, and a child root
progression

```math
Q=\{x,x+d,x+2d\}\subseteq P_C.
```

Apply the oriented completion map:

```math
T=F_r(Q).
```

Then `T` is a parent root three-AP. Its step is

```math
h(T)
=
\begin{cases}
2d,&\text{side},\\
d,&\text{middle},\\
d/2,&\text{doubled side}.
\end{cases}
```

Define

```math
\alpha_{\rm side}=\frac12,
\qquad
\alpha_{\rm mid}=1,
\qquad
\alpha_{\rm dbl}=2.
```

The transport is exactly weight-preserving:

```math
\boxed{
\frac{\alpha_t}{d(Q)}
=
\frac1{h(T)}.
}
```

---

## 3. Target multiplicity

For the fixed type `t`, let

```math
m_t(T)
```

be the number of child three-AP occurrences transported to one parent target
`T`.

The type-weighted child load is therefore

```math
\alpha_t
\sum_C\mathcal L_3(P_C)
=
\sum_T\frac{m_t(T)}{h(T)}.
```

Separate first appearance from collision excess:

```math
\sum_T\frac{m_t(T)}{h(T)}
=
\sum_{T:m_t(T)>0}\frac1{h(T)}
+
\sum_T\frac{(m_t(T)-1)_+}{h(T)}.
```

Since every used target is a parent three-AP,

```math
\sum_{T:m_t(T)>0}\frac1{h(T)}
\le
\mathcal L_3(P).
```

Define the type collision exposure

```math
X_t
=
\sum_T\frac{(m_t(T)-1)_+}{h(T)}.
```

Then

```math
\boxed{
\alpha_t
\sum_C\mathcal L_3(P_C)
\le
\mathcal L_3(P)+X_t.
}
```

This is the first type-weighted three-AP Bellman row.

---

## 4. Exact rectangle representation of `X_t`

Fix a target `T` and choose one deterministic base reference `r_0` among its
preimages. For the fixed type, the inverse completion formula determines the
child progression uniquely from `(T,r)`. Hence distinct excess preimages are
in bijection with the remaining references

```math
R_T\setminus\{r_0\}.
```

For every `r` in that set,

```math
\frac1{h(T)}
=
\frac{|r-r_0|}{h(T)}
\frac1{|r-r_0|}.
```

Consequently

```math
\boxed{
X_t
=
\sum_T
\sum_{r\in R_T\setminus\{r_0(T)\}}
\frac{|r-r_0(T)|}{h(T)}
\frac1{|r-r_0(T)|}.
}
```

Every summand is a named collision rectangle token. Its physical data are:

```text
parent target progression T;
base and excess references;
reference pair gap delta;
target step h;
aspect ratio delta/h;
child type;
completion rectangle corners.
```

---

## 5. Same-shell lower-scale reserve

Suppose a target/type collision group is further restricted to preimage child
progressions in one shell `[M,2M)`.

The child progression span is

```math
\Delta_t(T)
=
\begin{cases}
h(T),&\text{side},\\
2h(T),&\text{middle},\\
4h(T),&\text{doubled side}.
\end{cases}
```

The reference interval has length less than

```math
M-\Delta_t(T).
```

Let `D(R_T)` be the positive translated reference-difference set. The
reference-gap lemma gives

```math
\boxed{
\frac{m_t(T)-1}{h(T)}
<
\left(
\frac{M-\Delta_t(T)}{h(T)}
\right)
H(D(R_T)).
}
```

Every token of `D(R_T)` is below `M`, so this collision reserve descends
strictly in scale.

---

## 6. Three-type vector row

Applying the theorem separately gives

```math
\frac12\mathcal L_3(\mathcal C_{\rm side})
\le
\mathcal L_3(P)+X_{\rm side},
```

```math
\mathcal L_3(\mathcal C_{\rm mid})
\le
\mathcal L_3(P)+X_{\rm mid},
```

and

```math
2\mathcal L_3(\mathcal C_{\rm dbl})
\le
\mathcal L_3(P)+X_{\rm dbl}.
```

Summing them naively spends the parent load three times. A scalar proof must
either:

1. allocate parent target capacity across the three types;
2. retain one strategically chosen type at each target;
3. merge mixed-type first appearances into a common rectangle ledger; or
4. use a vector potential whose transition matrix has spectral radius below
   one after shell descent.

This is now a precise finite-dimensional problem rather than an unspecified
pair-energy activation gap.

---

## 7. Strategic consequence

The theorem supplies the predeclared conceptual transfer law required before
any further corrected-frontier propagation:

```text
weighted child AP load
=
parent AP first appearance
+
explicit rectangle-aspect collision exposure.
```

Further finite propagation is still deferred because the exposure terms have
not yet been proved globally summable. The next analytical target is a
three-type allocation or vector-potential theorem for

```math
(X_{\rm side},X_{\rm mid},X_{\rm dbl}).
```
