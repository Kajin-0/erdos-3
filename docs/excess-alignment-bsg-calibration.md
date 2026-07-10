# Excess alignment: BSG calibration

## Status

Quantitative proof audit.  This note calibrates the proposed passage

```math
\text{excess translated overlap of edge fibers}
\Longrightarrow
\text{Balog--Szemeredi--Gowers structure}.
```

The conclusion is restrictive: excess over the ambient random baseline is not by itself enough.  The relevant BSG parameter is the excess factor multiplied by the fiber density in the ambient group.

## Cross-energy of two fibers

Let `G` be a finite abelian group of size

```math
N=|G|,
```

and let

```math
X,Y\subseteq G,
\qquad
|X|\asymp |Y|\asymp \tau.
```

Define

```math
r_{X,Y}(h)=|X\cap(Y-h)|
```

and the cross-additive energy

```math
E(X,Y)=\sum_{h\in G}r_{X,Y}(h)^2.
```

Equivalently,

```math
E(X,Y)
=
|\{x_1,x_2\in X,\ y_1,y_2\in Y:
 x_1-y_1=x_2-y_2\}|.
```

The automatic ambient baseline is

```math
E(X,Y)\ge \frac{|X|^2|Y|^2}{N}
\asymp \frac{\tau^4}{N}.
```

Write the excess factor as

```math
\kappa
=
\frac{N E(X,Y)}{|X|^2|Y|^2}.
```

Thus

```math
E(X,Y)\asymp \kappa\frac{\tau^4}{N}.
```

## The BSG-normalized energy

The natural scale for a strong BSG conclusion is not `tau^4/N`; it is

```math
|X|^{3/2}|Y|^{3/2}\asymp \tau^3.
```

Define

```math
\eta
=
\frac{E(X,Y)}{|X|^{3/2}|Y|^{3/2}}.
```

For comparable fiber sizes,

```math
\eta
\asymp
\frac{\kappa\tau^4/N}{\tau^3}
=
\kappa\frac{\tau}{N}.
```

If

```math
\beta=\frac{\tau}{N}
```

is the ambient density of a fiber, then

```math
\boxed{\eta\asymp \kappa\beta.}
```

This is the correct conversion from ambient excess alignment to the BSG parameter.

## Consequence

A constant excess factor

```math
\kappa\asymp1
```

gives only

```math
\eta\asymp\beta,
```

which is very small when the edge fibers are sparse.

Even a visibly large excess

```math
\kappa\gg1
```

may still be quantitatively useless unless

```math
\kappa\beta
```

is large enough to survive the polynomial losses in BSG and the later density-increment iteration.

To obtain a constant-scale BSG input directly, one would need

```math
\kappa\gtrsim\beta^{-1}=\frac{N}{\tau}.
```

That is an enormous excess requirement for sparse fibers.

## Equivalent maximum-overlap calibration

Since

```math
\sum_h r_{X,Y}(h)=|X||Y|,
```

one has

```math
\max_h r_{X,Y}(h)
\ge
\frac{E(X,Y)}{|X||Y|}.
```

Using the excess parameter,

```math
\max_h r_{X,Y}(h)
\gtrsim
\kappa\frac{\tau^2}{N}
=
\kappa\beta\tau.
```

Thus the largest guaranteed aligned overlap occupies only a fraction

```math
\frac{\max_h r_{X,Y}(h)}{\tau}
\gtrsim
\kappa\beta
```

of either fiber.

The same parameter `kappa beta` appears again.  This confirms that the scaling obstruction is intrinsic, not an artifact of one formulation of BSG.

## Application to the pair-fiber graph

For edge fibers

```math
X_{d,e}
=
\{x:x,x+d,x+2e,x+3e\in A\},
```

suppose

```math
|X_{d,e}|\asymp\tau.
```

The previous aligned-energy branch compared the global average against

```math
\tau^4/N.
```

This calibration shows that the useful condition is stronger.  For many common-neighbor pairs, one needs

```math
E(X_{d_1,e},X_{d_2,e})
\ge
\eta\tau^3
```

with an `eta` that survives the intended iteration.

Equivalently, the ambient excess must satisfy

```math
\kappa\ge \eta\frac{N}{\tau}.
```

A statement merely asserting

```math
\kappa>1+c
```

is not enough.

## The localization escape

There is a more plausible way to improve the parameter.

Suppose sifting localizes the fibers inside a common ambient set

```math
V\subseteq G,
\qquad
|V|=M\ll N,
```

while retaining

```math
|X|,|Y|\asymp\tau.
```

The relevant local density becomes

```math
\beta_V=\frac{\tau}{M},
```

and the local random baseline becomes

```math
\frac{\tau^4}{M}.
```

If the translated differences are also effectively confined to a set of size `M`, then the BSG parameter is calibrated by

```math
\eta_V\asymp\kappa_V\beta_V.
```

Shrinking `M` can therefore turn weak global alignment into strong relative alignment.

This suggests that the purpose of sifting should be not merely to increase raw energy, but to produce a smaller common ambient neighborhood in which the fibers have appreciable relative density.

## Revised excess-alignment target

The earlier target

```math
\text{excess aligned energy}
\Rightarrow
\text{BSG structure}
```

should be replaced by the quantitatively correct target:

> Find many fiber pairs `X,Y` and a common ambient set `V` such that
>
> ```math
> X,Y\subseteq V,
> \qquad
> |X|,|Y|\ge\beta_V|V|,
> ```
>
> and
>
> ```math
> E_V(X,Y)\ge\eta |X|^{3/2}|Y|^{3/2},
> ```
>
> where `eta` and `beta_V` are large enough to survive BSG and the subsequent increment step.

Here `E_V` should count only the controlled difference/translation regime supplied by the localized model.

## Architectural correction

The high-`J` route is now:

```math
\text{high }J\text{-energy}
\Rightarrow
\text{dyadic direction graph}
\Rightarrow
\text{labelled fiber system}
\Rightarrow
\boxed{\text{localize to a smaller common ambient set}}
\Rightarrow
\text{relative fiber energy strong enough for BSG}
\Rightarrow
\text{structured neighborhood or increment}.
```

Global excess alignment without localization is generally too weak.

## Immediate next proof task

Construct a candidate localization operation from the existing load function.

A natural object is a popular pair-neighborhood

```math
V_x=\{x+d:d\in D,\ x+d\in A\},
```

or a common-neighbor refinement obtained by fixing a popular anchor, direction, or shift.

The task is to show that one can pass to a subsystem where:

1. the edge fibers remain large;
2. they lie in a common ambient set `V` much smaller than `G`;
3. the relative density `tau/|V|` increases by a power of `alpha`;
4. the number of surviving directions and configurations remains sufficient for iteration.

This localization step, rather than raw global BSG, is now the central quantitative target.
