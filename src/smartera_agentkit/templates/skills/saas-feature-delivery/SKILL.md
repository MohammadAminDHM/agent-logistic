---
name: saas-feature-delivery
description: Deliver a bounded SaaS customer journey from acceptance examples through implementation and verified release preparation.
---

# saas-feature-delivery

1. Pick one customer, problem and valuable outcome. Establish acceptance and
   non-goals; resolve critical unknowns before coding permissions or payments.
2. Reuse canonical feature artifacts. With Spec Kit, follow the installed
   integration's specify/plan/tasks/implement/converge process. Otherwise write a
   compact slice plan. Do not duplicate existing specs or regenerate all stages.
3. Trace the minimum affected source and implement the UI/API/storage journey
   as applicable. Prefer established components; defer unrelated dashboards and
   integrations. For a small bug, directly diagnose, repair and verify instead.
4. Test the real user outcome plus tenant isolation, authorization, billing
   event idempotency and recovery when relevant. State what is mocked or blocked.
5. Compare every acceptance example with observed results, reopening gaps.
   Prepare deployment/configuration and rollback instructions; obtain required
   release authorization before deploying or publishing.
6. If present, read repository-root `.agent/context/SAAS.md` and the relevant
   `.agent/workflows/DELIVERY.md` section. Report a verified slice, not an
   assumption that a scaffold is a working or revenue-generating SaaS product.
