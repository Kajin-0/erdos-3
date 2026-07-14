# Deterministic probe workflow hardening

## Status

Implemented directly on `main` on 2026-07-14. This is an infrastructure result, not a mathematical theorem or certificate.

## Failure that motivated the change

Several experimental workflows deleted optional JSON/summary outputs after a failed compile or probe and then executed a named pathspec such as

```bash
git add -A data/example_probe.json
```

When the optional file had never been tracked and was absent, Git terminated with exit code 128. The staging failure occurred after the workflow had written the real compile/probe status and stderr, so the visible Git error masked the original failure and prevented the diagnostic status from being committed.

## Repository-wide contract

Deterministic Python probes now use one reusable workflow and four shared helpers:

- `.github/workflows/reusable-python-probe-recorder.yml`;
- `src/run_atomic_python_probe.sh`;
- `src/stage_optional_probe_outputs.sh`;
- `src/commit_probe_outputs.sh`;
- `src/assert_probe_status.sh`.

The contract is:

1. probe, summary, and certificate outputs are written to temporary files;
2. an output is moved into `data/` only after the producing command succeeds;
3. stale tracked outputs are removed before execution and their deletions are staged safely;
4. a never-created absent path is ignored rather than passed to `git add`;
5. the status file records compile, probe, summary, verifier, source commit, workflow run, attempt, and stderr;
6. diagnostic artifacts are uploaded for 30 days;
7. the status and any valid outputs/deletions are recorded before the workflow reports the original failure;
8. generated-result writers share the repository-wide concurrency group `probe-result-writers-main`;
9. a result is not rebased and pushed if `src/` or `.github/workflows/` changed after the recorded source commit;
10. a rebase conflict is aborted and reported explicitly.

## Safe optional staging

`src/stage_optional_probe_outputs.sh` implements the required three-way behavior:

```text
file exists                          -> git add -- path
file absent but previously tracked  -> git rm -- path
file absent and never tracked       -> no operation
```

It does not suppress Git errors with `|| true`.

## Validation

`src/test_probe_workflow_helpers.sh` tests:

- staging a new optional output;
- staging deletion of a tracked optional output;
- ignoring a never-created absent output;
- atomic successful probe/summary publication;
- deletion of partial output after a failing probe;
- explicit failure from a preserved status record.

`src/lint_probe_workflows.py` rejects:

- `git add -A data/<specific optional path>`;
- direct redirection into deterministic probe, summary, or certificate paths;
- probe writers that bypass the shared recorder;
- probe writers without the common serialization group.

The linter and helper tests run in `.github/workflows/probe-workflow-lint.yml`, which also commits `data/probe_workflow_lint_status.txt` on pushes so failures remain inspectable after context loss.

## Direct-to-main policy

The repository owner requires generated research results to be recorded without manual PR merges. Accordingly, generated-result writers still commit directly to `main`, but they are serialized and reject stale source rebases. This is safer than the previous independent retry loops but remains intentionally stricter than a fully artifact-only architecture.

Successful and failed run artifacts are retained separately from committed certified results. A probe output is not a durable mathematical claim until its verifier/certificate and certainty-ledger entry are recorded.
