# PB reproducibility manifest generator

## Purpose

External PB/MaxSAT output is not a certificate by itself.  A reproducible experiment must bind the exact model, exact solver output, solver metadata, and independent candidate checks into one machine-readable record.

The script

```text
src/pb_manifest.py
```

generates a JSON manifest with no third-party dependencies.

## Example

```bash
python src/pb_manifest.py \
  --experiment-id cyclic_b55_k4_s21_harmonic_proxy \
  --repo-commit "$(git rev-parse HEAD)" \
  --model models/cyclic_b55_k4_s21_harmonic_proxy.opb \
  --solution solver_outputs/cyclic_b55_k4_s21_harmonic_proxy.sol \
  --output manifests/cyclic_b55_k4_s21_harmonic_proxy.json \
  --base 55 \
  --k 4 \
  --objective harmonic_proxy \
  --expected-size 21 \
  --solver-name RoundingSat \
  --solver-version '<exact version>' \
  --solver-command '<exact command line>' \
  --solver-status OPTIMUM \
  --wall-time-seconds '<measured wall time>' \
  --cpu-time-seconds '<measured CPU time>' \
  --objective-value '<reported objective>' \
  --objective-bound '<reported bound>' \
  --optimality-gap 0
```

Shell quoting and the exact version command depend on the selected solver.

## Recorded hashes

The manifest computes SHA-256 hashes of:

1. the OPB model;
2. the raw solver output.

This prevents a result from being detached from the exact files that produced it.

## Independent checks for feasible assignments

For solver status `OPTIMUM` or `SATISFIABLE`, the generator independently:

1. parses every expected variable `x0,...,x{b-1}`;
2. rejects incomplete assignments by default;
3. records true, false, and missing-variable counts;
4. checks the requested cardinality profile;
5. checks whether digit zero is present when required;
6. rechecks cyclic `k`-AP-freeness;
7. recomputes the shifted Kempner harmonic sum;
8. records whether the independently checked candidate beats the target.

Use `--allow-partial-assignment` only for legacy outputs.  Such a manifest records that the assignment is incomplete and should not be treated as an optimality certificate without separate justification.

## UNSATISFIABLE and UNKNOWN results

For status `UNSATISFIABLE` or `UNKNOWN`, the manifest records the model hash, solver-output hash, command, status, timing, and objective metadata, but sets

```json
"independent_check": null
```

because no feasible assignment exists to recheck.

An UNSAT claim still requires a solver proof/certificate when the solver supports one.  The manifest records provenance; it does not independently prove UNSAT.

## Status discipline

Use exactly one of:

```text
OPTIMUM
SATISFIABLE
UNSATISFIABLE
UNKNOWN
```

`SATISFIABLE` means a feasible candidate was found but optimality was not established.  Do not report it as an optimum.

`OPTIMUM` should be used only when the solver output establishes optimality and the manifest includes the reported objective bound or zero gap when available.

## Publication rule

A solver-backed numerical claim should include:

- the OPB model;
- raw solver output;
- generated JSON manifest;
- any solver proof/certificate;
- the repository commit named in the manifest.

Without these artifacts, the result remains a candidate computation rather than a reproducible certificate.
