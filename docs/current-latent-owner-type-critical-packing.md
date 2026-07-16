# Current-latent owner-scale bounds

## Status

Corrected state-independent owner-scale bound for one parent pair with exactly one current owner and one recursive latent owner.

The former orientation-specific zero/quarter theorem depended on the false claim that every coordinated middle child has shell base at most `N/4`. The correct universal bound is

```math
L_{\rm current},L_{\rm latent}\le\frac N2.
```

Therefore at owner exponent one the current-latent residual is at most one half of the parent pair unit. A shell-valid retained-policy example attains residual one quarter; sharpness of the universal one-half bound is not asserted here.

---

## 1. Setup

Let

```math
P\subseteq[N,2N)
```

and fix a parent pair

```math
f=\{x,y\},
\qquad g=y-x.
```

Suppose `f` has exactly:

```text
one current owner;
one recursive latent owner.
```

At owner exponent `p`, the current occurrence contributes

```math
\frac{L_{\rm cur}^p}{g}
```

and the latent occurrence contributes to the doubled pair coordinate

```math
\frac{2L_{\rm lat}^p}{g}.
```

The parent pair capacity is

```math
\frac{N^p}{g}.
```

---

## 2. Correct universal bound

Every child label is a positive difference of two roots in `[N,2N)`, so every child shell base satisfies

```math
L\le\frac N2.
```

Hence

```math
\frac{L_{\rm cur}^p+2L_{\rm lat}^p}{N^p}
\le
3\,2^{-p}.
```

At `p=1`,

```math
\boxed{
\operatorname{Load}_{\rm cur-lat}
\le
\frac32\frac Ng.
}
```

After one parent unit is assigned, the universal residual is

```math
\boxed{
\operatorname{Res}_{\rm cur-lat}(f)
\le
\frac12\frac Ng.
}
```

No source orientation gives a better state-independent bound using owner scale alone.

At `p=2`,

```math
3\,2^{-2}=\frac34,
```

so the complete current-latent owner pair fits strictly inside one quadratic parent pair unit.

---

## 3. Exact recursive example with residual one quarter

The parent

```math
\{65,97,98,99,113,114,115,119,120,121,125,126,127\}
\subset[64,128)
```

is four-AP-free and, under the actual retained policy, has three resources that are:

```text
current in a recursive middle child of shell base 16;
latent in a recursive backbone child of shell base 32.
```

Thus

```math
\frac{L_{\rm cur}+2L_{\rm lat}}N
=
\frac{16+64}{64}
=
\frac54.
```

Each resource leaves residual

```math
\frac14\frac Ng.
```

This disproves zero correction. It does not prove that `1/4` is the universal maximum.

Primary executable:

```text
src/probe_recursive_current_latent_gadget.py
```

---

## 4. Certified retained-chain comparison

Across the four recorded transitions through the split fifth frontier:

```text
current-latent repeated resources  33
terminal current owners            33
recursive current owners            0
maximum combined ratio          33/64
```

Thus the recorded chain has no recursive current-latent correction. This finite fact is compatible with, but much stronger than, the universal bound.

Primary reference:

```text
docs/certified-current-latent-critical-packing.md
```

---

## 5. Correct coefficient hierarchy

At exponent one:

```text
current-latent residual <= 1/2;
latent-latent residual  <= 1, sharp.
```

At exponent two:

```text
current-latent complete load <= 3/4;
latent-latent complete load  <= 1.
```

Therefore exponent two eliminates all owner-multiplicity correction, while exponent one requires a separate occurrence/depth mechanism.

Primary correction:

```text
docs/coordinated-middle-half-scale-critical-no-go.md
```
