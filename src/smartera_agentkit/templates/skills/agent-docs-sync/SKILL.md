---
name: agent-docs-sync
description: Synchronize project agent documents when substantial verified changes make them stale.
---

# agent-docs-sync

1. Inspect the actual changed source, tests and available logs.
2. Identify only affected agent docs, current task state and ADRs.
3. Update grounded facts with evidence; preserve unresolved TODOs.
4. Avoid wholesale rewrites and unverifiable success claims.

Inputs: task context and verified project state.

Output: evidence-backed findings and proposed changes.

Verification: report executed checks and checks not run.
