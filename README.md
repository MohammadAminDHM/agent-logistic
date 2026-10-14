# Smartera AgentKit — CLI starter / MVP prototype

A **new starter implementation**, reconstructed from `PROJECT_BRIEF_ORIGINAL.md` (the original Oct 7 brief). The original deliverable was a **spec**, not working source. Development preview **0.1.0.dev1** is [published on PyPI](https://pypi.org/project/smartera-agentkit/0.1.0.dev1/). It does **not** claim to finish all 12 Codex tasks or provide production-grade transactions.

## Requirements

Python 3.10+ with no runtime dependencies; for isolated execution use [uv](https://docs.astral.sh/uv/).

The optional `npx` launcher also requires Node.js 18+ with npm, and `uvx` on
`PATH`. It delegates to the same Python CLI without installing dependencies in
the target project or downloading uv automatically.

Release setup and measured publication results are in
[docs/PUBLISHING.md](docs/PUBLISHING.md).

## SaaS workflow in the development checkout

The unpublished **0.1.0.dev2** checkout adds an optional `saas` profile informed
by RTK, Graphify and GitHub Spec Kit:

```bash
uvx --from . smartera-agentkit init /path/to/project --profile saas --dry-run
uvx --from . smartera-agentkit init /path/to/project --profile saas
```

It adds selective-context skills, a small feature-delivery workflow, optional
tool procedures and SaaS acceptance templates. It preserves existing specs and
does not install or execute external tools. Use it with `--profile local-ai` when
both apply. See [workflow integrations and checks](docs/WORKFLOW_INTEGRATIONS.md).
The public `0.1.0.dev1` release does not include this profile.

## Run from PyPI

With uv installed, run from the project you want to scaffold:

```bash
uvx smartera-agentkit --help
uvx smartera-agentkit init . --dry-run
uvx smartera-agentkit init .
uvx smartera-agentkit doctor .
```

To pin the published development preview explicitly:

```bash
uvx --from 'smartera-agentkit==0.1.0.dev1' smartera-agentkit --help
```

Public installation and scaffold preservation were verified outside the source
checkout. Artifact checks passed on Windows, Linux and macOS with Python
3.10–3.12. First use needs the package and a compatible Python runtime available
through network access or local caches. This remains an experimental preview.

## Local install / build

```bash
# From this directory (an online index or populated dependency cache may be needed):
uvx --from . smartera-agentkit --help
uvx --from . smartera-agentkit init /path/to/my-project --dry-run
uvx --from . smartera-agentkit init /path/to/my-project --profile local-ai --project-name MyProject
uvx --from . smartera-agentkit doctor /path/to/my-project
uvx --from . smartera-agentkit list
```

The equivalent local `npx` commands use the built wheel (`npm pack` also builds it):

```bash
uv build --wheel
npx --yes --package . smartera-agentkit --help
npx --yes --package . smartera-agentkit init /path/to/my-project --dry-run
npx --yes --package . smartera-agentkit init /path/to/my-project --profile local-ai
npx --yes --package . smartera-agentkit doctor /path/to/my-project
```

Run these from this checkout. From another directory, replace `.` after
`--from` or `--package` with the absolute path to this checkout. Relative CLI
targets still resolve against the directory you run the command from. On
Windows PowerShell, use `npx.cmd` if execution policy blocks `npx.ps1`.

The npm package is private to prevent accidental publication; bare
`npx smartera-agentkit` is not a supported public installation path.
Local source execution may need network access for build tooling;
offline execution requires a populated cache. The npm launcher follows
[npm exec's local package support](https://docs.npmjs.com/cli/v11/commands/npm-exec/)
and delegates isolation to [uvx](https://docs.astral.sh/uv/guides/tools/).

Windows PowerShell:

```powershell
uvx --from . smartera-agentkit init "D:\Projects\My AI Project" --profile local-ai
```

To rebuild and verify both local artifacts from a disposable directory:

```bash
npm pack --pack-destination dist
python scripts/smoke_launchers.py
```

The smoke script removes `PYTHONPATH` and enables UTF-8 for redirected Python
output. For Unicode target paths in other redirected Windows sessions, set
`$env:PYTHONUTF8 = '1'` before launching. See `docs/DEV_NOTES.md` for measured
results and platform limitations.

Or, if testing locally with installed dependencies:

```bash
PYTHONPATH=src python -m smartera_agentkit init /tmp/try-agentkit --dry-run
PYTHONPATH=src python -m smartera_agentkit init /tmp/try-agentkit
python -m pytest -q
```

## Implemented in this starter

- `init`, `add profile local-ai`, `add skill NAME`, `list`, `doctor` and `--dry-run` / `--json`.
- Bundled base templates, narrow skills, and a `local-ai` profile; `AGENTS.md` keeps all user text outside an owned marker block.
- Preflight checking of conflicting existing files, explicit ownership manifest, hashes, no-op repeat init.
- Symlink-file and symlink-parent refusal for managed file paths.
- Individual same-directory atomic file replacement and simple best-effort rollback on normal exceptions.
- A limited frontmatter checker for bundled skills; full safe-YAML validation is still to be implemented.

## Known gaps / roadmap

**Not production hardened.** The initial implementation is a starting point for Codex tasks T01–T08. It lacks a durable crash-recovery journal, OS-specific junction checks on Windows, durable lock across concurrent processes, and full malicious-path testing. The release workflow now verifies the wheel and a rebuilt source distribution on three operating systems with Python 3.10–3.12; this does not complete the remaining safety gates. It intentionally refuses unsupported `update` (T09, v0.2). Do not treat its preservation behavior as fully transactional in cases of power loss, concurrent processes, or abrupt termination. The master specification and acceptance criteria remain in `PROJECT_BRIEF_ORIGINAL.md`.

The target project does not need any AgentKit dependencies installed; uvx runs
the CLI in its isolated tool environment.
