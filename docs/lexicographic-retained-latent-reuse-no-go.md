# Lexicographic retained latent-reuse no-go

## Status

Explicit 13-point counterexample showing that the actual lexicographic coordinated-deletion output followed by maximum-harmonic point-disjoint retention can retain two recursive children sharing latent parent-pair resources.

The example has pure latent-latent reuse: no current-latent term is involved in the obstruction. It also defeats payment by one unweighted reference pair.

---

## 1. Parent

Let

```math
P
=
\{1,4,5,6,20,21,22,26,27,28,32,33,34\}.
```

Direct exhaustive verification shows that `P` is four-AP-free.

The lexicographic coordinated-deletion schedule selects:

```text
(4,5,6), step 1;
(20,21,22), step 1;
(26,27,28), step 1;
(32,33,34), step 1;
(21,27,33), step 6, sponsor 33;
(22,28,34), step 6, sponsor 34.
```

At step `1`, the parity rule selects the left endpoint as sponsor. At step `6`, it selects the right endpoint.

---

## 2. Retained recursive middle child

The four selected step-one centers are

```math
5,21,27,33
```

with sponsors

```math
4,20,26,32.
```

After subtracting the minimum center `5`, the middle fiber contains

```math
\{16,22,28\}.
```

Its affine reference is the minimum sponsor

```math
r_M=4,
```

and its root set is

```math
Q_M=\{20,26,32\}.
```

Indeed

```math
Q_M-r_M
=
\{16,22,28\}.
```

This is a three-term progression of step `6`, so the middle child is recursive.

---

## 3. Retained recursive backbone child

The minimum parent root is

```math
r_B=1.
```

The relevant backbone shell contains labels

```math
\{19,20,21,25,26,27,31\}
```

with roots

```math
\{20,21,22,26,27,28,32\}.
```

It is recursive; for example

```math
19,25,31
```

is a three-term progression of step `6`.

The middle and backbone children are point-disjoint:

```math
\{16,22,28\}
\cap
\{19,20,21,25,26,27,31\}
=
\varnothing.
```

Both survive the exact maximum-harmonic point-disjoint retained quotient.

---

## 4. Shared latent root pairs

The two recursive children share the root set

```math
Q=\{20,26,32\}.
```

Thus the parent resources

```math
\{20,26\},
\qquad
\{20,32\},
\qquad
\{26,32\}
```

have two recursive latent owners and no current owner.

Their gaps are

```text
6, 12, 6.
```

The genuine latent-latent residual is

```math
\begin{aligned}
R_{\rm latent-latent}
&=
\frac16+
\frac1{12}+
\frac16\\
&=
\boxed{\frac5{12}}.
\end{aligned}
```

No current-latent reclassification is available.

---

## 5. One reference pair is insufficient

The child references are

```math
r_B=1,
\qquad
r_M=4,
```

so

```math
\delta=3.
```

The reference-pair capacity is

```math
\frac1\delta=\frac13.
```

Therefore

```math
\boxed{
R_{\rm latent-latent}
=
\frac5{12}
>
\frac13.
}
```

The exact ratio is

```math
\frac{5/12}{1/3}
=
\boxed{\frac54}.
```

The rectangle aspects are

```math
\frac36,
\qquad
\frac3{12},
\qquad
\frac36.
```

All are near in the pointwise sense `delta<=D`, but three demands reuse the same reference-pair identity. One physical reference capacity still cannot pay their union.

This distinguishes aspect control from reference-token reuse.

---

## 6. Two translated reserve copies

The duplicated middle fiber has selected step `d=1`. Its center-copy reserve pairs are

```math
\{21,27\},
\qquad
\{21,33\},
\qquad
\{27,33\},
```

and its opposite-copy reserve pairs are

```math
\{22,28\},
\qquad
\{22,34\},
\qquad
\{28,34\}.
```

Every reserve pair has the same gap and reciprocal weight as its duplicated sponsor pair.

The reserve graph is three disjoint edges. Hence the full latent residual packs exactly into either the three center-copy pairs or the three opposite-copy pairs.

The example defeats one-reference payment but is closed by the two-choice translated reserve.

---

## 7. Exact retained profile

The retained output has:

```text
retained child states          = 6
repeated parent resources      = 3
current-latent resources       = 0
latent-latent resources        = 3
maximum owner degree           = 2
maximum latent degree          = 2
current-latent mass            = 0
latent-latent residual         = 5/12
complete branching excess      = 5/12
reserve graph vertices         = 6
reserve graph edges            = 3
reserve graph cycle rank       = 0
```

The child-side resources remain point-disjoint, so child recreation and owner cycle mass are zero.

---

## 8. Consequence

The conjecture

```text
coordinated deletion plus maximum-harmonic point-disjoint retention always gives ell_f<=1
```

is false.

The recorded retained chain through `F5` has zero latent-latent residual, but this is not universal. The correct architecture is:

```text
latent degree at most two;
one backbone-middle duplicate;
two equal-gap translated reserve options;
pseudoforest Hall criterion.
```

Verifier:

```text
src/verify_lexicographic_retained_latent_reuse_no_go.py
```