# Exact pair-resource contraction from the third to fourth retained frontier

## Status

Exact finite theorem for the certified transition from the fourteen third-generation recursive retained states to the complete fourth retained family.

The result precedes global root uniqueness. It verifies both occurrence-valued and union-valued pair-resource contraction in the presence of limited pair reuse.

No fifth- or sixth-generation propagation is used for the test.

Primary files:

- `src/probe_pair_resource_third_to_fourth.py`;
- `src/verify_pair_resource_third_to_fourth.py`;
- `data/pair_resource_third_to_fourth_certificate_2026-07-14.txt`.

---

## 1. Third recursive parent family

The third recursive family has:

```text
14 states
4,789 points
14 affine states
0 non-affine states.
```

Its complete current-plus-latent pair-resource multiset has:

```text
2,155,298 resource occurrences
2,155,127 distinct resource tokens
maximum multiplicity 2
171 repeated resource tokens.
```

The parent resources split into:

```text
4,789 current pairs
2,150,356 latent pairs.
```

Occurrence-valued resource mass is

```text
W_occ(R3) = 7828.862146571999...
```

while union-valued resource mass is

```text
W_union(R3) = 7821.150527735019...
```

The exact repeated-pair mass is

```text
R_pair(R3) = 7.711618836980...
```

---

## 2. Complete fourth output

The complete fourth retained family has:

```text
23 states
1,794 points
11 terminal states
12 recursive states.
```

Every output comes from an affine third-generation parent.

Its current-plus-future pair-resource multiset has:

```text
372,299 resource occurrences
372,286 distinct resource tokens
maximum multiplicity 2
13 repeated resource tokens.
```

The resources split into:

```text
77 terminal current pairs
1,717 recursive current pairs
370,505 recursive latent pairs.
```

Occurrence-valued resource mass is

```text
W_occ(F4) = 2747.630136815823...
```

union-valued resource mass is

```text
W_union(F4) = 2747.496183058024...
```

and repeated-pair mass is

```text
R_pair(F4) = 0.133953757799...
```

Thus pair reuse falls by a factor of approximately

```math
\frac{7.711618836980\ldots}
     {0.133953757799\ldots}
\approx57.57.
```

---

## 3. Exact resource containment

Every fourth current pair and every fourth recursive latent pair belongs to the third-generation parent resource universe.

```text
missing current resource occurrences = 0
missing latent resource occurrences  = 0.
```

All fourth output resources come from parent latent pairs:

| fourth resource class | from parent current | from parent latent |
|---|---:|---:|
| terminal current | `0` | `77` |
| recursive current | `0` | `1,717` |
| recursive latent | `0` | `370,505` |

This is the same type conversion later certified at the fifth frontier.

---

## 4. Occurrence-valued contraction

Despite pair multiplicity two, the occurrence-valued resource potential contracts:

```math
\boxed{
W_{\rm occ}(F_4)
<
W_{\rm occ}(R_3).
}
```

Exact values:

```text
left  = 2747.630136815823...
right = 7828.862146571999...
```

with surplus

```text
5081.232009756176...
```

and ratio approximately

```text
0.350966...
```

---

## 5. Union-valued contraction

The canonical no-double-payment potential also contracts:

```math
\boxed{
W_\cup(F_4)
<
W_\cup(R_3).
}
```

Exact values:

```text
left  = 2747.496183058024...
right = 7821.150527735019...
```

with surplus

```text
5073.654344676995...
```

The union row is the state-independent theorem-level accounting convention. The occurrence row additionally shows that the small amount of pair reuse does not threaten contraction on this transition.

---

## 6. Consequence

The affine pair-resource regime is already valid before the unique-root frontier.

The fourth-to-fifth expansion was not the first point where pair accounting became effective. At `R_3 -> F_4`:

- affine closure is complete;
- containment is exact;
- pair multiplicity is bounded by two;
- repeated-pair mass is tiny relative to available capacity;
- both occurrence and union resource potentials contract by large margins.

The unresolved finite prefix moves earlier to:

```text
R1 -> F2
R2 -> F3.
```

---

## 7. Non-consequences

This theorem does not bound the pair-resource capacity entering the retained tree from the original dyadic block.

It also does not prove:

- that occurrence-valued pair mass always contracts;
- that pair multiplicity is universally at most two across arbitrary retained policies;
- that the full latent pair universe is economically affordable;
- a summable activated-pair theorem;
- or the four-term reciprocal-sum theorem.

Its role is to remove the third-to-fourth transition from the obstruction list and isolate the remaining activation problem and earlier finite reuse prefix.
