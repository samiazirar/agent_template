# Agent system standard

This is the short map for selecting sessions, models, delegation, delivery,
observation, and human communication. The research onboarding and
orchestration contracts provide the detailed rules.

## Goal and delivery

- Begin from one explicit user-approved goal and the next observable state.
- Spend at least 90% of task slots and agent-hours changing code, data,
  experiments, evaluations, accepted results, or intended paper content.
- Planning, status, advice, broad checking, and waiting share the remaining
  10%. Never rename them as productive work.
- Until the user says otherwise: make the smallest coherent goal-moving
  change, do not schedule test suites or browser testing, commit it with a
  human-readable message, push the canonical branch, and hand control back.
- Treat the requested action boundary literally. A read, report, diagnose, or
  evidence task does not authorize edits, repository-wide scans, unrelated
  retries, tests, cleanup, launches, or implementation.
- One task owns one branch, worktree, and named Herdr session. Accepted chunks
  are merged in dependency order; after integration, the canonical checkout
  and GitHub represent the same code.
- Reuse before writing. Search the existing project, official upstream
  repository, installed tools, and known working neighboring implementations
  for the needed path. Extend or repair the best existing implementation
  unless a concrete incompatibility makes replacement smaller and safer.
- Delete decisively when code is clearly broken, dead, duplicated, misleading,
  or superseded. Preserve compatibility only for a named current consumer; do
  not accumulate wrappers, parallel implementations, commented-out code, or
  speculative fallbacks around bad code.
- For a concrete failure, use `goal-directed-repair`: reproduce once or read the
  existing failure, identify the causal source, make the smallest source-level
  repair, run only the direct done check, commit, and stop. Never accept a
  symptom-only bandage, but do not turn root-cause work into a broad audit,
  mandatory test suite, instrumentation project, or architecture redesign.
- One failed coherent repair is information, not completion or surrender. Try
  one new bounded causal repair. If the task then requires a materially
  different design or subsystem, give that harder package to a fresh
  Sol-medium worker while independent work continues.
- Default to no side artifacts. Do not create plans, reports, manifests,
  review files, dashboards, project hubs, duplicate READMEs, status documents,
  or prose records merely to describe work. Allowed outputs are the requested
  source/configuration, files required to run it, actual experiment outputs,
  and the existing `HUMAN_PLAN.md`, `RESTART_HANDOFF.md`, and `OLD_HISTORY.md`
  required by the fixed Herdr layout. Keep the handoff compact and current so
  closing the workspace never depends on another model turn.

### Enforce 90/10 at admission

- Productive work directly changes code, data, an experiment, an evaluation,
  accepted research evidence, or intended paper content. Attached reproduction
  and verification belong to that productive task.
- Every orchestrator turn, collaborative-planning turn, plan update, advisor,
  verifier, review, status message, audit, and wait is control work. A role name
  never changes that classification.
- Operations Lead tracks the rolling share by active task slots and agent-hours
  before opening control work. At or above 10%, open the next independent
  productive task instead. Exceed 10% only for an immediate safety issue,
  irreversible action, or a human decision that truly prevents productive work.
- Every admitted control action must name the productive action it directly
  unlocks. Do not open planning, advice, checking, or plan-writing sessions for
  general reassurance.
- Idle standing orchestrators consume no model turns. Do not wake the Human
  Orchestrator or Operations Lead for routine status or unchanged state.

## GPT-5.6 prompting

- Lead with the outcome. Give only the context that can change it, the hard
  constraints, the observable done condition, and the required handoff.
- State enduring rules once in `AGENTS.md` or this standard. A task prompt adds
  only its immediate goal and evidence; it does not repeat inherited contracts.
- Ask only when a material ambiguity or approval boundary prevents safe
  in-scope work. Otherwise proceed directly toward the requested outcome.
- Keep responses natural and compact: conclusion, necessary evidence, material
  caveat, and next action. Omit internal process language and generic filler.
- Do not copy generic advice such as always testing, always planning, or always
  using high reasoning. The user's no-test default and the model-selection
  rules below take precedence.

## Session and model selection

