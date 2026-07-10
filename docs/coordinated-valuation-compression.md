# Coordinated valuation compression

## Status

Exact refinement of the role-compressed harmonic branching theorem.

The previous construction compressed the first-, middle-, and last-point star families independently.  That preserves the optimal lower bound obtained there, but it leaves avoidable multiplicity: the same three-term progression may survive in all three roles.

A global valuation coloring coordinates the compression across all block points:

1. a parity coloring of `v_2(s)` assigns every step to exactly one side role;
2. a three-coloring of `v_2(s)-v_3(s)` selects the middle role;
3. the total retained harmonic mass is still at least `4/3` of the full weighted three-AP load;
4. every three-term progression produces either one or two retained children, never three;
5. every retained child has pairwise-disjoint first three dilates.

Thus the harmonic branching lower bound `8/3` survives while the role multiplicity per progression is reduced to `2`.

## Dyadic setup

Let

```math
B=A\cap[N,2N),
\qquad
|B|=\alpha N,
```

where `A` is 4-AP-free.

For `x in B`, define the full role-star step sets

```math
U_1(x)=\{s:x,x+s,x+2s\in B\},
```

```math
U_2(x)=\{s:x-s,x,x+s\in B\},
```

and

```math
U_3(x)=\{s:x-2s,x-s,x\in B\}.
```

Let

```math
\mathcal L(B)
=
\sum_{p,s:\ p+s,p+2s,p+3s\in B}\frac1s
```

be the full weighted three-AP load.  Each progression contributes once to each role, so

```math
\sum_{x\in B}H(U_i(x))=\mathcal L(B)
\qquad(i=1,2,3),
```

where

```math
H(S)=\sum_{s\in S}\frac1s.
```

Also

```math
\boxed{
\mathcal L(B)
\ge
2\left(\alpha-\frac{r_3(N)}N\right).
}
```

## Global side-role coloring

Define the parity color

```math
\epsilon(s)=v_2(s)\pmod 2.
```

Set

```math
V_1(x)=\{s\in U_1(x):\epsilon(s)=0\},
```

and

```math
V_3(x)=\{s\in U_3(x):\epsilon(s)=1\}.
```

The assignments may be swapped; the stated choice is fixed for definiteness.

For every positive integer `s`, the values `epsilon(s)` and `epsilon(2s)` are opposite.  Hence

```math
V_1(x)\cap2V_1(x)=\varnothing,
```

and

```math
V_3(x)\cap2V_3(x)=\varnothing.
```

For a first-point star `U_1(x)`, 4-AP-freeness already gives

```math
U_1(x)\cap3U_1(x)=\varnothing
```

and

```math
2U_1(x)\cap3U_1(x)=\varnothing.
```

The same reflected statements hold for `U_3(x)`.  Therefore

```math
\boxed{
V_1(x),2V_1(x),3V_1(x)
\text{ are pairwise disjoint},
}
```

and

```math
\boxed{
V_3(x),2V_3(x),3V_3(x)
\text{ are pairwise disjoint}.
}
```

### Exact total side mass

For a fixed step `s`, let

```math
n_B(s)
=
|\{p:p+s,p+2s,p+3s\in B\}|.
```

The step `s` appears exactly `n_B(s)` times in the first role and exactly `n_B(s)` times in the last role.

If `epsilon(s)=0`, all its retained side occurrences are in the first role; if `epsilon(s)=1`, all are in the last role.  Hence every three-AP occurrence contributes to exactly one retained side child and

```math
\boxed{
\sum_xH(V_1(x))
+
\sum_xH(V_3(x))
=
\mathcal L(B).
}
```

There is no side-role loss after coordinating the two parity classes.

## Global middle-role coloring

Define

```math
\chi(s)=v_2(s)-v_3(s)\pmod 3.
```

For `c in Z/3Z`, put

```math
W_c
=
\sum_s\frac{n_B(s)}s\,1_{\chi(s)=c}.
```

Since

```math
W_0+W_1+W_2=\mathcal L(B),
```

choose a color `c_*` with

```math
W_{c_*}\ge\frac13\mathcal L(B).
```

Define

```math
V_2(x)=\{s\in U_2(x):\chi(s)=c_*\}.
```

For a middle-point star, 4-AP-freeness already gives

```math
U_2(x)\cap2U_2(x)=\varnothing
```

and

