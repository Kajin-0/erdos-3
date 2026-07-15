# Source-weighted sponsor-pair transport collision

## Status

State-independent refinement of sponsor-pair forward transport.

The existing terminal-target collision row charges every additional source pair
at the terminal target weight. Forward transport makes that valid, but it can be
strictly wasteful because pair weight may increase along the transport path.
This note keeps the actual source weights and gives a smaller exact collision
term.

---

## 1. Transport fibers

Let `A` be a finite set of activated pair tokens in one affine parent and let

```math
T:A\to Z
```

be the deterministic sponsor-pair terminal map. Forward transport gives

```math
w(e)\le w(T(e)),
\qquad
w(\{x,y\})=\frac1{|x-y|}.
```

For each terminal target `z`, write

```math
A_z=\{e\in A:T(e)=z\}.
```

Choose one deterministic maximum-weight source

```math
e_z^*\in\operatorname*{argmax}_{e\in A_z}w(e).
```

Ties may be resolved lexicographically.

---

## 2. Exact source first-use identity

Define the source-weighted transport-collision mass

```math
R_{\rm src}(A)
=
\sum_{z\in Z}
\sum_{e\in A_z\setminus\{e_z^*\}}w(e).
```

The source family partitions exactly into one first source per terminal fiber
and the remaining sources. Therefore

```math
\boxed{
\sum_{e\in A}w(e)
=
\sum_{z\in Z}w(e_z^*)
+
R_{\rm src}(A).
}
```

Since `w(e_z^*)<=w(z)` for every target,

```math
\boxed{
\sum_{e\in A}w(e)
\le
\sum_{z\in T(A)}w(z)
+
R_{\rm src}(A).
}
```

This is the source-weighted sponsor-pair transport row.

---

## 3. Strict refinement of terminal-weight collision

The earlier collision term is

```math
R_{\rm term}(A)
=
\sum_z(|A_z|-1)w(z).
```

Every non-first source in `A_z` satisfies `w(e)<=w(z)`. Hence

```math
\boxed{
R_{\rm src}(A)
\le
R_{\rm term}(A).
}
```

The difference is the transport-amplification slack

```math
\boxed{
S_{\rm amp}(A)
=
R_{\rm term}(A)-R_{\rm src}(A)
=
\sum_z
\sum_{e\in A_z\setminus\{e_z^*\}}
\bigl(w(z)-w(e)\bigr)
\ge0.
}
```

Thus terminal-target multiplicity remains a valid coarse certificate, while the
source-weighted term is always at least as strong and is strictly stronger
whenever an extra source gains pair weight before reaching its terminal target.

---

## 4. Completed-target activation inequality

Let `Z_comp(A)` be the distinct terminal targets whose prescribed direct,
backward, or residual completion lies in the parent. The terminal-pair
three-AP witness theorem gives

```math
\sum_{z\in Z_{\rm comp}(A)}w(z)
\le
\frac52\mathcal L_3(P).
```

Let

```math
M_{\rm out}(A)
=
\sum_{z\notin Z_{\rm comp}(A)}w(z).
```

Combining the completed-target capacity with the source-weighted row gives

```math
\boxed{
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm out}(A)
+
R_{\rm src}(A).
}
```

After an ambient split,

```math
M_{\rm out}(A)=M_{\rm ext}(A)+M_{\rm hole}(A),
```

so the refined whole-tree interface is

```math
\boxed{
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm ext}(A)
+
M_{\rm hole}(A)
+
R_{\rm src}(A).
}
```

No fitted coefficient is used.

---

## 5. Union-valued interpretation

The first source `e_z^*` is only a deterministic representative of one terminal
fiber. It is not a new globally reusable token. The union-valued object is the
terminal target `z`; the remaining source mass is retained explicitly in
`R_src`.

This avoids two invalid inferences:

1. terminal-target first appearance does not by itself pay all source pairs;
2. terminal-weight collision mass need not be paid when the smaller source
   weights are available.

The correct ledger stores, for each terminal target:

```text
terminal pair z;
source pair family A_z;
maximum-weight first source e_z*;
source-weighted collision mass;
terminal-weight collision mass;
transport-amplification slack.
```

---

## 6. Certified-frontier consequence

On the recorded residual-sponsor fourth-to-fifth diagnostic frontier, the
existing aggregate values imply

```math
R_{\rm src}
\le
710.942575247229\ldots
```

and, because

```math
\sum_{e\in A}w(e)
-
\sum_{z\in T(A)}w(z)
=
211.161055991560\ldots,
```

also

```math
211.161055991560\ldots
\le
R_{\rm src}.
```

The exact value requires only regrouping the already classified activated
source pairs by terminal target. No sixth retained generation is required.

---

## 7. Next exact object

The next finite probe should report, both globally and per parent:

1. `R_src`, `R_term`, and `S_amp`;
2. prescribed terminal completion status rather than initial-pair completion;
3. completed, external-root, and ambient-unresolved target union mass;
4. residual-minimum stars, other residual-sponsor pairs, and sponsor-sponsor
   pairs separately;
5. source-weighted collision concentration by parent class, path length,
   terminal class, selected step, and sponsor side.

The result determines whether the next theorem should target completed-edge
capacity, external completion transport, genuine-hole witnesses, or merge-fiber
collision reuse.
