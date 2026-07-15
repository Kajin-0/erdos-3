# Repeated step-state reference reserve

## Status

State-independent transposition lemma for repeated lower-scale step states
embedded at several completion references in one four-AP-free dyadic parent.

The lemma applies to multiplicity among the heavy completion-step fibers from
the terminal-pair light/heavy transfer. It converts each repeated state fiber
into a concrete two-scale rectangle ledger and a lower-than-parent
reference-difference reserve. It does not, by itself, remove the rectangle
aspect coefficient.

---

## 1. Repeated double-translate state

Let

```math
P\subseteq[N,2N)
```

be four-AP-free. Let

```math
S\subseteq[M,2M)
```

be nonempty, and fix one orientation

```math
\sigma\in\{-1,+1\}.
```

Suppose a finite reference set `C` satisfies

```math
c+\sigma S\subseteq P,
\qquad
c+2\sigma S\subseteq P
```

for every `c in C`.

Thus every reference `c` carries one occurrence of the same completion-step
state `S`. The occurrence load is

```math
|C|H(S).
```

Choose one deterministic base reference

```math
c_0=\min C
```

and write

```math
D(C)=\{c-c_0:c\in C,\ c>c_0\}.
```

The repeated-state collision load after first appearance is

```math
\boxed{
R(S,C)=(|C|-1)H(S).
}
```

---

## 2. Both coordinate sets are four-AP-free

The state `S` is four-AP-free because, for any fixed `c in C`,

```math
c+\sigma S\subseteq P.
```

Likewise `C` is four-AP-free. Fix any `s in S`. Then

```math
C+\sigma s\subseteq P.
```

A four-term progression in `C` would translate to one in `P`.

Translation now gives

```math
\boxed{
D(C)\text{ is four-AP-free.}
}
```

This conclusion does not require the references themselves to belong to `P`.
It applies in particular when the references are certified completion holes.

---

## 3. Strict reference-scale reduction

Write

```math
a=\min S,
\qquad
b=\max S,
\qquad
\Delta=b-a.
```

For right orientation, the two embeddings imply

```math
N-a\le c<2N-2b.
```

For left orientation they imply the reflected interval

```math
N+2b\le c<2N+a.
```

Therefore in both orientations

```math
\boxed{
\operatorname{diam}(C)
<
N-2b+a
=
N-b-\Delta.
}
```

Since `a>=M`,

```math
\boxed{
D(C)\subset(0,N-M).
}
```

After standard dyadic resolution, every shell of the reference-difference
reserve has base at most `N/2`. This is strict descent from the parent shell,
although it need not descend below the step-state shell `M`.

---

## 4. Exact state/reference rectangle identity

Every extra reference gives one copy of every step in `S`. Therefore

```math
R(S,C)
=
\sum_{\delta\in D(C)}
\sum_{d\in S}
\frac1d.
```

For every rectangle cell `(delta,d)`,

```math
\frac1d
=
\frac\delta d\frac1\delta.
```

Hence

```math
\boxed{
R(S,C)
=
\sum_{\delta\in D(C)}
\sum_{d\in S}
\frac\delta d\,w(\delta).
}
```

Here `w(delta)=1/delta` is the harmonic token of the lower-than-parent
reference-difference reserve. The coefficient `delta/d` is the exact rectangle
aspect ratio.

No multiplicity constant or fitted coefficient is hidden.

---

## 5. Dyadic aspect ledger

For every integer `k`, define

```math
\mathcal R_k(S,C)
=
\{(\delta,d):
\delta\in D(C),
\ d\in S,
\ 2^kd\le\delta<2^{k+1}d\}.
```

Then

```math
\boxed{
R(S,C)
\le
\sum_k
2^{k+1}
\sum_{(\delta,d)\in\mathcal R_k(S,C)}
\frac1\delta.
}
```

The token must retain both `delta` and `d`; projecting only to `delta` would
hide reuse across the steps of `S`.

The near rectangle region `k<0` has coefficient at most one. The far region
`k>=0` is the genuine two-scale obligation.

---

## 6. Coarse product bound

Since every `delta in D(C)` is below `N-2b+a`,

```math
H(D(C))
>
\frac{|C|-1}{N-2b+a}.
```

Thus

```math
\boxed{
R(S,C)
<
(N-2b+a)H(S)H(D(C)).
}
```

The dimensionless coefficient

```math
\kappa_N(S)
=
(N-2\max S+\min S)H(S)
```

is the coarse rectangle-content feature. It is exact enough for a Bellman/LP
interface but can be very loose; the dyadic aspect ledger is the preferred
form.

---

## 7. First-appearance requirement

Different repeated step states can generate the same rectangle token. The
whole-tree object is therefore the physical first-appearance union of

```math
(\delta,d,k,\sigma),
\qquad
2^kd\le\delta<2^{k+1}d.
```

Every repeated occurrence cell maps to exactly one such token. Reuse must be
recorded explicitly rather than absorbed into a state multiplicity.

This is the correct next ledger after completion-step light/heavy transfer:

```text
heavy completion fiber occurrence;
step-state first appearance;
completion-reference difference;
rectangle aspect band;
rectangle-token first appearance.
```

---

## 8. Scope

The lemma resolves the geometry and the strict parent-scale reduction of one
repeated step-state fiber. It does not yet prove that all far-aspect rectangle
tokens are summable across the complete recursion tree.

The remaining theorem must exploit one of:

1. first-appearance packing of the two-coordinate rectangle tokens;
2. a Bellman potential carrying both step scale and reference scale;
3. a second light/heavy transpose on far-aspect token families;
4. additional four-AP completion obstructions at exceptional aspect ratios.

A scalar rank on the step state or reference set alone is insufficient.
