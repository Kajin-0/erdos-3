# Maximal-ambient completion dichotomy

## Status

State-independent reduction for completion obligations in the four-term
reciprocal-sum problem.

After enlarging the ambient four-AP-free set to an inclusion-maximal one, every
positive selected completion is either an actual ambient root or a certified
four-AP hole. Thus the terminal-pair transfer has no anonymous positive-integer
completion class.

---

## 1. Maximal ambient reduction

Let

```math
A\subseteq\mathbb N
```

be four-AP-free. By Zorn's lemma, `A` is contained in an inclusion-maximal
four-AP-free set

```math
B\subseteq\mathbb N.
```

If `A` has divergent reciprocal sum, so does `B`. Therefore it is sufficient
to prove the desired summability theorem for maximal `B`.

For every

```math
c\in\mathbb N\setminus B,
```

maximality implies that

```math
B\cup\{c\}
```

contains a nontrivial four-term progression. Since `B` itself is four-AP-free,
that progression contains `c` and three points of `B`.

Hence

```math
\boxed{
 c\in B
 \quad\text{or}\quad
 c\text{ has a three-root four-AP witness in }B.
}
```

The alternatives are disjoint.

---

## 2. Positivity of shell-pair completions

Let

```math
P=B\cap[N,2N)
```

and let

```math
x<y,
\qquad
x,y\in P,
\qquad
D=y-x.
```

Then

```math
0<D<N.
```

The possible integer three-AP completions of the physical pair are

```math
x-D,
\qquad
y+D,
```

and, when `D` is even,

```math
x+D/2.
```

All are positive:

```math
x-D
\ge
N-(N-1)
=1.
```

Therefore maximality applies to every selected completion of a target pair
inside one standard dyadic shell. There is no nonpositive boundary remainder.

---

## 3. Ambient-root versus ambient-hole targets

Let `Z` be any selected family of physical target pairs in `P`, with one tagged
integer completion for every target.

Partition

```math
Z
=
Z_{\rm root}
\sqcup
Z_{\rm hole},
```

where:

- `Z_root` contains targets whose tagged completion belongs to `B`;
- `Z_hole` contains targets whose tagged completion does not belong to `B`.

Every target in `Z_root` is an edge of an actual ambient three-AP in `B`.
Every target in `Z_hole` has a certified four-AP witness using three ambient
roots from `B`.

Thus the former completion remainder becomes

```text
ambient completed-edge ledger;
globally certified ambient-hole ledger.
```

No third positive-integer class remains.

---

## 4. Three completion roles

For one tagged completion `c`, a target can have one of three roles.

### Right adjacent edge

```math
\{c+d,c+2d\},
\qquad d>0,
```

with weight `1/d`.

### Left adjacent edge

```math
\{c-2d,c-d\},
\qquad d>0,
```

with weight `1/d`.

### Outer edge

```math
\{c-d,c+d\},
\qquad d>0,
```

with weight `1/(2d)`.

For each role define its selected step fiber:

```math
S_c^{+},
\qquad
S_c^{-},
\qquad
S_c^{0}.
```

The weighted target load is

```math
H(S_c^+)
+
H(S_c^-)
+
\frac12H(S_c^0).
```

---

## 5. Every role fiber is four-AP-free

For the right role,

```math
c+S_c^+\subseteq B.
```

For the left role,

```math
c-S_c^-\subseteq B.
```

For the outer role,

```math
c+S_c^0\subseteq B.
```

A four-AP in any step fiber would translate or reflect to a four-AP in `B`.
Therefore all three role fibers are four-AP-free.

---

## 6. Scale descent

For adjacent-edge fibers, both target endpoints lie in `[N,2N)`, so

```math
d<N.
```

After dyadic resolution, every shell base satisfies

```math
M\le N/2.
```

For outer-edge fibers, the endpoint span is `2d<N`, so

```math
d<N/2
```

and every resolved shell base satisfies

```math
M\le N/4.
```

Thus every certified-hole fiber descends strictly below the target shell.

---

## 7. Canonical support allocation with all roles

Assign every ambient hole `c` its deterministic canonical adjacent support pair

```math
f(c)\subseteq B
```

from one four-AP witness. One support pair serves at most two distinct holes.
Each hole has at most three nonempty completion roles. Therefore one physical
support pair indexes at most six selected role fibers:

```math
\boxed{
m(f)\le6.}
```

Let `L_i` denote the weighted load of one role fiber, including the coefficient
`1/2` for an outer-edge fiber. For an unreserved support, call a role fiber
light when

```math
L_i
\le
\frac1{m(f)}w(f).
```

The total light load on `f` is at most `w(f)`. Reserved supports are handled by
the capacity-aware rule and emit no light fibers.

Heavy role fibers remain named lower-scale four-AP-free outputs with their role
coefficient attached.

---

## 8. Maximal-ambient transfer form

Let `C_src` be the carried source-collision pair set and `F_light` the disjoint
unreserved light-support union. Then

```math
\boxed{
J(A)
\le
J(Z_{\rm root})
+
J(C_{\rm src}\cup F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm amb}}\alpha(S)H(S),
}
```

where

```math
\alpha(S)\in\{1,1/2\}
```

records adjacent or outer completion role.

The former anonymous ambient completion term has disappeared. What remains is:

```text
actual ambient completed target edges;
disjoint outgoing pair capacity;
strictly lower-scale certified-hole fibers.
```

The ambient completed-edge term must be packed globally across dyadic parent
blocks; it is no longer an uncertainty about whether the completion exists.

---

## 9. Scope

This theorem does not by itself bound the global ambient-edge union. A target
pair in one shell may be completed by a root in another shell, so the local
`(5/2)L_3(P)` capacity of the current shell is not automatically available.

The remaining cross-shell theorem must route `Z_root` to the dyadic block or
ancestor at which the complete three-AP first appears. The maximal-ambient
reduction guarantees that this is a first-appearance problem, not an existence
problem.
