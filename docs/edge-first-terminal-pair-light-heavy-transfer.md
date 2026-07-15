# Edge-first terminal-pair light/heavy transfer

## Status

State-independent composition theorem for one activated physical-pair family in
a four-AP-free dyadic parent.

The theorem combines:

```text
source-weighted sponsor-pair transport;
full three-AP edge capacity;
completion-step fiber light/heavy transfer.
```

It gives the correct terminal-payment row without recursively activating every
certified-hole witness pair.

---

## 1. Activated source family

Let

```math
P\subseteq[N,2N)
```

be four-AP-free and equipped with one deterministic deletion schedule. Let

```math
A
```

be any finite set of activated physical root pairs. Apply monotone sponsor-pair
transport to every source pair. Write

```math
T(e)=z
```

for the terminal target of `e` and

```math
Z=T(A)
```

for the physical terminal-target union.

For each `z in Z`, choose one source of maximum initial pair weight,

```math
e_z^*\in T^{-1}(z).
```

Define the source-weighted collision term

```math
R_{\rm src}(A)
=
\sum_{z\in Z}
\sum_{\substack{e:T(e)=z\\e\ne e_z^*}}
w(e).
```

Then

```math
\sum_{e\in A}w(e)
=
\sum_{z\in Z}w(e_z^*)
+
R_{\rm src}(A)
\le
J(Z)+R_{\rm src}(A).
```

Thus

```math
\boxed{
J(A)
\le
J(Z)+R_{\rm src}(A).
}
```

---

## 2. Edge-first target partition

Partition the terminal targets into three disjoint classes.

### Three-AP edge targets

Let `Z_edge` contain every target that is an edge of at least one three-term
progression in the available parent or ambient root universe used for the
current transfer.

The full-edge capacity theorem gives

```math
\boxed{
J(Z_{\rm edge})
\le
\frac52\mathcal L_3(P).
}
```

The test uses every possible completion of the physical pair, not only the
completion prescribed by its terminal transport class.

### Certified same-shell holes

After edge-supported targets are removed, let `Z_hole` contain targets assigned
one selected completion

```math
c\in[N,2N)\setminus P
```

that has an explicit four-AP witness using three points of `P`.

The target and selected completion determine one orientation and step:

```math
z
=
\{c+\sigma d,c+2\sigma d\},
\qquad
\sigma\in\{-1,+1\}.
```

### Ambient remainder

Let `Z_amb` contain the remaining targets. This includes, depending on the
ambient model:

```text
admissible same-shell extensions;
completions present outside the current parent lineage;
outside-shell completions;
completion obligations not yet certified by a three-root hole witness.
```

Write

```math
M_{\rm amb}=J(Z_{\rm amb}).
```

Therefore

```math
J(Z)
=
J(Z_{\rm edge})
+
J(Z_{\rm hole})
+
M_{\rm amb}.
```

---

## 3. Completion-step transfer on the hole class

Assign every certified completion `c` its deterministic canonical adjacent
witness pair `f(c)`. For each completion and orientation form the four-AP-free
completion-step fiber

```math
S_{c,\sigma}
=
\{d:\{c+\sigma d,c+2\sigma d\}\in Z_{\rm hole}\}.
```

Group these fibers by physical support pair. Use the adaptive threshold

```math
H(S_{c,\sigma})
\le
\frac1{m(f)\,\operatorname{gap}(f)}
```

for light fibers, where `m(f)<=4` is the number of nonempty oriented fibers
assigned to `f`.

Let

```math
F_{\rm light}
```

be the physical union of support pairs carrying at least one light fiber, and
let

```math
\mathcal H_{\rm comp}
```

be the family of heavy completion-step fibers. The completion-step transfer
proves

```math
\boxed{
J(Z_{\rm hole})
\le
J(F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm comp}}H(S).
}
```

Every heavy output is four-AP-free and resolves only into dyadic shells with
base at most `N/4`.

---

## 4. Master terminal-payment inequality

Combining the source-weighted transport identity, the edge-first partition,
the full-edge capacity theorem, and the completion-step transfer gives

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm comp}}H(S)
+
M_{\rm amb}
+
R_{\rm src}(A).
}
```

Every term has a distinct role:

```text
(5/2)L3(P)             completed physical target edges;
J(F_light)             one activation per light witness-support identity;
H_comp                 named lower-scale four-AP-free recursive fibers;
M_amb                  genuine ambient or cross-scale completion obligations;
R_src                   exact extra source-pair mass after target first use.
```

No terminal-weight collision coefficient and no support-rewrite rank appear.

---

## 5. First-appearance form

Suppose a global physical-pair ledger `E_seen` already contains some light
support identities. Only new identities must be activated:

```math
F_{\rm new}
=
F_{\rm light}\setminus E_{\rm seen}.
```

Then

```math
J(E_{\rm seen}\cup F_{\rm light})
=
J(E_{\rm seen})+J(F_{\rm new}).
```

Thus the pair output is collision-sound under physical first appearance.
Repeated use of an existing support identity creates no new pair token.

The master row may therefore be inserted into a whole-tree ledger with

```math
J(F_{\rm light})
```

replaced by the increment

```math
J(F_{\rm new})
```

when the previously seen union is carried explicitly.

---

## 6. Why a universal support rank is unnecessary

The exact `S7` diagnostic shows that recursively activating every canonical
support identity happens to terminate after five layers. Exact rank searches
also show that this finite support graph is not governed by any tested simple
coordinate, gap, dyadic, sponsor-rank, short lexicographic, small affine, or
seven-state affine potential.

The present theorem explains why this is not the required universal object.

```text
light certified-hole fibers terminate into one support pair;
heavy certified-hole fibers recurse directly at lower scale.
```

Only the light support union enters sponsor-pair transport. The heavy class does
not remain in the support rewrite graph.

---

## 7. Remaining whole-tree problem

The terminal target itself is now resolved into approved resource types. The
remaining global obligations are narrower:

1. control first appearances of light support pairs across distinct parents;
2. apply the existing occurrence-family light/heavy transfer to
   `R_src(A)` and other collision-preimage families;
3. control overlap among lower-scale heavy fibers;
4. absorb the two-level scale descent into the Bellman potential;
5. resolve the true ambient remainder `M_amb` by maximality or cross-block
   transport.

This is the correct interface for the next LP or Bellman search. A rank for the
finite `S7` support cascade is not.
