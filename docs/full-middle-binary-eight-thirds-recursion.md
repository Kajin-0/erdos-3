# Full-middle binary eight-thirds recursion

## Status

Exact strengthening of the deletion-DAG occurrence recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Run side-anchor deletion until a three-term-progression-free residual of size `s` remains, and put

```math
K=|D|-s.
```

The spanning-forest construction supplies two structural child families whose total cardinality is exactly `2K`. After retaining at most one structural occurrence per parent element, at least `2K/3` structural occurrences remain.

The earlier recursion retained only one of three valuation colors in the middle role. That restriction is unnecessary for recursive descent: the full middle child at a fixed center is already four-term-progression-free. Retaining every sponsored middle occurrence contributes harmonic mass at least `2K/N`.

Combining the full middle family with the thinned structural family gives a binary occurrence genealogy with harmonic branching factor `8/3`:

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac83 H(D)
-
\frac83\frac{r_3(N)}N.
}
```

Every parent element creates at most two retained child occurrences.

The theorem still concerns harmonic mass with multiplicity. It does not control harmonic mass of distinct numerical labels.

---

# 1. Side-anchor deletion family

Write the selected progressions as

```math
(a_i,b_i,c_i),
\qquad
 a_i+c_i=2b_i,
\qquad
 i=1,\ldots,K,
```

where `a_i` is the deleted coordinated side anchor, `b_i` is the middle point, and `c_i` is the opposite endpoint.

Let

```math
q_i=|b_i-a_i|=|c_i-b_i|.
```

Because the progression lies in an interval of length `N`,

```math
\boxed{q_i\le N/2.}
```

Every deleted sponsor `a_i` occurs in exactly one selected progression and therefore creates exactly one sponsored middle occurrence of numerical label `q_i`.

---

# 2. Full middle children are four-term-progression-free

For every center `x`, define the full sponsored middle child

```math
M_x
=
\{q_i:b_i=x\}.
```

There is no duplication inside one `M_x`: a center `x` and a positive step `q` determine the progression

```math
x-q,
\qquad x,
\qquad x+q
```

uniquely.

Suppose

```math
q,
\quad q+r,
\quad q+2r,
\quad q+3r
```

were contained in `M_x`. Then the four points

```math
x+q,
\quad x+q+r,
\quad x+q+2r,
\quad x+q+3r
```

would all lie in `D`, giving a nontrivial four-term arithmetic progression in `D`.

Therefore

```math
\boxed{M_x\text{ is four-term-progression-free for every }x.}
```

Every element of every `M_x` is at most `N/2`, so the full middle family lies strictly below the parent scale after dyadic shell resolution.

---

# 3. Exact full-middle harmonic load

Every selected progression contributes exactly one middle occurrence. Hence

```math
\sum_x H(M_x)
=
\sum_{i=1}^{K}\frac1{q_i}.
```

Since `q_i<=N/2`,

```math
\frac1{q_i}\ge\frac2N.
```

Therefore

```math
\boxed{
\sum_xH(M_x)
\ge
\frac{2K}{N}.
}
```

No valuation coloring or one-third loss is needed.

The valuation color

```math
\chi(q)=v_2(q)-v_3(q)\pmod3
```

was required in the older side-middle packing program to make the first three dilates of a middle child pairwise disjoint. The deletion-DAG recursion only requires each child itself to be four-term-progression-free and lower scale. The full middle children already satisfy those two properties.

---

# 4. Structural child families

Choose one incoming edge for every nonroot vertex of the deletion DAG. The chosen edges form a spanning forest with components

```math
C_1,\ldots,C_\rho.
```

Translate each component by its numerical minimum:

```math
\Theta_j
=
\{x-\min C_j:x\in C_j,\ x>\min C_j\}.
```

Then each `Theta_j` is four-term-progression-free, lies in `[1,N)`, and

```math
\sum_j|\Theta_j|=K+s-\rho.
```

For every target vertex `v`, let `I_v` be its incoming sponsors, let

```math
p_v=\min I_v,
```

and define

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Each `Delta_v` is four-term-progression-free, lies in `[1,N)`, and the exact indegree-excess identity gives

```math
\sum_v|\Delta_v|=K-s+\rho.
```

Therefore

```math
\boxed{
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
=2K.
}
```

---

# 5. One structural occurrence per parent

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

A residual parent element is associated with at most one structural occurrence. A deleted sponsor is associated with at most three structural occurrences:

1. at most one component occurrence;
2. at most two merge occurrences, because it has exactly two outgoing deletion-DAG edges.

Let `r` be the number of structural occurrences associated with residual vertices. Then

```math
0\le r\le s.
```

The deleted sponsors carry `2K-r` structural occurrences in total. Since each deleted sponsor carries at most three, at least

```math
\frac{2K-r}{3}
```

deleted sponsors carry one or more structural occurrences.

Retain one structural occurrence from every such deleted sponsor, together with all `r` residual structural occurrences. The retained structural cardinality is at least

```math
\frac{2K-r}{3}+r
=
\frac{2K}{3}+\frac{2r}{3}
\ge
\frac{2K}{3}.
```

Every retained structural label is smaller than `N`, so

```math
\boxed{
\sum H(\text{retained structural children})
\ge
\frac{2K}{3N}.
}
```

Each parent element is associated with at most one retained structural occurrence.

---

# 6. Binary eight-thirds theorem

Retain:

1. every sponsored middle occurrence;
2. at most one structural occurrence associated with each parent element.

A deleted sponsor creates exactly one middle occurrence and at most one retained structural occurrence. A residual parent creates no middle occurrence and at most one retained structural occurrence. Thus

```math
\boxed{
\text{every parent element creates at most two retained child occurrences.}
}
```

Combining the middle and structural lower bounds gives

```math
\begin{aligned}
\sum H(\text{retained children})
&\ge
\frac{2K}{N}
+
\frac{2K}{3N}\\
&=
\frac{8K}{3N}.
\end{aligned}
```

Hence

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac83\frac{|D|-s}{N}.
}
```

