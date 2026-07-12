# A fan of 525,189 exact summable tails from `S_10`

## Status

Exact finite arithmetic consequence of:

1. the certified `S_8` completion maximum;
2. two applications of the small-offset completion-descent lemma;
3. the exact-tail basin criterion.

The recorded state `S_10` does not merely admit one summable exact continuation. It admits at least

```math
\boxed{525189}
```

distinct scheduled infinite exact factor-eight tails.

**Verifier:** `src/verify_depth10_exact_tail_basin_fan.py`.

**Certificate:** `data/depth10_exact_tail_basin_fan_certificate_2026-07-12.txt`.

---

## 1. Completion-free interval inherited from `S_8`

For the certified depth-eight anchor set

```math
A_8=\{0\}\cup S_8,
```

the exact completion search finds no three-term-progression completion above

```math
C_8^{\max}=17038008.
```

Since

```math
2L_8=16777216,
```

every integer

```math
D\ge260793
```

satisfies

```math
2L_8+D>C_8^{\max}
```

and is therefore absent from the completion set.

---

## 2. Lifting a missing completion to `S_10`

The exact steps from `S_8` to `S_9` and from `S_9` to `S_10` both use offset `1`:

```math
R_8=2L_8+1,
\qquad
R_9=2L_9+1.
```

Small-offset completion descent subtracts three times the offset at each step. Thus a hypothetical completion in `S_10` at

```math
2L_{10}+k
```

would descend to a completion in `S_8` at

```math
2L_8+(k-6).
```

The two descent lemmas apply provided

```math
0<k\le L_9/8
```

and

```math
0<k-3\le L_8/8.
```

The second condition is stronger and gives

```math
k\le1048579.
```

Combining this with `k-6>=260793` gives the interval

```math
\boxed{
260799\le k\le1048579.
}
```

For every `k` in this interval, `S_10` has no three-term progression completed at `2L_10+k`.

---

## 3. Sponsor-compatible basin offsets

The exact-tail basin criterion additionally requires

```math
v_2(k)\equiv0\pmod2.
```

There are exactly

```math
\boxed{525189}
```

such integers in the interval. Their two-adic distribution is:

| `v_2(k)` | Count |
|---:|---:|
| 0 | 393891 |
| 2 | 98472 |
| 4 | 24618 |
| 6 | 6155 |
| 8 | 1539 |
| 10 | 385 |
| 12 | 96 |
| 14 | 24 |
| 16 | 6 |
| 18 | 2 |
| 20 | 1 |

The canonical SHA-256 hash of the increasing offset list is

```text
99eb9011d140b420ddf4bd2bf33b6d98d9381b36e12089e231eda8323c548e60
```

---

## 4. Distinct infinite tails

For each valid initial offset `k`, define

```math
k_n=4^nk,
```

```math
R_{10+n}=2L_{10+n}+k_n,
```

and apply exact three-translate reproduction at scale factor `8`.

The basin criterion proves that every resulting state is four-term-progression-free and exact-backbone. Distinct initial offsets give distinct first separations and therefore distinct first child states. Their later offsets remain distinct after multiplication by `4`.

Thus `S_10` is the root of at least `525189` distinct certified infinite exact tails.

---

## 5. Common terminal charge

The state size, scale, and certified replay multiplicity are independent of which valid offset is selected. Every tail has the same total certified weighted density:

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{4P_{10}(|S_{10}|+1)}{L_{10}}
=
\frac{33215}{16384}.
}
```

This demonstrates that the summable basin at `S_10` has substantial width in the separation parameter. It remains possible that other descendants of `S_10` avoid all these scheduled exact tails; the whole-tree problem is still open.
