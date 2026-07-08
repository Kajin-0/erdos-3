# Cyclic run decomposition of shadow counts

## Status

Proof-audit structural reduction.  This note decomposes the endpoint and interior shadow counts by fixing a nonzero common difference and viewing `A` as a cyclic binary string with no four consecutive ones.

## Setup

Let `A subset F_p` be 4AP-free, with

```math
m=|A|.
```

Fix `d != 0`.  Since multiplication by `d` permutes `F_p`, the sequence

```math
b_t = 1_A(td),
qquad t in F_p,
```

is a cyclic binary string of length `p` with exactly `m` ones.

Because `A` is 4AP-free, this cyclic string has no four consecutive ones.

Decompose it into cyclic runs of ones of lengths

```math
ell_s in {1,2,3},
```

separated by zero gaps of lengths

```math
g_s >= 1.
```

Here `g_s` is the zero gap after the run of length `ell_s`, and before the next run `ell_{s+1}`.

## Endpoint shadow for a fixed difference

Let

```math
E_d = # { t : b_t b_{t+1} b_{t+2}=1 }.
```

Since no run has length larger than `3`, each run of length `3` contributes exactly one consecutive triple, and runs of length `1` or `2` contribute none.  Hence

```math
E_d = # { s : ell_s=3 }.
```

The two endpoint missing-slot shadows are both shifts of this same count.

## Interior shadows for a fixed difference

Define the two interior missing-slot counts

```math
J_{1,d} = # { t : b_t b_{t+2} b_{t+3}=1 },
```

and

```math
J_{2,d} = # { t : b_t b_{t+1} b_{t+3}=1 }.
```

Because there are no four consecutive ones, the first count corresponds to the local pattern

```math
1 0 1 1,
```

and the second to

```math
1 1 0 1.
```

In run-gap notation,

```math
J_{1,d}
= # { s : g_s=1 \text{ and } ell_{s+1} >= 2 },
```

while

```math
J_{2,d}
= # { s : ell_s >= 2 \text{ and } g_s=1 }.
```

Thus the interior shadow counts measure adjacent runs separated by a single zero, with a neighboring run of length at least two.

## Global shadow counts

The global endpoint shadow count is

```math
E = m + sum_{d != 0} E_d,
```

where the `m` term comes from `d=0`.

For the two interior orientations,

```math
I_1 = m + sum_{d != 0} J_{1,d},
qquad
I_2 = m + sum_{d != 0} J_{2,d}.
```

Globally `I_1=I_2` by reversing the common difference, so the common interior shadow count is

```math
I = I_1=I_2.
```

## Consequences

The product-obstruction search can be expressed as follows:

- `E>p` means that, across all nonzero directions, the cyclic views of `A` contain more than `p-m` length-three runs.
- `I>p` means that, across all nonzero directions, the cyclic views contain more than `p-m` single-zero gaps adjacent to a run of length at least two.

The random-scale lower bounds

```math
E,I >= m^3/p
```

mean that these run features occur at least as often as in a random set of density `m/p`.

## Interpretation

This is stronger structural information than the aggregate inequality `2E+2I <= p(p-1)+4m`.

A pure tensor enemy would need many directions in which `A` has either many length-three runs or many single-zero-separated near-runs, while still having no four consecutive ones in any direction.

## Next research question

Can run-level constraints across many directions force an actual 4AP, or at least prove the two-shadow domination implication

```math
E,I >= m^3/p
quad => quad
E,I <= p?
```
