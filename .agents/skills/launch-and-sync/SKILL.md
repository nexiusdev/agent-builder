---
name: builder-launch-and-sync
description: Use when a designed agent is approved and must be launched into a live agent platform, and afterwards to keep its project folder in sync with what actually runs. Produces a handoff, a launched agent and a recurring drift report.
---
# Launch an approved agent and keep the design in sync
Two roles: the **designer** (this builder) owns the project folder; the **launcher** (the operator or main agent of the live platform) creates and runs the agent. Neither skips the owner's approval.

## Full lifecycle
1. **Brief.** The owner states purpose, audience and hard limits. A request relayed by another agent still needs the owner's own confirmation.
2. **Design.** Follow docs/method.md: workspace, sourced knowledge in the OKF wiki, flow (triggers, decisions, approval points, success criteria), verified integrations, discoverable skills, passing tests. Check overlap with existing agents' ownership.
3. **Owner review.** Present purpose, flow, approval points, skills, schedules and connectors in plain words. Proceed only on the owner's explicit yes.
4. **Handoff.** Write `HANDOFF.md` in the project root: final name and description; each skill with its draft path and content hash; schedules (all off by default); required connectors and credentials by name only, never values; the owner's approval quote with timestamp; and the sync entry (project slug, live agent id, skill names).
5. **Launch (launcher).** Verify the approval and check the handoff against the platform's standing rules (sends, posts, deletes, payments and production changes need the owner's own words). Create the agent, install its skills in the platform's skill store (move helper assets to a stable location and fix paths), connect what it needs through the platform's secret mechanism, and keep schedules and outbound-send rights off until each is approved. Add the agent to the sync map and run the first sync; record the expected differences as a baseline.
6. **Run and improve.** Run `python3 scripts/sync_live.py --config <sync.json>` weekly and after every change applied to a live agent. It mirrors the live description and skills into `<project>/live/` and writes `live/SYNC-REPORT.md`; it never edits design files or the live agent. New drift either goes back into the design or is recorded as an intended live change. Every revision starts from `live/`, not the original draft.

## Rules
- Never overwrite existing work; never print secrets.
- Structural validation does not prove the agent works; verify behaviour against the success criteria after launch.
