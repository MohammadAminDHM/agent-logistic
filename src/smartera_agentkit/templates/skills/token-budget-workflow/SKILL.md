---
name: token-budget-workflow
description: Reduce repeated repository discovery and noisy command output during coding tasks while retaining correctness evidence.
---

# token-budget-workflow

1. Read the selected task/spec and current diff summary. Search exact symbols
   before opening files. Start with a small file/line budget and expand only for
   a concrete missing dependency or verification need.
2. If RTK is installed, use its supported commands for routine output. Keep
   unfiltered evidence for ambiguous failures and inspect complete source for
   authorization, billing, data ownership and migrations.
3. If a current Graphify graph exists, query the affected relationship with a
   budget; verify its source locations. Do not rebuild a graph for each question.
   Use narrow native searches when either tool is absent.
4. Save bulky logs as local artifacts and keep a short resumable task state.
   Record actual checks; never interpret compressed output as a passing gate.
5. If present, use repository-root `.agent/quality/TOKEN_BUDGET.md` for comparison
   measurements. Do not claim reduced total token use or faster delivery without
   comparable evidence. Installations, hooks and API proxies require separate
   authorization; this workflow does not enable them.
