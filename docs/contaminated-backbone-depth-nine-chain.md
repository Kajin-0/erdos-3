# Contaminated-backbone depth-nine chain

## Status

Exact finite computer-assisted construction.

The recorded depth-eight state has no factor-two or factor-four continuation. This note records its first valid exact factor-eight continuation, extending the certified scale sequence to

```math
\boxed{4,8,4,4,8,4,8,8.}
```

The construction is finite. It does not prove indefinite continuation or solve the reciprocal-sum problem.

**Verifier:** `src/verify_contaminated_backbone_depth9.cpp`.

**Certificate:** `data/contaminated_backbone_depth9_certificate_2026-07-11.txt`.

---

## 1. Parent state

The depth-eight state satisfies

```math
S_8\subseteq[8388608,16777216),
\qquad
|S_8|=29523,
```

```math
\max S_8=14604604,
\qquad
P_8^{\mathrm{cert}}=256,
```

and

```math
W_8
=
P_8^{\mathrm{cert}}\frac{|S_8|}{8388608}
=
\frac{29523}{32768}.
```

The complete cheap-extension certificate proves

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

Thus every continuation of this recorded state in the standard-dyadic disjoint three-translate replay model either terminates or has scale factor at least `8`.

---

## 2. The first exact factor-eight candidate fails

Exact backbone reproduction begins at

```math
R=2L_8=16777216.
```

This candidate contains the explicit four-term progression

```math
0,
\quad8388608,
\quad16777216,
\quad25165824.
```

Hence `R=2L_8` is invalid.

---

## 3. First valid exact factor-eight continuation

The next sponsor-compatible separation is

```math
\boxed{R_8=16777217.}
```

It has

```math
v_2(R_8)=0,
```

so coordinated side-anchor deletion selects the left endpoint.

Let

```math
A_8=\{0\}\cup S_8
```

and form

```math
G_9
=
A_8
\cup
(A_8+R_8)
\cup
(A_8+2R_8).
```

The verifier checks:

1. the three translate layers are disjoint;
2. `G_9` is four-term-progression-free;
3. the increasing left-sponsor deletion schedule is feasible;
4. the middle multiplicity fiber is exactly `S_8`;
5. the backbone shell is exactly `S_8`;
6. `R_8` is the first valid sponsor-compatible exact factor-eight separation.

The raw state has

```math
|G_9|=88572,
\qquad
0\le G_9\le48159038<67108864.
```

Its hashes are

```text
SHA256 68fd383e153a8a6beb5ed42b643b21a2f841abeac3e015f8a38a26866963cc5c
FNV64  a323906d13700252
```

Define

```math
S_9=67108864+G_9.
```

Then

```math
S_9\subseteq[67108864,134217728),
\qquad
|S_9|=88572,
```

```math
\min S_9=67108864,
\qquad
\max S_9=115267902.
```

Its hashes are

```text
SHA256 43811627a1a49910ecea5656f6542f533d3e177adc2be80daccfe2092c4f650b
FNV64  5005dc89644a7b80
```

and its certified identical-history persistence lower bound is

```math
\boxed{P_9^{\mathrm{cert}}=512.}
```

---

## 4. Weighted-density repayment

The depth-nine weighted density is

```math
W_9
=
512\frac{88572}{67108864}
=
\boxed{\frac{22143}{32768}}.
```

The final factor-eight step contracts weighted density by

```math
\boxed{
\frac{W_9}{W_8}
=
\frac{7381}{9841}
\approx0.750025.
}
```

Relative to the depth-five state,

```math
\boxed{
\frac{W_9}{W_5}
=
\frac{7381}{11648}
\approx0.633671.
}
```

The branch now contains two consecutive exact factor-eight repayments after the depth-seven cheap release:

```math
8,4,8,8.
```

Relative to the base state,

```math
\frac{W_9}{W_1}
=
\frac{7381}{4096}
\approx1.80200>1.
```

Thus the branch remains above its base weighted density after eight outer generations, although the recovery block beginning at `S_5` contracts substantially.

---

## 5. Consequences and next target

The certified transition pattern is now

```math
\boxed{4,8,4,4,8,4,8,8.}
```

This demonstrates a delayed release followed by two forced exact-recovery steps. It does not establish a universal cycle law: the result concerns one explicit continuation path.

The immediate finite question is whether `S_9` admits a factor-two or factor-four descendant. The broader proof target remains a state-dependent potential or finite-state classification that bounds the long-run average scale growth over the entire continuation tree.