```math
U_2(x)\cap3U_2(x)=\varnothing.
```

It remains to exclude an overlap between `2V_2(x)` and `3V_2(x)`.

Suppose

```math
2a=3b
```

with `a,b in V_2(x)`.  Then

```math
v_2(b)=v_2(a)+1,
\qquad
v_3(b)=v_3(a)-1,
```

so

```math
\chi(b)-\chi(a)=2\pmod3.
```

Thus `a` and `b` cannot have the same `chi`-color.  Therefore

```math
2V_2(x)\cap3V_2(x)=\varnothing.
```

Consequently

```math
\boxed{
V_2(x),2V_2(x),3V_2(x)
\text{ are pairwise disjoint}.
}
```

The retained middle mass is

```math
\boxed{
\sum_xH(V_2(x))
=
W_{c_*}
\ge
\frac13\mathcal L(B).
}
```

## Coordinated branching theorem

Combining the side and middle contributions gives

```math
\sum_{x\in B}\sum_{i=1}^3H(V_i(x))
\ge
\left(1+\frac13\right)\mathcal L(B).
```

Therefore

```math
\boxed{
\sum_{x\in B}\sum_{i=1}^3H(V_i(x))
\ge
\frac43\mathcal L(B)
\ge
\frac83\left(\alpha-\frac{r_3(N)}N\right).
}
```

Since

```math
H(B)\le\alpha,
```

we also obtain

```math
\boxed{
\sum_{x\in B}\sum_{i=1}^3H(V_i(x))
\ge
\frac83H(B)
-
\frac83\frac{r_3(N)}N.
}
```

Thus the `8/3` harmonic branching factor survives the global coordination.

## At most two children per progression

Fix a three-term progression

```math
p+s,p+2s,p+3s\in B.
```

Exactly one side occurrence is retained:

- if `epsilon(s)=0`, the first-point child at `p+s` retains `s`;
- if `epsilon(s)=1`, the last-point child at `p+3s` retains `s`.

The middle-point child at `p+2s` retains `s` precisely when

```math
\chi(s)=c_*.
```

Hence every weighted three-AP incidence creates either one or two retained child memberships, never three.

Equivalently, for each step `s`, its retained child multiplicity is

```math
m_B(s)
=
n_B(s)\left(1+1_{\chi(s)=c_*}\right),
```

so

```math
\boxed{
n_B(s)\le m_B(s)\le2n_B(s).
}
```

Since fixed-step three-term progressions are pairwise disjoint in a 4-AP-free set,

```math
3n_B(s)\le|B|.
```

Therefore

```math
\boxed{
m_B(s)\le\frac{2|B|}{3}.}
```

The important point is structural rather than this crude cardinality bound: the factor `8/3` lower bound no longer comes from allowing three role copies of every progression.  The role multiplicity has been deterministically capped at `2`.

## Iteration

Each retained child

```math
V_i(x)\subseteq[1,N/2]
```

is 4-AP-free and has pairwise-disjoint first three dilates.  After dyadic resolution, the construction can be repeated on every child shell.

At every node:

1. the total retained child harmonic mass is at least `8/3` of the parent harmonic mass, up to the Roth error;
2. every parent three-AP produces at most two retained child incidences;
3. the side-role decision is determined globally by `v_2(s) mod 2`;
4. the middle-role decision is determined by one global `v_2-v_3 mod 3` color chosen for that node.

This replaces independent chain compression by a coordinated finite-state rule.

## Remaining obstruction

The per-progression role multiplicity is now bounded by `2`, which is strictly below the harmonic mass growth factor `8/3`.

However, a terminal step may participate in many different three-term progressions at successive nodes.  Therefore the statement

```math
\text{path multiplicity}\le2^h
```

does not follow merely from the two-role cap.

The revised target is sharper:

> Control the growth caused by the number of distinct fixed-step three-APs, after the role choice itself has been reduced to a binary decision.

A successful next theorem may take either form:

1. a weighted energy bound for the fixed-step multiplicities `n_B(s)` across the recursive tree;
2. a path encoding in which the sequence of underlying three-AP occurrences has subexponential redundancy;
3. a stopping-time inequality charging large `n_B(s)` to disjoint parent points and summable Roth-error termination.

The coordinated theorem isolates the remaining multiplicity entirely in the choice of the underlying three-term progression, rather than in the three role labels.