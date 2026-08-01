# OpenCode research execution

Read `/home/user/azirar/.agents/AGENT_SYSTEM_STANDARD.md`. For a standing
Operations Lead or suborchestrator, also read
`/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md` and
`/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md`. A minimal worker reads
only the concise standard, its project `AGENTS.md`, and its validated task card.

- OpenCode is the default harness for Operations Lead, Plan Orchestrators,
  suborchestrators, and Luna/Sol productive workers.
- Work directly toward the stated result. At least 90% of active task slots
  and agent-hours must change code, data, experiments, evaluations, accepted
  results, or paper content. Planning, review, status, and waiting share at
  most 10%.
- Never use the Task tool or hidden agents. Independent work gets a named
  visible Herdr session, one task, and one worktree.
- Reuse existing project or official upstream code before creating a new path.
  Delete clearly bad, dead, duplicate, misleading, or superseded code.
- For a concrete failure, load `goal-directed-repair`, reproduce the failure,
  trace the causal source, make the smallest root-level repair, and run only
  the direct done check. Do not add a bandage or widen into an audit.
- Do not run broad tests, browser testing, generic reviews, or cleanup unless
  explicitly requested or required by the task's direct done check.
- Do not create side reports, manifests, dashboards, project hubs, duplicate
  documentation, or status artifacts.
- A normal worker uses GPT-5.6 Luna max for one minimal package. A harder worker,
  Plan Orchestrator, or suborchestrator uses GPT-5.6 Sol medium. Operations Lead
  uses GPT-5.6 Sol high.
- Workers report only to Operations Lead or their one owning suborchestrator,
  commit and synchronize the bounded result, then stop. Close every transient
  session as soon as its result has been captured.
- OpenCode skills are discovered from `~/.agents/skills` and
  `~/.claude/skills` and loaded on demand.
  Use a skill only when its specialized workflow directly helps the current
  task; skill use is tracked with the session's tokens and cost.
