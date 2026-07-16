# Completion-step fiber light/heavy transfer

## Status

State-independent transfer theorem for terminal pair targets whose selected
completion is a certified same-shell hole of a four-AP-free block.

The theorem replaces recursive activation of every hole-witness support pair by
an exact stopping-time alternative:

```text
light completion fibers -> one physical support-pair activation;
heavy completion fibers -> lower-scale four-AP-free recursive states.
```

It applies after ordinary three-AP edge capacity has been removed and before
sponsor-pair transport is applied to the remaining light support pairs.

---

## 1. Selected completion targets

Let

```math
P\subseteq[N,2N)
```

be four-AP-free. Consider any selected family of distinct tagged terminal
targets

```math
(c,\sigma,d),
\qquad
\sigma\in\{-1,+1\},
\qquad d>0,
```

such that

```math
c\notin P,
\qquad
c+\sigma d\in P,
\qquad
c+2\sigma d\in P.
```

The physical target pair is

```math
e(c,\sigma,d)
=
\{c+\sigma d,c+2\sigma d\},
```

and has weight

```math
w(e)=\frac1d.
```

The tag records one selected completion and orientation. Thus one physical
target contributes at most once to the present transfer.

Assume also that the selected completion lies in the same dyadic shell:

```math
c\in[N,2N).
```

Completions outside this shell remain in the ambient cross-scale ledger.

---

## 2. Oriented completion-step fibers

For one selected completion and orientation define

```math
S_{c,\sigma}
=
\{d:(c,\sigma,d)\text{ is selected}\}.
```

The target load decomposes exactly as

```math
\boxed{
L(\mathcal T)
=
\sum_{c,\sigma}H(S_{c,\sigma}),
}
```

where

```math
H(S)=\sum_{d\in S}\frac1d.
```

No target multiplicity is hidden in this identity.

---

## 3. Every completion-step fiber is four-AP-free

Suppose

```math
d,d+r,d+2r,d+3r\in S_{c,\sigma}
```

with `r>0`. Then

```math
c+\sigma d,
\quad
c+\sigma(d+r),
\quad
c+\sigma(d+2r),
\quad
c+\sigma(d+3r)
```

are four points of `P` in arithmetic progression, with common difference
`|r|`. This contradicts four-AP-freeness.

Therefore

```math
\boxed{
S_{c,\sigma}\text{ is four-AP-free.}
}
```

This argument uses only one endpoint from each target pair.

---

## 4. Strict scale descent

Because

```math
c,\ c+\sigma d,\ c+2\sigma d\in[N,2N),
```

one has

```math
2d<N.
```

Hence

```math
\boxed{
d<N/2.
}
```

After standard dyadic resolution, every nonempty shell of
`S_{c,sigma}` has base

```math
M\le N/4.
```

Thus every heavy completion-step fiber is a genuine lower-scale recursive
state, descending by at least two dyadic levels in shell base.

---

## 5. Canonical hole supports

Suppose every selected completion `c` is certified by a four-term witness with
three points in `P`. Assign `c` its deterministic canonical adjacent witness
pair

```math
f(c)=\{u,v\},
\qquad
h(c)=v-u.
```

The canonical hole-support theorem gives

```math
\boxed{
|\{c:f(c)=f\}|\le2.
}
```

Each completion has at most two orientations. Therefore one physical support
pair indexes at most four nonempty oriented completion fibers:

```math
\boxed{
m(f)
:=
|\{(c,\sigma):f(c)=f,\ S_{c,\sigma}\ne\varnothing\}|
\le4.
}
```

---

## 6. Adaptive light/heavy threshold

For one physical support pair `f` of gap `h`, let `m=m(f)`. Call one of its
oriented fibers light when

```math
H(S_{c,\sigma})
\le
\frac1{mh}
=
\frac1m w(f),
```

and heavy otherwise.

The complete light load attached to `f` obeys

```math
\sum_{\substack{(c,\sigma):f(c)=f\\
S_{c,\sigma}\text{ light}}}
H(S_{c,\sigma})
\le
m\frac1{mh}
=
\frac1h
=
w(f).
```

Therefore one activation of the physical support pair pays every light fiber
assigned to it:

```math
\boxed{
L_{\rm light}(f)\le w(f).
}
```

No copy of `f` is created per completion or per orientation.

---

## 7. Heavy fibers

Every heavy fiber satisfies

```math
H(S_{c,\sigma})
>
\frac1{m(f)h(f)}
\ge
\frac1{4h(f)}.
```

It also has the exact certificates

```text
S_{c,sigma} is four-AP-free;
S_{c,sigma} lies below N/2;
all of c+sigma S and c+2 sigma S lie in P;
its harmonic mass exceeds its allocated support-pair share.
```

The correct output is the lower-scale fiber itself. It is not another unpaid
scalar coefficient and it is not forced through sponsor-pair transport.

---

## 8. Transfer inequality

Let

```math
E_{\rm light}
=
\{f:\text{at least one light fiber is assigned to }f\}.
```

Then the selected certified-hole target load satisfies

```math
\boxed{
L(\mathcal T)
\le
J(E_{\rm light})
+
\sum_{S\in\mathcal H}H(S),
}
```

where

```math
J(E)=\sum_{f\in E}w(f)
```

and `H` is the family of heavy oriented completion-step fibers.

The inequality is collision-sound:

```text
one physical support identity appears once in E_light;
every selected target belongs to exactly one tagged fiber;
every heavy output is a named lower-scale four-AP-free set.
```

---

## 9. Interface with the existing proof program

The correct terminal-payment order is now:

```text
1. pay every target that is an edge of a parent or ambient three-AP;
2. retain admissible ambient completions in the external-root ledger;
3. apply the completion-step light/heavy transfer to certified same-shell holes;
4. transport only the resulting light physical support pairs;
5. recurse on the heavy completion-step fibers at lower scale.
```

This explains why recursively activating every canonical support pair is too
strong. The five-layer `S7` support closure remains a valid finite diagnostic,
but the state-independent proof architecture stops light fibers and recurses on
heavy fibers instead of seeking a scalar rank for the entire support rewrite.

---

## 10. Remaining whole-tree obligations

A complete theorem still must:

1. merge first appearances of `E_light` with the existing physical pair union;
2. control overlap among heavy completion-step fibers from different parent
   states;
3. combine their two-level scale descent with the Bellman potential;
4. keep same-shell certified holes separate from outside-shell ambient
   completions;
5. preserve the source-weighted collision ledger before target tagging.

The gain is structural: certified-hole target mass now has exactly the same
light-pair versus heavy-lower-scale architecture as the established
three-AP occurrence-family transfer.
