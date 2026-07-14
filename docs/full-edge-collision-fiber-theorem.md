# Full-edge collision-fiber theorem

## Status

Symbolic one-generation theorem for oriented full-edge recursion after affine
root reconstruction. It identifies the exact geometry behind transport
collisions of active three-AP edge resources.

The theorem does not bound collision multiplicity. It shows that every
collision fiber is a three-translate affine image of its reference set.

---

## 1. Oriented completion maps

Let an oriented affine child have reference root `r` and root subset `Q`.
The full-edge construction has three completion types.

### Side child

Every child root `q` is accompanied in the parent by the outward completion

```math
F_r^{\rm side}(q)=2q-r.
```

### Middle child

Every child root `q` is accompanied by the reflected completion

```math
F_r^{\rm mid}(q)=2r-q.
```

### Doubled-side child

Every child root `q` is accompanied by the midpoint

```math
F_r^{\rm dbl}(q)=\frac{r+q}{2}.
```

The parity rule in the doubled-side construction guarantees integrality.
Each map is affine and injective.

If

```math
Q=\{x,x+d,x+2d\}
```

is a child three-term progression, then `F_r(Q)` is a parent three-term
progression. Its step is respectively

```text
side:         2d;
middle:       d;
doubled side: d/2.
```

Thus every active child pair edge transports to an active parent pair edge.

---

## 2. Fixing one parent witness

Fix a parent three-term progression

```math
T=\{a,a+h,a+2h\}.
```

For one child type, let `R_T` be the set of reference roots `r` for which a
child progression `Q_r` satisfies

```math
F_r(Q_r)=T.
```

The inverse formulas are exact.

### Side collision fiber

```math
Q_r=\frac{T+r}{2}.
```

Therefore

```math
\bigcup_{r\in R_T}Q_r
=
\frac12R_T+\frac12T.
```

Writing out the three points of `T`, this is

```math
\left(\frac12R_T+\frac a2\right)
\cup
\left(\frac12R_T+\frac a2+\frac h2\right)
\cup
\left(\frac12R_T+\frac a2+h\right).
```

It is three equal translates of `R_T/2`, separated by `h/2`.

### Middle collision fiber

```math
Q_r=2r-T,
```

so

```math
\bigcup_{r\in R_T}Q_r
=
2R_T-T.
```

This is three equal translates of `2R_T`, separated by `h`.

### Doubled-side collision fiber

```math
Q_r=2T-r,
```

so

```math
\bigcup_{r\in R_T}Q_r
=
2T-R_T.
```

This is three equal translates of `-R_T`, separated by `2h`.

Hence every transport collision has the same structural form:

```math
\boxed{
\text{collision fiber}
=
A\cup(A+s)\cup(A+2s)
}
```

for an affine image `A` of the reference set.

---

## 3. Disjointness of the witness progressions

All `Q_r` for fixed `T` and fixed child type have the same common difference.
Distinct fixed-step three-term progressions inside a four-AP-free set are
pairwise disjoint. Indeed, two such progressions sharing a point have starts
differing by one or two steps, and their union contains four consecutive
points of that step.

Therefore

```math
\boxed{
\left|\bigcup_{r\in R_T}Q_r\right|
=3|R_T|.
}
```

The collision multiplicity `|R_T|` is exactly one third of the size of the
forced three-translate layer family.

Both `R_T` and the forced layer family are subsets of the four-AP-free parent
root set. In particular, both are four-AP-free.

---

## 4. Exact edge-energy scaling

The three unordered edges of a three-AP of step `s` have total pair weight

```math
E_3(s)
=
\frac1s+\frac1s+\frac1{2s}
=
\frac5{2s}.
```

Let `m=|R_T|`. Since the parent witness `T` has step `h`, its edge energy is

```math
E(T)=\frac5{2h}.
```

The total child witness-edge occurrence energy in one collision fiber is

```math
\boxed{
\begin{aligned}
\text{side} &: 2mE(T),\\
\text{middle} &: mE(T),\\
\text{doubled side} &: \frac m2E(T).
\end{aligned}
}
```

These coefficients are precisely the inverse gap-scaling factors of the three
completion maps.

---

## 5. Difference exclusions in a collision reference set

Let the child witness step be `d`.

For a side collision fiber, every `Q_r` contains pair gaps `d` and `2d`.
The reflection-grid four-AP test implies that the reference set contains no
pair at any of the differences

```math
\boxed{d,2d,4d,8d.}
```

For a middle collision fiber, applying the same test to both pair gaps gives

```math
\boxed{d/4,d/2,d,2d}
```

whenever the displayed quantities are integral.

For a doubled-side collision fiber the corresponding forbidden differences
are

```math
\boxed{d/2,d,2d,4d}
```

in the integral cases.

These exclusions strengthen the bare fact that `R_T` is four-AP-free, but do
not force bounded cardinality.

---

## 6. Consequence

Transport collisions are not arbitrary reuse. Every multiplicity `m` creates
three affine copies of an `m`-point reference set inside the parent root set.
Thus the collision problem has been reduced to the same three-translate
geometry as the aligned-diamond obstruction.

The remaining theorem must charge

```math
mE(T)
```

against the scale, support, or future termination cost of the forced layer
family. A uniform collision-multiplicity constant is neither proved nor
needed by this identity—and is in fact false by the parametric reuse theorem.
