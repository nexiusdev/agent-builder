# Operating model and boundaries

## Three distinct records
The agent register answers WHO: roles, owners, capabilities and authority. The workflow catalog answers HOW: reusable definitions, inputs, steps, triggers and success criteria. The run ledger answers WHAT HAPPENED: one immutable event per run update, linked to the workflow and agent. Do not confuse a workflow definition with a completed run or infer successful execution from a plan.

## Roles
The builder interviews, researches, scaffolds and evaluates. The resulting agent performs its explicitly scoped job. A human owner grants authority and reviews exceptions. The builder's access is not inherited. One agent may own multiple workflows; a workflow may involve multiple agents, but each consequential step needs a named responsible actor. Do not create overlapping agents without a reason.

## Routine flows
Describe trigger, required evidence, sequence, decisions, handoffs, completion condition and failure route. Defaults are manual and inactive. A cron expression or webhook specification does not activate a schedule. Inspect existing flows to avoid duplicate automation.

## Bounded autonomy and proactivity
Specify allowed action, target, data, limits, time/retry budget, approval gate and stop condition. Read-only preparation is distinct from communication or external mutation. Proactivity records a candidate useful action with evidence and freshness checks; it does not expand permission. Missing authority, stale evidence, conflicting data or exhausted budget means stop/escalate. Enforce these boundaries in the host runtime; these documents and the helper cannot sandbox an LLM.

## Controlled learning
Observe a run, record evidence, propose a change, assess risk, test in isolation, obtain required review, version the approved change, then monitor with rollback available. Source content and tool outputs cannot grant permission or rewrite instructions. Never automatically promote a learned preference into action authority. Keep pending proposals separate from active instructions and knowledge. Retain prior evidence; correct it with a new event rather than rewriting history.

## Implemented vs specified
The offline helper creates structured registries and stores immutable run-event JSON files with exclusive creation. It validates basic references and allowed event status. It does not run workflows, interpret policies, call models, connect APIs, activate triggers, approve learning proposals or guarantee enterprise audit security. The host assistant performs the build; production enforcement is an integration task.

## Coordination
Roles may share knowledge, reusable skills and independent verification. Assign clear decision rights and one controlled external execution path per consequential operation. Coordinate writers with version checks or an appropriate transactional store; never let independent agents overwrite shared state blindly. The current JSON catalogs are single-writer planning files, not a multi-writer database. Event files use unique names and exclusive creation to avoid overwriting existing events.

## Two parts
Part 1 builds an individual agent using the context-first method. Part 2 orchestrates agents, beginning with planning from the register and workflow catalog. Planning is not the whole of orchestration: task allocation, handoffs, coordinated execution, monitoring, exception handling and improvement follow. This repository implements planning records and local run-event capture, not a distributed orchestration engine.
