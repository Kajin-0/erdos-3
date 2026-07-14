# Exact pair-energy Bellman row at the fifth retained frontier

## Status

Exact finite theorem for the certified baseline transition from the twelve fourth-generation recursive retained states to the complete fifth retained family.

No sixth-generation state is constructed or used.

The theorem combines:

- the fixed `local37` first-generation policy;
- lexicographic recursive continuation;
- exact-state quotienting;
- componentwise maximum-harmonic same-shell retention;
- original root provenance;
- the symbolic affine pivot pair-energy theorem.

Primary files:

- `src/probe_pair_energy_frontier.py`;
- `src/verify_pair_energy_frontier.py`;
- `data/pair_energy_frontier_certificate_2026-07-14.txt`.

---

## 1. Pair energy

For a retained state whose distinct original root labels form `P`, define

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

For a family of states, occurrence-valued pair energy sums `J(P)` over state occurrences. Union-valued pair energy counts each root-pair token only once.

At both recorded recursive frontiers in this theorem, root sets are globally disjoint. Therefore every root and every root pair has multiplicity one, and occurrence-valued and union-valued pair energy agree exactly.

---

## 2. Fourth recursive frontier

The fourth recursive family has:

```text
12 states
1,717 points
1,717 distinct root labels
maximum root multiplicity 1
370,505 pair occurrences
370,505 distinct root pairs
maximum pair multiplicity 1
12 affine states
0 non-affine states.
```

Its harmonic mass is

```text
H(R4) = 1.536133538213...
```

and its exact pair energy is

```text
J(R4) = 2743.858245303490...
```

The equality

```math
370505
=
\sum_{S\in R_4}\binom{|S|}{2}
```

is recorded and certified.

---

## 3. Fifth retained output

The complete fifth retained family has:

| type | states | points | harmonic mass |
|---|---:|---:|---:|
| terminal | `8` | `17` | `2.043863226048...` |
| recursive | `13` | `1015` | `2.042771729559...` |
| total | `21` | `1032` | `4.086634955606...` |

The fifth recursive family has:

```text
1,015 distinct root labels
maximum root multiplicity 1
106,381 pair occurrences
106,381 distinct root pairs
maximum pair multiplicity 1
13 affine states
0 non-affine states.
```

Its exact pair energy is

```text
J(R5) = 1582.379988513372...
```

No repeated pair energy is present on either side of the transition.

---

## 4. Exact Bellman row

The complete fifth output satisfies

```math
\boxed{
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4^{\rm rec}).
}
```

The certified values are

```text
left  = H(F5) + J(R5_recursive)
      = 1586.466623468978...

right = J(R4_recursive)
      = 2743.858245303490...
```

with exact surplus

```text
right - left
= 1157.391621834512...
```

and ratio

```math
\boxed{
\frac{H(F_5)+J(R_5^{\rm rec})}
     {J(R_4^{\rm rec})}
=0.578188259610\ldots<1.
}
```

Thus only `57.8189%` of the available fourth-generation root-pair capacity remains as fifth output mass plus future recursive pair capacity.

This row is exact in both occurrence and union conventions because pair multiplicity is one.

---

## 5. Why raw harmonic expansion is not a contradiction

Recursive harmonic mass alone expands:

```math
\frac{H(R_5)}{H(R_4)}
=1.329813898820\ldots.
```

But the correct affine potential is not raw harmonic mass. It is harmonic output plus unused root-pair energy.

The transition consumes

```text
J(R4) - J(R5) = 1161.478256790118...
```

of pair energy while emitting

```text
H(F5) = 4.086634955606...
```

of retained harmonic output. The pair-energy decrease is therefore much larger than the harmonic expansion.

The previously failing transition is strongly contractive in the pair potential.

---

## 6. Structural interpretation

Every retained affine point `u` with root provenance `p` has a reference root

```math
r=p-u
```

and consumes the pair token `(r,p)` of weight `1/u`.

At this frontier:

- every recursive state is affine;
- every root belongs to one state;
- every latent pair belongs to one state;
- the fifth complete harmonic output and the fifth recursive latent pairs fit inside the fourth latent pair set with large surplus.

This is the first legitimate retained-child Bellman row in the repository whose potential has:

1. a state-independent symbolic definition;
2. a treewise pair-packing theorem;
3. exact finite verification on the adversarial transition;
4. no fitted coefficients.

---

## 7. What this closes

The result closes the local fourth-to-fifth failure for the certified baseline transition.

In particular, the failure of

```math
H+kR
```

for every finite `k` does not rule out a Bellman potential. Current-generation repeated-root mass was the wrong reserve. Root-pair energy stores the future affine pivot opportunities that remain after root multiplicity has fallen to one.

---

## 8. What remains open

This theorem does not prove:

- that the earlier retained generations are entirely affine;
- that pair multiplicity is controlled before generation four;
- that the same retained quotient is globally optimal;
- that every policy admits a pair-energy row;
- that entering pair energy is bounded by parent harmonic mass;
- that non-affine middle-fiber output is terminal or negligible;
- a whole-tree Bellman inequality from the original dyadic block;
- or the four-term reciprocal-sum theorem.

The next bottleneck is now sharply defined:

```math
\boxed{
\text{transport into the affine pair-energy regime}
+
\text{control of pair-token reuse before uniqueness.}
}
```

The correct earlier-generation diagnostics are:

1. affine-state coverage;
2. occurrence versus union pair energy;
3. maximum pair-token multiplicity;
4. first-appearance versus reused `(u,p)` mass;
5. pair-energy rows across `R_1 -> F_2`, `R_2 -> F_3`, and `R_3 -> F_4`.

Generation six remains unnecessary.
