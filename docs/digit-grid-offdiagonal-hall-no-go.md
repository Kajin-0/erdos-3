# Digit-grid off-diagonal Hall no-go

## Status

Symbolic infinite-family counterexample to any universal theorem that attempts to pack all recursive heavy demand using only the unmatched cross-copy physical pair union.

A carry-free base-10 digit set is four-AP-free but contains exponentially many compatible three-AP starts across exponentially many steps. Pairing first-copy and second-copy progressions of the same step produces at least `10^m-9^m` recursive states, while every off-diagonal cross pair lies in a physical grid with only `9^m` possible edges.

After protected maximal extension, every selected completion remains a forced heavy hole. For `m>=5`, total recursive debt exceeds the entire off-diagonal pair-union capacity.

The theorem complements the complete-bipartite projected-copy no-go:

```text
complete-bipartite family defeats internal projected-copy energy;
digit-grid family defeats off-diagonal cross-copy energy.
```

A viable universal theorem must combine both resources or add production/maximality capacity.

---

## 1. Carry-free digit set

Fix

```math
m\ge5
```

and define

```math
D_m
=
\left\{
\sum_{i=0}^{m-1}\varepsilon_i10^i:
\varepsilon_i\in\{0,1,2\}
\right\}.
```

Then

```math
|D_m|=3^m.
```

Its diameter is

```math
L
=
2\sum_{i=0}^{m-1}10^i
=
\frac{2(10^m-1)}9.
```

### Four-AP-freeness

Suppose four elements of `D_m` formed an arithmetic progression. The two second-difference equations give balanced base-10 expansions with coefficients in `[-4,4]`.

A nonzero balanced expansion with coefficients of absolute value at most four cannot vanish in base ten: its largest nonzero digit term exceeds the sum of all smaller possible terms. Therefore both equations hold digitwise.

At each digit, four values in `{0,1,2}` form a four-term arithmetic progression. They must be constant. Hence all four integers are equal.

Thus

```math
\boxed{D_m\text{ is four-AP-free}.}
```

---

## 2. Many three-APs by step

For every nonempty digit subset

```math
S\subseteq\{0,\ldots,m-1\},
```

define

```math
q_S
=
\sum_{i\in S}10^i.
```

A start `x` produces the three-AP

```math
x,
\qquad
x+q_S,
\qquad
x+2q_S
```

inside `D_m` whenever:

```text
its digits in S are zero;
its digits outside S are arbitrary in {0,1,2}.
```

Therefore the number of such starts is

```math
A_S=3^{m-|S|}.
```

The number of ordered pairs of first- and second-copy starts with the same step is at least

```math
\sum_{\varnothing\ne S}A_S^2
=
\sum_{s=1}^m\binom ms9^{m-s}
=
10^m-9^m.
```

---

## 3. Two macro layers in one dyadic block

Choose a power of two `M` satisfying

```math
M>8L.
```

Put

```math
\Delta=\frac{3M}{2}.
```

Define two physical point layers

```math
X=4M+D_m
```

and

```math
Y=4M+\Delta+2D_m.
```

Both layers are four-AP-free. Their macro separation is larger than twice the complete offset width, so any four-AP in `X union Y` would have constant macro-layer indicator. Hence

```math
\boxed{X\cup Y\text{ is four-AP-free}.}
```

Also

```math
X\cup Y\subseteq[4M,8M).
```

---

## 4. Compatible recursive state family

Fix a nonempty `S` and two valid starts `x,y` for step `q_S`. Define

```math
T_{x,y,S}
=
\Delta+2y-x+\{0,q_S,2q_S\}.
```

Because `x,y,q_S<=L` and `M>8L`,

```math
M<\min T_{x,y,S}
```

and

```math
\max T_{x,y,S}<2M.
```

Thus

```math
T_{x,y,S}\subseteq[M,2M).
```

It is a three-AP and hence recursively continuing.

Define the completion reference

```math
c_{x,y,S}
=
4M-\Delta+2x-2y.
```

Then

```math
c_{x,y,S}+T_{x,y,S}
=
4M+x+\{0,q_S,2q_S\}
\subseteq X
```

and

```math
c_{x,y,S}+2T_{x,y,S}
=
4M+\Delta+2y+\{0,2q_S,4q_S\}
\subseteq Y.
```

Distinct triples `(x,y,S)` give distinct ordered double-copy configurations. The family contains at least

```math
10^m-9^m
```

recursive embedded states.

---

## 5. Protected maximal extension

Activate the three matched cross-copy pairs for every state. Protect:

1. every selected completion `c_{x,y,S}`;
2. every alternative positive three-AP completion of every activated pair;
3. one required point from every four-AP witness of every selected completion with step less than `M`.

The finite core remains four-AP-free after adding one selected completion: the macro-layer argument has three layer indices and the selected completion occupies its own layer. Therefore the protected points required in item 3 always exist.

Apply the protected maximal extension lemma. It gives an inclusion-maximal four-AP-free ambient set containing `X union Y` and avoiding every protected point.

Consequently:

```text
every activated pair selects the prescribed completion hole;
every canonical support gap is at least M;
every selected three-point fiber is forced heavy;
every fiber is recursively continuing.
```

---

## 6. Recursive debt

Every state lies in `[M,2M)`, so

```math
H(T_{x,y,S})
>
\frac3{2M}.
```

Therefore total recursive debt satisfies

```math
\boxed{
D_m^{\rm rec}
>
\frac{3(10^m-9^m)}{2M}.
}
```

---

## 7. Complete off-diagonal pair-union capacity

Every off-diagonal cross-copy physical pair has one endpoint in `X` and one endpoint in `Y`. Thus the complete physical union contains at most

```math
|X||Y|=9^m
```

pairs.

Every cross-layer gap is at least

```math
\Delta-L
>
M.
```

Hence every such pair has weight less than `1/M`. Therefore

```math
\boxed{
J(E_{\rm off,union})
<
\frac{9^m}{M}.
}
```

For `m>=5`,

```math
\frac{3(10^m-9^m)}{2M}
>
\frac{9^m}{M},
```

because

```math
\left(\frac{10}{9}\right)^m
>
\frac53.
```

Thus

```math
\boxed{
D_m^{\rm rec}
>
J(E_{\rm off,union})
\qquad(m\ge5).
}
```

The unrestricted off-diagonal Hall theorem fails even for a protected maximal direct-discharge family.

---

## 8. Why internal pair energy can repair this family

The digit layers contain many short internal pairs. Their internal pair energy is not included in the preceding upper bound and may be much larger than the recursive debt.

Therefore this construction is not a counterexample to a theorem using the **combined** resource family

```text
internal first-copy pairs;
internal second-copy pairs;
off-diagonal cross-copy pairs.
```

It proves only that the off-diagonal reserve cannot replace the internal resources universally.

---

## 9. Strategic consequence

Two complementary extremal families are now known:

### Complete-bipartite translation grid

```text
quadratic state incidence;
linear projected-copy resources;
quadratic off-diagonal resources.
```

### Carry-free digit grid

```text
superquadratic compatible state incidence relative to point count;
quadratic off-diagonal physical grid;
large internal short-pair resource.
```

Each resource repairs the other's obstruction. A viable universal potential must retain a controlled combination of internal pair energy, cross-copy incidence energy, production ownership, and maximality-witness output.

No single projected pair family identified so far is sufficient.