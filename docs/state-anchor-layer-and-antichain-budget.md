# State-anchor layering and antichain persistence budget

## Status

Exact second-stage compression of exact lifted-progression persistence.

After global lifted-center layering, the remaining multiplicity consists of repeated terminal uses of one exact root progression

```math
P(x,q)=\{x-q,x,x+q\}.
```

This note proves two further facts.

1. Terminal copies occurring in states with different root translation anchors can be resolved exactly into lower-scale four-term-progression-free anchor-difference children.
2. Copies that retain the same root anchor form an antichain in the occurrence genealogy of one root sponsor. Their multiplicity is bounded by the current local sponsor label, not merely by the root scale.

The only remaining persistence is therefore repetition of the same local progression in several incomparable recursive states with the same root translation anchor.

---

## 1. Every recursive state has a root anchor

Fix a root block

```math
D\subseteq[N,2N).
```

Every recursive state, after any required dyadic shell restriction, can be written as

```math
S=B-t,
\qquad
B\subseteq D,
```

where the root translation anchor satisfies

```math
t\in\{0\}\cup D.
```

The root state has anchor `t=0`.

Assume inductively that a state has the form `B-t`. A component child, merge child, or middle multiplicity-fiber child subtracts a local anchor of the form

```math
b_0-t
```

for some `b_0 in B subseteq D`. Therefore the child has the form

```math
B'-b_0
```

with `B' subseteq D`, so its new root anchor is `b_0 in D`.

Restricting to a dyadic shell only replaces `B'` by a subset and does not change the anchor.

Hence every nonroot recursive state is a translate by one root point of `D`.

---

## 2. Anchor multiplicity of one exact lifted progression

Fix a step `q` and lifted center `x`. Consider all terminal occurrences that lift to

```math
x-q,
\quad x,
\quad x+q
```

inside the root block.

For each root anchor `t`, let

```math
\lambda_{x,q}(t)
```

be the number of such terminal occurrences produced in recursive states with anchor `t`.

The root anchor `t=0` contributes at most one occurrence because the root state occurs only once and within-state middle labels are already distinct.

For nonroot anchors define

```math
\nu^+_{x,q}
=
\sum_{t\in D}\lambda_{x,q}(t)
```

and

```math
M_{x,q}
=
\max_{t\in D}\lambda_{x,q}(t).
```

For each integer `k>=1`, define the anchor layer

```math
A_{x,q}^{(k)}
=
\{t\in D:\lambda_{x,q}(t)\ge k\}.
```

The nonempty layers are nested and their number is exactly `M_{x,q}`. The layer-cake identity gives

```math
\boxed{
\nu^+_{x,q}
=
\sum_{k=1}^{M_{x,q}}|A_{x,q}^{(k)}|.
}
```

Each layer is a subset of the four-term-progression-free root set `D` and is therefore four-term-progression-free.

---

## 3. Anchor-difference children

For every nonempty layer choose

```math
t_{x,q,k}
=
\min A_{x,q}^{(k)}
```

and define

```math
\Gamma_{x,q,k}
=
\{t-t_{x,q,k}:
  t\in A_{x,q}^{(k)},
  \ t>t_{x,q,k}\}.
```

Because all nonroot anchors lie in `[N,2N)`, one has

```math
\Gamma_{x,q,k}\subseteq[1,N).
```

A four-term progression in `Gamma_{x,q,k}` would translate to one in `A_{x,q}^{(k)} subseteq D`. Hence

```math
\boxed{
\Gamma_{x,q,k}
\text{ is four-term-progression-free}.
}
```

Also,

```math
|\Gamma_{x,q,k}|
=
|A_{x,q}^{(k)}|-1.
```

Therefore

```math
\begin{aligned}
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|
&=
\sum_{k=1}^{M_{x,q}}|A_{x,q}^{(k)}|\\
&=
\nu^+_{x,q}.
\end{aligned}
```

Thus

```math
\boxed{
\nu^+_{x,q}
=
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|.
}
```

Interpretation:

- retain at most `M_{x,q}` terminal copies of `q`, one for each nonempty anchor layer;
- export every remaining different-anchor copy into a lower-scale four-term-progression-free anchor-difference child.

All multiplicity arising from distinct root translations is resolved exactly.

---

## 4. Harmonic lower bound for anchor resolution

Every terminal step produced below the root block satisfies

```math
q\le N/2.
```

Each retained terminal copy therefore contributes at least `2/N`. Every anchor-difference label lies below `N` and contributes more than `1/N`.

Consequently the anchor-resolved output for fixed `(x,q)` has harmonic mass at least

