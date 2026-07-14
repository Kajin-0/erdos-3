# Repository agent instructions

## GitHub Actions

Do not create a new GitHub Actions workflow for an individual theorem, claim number, documentation patch, probe, or one-time result unless no existing reusable workflow can perform the task.

Before adding or changing a workflow:

1. inspect `.github/workflows`;
2. inspect `src/lint_probe_workflows.py`;
3. reuse `.github/workflows/reusable-python-probe-recorder.yml` or the documented canonical pattern;
4. run `python3 src/lint_probe_workflows.py`;
5. run `bash src/test_probe_workflow_helpers.sh`;
6. explain in the change why a new permanent workflow is necessary.

One-time workflows must be deleted after successful execution. Completed documentation patches remain as source scripts and reproducible commands, not permanent writable workflows.

Before committing any change under `.github/workflows/` or matching `src/*probe*`, `src/*workflow*`, or `src/*patch*`, run:

```bash
python3 src/lint_probe_workflows.py
bash src/test_probe_workflow_helpers.sh
```

Do not commit or push unless both commands return exit code `0`. The authoritative contract is `docs/github-actions-workflow-contract.md`; the linter is the executable authority when prose and implementation differ.
