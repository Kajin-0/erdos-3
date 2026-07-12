# Infinite exact factor-eight tail from the recorded depth-ten state

## Status

Exact theorem with an elementary induction and a finite computer-assisted seed certificate.

The recorded contaminated-backbone branch reaches

```math
S_{10}\subseteq[L_{10},2L_{10}),
\qquad
L_{10}=536870912,
\qquad
|S_{10}|=265719.
```

This note proves that `S_10` has an explicit infinite sequence of exact-backbone continuations. Every later scale factor is exactly `8`, every state is four-term-progression-free, identical-history persistence continues to double, and the multiplicity-weighted density along the tail is summable.

The result concerns one continuation path. It does not classify every descendant of `S_10`, and it does not prove that the union of different dyadic states is globally four-term-progression-free.

**Finite seed verifier:** `src/verify_infinite_exact_tail_from_depth10.cpp`.

**Exact layer-pattern verifier:** `src/verify_exact_tail_pattern_lemmas.py`.

**Certificate:** `data/infinite_exact_tail_from_depth10_certificate_2026-07-12.txt`.

---

## 1. Two layer-pattern lemmas

Let

```math
S\subseteq[L,7L/4),
\qquad
A=\{0\}\cup S,
```

and let

```math
2L<R\le\frac{65}{32}L.
```

Put

```math
G=A\cup(A+R)\cup(A+2R).
```

### Lemma 1: top-layer reduction

Assume `A` is four-term-progression-free. Every nontrivial four-term progression in `G` is caused by one of two obstructions:

1. `S` contains a three-term progression whose missing left or right completion is `R`;
2. `R` is even and `R/2` belongs to `S`.

Because the three translate layers are separated, the layer indices of an increasing four-term progression are nondecreasing. Exact rational enumeration leaves only the following patterns:

| Layer patterns | Consequence |
|---|---|
| `0000`, `1111`, `2222` | a four-term progression already lies in `A` |
| `0001`, `0012`, `1112` | a three-term progression in `S` is completed at `R` |
| `0011`, `0112`, `1122` | `R/2` belongs to `S` |

No other layer pattern is compatible with the shell bounds.

Consequently, if `S` has no three-term progression completed at `R`, and either `R` is odd or `R/2` is absent from `S`, then `G` is four-term-progression-free.

### Lemma 2: small-offset completion descent

Write

```math
R=2L+k,
\qquad
0<k\le L/32,
```

and let

```math
S'=8L+G.
```

Let `c` satisfy

```math
0<c\le L/8.
```

If `S'` contains an increasing three-term progression whose missing right completion is

```math
2(8L)+c,
```

then the progression must use translate layers `0,1,2`. Its three base points form a three-term progression in `S`, and their missing right completion is

```math
2L+(c-3k).
```

The converse also holds. A base progression completed at `2L+(c-3k)` lifts through layers `0,1,2` to a progression in `S'` completed at `16L+c`. The same statement holds for left completions.

The exact rational verifier finds only layer pattern `012`, with all three base entries in `S`, throughout

```math
0\le k/L\le1/32,
\qquad
0\le c/L\le1/8.
```

---

## 2. Finite seed data at `S_8`

The certified depth-eight state satisfies

```math
L_8=8388608,
\qquad
|S_8|=29523,
\qquad
\max S_8=14604604<\frac74L_8.
```

It also has the lower-gap property

```math
S_8\cap(L_8,L_8+L_8/8)=\varnothing.
```

The exact completion search for

```math
A_8=\{0\}\cup S_8
```

finds

```text
2772873 distinct three-term-progression completion coordinates
minimum completion = 6291444
maximum completion = 17038008.
```

Choose

```math
D=2^{18}-1=262143.
```

Then

```math
2L_8+D=17039359>17038008.
```

Thus no three-term progression in `A_8`, and in particular none in `S_8`, has missing completion `2L_8+D`.

---

## 3. Starting from the recorded `S_10`

The recorded path from `S_8` to `S_10` uses exact separation offsets

```math
k_8=k_9=1,
\qquad
R_j=2L_j+k_j.
```

Completion descent through these two steps subtracts

```math
3k_8+3k_9=6.
```

Define

```math
k_{10}=D+6=262149.
```

A hypothetical three-term progression in `S_10` completed at

```math
2L_{10}+k_{10}
```

would descend first to offset `D+3` in `S_9`, and then to offset `D` in `S_8`. The finite seed certificate excludes the latter. Therefore `S_10` has no three-term progression completed at `2L_10+k_10`.

