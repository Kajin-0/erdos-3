# Full-fitting exact-tail basin from `S_10`

## Status

Exact finite classification plus an elementary induction theorem with exact rational layer-pattern verification.

Among all valid positive exact factor-eight children of the recorded depth-ten state, all but `88608` enter certified infinite exact factor-eight tails under the scheduled recurrence

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n.
```

The resulting basin contains

```math
\boxed{408767151}
```

distinct exact children, or approximately `99.9783%` of the complete valid exact-child family.

**Verifier:** `src/verify_full_fitting_exact_tail_basin.py`.

**Certificate:** `data/full_fitting_exact_tail_basin_certificate_2026-07-12.txt`.

---

## 1. Complete exact-child domain

For the recorded state

```math
S_{10}\subseteq[L_{10},2L_{10}),
\qquad
L_{10}=536870912,
```

```math
|S_{10}|=265719,
\qquad
\max S_{10}=920574272,
```

write every fitting exact separation as

```math
R_0=2L_{10}+k.
```

The complete exact classification gives

```math
1\le k\le613454687
```

and

```text
408969792 sponsor-compatible positive offsets
54999 completion obstructions
59034 first-step half-separation obstructions
0 overlap between the obstruction classes.
```

Therefore

```math
\boxed{408855759}
```

positive offsets produce valid four-term-progression-free exact children.

This theorem classifies the future scheduled behavior of those valid children.

---

## 2. Scheduled recurrence

Put

```math
L_0=L_{10},
\qquad
S_0=S_{10},
\qquad
k_0=k,
```

and define

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n,
\qquad
R_n=2L_n+k_n.
```

Let

```math
A_n=\{0\}\cup S_n,
```

```math
G_{n+1}
=
A_n\cup(A_n+R_n)\cup(A_n+2R_n),
```

```math
S_{n+1}=L_{n+1}+G_{n+1}.
```

The initial parent `G_1` is assumed valid because `k` belongs to the complete valid exact-child list.

The problem is to determine when every scheduled successor is also four-term-progression-free.

---

## 3. Exact pattern persistence over the full fitting range

Write

```math
q_n=\frac{\max S_n}{L_n},
\qquad
r_n=\frac{k_n}{L_n}.
```

The exact recurrence is

```math
q_{n+1}
=
1+\frac{q_n+4+2r_n}{8},
```

```math
r_{n+1}=\frac{r_n}{2}.
```

At the largest fitting initial offset,

```math
q_0=\frac{920574272}{536870912},
\qquad
r_0\le\frac{613454687}{536870912}.
```

The successive exact upper bounds are

| Generation | `q_n` upper bound | `r_n` upper bound |
|---:|---:|---:|
| 0 | `14383973/8388608` | `613454687/536870912` |
| 1 | `4294967295/2147483648` | `613454687/1073741824` |
| 2 | `32518589819/17179869184` | `613454687/2147483648` |
| 3 | `248492295019/137438953472` | `613454687/4294967296` |

Exact rational vertex enumeration proves, for generations `0`, `1`, and `2`:

1. the standard nine top-layer patterns are the only feasible four-term-progression patterns;
2. the scheduled completion descent has the unique layer pattern `012` and base pattern `111`.

Consequently, at each of these generations a new four-term progression can arise only from:

1. a three-term progression completed at the scheduled separation; or
2. the scheduled half-separation point lying in the state.

The completion obstruction descends to the preceding scheduled separation. Since the preceding parent is valid, no scheduled completion obstruction occurs.

After the third finite generation,

```math
q_3<\frac{15}{8},
\qquad
r_3<\frac14.
```

This is the invariant exact-tail region already certified by the half-scale basin theorem. Thus only the first two new scheduled half-separation tests require finite classification.

---

## 4. Second scheduled half obstruction

The second scheduled separation is

```math
R_1=2L_1+k_1=16L_0+4k.
```

Its half is

```math
\frac{R_1}{2}=L_1+2k.
```

Because

```math
S_1=L_1+G_1,
```

the half obstruction is

```math
2k\in G_1.
```

