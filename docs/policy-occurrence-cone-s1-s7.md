# Common occurrence-weight policy cone through `S_7`

## Status

Exact finite policy-ranking theorem for the recorded deterministic schedules.

Define

```math
C_\lambda(\pi)=T_\pi+\lambda O_\pi+E_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, and `E` is normalized terminal-residual error.

**Verifier:** `src/verify_policy_occurrence_cone_s1_s7.py`.

**Certificate:** `data/policy_occurrence_cone_s1_s7_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
4d1e8eae67c474dee651bcee35397c84906c0216649ddfe7794529c1d990d907
```

---

## 1. Exact upper boundary from `S_1`

On `S_1`, reverse lexicographic deletion has larger terminal mass but smaller occurrence mass than lexicographic deletion. Exact arithmetic gives

```math
C_\lambda(\mathrm{reverse})-C_\lambda(\mathrm{lex})>0
\quad\Longleftrightarrow\quad
\lambda<\frac{260}{63}.
```

At the witness weight `lambda=3`, the exact difference is

```math
\frac{71}{624}>0.
```

Thus `S_1` imposes the finite upper boundary

```math
\lambda<\frac{260}{63}\approx4.12698.
```

---

## 2. `S_2` through `S_6`

For every recorded state `S_2,...,S_6`, reverse lexicographic deletion has:

1. larger terminal-step harmonic mass;
2. larger middle-fiber occurrence mass;
3. no smaller residual error.

Therefore lexicographic deletion is cheaper for every nonnegative occurrence weight `lambda` on these six tested comparisons. In particular, the exact score differences at `lambda=3` are positive.

---

## 3. `S_7` targeted policy

At `S_7`, the delayed-seed policy is cheaper than lexicographic deletion exactly when

```math
\lambda>\lambda_*,
```

where the previously certified threshold satisfies

```math
\lambda_*<\frac{477}{200}=2.385.
```

Reverse lexicographic deletion remains more expensive than lexicographic deletion at `lambda=3`.

Combining the `S_1` upper boundary with the `S_7` lower boundary gives the certified nonempty subcone

```math
\boxed{
\frac{477}{200}<\lambda<\frac{260}{63}
}.
```

The rational witness

```math
\boxed{\lambda=3}
```

lies in this interval. Under `C_3`, the tested policy choice is:

```text
S1-S6: lexicographic
S7:    delayed-seed
```

and reverse lexicographic deletion is rejected on every `S_1,...,S_7` comparison.

---

## 4. Scope

This is the first exact common policy-weight interval spanning the recorded states. It shows that the `S_7` delayed-seed improvement is compatible with the earlier-state lexicographic choices under one fixed coefficient.

It does **not** prove:

- that `C_lambda` is a valid retained-child Bellman potential;
- that these schedules are globally optimal among all complete coordinated schedules;
- that the same interval survives additional deterministic policies;
- or that the provenance-preserving retention quotient exists.

The next exact task is to add additional policy families and intersect their rational half-spaces. A first infeasible subsystem would identify the missing coordinate required by the whole-tree potential.
