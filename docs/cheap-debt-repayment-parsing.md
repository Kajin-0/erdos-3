# Cheap-debt repayment parsing theorem

## Status

Elementary consequence of the scale-word Bellman identity. This note gives a sufficient combinatorial condition for a continuation path to have summable total weighted density.

It does not prove that every geometrically valid path admits the required parsing.

---

## 1. Endpoint ratio for a finite block

Let a block begin with a state of size `N`, replay multiplicity `P`, and scale `L`. Suppose the block has length `H` and cumulative scale product

```math
C=\prod_{j=0}^{H-1}c_j.
```

For the factor-eight reference potential

```math
\mathfrak B=\frac{4P(N+1)}L,
```

the exact endpoint ratio is

```math
\boxed{
\frac{\mathfrak B_H}{\mathfrak B_0}
=
\frac{2^H}{C}
\frac{3^H(N+\tfrac32)-\tfrac12}{N+1}.
}
```

The ratio depends on the scale factors only through `C`, so their order inside the block is irrelevant.

---

## 2. Three repayment block types

Assume

```math
N\ge9.
```

### Type A: neutral-or-better single step

For a one-step block with

```math
C\ge8,
```

```math
\frac{\mathfrak B_1}{\mathfrak B_0}
=
\frac{2(3N+4)}{C(N+1)}
\le
\frac{3N+4}{4(N+1)}
<1.
```

This includes every factor-eight or larger step not reserved to repay earlier debt.

### Type B: one factor-four debt plus two factor-eight repayments

For a three-step block with

```math
C\ge4\cdot8\cdot8=256,
```

```math
\frac{\mathfrak B_3}{\mathfrak B_0}
\le
\frac{27N+40}{32(N+1)}.
```

For `N>=9`, this is at most

```math
\frac{283}{320}.
```

Thus any permutation of

```text
4,8,8
```

strictly repays one factor-four debt. Larger factors only strengthen the contraction.

### Type C: one factor-two debt plus four factor-eight repayments

For a five-step block with

```math
C\ge2\cdot8^4=8192,
```

```math
\frac{\mathfrak B_5}{\mathfrak B_0}
\le
\frac{243N+364}{256(N+1)}.
```

For `N>=9`, this is at most

```math
\boxed{
\frac{2551}{2560}
<1.
}
```

Thus any permutation of

```text
2,8,8,8,8
```

strictly repays one factor-two debt.

---

## 3. Parsing theorem

Consider an infinite continuation path whose state sizes are at least `9`. Suppose its scale-factor word can be partitioned into finite consecutive blocks of the following forms:

1. a one-step block with product at least `8`;
2. a three-step block with product at least `256`;
3. a five-step block with product at least `8192`.

Then the Bellman potential at successive block boundaries contracts by the uniform factor

```math
q=\frac{2551}{2560}<1.
```

Within any block, every dyadic scale factor is at least `2`. The one-step potential ratio is bounded above by

```math
\frac{2(3N+4)}{2(N+1)}
<
\frac72.
```

Since every block has length at most `5`, all intermediate potentials are bounded by a universal multiple of the potential at the block entrance. Also

```math
W=\frac{PN}{L}<\frac14\mathfrak B.
```

Therefore the total weighted density over each block is bounded by a universal constant times its entrance potential. Summing over geometrically contracting block entrances gives

```math
\boxed{
\sum_{h\ge0}W_h<\infty.
}
```

---

## 4. Debt-token interpretation

The parsing can be viewed as a matching rule:

- each factor-four token must be matched with two factor-eight tokens;
- each factor-two token must be matched with four factor-eight tokens;
- unmatched factor-eight or larger tokens form their own contracting blocks;
- factors at least `16` may replace multiple factor-eight repayment tokens through the product criterion.

The matching must use disjoint consecutive blocks, but the order inside each block is irrelevant.

---

## 5. Recorded branch

After the depth-seven factor-four release, the structural exclusions at `S_7` and `S_8` force two consecutive factor-eight steps. Thus the relevant three-step word is

```text
4,8,8
```

and forms a Type-B repayment block. The following factor-eight steps are Type-A blocks and enter the exact summable basin.

This separates the proof into two components:

1. **geometry:** force an admissible repayment parsing;
2. **accounting:** apply the theorem above.

---

## 6. Remaining problem

A whole-tree proof would follow from a state-independent theorem that every infinite continuation scale word admits such a parsing, perhaps after allowing a finite collection of additional repayment blocks.

Equivalent geometric tasks include:

1. show that factor-four steps force two later factor-eight equivalents before another unmatched cheap step;
2. show that factor-two steps force four later factor-eight equivalents;
3. allow larger scale factors to repay several cheap debts at once;
4. charge exceptional unparsed cheap steps to contamination export or overlap packing.
