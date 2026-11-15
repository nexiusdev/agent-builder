# TODO
- [x] Inspect upstream template and preserve MIT attribution.
- [x] Add method, questions, skills, templates and fictional exercise.
- [x] Four helper tests passed: scaffold, no overwrite, missing files, skill metadata.
- [ ] Evaluate real assistant behavior in target host with user examples.

## Operating-model update
- [x] Separate agent register, workflow catalog, immutable event ledger and learning proposals.
- [x] Add role boundaries, routine flows, bounded autonomy and proactivity guidance.
- [x] Preserve existing-project records during upgrade.
- [x] Six unit tests pass; live host behavior and integrations remain untested.

## Communication design update
- [x] Add communication-design skill, questions, contract and example envelope.
- [x] Add offline envelope validator and six validation tests (12 total tests passing).
- [ ] Validate delivery, acknowledgement, duplicate/cancellation handling and authentication in actual host runtime; no transport implemented.

## Deliverable design
- [x] Add explicit owner/consumer, format, evidence, review, lifecycle/version/access and handoff contract.
- [x] Add discoverable skill, questions and offline validator.
- [x] 18 tests pass; actual quality, approval and delivery verification require host integration.

## Individual communication and handoff clarification
- [x] Communication/handoff design applies to every individual agent, including human-facing interactions.
- [x] Init and upgrade create inactive communication contracts without replacing existing ones.
- [x] 20 tests pass, including new scaffold contract and preservation cases.

## Required per-agent task tracking
- [x] Default local operational to-do, explicit tracker configuration and preservation-safe upgrades.
- [x] Add ownership/status/conflict guidance and local locking/revision updater.
- [x] 24 tests pass; builtin board integration remains unimplemented.

## Public personal-use release
- [x] Adapt repository positioning for practical personal use; retain upstream MIT attribution.
- [x] 24 tests and both offline validators pass; diff whitespace check passes. Inspected tracked files and scanned 82 history blobs for common secret patterns; no findings (not an exhaustive security guarantee).
- [x] Align method documentation to seven checkpoints with progressive prompting throughout.
- [x] Published to https://github.com/oruenboi/agent-builder using GitHub CLI. Verified public visibility, MIT license and release commit ff1557a3b371f519a0c515e56401b85dfba192d2 on main. No GitHub CI checks are configured.
