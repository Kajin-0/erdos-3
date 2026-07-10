# Depth-two affine-lift overlap counterexample

## Status

Exact obstruction to a naive bounded-overlap strategy.

The affine-tree recursion forces many depth-`h` lifts to overlap in the root.  A tempting next lemma was that a fixed root point and terminal direction can belong to only boundedly many lifts in a 4-AP-free root.

This is false already at depth two.

There are arbitrarily large finite 4-AP-free sets containing arbitrarily many distinct depth-two ternary lifts which:

1. have the same terminal direction;
2. share the same three root points;
3. arise from genuine predecessor-fiber paths.

A rough quantitative construction gives overlap multiplicity at least a fixed power of the ambient diameter.

Therefore any successful overlap theorem must use more than the endpoint `x`, terminal direction `d`, and 4-AP-freeness of the union.  It must exploit scale distribution, path weights, or the full recursive mass hypotheses.

## A one-parameter family of depth-two lifts

Fix terminal direction

```math
d=1.
```

For an integer parameter `L`, take

```math
q_1=-L-3,
\qquad
q_2=L.
```

The associated depth-two ternary lift is

```math
\mathcal S_L
=
\left\{
q_1+i_1q_2+i_1i_2d:
 i_1,i_2\in\{1,2,3\}
\right\}.
```

A direct expansion gives

```math
\boxed{
\mathcal S_L
=
\{-2,-1,0\}
\cup
\{L-1,L+1,L+3\}
\cup
\{2L,2L+3,2L+6\}.
}
```

Thus every member of the family has the same terminal direction `d=1` and contains the common three-point progression

```math
\boxed{\{-2,-1,0\}.}
```

## Genuine predecessor-path realization

Suppose a root set `D_0` contains `mathcal S_L`.

Set

```math
D_1=E_{q_1}(D_0)
=
\{x:q_1+x,q_1+2x,q_1+3x\in D_0\}.
```

Because `mathcal S_L subseteq D_0`, the three values

```math
L+1,
\qquad
L+2,
\qquad
L+3
```

belong to `D_1`.

Hence

```math
1\in E_{q_2}(D_1),
```

because

```math
q_2+1=L+1,
\quad
q_2+2=L+2,
\quad
q_2+3=L+3.
```

Therefore each `mathcal S_L` is not merely a formal affine set.  It is the full ternary lift of a genuine depth-two predecessor path

```math
D_0
\longrightarrow
E_{-L-3}(D_0)
\longrightarrow
E_L(E_{-L-3}(D_0))
```

ending at the same direction `d=1`.

## Finite-avoidance lemma

Let `U` be any finite 4-AP-free integer set containing

```math
F=\{-2,-1,0\}.
```

Then there are infinitely many integers `L` such that

```math
U\cup\mathcal S_L
```

is still 4-AP-free and introduces no new collision outside the fixed set `F`.

### Proof

Every point of `mathcal S_L` has the form

```math
aL+b
```

with coefficient

```math
a\in\{0,1,2\}.
```

The coefficient-`0` points are the fixed set `F`, the coefficient-`1` points are

```math
L-1,L+1,L+3,
```

and the coefficient-`2` points are

```math
2L,2L+3,2L+6.
```

Fix an ordered choice of four candidate points from

```math
U\cup\mathcal S_L.
```

The condition that they form a four-term arithmetic progression is a system of linear equations in `L`.

For this system to hold identically in `L`, the four coefficients of `L` would themselves have to form a four-term arithmetic progression inside

```math
\{0,1,2\}.
```

The only such coefficient progression is constant.

- Four coefficient-`0` points would lie entirely in `U`, which is 4-AP-free.
- There are only three coefficient-`1` points.
- There are only three coefficient-`2` points.

Hence no nontrivial four-term progression relation is an identity in `L`.  Each fixed candidate pattern excludes at most finitely many, in fact at most one, values of `L`.

There are only finitely many candidate patterns, so only finitely many bad values of `L`.

The same argument applies to unwanted collisions.  Therefore infinitely many admissible `L` remain.

## Arbitrarily large common-overlap families

Start with

```math
U_0=F.
```

Choose `L_1` so that

```math
U_1=U_0\cup\mathcal S_{L_1}
```

is 4-AP-free.

Inductively, after constructing a finite 4-AP-free set `U_{k-1}`, choose `L_k` outside the finite forbidden set supplied by the finite-avoidance lemma, and put

```math
U_k
=
U_{k-1}\cup\mathcal S_{L_k}.
```

Then `U_k` is 4-AP-free and contains `k` distinct depth-two lifts

```math
\mathcal S_{L_1},\dots,\mathcal S_{L_k}
```

with common terminal direction `1` and common root points

```math
-2,-1,0.
```

Thus for every `k` there is a finite 4-AP-free root supporting at least `k` distinct depth-two paths with the same terminal direction through each of those three points.

After translating by `3`, all points are positive.  The common root points become

```math
1,2,3,
```

and 4-AP-freeness and the predecessor-path interpretation are unchanged.

## Rough polynomial-size realization

The construction can be made quantitative.

At stage `k`, the current union has `O(k)` points.  There are `O(k^4)` ordered four-point patterns that could become a new 4-AP after adjoining `mathcal S_L`, and each pattern excludes at most one value of `L`.  Collisions exclude only `O(k)` additional values.

Hence one may choose `L_k` within an interval of length `O(k^4)` beyond `L_{k-1}`.  Summing these increments gives

```math
L_k=O(k^5).
```

The translated root then lies in an interval of length `O(k^5)` while supporting `k` common-overlap depth-two lifts.

Consequently, for infinitely many ambient sizes `M`, one can have fixed-point, fixed-terminal depth-two multiplicity at least

```math
\boxed{cM^{1/5}}
```

for an absolute constant `c>0`.

The exponent `1/5` is not intended to be optimal.  Its purpose is to show that the failure is much stronger than a logarithmic defect.

## Consequence for the previous overlap target

A bound of the form

```math
c_h(x,d)=O_h(1)
```

is impossible, even for `h=2`.

More strongly, no polylogarithmic upper bound in the ambient scale can hold for arbitrary 4-AP-free unions of depth-two lifts.

Therefore the earlier proposed route

```math
\text{forced average lift overlap}
\Longrightarrow
\text{bounded pointwise overlap}
\Longrightarrow
\text{contradiction}
```

cannot work at this level of generality.

## What extra hypotheses remain available

The counterexample uses sparse, deliberately separated lift parameters.  It does not satisfy any demonstrated lower bound on recursive mass at every intermediate node.

A viable overlap theorem must therefore incorporate at least one of:

1. **mass regularity:** every internal node remains above the Roth-error scale;
2. **weighted path abundance:** many lifts occur with controlled scale distribution, not merely arbitrary sparse parameters;
3. **common-node incidence:** paths share substantial intermediate fibers, rather than only a root point and terminal direction;
4. **row-column primitive density:** the lift family arises from the primitive weighted incidence theorem with large total weight;
5. **energy rather than maximum multiplicity:** high second moment across lifts may force a structured collision even though maximum multiplicity alone can be large.

## Revised target

The correct next question is not whether pointwise lift multiplicity is bounded.

It is:

> Can a 4-AP-free root support the amount of **weighted, recursively mass-regular** lift overlap forced by harmonic divergence?

The finite-avoidance family shows that sparse overlap is harmless.  Any contradiction must use the quantitative distribution of the entire recursive tree.