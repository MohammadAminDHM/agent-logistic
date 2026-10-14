# SaaS delivery context

Read this for product scope, then load only the workflow needed for the task.
This is an optional AgentKit profile, not a configured hosting service.

## Product decisions

- Target customer and expensive problem: TODO
- One workflow the first customer will pay for: TODO
- First useful outcome and observable acceptance test: TODO
- Existing stack and reuse constraints: TODO; see `TECH_STACK.md`.
- Tenant model and data-isolation boundary: TODO
- Identity provider, roles and authorization rules: TODO
- Pricing hypothesis and billing requirement for this slice: TODO
- Sensitive data, retention and deletion requirements: TODO
- Hosting budget, deployment owner and recovery target: TODO

## Start small

Choose one journey that crosses the real UI, API and persistence boundaries.
Define what the user can do, how success is verified, and what is deferred.
Prefer existing components and managed services when they meet confirmed needs;
do not choose a provider or incur cost from assumptions. Keep secondary personas,
integrations and dashboards out of the first slice unless acceptance needs them.

## Selective routing

- New feature or MVP slice: `.agent/workflows/DELIVERY.md`.
- Optional RTK, Graphify or Spec Kit commands: `.agent/workflows/TOOLS.md`.
- Evidence and context budget: `.agent/quality/TOKEN_BUDGET.md`.
- No existing feature specification: copy the structure from
  `.agent/plans/active/SAAS_SLICE.md` for the selected change.
- Existing `specs/<feature>/spec.md`, `plan.md`, `tasks.md`: use those as the
  single feature record; link from `.agent/tasks/ACTIVE.md`, do not duplicate them.

Fill unknown decisions from user input or repository evidence. These templates
do not establish tested authentication, billing, tenancy or deployment.
