# Role-compressed harmonic branching

## Status

Exact refinement of the harmonic star recursion.

The previous star identity first applied primitive extraction in every predecessor row and then reorganized the retained incidences by block point and role.  That row compression loses a factor `3` before the star recursion even begins.

It is unnecessary.

Starting from **all** three-term progressions in a 4-AP-free dyadic block, the first-point and last-point star children have only a doubling-chain obstruction, while middle-point star children have only a `3/2`-chain obstruction.  Compressing these role-specific chains preserves respectively one half, one third, and one half of the harmonic step mass.

Since every three-term progression contributes once to each role, the total retained child mass is at least

```math
\frac12+\frac13+\frac12=\frac43
```

times the full weighted three-AP load.  The weighted three-AP load is at least twice the parent block density.

Hence the total retained harmonic mass of the smaller 4-AP-free children is at least

```math
\boxed{\frac83}
```

times the parent block harmonic mass, up to the summable Roth error.

This is the strongest exact scale-descending harmonic branching factor obtained so far.

## Dyadic block and full weighted three-AP load

Let

```math
B=A\cap[N,2N),
\qquad
|B|=\alpha N,
```

where `A` contains no nontrivial four-term arithmetic progression.

For every nontrivial three-term progression

```math
p+s,
\qquad
p+2s,
\qquad
p+3s
```

inside `B`, retain the incidence `(p,s)` without any preliminary row compression.

Define the full step-weighted load

```math
\mathcal L(B)
=
\sum_{p,s:\ p+s,p+2s,p+3s\in B}
\frac1s.
```

Every such step satisfies `s<=N/2`, hence `1/s>=2/N`.  The deletion bound gives

```math
T_3(B)\ge |B|-r_3(N).
```

Therefore

```math
\boxed{
\mathcal L(B)
\ge
2\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

## Uncompressed role-star sets

For `x in B`, define

```math
U_1(x)
=
\{s:x,x+s,x+2s\in B\},
```

```math
U_2(x)
=
\{s:x-s,x,x+s\in B\},
```

and

```math
U_3(x)
=
\{s:x-2s,x-s,x\in B\}.
```

These are exactly the step sets of three-term progressions in which `x` is respectively the first, middle, or last point.

Each weighted progression contributes once to each role, so

```math
\boxed{
\sum_{x\in B}H(U_i(x))
=
\mathcal L(B)
\qquad(i=1,2,3),
}
```

where

```math
H(S)=\sum_{s\in S}\frac1s.
```

Hence the total uncompressed star mass is

```math
\sum_x\sum_{i=1}^3H(U_i(x))
=3\mathcal L(B).
```

## Every role-star set is 4-AP-free

Fix `x` and `i`.  Suppose

```math
s,s+r,s+2r,s+3r\in U_i(x)
```

with `r ne 0`.

Choose a different role branch `k ne i`.  The corresponding points

```math
x+(k-i)s,
```

```math
x+(k-i)(s+r),
```

```math
x+(k-i)(s+2r),
```

```math
x+(k-i)(s+3r)
```

all lie in `B` and form a nontrivial four-term progression.

Thus

```math
\boxed{U_i(x)\text{ is 4-AP-free}.}
```

The stronger role-specific ratio exclusions below are what make improved compression possible.

# Side roles: first and last points

## Ratio exclusions for `U_1(x)`

Let

```math
T=U_1(x).
```

Then

```math
\boxed{T\cap3T=\varnothing}
```

and

```math
\boxed{2T\cap3T=\varnothing.}
```

### Proof of `T cap 3T = emptyset`

If `s,3s in T`, then `B` contains

```math
x,x+s,x+2s
```

and

```math
x,x+3s,x+6s.
```

The four points

```math
x,x+s,x+2s,x+3s
```

form a 4-AP.

### Proof of `2T cap 3T = emptyset`

Suppose

```math
2a=3b
```

with `a,b in T`.  Write

```math
a=3u,
\qquad
b=2u.
```

The step `2u` progression supplies

```math
x,x+2u,x+4u,
```

and the step `3u` progression supplies `x+6u`.  Hence

```math
x,x+2u,x+4u,x+6u
```

is a 4-AP.

Thus the only possible overlap among

```math
T,2T,3T
```

is between `T` and `2T`.

## Doubling-chain compression

Inside `T`, connect

```math
t\longrightarrow2t
```

whenever `2t in T`.

The components are increasing doubling chains.  Let

```math
V_1(x)\subseteq U_1(x)
```

be their initial vertices.

The reciprocal mass of a doubling chain starting at `t_0` is at most

```math
\frac1{t_0}\sum_{j\ge0}2^{-j}
=
\frac2{t_0}.
```

Therefore

```math
\boxed{
H(V_1(x))
\ge
\frac12H(U_1(x)).
}
```

By construction,

```math
V_1(x)\cap2V_1(x)=\varnothing.
```

The inherited exclusions give

```math
V_1(x)\cap3V_1(x)=\varnothing
```

and

```math
2V_1(x)\cap3V_1(x)=\varnothing.
```

Hence

```math
\boxed{
V_1(x),2V_1(x),3V_1(x)
\text{ are pairwise disjoint}.}
```

## Last-point role

The same argument, reflected about `x`, applies to

```math
U_3(x)=\{s:x-2s,x-s,x\in B\}.
```

There is a subset

```math
V_3(x)\subseteq U_3(x)
```

such that

```math
\boxed{
H(V_3(x))
\ge
\frac12H(U_3(x))
}
```

and

```math
\boxed{
V_3(x),2V_3(x),3V_3(x)
\text{ are pairwise disjoint}.}
```

# Middle role

## Ratio exclusions for `U_2(x)`

Let

```math
T=U_2(x).
```

Then

```math
\boxed{T\cap2T=\varnothing}
```

and

```math
\boxed{T\cap3T=\varnothing.}
```

### Proof of `T cap 2T = emptyset`

If `s,2s in T`, then `B` contains

```math
x-s,x,x+s
```

and

```math
x-2s,x,x+2s.
```

The four points

```math
x-2s,x-s,x,x+s
```

form a 4-AP.

### Proof of `T cap 3T = emptyset`

If `s,3s in T`, then `B` contains `x-s,x+s` and `x-3s,x+3s`.  The sequence

```math
x-3s,x-s,x+s,x+3s
```

is a 4-AP of common difference `2s`.

Thus the only possible overlap among

```math
T,2T,3T
```

is between `2T` and `3T`.

## `3/2`-chain compression

Whenever

```math
3t\in2T,
```

define

```math
\phi(t)=\frac32t\in T.
```

This is an injective increasing map on its domain.  Its components are chains with ratio `3/2`.

Let

```math
V_2(x)\subseteq U_2(x)
```

be the initial vertices of these chains.

The reciprocal mass of a chain beginning at `t_0` is at most

```math
\frac1{t_0}
\sum_{j\ge0}\left(\frac23\right)^j
=
\frac3{t_0}.
```

Therefore

```math
\boxed{
H(V_2(x))
\ge
\frac13H(U_2(x)).
}
```

The initial-vertex property gives

```math
2V_2(x)\cap3V_2(x)=\varnothing.
```

Together with the inherited exclusions,

```math
\boxed{
V_2(x),2V_2(x),3V_2(x)
\text{ are pairwise disjoint}.}
```

# Total retained harmonic mass

Summing the three role-specific estimates over `x` gives

```math
\sum_xH(V_1(x))
\ge
\frac12\mathcal L(B),
```

```math
\sum_xH(V_2(x))
\ge
\frac13\mathcal L(B),
```

and

```math
\sum_xH(V_3(x))
\ge
\frac12\mathcal L(B).
```

Therefore

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(V_i(x))
\ge
\frac43\mathcal L(B).
}
```

