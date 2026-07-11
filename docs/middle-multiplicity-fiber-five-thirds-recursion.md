# Middle multiplicity-fiber five-thirds recursion

## Status

Exact one-generation multiplicity-resolution theorem for the full-middle deletion-DAG recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Run side-anchor deletion until a three-term-progression-free residual of size `s` remains, and put

```math
K=|D|-s.
```

The full-middle binary theorem retains every selected common-difference occurrence and obtains harmonic occurrence growth factor `8/3`. The present note resolves all repeated middle labels inside one parent node:

- retain one terminal distinct copy of each selected step `q`;
- convert every additional occurrence of `q` into a lower-scale four-term-progression-free child of center differences.

Combining this multiplicity resolution with the existing thinned structural family gives a binary hybrid output satisfying

```math
\boxed{
H(\text{terminal distinct steps})
+
\sum H(\text{recursive children})
\ge
\frac53 H(D)
-
\frac53\frac{r_3(N)}N.
}
```

This bound is weaker than the raw `8/3` occurrence theorem, but it removes all within-node multiplicity of middle labels exactly. It therefore addresses the actual distinct-mass bottleneck rather than only strengthening occurrence branching.

---

# 1. Selected middle occurrences

Write the selected progressions as

```math
(a_i,b_i,c_i),
\qquad
 a_i+c_i=2b_i,
\qquad
 i=1,\ldots,K,
```

where `a_i` is the deleted sponsor, `b_i` is the center, and

```math
q_i=|b_i-a_i|=|c_i-b_i|.
```

Because each progression lies in an interval of length `N`,

```math
1\le q_i\le N/2.
```

A center `x` and a positive step `q` determine the progression

```math
x-q,
\qquad x,
\qquad x+q
```

uniquely. Hence there is at most one selected progression with a given ordered pair `(x,q)`.

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the set of distinct selected steps, and write

```math
m(q)=|\{i:q_i=q\}|.
```

Then

```math
\sum_{q\in Q}m(q)=K.
```

---

# 2. Center fibers of a repeated step

For every `q in Q`, define its center fiber

```math
X_q
=
\{b_i:q_i=q\}.
```

Then

```math
|X_q|=m(q).
```

Each `X_q` is a subset of `D`, and therefore is four-term-progression-free.

Let

```math
x_q=\min X_q
```

and define the multiplicity-difference child

```math
\Xi_q
=
\{x-x_q:x\in X_q,\ x>x_q\}.
```

Then

```math
|\Xi_q|=m(q)-1.
```

Since all centers lie in `[N,2N)`, every element of `Xi_q` lies in `[1,N)`:

```math
\boxed{\Xi_q\subseteq[1,N).}
```

If

```math
d,\ d+r,\ d+2r,\ d+3r\in\Xi_q,
```

then translating by `x_q` gives a four-term progression inside `X_q subseteq D`. Hence

```math
\boxed{\Xi_q\text{ is four-term-progression-free}.}
```

---

# 3. Exact multiplicity-excess identity

Summing over the distinct selected steps gives

```math
\begin{aligned}
\sum_{q\in Q}|\Xi_q|
&=\sum_{q\in Q}(m(q)-1)\\
&=K-|Q|.
\end{aligned}
```

Therefore

```math
\boxed{
|Q|+\sum_{q\in Q}|\Xi_q|=K.
}
```

This is the exact middle-label multiplicity decomposition:

- one representative copy for every distinct numerical step;
- one lower-scale center-difference occurrence for every additional copy.

No middle occurrence is lost at the cardinality level.

---

# 4. Binary sponsor association

For each `q`, choose the selected progression centered at `x_q` as the representative occurrence of `q`.

- Its deleted sponsor is associated with the terminal distinct label `q`.
- Every other selected progression with center `x in X_q` is associated with the recursive occurrence `x-x_q in Xi_q`.

Every selected progression has a unique deleted sponsor. Thus every deleted sponsor receives exactly one multiplicity-resolved middle output:

```math
\boxed{
\text{one terminal distinct step or one }\Xi_q\text{ occurrence}.
}
```

Use the existing spanning-forest/merge thinning to retain at most one structural occurrence associated with each parent element. Therefore:

- a deleted sponsor creates one multiplicity-resolved middle output and at most one structural output;
- a residual parent creates at most one structural output.

Hence

```math
\boxed{
\text{every parent element creates at most two outputs.}
}
```

The hybrid genealogy remains binary.

---

# 5. Harmonic mass of the multiplicity-resolved middle output

Every representative step satisfies `q<=N/2`, so

```math
\frac1q\ge\frac2N.
```

Every recursive multiplicity-difference label lies below `N`, so each contributes more than `1/N`.

Consequently,

```math
\begin{aligned}
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
&\ge
\frac{2|Q|}{N}
+
\frac{K-|Q|}{N}\\
&=
\frac{K+|Q|}{N}\\
&\ge
\frac KN.
\end{aligned}
```

Thus

```math
\boxed{
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
\ge
\frac KN.
}
```

Here `H(Q)` is terminal distinct harmonic mass inside this parent node. The sets `Xi_q` are genuine lower-scale four-term-progression-free recursive children.

---

# 6. Adding the thinned structural family

The spanning-forest and merge-difference structural families have total cardinality `2K`. Retaining at most one structural occurrence per parent element preserves at least `2K/3` structural occurrences. Every retained structural label is below `N`, so

```math
\boxed{
\sum H(\text{retained structural children})
\ge
\frac{2K}{3N}.
}
```

Combining this with the multiplicity-resolved middle output gives

```math
\begin{aligned}
&H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
\sum H(\text{retained structural children})\\
&\qquad\ge
\frac KN+
\frac{2K}{3N}\\
&\qquad=
\frac{5K}{3N}.
\end{aligned}
```

Hence

```math
\boxed{
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
\sum H(\text{retained structural children})
\ge
\frac53\frac{|D|-s}{N}.
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
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
\sum H(\text{retained structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

---

# 7. Interpretation

The raw full-middle theorem gives factor `8/3`, but counts every repeated step separately. The present theorem gives factor `5/3` for a more informative hybrid quantity:

1. terminal harmonic mass of distinct selected steps;
2. recursive lower-scale children encoding exactly the excess multiplicity;
3. recursive structural children from the deletion DAG.

The identity

```math
|Q|+\sum_q|\Xi_q|=K
```

shows that within-node middle multiplicity is not discarded. It is converted into lower-scale four-term-progression-free structure.

This is a direct partial resolution of the multiplicity bottleneck.

---

# 8. Remaining gap

The same numerical terminal step can still occur in different parent nodes, and recursive `Xi_q` or structural children can also repeat across states. Thus the theorem does not yet establish a global distinct-mass gain.

The next target is now more specific:

```math
\boxed{
\text{control repetition of terminal representatives and fiber children across different parent states.}
}
```

Possible routes are:

1. group equal terminal steps across sibling or same-depth states and repeat the center-fiber construction globally;
2. construct a potential that counts terminal distinct mass once while recursively charging repeated copies to lower-scale fibers;
3. prove that repeated cross-state copies require disjoint sponsor mass or create an additional lower-scale difference family.
