# Research execution defaults

Read `/home/user/azirar/.agents/AGENT_SYSTEM_STANDARD.md` for the concise
system structure and model-selection map.

Human Orchestrator, Operations Lead, and each suborchestrator also read
`/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md` and
`/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md`. Workers do not load
those long manuals: the concise standard and their validated task card are the
complete operating context for one minimal work package.

# Delegation

- Delegate only work that materially benefits from a separate context.
- Native Codex subagents are disabled. Create named Herdr sessions for approved
  independent tasks.
- One worker owns one minimal work package and one worktree. Close it after the
  package report; a later package or correction gets a fresh chat.
- Create one Sol-medium suborchestrator for one meaningful multi-package task.
  It owns the task goal and finish condition, does no coding, issues only the
  next useful package, launches fresh workers, and may not spawn another
  suborchestrator. Send an already-atomic package directly to one worker.
- More sessions are welcome when they perform independent productive work.
  Never create sessions merely for status, waiting, routine review, or advice.
- Keep `HUMAN_PLAN.md` at milestone/workstream level. Exact worker tasks and
  names belong in Herdr when execution begins, not in the human document.
- Route every compact completion envelope only to the Operations Lead. It
  reloads technical evidence and sends only accepted material meaning, genuine
  decisions, or human questions to the Human Orchestrator. The Human
  Orchestrator owns human conversation and plan meaning; it does not receive
  worker transcripts, manage execution, edit files, use Git, or control Herdr.
- Human Orchestrator speaks in ordinary project language: answer first, then
  what it means, what happens next, and one real choice if needed. It must not
  expose internal process terms such as evidence, accepted meaning, observable,
  routing, envelope, pane, session, worker, lifecycle, verified, authority,
  blocker, or `READY FOR HUMAN`, or use all-caps process headings, unless the
  user explicitly asks about the system.
- Standing roles are one native-Codex Sol-high Human Orchestrator and one
  native-Codex Sol-high Operations Lead with sole operational authority.
- Cross-pane requests use the installed `herdr-role-message` helper, not native
  model-agent discovery. Human Orchestrator uses
  `herdr-role-message operations`; Operations Lead uses
  `herdr-role-message human`; technical
  roles return with `herdr-role-message operations`. Human Orchestrator may
  also run `herdr-project-save-close --close` only after the Human explicitly
  asks to close and Operations has completed the final save. It may use no
  other Herdr control command.
- “Do,” “go,” and “continue” authorize the already-discussed next action.
  Forward and start it rather than replying with readiness or asking the user
  to repeat the instruction.
- A Plan Orchestrator is temporary, belongs with the orchestrators rather than
  workers, edits only `HUMAN_PLAN.md` from accepted meaning and checked
  evidence, reports only to the Operations Lead, and closes after one commit.

# Goals and progress

- Until further notice, optimize for fast goal movement: implement the smallest
  coherent requested change, commit and sync it, then hand the turn back. Do not
  schedule test suites, browser testing, broad reviews, or cleanup passes.
- Reuse the strongest existing project or official-upstream implementation
  before writing a new path. Delete clearly bad, dead, duplicated, misleading,
  or superseded code instead of wrapping or preserving it without a named live
  consumer.
- For a concrete failure, use `goal-directed-repair`. Find the causal source
  and make the smallest root-level fix; do not accept a bandage, widen into an
  audit, create a test suite, or give up after one failed coherent attempt.
- Create no side artifacts by default: no reports, manifests, dashboards,
  project hubs, review files, duplicate READMEs, or status documents. Keep the
  requested source/configuration, required run files, actual outputs, and the
  existing `HUMAN_PLAN.md`, `RESTART_HANDOFF.md`, and `OLD_HISTORY.md`. Keep
  the compact restart handoff current after material results, task changes,
  external waits, and decisions.
- Before work: state the current and expected result, act, compare observed to
  expected, and return the saved result. Do not open another planning turn.
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

- A worker wakes its parent directly with `herdr-role-message` when it finishes
  or needs recovery. Operations and suborchestrators never run `herdr wait`,
  `sleep`, or polling loops for child roles. They arm `herdr-emergency-wake`
  before yielding; it wakes the parent once if the child remains open past the
  task-specific silence interval. Closing the child disarms the fallback.