Using the weighted three-AP lower bound,

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(V_i(x))
\ge
\frac83\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

Since

```math
H(B)\le\alpha,
```

we obtain the parent-child comparison

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(V_i(x))
\ge
\frac83H(B)
-
\frac83\frac{r_3(N)}N.
}
```

Thus the role-compressed child family has a supercritical harmonic branching factor `8/3`, up to the summable Roth error.

## Properties of every retained child

For every `x` and role `i`, the retained child

```math
V_i(x)\subseteq[1,N/2]
```

satisfies:

1. `V_i(x)` is 4-AP-free;
2. `V_i(x),2V_i(x),3V_i(x)` are pairwise disjoint;
3. its harmonic mass is retained with a role-dependent constant loss;
4. it lies at at most half the parent scale.

The union

```math
V_i(x)\cup2V_i(x)\cup3V_i(x)
```

need not itself be 4-AP-free.  The recursion uses 4-AP-freeness of the child set `V_i(x)`, while pairwise disjointness of its first three dilates supplies additional multiplicative rigidity.

## Iteration after dyadic resolution

Each child may occupy several dyadic shells below `N/2`.  Decompose

```math
V_i(x)
=
\bigcup_{k<j}
V_i(x)\cap[2^k,2^{k+1}),
\qquad N=2^j.
```

Harmonic mass adds exactly over these shells, and every shell remains 4-AP-free.

Therefore the role-compressed construction can be iterated scale by scale without losing mass beyond the explicit role-compression constants and the summable Roth errors.

Formally, persistent low-error recursion produces total depth-`h` harmonic mass on the order of

```math
\left(\frac83\right)^h
```

times the root mass, counted with multiplicity.

## Why this improves the previous star recursion

The earlier procedure was

```math
\text{all 3APs}
\longrightarrow
\text{row primitive extraction}
\longrightarrow
\text{star children}.
```

The row extraction retained only one third of the weighted load, after which the three roles restored a factor `3`, giving total branching factor approximately `2` relative to the parent harmonic mass.

The role-compressed procedure is

```math
\text{all 3APs}
\longrightarrow
\text{role stars}
\longrightarrow
\text{role-specific chain compression}.
```

Because the side roles lose only a factor `2`, the resulting factor improves from `2` to

```math
\boxed{8/3}.
```

## Remaining obstruction

The mass is still counted with multiplicity.  The depth-two finite-avoidance construction shows that large unweighted overlap is possible.

However, the recursive family now satisfies stronger hypotheses:

- total harmonic mass grows at rate `8/3` rather than `2`;
- every child is 4-AP-free;
- every child has pairwise-disjoint first three dilates;
- all branches descend in scale;
- Roth-error termination is summable.

The revised target is a weighted multiplicity upper bound with exponential rate strictly below `8/3`.

Any theorem of the form

```math
\text{total depth-}h\text{ multiplicity}
\le
(C+o(1))^h
```

with

```math
C<8/3
```

would close the mass-regular recursive branch.