Using

```math
H(D)\le\frac{|D|}{N}
```

and

```math
s\le r_3(N),
```

we obtain

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

---

# 7. Comparison with earlier binary bounds

The successive internally proved binary lower bounds were

```math
\frac76H(D)-\frac53\frac{r_3(N)}N,
```

then

```math
\frac43H(D)-\frac43\frac{r_3(N)}N,
```

then

```math
\frac{16}{9}H(D)-\frac{16}{9}\frac{r_3(N)}N,
```

and now

```math
\boxed{
\frac83H(D)-\frac83\frac{r_3(N)}N.
}
```

The improvement is not a stronger allocation inequality. It removes an unnecessary one-third middle-color restriction inherited from an older proof branch.

---

# 8. What this resolves

The full middle family gives a canonical lower-scale four-term-progression-free child for every selected progression. The recursion therefore has simultaneously:

1. binary per-parent genealogy;
2. full middle load with no color loss;
3. complementary spanning-forest and merge structural children;
4. harmonic occurrence growth factor `8/3`.

The branching-strength problem is no longer the principal issue.

---

# 9. Remaining gap

The theorem controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` counts descendant occurrences of the numerical label `d`.

The original problem concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

Thus the closing target is

```math
\boxed{
\text{control weighted multiplicity growth at an exponential rate strictly below }8/3.
}
```

Because the genealogy is binary, raw occurrence count grows at most like `2^h`, already below `(8/3)^h`. However, reciprocal weights can grow when labels contract. A closing theorem must therefore control the joint effect of multiplicity and scale contraction, not occurrence count alone.

The most direct next targets are:

1. a potential combining reciprocal weight with genealogical depth or label contraction;
2. an energy bound for repeated numerical labels across distinct child states;
3. a stopping theorem showing that repeated rapid contraction forces scale-compensated distinct mass.