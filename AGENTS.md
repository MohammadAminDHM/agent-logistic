# Working on Smartera AgentKit

Read `PROJECT_BRIEF_ORIGINAL.md` for the original product requirements and 12 ordered Codex tasks. The existing source is a **prototype**, not a completed production release. Follow `README.md` for local usage and known gaps.

- Preserve the original project brief exactly.
- Implement tasks T01–T08 before v0.2+ enhancements; do not claim unverified gates passed.
- Treat preservation, read-only dry-run, safe file ownership and ability to recover from failures as critical requirements.
- Run `PYTHONPATH=src python -m pytest -q tests`; build a wheel and smoke-test it outside the checkout.
- Do not automatically commit, push, publish to PyPI, or modify unrelated repositories.
- Report actual checks and cross-platform validation limitations.
