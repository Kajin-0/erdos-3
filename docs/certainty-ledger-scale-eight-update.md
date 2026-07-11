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

## CL-next: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, cardinality, and shell arguments.

**Certainty:** high.

**Audit state:** awaiting independent review and integration into `docs/certainty-ledger.md`.

### Equal-translate ceiling

A four-term-progression-free equal-translate state contains at most three layers. Four layers would contain

```math
0,R,2R,3R.
```

The occurrence genealogy is binary, so one parent has at most two persistent children.

### Dyadic scale barrier

For an exact replication step

```math
G=A\cup(A+R)\cup(A+2R),
```

with uncontaminated backbone reproduction `R>=2L` and

```math
L'+G\subseteq[L',2L'),
```

one has `2R in G`, hence

```math
L'>2R\ge4L.
```

Because `L'/L` is a power of two,

```math
\boxed{L'\ge8L.}
```

Thus after `h` exact generations,

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

### Sharp weighted-density theorem

The maximal exact one-step efficiency is

```math
\boxed{
\rho_{\mathrm{exact}}
\le
\frac{2\cdot3}{8}
=
\frac34.
}
```

Writing

```math
n_h=|S_h|,
\qquad
\alpha_h=\frac{n_h}{L_h},
\qquad
P_h=2^h,
```

and

```math
C_0=\frac{n_0+3/2}{L_0},
```

one has

```math
\boxed{
\alpha_h\le C_0\left(\frac38\right)^h,
}
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
\le4C_0.
}
```

The scale-eight family attains the exponents `1/3` and `2-log_2(3)`. Therefore ambient persistence, density decay, and aggregate weighted-density charge are optimal inside the exact standard-dyadic equal-translate model.

**Primary notes:**

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

**Consequence:** the canonical exact obstruction is no longer the unresolved case. The remaining bottleneck consists of overlapping, approximate, cross-parent, nonuniform, multishell, or interacting genealogies.

**Caveat:** this does not yet control arbitrary persistence in the full recursive proof program.
