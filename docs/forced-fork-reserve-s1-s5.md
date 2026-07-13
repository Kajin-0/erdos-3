# Parent-intrinsic forced-fork reserve through `S_5`

## Status

Exact finite computer-assisted theorem with a general combinatorial lemma.

The earlier novelty calculations depend on the deletion schedule. This note identifies a schedule-independent structure visible directly in the parent state: **root-forced coordinated forks**.

A root-forced progression must be selected in every complete coordinated deletion schedule. Repeated forced centers with the same step therefore create unavoidable middle-fiber occurrence mass, independent of how the remaining schedule is chosen.

For the recorded states `S_1,...,S_5`, this gives positive parent-intrinsic lower bounds:

```text
S1: reserve = 1/21
S2: reserve = 388668/6990295 > 1/18
S3: reserve > 1/51
S4: reserve > 1/200
S5: reserve > 1/624
```

**Verifier:** `src/verify_forced_fork_reserve_s1_s5.py`.

**Certificate:** `data/forced_fork_reserve_s1_s5_certificate_2026-07-13.txt`.

---

## 1. Coordinated actions

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Every three-term progression

```math
P=(a,a+q,a+2q)\subseteq D
```

defines one coordinated deletion action. Its sponsor is

```math
a
```

when `v_2(q)` is even and

```math
a+2q
```

when `v_2(q)` is odd.

Write

```math
s(P)
```

for the sponsor and let

```math
\mathcal A_x(D)
=
\{P:s(P)=x\}
```

be the initial actions capable of deleting point `x`.

---

## 2. Root-forced fork lemma

Call an initial progression

```math
P=\{a,b,c\}
```

**root-forced** when

```math
\boxed{
\mathcal A_a(D)
\cup
\mathcal A_b(D)
\cup
\mathcal A_c(D)
=
\{P\}.
}
```

In words, the action `P` itself is the only initial coordinated action whose sponsor lies in `P`.

### Lemma

Every complete coordinated deletion schedule on `D` selects every root-forced progression.

### Proof

Deletion only removes points, so every progression available later was already present in the initial state. Therefore every later action capable of deleting a point of `P` belongs to

```math
\mathcal A_a(D)
\cup
\mathcal A_b(D)
\cup
\mathcal A_c(D).
```

For a root-forced progression this union is `{P}`. If the schedule never selects `P`, no point of `P` is ever deleted. Then `P` remains in the terminal residual, contradicting that the residual is three-term-progression-free. Hence `P` must be selected. `square`

This lemma is state-independent. The finite verifier enumerates the root-forced family for the recorded states.

---

## 3. Forced-center reserve

For each step `q`, let

```math
Y_q(D)
```

be the set of centers of root-forced progressions having step `q`. Every complete schedule `sigma` has a selected-center set

```math
X_q^\sigma
```

with

```math
Y_q(D)\subseteq X_q^\sigma.
```

The actual middle fiber is

```math
\Xi_q^\sigma
=
\{x-\min X_q^\sigma:x\in X_q^\sigma,\ x>\min X_q^\sigma\}.
```

The minimum center need not be forced. Let

```math
C_q(D)
```

be the set of every initially possible center with step `q`. Since

```math
m_q^\sigma=\min X_q^\sigma
```

belongs to `C_q(D)` and satisfies

```math
m_q^\sigma\le\min Y_q(D),
```

