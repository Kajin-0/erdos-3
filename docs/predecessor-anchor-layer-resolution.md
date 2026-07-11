# Predecessor-anchor layer resolution

## Status

Exact third-stage compression of terminal persistence after lifted-center and root-anchor layering.

Fix one exact lifted progression

```math
P(x,q)=\{x-q,x,x+q\}
```

and one root translation anchor `t`. Suppose several incomparable recursive states anchored at `t` emit the same terminal step `q` from this exact progression.

This note groups those copies by the root anchor of their immediate parent state. Every copy arising from a different predecessor anchor is exported to a lower-scale four-term-progression-free difference child.

The remaining atom is repeated use of the same ordered anchor transition

```math
p\longrightarrow t.
```

---

## 1. Root anchors along an occurrence path

Let

```math
a=x-\sigma(q)q
```

be the root sponsor of `P(x,q)`.

A recursive state anchored at `u` contains the sponsor with local label

```math
s(u)=a-u>0.
```

If a child state has anchor `v`, the half-contraction theorem gives

```math
s(v)\le\frac12s(u).
```

Equivalently,

```math
a-v\le\frac12(a-u),
```

so

```math
\boxed{
v\ge\frac{a+u}{2}>u.
}
```

Thus root anchors increase strictly along every descendant path toward the fixed root sponsor `a`.

In particular, root anchors never repeat along one path.

---

## 2. Immediate predecessor multiplicities

Fix a target anchor `t`. Every terminal copy counted by

```math
\lambda_{x,q}(t)
```

occurs in a state with one immediate parent state, except for a possible root-state occurrence.

Let

```math
c_{x,q,t}(p)
```

be the number of copies whose immediate parent state has root anchor `p` and whose terminal state has root anchor `t`.

For nonroot predecessor anchors,

```math
p\in D_{\mathrm{root}}.
```

The root predecessor `p=0` is treated separately. The root state occurs only once and creates at most two child states, so

```math
c_{x,q,t}(0)\le2.
```

For nonroot predecessors define

```math
\lambda^+_{x,q}(t)
=
\sum_{p\in D}c_{x,q,t}(p)
```

and

```math
C_{x,q}(t)
=
\max_{p\in D}c_{x,q,t}(p).
```

---

## 3. Predecessor anchor layers

For each integer `k>=1`, define

```math
P_{x,q,t}^{(k)}
=
\{p\in D:c_{x,q,t}(p)\ge k\}.
```

The nonempty layers are nested, and their number is exactly `C_{x,q}(t)`. The layer-cake identity gives

```math
\boxed{
\lambda^+_{x,q}(t)
=
\sum_{k=1}^{C_{x,q}(t)}
|P_{x,q,t}^{(k)}|.
}
```

Every layer is a subset of the root four-term-progression-free set `D`.

---

## 4. Predecessor-difference children

For each nonempty layer choose

```math
p_{x,q,t,k}
=
\min P_{x,q,t}^{(k)}
```

and define

```math
\Lambda_{x,q,t,k}
=
\{p-p_{x,q,t,k}:
  p\in P_{x,q,t}^{(k)},
  \ p>p_{x,q,t,k}\}.
```

Since all nonroot predecessor anchors lie in `[N,2N)`,

```math
\Lambda_{x,q,t,k}\subseteq[1,N).
```

A four-term progression in `Lambda_{x,q,t,k}` would translate to one in `P_{x,q,t}^{(k)} subseteq D`. Hence

```math
\boxed{
\Lambda_{x,q,t,k}
\text{ is four-term-progression-free}.
}
```

Also,

```math
|\Lambda_{x,q,t,k}|
=
|P_{x,q,t}^{(k)}|-1.
```

Therefore

```math
\begin{aligned}
C_{x,q}(t)
+
\sum_{k=1}^{C_{x,q}(t)}
|\Lambda_{x,q,t,k}|
&=
\sum_{k=1}^{C_{x,q}(t)}
|P_{x,q,t}^{(k)}|\\
&=
\lambda^+_{x,q}(t).
\end{aligned}
```

Thus

```math
\boxed{
\lambda^+_{x,q}(t)
=
C_{x,q}(t)
+
\sum_{k=1}^{C_{x,q}(t)}
|\Lambda_{x,q,t,k}|.
}
```

Interpretation:

- retain at most `C_{x,q}(t)` copies associated with one predecessor anchor;
- export every copy arising from a different predecessor anchor to a lower-scale four-term-progression-free predecessor-difference child.

The possible root-predecessor contribution `c(0)<=2` is retained separately.

---

## 5. Predecessor interval localization

The parent state anchored at `p` has local sponsor label

```math
A=a-p.
```

The child state anchored at `t` has local sponsor label

```math
s=a-t.
```

Half-contraction gives

```math
s\le A/2.
```

Equivalently,

```math
\boxed{
p\le2t-a<t.
}
```

Thus all predecessor anchors of a fixed target anchor `t` lie in the interval

```math
[N,\ 2t-a].
```

Its length is at most

```math
2(t-N)-a+N,
```

and shrinks rapidly when `t` is close to `a`.

---

## 6. Same-transition antichain budget

Fix one ordered transition

```math
p\longrightarrow t.
```

All parent occurrences producing copies counted by `c_{x,q,t}(p)` have the same positive local sponsor label

```math
A=a-p.
```

Two occurrences of the same label `A` cannot be ancestor and descendant because labels strictly halve along recursive edges. Hence these parent occurrences form an antichain in the descendant tree of root sponsor `a`.

The antichain conservation lemma gives

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

Therefore

```math
\boxed{
c_{x,q,t}(p)
\le
\left\lfloor\frac{a}{a-p}\right\rfloor.
}
```

Since

```math
a-p\ge2(a-t),
```

one also has

```math
c_{x,q,t}(p)
\le
\left\lfloor
\frac{a}{2(a-t)}
\right\rfloor.
```

A high-multiplicity transition must therefore begin extremely close to the root sponsor:

```math
c_{x,q,t}(p)\ge m
\quad\Longrightarrow\quad
p\ge a\left(1-\frac1m\right).
```

---

## 7. Iterated anchor-history compression

The same construction can be iterated backward.

After fixing the target anchor `t` and predecessor anchor `p`, group the remaining copies by the anchor preceding `p`. Different earlier anchors again form subsets of the root four-term-progression-free set and can be exported by layer translation.

After `h` backward stages, the residual copies share an identical root-anchor history

```math
t_0<t_1<\cdots<t_h=t.
```

The corresponding sponsor gaps satisfy

```math
a-t_{j+1}
\le
\frac12(a-t_j).
```

Hence

```math
h
\le
\left\lfloor
\log_2\frac{a}{a-t}
\right\rfloor.
```

The anchor-history depth is logarithmic.

---

## 8. Revised residual atom

The multiplicity compression now proceeds through four levels.

1. Different lifted centers are exported by center layers.
2. Different target anchors are exported by root-anchor layers.
3. Different predecessor anchors are exported by predecessor-anchor layers.
4. The process may be iterated through the complete anchor history.

The unresolved atom is

```math
\boxed{
\text{multiple state occurrences with the same complete anchor history and the same local progression}.
}
```

Such multiplicity can arise only when one parent occurrence creates two aligned child states with the same next anchor, as in the sharp middle-backbone diamond, and when those aligned duplications recur coherently along several copies of the same anchor history.

The next target is therefore no longer arbitrary convergence. It is a self-replication theorem for an aligned anchor-history diamond:

```math
\boxed{
\text{can the sharp one-step aligned diamond repeat along the same anchor history without forcing a four-term progression?}
}
```
