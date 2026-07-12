# Extended completion descent through target offset `4L`

## Status

Elementary layer-pattern theorem with exact rational polytope verification.

This strengthens the completion-descent range used in the original infinite-tail proof. The layer conclusion is unchanged, but the target completion offset may be as large as four times the parent scale.

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
0<c\le4L.
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
5. `0<=c/L<=4`.

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

Thus

```math
\boxed{
\text{completion at }16L+c
\quad\Longrightarrow\quad
\text{parent completion at }2L+(c-3k).
}
```

The converse lift holds whenever the three parent points exist. The reflected left-completion statement follows by the same calculation.

---

## 4. Relation to the infinite-tail induction

The original scheduled tail only needs

```math
0<c\le L/8,
```

because its child offset is `c=4k<=L/8`.

The range through `2L` certifies the entire depth-ten basin-criterion interval. The range through `4L` additionally certifies the only geometrically possible completion offsets needed for the complete exact factor-eight classification from `S_10`.

For the first descent from `S_10` to `S_9`, a completion at `2L_10+k` is geometrically possible only for

```math
k\le230535808<4L_9.
```

After descent, the `S_9` shell geometry shows that a second descent is required only for

```math
k\le29209215,
```

and then

```math
k-3<4L_8.
```

Thus every completion obstruction in the full fitting exact factor-eight range has an exact test against the signed completion set of `S_8`.

---

## 5. Consequences

### Full basin-criterion fan

Every

```math
4\le k\le L_{10}/32
```

has an exact two-step completion test. This gives the `11129810`-tail basin fan recorded in `docs/depth-ten-exact-tail-basin-fan.md`.

### Full exact factor-eight classification

For every fitting positive exact offset

```math
1\le k\le613454687,
```

the completion obstruction is either geometrically impossible or descends exactly to the certified `S_8` completion set. Combined with the state-specific top-layer pattern theorem and the half-separation test, this yields the complete classification in

```text
docs/depth-ten-full-exact-factor-eight-classification.md
```
