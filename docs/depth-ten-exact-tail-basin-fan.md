# A fan of 644,052 exact summable tails from `S_10`

## Status

Complete exact two-step-descent classification within the certified small-offset range, using:

1. the full signed `S_8` three-term-progression completion set;
2. two applications of the small-offset completion-descent lemma;
3. the exact-tail basin criterion.

The recorded state `S_10` admits

```math
\boxed{644052}
```

distinct scheduled infinite exact factor-eight tails.

**Full verifier:** `src/verify_depth10_full_exact_tail_basin_fan.cpp`.

**Lightweight upper-interval subfamily verifier:** `src/verify_depth10_exact_tail_basin_fan.py`.

**Certificate:** `data/depth10_exact_tail_basin_fan_certificate_2026-07-12.txt`.

---

## 1. Complete signed completion set at `S_8`

Let

```math
A_8=\{0\}\cup S_8.
```

The exact completion search constructs every signed coordinate that completes a nontrivial three-term progression in `A_8`. The set contains

```text
2772873
```

distinct coordinates.

The full verifier reconstructs this set directly from the 29,524-point anchor set before testing any depth-ten offset.

---

## 2. Two-step completion descent

The exact steps from `S_8` to `S_9` and from `S_9` to `S_10` both use offset `1`:

```math
R_8=2L_8+1,
\qquad
R_9=2L_9+1.
```

A hypothetical completion in `S_10` at

```math
2L_{10}+k
```

descends first to offset `k-3` at `S_9`, then to offset

```math
k-6
```

at `S_8`. Thus the corresponding seed completion coordinate is

```math
2L_8+(k-6).
```

The descent lemmas apply when

```math
0<k\le L_9/8
```

and

```math
0<k-3\le L_8/8.
```

Together these give the complete integer range

```math
\boxed{4\le k\le1048579.}
```

The basin criterion also requires

```math
v_2(k)\equiv0\pmod2.
```

---

## 3. Complete sponsor-compatible classification

There are exactly

```text
699051
```

integers in the permitted range with even two-adic valuation.

For each one, the verifier tests whether

```math
2L_8+(k-6)
```

belongs to the complete signed `S_8` completion set.

Exactly

```text
54999
```

sponsor-compatible offsets are blocked by a seed completion. The remaining

```math
\boxed{644052}
```

offsets are valid exact-tail basin entries.

The first and last valid offsets are

```math
k=4
```

and

```math
k=1048579.
```

The canonical hashes of the comma-terminated increasing valid-offset list are

```text
FNV-64  5e1b143b6a59b345
SHA-256 22daeb2366e5e3324b7e835c61adb34f8e08c0ae203b86420c941f53991069b4
```

---

## 4. Two-adic distribution

| `v_2(k)` | Valid offsets |
|---:|---:|
| 0 | 483016 |
| 2 | 120732 |
| 4 | 30191 |
| 6 | 7584 |
| 8 | 1892 |
| 10 | 472 |
| 12 | 123 |
| 14 | 31 |
| 16 | 8 |
| 18 | 2 |
| 20 | 1 |

Every class has even valuation, so coordinated deletion selects the left sponsor throughout the induced exact tail.

---

## 5. Distinct infinite tails

For every valid initial offset `k`, define

```math
k_n=4^nk,
```

```math
R_{10+n}=2L_{10+n}+k_n,
```

and apply exact three-translate reproduction at factor `8`.

The basin criterion proves that every resulting state is four-term-progression-free and exact-backbone. Distinct initial offsets give distinct first separations and therefore distinct first child states. Multiplication by `4` preserves distinctness at all later generations.

Thus `S_10` is the root of at least

```math
\boxed{644052}
```

distinct certified infinite exact tails.

---

## 6. Common terminal charge

State size, scale, and certified replay multiplicity do not depend on which valid offset is chosen. Every tail has the same total certified weighted density:

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{4P_{10}(|S_{10}|+1)}{L_{10}}
=
\frac{33215}{16384}.
}
```

---

## 7. Earlier interval-only subfamily

The lightweight Python verifier certifies the simpler completion-free upper interval

```math
260799\le k\le1048579,
```

which contains

```text
525189
```

valid sponsor-compatible offsets. Its list SHA-256 is

```text
99eb9011d140b420ddf4bd2bf33b6d98d9381b36e12089e231eda8323c548e60
```

This remains a correct independently reproducible subfamily. The full C++ verifier strengthens it by testing the entire signed completion set and adding another

```text
118863
```

certified tails.

---

## 8. Scope

The result demonstrates that the summable basin at `S_10` has substantial width in the separation parameter. It does not classify every factor-eight descendant, and it does not control the factor-two or factor-four escape domains. The whole continuation-tree problem remains open.
