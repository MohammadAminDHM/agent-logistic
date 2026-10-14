---
name: failing-test-diagnosis
description: Reproduce and diagnose a failing test before applying a minimal fix.
---

# failing-test-diagnosis

1. Reproduce using the precise failing command and capture evidence.
2. Identify the first causal error instead of masking symptoms.
3. Apply the smallest authorized fix.
4. Run targeted and meaningful regression tests; report remaining gaps.

Inputs: task context and verified project state.

Output: evidence-backed findings and proposed changes.

Verification: report executed checks and checks not run.
