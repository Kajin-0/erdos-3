# Current proof program update: scale-eight persistence benchmark

## Status

This file records the project-level update produced by the scale-eight aligned-diamond construction. It is intended to be folded into `docs/current-proof-program.md` and `docs/certainty-ledger.md` after review.

## New certified benchmark

There are computer-certified four-term-progression-free blocks

```math
S_h\subseteq[L_h,2L_h)
```

with

```math
L_h=8^{h+1},
\qquad
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
\text{identical-history persistence}=2^h.
```

Therefore

```math
\boxed{
\text{persistence}=\frac12L_h^{1/3}.
}
```

The infinite family is certified by `src/verify_scale_eight_aligned_diamond.py` using a 34-state base-eight automaton and a 17,238-state product/carry search.

## Exact-model classification

The elementary notes

```text
docs/three-translate-dyadic-scale-barrier.md
docs/exact-three-translate-weighted-density-theorem.md
```

classify the canonical exact standard-dyadic equal-translate obstruction.

### Translate-layer ceiling

If an equal-translate raw state contains

```math
A,A+R,\ldots,A+(r-1)R
```

with `0 in A`, then `r>=4` immediately produces the four-term progression

```math
0,R,2R,3R.
```

Hence

```math
\boxed{r\le3.}
```

The occurrence genealogy is binary, so the maximal exact architecture has three support layers and two persistent children.

### Scale barrier

Every exact standard-dyadic three-translate replication step satisfies

```math
\boxed{L'\ge8L.}
```

Indeed, exact backbone reproduction requires `R>=2L`; because `2R` belongs to the raw state and the next raw state must fit below `L'`, one has `L'>2R>=4L`. Since `L'/L` is a power of two, `L'/L>=8`.

After `h` exact replication steps,

```math
L_h\ge8^hL_0,
\qquad
P_h=2^h,
```

so

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

The scale-eight family attains this exponent.

### Sharp weighted-density decay

The exact cardinality recurrence is

```math
n_{h+1}=3(n_h+1).
```

Consequently every exact genealogy satisfies

```math
\alpha_h
\le
C_0\left(\frac38\right)^h,
```

```math
\boxed{
P_h\alpha_h
\le
C_0\left(\frac34\right)^h
=
C_0P_h^{\log_2 3-2},
}
```

and

```math
\boxed{
\sum_{h\ge0}P_h\alpha_h
\le
4C_0,
\qquad
C_0=\frac{n_0+3/2}{L_0}.
}
```

The one-step exact efficiency ratio is

```math
\boxed{
\rho_{\mathrm{exact}}
=
\frac{
2\text{ persistent children}
\times
3\text{ support layers}
}{
8\text{ scale expansion}
}
=
\frac34.
}
```

The scale-eight family attains the exponents. Thus ambient persistence, density decay, and aggregate weighted-density charge are sharp inside the exact model.

This is not a universal upper bound for arbitrary persistence mechanisms in the full recursion.

## Change to the active bottleneck

The canonical exact obstruction is no longer the unresolved case. It already has a sharp geometric contraction factor `3/4`.

The remaining theorem must control behavior outside that model:

1. overlapping or partially resolved translate layers;
2. several parent states feeding one terminal history;
3. nonuniform branching or child counts;
4. approximate rather than exact state recurrence;
5. persistence distributed across several dyadic shells;
6. many genealogies whose aggregate charges cannot be separated.

The active target is now:

```math
\boxed{
\text{decompose general persistence into exact or near-exact genealogies plus a quantitatively cheaper error class.}
}
```

A useful theorem would define a rigorous local efficiency ratio `rho` for general recursive segments and prove a dichotomy:

1. `rho` close to `3/4` forces structural proximity to the exact equal-translate architecture;
2. otherwise `rho<=3/4-delta` for some uniform `delta>0`.

## Research priority

The next work should focus on:

1. defining a quantitative defect from exact `3`-for-`2`, scale-eight replication;
2. proving stability or rigidity when that defect is small;
3. proving stronger contraction when the defect is bounded away from zero;
4. controlling overlap among near-exact genealogy segments.

The old `O(20^h)` ambient-scale estimate is superseded by `L_h=8^{h+1}`. The possibility of a smaller dyadic factor is closed for exact equal-translate replication; any improvement must use a genuinely different mechanism.
