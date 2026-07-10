# Seven-thirds local packing counterexample

## Status

Exact finite counterexample to a proposed one-edge packing theorem.

The coordinated role recursion produces a harmonic branching factor `8/3`.  A natural local target was therefore to prove, for every paired side-middle shell with equal cardinalities,

```math
|A(S)\cup M_q(T)|\ge \frac83|S|-O(1),
```

where

```math
A(S)=\{0\}\cup S\cup2S
```

and

```math
M_q(T)=\{q\}\cup(q-T)\cup(q+T).
```

This target is false, even under all coordinated valuation constraints and with a four-term-progression-free parent.

There is an explicit example with

```math
|S|=|T|=45,
```

but

```math
\boxed{|A(S)\cup M_q(T)|=107<120=\frac83|S|.}
```

The ratio is

```math
\frac{107}{45}\approx2.3778,
```

which is close to the proved lower bound `7/3`.

## The three-source component template

Fix an odd base step `q` and a parameter `x<q`.  Put

```math
s_1=x,
\qquad
s_2=q-x,
\qquad
s_3=\frac{q+x}{2},
```

and

```math
t_0=q-x,
\qquad
t_1=|q-2x|,
\qquad
t_2=x.
```

The three sources satisfy the coefficient-word relations for `211`:

```math
2s_1+2s_2=2q,
```

and

```math
s_2+2s_3=2q.
```

The corresponding absorption component is the path

```math
t_0-s_1-t_1-s_2-t_2-s_3.
```

The first two sources are completely absorbed and the final source is partially absorbed.  Thus the component has three side sources, three middle witnesses, and five side-middle intersection points.

Its translated parent set is

```math
\{0,q\}
\cup
\left\{
 x,
 q-x,
 \frac{q+x}{2},
 2x,
 2q-2x,
 q+x,
 2q-x
\right\}.
```

When the seven variable points are distinct, one component occupies exactly nine parent points.

## Explicit coordinated family

Take

```math
q=4993,
\qquad
R=2048,
```

and

```math
X=
\{
2065,
2149,
2161,
2221,
2241,
2353,
2365,
2437,
2449,
2581,
2641,
2653,
2689,
2737,
2753
\}.
```

For every `x in X`, define the three-source component above.  Let

```math
S
=
\bigcup_{x\in X}
\left\{
 x,
 q-x,
 \frac{q+x}{2}
\right\},
```

and

```math
T
=
\bigcup_{x\in X}
\left\{
 q-x,
 |q-2x|,
 x
\right\}.
```

Then the following exact properties hold.

### Shell and cardinality

```math
S\subseteq[R,2R),
```

and all three affine source images are disjoint, so

```math
\boxed{|S|=45.}
```

The three witness images are also disjoint, so

```math
\boxed{|T|=45.}
```

### Coordinated side color

Put

```math
C=S\cup\{q\}.
```

Every element of `C` has the same side color

```math
v_2(s)\equiv0\pmod2.
```

Moreover,

```math
C,
\qquad2C,
\qquad3C
```

are pairwise disjoint.

### Coordinated middle color

Every element of `T` has the same middle color

```math
v_2(t)-v_3(t)\equiv0\pmod3.
```

Thus this is a legitimate coordinated side-middle incidence system.

### Component decomposition

The complete side-middle intersection graph has exactly fifteen connected components.  Every component has

```math
3
```

side sources,

```math
3
```

middle witnesses, and coefficient word `211` in the orientation above.

Hence the graph has

```math
45
```

left vertices,

```math
45
```

right vertices, and

```math
75
```

intersection edges.

### Four-term-progression-free parent

Define

```math
P=A(S)\cup M_q(T).
```

An exact exhaustive check gives

```math
\boxed{P\text{ contains no nontrivial four-term arithmetic progression}.}
```

The two individual lifts have

```math
|A(S)|=91,
\qquad
|M_q(T)|=91,
```

and their intersection has

```math
|A(S)\cap M_q(T)|=75.
```

Therefore

```math
\boxed{|P|=91+91-75=107.}
```

## Minimal verification script

The following dependency-free Python fragment verifies all finite claims.

```python
from collections import defaultdict, deque

q = 4993
R = 2048
X = {
    2065, 2149, 2161, 2221, 2241,
    2353, 2365, 2437, 2449, 2581,
    2641, 2653, 2689, 2737, 2753,
}


def vp(n, p):
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def has_4ap(values):
    values = set(values)
    hi = max(values)
    for a in values:
        for d in range(1, (hi - a) // 3 + 1):
            if a + d in values and a + 2*d in values and a + 3*d in values:
                return True
    return False


S = set()
T = set()
for x in X:
    S.update({x, q - x, (q + x) // 2})
    T.update({q - x, abs(q - 2*x), x})

C = S | {q}
A = {0} | S | {2*s for s in S}
M = {q} | {q - t for t in T} | {q + t for t in T}
P = A | M

assert S <= set(range(R, 2*R))
assert len(S) == len(T) == 45
assert len({vp(s, 2) % 2 for s in C}) == 1
assert len({(vp(t, 2) - vp(t, 3)) % 3 for t in T}) == 1
assert not (C & {2*s for s in C})
assert not (C & {3*s for s in C})
assert not ({2*s for s in C} & {3*s for s in C})
assert not has_4ap(P)
assert len(A) == len(M) == 91
assert len(A & M) == 75
assert len(P) == 107
```

## Consequence for the recursion

The local strategy

```math
\text{paired side-middle descendants}
\Longrightarrow
\frac83\text{-packing in one parent}
```

cannot hold without additional hypotheses.

The counterexample shows that the shell-local lower bound

```math
|A(S)\cup M_q(T)|
\ge
1+\max\left\{2|S|,2|T|,|S|+\frac43|T|\right\}
```

is close to sharp in the equal-cardinality regime.  In particular, the previously identified `1/3` gap cannot be closed by a stronger universal one-generation incidence count.

The remaining route must use genuinely recursive information absent from this example, such as:

1. persistence of harmonic mass over several descending generations;
2. compatibility of the fifteen local components with lower descendant states;
3. repeated reuse of the same valuation colors across a path;
4. a multigeneration energy or entropy inequality rather than a one-edge union bound.

The revised target is therefore:

> Prove that near-`7/3` local packing cannot persist through many mass-regular generations without either producing a four-term progression or forcing summable termination.
