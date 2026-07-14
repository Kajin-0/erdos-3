# Full-edge dyadic scale and gap monotonicity

## Status

Symbolic refinement of oriented full-edge coordinated branching after mandatory
standard dyadic shelling.

The theorem supplies a strict path coordinate for every persistent physical
root pair.  It does not by itself bound cross-branch multiplicity.

---

## 1. Parent and shell scales

Let

```math
B\subseteq[N,2N)
```

be a four-AP-free parent block, where `N` is a power of two.  Resolve every
full-edge numerical child into standard dyadic shells

```math
C\subseteq[M,2M),
```

where `M` is also a power of two.

For an ordinary side or oriented middle child, every token is a progression
step `d`.  Since a three-AP inside `[N,2N)` satisfies

```math
0<d<N/2,
```

no such token can lie in the shell `[N/2,N)`.  Therefore every nonempty side
or middle shell satisfies

```math
\boxed{M\le N/4.}
```

For a doubled-side child, every token is `2d<N`.  Hence every nonempty doubled
shell satisfies

```math
\boxed{M\le N/2.}
```

These bounds are sharp at the dyadic level.

---

## 2. Exact side/doubled-shell pairing

Let `V` be one parity-selected side child.  Multiplication by two maps every
standard dyadic shell of `V` bijectively onto one shell of `2V`:

```math
V\cap[M,2M)
\longmapsto
2V\cap[2M,4M).
```

Thus a doubled-side shell is not an independent structural state.  It is the
exact dilation by two of its side sibling one dyadic level lower.  Their
harmonic masses satisfy

```math
H(2C)=\frac12H(C).
```

Any recursive pattern in a doubled shell is therefore the dilation of the
same recursive pattern in the paired side shell.

---

## 3. Persistent pair gap inside one shell

Represent an oriented affine child as

```math
S_{r,\sigma}(P)
=
\{\sigma(p-r):p\in P\},
\qquad
\sigma\in\{-1,+1\}.
```

Let an unordered physical root pair

```math
e=\{u,v\},
\qquad u<v,
```

belong to the latent pair set of a shell `C\subseteq[M,2M)`.  Put

```math
D=v-u.
```

The two current labels corresponding to `u` and `v` lie in one interval of
length `M`.  Their difference is exactly `D`, independent of orientation.
Consequently

```math
\boxed{0<D<M.}
```

This is the basic gap-versus-shell inequality.

---

## 4. Reference interval

For right orientation, the shell conditions are

```math
M\le u-r<v-r<2M.
```

Hence

```math
v-2M<r\le u-M.
```

For left orientation, the analogous conditions give

```math
v+M\le r<u+2M.
```

In either orientation, all references that realize the same pair in the same
shell scale lie in an interval of length

```math
\boxed{M-D.}
```

The interval collapses as the pair gap approaches the shell scale.

---

## 5. Strict gap-ratio growth along a lineage

Suppose the same physical pair survives from a shell of base `M` to a
recursive descendant shell of base `M'`.  Full-edge scale descent gives

```math
M'\le M/2,
```

and gives `M'\le M/4` on an ordinary side or middle transition.  The physical
gap `D` does not change under affine reference pivots.  Therefore

```math
\boxed{
\frac{D}{M'}
\ge
2\frac{D}{M}.
}
```

The normalized pair gap at least doubles at every persistence step and at
least quadruples on ordinary side/middle steps.

Since persistence requires `D<M'`, a pair beginning in a shell of base `M_0`
can remain latent for fewer than

```math
\log_2(M_0/D)
```

further transitions.  In particular, no physical pair has an infinite latent
lineage.

This is a pathwise termination theorem.  It does not rule out the same pair
entering several descendant shells before those paths terminate.

---

## 6. Same-type forbidden reference gaps

Fix a persistent pair of gap `D`.

For two side children of the same orientation and type, or two middle children
of the same orientation and type, references differing by `D` force four
completion points in arithmetic progression.  Therefore

```math
R_t(e)\cap(R_t(e)+D)=\varnothing.
```

For two doubled-side children of the same type, references differing by `2D`
force the four midpoint completions into an arithmetic progression.  Hence

```math
R_t(e)\cap(R_t(e)+2D)=\varnothing.
```

These are exact one-parent restrictions on reference multiplicity.

---

## 7. Consequence for the active theorem

The remaining pair-persistence problem now has three simultaneous coordinates:

```text
physical pair identity e={u,v};
shell base M with D<M;
reference r in an interval of length M-D.
```

Along every lineage, `D` is fixed, `M` strictly decreases, and `D/M` grows at
least geometrically.  A whole-tree theorem must combine this pathwise
termination with a cross-branch bound on the number of admissible references
at each scale.

The exact next target is therefore a weighted reference-packing inequality,
not another retained generation:

```math
\sum_{\text{recursive shells containing }e}
\omega(M,r,e)
\le C
```

for a scale-sensitive weight `\omega` that telescopes as `D/M` increases.