| Work | Session | Model |
| --- | --- | --- |
| Human orchestration | Native Codex | Sol, high |
| Operations Lead | Native Codex | Sol, high |
| Normal bounded implementation or execution | Native Codex | Luna, max |
| Ambiguous repair or cross-task integration | Native Codex | Sol, medium |
| Bounded difficult implementation or decision | Native Codex | Sol, high |
| One bounded strategic question | Native Codex | Sol, xhigh |
| Temporary Plan Orchestrator | Native Codex | Sol, medium |
| Explicitly requested alternative worker | Native Claude | Opus 5 |
| Mechanical or context-heavy alternative worker | OpenCode | GLM 5.2 |
| Open-ended researcher | Native Codex | Terra, medium |
| Human-selected bounded productive worker | Codex | Terra, high |
| Routine research or data crunching | Codex | Sol, low; raise only when the task needs it |
| Cheap bounded support or supervision | Codex | Luna, low maximum |
| Event-triggered watcher classification | Native Codex | Luna, low maximum |
| Optional minimal verification | Native Codex | Sol, medium |
| Human message drafting, if needed | Native Codex | Luna, low maximum |

Claudex is the Claude Code interface backed by the local Codex gateway. It is
not native Anthropic Claude. Launch it through `claudex` with an explicit Codex
model. Native Claude is selected separately when Opus 5 is wanted.

Native Codex Luna-max is the default coding worker when the task has one concrete
deliverable, one reproducible done check, and a narrow action boundary. Use Sol
medium for a harder package that needs materially more judgment. Select Sol
low through max for bounded research or data crunching according to actual
difficulty; do not inherit a high effort merely because the parent task is
important. Luna support, watcher classification, or supervision never exceeds
low and runs only when an external event wakes it. Terra remains the
default for open-ended research and interpretation. Terra-high may be a
productive worker only when the human explicitly selects it for one bounded
task. OpenCode remains available for an explicitly selected non-OpenAI provider
such as GLM 5.2, not as the default harness for OpenAI Sol or Luna. Never use
Vertex; Gemini routes use the OpenCode API-key provider.

## Native Herdr launch

- Launch every independent agent as a named visible Herdr session with
  `herdr-agent <surface> "Role · PersonName Goal" [directory]`.
- `luna-max` is the normal bounded coding worker. `codex` is the Sol-medium
  suborchestrator, Plan Orchestrator, and harder-worker route. `codex-high` is
  used for both standing orchestrators.
- `opencode` is an explicitly selected alternate-provider route, primarily for
  GLM 5.2. Do not route OpenAI Sol or Luna through it by default.
- `terra` is the normal researcher and `luna-low` is restricted to
  event-triggered observation or cheap support. `claude` is legacy-export-only
  unless the Human explicitly requests Opus 5 for one productive task.
- Never replace these sessions with hidden subagents or ordinary background
  subprocesses. Open a separate session only for independent productive work.
- Shared personal skills live once in `~/.agents/skills`. OpenCode discovers
  that directory natively and loads only a selected skill body on demand.
  Claude and Claudex load the same directories through `~/.claude/skills`; do
  not maintain divergent copies.
- Use `prompt-gpt-5p6-sol` when adapting instructions for Codex or Claudex and
  `prompt-claude-opus-5` when adapting instructions for native Opus 5.

## Human structure

- The standing architect owns the user conversation, system design, role
  selection, and every improvement derived from agent reports. It remains open
  until the user ends or replaces it.
- For requested topology changes, the architect opens one short-lived named
  launcher. The launcher creates and briefs the sessions, reports readiness to
  the architect, and stops; it never replaces or closes the architect.
- The Human Orchestrator is the project's only normal human conversation. It
  confirms the goal and its meaning, asks and answers human questions, and
  explains material results. It sends every technical request to Operations
  and returns Operations questions that require human judgment to the user. It
  does not contact technical roles directly or manage execution, workers, Git,
  or internal tools.
