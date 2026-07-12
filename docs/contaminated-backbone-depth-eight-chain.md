# Contaminated-backbone depth-eight chain

## Status

Exact finite computer-assisted construction.

The depth-seven state from the alternative recovery branch has no factor-two or factor-four continuation. This note records the first valid exact factor-eight continuation and therefore extends the certified scale sequence to

```math
\boxed{4,8,4,4,8,4,8.}
```

The construction is finite. It does not prove indefinite continuation or solve the reciprocal-sum problem.

**Verifier:** `src/verify_contaminated_backbone_depth8.cpp`.

**Certificate:** `data/contaminated_backbone_depth8_certificate_2026-07-11.txt`.

---

## 1. Parent state

The recorded depth-seven state satisfies

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
\qquad
\max S_7=2021668.
```

Its certified identical-history persistence is

```math
P_7^{\mathrm{cert}}=128
```

and its weighted density is

```math
W_7=\frac{615}{512}.
```

The complete factor-two and factor-four exclusions prove that every continuation either terminates or has scale factor at least `8`.

---

## 2. First exact factor-eight continuation

Set

```math
\boxed{R_7=2097164.}
```

This is the first sponsor-compatible exact-backbone separation at factor eight for which the raw state is four-term-progression-free.

Its two-adic valuation is

```math
v_2(R_7)=2,
```

so the coordinated sponsor is the left endpoint.

Let

```math
A_7=\{0\}\cup S_7
```

and form

```math
G_8
=
A_7
\cup
(A_7+R_7)
\cup
(A_7+2R_7).
```

The verifier checks:

1. the three translate layers are disjoint;
2. `G_8` is four-term-progression-free;
3. the increasing left-sponsor schedule is feasible;
4. the middle multiplicity fiber is exactly `S_7`;
5. the backbone shell is exactly `S_7`.

The raw state has

```math
|G_8|=29523,
\qquad
0\le G_8\le6215996<8388608.
```

Its SHA-256 hash is

```text
83eb6c27fd29e9b3454d9918a32263e4ee4bc2bfd9c0d2136baf465861fd862d
```

and its FNV-64 audit hash is

```text
b5fad81d83531b77
```

Define

```math
S_8=8388608+G_8.
```

Then

```math
S_8\subseteq[8388608,16777216),
\qquad
|S_8|=29523,
```

with

```math
\min S_8=8388608,
\qquad
\max S_8=14604604.
```

Its SHA-256 hash is

```text
e0e750f074e3017b0d20b698c3f1dba3926a5fee5c40d4b0e7dea683b743888f
```

and its FNV-64 audit hash is

```text
023db79dd7cbf62b
```

The certified persistence lower bound is

```math
P_8^{\mathrm{cert}}=256.
```

---

## 3. Weighted-density compensation

The depth-eight weighted density is

```math
W_8
=
256\frac{29523}{8388608}
=
\boxed{\frac{29523}{32768}}.
```

The factor-eight step contracts weighted density by

```math
\boxed{
\frac{W_8}{W_7}
=
\frac{9841}{13120}
\approx0.750076.
}
```

Across the three-generation block beginning at `S_5`,

```math
8,4,8,
```

one has

```math
\boxed{
\frac{W_8}{W_5}
=
\frac{757}{896}
\approx0.844866.
}
```

Thus the cheap release at depth seven is repaid by the forced exact factor-eight continuation.

Relative to the base state,

```math
\boxed{
\frac{W_8}{W_1}
=
\frac{9841}{4096}
\approx2.40259.
}
```

The full seven-step path therefore still carries more weighted density than the base, even though the final three-generation recovery block contracts relative to `S_5`.

---

## 4. Consequences

The branch now has the certified transition pattern

```math
4,8,4,4,8,4,8.
```

This provides the first concrete example of delayed compensation:

1. a factor-eight exact recovery contracts;
2. a factor-four contaminated descendant releases stored growth;
3. the resulting state forbids factors two and four;
4. the first valid next continuation is exact factor eight and repays the release.

The next question is whether `S_8` admits another factor-two or factor-four descendant. Random sampling is not a certificate; the complete finite domains must be classified before any conclusion is recorded.

The broader proof target remains a state-dependent potential that explains and bounds repeated cycles of expensive recovery, cheap release, and forced repayment.