```math
\begin{aligned}
\frac{M_{x,q}}q
+
\sum_{k=1}^{M_{x,q}}H(\Gamma_{x,q,k})
&\ge
\frac{2M_{x,q}}N
+
\frac{\nu^+_{x,q}-M_{x,q}}N\\
&=
\frac{\nu^+_{x,q}+M_{x,q}}N\\
&\ge
\frac{\nu^+_{x,q}}N.
\end{aligned}
```

The possible root-anchor occurrence `t=0` is retained separately and contributes `1/q`.

---

## 5. The local sponsor label

The coordinated side-anchor orientation determines a sign

```math
\sigma(q)\in\{-1,+1\}
```

such that the root sponsor of `P(x,q)` is

```math
a=x-\sigma(q)q.
```

In a state with root anchor `t`, the local sponsor label is

```math
s(a,t)=a-t.
```

A terminal occurrence can occur only when `s(a,t)>0`.

Because its three-term progression lies in one dyadic shell, its step satisfies

```math
\boxed{q\le s(a,t)/2.}
```

---

## 6. Same-anchor copies form an antichain

Fix `x,q,t`, and consider all terminal copies counted by

```math
\lambda_{x,q}(t).
```

Every one of these copies is a descendant occurrence of the same root sponsor `a`, and every one has the same local sponsor label

```math
s=a-t.
```

Along every recursive edge, the associated positive label is at most one half of the parent label. Hence an occurrence of label `s` cannot be an ancestor of another occurrence of the same label `s`.

Therefore the copies counted by `lambda_{x,q}(t)` form an antichain in the descendant tree of root occurrence `a`.

---

## 7. Antichain conservation lemma

Consider any rooted occurrence tree with positive labels and the property

```math
\sum_{v\text{ child of }u}\ell(v)
\le
\ell(u)
```

at every node.

For every finite antichain `C`,

```math
\boxed{
\sum_{v\in C}\ell(v)
\le
\ell(\text{root}).
}
```

### Proof

Prune the tree below every node of `C`. Starting from the leaves and moving upward, replace the total label of selected descendants below a node by at most the label of that node. Repeating to the root gives the inequality.

The same statement follows by viewing the labels as a subprobability flow from the root.

---

## 8. Same-anchor persistence bound

Apply the antichain lemma to the copies with fixed `(x,q,t)`. Each has label

```math
s=a-t.
```

The root label is `a`. Hence

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le
 a.
}
```

Equivalently,

```math
\boxed{
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{a-t}\right\rfloor.
}
```

Since `a-t>=2q`, this implies

```math
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{2q}\right\rfloor.
```

This is stronger than charging every copy only by its terminal label `q`. The multiplicity is paid by the full local sponsor label `a-t`.

A useful geometric form is

```math
\boxed{
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
}
```

Thus high same-anchor persistence is possible only when the root anchor lies extremely close to the root sponsor.

For example,

```math
 t\le a/2
\quad\Longrightarrow\quad
\lambda_{x,q}(t)\le2.
```

---

## 9. Density-sensitive tail localization

For fixed exact progression `P(x,q)` and integer `m>=2`, define

```math
T_m(x,q)
=
\{t\in D:\lambda_{x,q}(t)\ge m\}.
```

The previous inequality gives

```math
T_m(x,q)
\subseteq
D\cap
\left[a-a/m,\ a\right).
```

Therefore

```math
\boxed{
|T_m(x,q)|
\le
r_4\!\left(\left\lceil a/m\right\rceil+1\right).
}
```

Here `r_4(L)` denotes the maximum size of a four-term-progression-free subset of an interval of length `L`.

The unresolved same-anchor multiplicity is therefore concentrated simultaneously:

1. near the bottom local scale `a-t`;
2. in a short interval of root anchors immediately below the sponsor `a`.

---

## 10. Revised residual

The multiplicity reduction now has three exact layers.

1. Different lifted centers are exported by global center-difference children.
2. For one exact lifted center, different root translation anchors are exported by anchor-difference children.
3. The remaining copies have the same step, lifted center, root sponsor, root anchor, and local sponsor label.

The final residual is

```math
\boxed{
\text{multiplicity of one identical local progression across incomparable recursive states}.
}
```

Such copies satisfy

```math
\lambda(a-t)\le a
```

and high multiplicity forces `t` into an interval of length `a/lambda` immediately below `a`.

The next target is to analyze the branching diamonds that create several incomparable states with the same root anchor. A closing theorem must either export those diamonds to additional lower-scale difference structure or prove that near-maximal repeated convergence forces a forbidden affine configuration in the root set.
