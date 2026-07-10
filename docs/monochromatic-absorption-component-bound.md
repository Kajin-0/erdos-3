# Monochromatic absorption component bound

## Status

Exact constant-size theorem for the coordinated side-middle absorption graph.

The earlier absorption-forest theorem used only the primitive dilation conditions

```math
C\cap2C=\varnothing,
\qquad
2C\cap3C=\varnothing.
```

The coordinated valuation construction supplies two additional global constraints:

1. all steps of a retained side child have one fixed color
   ```math
   \epsilon(s)=v_2(s)\pmod2;
   ```
2. all steps of the selected middle child have one fixed color
   ```math
   \chi(t)=v_2(t)-v_3(t)\pmod3.
   ```

Together these constraints imply

```math
\boxed{
\text{every connected absorption component contains at most three absorbed sources.}
}
```

Consequently, if `e` nonbase side sources are completely absorbed, then they require at least

```math
\boxed{
|N(E)|
\ge
e+\left\lceil\frac e3\right\rceil
\ge\frac43e
}
```

distinct middle-step witnesses.

## Coordinated setup

Let `C` be a retained side child and let `q\in C` be the base step of a duplicated side-middle pair. Assume

```math
C,\qquad2C,\qquad3C
```

are pairwise disjoint and `epsilon` is constant on `C`.

Let `T` be the selected middle child, so `chi` is constant on `T`.

For a nonbase source `s\in C\setminus\{q\}`, complete absorption means

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
- an edge for each relation
  ```math
  cs=q\pm t,
  \qquad c\in\{1,2\}.
  ```

The absorption-forest theorem shows that every component is a path, every left vertex has degree two, and every right vertex has degree at most two.

## Coefficient word of a four-source path

Suppose one component contains four consecutive sources

```math
s_1,s_2,s_3,s_4.
```

Let `r_i\in\{1,2\}` be the coefficient used by the edge leaving `s_i` to the right. The edge entering `s_i` uses coefficient `3-r_i`, because every absorbed source uses coefficient `1` once and coefficient `2` once.

Let the five consecutive right witnesses be

```math
t_0,t_1,t_2,t_3,t_4.
```

At an internal shared witness, the two affine representations have opposite signs. Hence

```math
r_i s_i+(3-r_{i+1})s_{i+1}=2q
\qquad(i=1,2,3).
```

The four-bit word

```math
r_1r_2r_3r_4
```

has sixteen possibilities. All five witnesses have the same `chi`-color, and

```math
v_2(s_i)\equiv v_2(q)\pmod2
\qquad(i=1,2,3,4).
```

## Seven words force a factor-two witness collision

Direct substitution shows that each word in

```math
1211,
\quad1221,
\quad2111,
\quad2112,
\quad2211,
\quad2212,
\quad2221
```

forces

```math
|t_i|=2|t_j|
```

for two right witnesses. More specifically:

- `1211`: `|t_1|=2|t_4|`;
- `1221`: `|t_4|=2|t_1|`;
- `2111`, `2112`: `|t_0|=2|t_3|`;
- `2211`: both `|t_3|=2|t_0|` and `|t_1|=2|t_4|`;
- `2212`: `|t_3|=2|t_0|`;
- `2221`: `|t_4|=2|t_1|`.

But

```math
\chi(2t)=\chi(t)+1\pmod3,
```

so two witnesses in ratio `2` cannot have the same middle color.

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

They are impossible for positive sources.

## Four words violate the side parity color

### Prefix `111`

For a word beginning with `111`,

```math
s_2=q-\frac{s_1}{2},
\qquad
s_3=\frac q2+\frac{s_1}{4}.
```

Put

```math
a=v_2(q),
\qquad b=v_2(s_1),
```

with `a\equiv b\pmod2`.

- If `b\le a`, then `s_1/2` has lower 2-adic valuation than `q`, so `s_2` has the opposite parity color.
- If `b>a`, then `b\ge a+2`; hence `v_2(s_2)=a`, while `v_2(s_3)=a-1`.

Thus `1111` and `1112` are impossible.

### Word `2222`

The first two recurrences are

```math
s_2=2(q-s_1),
\qquad
s_3=2(q-s_2).
```

If `v_2(s_1)\ne v_2(q)`, then `s_2` has the opposite parity color. If the valuations are equal, keeping `s_2` in the correct color forces

```math
v_2(s_2)\ge v_2(q)+2,
```

and then

```math
v_2(s_3)=v_2(q)+1.
```

So `2222` is impossible.

### Word `1222`

