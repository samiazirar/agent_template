@/home/user/azirar/.agents/AGENT_SYSTEM_STANDARD.md

# Native Claude boundary

- Native Claude Code is not a standing project or orchestration surface.
- Resume an old Claude session only to run `/export`, save its conversation in
  the project's old history, and close it.
- A new Opus 5 session may do productive work only when the Human explicitly
  selects Opus for one bounded package. It receives one deliverable, one direct
  done check, one worktree, and no hidden agents.
- Spend at least 90% of the package on the requested code, data, experiment,
  evaluation, or paper result. Do not add plans, audits, broad tests, browser
  tests, review stages, cleanup, or side documents.
- Reuse the strongest existing implementation. Delete clearly bad, dead,
  duplicate, misleading, or superseded code. For a concrete failure, use
  `goal-directed-repair` and fix the causal source rather than a symptom.
- Report only to the assigning Operations Lead or suborchestrator with
  `herdr-role-message`, which wakes that parent, then stop without waiting for
  acknowledgement. Never contact the Human or Human Orchestrator.
- Commit and synchronize the coherent bounded result. Use
  `herdr-costs report` for usage; do not create a usage artifact.
