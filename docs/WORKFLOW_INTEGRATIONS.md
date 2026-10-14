# SaaS delivery with bounded coding context

The **unpublished 0.1.0.dev2 checkout** adds an opt-in `saas` profile. The public
`0.1.0.dev1` release does not contain this profile. This is a user-requested
workflow/template addition within the existing scaffolding CLI; it does not
complete the outstanding MVP preservation/recovery gates or implement a SaaS.

## Try it locally

```bash
uvx --from . smartera-agentkit init /path/to/project --profile saas --dry-run
uvx --from . smartera-agentkit init /path/to/project --profile saas
uvx --from . smartera-agentkit doctor /path/to/project
```

For an initialized target, use `add profile saas /path/to/project`. Profiles
compose: `init /path/to/project --profile saas --profile local-ai`. Both routes
use the existing preflight/ownership engine; repeated additions are no-ops.
Existing `.specify/`, `specs/`, application files and user-owned profile documents
remain untouched. No external command is run by profile installation.

| Generated resource | Purpose |
| --- | --- |
| `.agent/context/SAAS.md` | Product decisions and selective routing |
| `.agent/workflows/DELIVERY.md` | Small user journey and acceptance/recovery checks |
| `.agent/workflows/TOOLS.md` | Optional RTK, Graphify and Spec Kit procedures |
| `.agent/quality/TOKEN_BUDGET.md` | Context budget and measurement worksheet |
| `.agent/plans/active/SAAS_SLICE.md` | Blank slice worksheet when no canonical spec exists |
| `token-budget-workflow` skill | Bounded discovery, compact routine output, raw critical evidence |
| `codebase-graph-navigation` skill | Budgeted graph navigation with source verification |
| `saas-feature-delivery` skill | Acceptance, thin implementation, convergence and release preparation |

The root instruction block contains one routing sentence for this profile,
not all its documentation. Skills load details only when relevant. Unknown
product facts remain TODO; strict doctor reports them rather than implying
that a scaffold proves application behavior.

## What each upstream contributes

Sources reviewed on 2026-10-14:

- [RTK](https://github.com/rtk-ai/rtk): routine terminal-output filtering and
  output measurement. Sensitive source/diff review remains unfiltered.
- [Graphify](https://github.com/Graphify-Labs/graphify): persistent dependency
  context, bounded questions and source locations. Code-only graphs omit docs.
- [Spec Kit](https://github.com/github/spec-kit): an explicit feature contract,
  implementation tasks and convergence. Reuse its existing artifacts rather
  than generating a competing specification tree.

These tools are optional, external dependencies. AgentKit does not bundle their
source/binaries, initialize global hooks, enable an API proxy, set model
credentials, choose a cloud provider, or deploy a paid service. Our generated
procedures are original instructions with upstream attribution. Check upstream
licenses for embedding/resale, including RTK edition differences.

Graphify's current shell entry point is `graphify extract . --code-only`; older
examples using a bare path may differ. Spec Kit 1.0.6 uses `--integration codex`
and installed `$speckit-*` skills in the checked fixture. These are agent
invocations, not terminal commands. Other versions/integrations can differ.

## Observed checks, with limits

- Local Python suite: 16 passed, 1 Windows symlink-privilege skip. It exercises
  profile composition, preview/no-op behavior, preservation, malformed ownership
  conflicts, independent skill installation and doctor dependency checks.
  The SaaS root instruction block is 1356 UTF-8 bytes versus 1125 for base-only;
  detailed procedures stay in selectively loaded files. This is a context-size
  observation, not a measured token-saving percentage.
- All three added skills passed the skill-creator metadata validator.
- dev2 wheel and sdist builds and strict Twine checks passed. The wheel, npm
  archive and local npx launcher passed the combined SaaS/local-ai smoke checks
  from an unrelated temporary working directory, including repeatability and
  preservation. A wheel rebuilt from the sdist passed the same wheel-only check.
- RTK **1.0.0 OSS**, downloaded into ignored local artifacts from the official
  release and checked against its published SHA-256, ran without global install
  or hook setup. On one synthetic repository with 30 untracked files,
  `git status` emitted **944 bytes** and `rtk git status` **837 bytes**, both
  exit 0. This modest example is not an agent-token, cost or delivery benchmark.
- Installed Graphify **0.9.65** extracted a synthetic three-file code corpus
  without model calls: **6 nodes, 9 edges**, then 2 communities with labels
  disabled. A query budgeted to 1200 returned the relevant calls/imports and
  source lines. One document was explicitly omitted by code-only extraction.
- Installed Spec Kit **1.0.6** initialized an isolated Codex fixture, generated
  `.specify/memory/constitution.md` and the expected `.agents/skills/speckit-*`
  files. This validates CLI setup, not actual host discovery or model behavior.
- No measured reduction in total conversation tokens, invoice cost, rework or
  time to revenue is claimed. Use the generated measurement worksheet for
  comparable workloads. This implementation was exercised locally on Windows;
  the older release's CI results do not establish this revision's platform gates.

The integration fixtures, logs and downloaded test binary live under ignored
`.artifacts/`. They are not runtime dependencies or package contents.
