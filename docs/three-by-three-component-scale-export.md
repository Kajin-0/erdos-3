# Three-by-three component scale export

## Status

Exact cross-scale theorem for the local configuration responsible for near-`7/3` side-middle packing.

The finite counterexample to a universal `8/3` one-edge packing theorem is built from absorption components having:

```math
3
```

side sources,

```math
3
```

middle witnesses, and

```math
5
```

intersection edges.

Such a component is locally efficient because two side sources are completely absorbed while the third is only partially absorbed.  The theorem below shows that this efficiency cannot remain within one dyadic scale:

```math
\boxed{
\text{every such component exports at least one middle witness below the side shell.}
}
```

Thus the missing local packing mass is transferred to a smaller scale rather than destroyed.

## Coordinated setup

Let

```math
S\subseteq[R,2R)
```

be a retained coordinated side shell.  Hence:

1. all elements of `S` have the same side color
   ```math
   \epsilon(s)=v_2(s)\pmod2;
   ```
2. the base step `q` has that same side color;
3. the first three dilates of the full side child are pairwise disjoint.

Let `T` be the selected coordinated middle child, so every element of `T` has the same color

```math
\chi(t)=v_2(t)-v_3(t)\pmod3.
```

Consider one connected component of the full side-middle intersection graph having three side sources

```math
s_1,s_2,s_3\in S
```

and three middle witnesses.  Such a component is a path with one endpoint on each side of the bipartition.  Two of its side sources have degree two and one has degree one.

Choose an orientation and encode the branch coefficient used to the right of `s_i` by

```math
r_i\in\{1,2\}.
```

At each shared witness,

```math
r_i s_i+(3-r_{i+1})s_{i+1}=2q
\qquad(i=1,2).
```

The coefficient word is

```math
r_1r_2r_3\in\{1,2\}^3.
```

## Six coefficient words are impossible

There are eight words.  Six cannot occur when all three sources lie in one dyadic shell and have the coordinated side color.

### Word `111`

The recurrences give

```math
s_2=q-\frac{s_1}{2},
\qquad
s_3=\frac q2+\frac{s_1}{4}.
```

Put

```math
a=v_2(q),
\qquad
b=v_2(s_1),
```

with `a congruent b mod 2`.

- If `b<=a`, then `s_1/2` has strictly smaller 2-adic valuation than `q`, so
  ```math
  v_2(s_2)=b-1,
  ```
  which has the wrong parity.
- If `b>a`, then `b>=a+2`.  Consequently
  ```math
  v_2(s_3)=a-1,
  ```
  again the wrong parity.

Thus `111` is impossible.

### Word `222`

Here

```math
s_2=2(q-s_1),
\qquad
s_3=2(q-s_2).
```

If `v_2(s_1) ne v_2(q)`, then the first subtraction is controlled by the term of lower valuation and `s_2` has the opposite parity color.

If the two valuations are equal, retaining the correct color for `s_2` forces

```math
v_2(s_2)\ge v_2(q)+2.
```

Then `q` controls `q-s_2`, so

```math
v_2(s_3)=v_2(q)+1,
```

again the opposite color.  Hence `222` is impossible.

### Word `112`

The sources are

```math
s_1=x,
\qquad
s_2=q-\frac x2,
\qquad
s_3=q+\frac x2.
```

Therefore

```math
s_3=s_1+s_2.
```

Since `s_1,s_2>=R`, this gives `s_3>=2R`, outside the half-open shell.

### Word `121`

The recurrences yield

```math
s_1=s_2+2s_3.
```

Thus `s_1>=3R`, impossible.

### Word `122`

One obtains

```math
s_1=s_2+s_3,
```

so again the largest source is at least `2R`.

### Word `212`

Here

```math
s_3=s_2+2s_1,
```

which is incompatible with all three sources lying below `2R`.

Therefore only

```math
\boxed{211\quad\text{and}\quad221}
```

can occur.

## Word `211` exports a lower-scale witness

For `211`, write

```math
s_1=x,
\qquad
s_2=q-x,
\qquad
s_3=\frac{q+x}{2}.
```

Since

```math
q=s_1+s_2,
```

the shared witness between `s_1` and `s_2` has magnitude

```math
|q-2s_1|
=
|s_2-s_1|.
```

Because

```math
s_1,s_2\in[R,2R),
```

we have

```math
\boxed{|s_2-s_1|<R.}
```

Thus every `211` component contains a middle witness below the side shell.

More explicitly:

- if the right-side endpoint is the partial source, the witnesses include
  ```math
  |s_2-s_1|;
  ```
- in the reflected endpoint orientation, the endpoint witness also includes
  ```math
  \frac{s_2}{2}<R.
  ```

Either orientation exports a lower-scale witness.

## Word `221` exports a lower-scale witness

For `221`, write

```math
s_1=x,
\qquad
s_2=2(q-x),
\qquad
s_3=2x-q.
```

Then

```math
s_1=s_3+\frac{s_2}{2}.
```

One shared witness has magnitude

```math
|q-2s_2|
=
|s_3-s_2|.
```

Since `s_2,s_3` lie in the same shell,

```math
\boxed{|s_3-s_2|<R.}
```

In the opposite endpoint orientation, the endpoint witness

```math
\frac{s_2}{2}
```

is also below `R`.  Therefore every `221` component exports a lower-scale witness as well.

## Scale-export theorem

Combining the classification:

```math
\boxed{
\begin{minipage}{0.82\linewidth}
Every coordinated side-middle intersection component with three side sources and three middle witnesses, whose side sources all lie in one shell $[R,2R)$, contains at least one middle witness $t<R$.
\end{minipage}
}
```

The witness is a vertex of that component.  Distinct connected components therefore export distinct lower-scale witnesses.

If `b` denotes the number of three-source/three-witness components, then

```math
\boxed{
b
\le
|T\cap[1,R)|.
}
```

## Harmonic charge

Every exported witness satisfies `t<R`, hence

```math
\frac{R}{t}>1.
```

Therefore

```math
\boxed{
b
\le
R\sum_{t\in T\cap[1,R)}\frac1t.}
```

This is the relevant form for the reciprocal-sum problem.

A three-source/three-witness component is exactly the local pattern that can lose approximately one parent point relative to the desired `8/3` packing rate.  The theorem shows that each such unit of local deficit carries at least one unit of the normalized lower-scale harmonic potential

```math
R H(T_{<R}).
```

## Interpretation of the explicit counterexample

In the explicit `q=4993` construction:

- each component has three side sources in `[2048,4096)`;
- two middle witnesses remain at that scale;
- the third witness is
  ```math
  |q-2x|<2048.
  ```

Thus the construction approaches the cardinality constant `7/3` only by exporting one third of its witness count to smaller scales.  It is not a same-scale harmonic counterexample to the coordinated recursion.

## Revised packing target

The correct target is not an uncorrected one-edge inequality with constant `8/3`.  It is a scale-compensated inequality of the schematic form

```math
\boxed{
\text{parent capacity}
+
R H(\text{exported lower-scale witnesses})
\ge
\frac83\times\text{side-shell mass}.
}
```

The three-by-three export theorem proves this compensation for the only currently known near-`7/3` component type.

The next task is to derive a full componentwise inequality for the entire side-middle intersection forest, showing that every deficit below the `8/3` same-scale target is charged to distinct lower-scale middle witnesses.  Such an inequality would fit directly into a telescoping multiscale potential.