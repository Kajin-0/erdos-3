# Four-ratio rectangle transport and the exact `S_10` residual profile

## Status

This note contains two different results:

1. an elementary state-independent theorem classifying every integer cancellation ratio by which a signed `0011` rectangle transports through one three-translate replication;
2. an exact finite profile of `512` equal-rank samples from the certified `177844250`-candidate `S_10` factor-four residual.

The transport theorem is universal. The sample profile is finite evidence and does not prove `N_{10,4}=0`.

---

## 1. Base rectangle

Let

```math
B'=G_S(B)=B\cup(B+S)\cup(B+2S).
```

Assume `B` contains the signed rectangle

```math
x,
\quad x+d,
\quad x+2d-U,
\quad x+3d-U,
```

where

```math
d>0,
\qquad
0<U<S.
```

This is the affine-spectrum incidence

```math
\mathcal F_B(U,-U;0)>0.
```

We seek outer separations

```math
T=kS\pm U
```

for which suitable parent and outer layer words cancel the second-difference terms in `S` and `U`.

---

## 2. Exact four-ratio classification

Exact enumeration of normalized layer words in `{0,1,2}^4` gives the following numbers of rectangle-cancellation pairs:

```text
k=1: 8
k=2: 8
k=3: 4
k=4: 4
k>=5: 0
```

Thus the only positive integer transport ratios are

```math
\boxed{k\in\{1,2,3,4\}.}
```

A canonical set of channels is:

| sign | `k` | outer word `lambda` | parent word `mu` | transported common difference |
|---|---:|---|---|---|
| `+` | 1 | `0011` | `1100` | `d` |
| `+` | 2 | `0011` | `2200` | `d` |
| `+` | 3 | `0011` | `1201` | `d+S` |
| `+` | 4 | `0011` | `0202` | `d+2S` |
| `-` | 1 | `0112` | `0011` | `d+S-U` |
| `-` | 2 | `0112` | `0022` | `d+2S-U` |
| `-` | 3 | `0112` | `1021` | `d+2S-U` |
| `-` | 4 | `0112` | `2020` | `d+2S-U` |

All displayed common differences are positive under `d>0` and `0<U<S`.

Therefore:

```math
\boxed{
\mathcal F_B(U,-U;0)>0
\Longrightarrow
G_{kS+U}(G_S(B))
\text{ contains a nontrivial four-term progression}
}
```

and

```math
\boxed{
\mathcal F_B(U,-U;0)>0,
\quad 0<U<S
\Longrightarrow
G_{kS-U}(G_S(B))
\text{ contains a nontrivial four-term progression}
}
```

for every

```math
k\in\{1,2,3,4\}.
```

**Symbolic verifier:** `src/verify_four_ratio_rectangle_transport.py`  
**Certificate:** `data/four_ratio_rectangle_transport_certificate_2026-07-13.txt`

---

## 3. Overlapping transport windows at depth ten

For the recorded state,

```math
S=R_9=134217729.
```

Use the certified depth-nine factor-four fit endpoint

```math
U_{\max}=76583776.
```

The four transport windows are

```text
k=1:   57633953 <= T <= 210801505
k=2:  191851682 <= T <= 345019234
k=3:  326069411 <= T <= 479236963
k=4:  460287140 <= T <= 613454692
```

Successive windows overlap because

```math
2U_{\max}>S.
```

Their union is the single interval

```math
[57633953,613454692],
```

which contains the complete rigorous lifted-completion residual

```math
[97474324,613454687].
```

Consequently every residual candidate `T` has at least one representation

```math
T=kR_9\pm U,
\qquad
1\le k\le4,
\qquad
0\le U\le76583776.
```

The only remaining question for this subsystem is whether at least one associated `U` belongs to the direct rectangle-support set

```math
\mathcal R(B_9)
=
\{U>0:\mathcal F_{B_9}(U,-U;0)>0\}.
```

---

## 4. Exact residual sample

The exact sampler regenerates the certified residual of size

```math
177844250
```

and selects midpoint equal-rank samples

```math
q_j=
\left\lfloor
\frac{(2j+1)177844250}{1024}
\right\rfloor,
\qquad 0\le j<512.
```

The sampled separations run from

```text
176639281 through 613171820.
```

For each sampled `T`, the verifier tests all admissible values

```math
U=|T-kR_9|\le76583776,
\qquad 1\le k\le4,
```

and records an explicit ancestor rectangle and transported progression.

All

```math
\boxed{512/512}
```

samples are covered. The selected channel split is

```text
k=1:   8
k=2:  23
k=3: 212
k=4: 269
```

Every row is independently checked for:

1. all four ancestor rectangle points in `B_9={0}\cup S_9`;
2. the exact parent and outer layer words;
3. positive equal spacing after transport;
4. membership of all four transported points in the actual `S_10` candidate.

The deterministic witness certificate has

```text
FNV-64:   85bfaba25312486b
SHA-256:  e43df5b7621ead4ee9bd1b02d3c812114a7d9a60f9130de0b5f6ab8cad419929
```

**Residual sampler:** `src/sample_depth10_lifted_s9_completion_residual.cpp`  
**Profile verifier:** `src/verify_depth10_residual_multik_rectangle_profile.cpp`  
**Runner:** `src/run_verify_depth10_residual_multik_rectangle_profile.sh`  
**Recorded certificate:** `data/depth10_lifted_residual_multik_rectangle_profile_certificate_2026-07-13.txt`

---

## 5. Exact next target

The sample is no longer the limiting object. The exact finite target is the zero set

```math
Z_9
=
\{1\le U\le76583776:
\mathcal F_{B_9}(U,-U;0)=0\}.
```

For every residual separation `T`, define

```math
K(T)
=
\{k\in\{1,2,3,4\}:|T-kR_9|\le76583776\}.
```

The four-ratio subsystem excludes `T` whenever

```math
\exists k\in K(T)
\quad
|T-kR_9|\notin Z_9.
```

Equivalently, the remaining rectangle-uncovered residual is

```math
\boxed{
\mathcal U_{10}
=
\left\{
T\text{ in the certified residual}:
|T-kR_9|\in Z_9
\text{ for every }k\in K(T)
\right\}.
}
```

Computing `Z_9` and then `\mathcal U_{10}` is the next exact structural calculation. If `\mathcal U_{10}` is empty, then the inherited interval, lifted completion support, and four-ratio rectangle transport together prove

```math
N_{10,4}=0.
```

If it is nonempty, its elements form a mathematically meaningful residual for the other 33 affine obstruction classes. No additional contiguous prefix certification is needed.

---

## 6. Computational design constraint

A naive enumeration of every pair of pair-starts is too large. For `B_9`, the pair-start catalog contains approximately

```text
13030061 nonempty difference groups
```

and the naive sum of pair counts is on the order of

```text
3.33e12 operations.
```

The depth-nine verifier already demonstrates the appropriate strategy: staged count bands, targeted difference tests, and recursive compression. The new engine must adapt that machinery to the direct rectangle equation

```math
U=2d-(y-x)
```

and its reversed orientation, rather than reuse the previous candidate formula without rederivation.
