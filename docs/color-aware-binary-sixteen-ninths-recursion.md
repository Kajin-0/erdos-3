# Color-aware binary sixteen-ninths recursion

## Status

Exact strengthening of the spanning-forest binary recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Run side-anchor deletion until a three-term-progression-free residual of size `s` remains, and put

```math
K=|D|-s.
```

The spanning-forest construction supplies two structural child families:

1. component-translation children;
2. merge-difference children.

Their total cardinality is exactly `2K`. Every structural label lies in `[1,N)`. Every deleted sponsor also has a selected common difference `q<=N/2`, carrying one of the three colors

```math
\chi(q)=v_2(q)-v_3(q)\pmod3.
```

Instead of first fixing the middle color and then retaining one structural occurrence per sponsor, choose the middle color jointly with the structural allocation. For sponsors in the chosen color, retain the middle occurrence and at most one structural occurrence. For sponsors outside the chosen color, retain at most two structural occurrences.

This keeps the genealogy binary and yields

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac{16}{9}H(D)
-
\frac{16}{9}\frac{r_3(N)}N.
}
```

The previous binary factors `7/6` and `4/3` are therefore superseded.

The theorem still concerns harmonic mass with multiplicity. It does not control the harmonic mass of distinct numerical labels.

---

# 1. Structural occurrences

Choose one incoming edge for every nonroot vertex of the affine deletion DAG. The selected edges form a spanning forest with components

```math
C_1,\ldots,C_\rho.
```

For each component, translate by its numerical minimum:

```math
\Theta_j
=
\{x-\min C_j:x\in C_j,\ x>\min C_j\}.
```

Each `Theta_j` is four-term-progression-free, lies in `[1,N)`, and

```math
\sum_j|\Theta_j|=|D|-\rho=K+s-\rho.
```

For every target vertex `v`, let `I_v` be its incoming sponsors, let `p_v=min I_v`, and define

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Each `Delta_v` is four-term-progression-free, lies in `[1,N)`, and the exact indegree-excess identity gives

```math
\sum_v|\Delta_v|=K-s+\rho.
```

Hence the total number of structural occurrences is

```math
\boxed{
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
=2K.
}
```

---

# 2. Association with parent elements

Associate every component occurrence

```math
x-\min C_j
```

with the parent element `x`.

Associate every merge occurrence

```math
a-p_v
```

with its nonminimal sponsor `a`.

A residual parent element is associated with at most one structural occurrence. A deleted sponsor is associated with:

- at most one component occurrence;
- at most two merge occurrences, because it has exactly two outgoing DAG edges.

Let

```math
r
```

be the number of structural occurrences associated with residual vertices. Then

```math
0\le r\le s.
```

For each deleted sponsor `a`, let

```math
\ell(a)\in\{0,1,2,3\}
```

be its number of associated structural occurrences. Since the total structural cardinality is `2K`,

```math
\boxed{
\sum_{a\text{ deleted}}\ell(a)=2K-r.
}
```

All `r` residual structural occurrences will be retained.

---

# 3. Color-aware binary allocation

Every deleted sponsor `a` comes from one selected progression with common difference `q_a`. Give `a` the color

```math
c(a)=\chi(q_a)\in\{0,1,2\}.
```

Fix a candidate color `c`.

## Sponsors in the chosen color

If

```math
c(a)=c,
```

retain:

1. the middle occurrence of value `q_a`;
2. one structural occurrence if `ell(a)>=1`.

The middle label satisfies

```math
q_a\le N/2,
```

so its harmonic weight is at least `2/N`. A retained structural label is below `N`, so its harmonic weight is at least `1/N`.

Thus the normalized guaranteed contribution of a chosen-color sponsor is

```math
2+1_{\ell(a)\ge1}.
```

## Sponsors outside the chosen color

If

```math
c(a)\ne c,
```

retain up to two associated structural occurrences. Their normalized guaranteed contribution is

```math
\min\{\ell(a),2\}.
```

In both cases the sponsor creates at most two retained child occurrences.

---

# 4. Averaging over the three colors

Average the normalized contribution of one deleted sponsor over the three possible chosen colors.

If its structural load is `ell`, the average is

```math
g(\ell)
=
\frac{
2+1_{\ell\ge1}
+
2\min\{\ell,2\}
}{3}.
```

Explicitly,

```math
\begin{array}{c|cccc}
\ell&0&1&2&3\\
\hline
g(\ell)&\frac23&\frac53&\frac73&\frac73
\end{array}
```

For every

```math
\ell\in\{0,1,2,3\},
```

one has the affine lower bound

```math
\boxed{
g(\ell)\ge\frac23+\frac59\ell.}
```

Indeed, equality holds at `ell=0` and `ell=3`, while the two intermediate values are larger.

Therefore the average, over the three colors, of the total normalized harmonic contribution from deleted sponsors is at least

```math
\begin{aligned}
\sum_{a\text{ deleted}}g(\ell(a))
&\ge
\frac23K
+
\frac59\sum_a\ell(a)\\
&=
\frac23K
+
\frac59(2K-r)\\
&=
\frac{16}{9}K-
\frac59r.
\end{aligned}
```

Adding the `r` retained residual structural occurrences gives average total normalized contribution at least

```math
\frac{16}{9}K+
\frac49r
\ge
\frac{16}{9}K.
```

Hence some color `c_*` satisfies

```math
\boxed{
N\sum H(\text{retained children for }c_*)
\ge
\frac{16}{9}K.
}
```

Equivalently,

```math
\boxed{
\sum H(\text{retained children})
\ge
\frac{16K}{9N}.
}
```

---

# 5. Binary sixteen-ninths theorem

Since

```math
K=|D|-s,
```

we obtain

```math
\sum H(\text{retained children})
\ge
\frac{16}{9}\frac{|D|-s}{N}.
```

Using

```math
H(D)\le\frac{|D|}{N}
```

and

```math
s\le r_3(N),
```

this yields

```math
\boxed{
\sum H(\text{retained children})
\ge
\frac{16}{9}H(D)
-
\frac{16}{9}\frac{r_3(N)}N.
}
```

Every parent element creates at most two retained child occurrences:

- a chosen-color deleted sponsor creates one middle and at most one structural occurrence;
- an unchosen-color deleted sponsor creates at most two structural occurrences;
- a residual parent creates at most one structural occurrence.

Thus

```math
\boxed{
\text{the retained occurrence genealogy is binary.}
}
```

---

# 6. Comparison with earlier binary bounds

The successive binary lower bounds are now:

```math
\frac76H(D)-\frac53\frac{r_3(N)}N,
```

then

```math
\frac43H(D)-\frac43\frac{r_3(N)}N,
```

and now

```math
\boxed{
\frac{16}{9}H(D)-\frac{16}{9}\frac{r_3(N)}N.
}
```

The improvement comes from using the middle-color choice as part of the binary allocation:

- a sponsor selected for the middle role needs only one structural slot;
- a sponsor not selected for the middle role can use both binary slots for structural occurrences.

The abstract load distribution showing that the averaging constant cannot be improved from the present information alone is:

```math
\frac13K
```

sponsors with structural load `0`, and

```math
\frac23K
```

sponsors with structural load `3`, with no residual structural occurrences. For this distribution the averaged lower bound is exactly `16K/9`.

Whether such an extremal load distribution is realizable by genuine four-term-progression-free deletion DAGs is a separate structural question.

---

# 7. Remaining gap

The theorem controls the multiset quantity

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` counts descendant occurrences of the numerical label `d`.

The original problem concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

Therefore the closing target becomes:

```math
\boxed{
\text{control weighted multiplicity growth at an exponential rate strictly below }16/9.
}
```

A more immediate structural target is to determine whether the abstract extremal load pattern

```math
\ell=0\text{ on one third of sponsors},
\qquad
\ell=3\text{ on two thirds},
```

can occur at large scale in an actual side-anchor deletion DAG. Ruling it out quantitatively would improve the binary factor further.