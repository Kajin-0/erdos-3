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

---

## CL-next: Dyadic scale-eight barrier for exact three-translate replication

**Status:** proved by an elementary shell argument.

**Certainty:** high.

**Audit state:** awaiting independent review and integration into `docs/certainty-ledger.md`.

Consider an exact three-translate aligned-replication step

```math
S\subseteq[L,2L),
\qquad
A=\{0\}\cup S,
```

```math
G=A\cup(A+R)\cup(A+2R),
```

followed by

```math
S'=L'+G\subseteq[L',2L'),
```

where `L` and `L'` are powers of two. If exact uncontaminated backbone reproduction requires

```math
R\ge2L,
```

then `2R` belongs to `G`, while `G subseteq[0,L')`. Hence

```math
L'>2R\ge4L.
```

Since `L'/L` is a power of two,

```math
\boxed{L'\ge8L.}
```

After `h` exact replication generations,

```math
L_h\ge8^hL_0,
\qquad
P_h=2^h,
```

and therefore

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

The scale-eight construction attains the exponent `1/3`, so this exponent is optimal inside the exact standard-dyadic three-translate replication model.

**Primary note:** `docs/three-translate-dyadic-scale-barrier.md`.

**Consequence:** the open possibility of reducing the dyadic scale factor below `8` is closed for this exact model. Any stronger persistence construction must use overlapping layers, cross-parent interaction, nonuniform branching, multishell reproduction, or another mechanism outside the theorem's hypotheses.

**Caveat:** this is not a universal `L^(1/3)` upper bound for arbitrary aligned-diamond persistence in the full recursive proof program.
