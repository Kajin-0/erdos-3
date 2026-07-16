# Point-disjoint latent-reuse no-go

## Status

Small explicit counterexample showing that point-disjoint affine retention does not eliminate latent-latent pair reuse.

The point-disjoint owner-forest theorem removes child-side recreation and cycle rank, but parent row stars can still contain two or more recursive latent owners.

---

## 1. Four-AP-free parent root set

Let

```math
P=\{1,2,3,5,6,9\}.
```

The set is four-AP-free. A direct finite check tests every possible positive step and finds no four-term arithmetic progression.

Let

```math
Q=\{3,6,9\}\subseteq P.
```

The set `Q` is a three-term progression of step `3`.

---

## 2. Two affine recursive children

Use references

```math
r_1=1,
\qquad
r_2=2.
```

The right-oriented affine children are

```math
S_1=Q-r_1=\{2,5,8\},
```

and

```math
S_2=Q-r_2=\{1,4,7\}.
```

Both are three-term progressions of step `3`, so both are recursively continuing.

They are point-disjoint:

```math
\boxed{S_1\cap S_2=\varnothing.}
```

Thus the family satisfies the numerical point-disjointness required by a retained quotient.

---

## 3. Complete latent-pair reuse

Both children have the same recursive root subset `Q`. Their latent parent resources are therefore

```math
\binom Q2
=
\bigl\{
\{3,6\},
\{6,9\},
\{3,9\}
\bigr\}.
```

Every one of these parent resources has

```math
c_f=0,
\qquad
\ell_f=2.
```

Hence every pair contributes one copy to the genuine latent-latent residual.

The exact residual mass is

```math
\begin{aligned}
R_{\rm latent-latent}
&=
\frac1{6-3}
+
\frac1{9-6}
+
\frac1{9-3}\\
&=
\frac13+\frac13+\frac16\\
&=
\boxed{\frac56}.
\end{aligned}
```

No current-latent reclassification is available.

---

## 4. Owner graph

For each of the three parent-pair vertices, the owner-incidence graph is a row star of degree two. The two numerical child pair leaves are distinct because `S_1` and `S_2` are disjoint.

Therefore:

```text
child recreation mass = 0;
cycle rank             = 0;
latent-latent residual = 5/6.
```

This separates the three concepts exactly.

---

## 5. Reference-pair payment

The reference pair is

```math
\{r_1,r_2\}=\{1,2\}
```

with gap

```math
\delta=1.
```

Every shared latent pair has gap `D` equal to `3`, `3`, or `6`. Thus all three rectangles are near-aspect:

```math
\delta\le D.
```

The complete latent residual satisfies

```math
\frac56<1=\frac1\delta.
```

So this counterexample does not defeat reference-pair payment. It shows only that the latent-latent ledger is genuinely necessary.

---

## 6. Strategic consequence

The following statement is false:

```text
point-disjoint affine recursive children have disjoint latent parent resources.
```

The correct surviving theorem must control common recursive root intersections by reference separation, rectangle aspect, shell descent, or production ownership.

The smallest model already has the exact form

```math
R_{\rm latent-latent}
=
J(Q_1\cap Q_2).
```

Verifier:

```text
src/verify_point_disjoint_latent_reuse_no_go.py
```