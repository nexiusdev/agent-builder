# Every agent needs a to-do mechanism
The user requires every agent to have a to-do list, either self-maintained or using an available builtin kanban. This applies to individual agents and orchestration participants, including the builder itself.

Default scaffolds use tasks/todo.json as the operational source of truth, configured in docs/task-tracking.json. devplan/todo.md tracks build milestones separately; avoid duplicating the same operational tasks there. An existing builtin platform board may instead be selected explicitly, naming board/project, owner, adapter and verified access. Never assume a specific platform or claim connectivity from a setting. There is no builtin adapter shipped here. Existing settings and task records survive upgrade.

Each item needs stable task ID, title, responsible owner and status. Add blocker, next action, due date, dependencies, workflow/run and deliverable references where useful. Status vocabulary: todo, in_progress, blocked, waiting, done, cancelled. Use done only with outcome evidence; handoff must identify the receiving owner and acceptance, not simply remove work from a list. Review the list at session start and after meaningful outcomes. Do not create external schedules merely because a task has a due date.

Local updates: python scripts/tasks.py TARGET --task-id T1 --title "Review sources" --owner knowledge-agent --status in_progress --expected-revision 0

The helper preserves other fields, locks writers and checks expected revision before atomic replacement. Conflict means reread and reconcile; don't change the revision argument blindly. A crashed process may leave a lock: inspect before manual recovery, never remove a live lock. This local-file coordination is not a distributed board or an access-control system. For a shared platform use its native transactions/revisions and least-privilege permissions. No agent may take over another owner's task silently.
