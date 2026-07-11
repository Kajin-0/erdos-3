# Dyadic scale-eight barrier for exact three-translate replication

## Status

Elementary theorem. No computation is required.

This note proves that the scale-eight aligned-diamond construction is ambient-scale optimal inside the exact standard-dyadic three-translate replication model used by the current recursion.

The theorem does **not** bound every possible aligned-diamond mechanism. It applies when one replication step is formed from three exact translates and is then placed into one standard dyadic shell.

---

## 1. Exact three-translate replication step

Let

```math
S\subseteq[L,2L)
```

be a nonempty state in a standard dyadic shell, where `L` is a power of two. Put

```math
A=\{0\}\cup S.
```

Choose an integer separation `R` and form

```math
G=A\cup(A+R)\cup(A+2R).
```

Assume the step has the exact aligned-replication geometry used in the self-replicating diamond:

1. the translate layers are separated from the original backbone shell, so
   ```math
   R\ge 2L;
   ```
2. the next state is obtained by translating `G` into a standard dyadic shell,
   ```math
   S'=L'+G\subseteq[L',2L'),
   ```
   where `L'` is also a power of two.

The first assumption ensures that the minimum-translation backbone shell `[L,2L)` contains the original copy `S` without contamination by the `R` or `2R` layers. It also implies `R>\max S`, since `S\subseteq[L,2L)`.

---

## 2. One-step scale barrier

### Theorem

Every exact three-translate replication step satisfying the assumptions above obeys

```math
\boxed{L'\ge 8L.}
```

### Proof

Because `0\in A`, the point

```math
2R
```

belongs to `G`. Since

```math
S'=L'+G\subseteq[L',2L'),
```

we must have

```math
G\subseteq[0,L'),
```

and therefore

```math
2R<L'.
```

The exact-backbone separation assumption gives

```math
R\ge2L,
```

so

```math
L'>2R\ge4L.
```

Both `L` and `L'` are powers of two. Hence the ratio `L'/L` is a power of two. The smallest power of two strictly larger than `4` is `8`. Thus

```math
L'\ge8L.
```

This proves the claim. `square`

---

## 3. Multigeneration consequence

Suppose an exact replication genealogy has `h` such steps, with dyadic shell scales

```math
L_0,L_1,\ldots,L_h.
```

Applying the one-step theorem repeatedly gives

```math
L_j\ge8L_{j-1}
```

and hence

```math
\boxed{L_h\ge8^hL_0.}
```

The exact aligned diamond doubles identical-history persistence at every step. Thus

```math
P_h=2^h.
```

Combining the two relations,

```math
P_h
=2^h
\le
\left(\frac{L_h}{L_0}\right)^{1/3}.
```

Therefore

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

For a fixed initial scale, every exact standard-dyadic three-translate replication family satisfies

```math
P_h=O(L_h^{1/3}).
```

---

## 4. Sharpness

The scale-eight construction has

```math
L_{h+1}=8L_h
```

at every generation and

```math
P_h=2^h.
```

It therefore attains equality in the scale exponent:

```math
P_h
=
\frac12L_h^{1/3}
```

for its normalization `L_1=64`.

Consequently:

```math
\boxed{
\text{the exponent }1/3\text{ is optimal in the exact standard-dyadic three-translate model.}
}
```

The earlier open question of reducing the uniform dyadic scale factor below `8` is closed negatively in this model. A better ambient-scale exponent would require leaving at least one of the hypotheses:

1. exact three-translate replication;
2. uncontaminated reproduction of the backbone shell;
3. one standard dyadic parent shell per replication generation;
4. exact doubling of identical-history persistence at each generation.

---

## 5. What remains open

This theorem does not establish a universal `L^(1/3)` upper bound for arbitrary persistence events in the full recursive proof program. More general mechanisms may involve:

- overlapping or partially resolved translate layers;
- several parent states contributing jointly to one persistence event;
- nonuniform branching rather than exact binary doubling;
- reproduction spread across more than one dyadic shell;
- approximate rather than exact child-state recurrence.

The main density-sensitive bottleneck is therefore unchanged. What is now resolved is the sharp ambient-scale law for the canonical exact three-translate obstruction.
