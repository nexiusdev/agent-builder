# Agent Builder
A file-native agent that helps build agents through increasing context, for practical personal use, based on Darryl's context-first method. Run it with an assistant that can read and edit files. No model key or package installation is required for the baseline.

## Start
1. Open this folder with your assistant.
2. Say: “Read AGENTS.md. Help me build an agent. Begin with the workspace, inspect what is already available, and ask only the next necessary questions.”
3. Describe the work and provide approved or fictional source material.
4. The builder produces a brief, sourced knowledge, flow, integration research, discoverable skills, tests and operating instructions incrementally.

## Optional local helper (Python 3.10+)
`python scripts/builder.py init /path/to/new-project --name "Support agent"`
`python scripts/builder.py questions knowledge`
`python scripts/builder.py validate /path/to/new-project`
`python -m unittest discover -s tests -v`
The init target must not exist: existing work is never overwritten. Helpers do not connect services or execute generated agents.

## Contents
- docs/method.md: method, checkpoints and interview approach
- config/stages.json: question bank
- .agents/skills/: discoverable builder skills (including launch-and-sync: owner review, handoff, launch and keeping the design in sync with the live agent)
- scripts/sync_live.py: mirrors a launched agent's live description and skills into <project>/live/ with a drift report
- templates/: integration and evaluation templates
- examples/: fictional support-agent example
- raw/ and wiki/: original Agent in a Folder sourced-wiki foundation
- devplan/: scope and validation status

## Limits
Actual reasoning, web research and file edits require a host assistant. No live API integration, scheduler, credential store or production deployment is bundled. Test records are examples, not proof of real-world accuracy. Use host-level controls for security.

## Attribution
Includes the MIT-licensed Agent in a Folder template by oruenboi at commit 871c2f0ce81d48f92c4ec71f561edeec895221a2, https://github.com/oruenboi/agent-in-a-folder. Original LICENSE, bootstrap and nested wiki/raw instructions retained. The initial fictional glossary example remains explicitly separate from the builder method. Darryl's method is captured from the user's project discussion; engineering safeguards and CLI are proposed implementation additions.

## Operating records (v2)
See docs/operating-model.md and templates/*-record.json. New projects include registry/agents.json, workflows/catalog.json, runs/events/ and learning/proposals/. Existing projects can be upgraded with `python scripts/builder.py upgrade PATH`; existing records are preserved.
Record a local event using `python scripts/builder.py event PATH --run-id RUN --workflow-id FLOW --agent-id AGENT --status started --summary "Synthetic check"`. Agent and workflow IDs must already be registered. Each invocation creates a new immutable event; it never starts a real workflow. These records are not a substitute for secured audit storage.

## Communication design
Use docs/communication-design.md, the communication-design skill and templates/message.json. Offline validation: `python scripts/validate_message.py templates/message.json`. It checks structure and vocabulary only; no transport, authentication, deduplication service or lifecycle engine is implemented.

Design deliverables explicitly for both agents and organisations: read docs/deliverable-design.md. Use templates/deliverable.json and `python scripts/validate_deliverable.py templates/deliverable.json`. Structural validation is not verified quality, authority or delivery.

Communication and handoffs are part of individual agent design, not only orchestration. Init and upgrade create docs/communication-contract.json with inactive defaults, preserving existing contracts. Define human-facing handoffs as carefully as agent-facing ones.

## Task tracking for every agent
New and upgraded projects get an operational local task list and explicit tracker configuration. See docs/task-management.md. The local updater supports locks and revision checks; builtin kanban adapters are not implemented.
