# Three-AP occurrence-family light/heavy transfer

## Status

State-independent transfer theorem for an arbitrary selected family of
distinct three-AP occurrences inside a four-AP-free dyadic block.

The theorem applies both to the entering parent three-AP family and to selected
recursive collision-preimage families. It decomposes occurrence load into
activated physical-pair capacity plus heavy lower-scale four-AP-free fibers.

---

## 1. Selected occurrence family

Let

```math
B\subseteq[N,2N)
```

be four-AP-free. Let

```math
\mathcal A
\subseteq
\{(p,d):p,p+d,p+2d\in B\}
```

be any set of distinct three-AP occurrences.

Its weighted occurrence load is

```math
L(\mathcal A)
=
\sum_{(p,d)\in\mathcal A}\frac1d.
```

No assumption is made that `A` contains every three-AP of `B`.

---

## 2. Canonical base occurrence for each step

For each used step `d`, define

```math
P_d^{\mathcal A}
=
\{p:(p,d)\in\mathcal A\}
```

and choose

```math
a_d=\min P_d^{\mathcal A}.
```

The base occurrence contributes one first-step token

```math
e_d=\{a_d,a_d+d\}
```

of weight `1/d`.

Distinct steps give distinct base-edge tokens: the pair `e_d` determines both
its left endpoint and its gap `d`.

Define

```math
E_{\rm step}(\mathcal A)
=
\{e_d:P_d^{\mathcal A}\ne\varnothing\}.
```

Then

```math
\boxed{
\sum_{e\in E_{\rm step}(\mathcal A)}w(e)
=
\sum_{d:P_d^{\mathcal A}\ne\varnothing}\frac1d.
}
```

---

## 3. Anchor-pair fibers

For every nonbase occurrence `(p,d)`, define the canonical anchor pair

```math
f=\{a_d,p\}.
```

For one parent pair `f={a,p}`, define

```math
S_f^{\mathcal A}
=
\{d:a_d=a,\ p\in P_d^{\mathcal A}\}.
```

Exactly as in the complete-family transpose,

```math
\boxed{
L(\mathcal A)
=
\sum_{e\in E_{\rm step}(\mathcal A)}w(e)
+
\sum_fH(S_f^{\mathcal A}).
}
```

Every fiber is four-AP-free because

```math
a+S_f^{\mathcal A}\subseteq B.
```

Every fiber step is below `N/2`; after standard dyadic resolution, all fiber
shell bases satisfy `M<=N/4`.

---

## 4. Light and heavy fibers

Let

```math
\delta(f)=|p-a|
```

for `f={a,p}`.

Call the fiber light when

```math
H(S_f^{\mathcal A})
\le
\frac1{\delta(f)}
=
w(f),
```

and heavy otherwise.

Let

```math
E_{\rm light}(\mathcal A)
=
\{f:S_f^{\mathcal A}\text{ is light and nonempty}\}.
```

Then

```math
\sum_{f\in E_{\rm light}}
H(S_f^{\mathcal A})
\le
\sum_{f\in E_{\rm light}}w(f).
```

Therefore

```math
\boxed{
L(\mathcal A)
\le
J(E_{\rm step})
+
J(E_{\rm light})
+
\sum_{f\in E_{\rm heavy}}H(S_f^{\mathcal A}),
}
```

where `J(E)=sum_{e in E}w(e)`.

The final term is genuine lower-scale recursive mass, not an unpaid scalar
coefficient.

---

## 5. Activated pair-union form

Put

```math
E_{\rm act}
=
E_{\rm step}\cup E_{\rm light}.
```

Each physical pair appears at most once in `E_step` and at most once in
`E_light`. Hence

```math
J(E_{\rm step})+J(E_{\rm light})
\le
2J(E_{\rm act}).
```

Thus

```math
\boxed{
L(\mathcal A)
\le
2J(E_{\rm act})
+
\sum_{f\in E_{\rm heavy}}H(S_f^{\mathcal A}).
}
```

This coefficient two is an exact worst-case union bound. The intersection
`E_step intersect E_light` is fully identified and may admit a sharper role
allocation, but no anonymous multiplicity is hidden.

---

## 6. Heavy-fiber certificate

If `f` is heavy, then

```math
H(S_f^{\mathcal A})
>
w(f).
```

The parent contains the four affine layers

```math
(a+S_f),
\qquad
(a+2S_f),
\qquad
(p+S_f),
\qquad
(p+2S_f).
```

Thus a heavy fiber has two simultaneous certificates:

```text
its harmonic mass exceeds the anchor-pair capacity it replaces;
it is a lower-scale four-AP-free state with a forced rectangle embedding in B.
```

Heavy fibers are therefore the only recursively persistent collision debt.
Light fibers terminate into physical-pair capacity.

---

## 7. Application to recursive collision preimages

Fix one full-edge completion type and one set of excess child three-AP
preimages after parent-target first appearance has been removed.

For a fixed base reference, completion transport is injective on target
three-APs, so the preimages form a set of distinct three-AP occurrences inside
the oriented child root set. Apply the present theorem shell by shell.

The type collision exposure therefore decomposes into:

```text
distinct child step-edge pairs;
light child anchor pairs;
heavy lower-scale step fibers.
```

This is the same transfer architecture at root entry and at recursive
transport collisions.

---

## 8. Strategic consequence

The former collision excess `Y(P)` is no longer atomic. It can be recursively
expanded by the light/heavy rule:

```text
first step -> activated physical pair;
light repeated step -> activated anchor pair;
heavy repeated step -> lower-scale four-AP-free fiber.
```

The remaining whole-tree theorem must merge activated physical-pair first
appearances across parent states and control overlap among heavy fibers.
Because heavy fibers descend by at least two dyadic levels, this is a narrower
packing problem than the original latent-pair activation question.
