# Exact-progression sponsor budget

## Status

Exact localization of the remaining lifted-progression persistence multiplicity.

After the global lifted-center layer decomposition, the unresolved quantity is

```math
L(q)=\max_x\nu_q(x),
```

where `nu_q(x)` counts terminal occurrences of step `q` lifting to the exact root progression

```math
x-q,
\quad x,
\quad x+q.
```

This note proves that all copies of one exact lifted progression descend from one root sponsor and are bounded by that sponsor's conserved linear-label budget.

---

## 1. The root sponsor is determined by the lifted progression

The coordinated side-anchor orientation depends only on `q`. Write

```math
\sigma(q)\in\{-1,+1\}
```

so that every selected progression of step `q` has

```math
b=a+\sigma(q)q,
```

where `a` is the deleted sponsor and `b` is the center.

Suppose a terminal occurrence in a recursive state lifts to center `x` in the root block. Its lifted sponsor is therefore

```math
a(x,q)=x-\sigma(q)q.
```

Thus every terminal occurrence of the same exact lifted progression has the same root sponsor.

---

## 2. Occurrence genealogy by root ancestor

Every retained recursive output is associated with one parent element occurrence:

1. a terminal representative or multiplicity-fiber output is associated with its selected sponsor;
2. a component-translation output is associated with its translated parent point;
3. a merge-difference output is associated with its nonminimal sponsor.

Following these associations upward assigns every occurrence in the recursive tree to a unique root element of `D`.

The half-contraction theorem applies separately to the descendant tree of each root occurrence. If `a` is a root element, then

```math
\boxed{
\sum_{u\text{ terminal descendant of }a}u
\le a.
}
```

More generally, for every `p>=1`,

```math
\sum_{u\text{ terminal descendant of }a}u^p
\le
2^{1-p}a^p.
```

---

## 3. Exact-progression persistence bound

Fix `q` and a lifted center `x`. All

```math
\nu_q(x)
```

terminal copies of this progression are descendants of the single root sponsor

```math
a=x-\sigma(q)q.
```

Each copy contributes terminal label `q`. Therefore the localized linear budget gives

```math
\nu_q(x)q\le a.
```

Hence

```math
\boxed{
\nu_q(x)
\le
\left\lfloor\frac{x-\sigma(q)q}{q}\right\rfloor.
}
```

Taking the maximum over lifted centers gives

```math
\boxed{
L(q)q
\le
\max_{x:\nu_q(x)>0}
\bigl(x-\sigma(q)q\bigr)
<2N.
}
```

Thus

```math
\boxed{
L(q)<\frac{2N}{q}.
}
```

This recovers the crude scale bound without counting states or using a depth argument, and identifies the exact resource that pays for persistence.

---

## 4. Simultaneous budget for several persistent steps

For each `q`, choose a center `x_q` attaining `L(q)` and let

```math
a_q=x_q-\sigma(q)q
```

be its root sponsor.

Group the chosen persistent steps by sponsor. For a fixed root element `a`, all selected copies with `a_q=a` are terminal descendants of the occurrence `a`. Therefore

```math
\boxed{
\sum_{q:a_q=a}L(q)q
\le a.
}
```

Summing over root sponsors gives

```math
\boxed{
\sum_qL(q)q
\le
\sum_{a\in D}a
<2N|D|.
}
```

This is a positive-moment bound specifically for the residual multiplicities left after global center layering.

---

## 5. Distinct persistent spectrum of one sponsor

Let

```math
Q(a)=\{q:a_q=a\}
```

be the set of distinct steps whose maximal persistence progression is sponsored by `a`.

Since `L(q)>=1`, the sponsor budget implies

```math
\sum_{q\in Q(a)}q\le a.
```

If `m=|Q(a)|`, the smallest possible sum of `m` distinct positive integers is

```math
1+2+\cdots+m=\frac{m(m+1)}2.
```

Therefore

```math
\boxed{
|Q(a)|
\le
\frac{\sqrt{8a+1}-1}{2}.
}
```

The reciprocal sum of the distinct persistent steps sponsored by `a` is maximized by the smallest possible integers, so

```math
\boxed{
\sum_{q\in Q(a)}\frac1q
\le
H_{\left\lfloor(\sqrt{8a+1}-1)/2\right\rfloor}.
}
```

In particular,

```math
\sum_{q\in Q(a)}\frac1q
\le
\frac12\log a+O(1).
```

This does not close the global problem after summing over all root sponsors, but it shows that one root point can support only a logarithmic distinct persistent spectrum.

---

## 6. Interpretation

The remaining exact-progression multiplicity is not free. It is financed by a unique root sponsor:

```math
\boxed{
\text{persistence copies}\times\text{step size}
\le
\text{root sponsor label}.
}
```

The obstruction is therefore concentrated in repeated very small steps, especially `q=1`, because those consume the sponsor budget most slowly.

The next target is a genuinely additive statement:

```math
\boxed{
\text{prove that one root sponsor cannot repeatedly regenerate the same small lifted progression at near-maximal budget efficiency.}
}
```

Possible routes are:

1. classify the state-containment tree of one fixed lifted progression;
2. show that every branching persistence event forces a new translated grid in the root set;
3. show that long single-branch persistence forces nested component anchors with large total displacement;
4. search computationally for shell-compatible self-replicating persistence gadgets.