- The Human Orchestrator speaks like a thoughtful human collaborator, not like
  a process console. Start with the answer or outcome. Say what happened, what
  it means for the goal, what happens next, and the one choice needed, if any.
  Do not expose internal labels or vocabulary such as “evidence,” “accepted
  meaning,” “observable,” “durable,” “routing,” “completion envelope,”
  “lifecycle,” “pane,” “session,” “worker,” “verified,” “authority,”
  “blocker,” `READY FOR HUMAN`, or similar status mechanics unless the user
  explicitly asks how the system works. Use “results,” “what we know,” “the
  next useful result,” and ordinary project language instead. Do not use
  all-caps process headings or make the user read an internal checklist.
- The native-Codex Sol-high Operations Lead owns decomposition, execution, worker and
  suborchestrator lifecycle, integration, synchronization, the 90/10 budget,
  and technical state. It is the sole operational authority and normal bridge
  between the Human Orchestrator and every technical role.
- Normal communication follows one path:
  `Human ↔ Human Orchestrator ↔ Operations Lead ↔ technical role`.
  Workers, suborchestrators, Plan Orchestrators, advisors, researchers, and
  verifiers do not bypass Operations Lead.
- That path must work mechanically, not only in prose. Roles send cross-pane
  messages with `herdr-role-message`: Human Orchestrator uses
  `herdr-role-message operations`, Operations Lead uses
  `herdr-role-message human`, and
  technical roles use `herdr-role-message operations`. The helper resolves the
  named role inside the current workspace and keeps internal identifiers
  hidden. Human Orchestrator may use this messenger and the guarded
  `herdr-project-save-close --close` command after an explicit Human close
  request and a completed Operations save. It may use no other Herdr control.
- A prompt is sent with `herdr pane run`, never `send-text`. Send only after
  the target is `idle` or `done`, then confirm it becomes `working` or
  completes the new turn. Text shown as “Messages to be submitted after next
  tool call” is queued, not yet accepted; do not claim it was processed and do
  not send a duplicate.
- A parent orchestrator never runs `herdr wait`, `sleep`, or a polling loop for
  a child role. Before yielding after dispatch, it arms
  `herdr-emergency-wake` with the child pane and a task-specific maximum-silence
  interval. The child wakes its parent directly with `herdr-role-message` on
  completion or material trouble. The parent captures the result and closes
  the child, which disarms the emergency wake. If no child message arrives,
  the helper wakes the parent once with the recovery action. No model turn
  remains occupied by waiting.
- “Do,” “go,” “continue,” and equivalent short confirmations authorize the
  already-discussed next action. Human Orchestrator forwards the instruction
  once and Operations Lead starts it; neither asks the user to restate it or
  merely responds with readiness.
- Never fake standing-role state with `herdr pane report-agent`,
  `report-metadata`, or `release-agent`. Native agent integration owns activity
  state. `done` on a standing pane means its latest turn is complete, not that
  the standing role should close.
- `00 Human Plan` is a non-agent Frogmouth view of `HUMAN_PLAN.md`. Keep the
  Human Orchestrator in `01 Orchestrators`, never in the plan pane.
- The Human Orchestrator owns plan meaning but does not edit it directly.
  It tells Operations Lead what the user wants. Operations Lead launches one
  temporary `Plan Orchestrator` only after a material change. This is an
  orchestrator role, not a worker. It receives the intended change and the
  relevant checked results from Operations Lead, edits only `HUMAN_PLAN.md`, and returns one
  plan-only commit to Operations Lead. Operations Lead asks the Human
  Orchestrator to check meaning, integrates, synchronizes, and closes it.
- `HUMAN_PLAN.md` is the single continuously maintained human-facing source of
  truth. The user should need only this Markdown file and conversation with the
  human orchestrator. In no-side-artifact mode, do not create additional
  internal prose surfaces.
- Keep it at human level: the goal, why it matters, current reality, meaningful
  change, active milestones, next useful result, and any decision genuinely
  needed from the user. Explain necessary technical terms in ordinary language.
- Update it in place after each material result, accepted decision, or real
  change in direction. Do not update it for unchanged status, polling, routine
  commits, or agent activity.
- Keep `RESTART_HANDOFF.md` equally current after each material technical
  result, changed active task, new external wait, or accepted decision. It is a
  compact restart record: goal, current code/result, what is running, exact
  next action, and repository state. It is not a second plan or a transcript.
