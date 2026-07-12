# Certainty-ledger update: contaminated-backbone cheap replication

## CL-next: Finite contaminated-backbone depth-five chain

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the identical-history interpretation pending independent review.

**Audit state:** awaiting independent expert review and integration into `docs/certainty-ledger.md`.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad
1\le h\le5,
```

with scales

```math
(L_1,L_2,L_3,L_4,L_5)
=
(64,256,2048,8192,32768)
```

and separations

```math
(R_1,R_2,R_3,R_4)
=
(61,303,1597,8195).
```

The outer dyadic scale factors are

```math
\boxed{4,8,4,4.}
```

At each step:

1. the selected step-`R_h` middle multiplicity fiber is exactly `S_h`;
2. the relevant backbone shell contains `S_h` plus additional points;
3. the deletion schedule inside `S_h` can be replayed in that backbone subset;
4. both continuations have the same new root anchor;
5. certified identical-history persistence doubles.

Thus

```math
P_h^{\mathrm{cert}}=2^h
```

is a certified lower bound.

The state cardinalities are

```math
12,39,120,363,1092.
```

The backbone contamination counts are

```math
4,1,33,1.
```

Define

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h}.
```

Then

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

and

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}.
}
```

**Primary note:** `docs/contaminated-backbone-depth-five-chain.md`.

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

**Certificate:** `data/contaminated_backbone_depth5_certificate_2026-07-11.txt`.

**Consequence:** the sharp exact-model `3/4` contraction does not extend to contaminated-backbone replication one step at a time, and contraction can fail over a four-step window.

**Explicitly false without stronger hypotheses:**

1. universal one-step `3/4` contraction for a backbone that merely contains the replay state;
2. universal strict contraction at every non-exact step;
3. contraction over every block of four consecutive outer steps;
4. a local dichotomy in which every departure from exact replication automatically incurs a stronger loss.

**Caveat:** this is finite. It does not prove indefinite extension, long-run growth, or a divergent reciprocal-sum counterexample.

---

## OB-next: Long-run contamination compensation

The active question is whether every sufficiently long contaminated-backbone genealogy eventually compensates for cheap scale-factor steps.

Useful target forms include:

1. cumulative scale expansion exceeding the `6`-per-generation threshold needed to offset disjoint `3`-for-`2` replication;
2. a monotone overlap potential that stores the debt created by factor-four steps;
3. export of contaminating points into additional lower-scale four-term-progression-free children;
4. a finite-state or spectral classification of repeatable contaminated patterns;
5. a theorem that repeated cheap steps force a four-term progression.

The immediate computational question is whether the certified factor pattern can be extended indefinitely or only through bounded bursts.
