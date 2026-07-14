# Retained terminal/recursive split

## Status

Exact finite theorem for the certified second-generation retained family.

The underlying transition is unchanged:

- `local37` first-generation policy;
- the unique `21`-state point-disjoint retained family;
- lexicographic coordinated deletion on every retained state;
- global exact-state quotienting and maximum-harmonic same-shell conflict selection;
- the resulting `27` retained second-generation states.

The new step separates states that are already three-term-progression-free from states that still require recursive coordinated deletion.

**Verifier:** `src/verify_retained_terminal_split.py`.

**Certificate:** `data/retained_terminal_split_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
9027800d0646568eea1d673d7dd597bf3d5129837f79006452e6e33c984d96ff
```

---

## 1. Exact split

The `27` retained states divide into:

| class | states | labels |
|---|---:|---:|
| terminal, three-term-progression-free | `13` | `43` |
| recursive, contains a three-term progression | `14` | `7,882` |

The terminal states have no coordinated-deletion action and therefore produce no further middle-fiber or backbone children under the recursive rule.

Their exact state-family hashes are:

```text
terminal:  0aa2aca9246119f832bb3b58dcc090683c41fb85ed3c47d5c73d0b398dfc672e
recursive: 925220ccdebe7629cdbe480752b6525d7b06bf794922b1573b7b93ef0064d47d
```

---

## 2. The apparent expansion is terminal

Let

```math
H_1=\text{first-generation retained harmonic mass},
```

```math
H_2^{\rm term}=\text{terminal second-generation mass},
\qquad
H_2^{\rm rec}=\text{recursive second-generation mass}.
```

The earlier result was

```math
6.828
<
\frac{H_2^{\rm term}+H_2^{\rm rec}}{H_1}
<
6.829.
```

The split shows that terminal states contribute

```math
0.862
<
\frac{H_2^{\rm term}}{H_2^{\rm term}+H_2^{\rm rec}}
<
0.863.
```

Only

```math
0.137
<
\frac{H_2^{\rm rec}}{H_2^{\rm term}+H_2^{\rm rec}}
<
0.138
```

belongs to states that continue recursively.

Most importantly,

```math
\boxed{
0.937
<
\frac{H_2^{\rm rec}}{H_1}
<
0.938.
}
```

Thus the recursive retained branch contracts by

```math
\boxed{
0.062
<
\frac{H_1-H_2^{\rm rec}}{H_1}
<
0.063.
}
```

This is the first exact two-generation contraction of the genuinely recursive retained branch for the adversarial `S_7` transition.

---

## 3. Extreme scale contraction is predominantly terminal

The scale-profile certificate identified `196` retained points with

```math
\left\lfloor\log_2(p/u)\right\rfloor\ge8.
```

Only `42` of those points are in terminal states, but they carry between `91.3%` and `91.4%` of the harmonic mass in that scale tail. The recursive portion of the depth-eight tail contributes only

```math
0.081
<
\frac{H_2^{\rm rec}[d_-\ge8]}{H_2}
<
0.082.
```

All four points with at least sixteen binary orders of contraction are terminal. The single point

```text
u = 1,
p = 1,354,066
```

is terminal as well. It contributes more than half of total second-generation retained mass, but it creates no recursive descendant.

---

## 4. Interpretation

The previous scale analysis correctly located the harmonic expansion at repeated provenance and extreme contraction. The terminal split identifies its role in the recursion:

```text
extreme repeated-provenance contraction -> terminal sink mass,
not persistent recursive load.
```

The full `6.828`–`6.829` ratio should therefore not be used as the recursive Bellman debt. The correct recursive comparison on this transition is the `0.937`–`0.938` ratio.

The remaining issue is global terminal accounting. A three-term-progression-free retained state is safe from further coordinated deletion, but its harmonic mass must still be charged exactly once across the whole branching construction. Exact-state quotienting and point-disjoint retention solve this within the recorded two-generation family; a general theorem must prevent terminal sink mass from being recreated or counted repeatedly across deeper branches.

This result does not prove a universal contraction. It is a fixed-policy, fixed-retention, two-generation theorem on the certified `S_7` transition.
