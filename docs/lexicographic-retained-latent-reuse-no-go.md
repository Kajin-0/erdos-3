# Lexicographic retained latent-reuse no-go

## Status

Explicit 13-point counterexample showing that the actual lexicographic coordinated-deletion output followed by maximum-harmonic point-disjoint retention can retain two recursive children sharing latent parent-pair resources.

This is stronger than the arbitrary affine no-go. It occurs inside the repository's deletion and retention semantics.

---

## 1. Parent

Let

```math
P
=
\{25,31,32,33,68,69,70,73,74,75,78,79,80\}.
```

Direct exhaustive verification shows that `P` is four-AP-free.

The lexicographic coordinated-deletion schedule selects:

```text
(31,32,33), step 1;
(68,69,70), step 1;
(73,74,75), step 1;
(78,79,80), step 1;
(69,74,79), step 5;
(70,75,80), step 5.
```

For both steps, the parity rule selects the left endpoint as sponsor.

---

## 2. Retained recursive middle child

The four selected step-one centers are

```math
32,69,74,79
```

with sponsors

```math
31,68,73,78.
```

After subtracting the minimum center `32`, the middle fiber contains

```math
\{37,42,47\}.
```

Its affine reference is the minimum sponsor

```math
r_M=31,
```

and its root set is

```math
Q_M=\{68,73,78\}.
```

Indeed

```math
Q_M-r_M
=
\{37,42,47\}.
```

This is a three-term progression of step `5`, so the middle child is recursive.

---

## 3. Retained recursive backbone child

The minimum parent root is

```math
r_B=25.
```

The high backbone shell contains labels

```math
\{43,44,45,48,49,50,53,54,55\}
```

with roots

```math
\{68,69,70,73,74,75,78,79,80\}.
```

It is recursive; for example

```math
43,48,53
```

is a three-term progression of step `5`.

The middle child and backbone child are numerically point-disjoint:

```math
\{37,42,47\}
\cap
\{43,44,45,48,49,50,53,54,55\}
=
\varnothing.
```

Both therefore survive the point-disjoint retained quotient. The backbone has larger harmonic weight than every conflicting alternative and the exact maximum-weight selection is deterministic.

---

## 4. Shared latent root pairs

The recursive children share the root set

```math
Q=\{68,73,78\}.
```

Hence the parent latent resources

```math
\{68,73\},
\qquad
\{68,78\},
\qquad
\{73,78\}
```

have two recursive latent owners and no current owner.

Their gaps are

```text
5, 10, 5.
```

The genuine latent-latent activation residual is therefore

```math
\begin{aligned}
R_{\rm latent-latent}
&=
\frac15+rac1{10}+rac15\\
&=
\boxed{\frac12}.
\end{aligned}
```

This residual survives current-latent reclassification.

---

## 5. Reference pair is insufficient

The two child references are

```math
r_B=25,
\qquad
r_M=31,
```

so the reference separation is

```math
\delta=6.
```

The reference-pair capacity is

```math
\frac1\delta=\frac16.
```

Thus

```math
\boxed{
R_{\rm latent-latent}
=
\frac12
>
\frac16.
}
```

The ratio is exactly `3`.

The three rectangle aspects are

```math
\frac65,
\qquad
\frac6{10},
\qquad
\frac65.
```

Two are far and one is near. The complete aspect identity remains exact, but one unweighted reference pair cannot pay the shared pair energy.

---

## 6. Additional current-latent overlap

The same retained family also contains a terminal middle child

```math
\{1\}
```

with reference `69` and root `70`. Its current resource

```math
\{69,70\}
```

is latent in the recursive backbone child.

That degree-two current-latent overlap has mass `1` and is absorbed by the terminal current term as in `docs/current-latent-overlap-decomposition.md`.

It is separate from the latent-latent residual `1/2`.

---

## 7. Exact retained profile

The retained output has:

```text
retained child states          = 5
repeated parent resources      = 4
current-latent resources       = 1
latent-latent resources        = 3
maximum owner degree           = 2
maximum latent degree          = 2
current-latent mass            = 1
latent-latent residual         = 1/2
complete branching excess      = 3/2
```

The child-side resource identities remain point-disjoint, so:

```text
child recreation mass = 0;
owner cycle rank       = 0.
```

---

## 8. Consequence

The following stronger structural conjecture is false:

```text
coordinated deletion plus maximum-harmonic point-disjoint retention always gives ell_f <= 1.
```

It holds on every recorded retained transition through `F5` but not universally.

The active theorem must pay shared recursive root intersections using a scale- and aspect-sensitive resource. Neither point disjointness, current-latent reclassification, nor one reference-pair capacity is sufficient.

Verifier:

```text
src/verify_lexicographic_retained_latent_reuse_no_go.py
```