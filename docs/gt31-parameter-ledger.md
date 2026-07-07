# GT31 parameter ledger

## Status

Initial workbench for tracking the parameter losses in Green--Tao Theorem 3.1.

## Correction: thickness sign

The useful thickness form is

```math
P(r=0) << exp(eta^{-O(1)})/p,
```

not a negative exponential.  This is consistent with the extracted corollary row

```math
P(r_v=0) << exp(eta^{-C5^2})/p.
```

The gamma diagnostic is unchanged: if

```math
P(r=0) << exp(c eta^{-gamma})/p,
```

then the application to 4AP-free sets gives approximately

```math
r_4(N) << N(log N)^(-1/(4 gamma)).
```

The reciprocal-sum target requires

```math
gamma < 1/4.
```

## Confirmed early rows

| Stage | Input | Output | Loss type | Note |
|---|---:|---:|---|---|
| Cauchy--Schwarz | eta | eta^2 | squaring | Each use can double exponent pressure. |
| Popularity | eta | probability >= eta/(2C) | polynomial | Converts average lower bound to pointwise event. |
| Recurrence theorem | eta | recurrence error O(eta) | error budget | In the 4AP-free application, choose eta about alpha^4. |
| Thickness theorem | eta | exp(eta^{-O(1)})/p | exponential-over-p | Main hidden exponent to extract. |
| 4AP-free application | alpha | alpha^4 <= O(eta)+P(r=0) | counting | Multiplies the thickness exponent by 4. |

## Rows still needing line-by-line extraction

| Stage | Needed data |
|---|---|
| Factor construction | number of factors/atoms as a function of eta |
| Regular probability distribution | radius/thickness loss |
| Energy decrement | number of refinement rounds |
| Local recurrence inside atoms | eta-loss before building r |
| Zero-step avoidance | exact source of P(r=0) |

## Immediate question

Is eta^{-O(1)} mainly from repeated Cauchy--Schwarz squaring, or from Bohr/factor/radius regularization?

These require different attacks.
