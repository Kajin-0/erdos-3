# Factor-two inheritance exclusion for the depth-ten state

## Status

Exact theorem obtained by embedding the previously certified depth-nine factor-four domain.

Let

```math
S_9\subseteq[L_9,2L_9),
\qquad
S_{10}\subseteq[L_{10},2L_{10})
```

be the recorded states, with

```math
L_9=67108864,
\qquad
L_{10}=536870912.
```

This note proves

```math
\boxed{N_{10,2}=0.}
```

Thus every continuation of the recorded `S_10` in the standard-dyadic disjoint three-translate replay-containment model either terminates or has scale factor at least `4`.

**Verifier:** `src/verify_depth10_factor2_inheritance.py`.

**Certificate:** `data/depth10_factor2_inheritance_certificate_2026-07-12.txt`.

---

## 1. Embedded depth-nine anchor state

The exact depth-ten construction is

```math
S_{10}
=
L_{10}
+
\Bigl((\{0\}\cup S_9)+\{0,R_9,2R_9\}\Bigr),
```

where

```math
R_9=134217729.
```

In particular,

```math
\boxed{
L_{10}+(\{0\}\cup S_9)
\subseteq
S_{10}.
}
```

For any separation `R`, define

```math
G_h(R)
=
(\{0\}\cup S_h)+\{0,R,2R\}.
```

The preceding containment implies

```math
\boxed{
L_{10}+G_9(R)
\subseteq
G_{10}(R).
}
```

Therefore every four-term progression in `G_9(R)` lifts, by translation through `L_10`, to a four-term progression in `G_10(R)`.

---

## 2. Endpoint comparison

The largest separation fitting a factor-four continuation from `S_9` is

```math
\left\lfloor
\frac{4L_9-1-\max S_9}{2}
\right\rfloor
=
76583776.
```

The largest separation fitting a factor-two continuation from `S_10` is

```math
\left\lfloor
\frac{2L_{10}-1-\max S_{10}}{2}
\right\rfloor
=
76583775.
```

Hence

```math
\boxed{
\mathcal R_{10,2}
\subseteq
\mathcal R_{9,4},
}
```

where each domain includes the same coordinated sponsor condition `v_2(R)` even.

If the three `S_10` translate layers are disjoint, then the embedded `S_9` translate layers are also disjoint. Thus every layer-disjoint factor-two candidate from `S_10` is a layer-disjoint candidate in the complete factor-four domain from `S_9`.

---

## 3. Use of the certified depth-nine theorem

The complete depth-nine theorem proves

```math
\boxed{N_{9,4}=0.}
```

Every sponsor-compatible layer-disjoint separation in the factor-four fitting domain of `S_9` therefore produces a four-term arithmetic progression in `G_9(R)`.

By the embedding

```math
L_{10}+G_9(R)\subseteq G_{10}(R),
```

that progression also occurs in the corresponding depth-ten factor-two candidate.

Consequently

```math
\boxed{N_{10,2}=0.}
```

---

## 4. Consequence for Bellman debt

The recorded depth-ten state has no factor-two escape. Its only possible cheap continuation has scale factor `4`.

This removes the more expensive factor-two Bellman debt token from the continuation problem rooted at `S_10`. Any nonterminating path leaving `S_10` either:

1. takes a factor-four contaminated step;
2. takes a factor-eight exact step, whose complete child fan is already classified;
3. takes a scale factor at least `16`, which creates Bellman surplus.

The remaining finite `S_10` problem is therefore the complete factor-four escape domain.

---

## 5. Scope

This is a state-specific inheritance theorem. It does not prove that factor-two steps are universally impossible at other contaminated states. Its proof depends on:

1. the exact embedded copy of `S_9` inside `S_10`;
2. the endpoint inequality between the two finite domains;
3. the complete certified theorem `N_{9,4}=0`.
