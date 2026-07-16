# Direct maximal-ambient activated-pair discharge

## Status

State-independent replacement for the sponsor-pair terminal transport row in an inclusion-maximal four-AP-free ambient set.

The key observation is that an activated physical pair does not need to be transported before its completion geometry is used. The pair itself has positive three-AP completions. Maximality classifies each selected completion as an actual ambient root or a certified four-AP hole.

By reserving the entire entering activated pair union before allocating hole-support capacity, the resulting row has:

```text
no source-collision term;
no anonymous ambient term;
no pair used both as entering debt and light support;
a genuinely new outgoing pair union.
```

---

## 1. Activated pair family

Let

```math
B\subseteq\mathbb N
```

be inclusion-maximal four-AP-free, and put

```math
P=B\cap[N,2N).
```

Let

```math
A\subseteq\binom P2
```

be any finite physical activated pair set. No deletion schedule or sponsor transport map is required.

For

```math
z=\{x,y\},
\qquad x<y,
\qquad D=y-x,
```

the positive integer three-AP completion candidates are

```math
x-D,
\qquad
y+D,
```

and, when `D` is even,

```math
x+D/2.
```

All endpoint completions are positive because `x>=N` and `D<N`. The midpoint, when integral, lies in `[N,2N)`.

---

## 2. Deterministic completion priority

Assign every activated pair one completion by the following deterministic priority.

### Local root

If any completion belongs to `P`, choose the least tagged local witness. Put the pair in

```math
A_{\rm local}.
```

### Cross-shell root

Otherwise, if an endpoint completion belongs to `B\setminus P`, choose it and put the pair in

```math
A_{\rm cross}.
```

An integral midpoint root would lie in `P`, so every cross-shell root is necessarily an adjacent completion.

Both endpoint completions cannot belong to `B`: together with `x,y` they would form a four-AP. Thus the cross-shell root is unique when it exists.

### Maximality hole

If no completion belongs to `B`, choose one deterministic candidate and put the pair in

```math
A_{\rm hole}.
```

Maximality supplies a four-AP witness through the selected completion using three roots of `B`.

Therefore

```math
A
=
A_{\rm local}
\sqcup
A_{\rm cross}
\sqcup
A_{\rm hole}.
```

---

## 3. Local-root payment

Every pair in `A_local` is an edge of a three-AP contained entirely in `P`. The complete physical edge union of one three-AP of step `d` has energy

```math
\frac1d+\frac1d+\frac1{2d}
=
\frac5{2d}.
```

Consequently

```math
\boxed{
J(A_{\rm local})
\le
\frac52\mathcal L_3(P).
}
```

Each local physical edge is counted only once even if it belongs to several three-AP witnesses.

---

## 4. Cross-shell root swap

For a left completion

```math
c=x-D\in B\setminus P,
```

define

```math
\rho(z)=\{c,x\}.
```

For a right completion

```math
c=y+D\in B\setminus P,
```

define

```math
\rho(z)=\{y,c\}.
```

The target and image are adjacent edges of the same three-AP, so

```math
w(\rho(z))=w(z).
```

The global cross-shell injectivity theorem shows that one physical image has at most one target preimage. Let

```math
E_{\rm cross}=\rho(A_{\rm cross}).
```

Then

```math
\boxed{
J(A_{\rm cross})=J(E_{\rm cross}).
}
```

Every pair in `A` has both endpoints in `P`, while every pair in `E_cross` has endpoints in two different standard dyadic shells. Hence

```math
\boxed{
E_{\rm cross}\cap A=\varnothing.
}
```

---

## 5. Capacity-aware maximality-hole fibers

For every selected hole completion `c`, choose a deterministic four-AP witness and its canonical adjacent support pair

```math
f(c)\subseteq B.
```

Group the activated hole targets by completion role:

```text
left adjacent;
right adjacent;
outer/midpoint.
```

The associated weighted role loads are respectively

```math
H(S_c^-),
\qquad
H(S_c^+),
\qquad
\frac12H(S_c^0).
```

One canonical support pair serves at most two holes, and each hole has at most three roles. Thus one support indexes at most six role fibers:

```math
m(f)\le6.
```

Reserve the entire physical pair set

```math
R=A\cup E_{\rm cross}.
```

If `f in R`, declare every role fiber on `f` heavy. Otherwise call a weighted role fiber of load `L_i` light when

```math
L_i
\le
\frac1{m(f)}w(f).
```

Let `F_light` be the physical union of supports carrying at least one light role fiber. Then

```math
F_{\rm light}\cap R=\varnothing
```

and

```math
\boxed{
J(A_{\rm hole})
\le
J(F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm direct}}\alpha(S)H(S),
}
```

where `alpha=1` for adjacent roles and `alpha=1/2` for outer roles.

Every heavy fiber is four-AP-free. Adjacent fibers resolve to shell bases at most `N/2`; outer fibers resolve to bases at most `N/4`.

---

## 6. Direct discharge theorem

Combining the three classes gives

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
\sum_{S\in\mathcal H_{\rm direct}}\alpha(S)H(S),
}
```

where

```math
E_{\rm new}
=
E_{\rm cross}\cup F_{\rm light}.
```

Moreover,

```math
\boxed{
E_{\rm new}\cap A=\varnothing.
}
```

Thus all entering activated pair capacity is discharged into exactly three approved resources:

```text
local three-AP edge capacity;
genuinely new physical pair capacity;
strictly lower-scale four-AP-free heavy fibers.
```

There is no carried source-collision subset because no many-to-one transport map is introduced.

---

## 7. Simultaneous shell form

For a finite family of standard dyadic shells

```math
P_j=B\cap[2^j,2^{j+1})
```

and activated pair sets

```math
A_j\subseteq\binom{P_j}{2},
```

apply the completion priority to the global physical union

```math
A=\bigcup_jA_j.
```

The entering sets are disjoint across shells. Cross-shell swap images are globally injective. Canonical support multiplicity is globally at most six. Reserving all entering and cross-shell pairs before light allocation gives

```math
\boxed{
\sum_jJ(A_j)
\le
\frac52\sum_j\mathcal L_3(P_j)
+
J(E_{\rm new})
+
\sum_{S\in\mathcal H_{\rm direct}}\alpha(S)H(S),
}
```

with `E_new` a global physical pair union disjoint from every entering `A_j`.

---

## 8. Consequence for the proof program

The economical activation problem does not require sponsor-pair transport after passing to a maximal ambient set. Direct completion of the activated pair is stronger:

```text
sponsor transport:
  entering A -> terminal target union + source-collision pair reserve;

direct maximal completion:
  entering A -> local edge capacity + new pair union + lower-scale fibers.
```

The source-collision term disappears rather than being estimated.

Sponsor-pair transport remains a valid finite diagnostic and may still expose useful parity or deletion-order structure. It is no longer necessary for the maximal-ambient pair-discharge theorem.

---

## 9. Remaining global obligations

The theorem does not by itself prove the full reciprocal-sum result. The remaining obligations are:

1. telescope genuinely new pair capacity across recursive affine coordinates;
2. control terminal first appearance and recreation of heavy fibers;
3. process the recursive heavy fibers using their strict scale descent;
4. connect the local three-AP edge expenditure to the global branching production inequality;
5. verify that every activated pair family used by the retained proof has a sound physical root embedding before applying the theorem.

The local pair-activation bottleneck itself is removed in the maximal ambient model.