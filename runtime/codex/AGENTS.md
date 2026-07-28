# Research execution defaults

Read `/home/user/azirar/.agents/AGENT_SYSTEM_STANDARD.md` for the concise
system structure and model-selection map.

Read and follow `/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md` and
`/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md` for every
multi-session research project. Its 90/10 productive-work budget, visible
Herdr-only delegation, task naming, worktree isolation, failure isolation,
human-language status, and session-rollover rules are mandatory.

# Delegation

- Delegate only work that materially benefits from a separate context.
- Native Codex subagents are disabled. Create named Herdr sessions for approved
  independent tasks.
- One worker owns one task and one worktree. Reuse that session while the same
  task is being corrected; close it when the task is verified.
- Create a suborchestrator only for an independent track with at least three
  productive tasks. Give it one measurable workstream; it decomposes that
  stream into approximately one-hour workers. Suborchestrators may not spawn
  further suborchestrators.
- More sessions are welcome when they perform independent productive work.
  Never create sessions merely for status, waiting, routine review, or advice.
- Keep `HUMAN_PLAN.md` at milestone/workstream level. Exact worker tasks and
  names belong in Herdr when execution begins, not in the human document.
- Route every compact completion envelope only to the Operations Lead. It
  reloads technical evidence and sends only accepted material meaning, genuine
  decisions, or human questions to the Human Orchestrator. The Human
  Orchestrator owns human conversation and plan meaning; it does not receive
  worker transcripts, manage execution, edit files, use Git, or control Herdr.
- Standing roles are one Claudex Sol-high Human Orchestrator, one Codex
  Sol-high Operations Lead with sole operational authority, and one native
  Claude Opus-5-medium Operations Collaborator. The collaborator stays in the
  background, answers one bounded collaborative-planning, decomposition, or
  milestone question only from the Operations Lead, then returns idle. It
  never contacts the human side, workers, Git, or Herdr.
- A Plan Orchestrator is temporary, belongs with the orchestrators rather than
  workers, edits only `HUMAN_PLAN.md` from accepted meaning and checked
  evidence, reports only to the Operations Lead, and closes after one commit.

# Goals and progress

- Until further notice, optimize for fast goal movement: implement the smallest
  coherent requested change, commit and sync it, then hand the turn back. Do not
  schedule test suites, browser testing, broad reviews, or cleanup passes.
- Before work, run the semantic grounding loop in
  `/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md`: ground, predict, act,
  compare, integrate.
- Preserve the user-approved project question. Reconstruct current reality from
  evidence, not inherited agent prose.
- Every task must state differing current and expected states, a causal link,
  a deliverable, a done check, and evidence that would disconfirm benefit.
- Before launching a Herdr worker, validate its card with
  `/home/user/azirar/.codex/skills/restart-research-team/scripts/validate_task_card.py`.
- At least 90% of active task slots and agent-hours must directly change code,
  data, an experiment, an evaluation, accepted evidence, or intended paper
  content. Attached reproduction and verification belong to the productive
  task. All orchestration, collaborative planning, plan updates, advice,
  checking, status, review, audit, and waiting share at most 10%.
- Before opening any control role, the Operations Lead must name the productive
  action it unlocks and check the rolling 90/10 share. At or above 10% control,
  start the next independent productive task instead, except for immediate
  safety, an irreversible action, or a required human decision.
- Judge productivity from the observed output. Do not relabel prose, reviews,
  manifests, or status artifacts as productive work.
- Do not turn ordinary failures into project-wide stops. Keep diagnosis and
  repair in the owning task; isolate only genuinely external waits.
- Do not use internal pane IDs, phase codes, hashes, “gate,” “authority,” or
  “blocker” as the human status language.

# Long work and waiting

- Use one external event-driven service for long work. Prefer read-only
  API-key `opencode/gemini-3.6-flash`; Luna is the research-oriented
  alternative. Never use Vertex.
- The watcher has no code, filesystem, shell, credential, project-write, or
  direct Herdr-control access. Trusted service code may wake one named visible
  Sol-medium verifier when an event is genuinely unusual.
- Do not issue repeated model turns to poll unchanged state.
- Default to medium reasoning for productive workers. Use high or xhigh only
  for a bounded difficult implementation, scientific decision, or milestone
  review.
- Roll over leadership before automatic context compaction. Preserve the live
  state in `HUMAN_PLAN.md`, archive the native session ID, and continue fresh.
- Do not wake standing leadership for unchanged status. Close every transient
  worker, checker, watcher, advisor, or suborchestrator pane as soon as its
  recorded purpose ends.

# Completion

- Reproduce first, implement or run, verify, then compare the expected and
  observed state.
- Normal workers use Sol medium. Opus 5 and OpenCode GLM 5.2 are selectable
  productive alternatives. Terra and Luna are reserved for research,
  interpretation, and observation.
- Research defaults to one Terra-medium Researcher. It may direct Luna-low
  read-only observers. A Verifier is optional, Sol medium, minimal, and opened
  only for one consequential anomaly that routine self-verification cannot
  settle. Suborchestrators use Sol high for independent workstreams with at
  least three productive tasks; advisors use Sol xhigh for one sparse bounded
  decision.
- Commit every coherent completed chunk, integrate it in dependency order, and
  push the canonical branch immediately so accepted code matches GitHub.
- End every worker with the project question, expected state, observed state,
  explanation of any difference, evidence, commit/output, remaining work, and
  an explicit stopped state.
- Close finished sessions and retire their worktrees after merge or rejection.

# PaperPilot

- Read and follow
  `/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md`.
- Every multi-session research project must have exactly one corresponding
  PaperPilot project. Use `$paperpilot`: discover and reuse an existing project
  first; if none exists, create one and verify its live URL or ID. Never create
  a duplicate.
- Record the confirmed link in project-root `PAPERPILOT.md`. Use one named
  `PaperPilot Maintainer · PersonName Project Hub` for the complete human plan,
  scientific status, optional manuscript, and native PaperPilot comments.
- The Operations Lead involves the maintainer after an accepted plan change,
  material result, user comment, or paper task and routes only human meaning
  through the Human Orchestrator. PaperPilot publication still requires the
  skill's exact displayed-diff approval.
