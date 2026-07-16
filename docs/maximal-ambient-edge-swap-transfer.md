# Maximal-ambient edge-swap transfer

## Status

State-independent local transfer theorem for terminal target pairs in one
dyadic shell of an inclusion-maximal four-AP-free ambient set.

The theorem combines:

```text
source first-use/collision partition;
local completed-edge capacity;
weight-preserving cross-shell edge swap;
capacity-aware certified-hole light/heavy transfer.
```

In the maximal ambient model, the local terminal-pair row has no anonymous
completion remainder.

---

## 1. Dyadic shell in a maximal ambient set

Let

```math
B\subseteq\mathbb N
```

be inclusion-maximal four-AP-free, and put

```math
P=B\cap[N,2N).
```

Let `A` be a finite activated physical pair set inside `P`, and let

```math
T:A\to Z
```

be a monotone terminal transport map with target pairs `Z subseteq binom(P,2)`.

Choose one deterministic maximum-weight source for each target and let

```math
C_{\rm src}
```

be the remaining source-collision pair set. Then

```math
J(A)
\le
J(Z)+J(C_{\rm src}).
```

Every pair in `C_src` has both endpoints in `P`.

---

## 2. Selected completion trichotomy

Give every target pair `z={x,y}`, `x<y`, one selected positive integer
completion `c` forming a three-AP with `x,y`.

Because `B` is maximal, exactly one of the following holds.

### Local root

```math
c\in B\cap[N,2N)=P.
```

Then `z` is an edge of a three-AP lying entirely in `P`.

### Cross-shell root

```math
c\in B\setminus P.
```

For endpoints in one shell this can occur only for an adjacent-edge completion.

### Ambient hole

```math
c\notin B.
```

Then `c` has a four-AP witness using three points of `B`.

Thus

```math
Z
=
Z_{\rm local}
\sqcup
Z_{\rm cross}
\sqcup
Z_{\rm hole}.
```

---

## 3. Local completed-edge capacity

Every target in `Z_local` is a physical edge of a three-AP in `P`. Therefore

```math
\boxed{
J(Z_{\rm local})
\le
\frac52\mathcal L_3(P).
}
```

All possible local completions are tested; the selected transport completion
need not be the first local witness.

---

## 4. Cross-shell edge swap

Suppose first that the selected completion is to the left:

```math
c=x-(y-x),
\qquad
c\in B\setminus P.
```

Define

```math
\rho(z,c)=\{c,x\}.
```

Both pairs are adjacent edges of the same three-AP, so

```math
w(\rho(z,c))
=
\frac1{x-c}
=
\frac1{y-x}
=
w(z).
```

For a right completion

```math
c=y+(y-x),
```

define

```math
\rho(z,c)=\{y,c\}.
```

Again `w(rho)=w(z)`.

The map is injective on tagged cross-shell targets. Indeed:

```text
from {c,x} with c<N<=x, recover y=2x-c;
from {y,c} with y<2N<=c, recover x=2y-c.
```

Let

```math
E_{\rm cross}
=
\rho(Z_{\rm cross}).
```

Then

```math
\boxed{
J(Z_{\rm cross})
=
J(E_{\rm cross}).
}
```

Every pair in `E_cross` has one endpoint outside `P`, whereas every pair in
`C_src` lies inside `P`. Hence

```math
\boxed{
E_{\rm cross}\cap C_{\rm src}=\varnothing.
}
```

---

## 5. Capacity-aware ambient-hole transfer

For every target in `Z_hole`, assign the selected completion its canonical
four-AP witness support pair. Form its adjacent or outer completion-step fiber
with the appropriate weight coefficient.

Reserve the physical pair set

```math
R
=
C_{\rm src}\cup E_{\rm cross}.
```

A support pair in `R` emits no light fiber. Every unreserved support uses the
adaptive share threshold from the maximal-ambient completion theorem.

Let

```math
F_{\rm light}
```

be the resulting light-support union and `H_max` the weighted heavy-fiber
family. Then

```math
F_{\rm light}\cap R=\varnothing
```

and

```math
J(Z_{\rm hole})
\le
J(F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm max}}\alpha(S)H(S),
```

where `alpha(S)` is `1` for adjacent completion roles and `1/2` for outer roles.

---

## 6. Complete maximal-ambient row

Combining the source partition, local edge capacity, cross-shell edge swap, and
capacity-aware hole transfer gives

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(C_{\rm src}\cup E_{\rm cross}\cup F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm max}}\alpha(S)H(S).
}
```

The outgoing pair union is disjoint by construction:

```text
C_src:       both endpoints inside P;
E_cross:     one endpoint outside P;
F_light:     explicitly unreserved.
```

Every remaining heavy fiber is four-AP-free and descends strictly below the
current shell:

```text
adjacent role: resolved base at most N/2;
outer role:    resolved base at most N/4.
```

There is no `M_amb` term.

---

## 7. Terminal/recursive form

After dyadic resolution, split the heavy family into terminal and recursive
shells. The complete row becomes

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm out})
+
\operatorname{TermSink}_{\rm first}
+
\sum_{R\in\mathcal R_{\rm heavy}}\alpha(R)H(R)
+
\operatorname{TermRecreate},
}
```

where

```math
E_{\rm out}
=
C_{\rm src}\cup E_{\rm cross}\cup F_{\rm light}.
```

This is the desired local resource vocabulary:

```text
completed local AP capacity;
outgoing physical pair energy;
terminal first appearance;
strictly lower-scale recursive fibers.
```

---

## 8. Remaining global theorem

The local completion problem is now closed in the maximal ambient model. The
remaining work is global:

1. prove first-appearance packing for outgoing pair unions from different
   parent shells;
2. control entering pair energy before affine contraction begins;
3. pack terminal sink recreation;
4. combine one-level and two-level heavy-fiber descent with the Bellman
   potential;
5. control cross-parent root-pair reuse when outgoing cross-shell edges enter a
   different dyadic block.
