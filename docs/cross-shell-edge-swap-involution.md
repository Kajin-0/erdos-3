# Cross-shell edge-swap involution

## Status

State-independent termination theorem for the scale-preserving actual-root component of maximal-ambient direct pair discharge.

An adjacent completed pair in a four-AP-free set has at most one adjacent completion root. Swapping to the other edge of that three-AP makes the original pair the unique reverse swap. Thus the cross-shell edge-swap graph consists of isolated two-cycles. A first-appearance ledger emits at most one new pair identity from each entering pair before recording recreation.

---

## 1. Adjacent completions of one pair

Let

```math
e=\{x,x+D\},
\qquad D>0,
```

with both endpoints in a four-AP-free set `B`.

The two adjacent three-AP completion candidates are

```math
x-D
```

and

```math
x+2D.
```

They cannot both belong to `B`, because then

```math
x-D,
\quad x,
\quad x+D,
\quad x+2D
```

would be a nontrivial four-term arithmetic progression.

Therefore

```math
\boxed{
\#\bigl(B\cap\{x-D,x+2D\}\bigr)\le1.
}
```

---

## 2. Left swap

Suppose

```math
x-D\in B.
```

The completed three-AP is

```math
x-D,
\quad x,
\quad x+D.
```

The edge-swap output is

```math
e'=\{x-D,x\}.
```

Its right adjacent completion is the original root `x+D`, which belongs to `B`.

Its left adjacent completion `x-2D` cannot belong to `B`, because

```math
x-2D,
\quad x-D,
\quad x,
\quad x+D
```

would be a four-AP.

Hence `e'` has exactly one adjacent completion root and swapping again returns `e`.

---

## 3. Right swap

The reflected argument applies when

```math
x+2D\in B.
```

The swap output is

```math
e'=\{x+D,x+2D\},
```

whose unique adjacent completion root is `x`. A second swap returns the original pair.

---

## 4. Involution theorem

Let `rho` be the adjacent-root edge-swap map on tagged pairs for which an ambient adjacent completion root exists. Then

```math
\boxed{
\rho(\rho(e))=e.
}
```

Moreover `rho(e)` has no competing adjacent-root swap direction.

The physical gap is preserved:

```math
D(\rho(e))=D(e).
```

Thus every connected component of the scale-preserving adjacent-root swap graph is one undirected edge:

```text
e <-> rho(e).
```

---

## 5. First-appearance consequence

Maintain a first-appearance ledger for physical pair identities.

Starting from one entering pair `e`:

1. the first cross-shell swap may emit the new identity `rho(e)`;
2. any subsequent adjacent-root swap emits `e` again;
3. that output is recreation, not a new pair resource.

Therefore

```math
\boxed{
\text{one entering pair creates at most one new cross-shell swap identity.}
}
```

No infinite scale-preserving cross-shell first-appearance path exists.

---

## 6. Midpoint completions

For endpoints in one standard dyadic shell, a midpoint completion lies in the same shell. It belongs to the local completed-edge class rather than the cross-shell class.

If midpoint edge transfer is recorded separately, it halves the physical gap and is already strictly contracting. It is not part of the scale-preserving residue.

---

## 7. Strategic consequence

The direct-discharge dyadic pair-gap theorem identified two possible scale-preserving mechanisms:

```text
adjacent cross-shell actual-root swaps;
multiplicity-one light supports.
```

The present involution theorem removes the first from the persistent first-appearance frontier. After one new edge identity it becomes immediate recreation.

The only remaining mechanism capable of producing a long first-appearance chain without dyadic gap descent is therefore

```text
multiplicity-one light-support transfer.
```

The next universal theorem should classify exact-gap light-support transitions and combine strict integer-gap descent with four-AP witness geometry.
