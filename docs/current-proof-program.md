# Current proof program: obstruction coverage and whole-tree Bellman compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational reduction and recursive genealogy

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to absolute constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

Coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every retained output must be resolved into standard dyadic shells. The genealogy is binary, and for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

Center, root-anchor, predecessor-anchor, and antichain decompositions compress repeated labels. These tools control positive moments and local multiplicity, but reciprocal mass requires a genuinely treewise packing or potential theorem.

---

## 2. Sharp exact benchmark

The aligned-diamond recursion has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp |S_h|^{\log_3 2}.
```

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

A finite automaton and exact carry search certify that its union contains no nontrivial four-term progression.

Inside the exact standard-dyadic equal-translate model,

```math
L'\ge8L,
```

```math
P_h\alpha_h\le C_0(3/4)^h,
```

and

```math
\sum_hP_h\alpha_h\le4C_0.
```

Thus the exact uncontaminated model is sharply classified and summable.

---

## 3. Contaminated path dependence

A certified contaminated chain disproves universal local contraction. Its scale factors begin

```math
4,8,4,4,
```

and, with

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

one has

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

The chain extends through the recorded depth-ten state with scale word

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

At depth ten,

```math
L_{10}=536870912,
\qquad
|S_{10}|=265719,
\qquad
P_{10}=1024,
```

and

```math
W_{10}=\frac{265719}{524288}.
```

Universal one-step contraction, contraction over every four- or six-generation window, and universal two-generation recovery are false. Recovery is path-dependent.

The recorded states satisfy

```math
N_{7,2}=N_{7,4}=0,
```

```math
N_{8,2}=N_{8,4}=0,
```

and

```math
N_{9,2}=N_{9,4}=0.
```

Their finite domains are exhausted by completion, anchor, and equal-difference rectangle witnesses.

---

## 4. Exact factor-eight fan and Bellman accounting

Every valid positive exact factor-eight child of `S_10` has a certified infinite exact continuation. The complete fan contains

```math
\boxed{408855759}
```

valid children. The unmodified schedule handles `408767151`; the remaining `88608` are covered by finite `+1` repairs. Every tail has charge

```math
\boxed{
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
}
```

For constant exact scale factor `c>6`, the affine future-cost function is

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
```

At `c=8`,

```math
\mathfrak B_8=\frac{4P(N+1)}L.
```

For any disjoint three-translate step,

```math
\boxed{
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
}
```

Factors `2` and `4` create Bellman debt, factor `8` is neutral, and factors at least `16` create surplus. This identity is accounting; the missing global theorem must explain why arithmetic contamination forces repayment.

---

## 5. Exact state-independent obstruction spectrum

For

```math
G_R(B)=B\cup(B+R)\cup(B+2R),
```

write a possible progression as

```math
z_i=b_i+\lambda_iR,
\qquad
\lambda_i\in\{0,1,2\}.
```

After global layer normalization and reversal, the `80` nonconstant layer words reduce to exactly

```math
\boxed{34}
```

obstruction classes.

Define

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3.
```

The triple `(r,a,b)` uniquely reconstructs the normalized layer word. Define

```math
\mathcal F_B(A,C;Q)
=
\#\{(x,d):
 x,x+d,x+2d-A,x+3d-(2A+C)\in B,
