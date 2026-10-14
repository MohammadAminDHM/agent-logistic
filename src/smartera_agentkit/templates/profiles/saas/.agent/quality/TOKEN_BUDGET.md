# Context and delivery evidence

Start from the current task/spec and `git diff --stat`. Open a few exact files
or symbols before expanding to a dependency. As a starting budget, load at most
three source files or about 200 lines per discovery pass; expand when the task
needs it, recording the reason. Never let a budget conceal a critical check.

Use bounded Graphify queries for relationships and RTK for repetitive terminal
output when available. Read raw source for correctness and security decisions.
Keep long logs in local artifacts; return the useful failure and artifact path.
Avoid secrets in logs. After verified work, record a short resumable state with
changed paths, result, next action and unresolved facts. Do not reread every
document or regenerate specs each session.

## Measure rather than promise

For the same task, revision, commands and acceptance checks, record:

| Observation | Baseline | With selected tools |
| --- | --- | --- |
| Actual agent input/output tokens, if exposed | TODO | TODO |
| Terminal output bytes | TODO | TODO |
| Retrieval/build cost and time | TODO | TODO |
| Time to a verified user outcome | TODO | TODO |
| Acceptance failures or rework | TODO | TODO |

Separate graph-build cost from query cost. RTK's output estimates are not a
measurement of the whole conversation or the invoice. Bytes divided by four
are a rough token estimate, not a tokenizer. Report no savings percentage or
delivery-speed improvement without comparable measurements. Missing tools
must fall back to narrow native commands, not prevent implementation.
