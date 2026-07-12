# Current proof program: continuation-tree compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A}1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. The theorem-style claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Dyadic reduction and one-generation recursion

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty
```

up to absolute constants. A divergent four-term-progression-free candidate must satisfy `alpha_j -> 0` while `sum_j alpha_j = infinity`.

For a four-term-progression-free block `D subseteq[N,2N)`, coordinated side-anchor deletion removes `K=|D|-s` sponsors and leaves a three-term-progression-free residual with `s<=r_3(N)`. The minimum-translation backbone

```math
\mathcal B(D)=\{d-\min D:d\in D,\ d>\min D\}
```

is four-term-progression-free, has size `|D|-1`, lies below `N`, and contracts each associated label by at least one half.

The strongest current one-generation inequalities are

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

The genealogy remains binary.

---

## 2. Shell interface and multiplicity compression

Every child must be resolved into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

Each parent produces at most two retained outputs, each at most half its label. For `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p,
```

and across the full tree,

```math
\sum_q\mu(q)q^p\le2^{1-p}\sum_{a\text{ root}}a^p.
```

Repeated labels at different centers, root anchors, and predecessor anchors are exported by translated layers. Copies with one fixed complete anchor history obey

```math
\lambda_{x,q}(t)(a-t)\le a.
```

These facts control positive moments and local multiplicity, but not reciprocal mass by themselves.

---

## 3. Self-replicating aligned diamonds and the exact model

The base gadget

```math
H=\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

supports identical-history persistence

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus `P_h asymp |S_h|^(log_3 2)`, disproving bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds based only on parent cardinality.

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton and an exact `17238`-state carry search certify that its union contains no nontrivial four-term progression.

Inside the exact standard-dyadic equal-translate model,

```math
L'\ge8L,
```

and, with `alpha_h=|S_h|/L_h`,

```math
P_h\alpha_h\le C_0\left(\frac34\right)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

The exact model is sharply classified.

---

## 4. Contaminated growth and path dependence

A certified contaminated chain has scale factors

```math
\boxed{4,8,4,4}
```

through `S_5`. For

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

Thus local contraction and contraction over every four-generation window are false.

The state `S_5` has no factor-two or factor-four continuation. Its smallest exact recovery enters a strongly contracting branch, but the alternative exact recovery

```math
R_5=93476
```

admits the factor-four descendant

```math
R_6=230164.
```

This gives

```math
\boxed{4,8,4,4,8,4}
```

through `S_7`, with

```math
W_7=\frac{615}{512},
\qquad
\frac{W_7}{W_5}=\frac{205}{182}>1.
```

Universal two-generation recovery and contraction over every six-generation window are therefore false. Recovery is path-dependent.

---

## 5. Structural cheap-extension exclusions

The recorded states `S_7`, `S_8`, and `S_9` each satisfy

```math
N_{h,2}=N_{h,4}=0.
```

The factor-four exclusions use explicit structural witnesses:

- `S_7`: `359419` disjoint candidates, covered by completion, `1001`, and `0011` witnesses;
- `S_8`: `4190292` disjoint candidates, covered by completion witnesses and bounded-memory residual joins;
- `S_9`: `39459384` disjoint candidates, with `30221222` completion witnesses and the residual reduced to seven explicit full-parent witnesses.

These are finite theorems for the recorded states, not state-independent results.

---

## 6. Recorded exact branch through `S_10`

The first valid exact continuations after `S_7` are

```math
R_7=2097164,
\qquad
R_8=16777217,
\qquad
R_9=134217729.
```

The certified scale sequence becomes

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

The depth-ten state satisfies

```math
S_{10}\subseteq[536870912,1073741824),
```

```math
|S_{10}|=265719,
\qquad
P_{10}^{\mathrm{cert}}=1024,
```

and

```math
W_{10}=\frac{265719}{524288}.
```

Relative to `S_5`,

```math
\frac{W_{10}}{W_5}=\frac{88573}{186368}\approx0.475259.
```

---

## 7. Infinite exact summable tail from `S_10`

Let

```math
D=2^{18}-1=262143,
\qquad
k_{10}=D+6=262149.
```

For `h>=10`, define

```math
L_{h+1}=8L_h,
\qquad
k_{h+1}=4k_h,
\qquad
R_h=2L_h+k_h,
```

and apply exact three-translate reproduction.

Two exact layer-pattern lemmas reduce every possible new four-term progression to either:

1. a three-term progression in `S_h` completed at `R_h`; or
2. the point `R_h/2` inside `S_h`.

A finite `S_8` certificate finds `2772873` three-term-progression completions, with maximum `17038008`. Since

```math
2L_8+D=17039359,
```

the seed completion is absent. Completion descent preserves the absence because `k_(h+1)=4k_h`, while a persistent lower gap excludes `R_h/2`.

For `n>=0`,

```math
k_{10+n}=262149\cdot4^n,
```

```math
|S_{10+n}|=\frac{3^{12+n}-3}{2},
\qquad
P_{10+n}^{\mathrm{cert}}=2^{10+n},
```

and

```math
W_{10+n}=\frac{3^{12+n}-3}{2^{20+2n}}.
```

The entire scheduled tail is summable:

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{33215}{16384}.
}
```

