# Fixed-step anchor-fiber transfer

## Status

State-independent entry theorem for numerical three-AP step multiplicity in a
four-AP-free dyadic block.

The theorem is the root-level analogue of the reference-gap collision charge.
It converts repeated use of one numerical difference into a strictly
lower-scale four-AP-free anchor-difference reserve.

---

## 1. Fixed-step anchor set

Let

```math
B\subseteq[N,2N)
```

be four-AP-free. For each positive integer `d`, define

```math
P_d
=
\{p:p,p+d,p+2d\in B\}
```

and put

```math
n_B(d)=|P_d|.
```

The weighted three-AP load is

```math
\mathcal L_3(B)
=
\sum_{d\ge1}\frac{n_B(d)}d.
```

---

## 2. Three disjoint translates

The parent contains

```math
P_d,
\qquad
P_d+d,
\qquad
P_d+2d.
```

These three translates are pairwise disjoint. If two fixed-step three-APs
shared a point, their starts would differ by `d` or `2d`, and their union would
contain four consecutive terms of common difference `d`.

Therefore

```math
\boxed{
|P_d\cup(P_d+d)\cup(P_d+2d)|
=3n_B(d).
}
```

The union is a subset of `B`, so it is four-AP-free. This is the exact
three-translate support forced by numerical step multiplicity.

---

## 3. First numerical appearance and excess

Define the distinct-step harmonic mass

```math
U(B)
=
\sum_{d:n_B(d)>0}\frac1d.
```

Then

```math
\mathcal L_3(B)
=
U(B)
+
R_{\rm step}(B),
```

where

```math
R_{\rm step}(B)
=
\sum_d\frac{(n_B(d)-1)_+}{d}.
```

The term `U(B)` is first numerical appearance of a step. The term
`R_step(B)` is pure same-step multiplicity.

---

## 4. Anchor-difference reserve

For every `d` with `n_B(d)>0`, choose

```math
p_0(d)=\min P_d
```

and define

```math
D(P_d)
=
\{p-p_0(d):p\in P_d,\ p>p_0(d)\}.
```

Since `P_d` is a subset of `B`, the translated set `D(P_d)` is four-AP-free.
Also

```math
P_d\subseteq[N,2N-2d),
```

so

```math
0<\delta<N-2d
\qquad
(\delta\in D(P_d)).
```

Thus every anchor-difference reserve lies strictly below the parent scale
`N`.

Its harmonic mass satisfies

```math
H(D(P_d))
>
\frac{n_B(d)-1}{N-2d}.
```

Consequently

```math
\boxed{
\frac{n_B(d)-1}{d}
<
\left(\frac Nd-2\right)
H(D(P_d)).
}
```

Summing over steps gives

```math
\boxed{
R_{\rm step}(B)
<
\sum_{d:n_B(d)>1}
\left(\frac Nd-2\right)
H(D(P_d)).
}
```

This is the fixed-step anchor-fiber transfer.

---

## 5. Pointwise aspect identity

Every extra anchor `p` creates the anchor pair

```math
f=\{p_0(d),p\},
\qquad
\delta=p-p_0(d).
```

The repeated numerical step weight factors exactly as

```math
\boxed{
\frac1d
=
\frac\delta d\frac1\delta.
}
```

Thus root-level same-step multiplicity has the same rectangle-aspect token as
recursive physical-pair reuse.

A dyadic ratio decomposition gives

```math
\frac{n_B(d)-1}{d}
<
\sum_k2^{k+1}H(D_k(P_d;d)),
```

where

```math
D_k(P_d;d)
=
\{\delta\in D(P_d):2^kd\le\delta<2^{k+1}d\}.
```

---

## 6. Difference exclusions

Two fixed-step progressions with start separation `delta` force a six-point
two-row configuration

```math
\{0,d,2d\}
\cup
\{\delta,\delta+d,\delta+2d\}
```

after translation.

Four-AP-freeness excludes the integer separations

```math
\boxed{d,2d,3d,4d.}
```

When integral, the half-step separations

```math
\boxed{d/2,3d/2}
```

are also excluded. These constraints are exact but do not bound
`n_B(d)` by a universal constant.

---

## 7. Base-six benchmark

For the base-six digit family with digits `{0,1,2}`, the step `d=1` has

```math
n_B(1)=3^{n-1}.
```

Its anchor set is exactly a scaled copy of the depth-`n-1` digit family:

```math
P_1=6A_{n-1}
```

before dyadic translation. Therefore the large unit-step load is not
unsupported multiplicity; it exports recursively to the lower-depth
anchor-difference family.

This confirms that the anchor-fiber transfer captures the precise structure
behind the linear-scale load-to-harmonic obstruction.

---

## 8. Unified entry and collision ledger

The root and recursive multiplicity problems now have one form.

### Root entry

```text
repeated numerical step d
-> start-anchor set P_d
-> three translates P_d,P_d+d,P_d+2d
-> lower-scale difference reserve D(P_d).
```

### Recursive collision

```text
repeated physical pair/root progression
-> reference set R
-> three affine completion translates
-> lower-scale difference reserve D(R).
```

Both use the exact aspect factorization

```math
\frac1{\text{repeated gap}}
=
\frac{\text{anchor/reference gap}}{\text{repeated gap}}
\frac1{\text{anchor/reference gap}}.
```

The active theorem should therefore use one first-appearance ledger for
anchor/reference rectangle tokens, rather than separate entering-AP and
recursive-collision potentials.
