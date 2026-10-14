# Publishing the development preview

The published version is [**0.1.0.dev1**](https://pypi.org/project/smartera-agentkit/0.1.0.dev1/), a pre-alpha prototype with the safety
limitations listed in README. Publication does not complete T01–T08 or establish
production safety. Do not promote it to a stable version without those gates.

The local checkout is now **0.1.0.dev2**, with the SaaS workflow profile described
in `WORKFLOW_INTEGRATIONS.md`. It has not been published. The workflow and local
artifact paths target dev2 for the next explicitly authorized publication;
historical dev1 release evidence below remains unchanged.

## Account setup

The repository remote is `MohammadAminDHM/agent-logistic`, default branch `main`.
Register a pending publisher at <https://pypi.org/manage/account/publishing/>:

| Field | Value |
| --- | --- |
| PyPI project name | `smartera-agentkit` |
| GitHub owner | `MohammadAminDHM` |
| Repository | `agent-logistic` |
| Workflow filename | `publish.yml` |
| Environment | `pypi` |

The owner reported completing this setup on 2026-10-14. A direct PyPI JSON
lookup returned HTTP 404 on that date. This does not reserve or guarantee
availability of the name; only a successful upload establishes ownership.

The GitHub `pypi` environment requires review by `MohammadAminDHM` and permits
deployments from `main`. Self-review is permitted so the owner can approve a
manually started release. No PyPI token is stored in source files.

If Trusted Publishing cannot be matched, a replacement PyPI API token may be
saved as the repository Actions secret `PYPI_API_TOKEN` at
<https://github.com/MohammadAminDHM/agent-logistic/settings/secrets/actions>.
The publish step uses this secret when present, otherwise it uses GitHub OIDC.
The secret is passed only through `UV_PUBLISH_TOKEN` in that upload step; it is
not exposed to build or verification jobs or put on the command line.
Never paste tokens into chat or commit them. Revoke any token shared in chat
before configuring a replacement. For the first upload of a new project, the
token needs permission to create a project; it can be replaced with a
project-scoped token after the project exists.

## Release steps

1. Review and explicitly authorize committing/pushing the project and publishing
   workflow to `main`. Local AGENTS.md prohibits automatic commits and pushes.
2. Open the repository's **Actions → Publish development package to PyPI**.
   Choose **Run workflow** on `main` and acknowledge the prototype limitations.
3. The workflow builds a wheel and sdist once, checks metadata, and tests the
   wheel and a rebuilt sdist on Windows, Linux and macOS with Python 3.10–3.12.
   It stops on any failure. Windows accounts without symlink privileges skip
   that specific test with an explicit reason; other failures are not skipped.
4. Review the matrix results and approve the waiting `pypi` environment job.
   That job uploads the tested artifacts using the configured Actions secret
   or GitHub OIDC and verifies the exact published version through uvx with a
   fresh cache.
5. After the next dev2 publication, verify the public journey (dev2 is not yet
   available at the time of this local change):

   ```bash
   uvx --from 'smartera-agentkit==0.1.0.dev2' smartera-agentkit --help
   uvx smartera-agentkit --help
   ```

   The pinned command is the explicit development-preview installation. Verify
   unpinned resolution before advertising it. Update README's availability
   statements only after the upload and public installation have succeeded.

The workflow only runs manually, never on ordinary pushes or pull requests.
It grants OIDC upload permissions only to the publish job. The npm package
remains private and is not published by this workflow. Version updates must
also update artifact paths in the npm launcher, smoke script and workflow.

## Local evidence on 2026-10-14

- Source tests: 6 passed, 1 skipped (Windows symlink privilege 1314).
- Wheel and sdist built with `uv build --no-sources --out-dir dist`.
- Both distributions passed `twine check --strict`.
- Release wheel and wheel rebuilt from the sdist passed
  `python scripts/smoke_launchers.py --wheel-only --python 3.12`, with the
  rebuilt artifact supplied through `--wheel` for the second invocation.
- [Release run 38549929006](https://github.com/MohammadAminDHM/agent-logistic/actions/runs/38549929006)
  built and checked both distributions and passed all nine OS/Python matrix
  jobs after commit `0901874` was pushed to `main`.
- Two approved upload attempts failed during OIDC token exchange with PyPI
  `invalid-publisher` (no publisher matching the presented claims). Neither
  attempt uploaded a distribution.
- [Release run 38557202164](https://github.com/MohammadAminDHM/agent-logistic/actions/runs/38557202164)
  succeeded after commit `bcb20e7`, using the replacement Actions secret.
  Build, all nine matrix jobs, protected upload and the workflow's fresh-cache
  public installation check passed. Both the wheel and sdist are on PyPI.
- A separate Windows check queried public PyPI metadata and installed the pinned
  version and bare `uvx smartera-agentkit --help` with fresh caches, outside the
  checkout with `PYTHONPATH` removed. Public list, dry-run, initialization with
  spaces/Unicode, existing instruction preservation, repeat-run bytes/mtimes,
  read-only doctor and invalid-profile exit code also passed. UTF-8 was enabled
  for redirected output. No complete T01–T08 or production-safety claim is made.

PyPI distributions are immutable. Future changes require a new version and
updated artifact paths; do not rebuild different files under `0.1.0.dev1`.

Official references: [PyPI pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/),
[GitHub publisher fields and environments](https://docs.pypi.org/trusted-publishers/adding-a-publisher/),
[uv package publication](https://docs.astral.sh/uv/guides/package/).
