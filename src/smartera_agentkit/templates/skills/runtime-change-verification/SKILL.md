---
name: runtime-change-verification
description: Verify observable runtime changes beyond syntax checks.
---

# runtime-change-verification

1. Write a testable scenario and expected visible behavior.
2. Run the actual workflow in a disposable environment where possible.
3. Exercise one failure path and assess regression impact.
4. Report command, environment, actual output and limitations; do not invent passing tests.

Inputs: task context and verified project state.

Output: evidence-backed findings and proposed changes.

Verification: report executed checks and checks not run.
