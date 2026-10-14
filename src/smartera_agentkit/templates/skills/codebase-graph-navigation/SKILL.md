---
name: codebase-graph-navigation
description: Trace dependencies and affected code using an existing Graphify graph before targeted source inspection.
---

# codebase-graph-navigation

1. Form one concrete code question. Check whether `graphify-out/graph.json`
   exists and covers the changed code. Do not read the entire graph into context.
2. Query with `graphify query "question" --budget 1200`. Resolve names against
   real graph symbols before using `graphify path "Source" "Destination"`.
3. Open only relevant source locations and tests. Distinguish extracted,
   inferred and ambiguous edges; verify sensitive behavior in raw source.
4. If stale, refresh a deliberately selected corpus when authorized. Code-only
   extraction omits document semantics; semantic extraction needs an authorized
   model/backend. Do not install hooks, upload documents or broaden the corpus
   implicitly. Read repository-root `.agent/workflows/TOOLS.md` when available.
5. If unavailable or not worthwhile for the repository size, use `rg` and exact
   file ranges. Record uncovered dependencies as unknowns rather than inventing
   edges or making graph generation a prerequisite for a small fix.
