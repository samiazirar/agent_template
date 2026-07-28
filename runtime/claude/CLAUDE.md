@/home/user/azirar/.agents/AGENT_SYSTEM_STANDARD.md
@/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md
@/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md

# Claude and Claudex enforcement

- Until further notice, optimize for direct goal movement. Implement the
  smallest coherent requested change, commit and sync it, and hand the turn
  back. Do not schedule test suites, browser testing, broad reviews, or cleanup
  passes.
- At least 90% of active task slots and agent-hours must directly change code,
  data, experiments, evaluations, accepted evidence, or paper content.
  Orchestration, collaborative planning, plan writing, advice, checking,
  status, review, audit, and waiting share at most 10%. Every control action
  must name the productive action it directly unlocks.
- Sol medium is the normal Codex/Claudex worker. Native Claude Opus 5 and
  OpenCode GLM 5.2 are selectable productive alternatives. Terra and Luna are
  reserved for research, interpretation, and observation.
- Long-running observation uses an external service with read-only API-key
  `opencode/gemini-3.6-flash`, or Luna for research observation. Never use
  Vertex. The watcher cannot inspect or modify code and trusted service code
  opens a named visible Sol-medium verifier only for a genuinely unusual event.
- Claudex may use relevant Claude-side workflows, skills, commands, hooks, and
  short-lived native helpers inside its one assigned task and worktree when
  they directly reduce that task's done check. The owning visible pane remains
  accountable and validates every resulting artifact.
- Do not turn a native helper into hidden independent work. Anything with its
  own outcome, task card, workspace, durable result, or reporting route must be
  a named visible Herdr session.
- Do not invoke a generic PR-review or recursive audit workflow for routine
  local implementation. Use a targeted workflow when it directly serves the
  assigned task or the defined release/result boundary.
- Fable is a short-lived milestone strategist, not an operational dependency.
- Claudex sessions must be launched and resumed through `claudex`, never
  directly through `claude`.
- Do not trust inherited plans as evidence. Every task must trace the frozen
  project question through current state, expected state, causal action, and
  observed evidence.
- Validate worker cards with
  `/home/user/azirar/.codex/skills/restart-research-team/scripts/validate_task_card.py`
  before launching them.
- The Claudex Sol-high Human Orchestrator owns only human conversation, goal
  meaning, human decisions, and intended plan meaning. It does not edit files,
  manage execution, or contact technical roles other than the Codex Sol-high
  Operations Lead.
- The Codex Sol-high Operations Lead is the sole operational authority. Every
  worker, suborchestrator, Plan Orchestrator, advisor, researcher, and verifier
  reports through it. Send compact result envelopes only to the Operations
  Lead; it routes accepted human meaning to the Human Orchestrator.
- The standing native Claude Opus-5-medium Operations Collaborator remains in
  the background. It answers one bounded collaborative-planning,
  decomposition-alternative, or milestone-interpretation question only from
  the Operations Lead, then returns idle. It never manages or contacts workers,
  integrates Git, controls Herdr, contacts the human side, or becomes an
  approval step.
- A temporary Sol-medium Plan Orchestrator edits only `HUMAN_PLAN.md`, reports
  only to the Operations Lead, and closes after one plan-only commit. Terra
  medium is the default Researcher; Luna is its read-only observer. Sol-medium
  Verifiers are optional and minimal. Sol-high suborchestrators exist only for
  independent workstreams with at least three productive tasks; Sol-xhigh
  advisors answer one sparse bounded decision.
- Every research project must have exactly one corresponding PaperPilot
  project. Use `$paperpilot`, reuse an existing project before creating a
  missing one, record the confirmed link in `PAPERPILOT.md`, and assign one
  named PaperPilot Maintainer to the human plan, scientific status, optional
  manuscript, and native comments.
- Follow `/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md`, including
  the maintainer's dedicated worktree/repository and the account-scoped proof
  that the project is visible from the user's confirmed PaperPilot account.
