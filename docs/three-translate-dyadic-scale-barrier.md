# Dyadic scale-eight barrier for exact three-translate replication

## Status

Elementary theorem. No computation is required.

This note proves that the scale-eight aligned-diamond construction is ambient-scale optimal inside the exact standard-dyadic equal-translate replication model used by the current recursion.

The theorem does **not** bound every possible aligned-diamond mechanism. It applies when one replication step is formed from exact equally spaced translates and is then placed into one standard dyadic shell.

---

## 1. Exact three-translate replication step

Let

```math
S\subseteq[L,2L)
```

be a nonempty state in a standard dyadic shell, where `L` is a power of two. Put

```math
A=\{0\}\cup S.
```

Choose an integer separation `R` and form

```math
G=A\cup(A+R)\cup(A+2R).
```

Assume:

1. the translate layers are separated from the original backbone shell, so
   ```math
   R\ge 2L;
   ```
2. the next state is obtained by translating `G` into a standard dyadic shell,
   ```math
   S'=L'+G\subseteq[L',2L'),
   ```
   where `L'` is also a power of two.

The first assumption ensures that the minimum-translation backbone shell `[L,2L)` contains the original copy `S` without contamination by the `R` or `2R` layers.

---

## 2. One-step scale barrier

### Theorem

Every exact three-translate replication step satisfying the assumptions above obeys

```math
\boxed{L'\ge 8L.}
```

### Proof

Because `0\in A`, the point `2R` belongs to `G`. Since

```math
S'=L'+G\subseteq[L',2L'),
```

we must have `G\subseteq[0,L')`, and therefore

```math
2R<L'.
```

The exact-backbone separation assumption gives `R\ge2L`, so

```math
L'>2R\ge4L.
```

Both `L` and `L'` are powers of two. Hence `L'/L` is a power of two. The smallest power of two strictly larger than `4` is `8`, proving

```math
L'\ge8L.
```

---

## 3. Multigeneration consequence

For an exact replication genealogy with scales `L_0,\ldots,L_h`, repeated application gives

```math
\boxed{L_h\ge8^hL_0.}
```

The exact aligned diamond doubles identical-history persistence at every step, so `P_h=2^h`. Therefore

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

For fixed initial scale, every exact standard-dyadic three-translate family satisfies `P_h=O(L_h^{1/3})`.

---

## 4. Equal-translate ceiling

The three-layer architecture is maximal among equal-translate four-term-progression-free constructions.

If a raw state contains

```math
A,A+R,\ldots,A+(r-1)R
```

with `0\in A` and `r\ge4`, then it contains

```math
0,R,2R,3R,
```

a nontrivial four-term arithmetic progression. Hence

```math
\boxed{r\le3.}
```

The occurrence genealogy is binary, so at most two persistent children can arise from one parent. Therefore

```math
3\text{ support layers}
\longrightarrow
2\text{ persistent children}
```

is the maximal exact equal-translate architecture compatible with four-term-progression-freeness.

Together with the scale barrier, the maximal one-step weighted-density efficiency is

```math
\boxed{
\rho_{\mathrm{exact}}
\le
\frac{2\cdot3}{8}
=
\frac34.
}
```

The companion note `docs/exact-three-translate-weighted-density-theorem.md` turns this into a sharp multigeneration decay and summability theorem.

---

## 5. Sharpness

The scale-eight construction has `L_{h+1}=8L_h` at every generation and `P_h=2^h`. Therefore

```math
P_h=\frac12L_h^{1/3}
```

under its normalization `L_1=64`. Consequently

```math
\boxed{
\text{the exponent }1/3\text{ is optimal in the exact standard-dyadic equal-translate model.}
}
```

A better ambient-scale exponent would require leaving at least one hypothesis:

1. exact equal-translate replication;
2. uncontaminated reproduction of the backbone shell;
3. one standard dyadic shell per replication generation;
4. exact binary persistence at each generation.

---

## 6. What remains open

This theorem does not establish a universal `L^(1/3)` upper bound for arbitrary persistence events. More general mechanisms may involve overlapping layers, cross-parent interaction, nonuniform branching, multishell reproduction, or approximate recurrence.

What is resolved is the sharp ambient-scale and one-step efficiency law for the canonical exact equal-translate obstruction.
