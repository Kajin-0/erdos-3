# Sharp weighted-density decay in the exact three-translate model

## Status

Elementary theorem obtained by combining the exact cardinality recurrence with the dyadic scale-eight barrier.

This proves the desired multiplicity-weighted density decay for the canonical exact three-translate aligned-diamond mechanism. It does not yet prove the corresponding statement for arbitrary persistence events in the full recursive program.

---

## 1. Model

Let

```math
S_j\subseteq[L_j,2L_j)
```

be a sequence of nonempty states in standard dyadic shells. Put

```math
A_j=\{0\}\cup S_j.
```

At every generation choose `R_j` and form three disjoint translates

```math
G_{j+1}
=
A_j
\cup
(A_j+R_j)
\cup
(A_j+2R_j).
```

Translate this raw state into the next standard dyadic shell:

```math
S_{j+1}=L_{j+1}+G_{j+1}
\subseteq
[L_{j+1},2L_{j+1}).
```

Assume:

1. exact uncontaminated backbone reproduction, so `R_j>=2L_j`;
2. the three translate layers are disjoint;
3. the aligned middle/backbone mechanism doubles identical-history persistence at every generation.

Write

```math
n_j=|S_j|,
\qquad
\alpha_j=\frac{n_j}{L_j},
\qquad
P_j=2^j.
```

---

## 2. Why three translate layers are maximal

More generally, suppose an equal-translate construction contains

```math
A,
A+R,
\ldots,
A+(r-1)R
```

with `0 in A`. Then the raw state contains

```math
0,R,2R,\ldots,(r-1)R.
```

If `r>=4`, the first four of these points form a nontrivial four-term arithmetic progression. Therefore every four-term-progression-free equal-translate architecture satisfies

```math
\boxed{r\le3.}
```

The repository's occurrence genealogy is binary, so one parent creates at most two persistent outputs. The three-layer architecture realizes the maximal relevant pair

```math
(r,b)=(3,2),
```

where `r` is the number of disjoint translate layers and `b` is the number of identical persistent children. Thus the `3`-for-`2` law is the extremal equal-translate architecture compatible with four-term-progression-freeness and binary persistence.

---

## 3. Exact cardinality growth

Because the three translate layers are disjoint and

```math
|A_j|=n_j+1,
```

one has

```math
\boxed{
n_{j+1}=3(n_j+1).
}
```

Equivalently,

```math
n_{j+1}+\frac32
=
3\left(n_j+\frac32\right).
```

Iterating from generation zero gives

```math
\boxed{
n_j
=
3^j\left(n_0+\frac32\right)-\frac32.
}
```

In particular,

```math
n_j
\le
3^j\left(n_0+\frac32\right).
```

---

## 4. Scale growth

The dyadic scale barrier proves at every exact replication step that

```math
L_{j+1}\ge8L_j.
```

Therefore

```math
\boxed{
L_j\ge8^jL_0.
}
```

---

## 5. Density decay

Combining the cardinality and scale estimates,

```math
\alpha_j
=
\frac{n_j}{L_j}
\le
\frac{n_0+3/2}{L_0}
\left(\frac38\right)^j.
```

Thus

```math
\boxed{
\alpha_j
\le
C_0\left(\frac38\right)^j,
\qquad
C_0=\frac{n_0+3/2}{L_0}.
}
```

Since

```math
P_j=2^j,
```

this can be written as

```math
\boxed{
\alpha_j
\le
C_0P_j^{\log_2 3-3}.
}
```

---

## 6. Multiplicity-weighted density

Multiplying by `P_j=2^j`,

```math
P_j\alpha_j
\le
C_0\left(\frac34\right)^j.
```

Equivalently,

```math
\boxed{
P_j\alpha_j
\le
C_0P_j^{\log_2 3-2}.
}
```

Because

```math
\log_2 3-2
\approx
-0.4150374993,
```

one obtains the sharp power-law decay

```math
\boxed{
P_j\alpha_j
\ll
P_j^{-(2-\log_2 3)}.
}
```

Thus the exact model satisfies the desired weighted-density estimate with

```math
\epsilon
=
2-\log_2 3
\approx
0.4150374993.
```

At the one-step level, the extremal equal-translate efficiency ratio is

```math
\boxed{
\rho_{\mathrm{exact}}
=
\frac{b r}{c}
\le
\frac{2\cdot3}{8}
=
\frac34,
}
```

where `c=L_{j+1}/L_j`. This is the source of the geometric contraction.

---

## 7. Summability across replication depth

The geometric form gives more than pointwise decay:

```math
\sum_{j\ge0}P_j\alpha_j
\le
C_0\sum_{j\ge0}\left(\frac34\right)^j
=
4C_0.
```

Hence

```math
\boxed{
\sum_{j\ge0}P_j\alpha_j
\le
4\frac{n_0+3/2}{L_0}.
}
```

This is an exact-model aggregate charging theorem: one complete exact replication genealogy spends only a bounded total amount of multiplicity-weighted dyadic density.

---

## 8. Sharpness

The scale-eight family has equality in the scale recurrence

```math
L_{j+1}=8L_j
```

and in the cardinality recurrence

```math
n_{j+1}=3(n_j+1).
```

It therefore has

```math
\alpha_j
\asymp
P_j^{\log_2 3-3}
```

and

```math
P_j\alpha_j
\asymp
P_j^{\log_2 3-2}.
```

Consequently the exponents in the theorem are optimal inside the exact standard-dyadic equal-translate model.

---

## 9. Consequence for the full proof program

The canonical exact aligned-diamond obstruction is now quantitatively controlled:

1. four-term-progression-freeness permits at most three equal translate layers;
2. binary persistence permits at most two persistent children;
3. the dyadic shell jump is at least eight;
4. persistence is at most order `L^(1/3)`;
5. multiplicity-weighted density decays with the sharp exponent `2-log_2(3)`;
6. the weighted density is summable along one exact genealogy.

Therefore any remaining obstruction to the full proof must exploit behavior outside this exact model, such as:

- overlap between replication layers;
- branching factors or child counts that vary with depth;
- several parent states merging into one terminal history;
- approximate replication rather than exact state recurrence;
- persistence distributed across multiple dyadic shells;
- many interacting genealogies whose aggregate charges cannot be separated.

The next active theorem should attempt to decompose general persistence into exact or near-exact genealogies plus a quantitatively cheaper error class.
