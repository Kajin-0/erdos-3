# Certainty-ledger update: scale-eight aligned diamonds

## CL-next: Scale-eight identical-history persistence

**Status:** computer-assisted exact construction.

**Certainty:** high for the finite-state certificate; medium-high for the full mathematical interpretation pending independent review.

**Audit state:** awaiting independent expert review and integration into `docs/certainty-ledger.md`.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h)
```

with

```math
\boxed{L_h=8^{h+1}},
```

```math
\boxed{|S_h|=\frac{9\cdot3^h-3}{2}},
```

and

```math
\boxed{
\text{identical-complete-anchor-history persistence}=2^h
=\frac12L_h^{1/3}.
}
```

The construction alternates the separations

```math
R_h
=
\begin{cases}
22\cdot8^h,&h\text{ odd},\\
17\cdot8^h,&h\text{ even},
\end{cases}
```

so `v_2(R_h)` is even at every level and the coordinated deleted side anchor is always the left endpoint.

The union of the states is recognized by a 34-state least-significant-digit-first base-eight DFA. The exact four-term-progression product/carry search explores 17,238 reachable states and reaches no accepting nontrivial progression state.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Primary note:** `docs/scale-eight-self-replicating-aligned-diamond.md`.

**Certificate signature:**

```text
e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

**Consequence:** the previous ambient-scale lower benchmark `L_h=O(20^h)` is superseded by exact scale growth `L_{h+1}=8L_h`. Any universal ambient-scale persistence bound must allow order `L^(1/3)`.

**Density benchmark:** with `P=2^h`,

```math
\alpha(P)\asymp P^{\log_2 3-3},
\qquad
P\alpha(P)\asymp P^{\log_2 3-2}.
```

The exponent `log_2 3-2` is negative, so the construction remains compatible with a theorem forcing decay of multiplicity-weighted density.
