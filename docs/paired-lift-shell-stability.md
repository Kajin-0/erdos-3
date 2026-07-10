# Shell-stable paired lift corollary

## Status

Exact corollary of the paired side-middle lift expansion theorem.

The original theorem was stated for a common descendant set `S` containing the base progression step `q`.  In recursive applications, descendants are decomposed into dyadic shells, and a given shell need not contain `q`.

No loss occurs: every arbitrary common subset still has ternary paired expansion.

## Setup

Let `P subset Z` be four-term-progression-free and suppose

```math
a,\qquad a+q,\qquad a+2q
```

is a three-term progression in `P`, with `q>0`.

Let `C` be the coordinated side child belonging to this progression and `M` its selected middle child.  Both contain `q`.

Let

```math
T\subseteq C\cap M
```

be any finite common descendant subset.  The set `T` is not required to contain `q`.

Because `C,2C,3C` are pairwise disjoint,

```math
(T\cup\{q\})\cap2(T\cup\{q\})=\varnothing.
```

Put

```math
S=T\cup\{q\}.
```

The paired side-middle expansion theorem applies to `S` and gives

```math
|L_{\rm side}(S)\cup L_{\rm mid}(S)|\ge3|S|.
```

## Adjoining the base step adds at most one point

Write the translated lifts as

```math
A(T)=\{0\}\cup T\cup2T
```

and

```math
M_q(T)=\{q\}\cup(q-T)\cup(q+T).
```

The points `0` and `q` are already present for every `T`:

- `0` is the side anchor;
- `q` is the middle anchor.

Adjoining `q` to the descendant set can add only the point `2q` to the union of the two lifts:

- the new side points are `q` and `2q`;
- the new middle points are `0` and `2q`;
- `0` and `q` were already present.

Hence

```math
|L_{\rm side}(S)\cup L_{\rm mid}(S)|
\le
|L_{\rm side}(T)\cup L_{\rm mid}(T)|+1.
```

If `q notin T`, then `|S|=|T|+1`, so

```math
|L_{\rm side}(T)\cup L_{\rm mid}(T)|
\ge
3(|T|+1)-1.
```

Therefore

```math
\boxed{
|L_{\rm side}(T)\cup L_{\rm mid}(T)|
\ge
3|T|+2
\qquad(q\notin T).
}
```

If `q in T`, the original theorem gives

```math
|L_{\rm side}(T)\cup L_{\rm mid}(T)|\ge3|T|.
```

Combining both cases:

```math
\boxed{
|L_{\rm side}(T)\cup L_{\rm mid}(T)|
\ge
3|T|
\quad\text{for every }T\subseteq C\cap M.
}
```

The reflected last-point side child satisfies the same conclusion.

## Dyadic-shell consequence

Let

```math
T_k=(C\cap M)\cap[2^k,2^{k+1}).
```

Then every shell has the independent paired expansion bound

```math
\boxed{
|L_{\rm side}(T_k)\cup L_{\rm mid}(T_k)|
\ge3|T_k|.
}
```

Thus the paired theorem is fully compatible with the shell decomposition used by the harmonic recursion.  Common descendant mass may be separated by scale without losing the ternary physical-space factor.

## Weighted interpretation on one shell

For a shell `T subseteq [R,2R)`,

```math
\frac{|T|}{2R}
\le
H(T)
\le
\frac{|T|}{R}.
```

The paired expansion therefore implies

```math
|L_{\rm side}(T)\cup L_{\rm mid}(T)|
\ge
3R H(T).
```

Using `H(T)<=|T|/R`, this becomes the exact bound

```math
\boxed{
|L_{\rm side}(T)\cup L_{\rm mid}(T)|
\ge3R H(T).
}
```

This gives a direct cardinality cost for common harmonic descendant mass at scale `R`.

## Remaining task

For each duplicated side-middle pair, split lower descendant mass into:

1. common shell mass, charged by the `3R H(T)` paired-expansion bound;
2. unmatched shell mass, which must be charged through separation between the two child states.

The common part is now quantitatively controlled at every scale.  The unresolved part is a global packing inequality for the unmatched descendants.