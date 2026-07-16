# Completion-step double affine lift

## Status

State-independent provenance lemma for heavy completion-step fibers.

A heavy fiber is not merely an abstract set of step integers. It carries two
simultaneous affine embeddings into the charged parent root universe. Retaining
this ordered double embedding distinguishes repeated numerical states until a
physical-pair projection is actually made.

---

## 1. Double embedding

Let

```math
P\subseteq\mathbb Z
```

and let a selected completion-step fiber satisfy

```math
S
=
\{d>0:c+\sigma d\in P,\ c+2\sigma d\in P\},
\qquad
\sigma\in\{-1,+1\}.
```

Define

```math
\iota_1(d)=c+\sigma d,
\qquad
\iota_2(d)=c+2\sigma d.
```

Then

```math
\iota_1(S)\subseteq P,
\qquad
\iota_2(S)\subseteq P.
```

For every nonempty `Q subseteq S`, define its ordered double lift

```math
\Lambda_{c,\sigma}(Q)
=
\bigl(\iota_1(Q),\iota_2(Q)\bigr).
```

---

## 2. The ordered double lift is injective

Suppose

```math
\Lambda_{c,\sigma}(Q)
=
(A,B)
```

with `Q` nonempty.

For right orientation,

```math
\min B>\min A,
\qquad
c=2\min A-\min B.
```

For left orientation,

```math
\max B<\max A,
\qquad
c=2\max A-\max B.
```

Thus the ordered pair `(A,B)` determines the orientation and the completion
reference. It then determines

```math
Q=\sigma(A-c).
```

Therefore

```math
\boxed{
\Lambda_{c,\sigma}(Q)
=
\Lambda_{c',\sigma'}(Q')
\Longrightarrow
(c,\sigma,Q)=(c',\sigma',Q').
}
```

Repeated equality of the abstract step set `Q` is not equality of the affine
resource occurrence unless the full completion reference and orientation also
agree.

---

## 3. Pair form and exact energy

For one physical step pair

```math
e=\{d_1,d_2\}\subseteq S,
\qquad
g=|d_2-d_1|,
```

its ordered double pair lift is

```math
\Lambda_{c,\sigma}(e)
=
\left(
\{c+\sigma d_1,c+\sigma d_2\},
\{c+2\sigma d_1,c+2\sigma d_2\}
\right).
```

The two parent-root pair gaps are `g` and `2g`. Hence

```math
J(\Lambda_{c,\sigma}(e))
=
\frac1g+\frac1{2g}
=
\frac32w(e).
```

Equivalently,

```math
\boxed{
w(e)=\frac23J(\Lambda_{c,\sigma}(e)).}
```

For any physical pair union `E` on the root coordinates of `S`, affine
injectivity inside each copy gives

```math
\boxed{
J(\iota_1(E))+J(\iota_2(E))
=
\frac32J(E).
}
```

---

## 4. Composition with recursive provenance

Suppose a recursive descendant of `S` has root provenance in the original
fiber coordinates. Every current or latent root pair of that descendant is a
literal pair

```math
\{d_1,d_2\}\subseteq S.
```

Composing the descendant provenance with `iota_1` and `iota_2` produces two
literal parent-root pairs in `P`. Therefore heavy-fiber recursion preserves the
same affine containment property used by the ordinary retained genealogy.

No abstract child pair needs to be treated as a new unrelated physical token.

---

## 5. What may still collide

The ordered double configuration is injective, but its individual pair
projections can be reused:

```text
two different double configurations may share their first pair;
two different double configurations may share their second pair;
a first pair from one configuration may equal a second pair from another.
```

Therefore one may not sum the two-copy pair energies independently without a
physical first-appearance ledger.

The correct collision object is the projection

```math
(c,\sigma,e,j)
\longmapsto
\iota_j(e),
\qquad j\in\{1,2\},
```

not equality of the abstract step state.

When two projections collide, the equality supplies an exact affine rectangle
relation among the two completion references and the two internal pair
coordinates. That is the interface to the reference-gap and rectangle-aspect
ledgers.

---

## 6. Consequence for repeated heavy states

A numerical profile such as

```text
9944 heavy-shell occurrences;
3521 abstract shell-state identities
```

must not be interpreted as `6423` automatic physical collisions. The
occurrences carry different ordered double lifts. Pair collision exists only
where their projected parent-root pairs agree.

Thus the correct recursive state is

```math
(S,c,\sigma,\iota_1,\iota_2),
```

or equivalently its ordered double image, rather than the unlabeled set `S`
alone.

---

## 7. Remaining allocation problem

The double lift provides more capacity than the internal step pair requires:

```math
J(\Lambda(e))=\frac32w(e).
```

But the two components can overlap across configurations. The next theorem
must allocate projected physical pair capacity collision-soundly. Viable
interfaces are:

1. source-weighted first appearance on the projected pair union;
2. a fractional matching between configurations and their two copies;
3. reference-gap transfer for repeated projections;
4. rectangle-aspect tokens for cross-copy collisions.

The essential correction is already exact: repeated abstract states retain
affine provenance and should not be merged before the pair projection is
examined.
