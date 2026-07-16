# Global shell-batched terminal-pair transfer

## Status

State-independent one-layer packing theorem for an inclusion-maximal four-AP-free ambient set.

The theorem batches all standard dyadic shells before allocating pair capacity. It proves that internal collision pairs, cross-shell edge-swap pairs, and globally light canonical support pairs form one disjoint physical pair union. Thus newly exported pair capacity is not duplicated merely because several dyadic parent shells are processed simultaneously.

It is a one-layer theorem. Repeated entering-pair occurrences across different recursive generations and terminal-sink recreation remain separate obligations.

---

## 1. Simultaneous dyadic shell data

Let

```math
B\subseteq\mathbb N
```

be inclusion-maximal four-AP-free. For a finite set of shell indices `J`, put

```math
I_j=[2^j,2^{j+1}),
\qquad
P_j=B\cap I_j.
```

For each `j`, let

```math
A_j\subseteq\binom{P_j}{2}
```

be a physical activated pair set. Apply one deterministic monotone terminal transport map on `P_j`, and let `Z_j` be the physical target union.

Because the shells are disjoint, the entering pair sets are disjoint:

```math
A_i\cap A_j=\varnothing
\qquad(i\ne j).
```

Hence

```math
J\!\left(\bigcup_jA_j\right)
=
\sum_jJ(A_j).
```

For every target choose one deterministic maximum-weight source. Let `C_j` be the remaining collision-source set. Then

```math
J(A_j)
\le
J(Z_j)+J(C_j).
```

Every pair in `C_j` has both endpoints in `I_j`, so the global collision reserve

```math
C=\bigcup_jC_j
```

is a disjoint physical union and

```math
J(C)=\sum_jJ(C_j).
```

---

## 2. Completion classes

Give every target pair in `Z_j` one selected positive three-AP completion. Maximality of `B` gives exactly three classes.

1. **Local root:** the completion belongs to `P_j`.
2. **Cross-shell root:** the completion belongs to `B\setminus P_j`.
3. **Ambient hole:** the completion does not belong to `B` and therefore has a four-AP witness using three roots of `B`.

Write

```math
Z_j
=
Z_{j,\mathrm{local}}
\sqcup
Z_{j,\mathrm{cross}}
\sqcup
Z_{j,\mathrm{hole}}.
```

The local completed-edge theorem gives

```math
J(Z_{j,\mathrm{local}})
\le
\frac52\mathcal L_3(P_j).
```

---

## 3. Global injectivity of cross-shell edge swaps

A cross-shell completion can only be an adjacent completion. Suppose

```math
a<b,
\qquad d=b-a.
```

The pair

```math
e=\{a,b\}
```

can be the swapped pair for at most two algebraic target candidates:

```math
z_+=\{b,b+d\},
\qquad
z_-=\{a-d,a\}.
```

If both candidates lay in `B`, then

```math
\{a-d,a,b,b+d\}
```

would be a four-term arithmetic progression in `B`. Therefore at most one candidate exists.

Consequently a physical cross-shell swapped pair uniquely determines its tagged target, completion side, and target dyadic shell. The edge-swap map is globally injective over all shell indices.

Let

```math
E_{\mathrm{cross}}
```

be the union of all swapped cross-shell pairs. Then

```math
\boxed{
\sum_jJ(Z_{j,\mathrm{cross}})
=
J(E_{\mathrm{cross}}).
}
```

Every pair in `E_cross` has endpoints in two different standard dyadic shells. Every pair in `C` has both endpoints in one shell. Hence

```math
\boxed{
E_{\mathrm{cross}}\cap C=\varnothing.
}
```

---

## 4. Global canonical support multiplicity

For every ambient hole `c`, choose one deterministic four-AP witness and its canonical adjacent support pair

```math
f(c)=\{u,u+q\}\subseteq B.
```

Algebraically, a hole assigned this support can only be one of

