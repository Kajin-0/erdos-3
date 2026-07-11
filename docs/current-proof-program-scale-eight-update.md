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

## Change to the active bottleneck

The density-sensitive theorem must now be compatible with the lower benchmark

```math
\alpha(P)\asymp P^{\log_2 3-3}
```

and

```math
P\alpha(P)\asymp P^{\log_2 3-2}.
```

Since

```math
\log_2 3-2<0,
```

the known efficient replication family still has decaying multiplicity-weighted density.

The most plausible closing target is consequently an upper theorem of the form

```math
P\alpha(P)\le \Psi(P),
\qquad
\Psi(P)\to0,
```

or an aggregate multiscale charging theorem with the same consequence. Any proposed exponent must allow the scale-eight family.

## Research priority

The next work should distinguish between:

1. a universal power-law decay for multiplicity-weighted density;
2. a weaker summable envelope across dyadic scales;
3. structural classification of replication mechanisms that approach the scale-eight benchmark.

The old `O(20^h)` ambient-scale estimate is superseded for lower-benchmark purposes by the exact scale law `L_h=8^{h+1}`.
