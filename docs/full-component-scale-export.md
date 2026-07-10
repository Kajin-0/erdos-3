# Full componentwise scale export

## Status

Exact completion of the finite component classification introduced in the component-deficit potential reduction.

Let `S subseteq [R,2R)` be a coordinated side shell and let `T` be the paired selected middle set.  Form the full side-middle intersection graph with edges

```math
cs=q\pm t,
\qquad c\in\{1,2\}.
```

The graph is a forest of paths.  The component-deficit reduction showed that the scale-compensated `8/3` packing inequality follows if every component `K` exports at least

```math
\kappa(K)
=
\max\left\{0,\left\lceil\frac{|V(K)|}{3}\right\rceil-1\right\}
```

distinct right witnesses below `R`.

This note proves exactly that.

The only component types requiring a credit are

```math
(2,2),
\quad(2,3),
\quad(3,2),
\quad(3,3),
\quad(4,3),
```

where `(l,r)` denotes the number of side and middle vertices.  The first four types export at least one lower-scale witness; the last type exports at least two.

Consequently, for equal shell cardinalities

```math
|S|=|T|=m,
```

one has the exact compensated estimate

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+\frac83m-\eta,
}
```

where `0<=eta<=2` records possible anchor coincidences.

## Path notation

Orient a path from left to right and list its side vertices as

```math
s_1,s_2,\ldots,s_l.
```

For every side vertex define

```math
r_i\in\{1,2\}
```

to be the branch coefficient used on the edge leaving `s_i` to the right.  At an internal side vertex the coefficient on the entering edge is then

```math
3-r_i.
```

At every shared middle witness,

```math
\boxed{
r_i s_i+(3-r_{i+1})s_{i+1}=2q.
}
```

The witness on that edge has magnitude

```math
\boxed{
t_i=|q-r_i s_i|.
}
```

All side sources satisfy

```math
R\le s_i<2R.
```

The coordinated side color means

```math
v_2(s_i)\equiv v_2(q)\pmod2.
```

The right witnesses are distinct vertices of the path, so witnesses identified at different path positions are automatically distinct.

# Type `(2,2)`

Orient the path as

```math
s_1-t_1-s_2-t_2.
```

The first source is partial and the second is complete.  There are four coefficient words.

## Word `11`

The shared equation gives

```math
s_2=q-\frac{s_1}{2}.
```

The endpoint witness is

```math
t_2=|q-s_2|=\frac{s_1}{2}<R.
```

## Word `12`

Here

```math
s_2=2q-s_1,
```

so

```math
q=\frac{s_1+s_2}{2}.
```

Therefore the shared witness satisfies

```math
t_1=|q-s_1|
=\frac{|s_2-s_1|}{2}
<R.
```

## Word `21`

Here

```math
s_2=q-s_1,
\qquad q=s_1+s_2.
```

Thus

```math
t_1=|q-2s_1|
=|s_2-s_1|
<R.
```

## Word `22`

Here

```math
s_2=2q-2s_1,
\qquad q=s_1+\frac{s_2}{2}.
```

The two witnesses are

```math
t_1=s_1-\frac{s_2}{2}
```

and

```math
t_2=\left|s_1-\frac{3s_2}{2}\right|.
```

Suppose both were at least `R`.  The first inequality gives

```math
s_1\ge R+\frac{s_2}{2}.
```

The alternative

```math
s_1-\frac{3s_2}{2}\ge R
```

is impossible because it would force `s_1>2R`.  Hence

```math
\frac{3s_2}{2}-s_1\ge R,
```

so

```math
s_1\le\frac{3s_2}{2}-R.
```

Combining gives

```math
R+\frac{s_2}{2}
\le
\frac{3s_2}{2}-R,
```

hence `s_2>=2R`, contradiction.

Therefore one of `t_1,t_2` is below `R`.

Thus every `(2,2)` component exports one lower-scale witness.

# Type `(2,3)`

Orient the path as

```math
t_0-s_1-t_1-s_2-t_2.
```

Both side sources are completely absorbed.

Again inspect the four coefficient words.

## Word `11`

As above,

```math
s_2=q-\frac{s_1}{2},
```

and the right endpoint witness is

```math
t_2=\frac{s_1}{2}<R.
```

## Word `12`

Here

```math
q=\frac{s_1+s_2}{2},
```

so the shared witness is

```math
t_1=\frac{|s_2-s_1|}{2}<R.
```

## Word `21`

Here

```math
q=s_1+s_2,
```

and

```math
t_1=|s_2-s_1|<R.
```

## Word `22`

Here

```math
q=s_1+\frac{s_2}{2}.
```

The left endpoint uses coefficient `1`, so

```math
t_0=|q-s_1|=\frac{s_2}{2}<R.
```

Thus every `(2,3)` component exports one lower-scale witness.

# Type `(3,2)`

Orient the path as

```math
s_1-t_1-s_2-t_2-s_3.
```

The middle side source is completely absorbed and the two endpoints are partial.  Put

```math
s_1=x.
```

There are eight coefficient words.

## Words `111` and `112`

Both begin with

```math
s_2=q-\frac{x}{2}.
```

The second shared witness is

```math
t_2=|q-s_2|=\frac{x}{2}<R.
```

## Word `121`

The source equations give

```math
s_2=2q-x,
\qquad
s_3=x-q.
```

Hence

```math
q=s_2+s_3.
```

The second shared witness is

```math
t_2=|q-2s_2|
=|s_3-s_2|
<R.
```

## Word `122`

Here

```math
s_3=2(x-q).
```

Therefore the first shared witness is

```math
t_1=|q-x|
=\frac{s_3}{2}
<R.
```

## Word `211`

Here

```math
s_2=q-x,
\qquad q=s_1+s_2.
```

Thus

```math
t_1=|q-2s_1|
=|s_2-s_1|
<R.
```

## Word `212`

The equations give

```math
s_3=q+x.
```

Since `q=x+s_2`,

```math
s_3=2s_1+s_2\ge3R,
```

contradicting `s_3<2R`.  This word is impossible.

## Word `221`

The equations give

```math
s_2=2q-2x,
\qquad
s_3=2x-q.
```

Since

```math
q=s_1+\frac{s_2}{2},
```

we have

```math
s_3=s_1-\frac{s_2}{2}.
```

The second shared witness is

```math
t_2=|q-2s_2|
=\left|s_1-\frac{3s_2}{2}\right|
=|s_3-s_2|
<R.
```

## Word `222`

Here

```math
s_3=4x-2q.
```

Therefore

```math
t_1=|q-2x|
=\frac{s_3}{2}
<R.
```

Thus every `(3,2)` component exports one lower-scale witness.

# Type `(3,3)`

This is the component treated by the three-by-three scale-export theorem.

The coordinated shell and valuation constraints leave only coefficient words

```math
211
\qquad\text{and}\qquad
221.
```

For `211`, one witness is

```math
|s_2-s_1|<R.
```

For `221`, one witness is

```math
|s_3-s_2|<R.
```

Thus every `(3,3)` component exports one lower-scale witness.

# Type `(4,3)`

This is the only seven-vertex component type.  Orient it as

```math
s_1-t_1-s_2-t_2-s_3-t_3-s_4.
```

The two internal sources `s_2,s_3` are completely absorbed.  We prove that every possible component exports two distinct lower-scale witnesses.

There are sixteen coefficient words.

## Four words force a nonpositive final source

Direct substitution gives:

```math
1121:
\quad s_4=-\frac12s_1,
```

```math
1122:
\quad s_4=-s_1,
```

```math
2121:
\quad s_4=-s_1,
```

```math
2122:
\quad s_4=-2s_1.
```

These words are impossible.

## Six words leave the dyadic shell

### Word `1112`

The formulas imply

```math
s_4=\frac{s_1+3s_2}{2}\ge2R.
```

### Words `1211` and `1212`

One obtains

```math
s_1=s_2+2s_3\ge3R.
```

### Words `1221` and `1222`

One obtains

```math
s_1=s_2+s_3\ge2R.
```

### Word `2112`

One obtains

```math
s_4=s_1+\frac{3s_2}{2}>2R.
```

### Word `2212`

One obtains

```math
s_4=s_3+2s_2\ge3R.
```

Thus all six words are impossible.

## Word `2211` violates the coordinated side color

Write

```math
s_1=u,
\qquad
a=q-u>0.
```

Then

```math
s_2=2a,
\qquad
s_3=u-a,
\qquad
s_4=\frac{u+3a}{2}.
```

Put

```math
\alpha=v_2(u),
\qquad
\beta=v_2(a).
```

Since `s_2=2a` has the same side color as `u`,

```math
\beta+1\equiv\alpha\pmod2.
```

Hence `alpha` and `beta` have opposite parity.

If `beta<alpha`, then

```math
v_2(s_3)
=v_2(u-a)
=\beta,
```

which has the wrong parity.  Therefore `alpha<beta`.

But then

```math
v_2(u+3a)=\alpha,
```

so

```math
v_2(s_4)=\alpha-1,
```

again the wrong parity.  Contradiction.

Thus `2211` is impossible.

## Word `1111` exports two witnesses

The shared witnesses include

```math
t_2=\frac{s_1}{2}<R
```

and

```math
t_3=\frac{s_2}{2}<R.
```

They are distinct right vertices of the component.

## Word `2111` exports two witnesses

Here

```math
q=s_1+s_2.
```

The first and third shared witnesses are

```math
t_1=|s_2-s_1|<R
```

and

```math
t_3=\frac{s_2}{2}<R.
```

## Word `2221` exports two witnesses

Write

```math
s_1=a+b,
\qquad
s_2=2a,
\qquad
s_3=2b,
\qquad
s_4=2a-b.
```

Then

```math
t_1=b=\frac{s_3}{2}<R
```

and

```math
t_3=|s_4-s_3|<R.
```

## Word `2222` exports two witnesses

With the same first three source parametrization, the fourth source is

```math
s_4=2(2a-b).
```

The shared witnesses include

```math
t_1=\frac{s_3}{2}<R
```

and

```math
t_2=\frac{s_4}{2}<R.
```

Thus every possible `(4,3)` component exports two distinct lower-scale witnesses.

# Componentwise export theorem

Combining all cases:

```math
\boxed{
\#\bigl(V_R(K)\cap[1,R)\bigr)
\ge
\max\left\{0,\left\lceil\frac{|V(K)|}{3}\right\rceil-1\right\},
}
```

where `V_R(K)` denotes the right-vertex set of the component.

Explicitly:

```math
\begin{array}{c|c|c}
(l,r)&|V(K)|&\text{lower-scale witnesses}\\
\hline
(2,2)&4&\ge1\\
(2,3),(3,2)&5&\ge1\\
(3,3)&6&\ge1\\
(4,3)&7&\ge2.
\end{array}
```

Different components have disjoint right-vertex sets, so all exported witnesses are globally distinct.

# Scale-compensated eight-thirds inequality

Assume

```math
|S|=|T|=m.
```

Let `c(G)` be the number of components, including isolated vertices.  The full intersection graph is a forest on `2m` vertices, so

```math
|A(S)\cup M_q(T)|
=
2+2m+c(G)-\eta,
```

where `0<=eta<=2` counts anchor coincidences.

For every component `K`, let

```math
\kappa(K)
=
\max\left\{0,\left\lceil\frac{|V(K)|}{3}\right\rceil-1\right\}.
```

Then

```math
1+\kappa(K)
\ge
\frac{|V(K)|}{3}.
```

Summing over components gives

```math
c(G)+\sum_K\kappa(K)
\ge
\frac{2m}{3}.
```

The componentwise export theorem and disjointness of components imply

```math
\sum_K\kappa(K)
\le
|T\cap[1,R)|.
```

Therefore

```math
\boxed{
|A(S)\cup M_q(T)|
+
|T\cap[1,R)|
\ge
2+\frac83m-\eta.
}
```

Since every exported witness `t<R` satisfies `R/t>1`,

```math
|T\cap[1,R)|
\le
R H(T\cap[1,R)).
```

Hence the harmonic form is

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+\frac83m-\eta.
}
```

This is the desired one-generation scale-compensated packing theorem for equal side and middle shell cardinalities.

## Interpretation

The finite counterexample with local ratio near `7/3` is now fully explained.  Its `(3,3)` components save one parent point relative to the `8/3` target, but each component necessarily contributes one distinct witness below the side shell.  The lower-scale harmonic term restores exactly the missing potential.

The only seven-vertex path would need two credits; the coefficient classification proves that it indeed exports two lower-scale witnesses whenever it exists.

Thus no local intersection pattern can destroy the `8/3` potential.  It can only transfer part of that potential to a smaller scale.

## Next task

Extend the theorem from equal shell cardinalities to unequal harmonic masses.

The natural target is a homogeneous inequality in

```math
H(S)
```

and

```math
H(T),
```

obtained by splitting the larger shell into matched and unmatched portions.  The matched portion is controlled by the theorem above; the unmatched portion should be charged by its individual binary lift size.

A successful weighted version would provide the local transition inequality needed for a telescoping multiscale potential over the coordinated harmonic recursion.