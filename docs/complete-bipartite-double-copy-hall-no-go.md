# Complete-bipartite double-copy Hall no-go

## Status

Symbolic infinite-family counterexample to the unrestricted two-copy Hall target for recursive affine states.

Four-AP-freeness, two individually sufficient affine pair-energy projections, strict first-copy gap descent, and injectivity of the ordered double lift do **not** imply global pair-capacity packing. A complete bipartite family has quadratically many recursive states but only linearly many projected copy resources.

The construction does not prove that the direct maximal-ambient retained family has this pathology. It proves that any universal theorem must use additional structure: maximality witnesses, production-token ownership, cross-copy pairs, or restrictions on which activated state families arise.

---

## 1. Translation sets

Fix

```math
k\ge29.
```

Define two disjoint geometric sets

```math
A_k
=
\{2\cdot3^i:0\le i<k\},
```

and

```math
C_k
=
\{2\cdot3^{k+j}:0\le j<k\}.
```

Both sets are three-AP-free and therefore four-AP-free. Put

```math
L=\max C_k.
```

Choose a power of two `q` satisfying

```math
q>L.
```

Let

```math
S=\{0,q,2q\}.
```

Choose a power of two `H` to be the least power of two satisfying

```math
H>2(L+4q).
```

Since `L<q`,

```math
H<4(L+4q)<20q.
```

Also

```math
H>8q.
```

---

## 2. Two projected copy layers

Define

```math
X
=
A_k+S
```

and

```math
Y
=
H+C_k+2S.
```

Thus `X` is the disjoint union of `k` three-APs of step `q`, and `Y` is the disjoint union of `k` three-APs of step `2q`.

### Four-AP-freeness of `X`

Write a point of `X` as

```math
a+jq,
\qquad a\in A_k,
\quad j\in\{0,1,2\}.
```

In either second-difference equation for a putative four-AP, the `A_k` contribution has absolute value less than `q`, while the other term is an integer multiple of `q`. Therefore the layer indices `j` must themselves form a four-AP in `{0,1,2}` and are constant. The four offsets would form a four-AP in `A_k`, impossible.

Hence `X` is four-AP-free.

### Four-AP-freeness of `Y`

The same argument applies with layer spacing `2q`. The offset second differences have absolute value less than `2q`, and `C_k` is four-AP-free. Thus `Y` is four-AP-free.

### Four-AP-freeness of the union

After subtracting the macro-layer offset, every point offset in `X` or `Y-H` lies in an interval of width less than

```math
L+4q.
```

Because

```math
H>2(L+4q),
```

the macro-layer indicators in `{0,1}` must have zero second differences in any four-AP. They are constant. The progression would lie entirely in `X` or entirely in `Y`, both impossible.

Therefore

```math
\boxed{X\cup Y\text{ is four-AP-free}.}
```

---

## 3. Placement in one standard dyadic parent block

Translate the union by `4H` and put

```math
P
=
(4H+X)
\cup
(4H+Y).
```

The first layer lies below `4H+3q`, and the second lies below `5H+5q`. Since `H>8q`,

```math
\boxed{P\subseteq[4H,8H).}
```

Translation preserves four-AP-freeness.

---

## 4. Complete bipartite recursive state family

For every

```math
a\in A_k,
\qquad
c\in C_k,
```

define

```math
T_{a,c}
=
H+c-a+S.
```

Because the `C_k` exponents are larger than all `A_k` exponents,

```math
H<\min T_{a,c}.
```

Also

```math
\max T_{a,c}
<
H+L+2q
<
2H.
```

Thus

```math
T_{a,c}\subseteq[H,2H).
```

Every `T_{a,c}` is a three-AP of step `q`, hence recursively continuing.

Define its translated completion reference

```math
r_{a,c}
=
3H+2a-c.
```

Then

```math
r_{a,c}+T_{a,c}
=
4H+a+S,
```

and

```math
r_{a,c}+2T_{a,c}
=
5H+c+2S.
```

These are exactly one first-copy node indexed by `a` and one second-copy node indexed by `c`.

The references are positive. They are also pairwise distinct: if

```math
2a-c=2a'-c',
```

then the separated ternary valuations force `c=c'` and then `a=a'`.

Consequently the ordered double-copy incidence graph is the complete bipartite graph

```math
K_{k,k}.
```

There are `k^2` distinct embedded recursive states, `k` first-copy resources, and `k` second-copy resources.

---

## 5. Total projected pair capacity

Each first copy is a three-AP of step `q`, with complete pair energy

```math
\frac1q+\frac1q+\frac1{2q}
=
\frac5{2q}.
```

Each second copy is a three-AP of step `2q`, with energy

```math
\frac1{2q}+\frac1{2q}+\frac1{4q}
=
\frac5{4q}.
```

Distinct copies inside each macro layer are disjoint because the translation diameters are less than `q`. The two macro layers are disjoint. Therefore the complete projected pair-resource union has exact capacity

```math
\boxed{
J_{\rm copies}
=
k\left(\frac5{2q}+\frac5{4q}\right)
=
\frac{15k}{4q}.
}
```

---

## 6. Quadratic recursive debt

Every state has three elements, all less than

```math
H+L+2q
<
H+3q.
```

Hence

```math
H(T_{a,c})
>
\frac3{H+3q}.
```

Summing over all `k^2` states gives

```math
\boxed{
D_k
=
\sum_{a\in A_k}
\sum_{c\in C_k}
H(T_{a,c})
>
\frac{3k^2}{H+3q}.
}
```

Since `H<20q`,

```math
D_k
>
\frac{3k^2}{23q}.
```

For `k>=29`,

```math
\frac{3k^2}{23q}
>
\frac{15k}{4q}.
```

Indeed this is equivalent to

```math
12k>345.
```

Therefore

```math
\boxed{
D_k>J_{\rm copies}
\qquad(k\ge29).
}
```

---

## 7. Failed Hall inequality

Take the subfamily consisting of all `k^2` states. Its first- and second-copy pair neighborhoods are exactly the `2k` copy resources above. Thus

```math
\sum_{a,c}H(T_{a,c})
>
J\!\left(
\bigcup_{a,c}
(E_1(T_{a,c})\cup E_2(T_{a,c}))
\right).
```

The unrestricted two-choice Hall inequality fails.

The failure persists despite:

```text
every state having two individually sufficient copy resources;
the ordered double lift being injective;
the parent being four-AP-free;
all states lying in one dyadic step shell;
the complete parent support lying in one dyadic root block.
```

---

## 8. What the construction does not prove

The completion references `r_{a,c}` are not required to be maximality-certified holes in this bare geometric construction. The family is therefore a no-go for a theorem based only on double-affine four-AP-free geometry.

A stronger theorem may still hold for the specific state families generated by direct maximal-ambient discharge, because maximality witnesses and the production-token ledger add structure and capacity not used here.

The construction also does not use cross-copy pairs between `X` and `Y`, including the vertical activated pairs themselves. Any successful universal potential may need those resources.

---

## 9. Strategic consequence

The universal target is not

```text
pack every recursive state into the union of its two internal copy energies.
```

That statement is false.

A viable theorem must use at least one additional ingredient:

1. maximality-hole witness pair energy;
2. parent full-edge production tokens;
3. cross-copy or vertical pair resources;
4. restrictions imposed by the actual activated-pair generation mechanism;
5. a higher-order rectangle/grid potential that sees the complete bipartite incidence.

The exact `S7` first-copy flow remains a valid finite theorem. It cannot be promoted to an unrestricted double-copy Hall theorem.