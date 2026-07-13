# Exact equal-rank sampler for the lifted-completion residual

## Status

Exact deterministic generator, not yet a witness-classification theorem.

The certified lifted `S_9` completion reduction leaves an ordered residual of

```math
N=177844250
```

sponsor-compatible, layer-disjoint `S_10` factor-four separations. Its certified invariants are

```text
first separation:  97474324
last separation:   613454687
FNV-64:            00369694f2d70526
```

The new sampler regenerates this residual from the same `S_9` completion bitsets and selects `512` midpoint equal-rank samples.

**Sampler:** `src/sample_depth10_lifted_s9_completion_residual.cpp`  
**Runner:** `src/run_sample_depth10_lifted_s9_completion_residual.sh`

---

## 1. Equal-rank definition

For

```math
0\le j<512,
```

the selected zero-based residual rank is

```math
\boxed{
q_j=
\left\lfloor
\frac{(2j+1)N}{1024}
\right\rfloor.
}
```

Thus each sample represents the midpoint rank of one of `512` equal-mass bins in the actual residual candidate list. This avoids the bias produced by sampling equal-width intervals in `R`, because sponsor compatibility, layer disjointness, and lifted-completion coverage are not spatially uniform.

For every selected separation `T`, the output also records

```math
U=T-4R_9,
\qquad
|U|,
```

where

```math
R_9=134217729.
```

These are the effective coordinates required by the exact `k=4` rectangle-transport channel.

---

## 2. Fail-closed audits

Before writing any sample row, the program independently checks:

1. `13,923,661` signed `S_9` completion coordinates;
2. `71,129,286` completion-to-base differences;
3. `354,838,701` lifted completion-support values;
4. the exact recursive `S_10` positive-difference support;
5. residual count `177,844,250`;
6. residual endpoints `97,474,324` and `613,454,687`;
7. ordered residual FNV-64 `00369694f2d70526`.

A mismatch aborts the run before the sample file is produced.

---

## 3. Output

The generated file has columns

```text
index rank separation signed_u abs_u
```

and exactly `512` data rows. The runner prints both:

- the FNV-64 hash of the ordered sampled separations;
- the SHA-256 hash of the complete output file.

The intended next stage is to classify these exact residual samples by outer layer word `lambda`, parent word `mu`, and ancestor-level obstruction mechanism. The sampler itself makes no claim that any sampled candidate is excluded or survives.

---

## 4. Reproduction

```bash
bash src/run_sample_depth10_lifted_s9_completion_residual.sh
```

The command first regenerates and verifies the certified lifted-completion objects, then scans the complete residual and writes the equal-rank sample.
