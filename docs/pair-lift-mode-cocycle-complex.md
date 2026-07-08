# Pair-lift mode cocycle complex

## Status

Extraction target.  This note removes the quotient-representative ambiguity in the sparse mode compatibility problem by lifting line modes to oriented spectral pairs.

The key idea is to replace

```math
(w,r)\quad\text{with}\quad (a,b),\qquad a+b=w.
```

Then the extracted line mode becomes an antisymmetric edge label on a graph of spectral frequencies.  In the isotropic quadratic model this edge label is a coboundary of a quadratic potential.  This gives a cleaner cocycle-stability target.

## Oriented pair graph

Let `Omega` be the active spectral cloud.  Define an oriented pair graph `Gamma` with vertex set contained in `Omega`.  An oriented edge is a pair

```math
a\to b
```

such that

```math
a,b\in\Omega,
\qquad
w=a+b\ne0,
```

and the line fiber associated to the sum `w` is active in the shear extraction.

For this edge, define

```math
H_{a,b}(t)=c_{a+tw}c_{b-tw},
\qquad w=a+b.
```

This is the same object as

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}
```

with `r=a` and `b=w-a`.

If fixed-line extraction gives a mode, write it as

```math
\mu(a,b)\in F_p.
```

Thus

```math
\mu(a,b)=m(a+b,a).
```

## Gauge removal

Changing the representative along the line sends

```math
(a,b)\mapsto(a+sw,b-sw).
```

The line function is translated:

```math
H_{a+sw,b-sw}(t)=H_{a,b}(t+s).
```

Therefore the frequency label is invariant along the shear orbit:

```math
\mu(a+sw,b-sw)=\mu(a,b).
```

This is the intrinsic version of representative-shift invariance.

## Reversal

Reversing the pair gives

```math
H_{b,a}(t)=H_{a,b}(-t).
```

Therefore the line mode reverses sign:

```math
\mu(b,a)=-\mu(a,b).
```

So `mu` is an antisymmetric edge label on the active pair graph, constant along shear orbits.

## Quadratic isotropic model

Suppose

```math
c_x\approx A(x)e_p(q(x))
```

where `q` is a homogeneous quadratic phase with associated quadratic form `Q_q` and polar form `B_q`.

For an edge `a -> b`, let

```math
w=a+b.
```

The phase of `H_{a,b}` is

```math
q(a+tw)+q(b-tw).
```

The coefficient of `t` is

```math
B_q(w,a-b)=2B_q(w,a)-B_q(w,w).
```

If the active directions are isotropic for `Q_q`, i.e.

```math
Q_q(w)=0,
```

then

```math
B_q(w,w)=2Q_q(w)=0,
```

and the line mode becomes

```math
\mu(a,b)=B_q(a+b,a-b).
```

Equivalently,

```math
\mu(a,b)=2Q_q(a)-2Q_q(b).
```

Thus, in the isotropic quadratic model, `mu` is a coboundary:

```math
\mu(a,b)=\Phi(a)-\Phi(b),
\qquad
\Phi(x)=2Q_q(x).
```

This automatically gives reversal and shear-orbit invariance when `Q_q(a+b)=0`.

## Cycle identities

Because the quadratic isotropic model gives a coboundary, every oriented cycle in the active pair graph must satisfy

```math
\sum_{i=1}^k \mu(x_i,x_{i+1})=0,
\qquad x_{k+1}=x_1.
```

In particular, every active triangle should satisfy

```math
\mu(a,b)+\mu(b,c)+\mu(c,a)=0.
```

And every active rectangle should satisfy

```math
\mu(a,b)+\mu(b,c)-\mu(a,d)-\mu(d,c)=0
```

whenever the orientations form a closed cycle.

These are gauge-free replacements for the quotient-coordinate rectangle identities.

## Sparse cocycle-stability target

The compatibility lemma can now be stated more cleanly:

> Let `Gamma` be a weighted active pair graph, and let `mu` be an antisymmetric edge label that is constant on shear orbits.  Suppose many weighted cycles in `Gamma` have zero `mu`-sum, and suppose failures of cycle closure do not already reveal low-rank concentration.  Then after graph cleaning, there is a large subgraph `Gamma'` and a potential `Phi` on its vertices such that
>
> ```math
> \mu(a,b)=\Phi(a)-\Phi(b)
> ```
>
> on most edges of `Gamma'`.

This is an ordinary sparse graph cocycle/coboundary stability problem once the pair lift is made.

## Additional quadraticity requirement

Recovering a potential `Phi` is not yet enough.  An arbitrary potential would only say the edge labels are globally consistent.  The quadratic model predicts more:

```math
\Phi(x)=2Q_q(x)
```

on a large structured subset.

Thus one needs a second step:

```math
\text{coboundary potential }\Phi
\Rightarrow
\text{quadratic or low-rank structure}.
```

A natural test is whether the second difference

```math
\Phi(x+h)+\Phi(x-h)-2\Phi(x)
```

is approximately bilinear/constant on many parallelograms in the active spectral cloud.  If so, `Phi` behaves quadratically on a large additive subset.  If not, the apparent line modes are not organized by a quadratic phase and must be treated as noise or as a different branch.

## Non-isotropic directions

The coboundary model is cleanest when

```math
Q_q(a+b)=0.
```

If the quadratic coefficient along the line is nonzero, then

```math
q(a+tw)+q(b-tw)
```

has a genuine `t^2` term.  On complete lines with flat amplitude, this tends to cancel in fixed-shift autocorrelation rather than produce a single line mode.

Therefore non-isotropic active directions require one of the following explanations:

1. support truncation blocks cancellation;
2. the relevant directions concentrate on an isotropic/low-rank set;
3. one must extract quadratic coefficients as well as affine modes, replacing `mu` by a richer edge label `(A(w),mu(a,b))`.

This is an important fork.  The current pair-lift cocycle complex handles the affine/isotropic line-mode branch.  A non-isotropic chirp branch will need a second-order label.

## Updated route

The phase-sensitive route now splits as follows:

```math
\text{large shear contribution}
\Rightarrow
\text{line-mode extraction}
\Rightarrow
\begin{cases}
\text{isotropic affine mode branch: pair-lift cocycle stability},\\
\text{non-isotropic chirp branch: extract quadratic line coefficients}.
\end{cases}
```

The isotropic branch target is now concrete:

```math
\mu(a,b)\text{ is an approximate coboundary of a quadratic potential.}
```

## Immediate proof task

Prove a graph-cleaning lemma for the pair-lifted active graph:

1. keep edges with stable extracted mode;
2. enforce reversal and shear-orbit invariance;
3. retain edges lying in many active cycles;
4. either obtain a large subgraph where `mu` is close to a coboundary, or show that failures concentrate on a low-rank/additive structure usable for a density increment.

This is the next precise combinatorial problem.