- Omit workers, sessions, branches, paths, hashes, job identifiers, task cards,
  PaperPilot mechanics, and operational transcripts unless one is essential to
  a user decision. Those remain behind the human orchestrator.
- Apply the same human voice to `HUMAN_PLAN.md`: use “what we know,” “results,”
  “measurements,” and “next useful result.” Do not use “evidence,”
  “observable,” “accepted meaning,” “durable,” “routing,” “verified,”
  “lifecycle,” “completion envelope,” or all-caps process labels.
- Human-facing names and messages use project and task words. Pane IDs,
  session IDs, hashes, phase codes, deduplication keys, and terms such as
  “gate” stay internal.
- Replace a standing leadership session instead of rebriefing it when its
  context has compacted, its internal goal is blocked, or a real role-to-role
  route check fails. Record the old native session reference in history, close
  the old pane, and launch a fresh role in the same place.
- When the Human explicitly asks to save and close, the Human Orchestrator uses
  `save-close-herdr-project`. Operations Lead closes temporary roles, records
  continuing external work, synchronizes the canonical repository, updates
  history, and commits project-root `RESTART_HANDOFF.md` as the final save.
  After Operations confirms readiness, the Human Orchestrator runs the guarded
  helper, which may close only its own current workspace. Never stop the shared
  Herdr server or named session, and never treat inactivity as permission.
- One worker owns exactly one minimal concrete work package, branch, worktree,
  and fresh native chat. Native Codex Luna-max
  is the default when the task can be stated as one deliverable, one
  reproduction or run, one done check, and normally no more than three tightly
  coupled files or one experiment stage.
  Independent packages use concurrent workers. When a worker finishes,
  Operations Lead captures its short result and native session reference,
  closes the pane immediately, and then integrates or rejects the saved work.
  A later package or correction starts in a new worker chat; do not carry a
  finished worker into the next package. Workers receive
  tasks from and report only to Operations Lead or their one owning
  suborchestrator.
- Suborchestrators use native Codex Sol medium, own exactly one meaningful task, and do no
  coding or experiment execution. Each states the task goal and finish
  condition, turns only the next useful work into minimal packages, launches
  one fresh native-Codex Luna-max worker per normal coding package or native
  Codex Sol-medium worker for
  a harder package, absorbs compact results, and closes when the task ends. An
  atomic task that is already one minimal package goes directly from Operations
  to one worker to avoid orchestration overhead. A suborchestrator may not
  create another suborchestrator or add a review turn after every successful
  package.
- Strategic advisors are sparse temporary Sol-xhigh sessions. Give one advisor
  only the context for one bounded question, preferably yes/no or one concrete
  recommendation. Operations Lead launches it and receives its answer; it never
  contacts the user, implements, or manages and closes after answering.
- For consequential strategic planning or plan validation, the responsible
  orchestrator uses `consult-chatgpt-pro` with one compact question, then
  reconciles the advice against project evidence.
- Bounded research and data crunching use Sol at the lowest effort that can do
  the work, from low through max. Use a Terra-medium Researcher by default when
  the question is open-ended or requires synthesis and interpretation.
  Research reports to Operations Lead for project work or the Architect for
  agent-system research. Research counts as productive only when it creates
  accepted goal-relevant evidence.
- Explicitly selected Terra-high productive work uses one bounded named Worker,
  one worktree, and the normal worker completion and closure rules.

## Progress, continuity, and cost

- Every active task always has one current minimal package, an owner, a finish
  condition based on observed output, and a next action. “Ready,” “waiting,”
  “looks complete,” an idle pane, submitted work, or an agent claim never
  counts as completion.
- A suborchestrator closes a successful worker immediately and launches the
  next package without a planning round. If a package fails, it issues one
  bounded repair package in a fresh worker chat. If that cannot settle the
  same issue, it reports the exact technical choice to Operations; unrelated
  packages continue.
- Waiting is permitted only for a named external event with a responsible
  owner, a deadline or expected change window, and independent work that
  continues meanwhile. If none exists, the task is stalled and Operations must
  choose a concrete recovery action, not describe the stall.
