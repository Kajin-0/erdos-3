# Paired side-middle lift expansion

## Status

Exact one-edge overlap theorem for the coordinated role recursion.

The coordinated valuation construction retains exactly one side role for every three-term progression, and sometimes also retains its middle role.  The extra middle incidence is not arbitrary duplicate mass.  If the corresponding side and middle children share a common descendant set, then the two physical lifts cannot overlap freely inside a four-term-progression-free parent.

The main conclusion is:

```math
\boxed{|L_{\rm side}(S)\cup L_{\rm mid}(S)|\ge 3|S|.}
```

Thus a duplicated side-middle continuation has ternary physical capacity at one edge, rather than two unrelated binary lifts occupying the same parent points.

## Setup

Let `P subset Z` be four-term-progression-free.  Fix a three-term progression

```math
a,\qquad a+q,\qquad a+2q
```

inside `P`, with `q>0`.

Assume the coordinated side role for the step `q` is the first-point role.  The reflected last-point case is identical.

Let `S` be a finite positive-integer set such that

```math
q\in S,
```

and suppose `S` is contained in both the first-point child anchored at `a` and the middle-point child anchored at `a+q`.  Equivalently,

```math
a,\ a+s,\ a+2s\in P
```

and

```math
a+q-s,\ a+q,\ a+q+s\in P
```

for every `s in S`.

Assume additionally that

```math
S\cap2S=\varnothing.
```

This holds for every retained coordinated child because its first three dilates are pairwise disjoint.

After translating by `-a`, define

```math
A(S)=\{0\}\cup S\cup2S
```

and

```math
M_q(S)=\{q\}\cup(q-S)\cup(q+S).
```

Both are subsets of the translated parent `P-a`.

## Individual lift sizes

Because `S` consists of positive integers and `S cap 2S` is empty,

```math
|A(S)|=1+2|S|.
```

Also `q-S`, `{q}`, and `q+S` are pairwise disjoint, so

```math
|M_q(S)|=1+2|S|.
```

The two lifts always share the base progression

```math
0,\qquad q,\qquad2q.
```

Indeed,

- `0=q-q`;
- `q in S`;
- `2q=q+q`.

The issue is to control all additional intersections.

## Key intersection lemma

For every

```math
s\in S\setminus\{q\},
```

at most one of the two points

```math
s,\qquad2s
```

can lie in `M_q(S)`.

### Proof

Suppose, for contradiction, that both `s` and `2s` lie in `M_q(S)`.

Then there exist `t,u in S` and signs `epsilon,delta in {−1,+1}` such that

```math
s=q+\epsilon t,
```

and

```math
2s=q+\delta u.
```

There are four sign patterns.  One is impossible by positivity, and each of the other three creates a four-term progression inside

```math
A(S)\cup M_q(S)\subseteq P-a.
```

#### Case 1: `epsilon=-1`, `delta=-1`

Here

```math
s=q-t,
\qquad
2s=q-u.
```

Thus

```math
q=s+t,
\qquad
u=t-s.
```

Positivity of `u` gives `t>s`.  The four points

```math
u,\quad t,\quad q,\quad q+s
```

belong to the union and form an arithmetic progression of common difference `s`.

#### Case 2: `epsilon=-1`, `delta=+1`

Here

```math
s=q-t,
\qquad
2s=q+u.
```

Thus

```math
q=s+t,
\qquad
u=s-t.
```

Positivity gives `s>t`.  The four points

```math
u,\quad s,\quad q,\quad q+t
```

belong to the union and form an arithmetic progression of common difference `t`.

#### Case 3: `epsilon=+1`, `delta=-1`

Here

```math
s=q+t,
\qquad
2s=q-u.
```

This implies

```math
u=q-2s=-s-t<0,
```

contrary to `u in S subset N`.

#### Case 4: `epsilon=+1`, `delta=+1`

Here

```math
s=q+t,
\qquad
2s=q+u.
```

Thus

```math
q=s-t,
\qquad
u=s+t.
```

The four points

```math
q-t,\quad q,\quad s,\quad u
```

belong to the union and form an arithmetic progression of common difference `t`.

Every feasible case contradicts four-term-progression-freeness.  Therefore both `s` and `2s` cannot lie in the middle lift.

## Intersection bound

Every point of

```math
A(S)\cap M_q(S)
```

other than

```math
0,q,2q
```

has a unique representation as either `s` or `2s` for some

```math
s\in S\setminus\{q\},
```

because `S cap 2S` is empty.

The key lemma shows that each such `s` contributes at most one additional intersection point.  Hence

```math
\boxed{
|A(S)\cap M_q(S)|
\le
3+(|S|-1)
=
|S|+2.
}
```

## Paired lift expansion theorem

Using inclusion-exclusion,

```math
|A(S)\cup M_q(S)|
=
|A(S)|+|M_q(S)|-|A(S)\cap M_q(S)|.
```

Therefore

```math
|A(S)\cup M_q(S)|
\ge
2(1+2|S|)-(|S|+2).
```

Thus

```math
\boxed{
|A(S)\cup M_q(S)|\ge3|S|.
}
```

Translating back gives the role-compatible form:

```math
\boxed{
|L_{\rm side}(S)\cup L_{\rm mid}(S)|
\ge3|S|.
}
```

The last-point side role follows by reflection.

## Sharpness

The factor `3` is sharp.

For example, take

```math
S=\{1,5,6\},
\qquad
q=6.
```

Then

```math
A(S)\cup M_q(S)
=
\{0,1,2,5,6,7,10,11,12\},
```

which has cardinality

```math
9=3|S|
```

and contains no nontrivial four-term arithmetic progression.

Thus no larger universal constant can follow from the stated one-edge hypotheses.

## Interpretation for coordinated branching

A selected middle-color three-term progression creates two retained child incidences:

1. its globally assigned side child;
2. its middle child.

If those two branches carry the same lower descendant set `S`, their parent lifts occupy at least `3|S|` points.  Treating them as two unrelated binary lifts would allow a total size as small as `2|S|`; the theorem recovers one full additional copy of `S` from four-term-progression-freeness.

This shows that the extra one-third of harmonic branching has a corresponding physical-space cost whenever duplicated branches continue to overlap below the first level.

## Remaining task

The theorem is local and conditional on a common descendant set.  In the full recursion, paired side and middle children may carry different descendants.

The next target is a weighted coupling lemma:

> Match a substantial portion of the harmonic mass in each selected side-middle pair through common lower descendants, or prove that the unmatched portions are sufficiently separated to consume comparable physical capacity independently.

Either outcome should assign a real parent-space cost to the extra middle-role mass.  This is more precise than seeking a uniform bound on arbitrary tree overlap.