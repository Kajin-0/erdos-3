# Monochromatic absorption component bound

## Status

Exact constant-size theorem for the coordinated side-middle absorption graph.

The earlier absorption-forest theorem used only the primitive dilation conditions

```math
C\cap2C=\varnothing,
\qquad
2C\cap3C=\varnothing.
```

It allowed path components of logarithmic length.  The coordinated valuation construction supplies two additional global constraints:

1. all steps of a retained side child have one fixed value of `v_2(s) mod 2`;
2. all steps of the selected middle child have one fixed value of
   ```math
   \chi(t)=v_2(t)-v_3(t)\pmod 3.
   ```

Together these constraints collapse every absorption path to at most three left vertices.

The main conclusion is:

```math
\boxed{
\text{every connected absorption component contains at most three absorbed sources.}
}
```

Consequently, if `e` nonbase side sources are completely absorbed, then they require at least

```math
\boxed{
|N(E)|\ge e+\left\lceil\frac e3\right\rceil
\ge\frac43e
}
```

distinct middle-step witnesses.

## Coordinated setup

Let `C` be a retained side child and let `q in C` be the base step of a duplicated side-middle pair.  Assume:

```math
C,\qquad2C,\qquad3C
```

are pairwise disjoint, and all elements of `C` have the same parity color

```math
\epsilon(s)=v_2(s)\pmod2.
```

Let `T` be the selected middle child.  Thus all `t in T` have one common color

```math
\chi(t)=v_2(t)-v_3(t)\pmod3.
```

For a nonbase source `s in C setminus {q}`, complete absorption means

```math
s,\quad2s
\in
M_q(T)
=
\{q\}\cup(q-T)\cup(q+T).
```

The bipartite absorption graph has:

- left vertices: completely absorbed sources;
- right vertices: their middle-step witnesses;
- one edge for each representation
  ```math
  cs=q\pm t,
  \qquad c\in\{1,2\}.
  ```

The absorption-forest theorem shows that every component is a path, every left vertex has degree two, and every right vertex has degree at most two.

## Coefficient word of a four-source path

Suppose, for contradiction, that one component contains four consecutive left sources

```math
s_1,s_2,s_3,s_4.
```

Let

```math
r_i\in\{1,2\}
```

be the coefficient used by the edge leaving `s_i` to the right.  The edge entering `s_i` from the left then uses coefficient

```math
3-r_i,
```

because every absorbed source uses coefficient `1` once and coefficient `2` once.

Let the five consecutive right witnesses be

```math
t_0,t_1,t_2,t_3,t_4.
```

At an internal shared witness, the signs of the two affine representations are opposite.  Hence

```math
r_i s_i+(3-r_{i+1})s_{i+1}=2q
\qquad(i=1,2,3).
```

The four-bit word

```math
r_1r_2r_3r_4
```

has only sixteen possibilities.

All five witnesses `t_j` belong to the same selected middle child, so

```math
\chi(t_0)=\chi(t_1)=\cdots=\chi(t_4).
```

All four sources and `q` belong to one retained side child, so

```math
v_2(s_i)\equiv v_2(q)\pmod2
\qquad(i=1,2,3,4).
```

## Seven words force a factor-two witness collision

Direct substitution in the affine recurrences shows that each word in

```math
1211,
\quad1221,
\quad2111,
\quad2112,
\quad2211,
\quad2212,
\quad2221
```

forces two distinct right witnesses to satisfy

```math
|t_i|=2|t_j|
```

for some `i ne j`.

For example:

- `1211` gives `|t_1|=2|t_4|`;
- `1221` gives `|t_4|=2|t_1|`;
- `2111` and `2112` give `|t_0|=2|t_3|`;
- `2211` gives both `|t_3|=2|t_0|` and `|t_1|=2|t_4|`;
- `2212` gives `|t_3|=2|t_0|`;
- `2221` gives `|t_4|=2|t_1|`.

But

```math
\chi(2t)=\chi(t)+1\pmod3,
```

so two witnesses in ratio `2` cannot have the same middle color.  These seven words are impossible.

## Four words force a nonpositive source

The words

```math
1121,
\quad1122,
\quad2121,
\quad2122
```

produce respectively

```math
s_4=-\frac12s_1,
\qquad
s_4=-s_1,
\qquad
s_4=-s_1,
\qquad
s_4=-2s_1.
```

Since all sources are positive, these four words are impossible.

## Four words violate the side parity color

It remains to eliminate

```math
1111,
\quad1112,
\quad1222,
\quad2222,
```

before treating the final word `1212`.

### Prefix `111`

For a word beginning with `111`,

```math
s_2=q-\frac{s_1}{2},
```

and

```math
s_3=\frac q2+\frac{s_1}{4}.
```

Put

```math
a=v_2(q),
\qquad
b=v_2(s_1),
```

with `a congruent b mod 2`.

- If `b<=a`, then the term `s_1/2` has smaller 2-adic valuation than `q`, so `s_2` has parity color opposite to `q`.
- If `b>a`, then parity forces `b>=a+2`.  In that case `v_2(s_2)=a`, while `s_2/2` has valuation `a-1`; hence `v_2(s_3)=a-1`, again the opposite color.

Therefore no word beginning with `111` is possible.  This eliminates `1111` and `1112`.

### Word `2222`

The first two recurrences are

```math
s_2=2(q-s_1),
```

and

```math
s_3=2(q-s_2).
```

If `v_2(s_1) ne v_2(q)`, then `s_2` immediately has the opposite parity color.  If the valuations are equal, retaining the correct color for `s_2` forces

```math
v_2(s_2)\ge v_2(q)+2.
```