- Use one external event-driven service only for genuinely long processes,
  schedulers, or remote work. It wakes a native-Codex Luna-low watcher only on
  a changed event or maximum-silence event.
- The watcher has no project-write authority and does not perform the waiting
  loop. It receives only bounded event data. Trusted service code may wake one
  named visible
  Sol-medium verifier when an event is genuinely unusual.
- Do not issue repeated model turns to poll unchanged state. Every watch names
  success, failure, maximum silence, owner, and the recovery action fired when
  silence expires. A watcher closes on its terminal event.
- Default coding workers to native Codex Luna max. Luna support or supervision may use low
  but never higher. Use Sol medium for harder coding. Select Sol low through
  max for bounded research or data crunching according to actual difficulty;
  use Terra medium for open-ended research.
- Roll over leadership before automatic context compaction. Preserve the live
  state in `HUMAN_PLAN.md`, archive the native session ID, and continue fresh.
- Replace leadership immediately when compaction already occurred, its
  internal goal is blocked, or a messenger round trip fails. Never use Herdr
  `report-agent`, `report-metadata`, or `release-agent` to rewrite standing-role
  activity state.
- Do not wake standing leadership for unchanged status. Close every transient
  worker, checker, watcher, advisor, Plan Orchestrator, researcher, PaperPilot
  Maintainer, or suborchestrator pane immediately after its final result and
  native session reference are captured, before integration. Resume the same
  task in a new pane only for a concrete correction.

# Completion

- Reproduce first, implement or run, verify, then compare the expected and
  observed state.
- Normal coding workers use native Codex Luna max for one clear, repeatable package with one
  deliverable and reproducible done check, normally within three tightly
  coupled files or one experiment stage. Escalate the same task to Sol medium
  after one failed coherent repair, material ambiguity, scope expansion, or a
  non-reproducible result. Opus 5 and OpenCode GLM 5.2 remain explicitly
  selectable alternatives. Terra-high remains human-selected only.
- Bounded research and data crunching use Sol at the lowest sufficient effort;
  open-ended research uses one Terra-medium Researcher. A Verifier is optional, Sol medium, minimal, and opened
  only for one consequential anomaly that routine self-verification cannot
  settle. Suborchestrators use Sol medium for one meaningful task and never
  code; advisors use Sol xhigh for one sparse bounded
  decision.
- Commit every coherent completed chunk, integrate it in dependency order, and
  push the canonical branch immediately so accepted code matches GitHub.
- Completion requires observed output that meets the task card. Ready, idle,
  waiting, submitted, or an agent's completion claim is not completion. Every
  active task always has a current package and next action; external waiting
  states name independent work that continues.
- `herdr-costs report` shows the human-named hierarchy with own and aggregate
  time, tokens, and API-equivalent dollars. Do not create a manual dashboard.
- For an explicit project save-and-close, Operations Lead closes every
  temporary role, records continuing external work, synchronizes Git, updates
  `OLD_HISTORY.md`, and commits `RESTART_HANDOFF.md` last. It then tells Human
  Orchestrator the workspace is ready for its guarded self-close.
- End every worker with the project question, expected state, observed state,
  explanation of any difference, evidence, commit/output, remaining work, and
  an explicit stopped state.
- Close finished sessions and retire their worktrees after merge or rejection.

# PaperPilot

- Use PaperPilot only when explicitly requested, required by a real
  manuscript/publication, or already accepted as the project's live surface.
  A no-side-artifact instruction disables PaperPilot setup and local hub files.
- When enabled, read and follow
  `/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md`, discover and
  reuse before creating, and never create a duplicate.
- Record the confirmed link in project-root `PAPERPILOT.md`. Use one named
  `PaperPilot Maintainer · PersonName Project Hub` for the complete human plan,
  scientific status, optional manuscript, and native PaperPilot comments.
- The Operations Lead involves the maintainer after an accepted plan change,
  material result, user comment, or paper task and routes only human meaning
  through the Human Orchestrator. PaperPilot publication still requires the
  skill's exact displayed-diff approval.
