# Complete factor-four exclusion for the depth-seven state

## Status

Exact finite computer-assisted theorem with structural witnesses.

Let `S_7` be the 9,840-point state from

```text
docs/contaminated-backbone-depth-seven-chain.md
```

with

```math
S_7\subseteq[1048576,2097152),
\qquad
\max S_7=2021668.
```

This note proves that `S_7` has no sponsor-compatible disjoint three-translate continuation at dyadic scale factor `4`. Together with the previously certified factor-two exclusion,

```math
\boxed{N_{7,2}=N_{7,4}=0.}
```

Therefore every continuation of this recorded state in the standard-dyadic replay-containment model either terminates or has scale factor at least `8`.

**Verifier:** `src/verify_depth7_no_factor4_extension.cpp`.

**Certificate:** `data/depth7_no_factor4_certificate_2026-07-11.txt`.

---

## 1. Finite candidate domain

For factor four, the next shell scale is

```math
L_8=4L_7=4194304.
```

For separation `R`, the raw parent is

```math
G_R
=
(\{0\}\cup S_7)
\cup
(\{0\}\cup S_7+R)
\cup
(\{0\}\cup S_7+2R).
```

The fit condition gives

```math
R
\le
\left\lfloor
\frac{4194304-1-2021668}{2}
\right\rfloor
=
1086317.
```

There are exactly

```text
724212
```

positive separations in this range with even two-adic valuation and therefore the coordinated left-sponsor orientation.

The three translate layers are disjoint exactly when neither `R` nor `2R` is a positive difference of two points of

```math
B=\{0\}\cup S_7.
```

Difference-set filtering leaves exactly

```text
359419
```

disjoint candidates.

The verifier assigns an explicit structural four-term-progression witness to every one of these candidates.

---

## 2. Completion witnesses

Suppose three points of `B` form a positive three-term progression

```math
a_0,a_1,a_2
```

and write

```math
z=2a_2-a_1
```

for its missing right completion. Let `b in B`. If

```math
|z-b|=kR,
\qquad
k\in\{1,2,3\},
```

then one of the available layer patterns has first second-difference coefficient zero and second coefficient `+/-k`. It converts the base triple and `b` into a nontrivial four-term progression in

```math
B+\{0,R,2R\}.
```

The analogous statement holds for missing left completions.

These completion witnesses cover

```text
352979
```

of the `359419` disjoint candidates.

---

## 3. Layer pattern `1001`

Let

```math
y,y+3d\in B
```

and

```math
x,x+d\in B.
```

If

```math
R=x-y-d>0,
```

then the four actual points

```math
y+R,
\quad
x,
\quad
x+d,
\quad
y+3d+R
```

are

```math
x-d,
\quad
x,
\quad
x+d,
\quad
x+2d,
```

and therefore form a nontrivial four-term progression. Their layer pattern is

```text
1001
```

relative to the base points.

This class covers another

```text
215
```

candidates.

---

## 4. Layer pattern `0011`

Let two base pairs have the same positive difference:

```math
x,x+d\in B,
\qquad
y,y+d\in B.
```

If

```math
R=x+2d-y>0,
```

then

```math
x,
\quad
x+d,
\quad
y+R,
\quad
y+d+R
```

becomes

```math
x,
\quad
x+d,
\quad
x+2d,
\quad
x+3d.
```

This is a four-term progression with layer pattern

```text
0011.
```

A range-filtered equal-difference join covers all remaining

```text
6225
```

candidates.

Thus

```math
352979+215+6225=359419,
```

and no disjoint candidate remains.

Therefore

```math
\boxed{N_{7,4}=0.}
```

---

## 5. Forced next-scale consequence

The separate depth-seven verifier already proves

```math
N_{7,2}=0.
```

Combining the two finite searches,

```math
\boxed{
\text{every continuation from }S_7\text{ either terminates or has }L_8/L_7\ge8.
}
```

For

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

three-translate growth gives

```math
\frac{W_{h+1}}{W_h}
=
\frac{6}{c_h}
\left(1+\frac1{|S_h|}\right).
```

Since `|S_7|=9840` and `c_7>=8`, every possible next continuation satisfies

```math
\boxed{
\frac{W_8}{W_7}
\le
\frac{9841}{13120}
\approx0.750076.
}
```

As

```math
W_7=\frac{615}{512},
```

one obtains

```math
\boxed{
W_8\le\frac{29523}{32768}
}
```

if an eighth state exists.

Relative to the depth-five state,

```math
\boxed{
\frac{W_8}{W_5}
\le
\frac{757}{896}
\approx0.844866.
}
```

Thus the alternative branch

```math
8,4
```

that initially grows weighted density must be followed by an expensive step or termination, and the full possible three-generation block

```math
8,4,\ge8
```

contracts relative to `S_5`.

---

## 6. Scope

This is a state-specific finite theorem. It does not prove that every contaminated state has no factor-four continuation after six generations, nor that all future paths eventually contract.

What it does establish is a longer exact compensation block:

```math
4,8,4,4,8,4
\quad\longrightarrow\quad
\ge8
```

or termination.

The next computational problem is to find and classify factor-eight continuations of `S_7`. The next proof problem is to identify a transition potential that explains why the cheap release at depth seven creates the structural completion and equal-difference witnesses that exclude another immediate cheap step.
