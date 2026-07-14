# Retained terminal sink identity ledger

## Status

Exact finite identity export for the certified second-generation retained family.

The source objects are unchanged:

- the `local37` first-generation policy;
- the unique `21`-state point-disjoint retained family;
- lexicographic coordinated deletion on those states;
- global exact-state quotienting and maximum-harmonic same-shell conflict selection;
- the resulting `27` retained second-generation states and `7,925` retained points.

The terminal/recursive split contains `13` three-term-progression-free terminal states with `43` points and `14` recursively continuing states with `7,882` points.

**Exporter:** `src/export_retained_terminal_sink_ledger.py`.

**Summary certificate:** `data/retained_terminal_sink_identity_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
1f25e54d10d73c0130535d12f264405f0e5adb954820725395deb7c86ac19bf9
```

---

## 1. Identity schema

The exporter writes one canonical JSONL record for each terminal retained state. Every record contains:

```text
class index
representative occurrence
first-generation parent class
source type and source step
dyadic exponent
complete numerical value set
complete root-provenance vector
complete immediate-provenance vector
pointwise scale records
```

Each pointwise record contains the descendant label `u`, original `S_7` root provenance `p`, immediate provenance, source, source step, dyadic shell, shell-depth drop, and exact lower and upper binary-log contraction.

The export is anchored to two previously certified immutable objects:

```text
second-generation retained-family SHA-256
  dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596

full 7,925-point ratio-record SHA-256
  904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3
```

The terminal numerical-state family is independently anchored by

```text
0aa2aca9246119f832bb3b58dcc090683c41fb85ed3c47d5c73d0b398dfc672e.
```

---

## 2. Exact one-generation ledger properties

Within the certified second-generation retained family:

```text
terminal sink states = 13
terminal sink points = 43
terminal numerical labels are pairwise unique
terminal numerical labels are disjoint from all recursive retained labels
terminal point tokens (u,p) are pairwise unique.
```

Therefore every terminal numerical point and every terminal `(descendant, root-provenance)` token can be charged exactly once inside this recorded family.

This strengthens the terminal/recursive split from a mass statement to an explicit identity ledger. The `86.2%`–`86.3%` terminal mass is no longer an anonymous error term: every contributing state and every contributing point has a deterministic numerical and provenance identity.

---

## 3. Scope

The theorem is deliberately local to the certified two-generation family. It does **not** prove that:

- the same numerical terminal state cannot be recreated by another branch;
- the same `(u,p)` pair cannot reappear after a later recursive transformation;
- root provenance alone is a globally injective terminal identifier;
- terminal sink mass is globally summable;
- or the recorded recursive contraction is universal.

The remaining theorem must control recreation across branches and generations. The natural next tests are:

1. compare terminal sink tokens against every earlier retained and raw output token;
2. propagate only the `14` recursive retained states and test whether any third-generation terminal token repeats a recorded sink token;
3. determine whether a path-augmented provenance token is injective or has bounded multiplicity;
4. export a Bellman row with separate `RecPack` and first-appearance `TermSink` coordinates.

---

## 4. Reproduction

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The runner regenerates and byte-compares the fixed summary certificate, reconstructs the complete terminal JSONL ledger, and verifies that it contains exactly `13` state records.

This check is part of the manually triggered extended workflow. It is not part of push-gating lightweight CI.
