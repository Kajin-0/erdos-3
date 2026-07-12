# Exact cheap-continuation candidate domains from `S_10`

## Status

Exact finite domain calculation. This note counts every sponsor-compatible separation whose three translate layers are disjoint and fit at dyadic factor `2` or `4`.

It does **not** classify the surviving candidates as four-term-progression-free or invalid. The complete `S_10` cheap-extension problem remains open.

**Verifier:** `src/verify_depth10_candidate_domains.cpp`.

**Certificate:** `data/depth10_candidate_domains_certificate_2026-07-12.txt`.

---

## 1. Parent state

The recorded state satisfies

```math
S_{10}\subseteq[536870912,1073741824),
```

```math
|S_{10}|=265719,
\qquad
\max S_{10}=920574272.
```

Its FNV-64 audit hash is

```text
405b941a1f8b2580
```

and it has the exact internal structure

```math
S_{10}
=
L_{10}
+
\Bigl(
A_9\cup(A_9+R_9)\cup(A_9+2R_9)
\Bigr),
```

where

```math
A_9=\{0\}\cup S_9,
\qquad
R_9=134217729.
```

---

## 2. Recursive positive-difference support

A candidate separation `R` has disjoint translate layers exactly when neither

```math
R
```

nor

```math
2R
```

is a positive difference of two points of

```math
\{0\}\cup S_{10}.
```

Enumerating all pairs of the 265,720-point anchor set would require roughly `35` billion pair operations. The verifier avoids this by reconstructing the support recursively:

1. build the positive-difference support of the 29,524-point set `A_8` directly;
2. lift it through the three `R_8` translate layers to obtain the support of `A_9`;
3. lift that support through the three `R_9` layers;
4. add the differences from the anchor zero to every point of `S_10`.

As an audit, the intermediate `A_9` support reproduces the previously certified `S_9` domain counts exactly.

---

## 3. Factor-two domain

The fit condition gives

```math
R\le76583775.
```

Among positive separations in this range,

```text
51055851
```

have even two-adic valuation and therefore the coordinated left-sponsor orientation.

After the exact layer-disjointness filter,

```math
\boxed{33026376}
```

candidates remain.

The canonical FNV-64 hash of the increasing candidate list is

```text
59cfbc6761c6224d
```

---

## 4. Factor-four domain

The fit condition gives

```math
R\le613454687.
```

There are

```text
408969792
```

sponsor-compatible separations and

```math
\boxed{348012826}
```

layer-disjoint candidates.

The canonical FNV-64 hash of the increasing candidate list is

```text
ae1d9e1ec77b2dfb
```

---

## 5. Interpretation

The domain has grown substantially from the earlier states:

```text
S7 factor-four disjoint domain:       359419
S8 factor-four disjoint domain:      4190292
S9 factor-four disjoint domain:     39459384
S10 factor-four disjoint domain:   348012826
```

A direct candidate-by-candidate full-parent scan is therefore no longer the preferred first method. The recursive structure must be exploited at the witness level, through one or more of:

1. recursive completion-set propagation;
2. recursive equal-difference rectangle joins;
3. a finite automaton or symbolic quotient for the exact tail states;
4. a theorem showing that all cheap descendants of basin states incur a bounded collection of structural obstructions.

Exploratory random middle-pair tests across the factor-four range found explicit four-term progressions, but sampling is not a certificate and is not included in the theorem statement.
