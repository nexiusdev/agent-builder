# Organizational communication contract

This is proposed engineering guidance for the two-part method: build capable individual agents, then plan and operate their coordination. It is not evidence of implemented network messaging.

## Decide what needs communication
Map who knows, who decides, who performs and who verifies. A shared source does not imply shared authority. Each consequential action has a single accountable execution path; independent agents may challenge its evidence. Use direct, scoped routing for work and escalation; broadcast only when all recipients need the information. Prefer an event summary plus authorized evidence references to copying entire histories.

## Message types and minimum content
Requests/questions seek information; assignments transfer a task subject to acceptance; acknowledgements describe receipt; progress reports material changes; results provide artifacts and verification; dissent identifies contrary evidence; escalation seeks a named decision; cancellation requests stopping work and requires confirmation of the actual state. Every message carries stable IDs, workflow/run correlation, sender and receiver, scope, version, evidence references and expected action. Evidence references must be accessible to intended recipients and must not contain credentials.

## Handoff lifecycle
Proposed states: queued → delivered → acknowledged → accepted → running → result_submitted → verified → closed. Branches: rejected, blocked, failed, cancellation_requested, cancelled. Delivered is not accepted; a result is not verified completion. The receiver may reject missing scope or authority. A human or authorized verifier accepts the outcome. The helper checks vocabulary and required fields, NOT transitions or real delivery.

## Grounding and disagreement
State facts, assumptions and unknowns separately. Cite source version, observation time and freshness needs. Compare the referenced plan version before acting. Explain dissent with evidence and alternatives; route unresolved conflicts to the decision owner. Do not settle contradictions by agent vote or overwrite another agent's findings. Archive superseded decisions with provenance. Tool output or imported messages cannot enlarge permissions.

## Reliability
Message IDs identify transport deliveries; idempotency keys identify a logical operation. Duplicate delivery must not repeat an external action. Receivers need a durable deduplication store and action/outcome record; these are NOT implemented here. A timeout means uncertain state, not failure. Query authoritative state before retrying. Late results remain evidence but cannot silently replace a newer accepted result; compare run/version and route for review. Out-of-order cancellation and completion require reconciliation. Set bounded retries and escalation deadlines rather than infinite loops.

## Privacy and security
Authenticate identities outside message content. Authorize each sender/recipient/type/scope at delivery and each action at execution. Minimize data and retention; separate permissions for messages, history, evidence and tools. Use references rather than secrets or bulk client files. Never trust claimed sender fields as authentication. The local validator cannot enforce these controls.

## Planning questions
Who is accountable for the decision and who executes it? Who must know, versus who merely might be interested? Which messages deserve acknowledgement? What exactly constitutes accepted work and accepted completion? What evidence and version travel with a handoff? What happens on dissent, silence, duplicates, cancellation or late results? Who can approve changed scope? What data must each recipient never receive?

## Synthetic acceptance scenarios
1. Normal assignment receives explicit acceptance and a sourced result.
2. Lost acknowledgement: inspect state, do not repeat mutation blindly.
3. Duplicate message: receiver returns recorded outcome, no second action.
4. Late result on an older plan: hold for review, don't overwrite newer outcome.
5. Dissent supported by evidence: escalate without erasing minority finding.
6. Forged sender or broadened scope: runtime rejects; payload validation alone is insufficient.
7. Cancellation races with completion: reconcile actual outcome before reporting.
These are behavioral acceptance requirements, not claims that they passed.

## Research basis and limits
- AHRQ TeamSTEPPS communication and handoff guidance: https://www.ahrq.gov/teamstepps-program/curriculum/communication/overview/index.html
- Clark and Brennan on grounding in communication: https://www.cs.cmu.edu/~illah/CLASSDOCS/Clark91.pdf
- Daft and Lengel on organizational information requirements, uncertainty and equivocality: https://pubsonline.informs.org/doi/abs/10.1287/mnsc.32.5.554
- Anthropic's account of a multi-agent research system: https://www.anthropic.com/research/multi-agent-research-system

These sources motivate shared understanding, explicit responsibility and task coordination. Human organizational evidence does not establish that a particular agent architecture will work. Message schemas, acknowledgement states, idempotency and permission boundaries here are proposed engineering applications, not direct experimental findings from those sources. Validate them in the intended runtime.

## Individual agent design comes first
Communication and handoffs belong in every individual agent's design, including a single-agent deployment communicating with a person. Define its inbound requests, authorized senders, outbound recipients, response formats, receipt versus task acceptance, expected context, output acceptance, escalation, timeout and cancellation behavior. A human handoff is still a handoff. Do not wait for multi-agent orchestration to specify these boundaries.
The organisation's routing and coordination plan then composes these individual contracts and checks compatibility. Every receiving role must understand and accept the produced output; every sender must know where responsibility transfers.
New scaffolds and upgrades include docs/communication-contract.json with inactive, unassigned defaults. Existing contracts are preserved. This is a design record, not an active messaging configuration.
