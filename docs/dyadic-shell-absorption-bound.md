# Dyadic-shell absorption bound

## Status

Exact shell-local refinement of the monochromatic absorption-component theorem.

The global coordinated theorem shows that an absorption component contains at most three completely absorbed side sources.  Recursive harmonic arguments resolve every child into dyadic shells before continuing.  Inside one shell, a three-source component is impossible.

The main conclusion is:

```math
\boxed{
\text{Every coordinated absorption component restricted to }[R,2R)
\text{ contains at most two left sources.}
}
```

Consequently, `e` completely absorbed sources in one shell require at least

```math
\boxed{
|N(E)|
\ge
e+\left\lceil\frac e2\right\rceil
\ge\frac32e
}
```

distinct middle witnesses.

## Setup

Let `C` be a coordinated side child, let `q in C` be the paired base step, and let `T` be the selected middle child.  Assume:

```math
C,\quad2C,\quad3C
```

are pairwise disjoint;

```math
v_2(s)\pmod2
```

is constant on `C`; and

```math
\chi(t)=v_2(t)-v_3(t)\pmod3
```

is constant on `T`.

Let

```math
S=C\cap[R,2R)
```

be one dyadic shell.  Construct the complete-absorption graph using only sources in `S`.

The global component theorem already implies that every component is a path with at most three left vertices.  It remains to exclude a three-source path inside one shell.

## Coefficient word of a three-source path

Suppose a component contains three consecutive sources

```math
s_1,s_2,s_3.
```

As before, let

```math
r_i\in\{1,2\}
```

be the branch coefficient used by the edge leaving `s_i` to the right.  Then

```math
r_i s_i+(3-r_{i+1})s_{i+1}=2q
\qquad(i=1,2).
```

There are eight words

```math
r_1r_2r_3\in\{1,2\}^3.
```

Four are eliminated before shell geometry is used.

### Word `111`

The prefix-`111` 2-adic argument from the global component theorem applies.  The first two recurrences are

```math
s_2=q-\frac{s_1}{2},
\qquad
s_3=\frac q2+\frac{s_1}{4},
```

and the three sources cannot all have the parity color of `q`.

### Word `222`

The corresponding prefix-`222` argument applies to

```math
s_2=2(q-s_1),
\qquad
s_3=2(q-s_2).
```

Again one source necessarily has the opposite `v_2 mod 2` color.

### Word `211`

The four right witnesses satisfy

```math
|t_0|=2|t_3|.
```

This is incompatible with their common middle color because

```math
\chi(2t)=\chi(t)+1\pmod3.
```

### Word `221`

Likewise,

```math
|t_3|=2|t_0|,
```

so `221` is impossible.

Thus only

```math
112,
\qquad121,
\qquad122,
\qquad212
```

can survive the coordinated valuation constraints.

## The four surviving words span more than one dyadic shell

Each remaining word has an elementary additive relation among its three positive sources.

### Word `112`

The recurrences give

```math
s_1=x,
\qquad
s_2=q-\frac x2,
\qquad
s_3=q+\frac x2.
```

Hence

```math
\boxed{s_3=s_1+s_2.}
```

### Word `121`

Writing `x=q+y`, positivity gives

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=y.
```

Therefore

```math
\boxed{s_1=s_2+2s_3.}
```

### Word `122`

Writing `x=q+y`, the sources are

```math
s_1=q+y,
\qquad
s_2=q-y,
\qquad
s_3=2y.
```

Thus

```math
\boxed{s_1=s_2+s_3.}
```

### Word `212`

The sources are

```math
s_1=x,
\qquad
s_2=q-x,
\qquad
s_3=q+x,
```

and therefore

```math
\boxed{s_3=s_1+s_2.}
```

In every surviving case, one positive source is at least the sum of the other two.

If all three sources belonged to

```math
[R,2R),
```

then the two smaller sources would each be at least `R`, so the largest would be at least `2R`, outside the half-open shell.

This contradiction eliminates every three-source component inside one dyadic shell.

## Shell component theorem

```math
\boxed{
\text{Every coordinated complete-absorption component in }[R,2R)
\text{ has one or two left vertices.}
}
```

The value `2` is attainable.  For example, there are coordinated two-source components with both sources in one shell for each of the four coefficient words of length two.  One explicit realization is

```math
q=17,
\qquad
S=\{11,12\}\subseteq[8,16),
```

with witnesses

```math
5,6,7.
```

All side steps have the same `v_2 mod 2` color, all witnesses and the base step have the same `chi`-color, and the associated minimal parent set

```math
\{0,10,11,12,17,22,23,24,34\}
```

is 4-AP-free.

## Witness expansion in one shell

Let

```math
e=|E|
```

be the number of completely absorbed shell sources and let `c` be the number of nonempty absorption components.

The forest identity remains

```math
|N(E)|=e+c.
```

Since every component has at most two left vertices,

```math
c\ge\left\lceil\frac e2\right\rceil.
```

Therefore

```math
\boxed{
|N(E)|
\ge
e+\left\lceil\frac e2\right\rceil
\ge\frac32e.
}
```

Equivalently,

```math
\boxed{
e\le\frac23|N(E)|\le\frac23|T|.}
```

This is a scale-local constant-factor improvement over the global `4/3` witness expansion.

## Shell packing consequence

Let

```math
m=|S|,
\qquad
n=|T|,
```

and suppose `e` sources of `S` are completely absorbed by the middle lift.

The general unabsorbed-source estimate is

```math
|A(S)\cup M_q(T)|
\ge
1+m+2n-e.
```

Using

```math
e\le\frac23n,
```

we obtain

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
1+m+\frac43n.
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
m+\frac43n
\right\}.
}
```

For equal shell cardinalities,

```math
m=n,
```

this gives

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
1+\frac73m.
}
```

The target leading constant from harmonic branching is `8/3`, so the remaining local packing gap has decreased to exactly `1/3` copy of the shell.

## Structural meaning of the remaining gap

The shell theorem shows that high complete absorption cannot organize into long paths.  Every component is either:

1. an isolated absorbed source with two private witnesses; or
2. a two-source path with one shared witness and two endpoint witnesses.

The only way to remain below the target `8/3` packing rate is for many endpoint reflections to land on branch points belonging to partially absorbed sources, while unused middle steps simultaneously absorb the remaining side points.

This is now a finite local incidence problem involving only one- and two-source components.  No unbounded path or logarithmic endpoint charge remains.

## Immediate next task

Classify the possible endpoint-reflection collisions for the four two-source coefficient words

```math
11,
\qquad12,
\qquad21,
\qquad22.
```

The target strengthening is

```math
|A(S)\cup M_q(T)|
\ge
\frac83\min\{m,n\}
```

in the comparable-cardinality shell regime, or a dichotomy in which failure of this bound forces an additional structured family of partially absorbed sources that can be charged at the next recursive level.
