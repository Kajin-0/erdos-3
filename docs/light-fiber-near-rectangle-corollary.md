# Light-fiber near-rectangle corollary

## Status

Immediate but structurally important corollary of the three-AP
occurrence-family light/heavy transfer.

Light fibers are exactly the part of repeated occurrence load that can be
terminated into one activated parent pair. Every far rectangle is necessarily
heavy and therefore recurses as a lower-scale four-AP-free fiber.

---

## 1. Setup

Let

```math
f=\{a,p\},
\qquad
\delta=p-a>0,
```

and let `S_f` be one anchor-pair step fiber arising from a selected family of
three-AP occurrences in a four-AP-free block.

The fiber is light when

```math
H(S_f)
\le
\frac1\delta.
```

It is heavy otherwise.

---

## 2. Far incidence forces heaviness

Suppose some

```math
d\in S_f
```

satisfies

```math
d<\delta.
```

Then

```math
H(S_f)
\ge
\frac1d
>
\frac1\delta.
```

Therefore

```math
\boxed{
d<\delta
\quad\Longrightarrow\quad
S_f\text{ is heavy}.}
```

Equivalently, every light fiber satisfies

```math
\boxed{
S_f\subseteq[\delta,\infty).
}
```

Thus every light-fiber rectangle has aspect

```math
\frac\delta d\le1.
```

---

## 3. Exact pair payment for a light fiber

For a light fiber,

```math
\boxed{
\sum_{d\in S_f}\frac1d
\le
\frac1\delta
=
w(f).
}
```

Hence the entire repeated occurrence family indexed by `f` can be paid by one
activation of the physical anchor pair `f`.

No per-step pair copy is needed. Reuse of `f` across all steps of the light
fiber is already absorbed by the threshold.

---

## 4. Rectangle witness

Every nonempty fiber contains at least one step `d`. The parent contains the
six-point two-row configuration

```math
\{a,a+d,a+2d\}
\cup
\{p,p+d,p+2d\}.
```

For a light fiber, `delta<=d`. Therefore the activated pair `f` comes with an
explicit near-aspect completion rectangle.

The exact aspect identity is

```math
\frac1d
=
\frac\delta d\frac1\delta,
\qquad
0<\frac\delta d\le1.
```

Summing over the fiber gives

```math
H(S_f)
=
\left(
\sum_{d\in S_f}\frac\delta d
\right)w(f),
```

with total coefficient at most one.

---

## 5. Heavy fibers are the recursive class

A heavy fiber satisfies

```math
H(S_f)>w(f).
```

It may be heavy for either reason:

1. it contains one far step `d<delta`;
2. it contains enough near steps that their total reciprocal mass exceeds
   `1/delta`.

In both cases the pair `f` alone is insufficient payment. The correct output
is the fiber itself:

```math
S_f\cap[M,2M),
\qquad M\le N/4,
```

resolved into lower-scale four-AP-free shells.

Thus the light/heavy rule is a genuine stopping-time decomposition:

```text
light fiber -> one activated pair with a near rectangle witness;
heavy fiber -> strictly lower-scale recursive state.
```

---

## 6. Interface with sponsor-pair transport

Apply the monotone sponsor-pair transport theorem to each activated light pair
`f`.

- If at least one endpoint is a deleted sponsor, the pair transports to a
  direct selected edge, a backward obstruction, or a residual target.
- If both endpoints survive in the residual, `f` is already a residual pair
  target.

The near rectangle attached to `f` supplies additional completion geometry for
backward or external-completion cases.

Consequently, light-fiber load feeds the existing pair-transport and
completion ledger. It does not create a new multiplicity problem.

---

## 7. Strategic consequence

The collision frontier now separates into two disjoint mechanisms:

```text
pair-transport mechanism:
  all light fibers, paid once by physical anchor pairs;

recursive-fiber mechanism:
  all heavy fibers, descending by at least two dyadic levels.
```

A complete transfer theorem must show that first appearances of light pairs
plus recursive heavy-fiber mass fit within the full-edge factor-five output
and terminal/external-completion releases. No uniform overlap constant is
required.
