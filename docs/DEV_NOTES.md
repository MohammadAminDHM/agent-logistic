# Implementation status

This directory was newly reconstructed from the original project brief, not recovered from an old ZIP or git repository. Start from tasks T01–T08 in `PROJECT_BRIEF_ORIGINAL.md`; test every acceptance item. The 0.1.0.dev1 starter deliberately does not implement production-grade journal/locking semantics. Development preview publication and CI results are recorded below and in `PUBLISHING.md`. `uvx --from .` installs a local package and must be run from this directory.

## Initial local uvx and npx checks (2026-10-14, before publication)

- Added a private npm package with a `smartera-agentkit` executable. It passes
  arguments to `uvx --from <bundled-wheel> smartera-agentkit` without a shell,
  retains the caller's working directory and propagates exit codes. uv is a
  prerequisite; the launcher does not install it automatically.
- `uv build --wheel` succeeded on Windows. `npm pack --pack-destination dist`
  builds the wheel through `prepack` and bundles it, preserving Python template
  dotfiles that npm would otherwise omit when packing the source tree.
- `python scripts/smoke_launchers.py` passed against the wheel, npm tarball, and
  local npm checkout, with runtime CWD outside this repository and `PYTHONPATH`
  removed. Each exercised help/list, dry-run without creating a target,
  spaces/Unicode, default target resolution, existing instructions, repeat init
  with unchanged bytes/mtimes, read-only doctor and invalid-profile exit code 2.
  A missing uvx executable also produced the expected diagnostic and exit code 1.
- `PYTHONPATH=src python -m pytest -q tests` (PowerShell equivalent) produced
  **6 passed, 1 failed**. The failing test could not create its symlink because
  Windows returned privilege error 1314; symlink refusal was not verified.
- Initial sandbox attempts could not access user caches/temp; successful build
  and artifact checks used approved access to those directories.
- Unicode output under Windows cp1252 redirection failed before CLI completion.
  The smoke harness explicitly enables `PYTHONUTF8=1`; this does not establish
  compatibility with arbitrary non-UTF-8 output streams.
- Verified here with Node 24.12.0, npm 11.6.2, uv/uvx 0.11.21 and Windows.
  Linux/macOS and minimum Node/Python versions were not tested. No public npm
  or PyPI availability, complete T01–T08 acceptance, or production release is
  claimed. The original brief remains unchanged.

## Published development preview (2026-10-14)

Version `0.1.0.dev1` was published to PyPI through
[run 38557202164](https://github.com/MohammadAminDHM/agent-logistic/actions/runs/38557202164).
All nine release verification jobs (Windows/Linux/macOS, Python 3.10–3.12)
passed before upload. Both the release wheel and a wheel rebuilt from the sdist
were exercised. A separate fresh-cache Windows check verified pinned and bare
uvx installation from public PyPI, plus preservation/repeatability checks outside
the checkout. The initial unprivileged local Windows symlink result above
remains a limitation of that local run; the published preview still lacks the
documented hardening. npm remains local-only. See `PUBLISHING.md` for details.
