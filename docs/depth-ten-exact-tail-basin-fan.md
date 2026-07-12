# A fan of 11,129,810 exact summable tails from `S_10`

## Status

Complete exact classification across the full exact-tail basin-criterion range, using:

1. the complete signed `S_8` three-term-progression completion set;
2. two applications of the extended completion-descent theorem;
3. the exact-tail basin criterion.

The recorded state `S_10` admits

```math
\boxed{11129810}
```

distinct scheduled infinite exact factor-eight tails.

**Full verifier:** `src/verify_depth10_full_exact_tail_basin_fan.cpp`.

**Layer-pattern verifier:** `src/verify_exact_tail_pattern_lemmas.py`.

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

## 2. Extended two-step completion descent

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

Exact rational layer enumeration proves that the unique descent pattern remains `012` whenever the target offset satisfies

```math
0<c\le2L.
```

This covers the entire basin-criterion range:

- first descent:
  ```math
  k\le L_{10}/32=L_9/4<2L_9;
  ```
- second descent:
  ```math
  k-3\le2L_8.
  ```

Therefore every integer

```math
\boxed{4\le k\le L_{10}/32=16777216}
```

has an exact two-step completion test against the signed `S_8` completion set.

---

## 3. Complete sponsor-compatible classification

There are exactly

```text
11184809
```

integers in the full range with

```math
v_2(k)\equiv0\pmod2.
```

For each one, the verifier tests whether

```math
2L_8+(k-6)
```

belongs to the complete signed `S_8` completion set.

Exactly

```text
54999
```

sponsor-compatible offsets are blocked. The remaining

```math
\boxed{11129810}
```

offsets are valid exact-tail basin entries.

The first and last valid offsets are

```math
k=4
```

and

```math
k=16777216.
```

The canonical hashes of the comma-terminated increasing valid-offset list are

```text
FNV-64  2a52c71cddac07f5
SHA-256 9cbbd28aab4db0a74d48c4a8eaf95d18b3854e56bd7138123734eaefe5b2d384
```

---

## 4. Two-adic distribution

| `v_2(k)` | Valid offsets |
|---:|---:|
| 0 | 8347334 |
| 2 | 2086812 |
| 4 | 521711 |
| 6 | 130464 |
| 8 | 32612 |
| 10 | 8152 |
| 12 | 2043 |
| 14 | 511 |
| 16 | 128 |
| 18 | 32 |
| 20 | 8 |
| 22 | 2 |
| 24 | 1 |

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

The basin criterion proves that every resulting state is four-term-progression-free and exact-backbone. Distinct initial offsets give distinct first separations and therefore distinct first child states. Multiplication by `4` preserves distinctness at every later generation.

Thus `S_10` is the root of at least

```math
\boxed{11129810}
```

distinct certified infinite exact tails.

---

## 6. Common terminal charge

State size, scale, and certified replay multiplicity do not depend on which valid offset is selected. Every tail has the same total certified weighted density:

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

## 7. Nested independently verified subfamilies

Two earlier counts remain correct as independently reproducible subfamilies.

### Complete signed fan through `k=1048579`

```text
range                 4..1048579
sponsor-compatible    699051
blocked                54999
valid                  644052
FNV-64                 5e1b143b6a59b345
SHA-256                22daeb2366e5e3324b7e835c61adb34f8e08c0ae203b86420c941f53991069b4
```

### Completion-free upper interval

```text
range                 260799..1048579
valid                 525189
SHA-256               99eb9011d140b420ddf4bd2bf33b6d98d9381b36e12089e231eda8323c548e60
```

The Python verifier certifies the latter lightweight subfamily. The full C++ verifier certifies all `11129810` offsets.

---

## 8. Scope

The result demonstrates that the summable exact basin occupies most sponsor-compatible offsets in the full small-offset region at `S_10`. It does not classify larger exact factor-eight offsets, and it does not control the factor-two or factor-four escape domains. The whole continuation-tree problem remains open.
