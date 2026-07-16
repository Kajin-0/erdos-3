# Off-diagonal cross-copy pair reserve

## Status

State-independent pair-energy theorem for every recursively continuing completion-step shell.

The two affine copies of one state contain a quadratic family of cross-copy physical pairs. After removing the matched vertical pairs that constitute the activated target debt, the remaining off-diagonal pairs still have enough total reciprocal-gap energy to pay the entire recursive state.

This is the first local resource that scales quadratically with the complete-bipartite double-copy obstruction.

---

## 1. Recursive step state

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

be recursively continuing. Then

```math
n\ge3.
```

---

## 2. Adjacent completion roles

For a right-adjacent role, the two affine point copies are

```math
X=\{c+d_i:1\le i\le n\}
```

and

```math
Y=\{c+2d_j:1\le j\le n\}.
```

The left-adjacent role is the reflected version and has identical pair gaps.

The matched pairs

```math
\{c+d_i,c+2d_i\}
```

have gaps `d_i` and form the activated target family of total weight `H(T)`.

Define the off-diagonal cross-copy pair family

```math
E_{\rm off}(T)
=
\bigl\{
\{c+d_i,c+2d_j\}:i\ne j
\bigr\}.
```

Because

```math
2d_j\ge2M>d_i,
```

every pair is nondegenerate, with gap

```math
2d_j-d_i>0.
```

Distinct ordered index pairs `(i,j)` give distinct physical pairs inside one embedded state. Thus

```math
|E_{\rm off}(T)|=n(n-1).
```

### Case `n>=4`

Every gap satisfies

```math
2d_j-d_i
<
4M-M
=
3M.
```

Therefore every off-diagonal pair has weight greater than `1/(3M)`, and

```math
J(E_{\rm off}(T))
>
\frac{n(n-1)}{3M}
\ge
\frac nM
\ge
H(T).
```

### Case `n=3`

Since `T` is recursive,

```math
T=\{d,d+q,d+2q\}
```

with `d>2q`.

The six off-diagonal gaps are

```math
d-2q,
\quad d-q,
\quad d,
\quad d+2q,
\quad d+3q,
\quad d+4q.
```

Their energy contains the two matched-denominator terms

```math
\frac1d
+
\frac1{d+2q}
```

and also

```math
\frac1{d-2q}
>
\frac1{d+q}.
```

Hence

```math
J(E_{\rm off}(T))
>
\frac1d
+
\frac1{d+q}
+
\frac1{d+2q}
=
H(T).
```

Thus for every adjacent recursive state,

```math
\boxed{
J(E_{\rm off}(T))>H(T).
}
```

---

## 3. Outer completion role

For an outer role, the two affine copies are

```math
X=\{c-d_i:1\le i\le n\}
```

and

```math
Y=\{c+d_j:1\le j\le n\}.
```

The matched activated pairs have gaps `2d_i` and total weight

```math
\frac12H(T).
```

The off-diagonal pairs have gaps

```math
d_i+d_j,
\qquad i\ne j.
```

Every such gap is strictly less than `4M`, so every weight is greater than `1/(4M)`. There are `n(n-1)` distinct pairs. Therefore

```math
J(E_{\rm off}(T))
>
\frac{n(n-1)}{4M}
\ge
\frac n{2M}
\ge
\frac12H(T),
```

because `n>=3` implies `n-1>=2`.

Hence

```math
\boxed{
J(E_{\rm off}(T))
>
\frac12H(T)
}
```

for every outer recursive state.

---

## 4. Unified role-weighted form

Let

```math
\alpha(T)
=
\begin{cases}
1,&\text{adjacent role},\\
1/2,&\text{outer role}.
\end{cases}
```

Then every recursive embedded state has a physical off-diagonal cross-copy pair set satisfying

```math
\boxed{
J(E_{\rm off}(T))
>
\alpha(T)H(T).
}
```

The activated matched target pairs are excluded from `E_off(T)`. Thus this is genuinely additional local pair capacity inside the same double-affine rectangle.

---

## 5. Complete-bipartite grid

In the maximal complete-bipartite no-go family, one state is indexed by one first-copy node `a` and one second-copy node `c`.

The six off-diagonal cross pairs of its two three-point copies have one endpoint in the copy indexed by `a` and one endpoint in the copy indexed by `c`. Because the projected copies are disjoint, a physical off-diagonal pair uniquely determines:

```text
first-copy node a;
second-copy node c;
point index in each copy.
```

Therefore all off-diagonal pair sets are disjoint across the `k^2` states. Their total capacity grows quadratically and pays the quadratic state debt.

This explains exactly why the projected-copy Hall theorem failed: it omitted the resource with the correct incidence order.

---

## 6. General overlap problem

For arbitrary direct-discharge families, one physical off-diagonal pair may occur in several embedded states. The local theorem does not prove global disjointness.

However the complete ordered data

```math
(c,\text{role},d_i,d_j)
```

is injective before physical projection. Repeated physical off-diagonal pairs therefore carry a higher-order affine incidence relation rather than anonymous multiplicity.

The next packing problem is:

```text
first physical off-diagonal-pair appearance
    -> pair capacity;
repeated appearance
    -> affine grid / reference-difference token.
```

Unlike projected copy energy, the off-diagonal family has quadratic cardinality in dense copy-incidence configurations.

---

## 7. Scale behavior

Adjacent off-diagonal gaps lie in `(0,3M)`. Outer off-diagonal gaps lie in `(2M,4M)`.

Thus this reserve is not uniformly gap-descending. It is an incidence reserve rather than a pure triangular reserve.

A complete potential must combine:

1. lower-gap horizontal-chain pairs for triangular descent;
2. off-diagonal cross pairs for dense two-projection incidence;
3. first-appearance or grid tokens for repeated cross-pair projection;
4. production-token ownership to prevent arbitrary activation.

---

## 8. Strategic consequence

Every recursive heavy state now has three separate local pair reservoirs:

```text
first internal copy;
second internal copy;
off-diagonal cross-copy pairs.
```

The first two can fail globally in complete-bipartite incidence. The third has the correct quadratic growth and repairs that exact obstruction.

The remaining universal question is whether four-AP-free direct-discharge geometry can force simultaneous congestion of all three reservoirs without creating compensating maximality or production output.