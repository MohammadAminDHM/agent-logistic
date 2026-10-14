# Optional tools: use only the section relevant to this task

AgentKit scaffolds these procedures; it does not install tools, execute them,
change agent hooks, initialize Spec Kit or send repository content to a model.
Check the installed tool's help/version before using examples. Review any
external initialization in a disposable copy before applying it to real work.

## RTK: compact routine terminal output

Upstream: https://github.com/rtk-ai/rtk

After separately installing RTK through its documented platform method:

```text
rtk --version
rtk git status
rtk git diff --stat
rtk gain
```

Use supported RTK filters for repetitive status, search and test summaries.
Read complete source and raw diffs for permissions, payments, data isolation,
migrations and ownership changes. If a summary omits needed failure details,
rerun the failing command unfiltered, preserving its exit code and full output
in an appropriate local artifact. Never replace validation with a compact log.

Hook setup is host-specific and may modify global files; AgentKit does not run
`rtk init`. Use explicit commands until the host integration is separately
reviewed. Do not enable proxies, API routing or telemetry as part of scaffolding.
Keep RTK external; editions have different licenses, so review the applicable
edition before embedding or reselling it in a service.

## Graphify: ask a bounded code question

Upstream: https://github.com/Graphify-Labs/graphify
Python distribution: `graphifyy`; executable: `graphify`.

For an existing, current `graphify-out/graph.json`:

```text
graphify query "Which code handles tenant authorization?" --budget 1200
graphify path "ExactSourceSymbol" "ExactDestinationSymbol"
```

Use real graph symbols for path queries. Confirm relevant source locations;
inferred edges are leads, not established facts. If the graph predates changed
code, refresh the affected graph before relying on it. For a selected local
code-only build, check help first; the reviewed CLI supports:

```text
graphify extract . --code-only --no-cluster
graphify cluster-only . --no-label
```

These commands create graph artifacts; they are not read-only checks. Code-only
graphs omit document semantics. Mixed-document extraction can use a model and
may send content externally: select an authorized backend and corpus first.
Exclude credentials, private payloads and generated/vendor trees. Reuse the
graph between questions; do not rebuild on every turn. If unavailable, use
`rg` and targeted file ranges without blocking delivery on tool installation.

## Spec Kit: one canonical spec per feature

Upstream: https://github.com/github/spec-kit
Current documented CLI needs Python 3.11+; AgentKit itself still needs 3.10+.
The reviewed CLI uses `--integration`, not older `--ai` examples.

```text
specify --version
specify init --help
```

For a new disposable directory, with the selected integration installed:

```text
specify init my-saas --integration codex
```

The native agent process is constitution once, then specify, plan, tasks,
implement and converge for the selected feature. Clarify critical unknowns
and analyze consistency when needed. Skills/commands run in agent chat, not
in the terminal; names and separators vary by integration and installed version.
Use the generated integration's actual names instead of inventing slash commands.

Reuse an existing `.specify/` and `specs/<feature>/` setup. Do not blindly run
`specify init --here --force` against existing work: it can overwrite files.
Review a baseline and a disposable-copy diff before explicitly authorizing
initialization. AgentKit supplies no automatic Spec Kit or cross-host adapter.
