# Exact-tail basin criterion

## Status

Elementary theorem, using the top-layer reduction and small-offset completion-descent lemmas proved in `docs/infinite-exact-tail-from-depth-ten.md` and verified exactly by `src/verify_exact_tail_pattern_lemmas.py`.

This criterion abstracts the recorded infinite tail from `S_10`. It gives a finite certificate for the existence of an infinite exact factor-eight continuation with explicitly summable certified replay weight.

The theorem concerns one scheduled continuation path. It does not assert that every descendant of the entry state follows the basin.

---

## 1. Basin certificate

Let `L` be a power of two and let

```math
S\subseteq[L,7L/4)
```

be four-term-progression-free. Let `P>=1` be the certified identical-history replay multiplicity carried by `S`.

Suppose there is an integer `k` satisfying:

1. **small positive offset**
   ```math
   0<k\le L/32;
   ```
2. **left-sponsor orientation**
   ```math
   v_2(k)\equiv0\pmod2;
   ```
3. **lower gap**
   ```math
   S\cap(L,L+L/8)=\varnothing;
   ```
4. **missing-completion condition**: no nontrivial three-term progression in `S` has missing left or right completion
   ```math
   2L+k.
   ```

Call `(S,L,k,P)` an **exact-tail basin certificate**.

---

## 2. Infinite scheduled continuation

Starting from

```math
S_0=S,
\qquad
L_0=L,
\qquad
k_0=k,
\qquad
P_0=P,
```

define for every `n>=0`

```math
L_{n+1}=8L_n,
```

```math
k_{n+1}=4k_n,
```

```math
R_n=2L_n+k_n,
```

```math
A_n=\{0\}\cup S_n,
```

and

```math
S_{n+1}
=
L_{n+1}
+
\Bigl(A_n\cup(A_n+R_n)\cup(A_n+2R_n)\Bigr).
```

Then every `S_n` is four-term-progression-free and lies in

```math
S_n\subseteq[L_n,7L_n/4).
```

At every generation:

1. the three translate layers are disjoint;
2. coordinated deletion selects the left sponsor;
3. the middle multiplicity fiber is exactly `S_n`;
4. the standard backbone shell is exactly `S_n`;
5. certified replay multiplicity doubles.

Thus this is an infinite exact-backbone factor-eight continuation.

---

## 3. Proof of the invariant

### 3.1 Offset and sponsor orientation

The closed forms are

```math
L_n=8^nL,
\qquad
k_n=4^nk.
```

Hence

```math
\frac{k_n}{L_n}
=
2^{-n}\frac{k}{L}
\le
\frac1{32}.
```

Also

```math
v_2(k_n)=v_2(k)+2n,
```

which is even. Since `0<k_n<L_n`,

```math
v_2(R_n)
=
v_2(2L_n+k_n)
=
v_2(k_n),
```

so the coordinated sponsor is always the left endpoint.

### 3.2 Adding zero does not create a four-term progression

Put `A_n={0} union S_n`. If a nontrivial increasing four-term progression in `A_n` used zero, zero would be its first term and its other terms would be

```math
d,2d,3d.
```

But `d>=L_n`, whereas `S_n subseteq[L_n,7L_n/4)`, so `3d` cannot belong to `S_n`. Therefore `A_n` is four-term-progression-free whenever `S_n` is.

### 3.3 Lower gap

The smallest positive point of the raw next state is `L_n`, because the unshifted copy of `S_n` begins there and `R_n>2L_n`. After adding `L_{n+1}=8L_n`,

```math
S_{n+1}\cap
(L_{n+1},L_{n+1}+L_{n+1}/8)
=
\varnothing.
```

Thus the lower-gap condition persists.

If `R_n` is even, then

```math
R_n/2=L_n+k_n/2
```

lies strictly in this gap. If `R_n` is odd, `R_n/2` is not an integer. Therefore the half-separation obstruction in the top-layer lemma is always absent.

### 3.4 Completion invariant

Assume no three-term progression in `S_n` is completed at

```math
2L_n+k_n.
```

The small-offset completion-descent lemma says that a progression in `S_{n+1}` completed at

```math
2L_{n+1}+k_{n+1}
```

would descend to a progression in `S_n` completed at

```math
2L_n+(k_{n+1}-3k_n).
```

Since

```math
k_{n+1}-3k_n=4k_n-3k_n=k_n,
```

this contradicts the induction hypothesis. The same argument handles left completions.

### 3.5 Four-term-progression-freeness

The top-layer reduction lemma applies because

```math
2L_n<R_n\le\frac{65}{32}L_n.
```

Every possible new four-term progression would require either the scheduled completion at `R_n` or the point `R_n/2` in `S_n`. Both are absent. Hence the raw next state and `S_{n+1}` are four-term-progression-free.

### 3.6 Shell and exact reproduction

The upper bound is preserved:

```math
\max S_{n+1}
=
8L_n+\max S_n+2R_n
<
8L_n+\frac74L_n+4L_n+\frac1{16}L_n
<
\frac74L_{n+1}.
```

Moreover,

```math
R_n>2L_n>\max S_n.
```

Therefore the translate layers are disjoint, the backbone shell `[L_n,2L_n)` contains exactly the unshifted state `S_n`, and the middle difference fiber is exactly `S_n`.

---

## 4. Exact future cost

Let

```math
N=|S|.
```

The cardinality recurrence is

```math
|S_{n+1}|=3(|S_n|+1),
```

so

```math
|S_n|
=
3^n\left(N+\frac32\right)-\frac32.
```

Certified replay multiplicity and scale satisfy

```math
P_n=2^nP,
\qquad
L_n=8^nL.
```

Define

```math
W_n=P_n\frac{|S_n|}{L_n}.
```

Then

```math
\boxed{
W_n
=
\frac{P}{L}
\left[
\left(N+\frac32\right)\left(\frac34\right)^n
-
\frac32\left(\frac14\right)^n
\right].
}
```

Consequently the entire scheduled future is exactly summable:

```math
\boxed{
\sum_{n\ge0}W_n
=
\frac{4P(N+1)}{L}.
}
```

This quantity is the **basin terminal charge**.

For the recorded depth-ten entry state,

```math
P=1024,
\qquad
N=265719,
\qquad
L=536870912,
```

and therefore

```math
\frac{4P(N+1)}L
=
\frac{33215}{16384},
```

agreeing with the explicit tail calculation.

---

## 5. Use in a whole-tree proof

Once a continuation state is certified to lie in this basin, its selected infinite exact descendant path can be replaced by the finite terminal charge

```math
\mathfrak B(S,L,P)
=
\frac{4P(|S|+1)}L.
```

This removes the need to expand that path generation by generation.

The unresolved whole-tree task is to prove one of the following:

1. every infinite path eventually acquires a basin certificate;
2. paths avoiding every basin have sufficiently large average scale growth;
3. contamination outside the basins creates an exportable or packable debt that pays for its future branching.

The criterion supplies a reusable absorbing state for a future finite-state, spectral, or potential-theoretic analysis of the continuation tree.
