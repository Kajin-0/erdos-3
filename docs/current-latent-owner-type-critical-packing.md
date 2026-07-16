# Current-latent owner-type critical packing

## Status

State-independent critical-scale refinement for one repeated parent pair with exactly one current owner and one recursive latent owner in the coordinated-deletion output architecture.

The source type determines the sharp correction:

```text
backbone current + middle latent -> zero correction;
middle current + backbone latent -> correction at most one quarter.
```

The second coefficient is sharp under the actual lexicographic deletion and point-disjoint retained policy.

---

## 1. Setup

Let a parent state lie in a standard dyadic shell of base `N`. Fix one physical parent resource

```math
f=\{x,y\},
\qquad g=y-x.
```

Suppose `f` has exactly:

```text
one current owner;
one recursive latent owner.
```

For a current child shell of base `L_cur`, the current occurrence contributes

```math
\frac{L_{\rm cur}}g
```

to the critical harmonic coordinate.

For a recursive latent child shell of base `L_lat`, the latent occurrence contributes

```math
\frac{2L_{\rm lat}}g
```

to the doubled critical pair coordinate.

The parent critical pair unit is

```math
\frac Ng.
```

---

## 2. Output-scale bounds

The coordinated-deletion geometry gives:

```text
backbone child shell base <= N/2;
middle-fiber child shell base <= N/4.
```

These are the same scale bounds used by the full-edge critical majorant.

---

## 3. Backbone current and middle latent

If the current owner is a backbone child and the latent owner is a middle child, then

```math
L_{\rm cur}\le\frac N2,
\qquad
L_{\rm lat}\le\frac N4.
```

Therefore

```math
L_{\rm cur}+2L_{\rm lat}
\le
\frac N2+2\frac N4
=N.
```

Hence the one parent pair unit pays both owners:

```math
\boxed{
\frac{L_{\rm cur}}g+
\frac{2L_{\rm lat}}g
\le
\frac Ng.
}
```

No current-latent correction is required in this orientation.

---

## 4. Middle current and backbone latent

If the current owner is a middle child and the latent owner is a backbone child, then

```math
L_{\rm cur}\le\frac N4,
\qquad
L_{\rm lat}\le\frac N2.
```

Thus

```math
L_{\rm cur}+2L_{\rm lat}
\le
\frac N4+N
=
\frac54N.
```

After the parent unit pays the backbone latent occurrence, the only possible residual is the middle current occurrence:

```math
\boxed{
\operatorname{Res}_{\rm cur-lat}(f)
\le
\frac14\frac Ng.
}
```

This improves the previous source-blind estimate `1/2`.

---

## 5. Sharp shell-valid counterexample

Consider

```math
P=
\{65,97,98,99,113,114,115,119,120,121,125,126,127\}
\subset[64,128).
```

The set is four-AP-free. Under the actual lexicographic deletion and maximum-harmonic point-disjoint retained policy, it keeps:

```text
recursive middle child:
  reference 97
  roots     {113,119,125}
  values    {16,22,28}
  shell base 16

recursive backbone child:
  reference 65
  roots     {97,98,99,113,114,115,119,120,121,125,126,127}
  values    {32,33,34,48,49,50,54,55,56,60,61,62}
  shell base 32
```

The three resources

```text
{97,113}, {97,119}, {97,125}
```

are current in the recursive middle child and latent in the recursive backbone child.

For each resource,

```math
N=64,
\qquad
L_{\rm cur}=16,
\qquad
L_{\rm lat}=32.
```

Therefore

```math
\frac{L_{\rm cur}+2L_{\rm lat}}N
=
\frac{16+64}{64}
=
\boxed{\frac54}.
```

The zero-correction conjecture fails, and the residual coefficient `1/4` is attained exactly.

Primary executable:

```text
src/probe_recursive_current_latent_gadget.py
```

---

## 6. Certified retained-chain comparison

Across the four recorded retained transitions through the split fifth frontier, every current-latent current owner is terminal. Their maximum complete ratio is only

```math
\frac{33}{64}.
```

Thus the recorded chain has zero recursive current-latent correction, but this is not universal.

Primary reference:

```text
docs/certified-current-latent-critical-packing.md
```

---

## 7. Updated overlap coefficients

The critical overlap row now has the exact source-type hierarchy:

```text
current-latent:
  backbone current / middle latent  -> 0
  middle current / backbone latent  -> at most 1/4, sharp

latent-latent:
  matched center/opposite reserve   -> 0
  unmatched middle export           -> at most 1/2
```

Because the current-latent and latent-latent profiles are mutually exclusive for one parent pair, the complete universal overlap coefficient remains `1/2`, but only the unmatched latent-latent case can attain that value.

The current-latent component should henceforth use `1/4`, not `1/2`.