Throughout the fitting range,

```math
2k<R_0,
```

so `2k` can only lie in the unshifted anchor layer. Therefore

```math
\boxed{
\frac{R_1}{2}\in S_1
\quad\Longleftrightarrow\quad
2k\in S_{10}.
}
```

Among sponsor-compatible fitting offsets, this gives

```text
88614 second-scheduled-step obstructions
minimum k 268435456
maximum k 460287135.
```

Hashes of the ordered obstruction list are

```text
FNV-64  9cbe1d4b4bf738d2
SHA-256 09f3cbb9ae87bfefcdc117f8e4340f4a1c93792ccf2a6b3ccacd5f2489ccb15e
```

Exactly `8` of these offsets were already excluded by the first-step half obstruction in the complete exact-child classification.

---

## 5. Third scheduled half obstruction

The third scheduled separation has half

```math
\frac{R_2}{2}=L_2+8k.
```

Thus the obstruction asks whether

```math
8k\in G_2.
```

Since

```math
8k<R_1,
```

this reduces to

```math
8k\in S_1.
```

Using

```math
S_1=8L_0+G_1,
```

one obtains

```math
8(k-L_0)\in G_1.
```

For every fitting offset, the nonnegative coordinate `8(k-L_0)` lies below `R_0`. Therefore it belongs to `G_1` exactly when it belongs to the original unshifted anchor set. Apart from the sponsor-incompatible value `k=L_0`, the condition is

```math
\boxed{
8(k-L_{10})\in S_{10}.
}
```

There are exactly two sponsor-compatible offsets:

```text
603979776
613416960
```

with hashes

```text
FNV-64  91e961fb57e2e687
SHA-256 ae93a9f5f94348348c156b29e75074a61097723d2d98bd497629c3df5a16ba4f
```

They are disjoint from both the first- and second-step half-obstruction classes.

---

## 6. Later half obstructions are impossible

At the next scheduled generation, the raw half-separation coordinate is

```math
32k.
```

The fitting exact range satisfies

```math
k<2L_{10},
```

so

```math
32k<64L_{10}=L_2.
```

The smallest positive point of the relevant raw parent is `L_2`. Hence the next half-separation obstruction is impossible.

The normalized offset halves thereafter, so every later half obstruction is also impossible. Completion descent and the invariant nine-pattern classification then continue indefinitely.

---

## 7. Complete basin count

The already-valid exact-child family has size

```math
408855759.
```

The second and third scheduled half classes contain

```text
88614 and 2 offsets,
```

with `8` overlaps between the second class and the first-step half class already removed from the valid-child family. Therefore the number of additional failures among valid exact children is

```math
88614+2-8=88608.
```

Hence

```math
\boxed{
408855759-88608
=
408767151
}
```

valid exact children enter infinite exact factor-eight tails.

The exact coverage fraction is

```math
\boxed{
\frac{408767151}{408855759}
=
\frac{10481209}{10483481}
}
```

or approximately

```text
99.9783278092458%.
```

Only

```math
\boxed{88608}
```

valid exact children remain outside this scheduled basin certificate.

The additional-obstruction list has hashes

```text
FNV-64  bd7c3b1c8c99b586
SHA-256 87e998e9e425e84c934ddb9c205ab4d934cd1af9f832662e7436595a66fae122
```

---

## 8. Terminal charge

Every certified tail begins at the same state `S_10`, with

```math
N=265719,
\qquad
P=1024,
\qquad
L=536870912.
```

Therefore every tail has total multiplicity-weighted density

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{4P(N+1)}L
=
\frac{33215}{16384}.
}
```

The charge is independent of the valid entry offset.

---

## 9. Scope

This theorem nearly classifies the entire valid exact factor-eight child family of `S_10` into explicit infinite summable tails.

It does not yet classify:

1. the `88608` valid exact children failing a scheduled half test;
2. factor-two or factor-four cheap escape candidates from `S_10`;
3. the full continuation tree.

The immediate exact-child target is now the finite exceptional set of `88608` valid offsets. The broader problem remains whole-tree Bellman compensation.
