# Scale-weighted three-AP load criticality

## Status

State-independent shell-aware refinement of the type-weighted three-AP
transport theorem.

Weighting each child witness by its dyadic shell base produces one scalar
first-appearance row. The three full-edge types consume exact parent-capacity
fractions `1/2`, `1/4`, and `1/4`. Collision exposure is the only excess term.

---

## 1. Scale-weighted load

For a family of standard dyadic shells `C`, define

```math
\Psi_1(\mathcal C)
=
\sum_{C\in\mathcal C}
M(C)\mathcal L_3(C),
```

where

```math
C\subseteq[M(C),2M(C))
```

and `L_3(C)` is occurrence-valued weighted three-AP load.

For a parent block `P` in `[N,2N)`, the parent scale-weighted load is

```math
\Psi_1(P)=N\mathcal L_3(P).
```

---

## 2. One transported witness

Fix a parent target three-AP `T` of step `h`.

### Side preimage

A side child preimage has step `h/2` and shell base

```math
M\le N/4.
```

Its scale-weighted contribution is at most

```math
\frac{M}{h/2}
\le
\frac{N}{2h}.
```

Thus one first side preimage uses at most one half of the parent target
capacity `N/h`.

### Middle preimage

A middle preimage has step `h` and shell base `M<=N/4`, so

```math
\frac Mh
\le
\frac{N}{4h}.
```

It uses at most one quarter of parent target capacity.

### Doubled-side preimage

A doubled-side preimage has step `2h` and shell base `M<=N/2`, so

```math
\frac{M}{2h}
\le
\frac{N}{4h}.
```

It also uses at most one quarter of parent target capacity.

Therefore one first preimage of each type satisfies

```math
\boxed{
\frac{N}{2h}
+
\frac{N}{4h}
+
\frac{N}{4h}
=
\frac Nh.
}
```

The parent witness pays all three type first appearances exactly at the
critical scale exponent.

---

## 3. First-appearance row

For every parent target `T`, choose at most one deterministic first preimage of
each type. Let `F` be the resulting child witness family.

Summing the preceding capacities over distinct parent targets gives

```math
\boxed{
\Psi_1(F)
\le
N\mathcal L_3(P).
}
```

No parent target is spent more than once: its scale-weighted capacity is
partitioned into the role fractions

```math
\boxed{
\frac12,
\qquad
\frac14,
\qquad
\frac14.
}
```

This removes the apparent triple spending in the unweighted type rows.

---

## 4. Collision excess

Let all child witness occurrences be retained, and define

```math
Y(P)
=
\sum_T
\left(
\sum_{Q\mapsto T}
\frac{M(Q)}{d(Q)}
-
\frac Nh
\right)_+,
```

where `h` is the step of `T`.

Then

```math
\boxed{
\Psi_1(\text{all child witnesses})
\le
N\mathcal L_3(P)
+
Y(P).
}
```

The excess `Y(P)` contains only second and later preimages after all three
role first-appearance capacities and any unused scale slack have been applied.
It is therefore a pure collision term.

Every summand of `Y(P)` has the collision-fiber and rectangle-aspect
certificates developed in the companion notes.

---

## 5. General scale moment

For `p>=0`, define

```math
\Psi_p(\mathcal C)
=
\sum_C M(C)^p\mathcal L_3(C).
```

Ignoring collision excess, the three first-preimage coefficients are

```math
\frac{2}{4^p},
\qquad
\frac{1}{4^p},
\qquad
\frac{1}{2^{p+1}}.
```

Hence

```math
\boxed{
\Psi_p(F)
\le
c_p N^p\mathcal L_3(P),
\qquad
c_p
=
\frac3{4^p}
+
\frac1{2^{p+1}}.
}
```

The threshold is exact:

```math
c_1=1,
```

while

```math
c_p<1
\qquad(p>1).
```

Thus the scale-weighted load is critical at exponent one and strictly
contracting at every higher scale moment before collision exposure is added.

---

## 6. Collision-reserve interface

For a same-shell collision group with target step `h`, shell base `M`, and
reference set `R_T`, the reference-gap theorem supplies a lower-scale reserve.
The target preimage spans are

```math
h,
\qquad
2h,
\qquad
4h
```

for side, middle, and doubled-side types. Therefore the multiplicity excess
can be bounded by the harmonic mass of `D(R_T)` with an explicit shell-slack
coefficient.

At the critical scale moment, the remaining task is to prove

```math
Y(P)
\le
\text{released scale slack}
+
\text{first-appearance reference reserve}
+
\text{terminal/external-completion credit}.
```

This is now the exact scalar closing target.

---

## 7. Strategic consequence

The local spectral problem is solved:

```text
side first appearance      = 1/2 parent target capacity;
middle first appearance    = 1/4 parent target capacity;
doubled first appearance   = 1/4 parent target capacity.
```

Only collision excess remains. A successful proof no longer needs to choose
one type, prepay the full root-pair energy, or fit a numerical coefficient.
It must show that the scale-critical excess `Y(P)` is globally summable through
reference-gap first appearance, strict shell descent, and obstruction release.
