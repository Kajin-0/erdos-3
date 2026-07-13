# Exact zero-novelty coordinated schedule on `S_2`

## Status

Exact finite computer-assisted witness.

The deterministic lexicographic schedule previously recorded for `S_2` has positive middle-fiber support outside the minimum-translation backbone. That value is not schedule invariant. This note gives a different valid coordinated deletion schedule for which every middle-fiber label is already contained in the backbone.

Consequently, the minimum novel-fiber mass over all coordinated schedules on `S_2` is exactly zero.

**Verifier:** `src/verify_s2_zero_novelty_schedule.py`.

**Certificate:** `data/s2_zero_novelty_schedule_certificate_2026-07-13.txt`.

---

## 1. Novel-fiber coordinate

For a coordinated deletion schedule `sigma` on a parent state `D`, let

```math
\Xi_q^{\sigma}
=
\{x-\min X_q^{\sigma}:x\in X_q^{\sigma},\ x>\min X_q^{\sigma}\}
```

be the exact middle multiplicity fiber for selected step `q`. Define

```math
F_{\sigma}(D)
=
\bigcup_q\Xi_q^{\sigma}
```

and

```math
\mathcal N_{\sigma}(D)
=
H\left(F_{\sigma}(D)\setminus\mathcal B(D)\right),
```

where

```math
\mathcal B(D)
=
\{d-\min D:d\in D,\ d>\min D\}
```

is the minimum-translation backbone.

The quantity is nonnegative for every schedule. Therefore one explicit schedule with value zero proves

```math
\min_{\sigma}\mathcal N_{\sigma}(D)=0.
```

---

## 2. Parent state

The recorded second state satisfies

```math
S_2\subseteq[256,512),
\qquad
|S_2|=39,
\qquad
\max S_2=470.
```

Its canonical SHA-256 hash is

```text
cff7a986bfeb8def36b5597655a585f261f8a58facdb1ee9339d72a9eaa78e37
```

and its backbone has `38` labels.

---

## 3. Explicit coordinated schedule

The verifier checks the following `22` progressions in order. For each step `q`, the coordinated rule deletes the left endpoint when `v_2(q)` is even and the right endpoint when `v_2(q)` is odd.

| time | left | middle | right | step | sponsor |
|---:|---:|---:|---:|---:|---:|
| 1 | 338 | 342 | 346 | 4 | 338 |
| 2 | 346 | 403 | 460 | 57 | 346 |
| 3 | 256 | 317 | 378 | 61 | 256 |
| 4 | 463 | 464 | 465 | 1 | 463 |
| 5 | 460 | 464 | 468 | 4 | 460 |
| 6 | 337 | 398 | 459 | 61 | 337 |
| 7 | 348 | 409 | 470 | 61 | 348 |
| 8 | 397 | 403 | 409 | 6 | 409 |
| 9 | 402 | 403 | 404 | 1 | 402 |
| 10 | 336 | 397 | 458 | 61 | 336 |
| 11 | 442 | 443 | 444 | 1 | 442 |
| 12 | 458 | 464 | 470 | 6 | 470 |
| 13 | 381 | 382 | 383 | 1 | 381 |
| 14 | 341 | 403 | 465 | 62 | 465 |
| 15 | 320 | 321 | 322 | 1 | 320 |
| 16 | 399 | 403 | 407 | 4 | 399 |
| 17 | 342 | 403 | 464 | 61 | 342 |
| 18 | 347 | 403 | 459 | 56 | 459 |
| 19 | 321 | 382 | 443 | 61 | 321 |
| 20 | 322 | 383 | 444 | 61 | 322 |
| 21 | 347 | 408 | 469 | 61 | 347 |
| 22 | 398 | 403 | 408 | 5 | 398 |

Every selected progression is present at its deletion time. The terminal residual is

```math
\{317,341,343,378,382,383,397,403,404,407,408,443,444,458,464,468,469\}
```

and is three-term-progression-free.

The canonical schedule SHA-256 is

```text
75409bc254f8ac850880dbd9a83276fb6b454f2bd064aef2a5e96bc7bb74dac8
```

---

## 4. Exact middle fibers

The selected step set is

```math
Q=\{1,4,5,6,56,57,61,62\}.
```

The nonempty fibers are

```math
\Xi_1=\{61,82,122,143\},
```

```math
\Xi_4=\{61,122\},
```

```math
\Xi_6=\{61\},
```

and

```math
\Xi_{61}=\{65,66,80,81,86,91,92\}.
```

The fibers for `q=5,56,57,62` are empty. Hence

```math
F_{\sigma}(S_2)
=
\{61,65,66,80,81,82,86,91,92,122,143\}.
```

The verifier checks the exact containment

```math
\boxed{
F_{\sigma}(S_2)
\subseteq
\mathcal B(S_2).
}
```

Therefore

```math
\boxed{
\mathcal N_{\sigma}(S_2)=0.
}
```

Since novel mass is nonnegative for every schedule,

```math
\boxed{
\min_{\sigma}\mathcal N_{\sigma}(S_2)=0.
}
```

---

## 5. Consequence for reserve design

The earlier lexicographic schedule has

```math
\mathcal N_{\mathrm{lex}}(S_2)
=
\frac{239396453}{200655312}>0,
```

while the schedule above has value zero. Thus the parent set `S_2` alone does not determine the novel-fiber coordinate.

The following proposed use is therefore invalid without an additional schedule convention or theorem:

```text
Treat novel fiber mass as a schedule-independent reserve stored by the parent.
```

The schedule-robust lower envelope also fails at the first recorded descendant:

```math
\inf_{\sigma}\mathcal N_{\sigma}(S_2)=0.
```

A viable continuation must instead do at least one of the following:

1. specify a constructive deletion policy and prove that its exported obstruction mass pays the Bellman debt;
2. optimize the schedule as part of the proof and control the resulting choices across the full tree;
3. replace raw novelty by a parent-intrinsic obstruction coordinate that cannot be erased by changing the schedule;
4. prove a packing theorem that charges imported fibers even when no new numerical labels appear.

The computation does not decide which alternative is sufficient.

---

## 6. Reproduction

Run

```bash
python3 src/verify_s2_zero_novelty_schedule.py \
  /tmp/s2_zero_novelty_schedule_certificate.txt
```

The recorded certificate has SHA-256

```text
e5d7a3bbefea78c7c5eeb85ec9155e947d00443e8c279ba6cfc72978267bf972
```

and is included in the lightweight proof-check workflow.

---

## 7. Scope

This result proves only the exact minimum for the finite parent `S_2`. It does not prove:

- that every parent has a zero-novelty schedule;
- that maximum or average novelty is small;
- that a canonical schedule cannot export useful reserve;
- a global overlap quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.
