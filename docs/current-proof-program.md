# Current proof program: obstruction coverage and whole-tree Bellman compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A}1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational recursion

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

The genealogy is binary. Every child must be resolved into standard dyadic shells. Every parent creates at most two retained outputs, each at most half its label, so for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

Center, root-anchor, predecessor-anchor, and antichain decompositions compress repeated labels. These tools control positive moments and local multiplicity, but not reciprocal mass by themselves.

---

## 2. Sharp exact model

The aligned-diamond recursion has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp|S_h|^{\log_3 2}.
```

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

A 34-state automaton and an exact `17238`-state carry search certify that its union contains no nontrivial four-term progression.

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

The exact model is sharply classified.

---

## 3. Contaminated path dependence

A certified contaminated chain has scale factors

```math
\boxed{4,8,4,4}
```

through `S_5`. With

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
\qquad
\frac{W_5}{W_1}=\frac{91}{32}.
```

Local contraction and contraction over every four-generation window are false.

The alternative exact recovery

```math
R_5=93476
```

admits the factor-four descendant

```math
R_6=230164,
```

giving

```math
\boxed{4,8,4,4,8,4}
```

through `S_7`, with

```math
\frac{W_7}{W_5}=\frac{205}{182}>1.
```

Universal two-generation recovery and contraction over every six-generation window are false. Recovery is path-dependent.

---

## 4. Recorded branch through `S_10`

The recorded states `S_7`, `S_8`, and `S_9` satisfy

```math
N_{h,2}=N_{h,4}=0.
```

Their factor-four layer-disjoint domains are exhausted by completion, `1001`, and equal-difference `0011` witnesses:

```text
S7:      359419
S8:     4190292
S9:    39459384
```

The first valid exact continuations are

```math
R_7=2097164,
\qquad
R_8=16777217,
\qquad
R_9=134217729.
```

The finite scale sequence is

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

```math
W_{10}=\frac{265719}{524288},
```

and

```math
\frac{W_{10}}{W_5}=\frac{88573}{186368}\approx0.475259.
```

---

## 5. Exact-tail layer theorems

For the certified exact-tail shell geometries, every new four-term progression in three translates comes from either:

1. a three-term progression completed at the separation `R`; or
2. the half-separation point `R/2` lying in the state.

For `R=2L+k`, child completion targets descend through the unique layer pattern `012`. The scheduled target `4k` descends exactly to the preceding separation `2L+k`.

These layer statements were verified by exact rational vertex enumeration in all entry, invariant, repair, and full-fitting regions used below.

---

## 6. Complete exact factor-eight fan from `S_10`

Write every fitting exact separation as

```math
R=2L_{10}+k,
\qquad
1\le k\le613454687.
```

There are `408969792` sponsor-compatible positive offsets. The complete first-step obstruction split is

```text
completion-blocked       54999
half-separation-blocked  59034
overlap                       0
```

so

```math
\boxed{408855759}
```

offsets give valid exact factor-eight children.

The unmodified schedule

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

already gives infinite exact tails for `408767151` valid children. The remaining valid children are repaired as follows:

```text
88606 second-step failures:  4k  -> 4k+1
2 third-step failures:       16k -> 16k+1
```

Therefore

```math
\boxed{
408767151+88606+2
=
408855759.
}
```

