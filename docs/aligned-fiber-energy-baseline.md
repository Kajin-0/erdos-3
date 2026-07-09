# Aligned fiber energy baseline

## Status

Labelled-fiber audit.  This note tests the next step after graph-DRC extraction from the dense direction graph.

The conclusion is another constraint: labelled fibers always have some translated overlap by averaging.  What is useful is not mere overlap, but concentration of overlap on few shifts or structured shifts.  High `J`-energy alone gives large fibers, but does not automatically give shift concentration.

## Edge fibers

For an edge `(d,e)` of the dyadic direction graph, define

```math
X_{d,e}=P_d\cap(P_e-2e)
=\{x:x,x+d,x+2e,x+3e\in A\}.
```

On the dyadic graph, assume

```math
|X_{d,e}|\sim \tau
```

for every edge.

If `e` is a common neighbor of `d_1` and `d_2`, then the two relevant fibers are

```math
X=X_{d_1,e},
\qquad
Y=X_{d_2,e}.
```

A translated overlap at shift `h` is

```math
r_{X,Y}(h)=|X\cap(Y-h)|
=|\{x:x\in X,\ x+h\in Y\}|.
```

## Automatic first-moment identity

For any two finite sets `X,Y subset G`,

```math
\sum_{h\in G} r_{X,Y}(h)=|X||Y|.
```

Thus for dyadic fibers with `|X|,|Y|\sim\tau`,

```math
\sum_h r_{X,Y}(h)\sim \tau^2.
```

This identity is automatic.  It does not use 4AP-freeness, direction structure, or graph density.

Consequently, the existence of many shifted overlaps is not a meaningful structural conclusion by itself.

## Baseline second moment

Define the pair-alignment energy

```math
E(X,Y)=\sum_h r_{X,Y}(h)^2.
```

By Cauchy--Schwarz,

```math
E(X,Y)\ge \frac{|X|^2|Y|^2}{N}.
```

For dyadic fibers this gives the random baseline

```math
E(X,Y)\gtrsim \frac{\tau^4}{N}.
```

This lower bound is also automatic.  It is the energy expected when the differences `X-Y` are spread nearly uniformly across `G`.

## Useful alignment means excess over baseline

The meaningful parameter is

```math
\kappa_{X,Y}
=\frac{N E(X,Y)}{|X|^2|Y|^2}.
```

Always

```math
\kappa_{X,Y}\ge1.
```

The branch `kappa_{X,Y}=O(1)` means translated overlaps are diffuse.  The branch `kappa_{X,Y}>>1` means many pairs of points in `X` and `Y` have repeated differences, so `X` and `Y` have correlated additive structure.

Thus aligned fiber energy must be measured as excess energy, not raw overlap.

## Common-neighbor aligned energy

For a dyadic graph `G`, define

```math
\mathcal E_{\mathrm{align}}
=
\sum_{e}\sum_{d_1,d_2\in N^-(e)}
\sum_h |X_{d_1,e}\cap(X_{d_2,e}-h)|^2.
```

The automatic baseline is approximately

```math
\sum_{e}\sum_{d_1,d_2\in N^-(e)}\frac{|X_{d_1,e}|^2|X_{d_2,e}|^2}{N}.
```

On a dyadic graph with `|X_{d,e}|\sim\tau`, this is

```math
\frac{\tau^4}{N}
\sum_e \deg^-(e)^2.
```

Graph DRC already gives

```math
\sum_e\deg^-(e)^2\ge \delta^2K^3,
```

so the trivial aligned-energy baseline is at least

```math
\mathcal E_{\mathrm{align}}
\gtrsim
\frac{\tau^4}{N}\delta^2K^3.
```

This is not yet structure.  It is the baseline forced by counting.

## Excess aligned energy branch

If

```math
\mathcal E_{\mathrm{align}}
\gg
\frac{\tau^4}{N}\sum_e\deg^-(e)^2,
```

then many common-neighbor fiber pairs have large additive energy.  For such pairs, Balog--Szemeredi--Gowers may produce large subsets

```math
X'\subseteq X_{d_1,e},
\qquad
Y'\subseteq X_{d_2,e}
```

with small difference set

```math
X'-Y'.
```

Since both `X'` and `Y'` are subsets of shifted 4-point shadows inside `A`, this is a plausible density-increment or structured-neighborhood branch.

This is the first genuinely useful labelled-fiber outcome.

## Diffuse aligned energy branch

If

```math
\mathcal E_{\mathrm{align}}
\lesssim
\frac{\tau^4}{N}\sum_e\deg^-(e)^2,
```

then common-neighbor fibers overlap like random sets after translation.  In this branch, graph DRC does not supply additive structure: the basepoint labels are incoherent.

Thus the route stalls unless a further sifting step creates aligned labels or a larger depleted relation.

## Why high J-energy alone is insufficient

High `J`-energy produced the dyadic graph and large fibers `X_{d,e}`.  But once the graph and fiber sizes are fixed, the translated-overlap baseline follows automatically for arbitrary fibers of those sizes.

Therefore the implication

```math
\text{high }J\text{-energy}
\Rightarrow
\text{useful labelled alignment}
```

is false without an excess-alignment hypothesis.

The correct implication is conditional:

```math
\text{high }J\text{-energy}
+
\text{excess aligned fiber energy}
\Rightarrow
\text{additive/fiber structure candidate}.
```

## Physical interpretation of excess alignment

If `X_{d_1,e}` and `X_{d_2,e}` have excess alignment at a shift `h`, then many `x` satisfy simultaneously

```math
x,x+d_1,x+2e,x+3e\in A
```

and

```math
x+h,x+h+d_2,x+h+2e,x+h+3e\in A.
```

This is an eight-point configuration consisting of two aligned skew 4-point shadows sharing the same `e` and shift `h`.

Repeated occurrence of the same or structured shifts `h` can expose repeated differences involving

```math
d_1-d_2.
```

That is the possible bridge from labelled fiber alignment to additive direction structure.

## Updated Branch-1 conclusion

The high-`J` branch now splits into:

1. **excess aligned energy:** use BSG/DRC on the physical fibers to get structured basepoints or direction differences;
2. **diffuse labels:** graph concentration is abstract only and does not yield additive structure;
3. **need new sifting:** create a subsystem where many fiber pairs have excess alignment or where many shifted interactions are depleted.

## Immediate next task

Formulate the excess-alignment lemma:

> If many dyadic edge fibers have excess translated energy, then either `A` has a density increment on a structured pair-neighborhood, or the direction set has additive structure.

The proof will likely require BSG on the aligned fibers plus a transfer step from structured fibers back to either `A` or `D`.