Then `q` dominates `q-s_2`, and

```math
v_2(s_3)=v_2(q)+1,
```

again the opposite color.  Thus `2222` is impossible.

### Word `1222`

Positivity allows the parametrization

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=2y,
\qquad
s_4=2q-4y,
```

with

```math
0<y<\frac q2.
```

Put `a=v_2(q)` and `b=v_2(y)`.

- If `b<a`, then `q plus or minus y` has valuation `b`, while `2y` has valuation `b+1`; the colors differ.
- If `b>a`, then keeping `2y` in the color of `q` forces `b+1 congruent a mod 2`, but `2(q-2y)` then has valuation `a+1`, the opposite color.
- If `b=a`, one of `q+y` and `q-y` has valuation exactly `a+1`.

Hence `1222` is impossible.

## The final word `1212`

The only remaining coefficient word is

```math
1212.
```

Its sources have the form

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=y,
\qquad
s_4=2q-y,
```

with

```math
0<y<q.
```

Let

```math
a=v_2(q),
\qquad
b=v_2(y).
```

Since `y=s_3` is a side source,

```math
b\equiv a\pmod2.
```

If `b>a`, then `2q-y` has valuation `a+1`, the wrong parity.  If `b=a`, one of `q+y` and `q-y` has valuation exactly `a+1`.  Therefore necessarily

```math
b<a,
\qquad
a-b\ge2.
```

The five right-witness magnitudes are

```math
t_0=q+2y,
```

```math
t_1=y,
```

```math
t_2=|q-2y|,
```

```math
t_3=q-y,
```

and

```math
t_4=3q-2y.
```

Their 2-adic valuations begin

```math
v_2(t_0)=b+1,
\quad
v_2(t_1)=b,
\quad
v_2(t_2)=b+1,
\quad
v_2(t_3)=b.
```

Set

```math
u=y,
\qquad
v=q-y.
```

Then

```math
t_1=u,
\qquad
t_3=v,
\qquad
t_2=|v-u|,
\qquad
t_0=v+3u.
```

Assume all witnesses have the same `chi`-color.  Since `t_1` and `t_3` have equal 2-adic valuations,

```math
v_3(v)\equiv v_3(u)\pmod3.
```

Since `t_2` has 2-adic valuation one larger,

```math
v_3(v-u)\equiv v_3(u)+1\pmod3.
```

If `v_3(v) ne v_3(u)`, the ultrametric identity gives

```math
v_3(v-u)=\min\{v_3(v),v_3(u)\},
```

whose residue is `v_3(u) mod 3`, contradiction.  Hence

```math
v_3(v)=v_3(u)=:h.
```

The required color of `v-u` then forces

```math
v_3(v-u)>h.
```

After dividing by `3^h`, the two resulting 3-adic units are congruent modulo `3`.  But

```math
v+3u
```

then has 3-adic valuation exactly `h`.  This contradicts the fact that `t_0=v+3u` has 2-adic valuation `b+1` and must have the same `chi`-color as `t_1=u`.

Thus `1212` is also impossible.

## Component-size theorem

All sixteen coefficient words have been eliminated.  Therefore an absorption path cannot contain four consecutive left sources.

```math
\boxed{
\text{Every coordinated monochromatic absorption component has at most three left vertices.}
}
```

The bound is sharp at the level of the stated hypotheses.  For example, one can realize a three-source path with

```math
q=7,
\qquad
C\supseteq\{1,12,13\},
```

and right witnesses

```math
5,6,17,19,
```

all having the same `chi`-color.

## Witness-expansion corollary

Let

```math
e=|E|
```

be the number of nonbase completely absorbed sources and let `c` be the number of nonempty absorption components.

The forest identity gives

```math
|N(E)|=e+c.
```

Since each component contains at most three left vertices,

```math
c\ge\left\lceil\frac e3\right\rceil.
```

Consequently

```math
\boxed{
|N(E)|
\ge
e+\left\lceil\frac e3\right\rceil
\ge
\frac43e.
}
```

Equivalently,

```math
\boxed{
e\le\frac34|N(E)|\le\frac34|T|.}
```

Thus coordinated complete absorption has a strict constant-factor witness cost, with no logarithmic loss and no scale-separation assumption.

## General packing consequence

Let

```math
S\subseteq C,
\qquad
m=|S|,
\qquad
n=|T|,
```

and let `e` sources of `S` be completely absorbed by the middle lift.  The general unabsorbed-source estimate gives

```math
|A(S)\cup M_q(T)|
\ge
1+m+2n-e.
```

Using `e<=3n/4`,

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
1+m+\frac54n.
}
```

Together with the individual lift sizes,

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
1+
\max\left\{
2m,
2n,
m+\frac54n
\right\}.
}
```

For `m=n`, this gives

```math
|A(S)\cup M_q(T)|
\ge
1+\frac94m.
```

This does not yet reach the target leading constant `8/3`, but it replaces the previous logarithmic comparable-scale control by a uniform constant.

## Revised remaining gap

The overlap problem is now quantitatively narrower.

- common descendant mass has ternary paired expansion;
- far-scale unmatched mass has the sharp piecewise packing theorem;
- comparable-scale complete absorption uses components of size at most three and costs at least `4/3` middle witnesses per absorbed source.

The remaining gap is the interaction between:

1. partially absorbed side sources;
2. middle steps not used by complete absorption;
3. endpoint reflections that land on branch points of those partially absorbed sources.

A finite component analysis of the three possible absorption-path sizes may sharpen the `9/4` equal-size constant toward `8/3`.  Unlike the earlier endpoint-charge problem, this is now a bounded local classification problem rather than an unbounded path problem.
