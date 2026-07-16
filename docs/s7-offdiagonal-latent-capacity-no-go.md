# Exact S7 off-diagonal latent-capacity no-go

## Status

Exact finite min-cut certificate on the direct `S7` recursive heavy frontier.

Every recursive state has off-diagonal cross-copy pair energy strictly exceeding its own debt. Nevertheless, every physical off-diagonal pair is already present in the entering activated pair union. After entering pairs are reserved, the strict-new off-diagonal capacity is exactly zero.

Thus off-diagonal cross energy is a valid latent pair reserve, but it is not an additional payment source on the recorded frontier.

---

## 1. Recursive frontier

Direct completion of the full activated pair union leaves

```text
recursive heavy shell occurrences = 278
recursive demand                  = 2.365133143358...
```

For every recursive state, remove the matched activated target pairs and retain all unmatched cross-copy pairs.

The statewise symbolic theorem verifies

```math
J(E_{\rm off}(T))
>
\alpha(T)H(T).
```

The minimum exact statewise surplus on this frontier is

```text
0.001483679041...
```

---

## 2. Physical projection profile

Across all `278` recursive states:

```text
off-diagonal pair occurrences = 19,226
distinct physical pairs       = 13,547
```

Every one of those `13,547` physical pairs already belongs to the entering activated pair set:

```text
entering overlaps = 13,547
new pairs          = 0
light overlaps     = 0
```

Therefore the off-diagonal resource is exactly a subset of entering latent pair energy.

---

## 3. Strict-new max-flow

Construct the exact rational flow network

```text
recursive state demand
    -> unmatched cross-copy pairs
    -> residual new physical pair capacity.
```

Capacity policy:

```text
entering activated pair: capacity zero;
light support: subtract previously allocated light load;
otherwise: one reciprocal-gap capacity.
```

The exact flow is

```text
available new capacity = 0
maximum flow           = 0
unmet demand           = 2.365133143358...
```

The minimum cut contains all `278` states and all `13,547` off-diagonal pair nodes, with zero sink capacity.

Thus

```math
\boxed{
\text{strict-new off-diagonal cross-pair payment fails completely on S7.}
}
```

---

## 4. Comparison with gap-triangular flow

The lower-gap horizontal-chain flow succeeds exactly because it treats activated pairs as Bellman child capacity after strict gap descent:

```text
recursive demand          = 2.365133143358...
exact lower-gap flow      = 2.365133143358...
unmet demand              = 0
physical child pairs used = 206
```

The distinction is structural:

```text
off-diagonal test:
  asks for a new resource disjoint from entering A;
  none exists.

horizontal-chain test:
  reuses an entering pair only as a strictly lower-gap child term;
  exact triangular cancellation is valid.
```

---

## 5. Consequence

The off-diagonal theorem remains essential for dense incidence no-go families because its physical union grows quadratically. On the recorded `S7` frontier, however, that quadratic family has already been activated upstream.

Therefore off-diagonal energy must enter any universal potential as one of:

1. latent pair energy already stored in the parent potential;
2. a scale-aware child pair transition;
3. a production-owned occurrence token;
4. a higher-order incidence token when physical projection collides.

It cannot be added as an independent second copy of pair capacity.

---

## 6. Reproducibility

Primary probe:

```text
src/probe_s7_direct_offdiagonal_cross_flow.py
```

Original exact no-go run:

```text
workflow run 29460803873
```

Artifact digest:

```text
sha256:7a98e72556e02bbfb6382c458b9b4c4f3d59e4fcc2fd139907543a1dc763aebd
```

Pair-universe hash:

```text
91a195147a13c7c157bf99d7bdeef2f14be2cda75216b88cfa3c184d8572efe9
```

The probe now records this expected infeasibility as a green exact no-go certificate.