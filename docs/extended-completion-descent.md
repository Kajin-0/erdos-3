# Extended completion descent through target offset `2L`

## Status

Elementary layer-pattern theorem with exact rational polytope verification.

This strengthens the completion-descent range used in the original infinite-tail proof. The layer conclusion is unchanged, but the target completion offset may now be as large as twice the parent scale.

**Verifier:** `src/verify_exact_tail_pattern_lemmas.py`.

---

## 1. Setup

Let

```math
S\subseteq[L,7L/4),
\qquad
A=\{0\}\cup S.
```

Choose

```math
R=2L+k,
\qquad
0\le k\le L/32,
```

and form

```math
G=A\cup(A+R)\cup(A+2R),
```

```math
S'=8L+G.
```

Let

```math
0<c\le2L.
```

Suppose `S'` contains an increasing nontrivial three-term progression whose missing right completion is

```math
2(8L)+c=16L+c.
```

---

## 2. Unique layer pattern

Write the three raw points as

```math
a_j+i_jR,
\qquad
j=0,1,2,
```

with

```math
a_j\in A,
\qquad
i_j\in\{0,1,2\}.
```

Because the translate layers are separated, an increasing progression has

```math
i_0\le i_1\le i_2.
```

Normalize by `L` and impose:

1. the second-difference equation for the three-term progression;
2. the equation placing its missing completion at `16L+c`;
3. `a_j/L` equal to zero or lying in `[1,7/4)`;
4. `0<=k/L<=1/32`;
5. `0<=c/L<=2`.

Exact rational vertex enumeration over every layer pattern and zero/nonzero base pattern leaves exactly

```text
layer pattern 012
base pattern 111.
```

No other pattern is feasible with positive progression step.

---

## 3. Descent identity

The unique pattern has one point in each translate layer. The three base points form a three-term progression in `S`, and the missing right completion of that base progression is

```math
\boxed{
2L+(c-3k).
}
```

Thus:

```math
\boxed{
\text{completion at }16L+c
\quad\Longrightarrow\quad
\text{parent completion at }2L+(c-3k).
}
```

The converse lift holds whenever the three parent points exist: a parent progression completed at `2L+(c-3k)` lifts through layers `0,1,2` to a progression in `S'` completed at `16L+c`.

The reflected left-completion statement follows by the same calculation.

---

## 4. Relation to the original lemma

The original infinite-tail induction only needs

```math
0<c\le L/8,
```

because its scheduled child offset is `c=4k<=L/8`.

The extended range

```math
0<c\le2L
```

is needed to pull the entire depth-ten basin-criterion interval back through the two exact offset-one steps from `S_10` to `S_8`.

At the first descent,

```math
c=k\le L_{10}/32=L_9/4<2L_9.
```

At the second descent,

```math
c=k-3\le2L_8.
```

Therefore every basin-criterion offset

```math
4\le k\le L_{10}/32
```

has an exact two-step completion test against the certified signed completion set of `S_8`.

---

## 5. Consequence

This theorem removes the former artificial upper bound `k<=1048579` from the depth-ten basin fan. The complete criterion range is

```math
4\le k\le16777216.
```

Within that range, basin validity is equivalent to:

1. even `v_2(k)`;
2. absence of the signed `S_8` completion coordinate
   ```math
   2L_8+(k-6).
   ```

The full finite classification is recorded in `docs/depth-ten-exact-tail-basin-fan.md`.