Positivity gives

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=2y,
\qquad
s_4=2q-4y,
```

with `0<y<q/2`. Put `a=v_2(q)` and `b=v_2(y)`.

- If `b<a`, then `q\pm y` has valuation `b`, while `2y` has valuation `b+1`.
- If `b>a`, retaining `2y` in the color of `q` forces `b+1\equiv a\pmod2`, but `2(q-2y)` has valuation `a+1`.
- If `b=a`, one of `q+y` and `q-y` has valuation exactly `a+1`.

Thus `1222` is impossible.

## The final word `1212`

The sources have the form

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=y,
\qquad
s_4=2q-y,
```

with `0<y<q`.

Let

```math
a=v_2(q),
\qquad b=v_2(y).
```

Since `y=s_3` is a side source, `b\equiv a\pmod2`.

- If `b>a`, then `2q-y` has valuation `a+1`.
- If `b=a`, one of `q+y` and `q-y` has valuation exactly `a+1`.

Hence necessarily

```math
b<a,
\qquad a-b\ge2.
```

The first four right-witness magnitudes are

```math
t_0=q+2y,
\qquad
t_1=y,
\qquad
t_2=|q-2y|,
\qquad
t_3=q-y.
```

Their 2-adic valuations are

```math
b+1,
\quad b,
\quad b+1,
\quad b.
```

Set

```math
u=y,
\qquad v=q-y.
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

Assume all witnesses have the same `chi`-color. Since `t_1` and `t_3` have equal 2-adic valuations,

```math
v_3(v)\equiv v_3(u)\pmod3.
```

Since `t_2` has 2-adic valuation one larger,

```math
v_3(v-u)\equiv v_3(u)+1\pmod3.
```

If `v_3(v)\ne v_3(u)`, then

```math
v_3(v-u)=\min\{v_3(v),v_3(u)\},
```

whose residue is `v_3(u)\pmod3`, contradiction. Therefore

```math
v_3(v)=v_3(u)=:h.
```

The color condition on `v-u` forces `v_3(v-u)>h`. Dividing by `3^h`, the resulting units are congruent modulo `3`. But then

```math
v_3(v+3u)=h,
```

whereas the one-step increase in `v_2(t_0)` would require its 3-adic valuation to be congruent to `h+1\pmod3`. Contradiction.

Thus `1212` is impossible.

## Component-size theorem

All sixteen words are eliminated. Therefore

```math
\boxed{
\text{every coordinated monochromatic absorption component has at most three left vertices.}
}
```

The value `3` is attainable even with a 4-AP-free parent. Take

```math
q=43,
\qquad
C=\{7,36,43,79\},
```

and

```math
T=\{7,29,36,43,115\}.
```

All elements of `C` have the same `epsilon`-color, all elements of `T` have the same `chi`-color, and `C,2C,3C` are pairwise disjoint. The three nonbase sources

```math
79,\quad7,\quad36
```

form a path with right witnesses

```math
115,\quad36,\quad29,\quad7.
```

The associated translated parent set is

```math
\{-72,0,7,14,36,43,50,72,79,86,158\},
```

which contains no nontrivial four-term arithmetic progression.

## Witness-expansion corollary

Let `e=|E|` and let `c` be the number of nonempty components. The forest identity gives

```math
|N(E)|=e+c.
```

Since every component has at most three left vertices,

```math
c\ge\left\lceil\frac e3\right\rceil.
```

Consequently

```math
\boxed{
|N(E)|
\ge
e+\left\lceil\frac e3\right\rceil
\ge\frac43e.
}
```

Equivalently,

```math
\boxed{
e\le\frac34|N(E)|\le\frac34|T|.}
```

Thus coordinated complete absorption has a strict constant-factor witness cost, with no logarithmic loss and no scale-separation assumption.

## General packing consequence

Let `S\subseteq C`, put `m=|S|`, `n=|T|`, and suppose `e` sources of `S` are completely absorbed. The general estimate

```math
|A(S)\cup M_q(T)|
\ge
1+m+2n-e
```

combined with `e\le3n/4` gives

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

For `m=n`,

```math
|A(S)\cup M_q(T)|
\ge
1+\frac94m.
```

This does not yet reach the target leading constant `8/3`, but it replaces logarithmic comparable-scale control by a uniform constant.

## Revised remaining gap

The overlap problem is now narrower:

- common descendant mass has ternary paired expansion;
- far-scale unmatched mass has the sharp piecewise packing theorem;
- global comparable-scale absorption has components of size at most three;
- after dyadic shelling, the separate shell theorem improves this to two.

The remaining task is a bounded local classification of endpoint reflections, partially absorbed sources, and unused middle steps.