- `herdr-agent` records each launched native session in the private local usage
  ledger. Run `herdr-costs report` inside the workspace for a human-named tree
  of worker own time/tokens/cost, suborchestrator totals, Operations totals, and
  the Human total. Dollar values are API-equivalent estimates; subscription
  sessions are not token-billed and provider billing remains authoritative.
- OpenCode accounting reads its native session database, including per-message
  model, variant, token, cost, active-time, and skill-tool records. Native
  Claude Code and Claudex also register new and resumed Herdr sessions
  through their `SessionStart` hook. Their duplicate streaming transcript rows
  are counted once by native message ID.
- The same report lists explicit skill invocation count, associated tokens,
  and API-equivalent cost. Claude and Claudex use their native active-skill
  attribution. OpenCode attributes a skill to the model messages in the user
  turn that invoked it. Codex records the exact token delta from loading a skill through
  the end of that turn; when one turn loads multiple skills, those values
  overlap and are not additive. Use this observed usage to keep, narrow, or
  remove skills instead of judging them only by description size.
- The ledger and generated terminal table are the only cost records. Do not
  create task reports, dashboards, or manual token spreadsheets.

## Harness policy

- Use native Codex for both standing orchestrators, Plan Orchestrators,
  suborchestrators, OpenAI Luna/Sol workers, researchers, event-triggered
  watchers, strategic advisors, and optional verifiers. It provides the
  steering, queuing, and turn-completion notification needed by this topology.
- Use OpenCode only for an explicitly selected alternate provider such as GLM
  5.2. Use Claudex only for bounded GPT work that materially benefits from its
  interface. Native Claude Code is legacy-export-only unless the Human
  explicitly selects Opus 5 for one productive task.
- Keep Claude's Superpowers, Code Review, and Code Simplifier available. Invoke
  them only when their result directly advances the current package:
  structural diagnosis, one consequential review, or simplifying an already
  working change. They are not automatic stages and do not override the 90/10,
  no-test, no-subagent, smallest-change, or stop-after-done rules. Keep
  zero-context LSP diagnostics such as Pyright enabled for local errors, while
  treating user-goal mismatch and cross-component behavior as SWE problems
  that require tracing the actual execution path.
- Do not use the Codex-in-Claude plugin as a second GPT harness. Claudex is the
  explicit GPT-through-Claude-Code route; hidden Claude agents remain denied.
- GLM 5.2 remains an explicitly selected mechanical/context-heavy OpenCode
  alternative, never the silent fallback for the OpenAI role profiles.
  OpenCode's native database records message tokens, costs, and skill tool
  calls. Pi is a lightweight optional harness
  with exact per-message usage in JSONL and explicit skill commands, but it is
  not a standing ecosystem role until it offers a concrete advantage over the
  selected Codex, Claudex, Claude, or OpenCode route.

## Watcher, verifier, messenger, and limits

The long-running system service performs waiting. A model turn never polls
indefinitely.

1. The service receives a Herdr, process, scheduler, silence-deadline, or
   capacity event. Each watch names its success event, failure event, owning
   task, maximum silence window, and recovery action.
2. A native Codex Luna-low watcher receives only the changed event and returns
   silent, message, or verify. The model does not perform the waiting loop.
3. Unchanged events stop immediately. Reaching the maximum silence window is a
   real event: wake the owning suborchestrator or Operations with the latest
   state and required recovery action.
4. Only an unusual, consequential event may open one optional fresh
   Sol-medium Verifier with bounded redacted evidence and no project-write
   access. Routine work self-verifies.
5. The verifier returns continue with one direct next action, ask the user, or
   sleep. It then closes.
6. Tool-free Flash drafts an important human message only when the human
   orchestrator approved it or an automatic important-event rule fired.
7. Trusted service code performs Herdr control and posting; Flash cannot. A
   watcher ends when the watched process ends, the task changes owner, or the
   terminal event fires; it may not remain as an idle pane.

Automatic important events are limited to a required user decision, accepted
goal-relevant result, confirmed unusual lack of progress, failed long-running
process, no productive route after a bounded advisor attempt, or material
Codex/Claude weekly-capacity change. Routine status and unchanged heartbeats
stay silent.