---

## 8. General exact-tail basin criterion

A state `(S,L,k,P)` is an exact-tail basin entry when:

```math
S\subseteq[L,7L/4),
\qquad
0<k\le L/32,
```

```math
v_2(k)\equiv0\pmod2,
```

```math
S\cap(L,L+L/8)=\varnothing,
```

and no three-term progression in `S` has missing completion `2L+k`.

Then the recurrence

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n,
\qquad
R_n=2L_n+k_n
```

produces an infinite exact four-term-progression-free tail.

If the entry state has size `N`, certified replay multiplicity `P`, and scale `L`, then

```math
W_n
=
\frac{P}{L}
\left[
\left(N+\frac32\right)\left(\frac34\right)^n
-
\frac32\left(\frac14\right)^n
\right],
```

and its exact basin terminal charge is

```math
\boxed{
\mathfrak B_8(S,L,P)
=
\sum_{n\ge0}W_n
=
\frac{4P(N+1)}L.
}
```

This is a reusable absorbing-state criterion for continuation-tree arguments.

**Primary reference:** `docs/exact-tail-basin-criterion.md`.

---

## 9. Basin width at `S_10`

Two completion descents from `S_10` to the certified `S_8` seed show that every offset

```math
260799\le k\le1048579
```

with even `v_2(k)` is a basin entry. There are exactly

```math
\boxed{525189}
```

such offsets.

Each produces a distinct infinite exact tail and has the same terminal charge

```math
\frac{33215}{16384}.
```

Thus the summable basin at `S_10` occupies a substantial finite interval of separation parameters rather than one isolated continuation.

**Primary references:**

- `docs/depth-ten-exact-tail-basin-fan.md`;
- `src/verify_depth10_exact_tail_basin_fan.py`;
- `data/depth10_exact_tail_basin_fan_certificate_2026-07-12.txt`.

---

## 10. Bellman potential

For an exact constant-scale continuation with scale factor `c>6`, size recurrence `N'=3(N+1)`, and replay recurrence `P'=2P`, the unique affine future-cost function satisfying

```math
\mathfrak B_c(N,P,L)
=
\frac{PN}{L}
+
\mathfrak B_c(N',P',cL)
```

is

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
\boxed{
\mathfrak B_8(N,P,L)=\frac{4P(N+1)}L.
}
```

A basin node can therefore be replaced exactly by this terminal value in a dynamic-programming or supermartingale argument.

**Primary reference:** `docs/exact-tail-bellman-potential.md`.

---

## 11. Current unresolved problem: whole-tree compensation

The existence of many summable tails from one state does not control all descendants. The active target is

```math
\boxed{
\text{prove that every infinite continuation path has summable total weighted density.}
}
```

Equivalent targets include:

1. every infinite path has long-run geometric-mean scale expansion greater than `6`;
2. every path eventually enters an exact or near-exact basin;
3. contamination creates a debt repaid by later scale growth or exported difference structure;
4. a parent potential dominates current weight plus the aggregate potential of all non-basin children;
5. the continuation tree has a finite-state or spectral quotient with subcritical weighted growth;
6. overlapping replay cores satisfy an aggregate packing theorem.

Immediate work:

1. classify factor-two and factor-four continuations of `S_10` that avoid the known basin fan;
2. generalize the top-layer and completion-descent lemmas to contaminated or near-exact steps;
3. construct a contamination-debt potential extending the exact Bellman potential;
4. search for a finite quotient of pre-basin continuation states.

The full Erdős problem remains unresolved.
