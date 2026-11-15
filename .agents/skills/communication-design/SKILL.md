---
name: builder-communication-design
description: Use when designing any individual agent’s communications and human or agent handoffs, or composing those contracts across an organisation. Produces a routing and handoff contract, not a messaging service.
---
# Design organizational communication
Read AGENTS.md and docs/communication-design.md. Inspect agent register and workflow catalog before asking questions.
1. Map decision rights, knowledge dependencies and one responsible execution owner for each consequential operation. Shared knowledge and independent verification remain allowed.
2. Classify necessary messages: request, assignment, acknowledgement, progress, result, question, dissent, escalation, cancellation. Avoid broad broadcasts when a named owner suffices.
3. Define sender-to-recipient routes, permitted types and minimum data. Do not grant access to complete history merely to deliver one task.
4. Specify expected output, evidence references, deadline, acceptance owner and escalation route. Separate delivery acknowledgement, task acceptance, execution and accepted outcome.
5. Define duplicates, late results, stale versions, refusals, conflicting conclusions and lost acknowledgements. Check uncertain execution before retrying.
6. Walk a normal handoff, an adverse case and a dissent case with synthetic messages. Save proposed contracts and test evidence; do not claim runtime enforcement.
Use templates/message.json and docs/communication-design.md. Actual external messaging still needs authorized connectors and runtime checks.

Start with the individual agent contract, even when no other agents exist. Inspect docs/communication-contract.json in the target scaffold. Then compose cross-agent routes if required.