```math
u-q,
\qquad
u+2q,
\qquad
u+3q.
```

The last two cannot both be holes assigned to the same support: their witness requirements would put all four points

```math
u,u+q,u+2q,u+3q
```

in `B`. Thus one canonical support pair serves at most two distinct holes.

Each hole has at most three selected completion roles:

```text
left adjacent;
right adjacent;
outer/midpoint.
```

Therefore, over all dyadic shells simultaneously, one support pair indexes at most six nonempty weighted role fibers:

```math
\boxed{m(f)\le6.}
```

This bound is global; it does not depend on the number of parent shells.

---

## 5. Global capacity-aware light/heavy rule

Reserve the physical pair set

```math
R=C\cup E_{\mathrm{cross}}.
```

For one support `f`, let its role-fiber loads be `L_1,\ldots,L_{m(f)}`. Adjacent roles use load `H(S)` and the outer role uses load `H(S)/2`.

If `f in R`, declare all of its fibers heavy. Otherwise call a role fiber light when

```math
L_i
\le
\frac1{m(f)}w(f).
```

Let `F_light` be the physical union of supports carrying at least one light role fiber. Then

```math
F_{\mathrm{light}}\cap R=\varnothing
```

and, for every unreserved support,

```math
\sum_{i:\,L_i\text{ light}}L_i
\le
w(f).
```

Summing over physical supports gives

```math
\sum_jJ(Z_{j,\mathrm{hole}})
\le
J(F_{\mathrm{light}})
+
\sum_{S\in\mathcal H_{\mathrm{global}}}\alpha(S)H(S),
```

where `alpha(S)` is `1` for adjacent roles and `1/2` for outer roles.

---

## 6. Global one-layer Bellman row

Combining source first use, local edge capacity, cross-shell injectivity, and global support allocation gives

```math
\boxed{
\sum_{j\in J}J(A_j)
\le
\frac52\sum_{j\in J}\mathcal L_3(P_j)
+
J(E_{\mathrm{out}})
+
\sum_{S\in\mathcal H_{\mathrm{global}}}\alpha(S)H(S),
}
```

with

```math
E_{\mathrm{out}}
=
C
\cup
E_{\mathrm{cross}}
\cup
F_{\mathrm{light}}.
```

The three sets in `E_out` are pairwise disjoint:

```text
C:             both endpoints in one shell;
E_cross:       endpoints in two different shells;
F_light:       explicitly unreserved against both sets.
```

Thus

```math
J(E_{\mathrm{out}})
=
J(C)+J(E_{\mathrm{cross}})+J(F_{\mathrm{light}})
```

without an overlap coefficient.

Every heavy role fiber is four-AP-free and descends below its target shell:

```text
adjacent role: resolved shell base at most one half of the parent base;
outer role:    resolved shell base at most one quarter of the parent base.
```

---

## 7. What this closes

The theorem closes the first-appearance packing problem created solely by processing several dyadic shells in the same transfer layer:

- collision-source pair sets from different shells cannot overlap;
- cross-shell edge-swap outputs cannot overlap each other;
- cross-shell outputs cannot overlap internal collision reserves;
- canonical support capacity can be shared globally using the sharp finite role bound `m(f)<=6`.

No anonymous ambient term remains, and no outgoing pair is counted twice within the batched layer.

---

## 8. Remaining treewise issue

The theorem does **not** assert that the same entering physical pair cannot recur in distinct recursive branches or generations. That is the genuine repeated-pair problem already isolated by the affine pair-resource and reference-gap theories.

A complete treewise argument must still combine:

1. this shell-batched outgoing union;
2. first appearance versus recurrence of entering pairs across generations;
3. terminal-sink first appearance and recreation;
4. lower-scale heavy-fiber recursion;
5. affine pair-energy telescoping once root-disjoint affine coordinates apply.

The gain is that cross-shell completion handling itself no longer contributes any additional pair multiplicity.