# Deliverables are first-class design objects

User clarification: “Deliverables are also part of the agent design and organisations.” This means both an individual agent and the coordinated organisation should be designed around useful outputs, their consumers and acceptance. The field schema below is a proposed implementation of that principle.

## Design before execution
Define the outcome and intended use; producer/owner; consumer; verifier and acceptance authority; required format or schema; evidence and provenance; quality and completion criteria; timing; version and access constraints. A task description without an agreed output contract leaves completion ambiguous. Internal intermediate outputs also need contracts when another agent relies on them.

## Responsibilities and handoff
An agent register records accountable roles. The workflow catalog maps required deliverables and dependencies. A deliverable record describes a specific artifact version and its review status. The run ledger records production, review and handoff events. Communication messages refer to the deliverable ID and exact version rather than an ambiguous “latest”. Share only with authorized consumers; an evidence reference must be accessible to its intended reviewer. Shared knowledge and independent verification remain possible without granting every agent write authority.

## Lifecycle
Proposed states: planned → draft → in_review → changes_requested or accepted → released → delivered; superseded and withdrawn are explicit later states. Content accepted is different from permission to publish; released is different from delivery confirmed. These are design states, not an implemented state machine. A receiving agent or human checks expected version, schema, evidence, completeness and authority before accepting a handoff. Record rejection reason and correction path. Preserve previous versions and do not overwrite accepted artifacts silently.

## Questions
What decision or action should this output support? Who owns and consumes it? What format and fields are required? What evidence must accompany it? Who reviews and accepts it, against which criteria? Is it internal, client-facing or public? Which recipients can access it? When is it due? What is the correction, versioning and withdrawal process? What proves successful delivery and downstream usability?

## Completion checks
Validate structure first, content second, authorization third and actual handoff last. Test missing evidence, wrong format, outdated version, unauthorized recipient, failed delivery and rejected review. The bundled validator checks structure and accepted-state evidence fields only; it cannot verify the truth of claims, identity, permissions, transitions, signature or delivery. Acceptance declarations in untrusted files are not authorization.
