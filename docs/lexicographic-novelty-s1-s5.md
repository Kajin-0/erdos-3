# Canonical lexicographic novelty through `S_5`

## Status

Exact finite computer-assisted reference for one constructive coordinated deletion policy.

The schedule-dependent zero-novelty witness on `S_2` proves that novel middle-fiber mass is not an intrinsic feature of the parent state. That does not prevent a proof from choosing a fixed deletion policy. This note tests the simplest canonical choice on the recorded contaminated genealogy.

At every current state, order all available three-term progressions by

```text
(step, left endpoint, middle, right endpoint)
```

and select the smallest tuple. Delete the coordinated side sponsor determined by the parity of `v_2(step)`.

The exact computation shows:

```text
S1: novel support 0
S2: novel support 8,   novel harmonic mass > 1193/1000
S3: novel support 57,  novel harmonic mass > 7/5
S4: novel support 173, novel harmonic mass > 29/20
S5: novel support 602, novel harmonic mass > 149/100
```

Thus the canonical policy exports positive obstruction support on every recorded state from `S_2` through `S_5`, even though another valid schedule on `S_2` exports none.

**Verifier:** `src/verify_lexicographic_novelty_s1_s5.py`.

**Certificate:** `data/lexicographic_novelty_s1_s5_certificate_2026-07-13.txt`.

---

## 1. Exact policy

For a parent state `D`, initialize the set of every nontrivial progression

```math
(a,a+q,a+2q)\subseteq D.
```

Order these by

```math
(q,a,a+q,a+2q).
```

At each deletion time, discard tuples containing a previously deleted point and choose the first remaining tuple. Delete

```math
a
```

when `v_2(q)` is even and

```math
a+2q
```

when `v_2(q)` is odd.

Because deletion only removes points, the initial ordered progression list is sufficient; no new progression can appear later.

For the selected centers `X_q`, define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Let

```math
F(D)=\bigcup_q\Xi_q
```

and split it into imported and novel support relative to

```math
\mathcal B(D)
=
\{d-\min D:d\in D,\ d>\min D\}.
```

---

## 2. Exact finite ledger

| state | size | deletions | residual | distinct steps | fiber occurrences | fiber union | imported | novel |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `S_1` | 12 | 6 | 6 | 2 | 4 | 4 | 4 | 0 |
| `S_2` | 39 | 26 | 13 | 5 | 21 | 18 | 10 | 8 |
| `S_3` | 120 | 92 | 28 | 10 | 82 | 59 | 2 | 57 |
| `S_4` | 363 | 305 | 58 | 11 | 294 | 206 | 33 | 173 |
| `S_5` | 1092 | 974 | 118 | 12 | 962 | 678 | 76 | 602 |

At every depth the verifier checks the exact middle-multiplicity identity

```math
|Q|+\sum_q|\Xi_q|=K,
```

where `K` is the number of deletions.

The novel-support fractions among deleted progressions are

```text
S2: 8/26
S3: 57/92
S4: 173/305
S5: 602/974
```

so the recorded policy does not merely produce one isolated novel label.

---

## 3. Exact harmonic lower bounds

The verifier computes the novel harmonic mass with exact `Fraction` arithmetic and certifies

```math
H(F(S_2)\setminus\mathcal B(S_2))
>
\frac{1193}{1000},
```

```math
H(F(S_3)\setminus\mathcal B(S_3))
>
\frac75,
```

```math
H(F(S_4)\setminus\mathcal B(S_4))
>
\frac{29}{20},
```

and

```math
H(F(S_5)\setminus\mathcal B(S_5))
>
\frac{149}{100}.
```

These are compact certified lower bounds, not decimal approximations used internally by the verifier.

---

## 4. Interpretation

Two finite facts now coexist:

1. `S_2` admits a coordinated schedule with zero novel support;
2. the canonical lexicographic policy has positive novel support on `S_2,S_3,S_4,S_5`.

Therefore the correct distinction is

```text
parent-intrinsic reserve: false for raw novelty;
policy-dependent exported reserve: still viable.
```

A proof using this route must include the deletion policy as part of the recursive state or prove that the policy is compatible with the full simultaneous child family. It cannot compute novelty from the parent set while leaving the schedule unspecified.

The finite data suggest a concrete next theorem target:

```math
\boxed{
\text{Under a fixed constructive policy, exported obstruction mass either pays cheap-step debt or forces bounded-overlap descendants.}
}
```

The current computation does not establish such an inequality. In particular, positive parent novelty alone does not control the novelty or overlap potential of every simultaneous child.

---

## 5. Reproduction

Run

```bash
python3 src/verify_lexicographic_novelty_s1_s5.py \
  /tmp/lexicographic_novelty_s1_s5_certificate.txt
```

The recorded certificate SHA-256 is

```text
6fe0b27e20284a93ef13c4a738122c4889432c2e673d63794ccec6a7ba36c2e1
```

and the check is included in `src/run_verify_transport_reserve.sh`.

---

## 6. Scope

This result is a finite policy reference. It does not prove:

- a uniform lower bound for arbitrary four-term-progression-free parents;
- positive novelty for every schedule;
- a monotone policy-dependent potential;
- bounded overlap among simultaneous descendants;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.