Every valid exact factor-eight child of `S_10` has an explicit infinite exact four-term-progression-free continuation. Every tail has total charge

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{33215}{16384}.
}
```

**Primary references:**

- `docs/complete-exact-child-tail-fan.md`;
- `src/verify_complete_exact_child_tail_fan.py`;
- `data/complete_exact_child_tail_fan_certificate_2026-07-12.txt`.

---

## 7. Bellman potential and debt

For constant exact scale factor `c>6`, the affine future-cost function is

```math
\boxed{
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
}
```

At `c=8`,

```math
\mathfrak B_8=\frac{4P(N+1)}L.
```

For any disjoint three-translate step with scale factor `c`,

```math
\boxed{
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
}
```

Factors `2` and `4` create debt, factor `8` is Bellman-neutral, and factors at least `16` create surplus.

A path whose scale word can be parsed into blocks

```text
[8 or larger]
[one 4 plus two 8-equivalents]
[one 2 plus four 8-equivalents]
```

has summable weighted density. The worst block-boundary contraction is

```math
\frac{2551}{2560}<1.
```

Universal geometric realizability of this parsing remains open. The Bellman identity is an accounting theorem; it does not by itself explain why cheap debt must be repaid.

---

## 8. Cheap-step geometry

For top slack

```math
T=2L-\max S,
```

a step with scale factor `c` and separation `R` satisfies

```math
\boxed{T'=T+(c-2)L-2R.}
```

Every cheap Bellman debt therefore carries a geometric certificate: strict slack consumption or imported prefix contamination. The missing theorem must convert this geometry and the associated arithmetic coverage into a branching-compatible reserve.

---

## 9. Complete factor-two exclusion from `S_10`

The exact depth-ten construction contains a translated anchor copy of the preceding state:

```math
\boxed{
L_{10}+(\{0\}\cup S_9)
\subseteq
S_{10}.
}
```

Therefore, for every separation `R`,

```math
L_{10}+G_9(R)\subseteq G_{10}(R),
```

where

```math
G_h(R)=(\{0\}\cup S_h)+\{0,R,2R\}.
```

The factor-four fit endpoint from `S_9` is `76583776`, while the factor-two fit endpoint from `S_10` is `76583775`. Hence every sponsor-compatible layer-disjoint factor-two candidate from `S_10` lies in the already exhausted factor-four domain of `S_9`. Since

```math
N_{9,4}=0,
```

every such progression lifts by translation into the `S_10` candidate. Thus

```math
\boxed{N_{10,2}=0.}
```

**Primary references:**

- `docs/depth-ten-factor-two-inheritance-exclusion.md`;
- `src/verify_depth10_factor2_inheritance.py`;
- `data/depth10_factor2_inheritance_certificate_2026-07-12.txt`.

---

## 10. Factor-four `S_10` domain: finite evidence, not the active theorem

The complete factor-four domain certificate gives

```text
maximum R:            613454687
sponsor-compatible:   408969792
layer-disjoint:       348012826
FNV-64:               ae1d9e1ec77b2dfb
```

The inherited interval `R<=76583775` contains exactly `33026376` layer-disjoint candidates and is excluded by the factor-two inheritance theorem. Therefore the genuinely new factor-four domain has

```math
\boxed{314986450}
```

candidates.

The first `10000` candidates in this new domain have explicit deterministic four-point witnesses. The certified prefix runs from

```text
R = 76583927
through
R = 76697408
```

and leaves at most

```math
314976450
```

unclassified candidates. This is a finite prefix certificate only. It does not prove `N_10,4=0` and does not validate the rejected bulk anchor reduction.

Sequential prefix certification is now deprioritized. The existing first-`10000` suite is retained as a regression test and theorem-discovery dataset.

**Primary references:**

- `docs/depth-ten-factor-four-first10000.md`;
- `src/run_verify_depth10_factor4_first10000.sh`;
- `docs/depth-ten-factor-four-exclusion-audit.md`.

---

## 11. Exact state-independent obstruction coverage

For

```math
G_R(B)=B\cup(B+R)\cup(B+2R),
```

write a potential progression as

```math
z_i=b_i+\lambda_iR,
\qquad
\lambda_i\in\{0,1,2\}.
```

After removing global layer shifts and quotienting by reversal, the `80` nonconstant raw layer words reduce to exactly

```math
\boxed{34}
```

obstruction classes: `30` reversal pairs and the four self-reversing classes

```text
0110  0220  1001  2002.
```

Define the exact signature

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3.
```

The triple `(r,a,b)` uniquely reconstructs the normalized layer word. A class occurs at separation `R` exactly when there are `x,d` such that

```math
x,
\quad x+d,
\quad x+2d-aR,
\quad x+3d-(2a+b)R
```

belong to `B`, with

```math
d+rR\ne0.
```

Define the affine-incidence spectrum

```math
\mathcal F_B(A,C;Q)
=
\#\{(x,d):x,x+d,x+2d-A,x+3d-(2A+C)\in B,
\ d+Q\ne0\}.
```

Then

```math
\Gamma_\lambda(B;R)
=
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R).
```

For the `0011` class this factors through pair-start sets

```math
P_d(B)=\{x\in B:x+d\in B\},
```

with exact recurrence

```math
\boxed{
P_d(G_S(B))
=
\bigcup_{i,j\in\{0,1,2\}}
\left(P_{d+(i-j)S}(B)+iS\right).
}
```

More generally, if `B'=G_S(B)` and a new separation `T` is tested, the labeled class coverage obeys

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

This is the exact state-independent obstruction-coverage recurrence. It corrects the insufficient one-scalar third-difference formulation: a four-term progression requires two second-difference constraints.

**Primary references:**

- `docs/three-translate-obstruction-coverage-recurrence.md`;
- `src/verify_three_translate_obstruction_classes.py`;
- `data/three_translate_obstruction_classes_certificate_2026-07-13.txt`.

---

## 12. Active target: whole-tree contamination reserve

A pathwise estimate alone is not enough. Exponentially many paths can each have finite charge while the full recursive tree has divergent total mass. The required theorem must control the branching genealogy after deduplication or packing.

The active target is a nonnegative reserve `Phi` in Bellman units such that a branching transition satisfies an inequality of the form

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

The reserve should combine normalized obstruction coverage, remaining dyadic slack, imported prefixes, and overlap packing. The conceptual mechanism is

```text
cheap replication
    -> Bellman debt
    -> growth of affine obstruction coverage or loss of slack
    -> forced expensive replication / exact-tail entry
    -> treewise repayment.
```

Approved next targets:

1. classify stratified witnesses across the full `S_10` factor-four range by the `34` exact layer classes;
2. trace each witness to parent-layer word `mu` and ancestor origin in the two-scale recurrence;
3. identify a small closed subsystem or monotone contraction of the uncovered-separation zero set;
4. define a normalized affine-coverage reserve in units `P/L`;
5. prove a branching Carleson/packing inequality for all retained children;
6. charge imported prefixes through difference export or overlap packing.

Deprioritized routes:

1. additional contiguous `S_10` prefix certification;
2. extending one distinguished branch without testing a recurrence or reserve;
3. more exact-tail counting;
4. local constants without a telescoping or branching consequence.

No current theorem closes the reserve inequality. The full Erdős problem remains unresolved.
