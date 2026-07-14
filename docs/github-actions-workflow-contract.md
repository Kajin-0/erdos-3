# GitHub Actions workflow contract

`src/lint_probe_workflows.py` is the executable authority for writable workflows.

## Ownership

- Use `.github/workflows/reusable-python-probe-recorder.yml` for Python probe/result jobs.
- Completed theorem or documentation patches are run as reproducible commands and do not retain permanent workflows.
- Do not create workflow-per-claim or `one-time-*.yml` infrastructure.
- A recurring documentation writer requires explicit justification and must be the sole owner of its patch scripts, triggers, and authoritative output files.

## Writable workflow sequence

Every direct writer must:

1. use `permissions: contents: write`;
2. serialize with `group: probe-result-writers-main` and `cancel-in-progress: false`;
3. run atomically and capture every applicable `*_exit_status`;
4. write `schema`, source commit/ref, run ID, and run attempt before the first `---` separator;
5. upload status and stderr artifacts with `if: always()`;
6. preserve or commit diagnostics through `src/commit_probe_outputs.sh`;
7. call `src/assert_probe_status.sh` only after artifact upload and preservation.

Use:

- `src/run_atomic_python_probe.sh` for probe/summary/certificate output;
- `src/run_atomic_documentation_patch.sh` for a justified recurring documentation patch;
- `src/stage_optional_probe_outputs.sh` for optional files;
- `src/commit_probe_outputs.sh` for serialized, stale-source-safe publication.

Never use `|| true`, `continue-on-error`, unsafe exact-path staging for optional output, or direct promotion of partial generated files.

See `docs/examples/canonical-documentation-patch-workflow.yml` for the inactive documentation-writer template. Run the linter and helper tests before committing workflow, probe, workflow-helper, or patch changes.
