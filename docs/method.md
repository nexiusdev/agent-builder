# Context-first agent-building method

This is a practical method for building a useful agent through increasing, verified context. Work in small prompts and preserve what was learned. More text alone does not make the agent more reliable.

## 1. Establish Agent in a Folder
Create the durable workspace first. Inspect existing files before writing. Establish source storage, knowledge, instructions, plans and a to-do mechanism. Verify that the host assistant can retrieve the right files. Preserve prior work.

## 2. Establish purpose and build knowledge early
Define enough purpose to choose relevant sources, then gather policies, examples and a good outcome. Record provenance, source precedence, gaps and uncertainty. Refine the brief as understanding increases. Do not ask the user questions already answered by approved evidence.

## 3. Design the work using accumulated context
Map triggers, inputs, decisions, outputs, exceptions and review points. Define what success looks like. Start with a provisional flow, then revisit it when tools and tests reveal constraints. Design from the actual work, not a generic component checklist.

## 4. Study API/MCP capabilities and build discoverable skills
Study official documentation and the actual integration. Separate documented capability from verified availability, permissions and tested behavior. Build skills around useful operations, with clear front-matter descriptions, activation cues, required inputs, failure handling and boundaries. Test that ordinary requests select the right skill. Never assume an MCP wrapper exposes every API capability.

## 5. Develop through progressive prompting throughout
Use this loop at every stage: carry forward context → study and propose → build → inspect → correct or extend → persist → next prompt. This is a continuous practice, not a one-time step after research. Keep decisions, evidence and working outputs in canonical files so the next prompt builds on a dependable foundation.

## 6. Complete the individual agent design
Define role, ownership and boundaries; deliverables and acceptance criteria; communication and handoffs; an authoritative to-do list or verified builtin kanban; routine flows and triggers; autonomy and approval limits; useful proactivity; controlled learning and regression review. Keep learning proposals distinct from approved rules. Do not activate external actions or schedules merely because their design exists.

## 7. Test the whole agent and improve the right layer
Run normal, difficult, ambiguous and failure cases. Test retrieval, skill selection, end-to-end flow, handoffs, output quality and permission boundaries. Record repeatable evidence. Fix the deficient source, skill, flow or instruction rather than adding vague prompt text. A complete document or passing offline helper test is not proof that a host agent works reliably.

## Orchestrating multiple agents
Once individual agents are designed, plan their collaboration using the agent register, workflow catalog, deliverable contracts and communication contracts. Give each decision and task a clear owner. Define shared interfaces, escalation, acceptance and coordination without conflicting authority. See operating-model.md, communication-design.md, deliverable-design.md and task-management.md.

## Interview rhythm
Read → identify a gap → ask one to three necessary questions → build → demonstrate → record → continue. Ask about outcomes and constraints, not technical details the builder can research. Stop for consequential ambiguity; otherwise label reasonable assumptions. The CLI question-bank categories are lookup topics, not a mandatory linear interview or an alternative sequence.
