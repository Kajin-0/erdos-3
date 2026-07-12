# Contaminated-backbone depth-ten chain

## Status

Exact finite computer-assisted construction.

The recorded depth-nine state has no factor-two or factor-four continuation. This note records its first valid exact factor-eight continuation, extending the certified scale sequence to

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

The construction is finite. It does not prove indefinite continuation or solve the reciprocal-sum problem.

**Verifier:** `src/verify_contaminated_backbone_depth10.cpp`.

**Certificate:** `data/contaminated_backbone_depth10_certificate_2026-07-12.txt`.

---

## 1. Parent state

The depth-nine state satisfies

```math
S_9\subseteq[67108864,134217728),
\qquad
|S_9|=88572,
```

```math
\max S_9=115267902,
\qquad
P_9^{\mathrm{cert}}=512,
```

and

```math
W_9
=
P_9^{\mathrm{cert}}\frac{|S_9|}{67108864}
=
\frac{22143}{32768}.
```

The complete cheap-extension certificate proves

```math
\boxed{N_{9,2}=N_{9,4}=0.}
```

Thus every continuation of this recorded state in the standard-dyadic disjoint three-translate replay model either terminates or has scale factor at least `8`.

---

## 2. The first exact factor-eight candidate fails

Exact backbone reproduction begins at

```math
R=2L_9=134217728.
```

This candidate contains the explicit four-term progression

```math
0,
\quad67108864,
\quad134217728,
\quad201326592.
```

Hence `R=2L_9` is invalid.

---

## 3. First valid exact factor-eight continuation

The next sponsor-compatible separation is

```math
\boxed{R_9=134217729.}
```

It has

```math
v_2(R_9)=0,
```

so coordinated side-anchor deletion selects the left endpoint.

Let

```math
A_9=\{0\}\cup S_9
```

and form

```math
G_{10}
=
A_9
\cup
(A_9+R_9)
\cup
(A_9+2R_9).
```

The verifier checks:

1. the three translate layers are disjoint;
2. `G_{10}` is four-term-progression-free;
3. the increasing left-sponsor deletion schedule is feasible;
4. the middle multiplicity fiber is exactly `S_9`;
5. the backbone shell is exactly `S_9`;
6. `R_9` is the first valid sponsor-compatible exact factor-eight separation.

The raw state has

```math
|G_{10}|=265719,
\qquad
0\le G_{10}\le383703360<536870912.
```

Its hashes are

```text
SHA256 d17dfd6e130c4ba222440b0a7b3ed35d91f9c020aed428462440c6b0f5b239c7
FNV64  3920bcc3f69c5c98
```

Define

```math
S_{10}=536870912+G_{10}.
```

Then

```math
S_{10}\subseteq[536870912,1073741824),
\qquad
|S_{10}|=265719,
```

```math
\min S_{10}=536870912,
\qquad
\max S_{10}=920574272.
```

Its hashes are

```text
SHA256 a4882bd7575cd3b49ac1c54d2bbf5123195ff2705faf6fd18751b49e05c7152b
FNV64  405b941a1f8b2580
```

and its certified identical-history persistence lower bound is

```math
\boxed{P_{10}^{\mathrm{cert}}=1024.}
```

---

## 4. Weighted-density repayment

The depth-ten weighted density is

```math
W_{10}
=
1024\frac{265719}{536870912}
=
\boxed{\frac{265719}{524288}}.
```

The final factor-eight step contracts weighted density by

```math
\boxed{
\frac{W_{10}}{W_9}
=
\frac{88573}{118096}
\approx0.750008.
}
```

Relative to the depth-five state,

```math
\boxed{
\frac{W_{10}}{W_5}
=
\frac{88573}{186368}
\approx0.475259.
}
```

The recovery segment after the depth-seven cheap release now contains three consecutive exact factor-eight repayments:

```math
8,4,8,8,8.
```

Relative to the base state,

```math
\frac{W_{10}}{W_1}
=
\frac{88573}{65536}
\approx1.35152>1.
```

Thus the branch remains above its base weighted density after nine outer generations, although the recovery block beginning at `S_5` contracts by more than half.

---

## 5. Consequences and next target

The certified transition pattern is now

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

This path demonstrates:

1. a contaminated cheap-growth burst;
2. path-dependent behavior at the first exact recovery;
3. one later factor-four release;
4. three consecutive forced exact factor-eight repayments.

It does not establish a universal cycle law. The immediate finite question is whether `S_{10}` admits a factor-two or factor-four descendant. The broader proof target remains a state-dependent potential or finite-state classification controlling the long-run average scale growth over the entire continuation tree.