\ d+Q\ne0\}.
```

Then

```math
\Gamma_\lambda(B;R)
=
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R).
```

The pair-start fibers satisfy

```math
\boxed{
P_d(G_S(B))
=
\bigcup_{i,j\in\{0,1,2\}}
\left(P_{d+(i-j)S}(B)+iS\right).
}
```

The full labeled two-scale recurrence is

```math
\boxed{
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_{\mu\in\{0,1,2\}^4}
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
}
```

This is the state-independent arithmetic framework for contamination growth.

**Primary references:**

- `docs/three-translate-obstruction-coverage-recurrence.md`;
- `src/verify_three_translate_obstruction_classes.py`;
- `data/three_translate_obstruction_classes_certificate_2026-07-13.txt`.

---

## 6. Complete factor-two exclusion from `S_10`

The depth-ten construction contains

```math
L_{10}+(\{0\}\cup S_9)\subseteq S_{10}.
```

Therefore

```math
L_{10}+G_9(R)\subseteq G_{10}(R).
```

The factor-four fit endpoint from `S_9` contains the complete factor-two fit range from `S_10`. Since

```math
N_{9,4}=0,
```

one obtains

```math
\boxed{N_{10,2}=0.}
```

This excludes all

```math
33026376
```

layer-disjoint factor-two candidates and also supplies the inherited lower part of the factor-four exclusion.

---

## 7. Complete factor-four exclusion from `S_10`

The complete factor-four layer-disjoint domain contains

```math
348012826
```

candidates. It splits exactly as

```math
\boxed{
33026376
+
137142200
+
177844250
=
348012826.
}
```

### 7.1 Inherited interval

The first `33026376` candidates are excluded by the translated `S_9` theorem above.

### 7.2 Lifted completion support

The certified depth-nine completion geometry has

```text
13923661 signed completion coordinates
71129286 completion-to-base differences.
```

Lifting these objects through the three embedded depth-nine copies gives

```text
354838701 lifted completion-to-base differences.
```

This removes

```math
137142200
```

additional candidates. The exact residual has

```math
\boxed{177844250}
```

members, ranging from `97474324` through `613454687`, with FNV-64

```text
00369694f2d70526.
```

### 7.3 Complete direct rectangle support of `B_9`

Let

```math
B_9=\{0\}\cup S_9.
```

The exact bounded-memory pair-fiber computation proves

```math
\boxed{
\mathcal F_{B_9}(U,-U;0)>0
\quad
\text{for every }1\le U\le76583776.
}
```

The proof consists of:

```text
76581484 structural support values from exact count bands;
2285 deterministic explicit terminal witnesses;
7 stored exact large-fiber witnesses.
```

Hence

```math
76581484+2285+7=76583776.
```

### 7.4 Four-ratio transport

A direct rectangle at effective separation `U` transports through one three-translate replication at precisely the integer ratios

```math
\boxed{k=1,2,3,4.}
```

For each such `k`, both

```math
T=kS+U
```

and

```math
T=kS-U
```

produce a nontrivial four-term progression, where

```math
S=R_9=134217729.
```

With

```math
U_{\max}=76583776,
```

the four overlapping windows cover the complete residual interval. The boundary case `U=0` is blocked by a pure layer-index progression in

```math
\{0,1,2\}+k\{0,1,2\}.
```

Therefore every residual candidate is excluded, and

```math
\boxed{N_{10,4}=0.}
```

Combining the two cheap factors gives the new exact frontier:

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

**Primary references:**

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `src/verify_b9_direct_rectangle_support.cpp`;
- `src/verify_four_ratio_rectangle_transport.py`;
- `src/verify_s10_factor4_rectangle_closure.py`;
- `src/run_verify_s10_factor4_rectangle_closure.sh`;
- `data/b9_direct_rectangle_support_certificate_2026-07-13.txt`.

---

## 8. What the depth-ten theorem does and does not prove

The result proves that the recorded state `S_10` has no admissible scale-factor `2` or `4` continuation. It replaces the invalid exploratory anchor reduction with actual structural and explicit witnesses.

It does **not** prove that every arbitrary deletion-DAG state reaches `S_10`, has the same direct rectangle coverage, or enters the exact factor-eight fan. A state-specific barrier can coexist with an uncontrolled branching family of other states.

The full Erdős problem therefore remains open.

---

## 9. Active theorem: whole-tree contamination reserve

A pathwise estimate is insufficient: exponentially many paths may each have finite charge while the full tree diverges.

The active target is a nonnegative reserve `Phi` in Bellman units satisfying a branching inequality of the form

```math
\boxed{
W(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(\mathfrak B(S')+\Phi(S')\right)
\le
\mathfrak B(S)+\Phi(S)
+
\operatorname{controlled\ error}.
}
```

The reserve should combine:

1. normalized affine obstruction coverage;
2. remaining dyadic slack;
3. imported-prefix mass;
4. overlap and deduplication packing.

The concrete repayment mechanism now visible at depth ten is

```text
cheap replication
    -> completion and pair-fiber contamination
    -> dense rectangle support
    -> complete elimination of future cheap replication.
```

The next deep theorem must make this mechanism quantitative and stable across arbitrary retained children.

---

## 10. Approved next targets

1. Define a normalized rectangle/completion coverage reserve in units `P/L`.
2. Derive one-sided growth or zero-set contraction under contaminated three-translate replication.
3. Prove that imported prefix copies contribute either new coverage or pack with bounded overlap.
4. Establish a branching Carleson inequality for all retained children.
5. Construct a finite-state or spectral quotient of the pre-basin continuation tree.
6. Determine which structural hypotheses behind the complete `B_9` rectangle interval persist for a class of states, rather than for one numerical state.

---

## 11. Superseded, false, or deprioritized targets

Do not use without new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. cardinality-only subpower bounds below exponent `log_3 2`;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every four- or six-step window;
6. universal two-generation recovery after an exact factor-eight step;
7. extrapolating one distinguished path to the whole continuation tree;
8. treating one or many exact tails as a whole-tree theorem;
9. using one third-difference equation as a complete four-term-progression test;
10. treating pathwise summability as sufficient for the branching deletion tree;
11. the rejected depth-ten anchor reduction;
12. additional contiguous `S_10` candidate-prefix certification.

The complete `S_10` cheap-extension theorem is now a finished state-specific component. The unresolved problem is to convert arithmetic contamination into a universal treewise reserve and packing theorem.
