# Parent-intrinsic forced-fork reserve through `S_7`

## Status

Exact finite computer-assisted theorem with a general combinatorial lemma.

A coordinated deletion action is a three-term progression together with its valuation-determined side sponsor. An initial progression is **root-forced** when its own action is the only initial action whose sponsor lies in that progression.

Every complete coordinated deletion schedule must select every root-forced progression. Repeated forced centers with the same step therefore create unavoidable middle-fiber occurrence mass independent of the later schedule.

**Verifier:** `src/verify_forced_fork_reserve_s1_s7.py`.

**Certificate:** `data/forced_fork_reserve_s1_s7_certificate_2026-07-13.txt`.

---

## 1. Root-forced fork lemma

For a parent state `D`, let `A_x(D)` be the set of initial coordinated actions whose sponsor is `x`. A progression

```math
P=\{a,b,c\}
```

is root-forced when

```math
\boxed{
\mathcal A_a(D)\cup\mathcal A_b(D)\cup\mathcal A_c(D)=\{P\}.
}
```

Deletion only removes points, so every later action was already an initial action. If a complete schedule never selected `P`, no point of `P` could be deleted. The terminal residual would still contain `P`, contradicting three-term-progression-freeness. Hence every complete schedule selects `P`.

---

## 2. Parent-intrinsic reserve

For each step `q`, let `Y_q(D)` be the centers of root-forced progressions having step `q`. Every complete schedule `sigma` has selected-center set

```math
Y_q(D)\subseteq X_q^\sigma.
```

Because the actual minimum center may come from an additional selected progression, define

```math
\psi_q(D)
=
\min_{
 m\in C_q(D),
 m\le\min Y_q(D)
}
\sum_{
 y\in Y_q(D),
 y>m
}
\frac1{y-m},
```

where `C_q(D)` is the set of all initially possible centers with step `q`. Put

```math
\boxed{
\Psi(D)=\sum_q\psi_q(D).
}
```

Then every complete coordinated schedule satisfies

```math
\boxed{
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
}
```

The quantity `Psi(D)` is determined by the parent state and coordinated sponsor rule, not by the later deletion order.

---

## 3. Exact recorded frontier

| state | initial actions | root-forced actions | compact exact lower bound for `Psi` |
|---:|---:|---:|---:|
| `S_1` | 9 | 3 | `1/21` |
| `S_2` | 60 | 5 | `1/18` |
| `S_3` | 398 | 9 | `1/51` |
| `S_4` | 2,195 | 12 | `1/200` |
| `S_5` | 11,523 | 19 | `1/624` |
| `S_6` | 58,708 | 28 | `1/4321` |
| `S_7` | 298,606 | 30 | `1/14046` |

The verifier stores and checks the exact rational reserve at every depth, along with canonical SHA-256 hashes of the forced-action families.

The exact `S_6` and `S_7` values are positive but substantially smaller than the earlier values. This confirms that positivity alone is not enough; the closing theorem needs scale compensation and bounded reuse.

---

## 4. Novelty-or-overlap identity

For one complete schedule, define novel support mass

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus\mathcal B(D)
\right)
```

and simultaneous overlap charge

```math
\Omega_\sigma(D)
=
H(\mathcal B(D))
+
\sum_qH(\Xi_q^\sigma)
-
H\left(
\mathcal B(D)\cup\bigcup_q\Xi_q^\sigma
\right),
```

with repeated middle-fiber occurrences included in the overlap accounting. Then

```math
\boxed{
\mathcal N_\sigma(D)+\Omega_\sigma(D)
=
\sum_qH(\Xi_q^\sigma)
\ge
\Psi(D).
}
```

Thus every schedule exports either new numerical support or certified overlap with simultaneous recursive output. The unresolved issue is whether this charge can be reused across descendants without a bounded packing cost.

---

## 5. Bellman limitation

The feature

```math
P\Psi(S)
```

is not a standalone stored Bellman potential. It increases across the recorded factor-four transition `S_1 -> S_2`, while that transition creates positive debt. The exact no-go is documented in `docs/forced-fork-bellman-no-go.md`.

The forced-fork reserve remains useful only as:

1. a guaranteed transition output feeding a packing theorem;
2. a seed for obstruction or rectangle growth;
3. one component of a larger potential with completion, target-demand, and overlap coordinates.

---

## 6. Active theorem target

The current target is a scale-compensated packing inequality preventing repeated payment by the same forced-fork labels. A useful form would compare the complete simultaneous child family:

```math
\sum_{S'\in\operatorname{Child}(S)}
\operatorname{Pack}(S')
+
\text{new obstruction charge}
\le
\operatorname{Pack}(S)
+
C\,P\Psi(S)
+
\text{controlled error}.
```

The finite certificate supplies the unavoidable local input. It does not supply the cross-generation packing theorem.

---

## 7. Reproduction

Run

```bash
python3 src/verify_forced_fork_reserve_s1_s7.py \
  /tmp/forced_fork_reserve_s1_s7_certificate.txt
```

The recorded certificate SHA-256 is

```text
032307354597d531340a4dc87c9646a9b4bde6b6f7f7cc2a427719cbe7be8190
```

and the check is included in `src/run_verify_transport_reserve.sh`.

---

## 8. Scope

The root-forced lemma is general, but the numerical values are finite computations for `S_1,...,S_7`. This result does not prove:

- a uniform lower bound for arbitrary parents;
- monotonicity of `Psi`;
- bounded cross-generation reuse;
- a complete child-packing inequality;
- a branching Bellman theorem;
- or the four-term Erdős conjecture.
