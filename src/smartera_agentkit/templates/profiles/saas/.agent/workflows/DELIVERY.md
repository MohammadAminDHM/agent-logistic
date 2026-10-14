# Deliver one SaaS slice

1. Read the current task, product decisions and existing feature spec. Identify
   the smallest user-visible outcome. For a small bug, diagnose and repair the
   original symptom directly; a full feature-spec cycle is unnecessary.
2. Record acceptance examples and a short non-goal list before implementation.
   Resolve unknowns that affect permissions, money, data or irreversible actions.
3. Map only affected entry points, dependencies and tests. Use a current graph
   if available; confirm critical paths in source. Do not index a tiny repository
   merely to satisfy a ritual. Preserve the established stack unless evidence
   justifies a change.
4. Plan the thin UI/API/storage path and a focused test for the customer outcome.
   Split work into independently verifiable tasks; add discovered work to the
   same task record instead of expanding scope silently.
5. Implement the working journey, including loading/error/empty states when
   relevant. Use actual authentication and persistence boundaries in acceptance
   checks. Label mocked behavior and external dependencies explicitly.
6. Run focused checks, then the repository's required verification. Record exact
   commands, results and outstanding limits. A passing unit test is not proof
   that a deployed service or paid integration works.
7. Compare implementation against each acceptance example. Reopen missing tasks
   until the slice meets its contract. Distinguish complete, partial and blocked.
8. Prepare a reviewable release: configuration names without secret values,
   migration/recovery steps, health checks, observable errors and rollback.
   Obtain any required authorization immediately before deployment/publication.

## SaaS acceptance when applicable

- A tenant cannot read or mutate another tenant's records, including by ID.
- Server-side authorization protects each sensitive action; UI hiding is not
  enforcement. Expired sessions and denied permissions have tested behavior.
- Billing events are authenticated and idempotent; test duplicate/reordered
  events and server-owned entitlement checks if payments are in scope.
- A failed migration, dependency outage or bad deployment has an exercised
  recovery path, or is reported as an unresolved release limitation.
- Logs omit credentials and personal payloads. User export/deletion follows the
  chosen policy. Set actual limits for expensive operations.

Use Spec Kit's native process when installed and selected; see `TOOLS.md` for
version-dependent invocation. Otherwise keep a short spec, plan and task list
in the slice document. Do not maintain two competing versions of the same spec.