---

## 4. Infinite exact recursion

For every `h>=10`, define

```math
L_{h+1}=8L_h,
```

```math
k_{h+1}=4k_h,
```

```math
R_h=2L_h+k_h,
```

and

```math
S_{h+1}
=
L_{h+1}
+
\Bigl(
A_h\cup(A_h+R_h)\cup(A_h+2R_h)
\Bigr),
\qquad
A_h=\{0\}\cup S_h.
```

The offset has closed form

```math
\boxed{
k_{10+n}=262149\cdot4^n.
}
```

### Sponsor orientation

Since `262149` is odd,

```math
v_2(k_{10+n})=2n.
```

The two-adic valuation of `2L_{10+n}` is larger, hence

```math
\boxed{
v_2(R_{10+n})=2n,
}
```

which is always even. Coordinated deletion therefore always selects the left sponsor.

### Small-offset bound

The ratio halves at every generation:

```math
\frac{k_{h+1}}{L_{h+1}}
=
\frac12\frac{k_h}{L_h}.
```

At the seed, `k_10<L_10/32`, so

```math
0<k_h<L_h/32
```

for every `h>=10`.

### Lower gap and the half-separation obstruction

The recorded `S_10` satisfies

```math
S_{10}\cap(L_{10},L_{10}+L_{10}/8)=\varnothing.
```

If this holds for `S_h`, then the smallest positive point of the next raw state is `L_h=L_{h+1}/8`, so the same gap holds for `S_{h+1}`.

When `R_h` is even,

```math
R_h/2=L_h+k_h/2
```

lies strictly inside this empty gap. Thus the half-separation obstruction in Lemma 1 never occurs.

### Completion invariant

Suppose `S_h` has no three-term progression completed at `2L_h+k_h`. Lemma 2 with

```math
c=k_{h+1}=4k_h
```

shows that a progression in `S_{h+1}` completed at `2L_{h+1}+k_{h+1}` would descend to a progression in `S_h` completed at

```math
2L_h+(4k_h-3k_h)
=2L_h+k_h,
```

which is impossible.

Therefore the scheduled completion obstruction is absent at every generation.

### Four-term-progression-freeness

Lemma 1 applies at every step:

1. `A_h` is four-term-progression-free;
2. no three-term progression in `S_h` is completed at `R_h`;
3. `R_h/2` is absent whenever `R_h` is even.

Hence every raw state, and therefore every `S_{h+1}`, is four-term-progression-free.

### Shell and exact-backbone invariants

The upper-shell bound is preserved because

```math
\max S_{h+1}
=
8L_h+\max S_h+2R_h
<
8L_h+\frac74L_h+4L_h+\frac1{16}L_h
<
\frac74L_{h+1}.
```

Also

```math
R_h>2L_h>\max S_h,
```

so the three translate layers are disjoint and the backbone shell `[L_h,2L_h)` contains exactly `S_h`. The middle multiplicity fiber is also exactly `S_h`. Thus this is an exact-backbone continuation at every generation.

---

## 5. Cardinality, persistence, and summable weight

For `n>=0`,

```math
L_{10+n}=2^{29+3n},
```

```math
|S_{10+n}|
=
\frac{3^{12+n}-3}{2},
```

and

```math
P_{10+n}^{\mathrm{cert}}=2^{10+n}.
```

Therefore

```math
\boxed{
W_{10+n}
=
P_{10+n}^{\mathrm{cert}}
\frac{|S_{10+n}|}{L_{10+n}}
=
\frac{3^{12+n}-3}{2^{20+2n}}.
}
```

In particular,

```math
W_{10+n}\sim
\frac{3^{12}}{2^{20}}
\left(\frac34\right)^n.
```

The entire infinite tail is summable:

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{3^{12}-1}{2^{18}}
=
\frac{33215}{16384}.
}
```

Thus the recorded contaminated branch enters an explicit infinite exact-recovery basin whose total multiplicity-weighted density is finite.

---

## 6. Consequence for the proof program

This establishes an actual long-run compensation mechanism on one contaminated continuation path:

```math
\text{finite contaminated growth}
\longrightarrow
\text{exact scale-eight basin}
\longrightarrow
\text{summable weighted tail}.
```

It does not control the full continuation tree. A proof of the four-term Erdős case still has to show that every infinite path either enters a summable basin of this type or pays an equivalent aggregate cost through contamination, overlap, or larger scale growth.