define

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
\frac1{y-m}.
```

Additional selected centers only add nonnegative fiber occurrence mass. Therefore every complete schedule satisfies

```math
\boxed{
\sum_q H(\Xi_q^\sigma)
\ge
\Psi(D),
}
```

where

```math
\boxed{
\Psi(D)=\sum_q\psi_q(D).
}
```

The quantity `Psi(D)` is determined by the initial parent state and the fixed coordinated sponsor rule. It does not depend on the later schedule.

---

## 4. Exact recorded values

| state | initial 3-AP actions | root-forced actions | exact reserve `Psi` | compact lower bound |
|---:|---:|---:|---:|---:|
| `S_1` | 9 | 3 | `1/21` | `1/21` |
| `S_2` | 60 | 5 | `388668/6990295` | `1/18` |
| `S_3` | 398 | 9 | `3364354489728494/168888762232172073` | `1/51` |
| `S_4` | 2195 | 12 | `16247372897720390023737791/3235490759356665773610042000` | `1/200` |
| `S_5` | 11523 | 19 | `15118361448154886467381751180403762551053086996176904193/9431956663304181282890330139658074870057520957610192175360` | `1/624` |

The compact lower bounds are exact rational comparisons checked by the verifier.

---

## 5. Examples

### `S_1`

The forced centers with step `1` are

```math
65,86.
```

No initially possible step-`1` center lies below `65`, so every schedule has

```math
H(\Xi_1)\ge\frac1{86-65}=\frac1{21}.
```

This recovers the exact exhaustive overlap floor.

### `S_2`

The forced step-`61` centers are

```math
317,382,403.
```

The smallest possible step-`61` center is `317`, giving

```math
\psi_{61}(S_2)
=
\frac1{65}+\frac1{86}
=
\frac{151}{5590}.
```

The forced step-`1` centers are

```math
382,403.
```

An additional selected step-`1` center can move the actual minimum as low as `321`. Minimizing over every possible minimum gives

```math
\psi_1(S_2)
=
\frac1{61}+\frac1{82}
=
\frac{143}{5002}.
```

Hence

```math
\Psi(S_2)
=
\frac{151}{5590}
+
\frac{143}{5002}
=
\frac{388668}{6990295}
>
\frac1{18}.
```

This lower bound holds for the lexicographic schedule, the zero-novelty witness, and every other complete coordinated schedule.

---

## 6. Relation to novelty and overlap

For one schedule define

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus
\mathcal B(D)
\right)
```

and the simultaneous overlap charge

```math
\Omega_\sigma(D)
=
H(\mathcal B(D))
+
\sum_qH(\Xi_q^\sigma)
-
H\left(
\mathcal B(D)\cup\bigcup_q\Xi_q^\sigma
\right).
```

The identity

```math
\boxed{
\mathcal N_\sigma(D)+\Omega_\sigma(D)
=
\sum_qH(\Xi_q^\sigma)
}
```

holds after the overlap term includes both imported support and repeated occurrence mass.

Therefore the forced-fork reserve gives the schedule-independent dichotomy

```math
\boxed{
\mathcal N_\sigma(D)+\Omega_\sigma(D)
\ge
\Psi(D).
}
```

This is the first parent-intrinsic positive reserve coordinate in the current deletion-DAG experiments. It remains an occurrence/overlap quantity, not yet a globally chargeable Bellman potential.

---

## 7. Active theorem target

The remaining step is no longer merely to find positive local reserve. It is to prove that forced-fork reserve cannot be paid repeatedly by the same numerical labels across descendants.

A useful target is a packing inequality of the form

```math
\boxed{
\sum_{S'\in\operatorname{Child}(S)}
\Psi(S')
+
\text{new obstruction charge}
\le
C\,\Psi(S)
+
\text{controlled error},
}
```

or a modified potential combining `Psi` with rectangle/completion deficits.

The finite values decay along the recorded states, so `Psi` alone is unlikely to pay every Bellman debt without additional scale normalization or obstruction coordinates.

---

## 8. Reproduction

Run

```bash
python3 src/verify_forced_fork_reserve_s1_s5.py \
  /tmp/forced_fork_reserve_s1_s5_certificate.txt
```

The recorded certificate SHA-256 is

```text
6941672cbe66bccd211f672eb5636440e63e7b3d36fb6063361dfbdc9922da27
```

and the check is included in `src/run_verify_transport_reserve.sh`.

---

## 9. Scope

The root-forced fork lemma is general, but the listed reserve values are finite computations for `S_1,...,S_5`. This result does not prove:

- a uniform lower bound for arbitrary parent states;
- that `Psi` is monotone;
- bounded cross-generation reuse of forced centers;
- a complete branching transition inequality;
- a Carleson packing theorem;
- or the four-term Erdős conjecture.
