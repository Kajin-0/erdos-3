# Repeated-state vertical-pair transfer

## Status

State-independent rectangle payment for repeated affine copies of one lower-scale step state.

After one deterministic base reference is chosen, every additional occurrence of the same oriented numerical state is paid by the vertical corresponding-point pairs between the base copy and the new copy. The available vertical pair energy strictly dominates the repeated state harmonic mass.

The lemma removes the aspect-ratio coefficient from the **whole-state** recurrence. Reuse of the resulting physical vertical pairs across different state configurations remains a pair first-appearance problem.

---

## 1. Repeated affine state

Let

```math
T=\{d_1,\ldots,d_n\}\subseteq[M,2M)
```

be finite and nonempty. Fix one orientation `sigma in {+1,-1}` and two distinct completion references

```math
c_0,
\qquad
c.
```

Assume the corresponding first affine copies

```math
c_0+\sigma T,
\qquad
c+\sigma T
```

lie in the ambient root set.

Write

```math
\delta=|c-c_0|.
```

If both copies belong to one shell-valid repeated-state family, the standard reference-interval argument gives

```math
0<\delta<M.
```

---

## 2. Vertical corresponding-point pairs

For every `d in T`, define

```math
v_d
=
\{c_0+\sigma d,c+\sigma d\}.
```

Each pair has gap exactly `delta`, and distinct values of `d` give distinct physical pairs. Therefore

```math
J(V(c_0,c;T))
=
\sum_{d\in T}w(v_d)
=
\frac{|T|}{\delta}.
```

Since `delta<M` and every `d>=M`,

```math
\frac{|T|}{\delta}
>
\frac{|T|}{M}
\ge
\sum_{d\in T}\frac1d
=
H(T).
```

Hence

```math
\boxed{
H(T)
<
J(V(c_0,c;T)).
}
```

For an outer completion role, whose weighted debt is `H(T)/2`, the same vertical pair set also pays the debt.

Writing the role coefficient as

```math
\alpha\in\{1,1/2\},
```

one has

```math
\boxed{
\alpha H(T)
<
J(V(c_0,c;T)).
}
```

---

## 3. First occurrence and repeated occurrence split

For every oriented numerical state `(M,T,sigma)`, choose one deterministic base reference `c_0`.

- The base occurrence is handled by the horizontal-chain transfer or by the ordinary affine pair-energy ledger.
- Every additional reference `c` is handled by the vertical pair family `V(c_0,c;T)`.

Thus a repeated numerical-state family with reference set `R` satisfies

```math
\boxed{
(|R|-1)\alpha H(T)
<
\sum_{c\in R\setminus\{c_0\}}
J(V(c_0,c;T)).
}
```

No factor `delta/r` appears. The full set of corresponding-point pairs absorbs the repeated state as one object.

---

## 4. Strict scale descent

Every vertical pair gap is a reference difference

```math
\delta<M.
```

Therefore its standard dyadic gap shell base is at most `M/2`.

The transfer is triangular in the same sense as the horizontal-chain transfer:

```text
repeated state at step-shell base M
    -> physical vertical pairs of gap below M.
```

---

## 5. Injective rectangle configuration

For fixed `c_0,c,sigma,T`, the complete ordered configuration

```math
\bigl(c_0+\sigma T,\ c+\sigma T\bigr)
```

is an affine two-copy rectangle. It determines:

```text
base reference c_0;
new reference c;
orientation sigma;
numerical state T.
```

Thus repeated state occurrences are injective at the full configuration level.

Projection to one physical vertical pair can collide across different states or reference families. Such a collision is genuine pair reuse and must be merged in a physical pair ledger.

---

## 6. Pair-reuse interface

Let `mathcal V` be the multiset of vertical pair occurrences generated over all repeated state families. Deterministic physical first appearance gives

```math
J_{\rm occ}(\mathcal V)
=
J(V_{\rm union})
+
R_{\rm vertical},
```

where `R_vertical` is the repeated physical-pair occurrence mass.

Every pair in `V_union` has gap strictly below its generating state scale. Repeated vertical pairs again carry affine rectangle/reference provenance, so the same first-appearance and reference-difference machinery applies.

The present theorem proves that the state multiplicity itself is not the obstruction. The only remaining multiplicity is projection collision among physical pair resources.

---

## 7. Strategic consequence

Recursive heavy output can be organized as follows:

```text
first occurrence of an oriented numerical state
    -> horizontal-chain pair capacity;
additional occurrence of the same state
    -> vertical corresponding-pair capacity.
```

Both outputs have strictly smaller gaps than the state shell base. This is stronger than charging every repeated horizontal edge separately and avoids the large rectangle aspect coefficient at the whole-state level.

A complete treewise proof now requires a lower-gap pair-union packing theorem for the combined horizontal and vertical physical pair families, plus terminal first appearance. No free-standing state multiplicity term remains.