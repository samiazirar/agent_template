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
- Default to no side artifacts. Do not create plans, reports, manifests,
  review files, dashboards, project hubs, duplicate READMEs, status documents,
  or prose records merely to describe work. Allowed outputs are the requested
  source/configuration, files required to run it, actual experiment outputs,
  and the existing `HUMAN_PLAN.md` and `OLD_HISTORY.md` required by the fixed
  Herdr layout. Project-root `RESTART_HANDOFF.md` is the one additional
  required record when the Human explicitly asks to save and close a project.

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
  Orchestrator or Operations Collaborator for routine status or unchanged state.

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
| Human orchestration | Claudex | Sol, high |
| Operations Lead | Codex | Sol, high |
| Background operations collaboration | Native Claude | Opus 5, medium |
| Normal implementation or execution | Codex or Claudex | Sol, medium |
| Bounded difficult implementation or decision | Codex or Claudex | Sol, high |
| One bounded strategic question | Codex or Claudex | Sol, xhigh |
| Temporary Plan Orchestrator | Codex or Claudex | Sol, medium |
| Independent alternative productive worker | Native Claude | Opus 5 |
| Mechanical or context-heavy alternative worker | OpenCode | GLM 5.2 |
| Researcher | Codex or Claudex | Terra, medium |
| Human-selected bounded productive worker | Codex | Terra, high |
| Cheap research observation | Codex or Claudex | Luna |
| Permanent event classification | OpenCode API key | Gemini 3.6 Flash |
| Optional minimal verification | Visible Codex or Claudex | Sol, medium |
| Human message drafting | OpenCode API key | Gemini 3.6 Flash |

Claudex is the Claude Code interface backed by the local Codex gateway. It is
not native Anthropic Claude. Launch it through `claudex` with an explicit Codex
model. Native Claude is selected separately when Opus 5 is wanted.

Terra and Luna normally serve research, interpretation, and observation.
Terra-high may be a productive worker only when the human explicitly selects
it for one bounded task; launch it as a Worker with normal worktree, commit,
reporting, and closure rules. Never use Vertex; Gemini routes use the OpenCode
API-key provider.

## Native Herdr launch

- Launch every independent agent as a named visible Herdr session with
  `herdr-agent <surface> "Role · PersonName Goal" [directory]`.
- `codex` and `claudex` use the synchronized GPT-5.6 Sol medium default.
  `claude` selects native Claude Opus 5 at medium effort by default.
- Never replace these sessions with hidden subagents or ordinary background
  subprocesses. Open a separate session only for independent productive work.
- Shared personal skills live once in `~/.agents/skills`. Claude and Claudex
  load the same directories through `~/.claude/skills`; do not maintain
  divergent copies.
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
- The Codex Sol-high Operations Lead owns decomposition, execution, worker and
  suborchestrator lifecycle, integration, synchronization, the 90/10 budget,
  and technical state. It is the sole operational authority and normal bridge
  between the Human Orchestrator and every technical role.
- The native Claude Opus-medium Operations Collaborator stays in the
  background. Operations Lead may wake it for one bounded collaborative plan,
  decomposition alternative, or milestone interpretation. It reports only to
  Operations Lead, never manages workers, integrates Git, contacts the Human
  Orchestrator, or becomes an approval step, and returns idle after one answer.
- Normal communication follows one path:
  `Human ↔ Human Orchestrator ↔ Operations Lead ↔ technical role`.
  Operations Collaborator is a bounded side input to Operations Lead. Workers,
  suborchestrators, Plan Orchestrators, advisors, researchers, and verifiers do
  not bypass Operations Lead.
- That path must work mechanically, not only in prose. Roles send cross-pane
  messages with `herdr-role-message`: Human Orchestrator uses
  `herdr-role-message operations`, Operations Lead uses
  `herdr-role-message human` or `herdr-role-message collaborator`, and
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
- One worker owns exactly one concrete subtask, branch, and worktree.
  Independent subtasks use concurrent workers. When a worker finishes,
  Operations Lead captures its short result and native session reference,
  closes the pane immediately, and then integrates or rejects the saved work.
  Workers receive
  tasks from and report only to Operations Lead or their one owning
  suborchestrator.
- Suborchestrators exist only for independent multi-step workstreams containing
  at least three productive subtasks. Each owns one workstream, launches one
  temporary worker per subtask, and closes when the stream ends. It may not
  create another suborchestrator.
- Strategic advisors are sparse temporary Sol-xhigh sessions. Give one advisor
  only the context for one bounded question, preferably yes/no or one concrete
  recommendation. Operations Lead launches it and receives its answer; it never
  contacts the user, implements, or manages and closes after answering.
- For consequential strategic planning or plan validation, the responsible
  orchestrator uses `consult-chatgpt-pro` with one compact question, then
  reconciles the advice against project evidence.
- Research defaults to one Terra-medium Researcher for a bounded evidence
  question. Terra may direct Luna read-only observers when cheaper parallel
  observation helps. Luna reports to Terra; Terra reports to Operations Lead
  for project work or the Architect for agent-system research. Research counts
  as productive only when it creates accepted goal-relevant evidence.
- Explicitly selected Terra-high productive work uses one bounded named Worker,
  one worktree, and the normal worker completion and closure rules.

## Watcher, verifier, messenger, and limits

The long-running system service performs waiting. A model turn never polls
indefinitely.

1. The service receives a Herdr, process, scheduler, silence, or capacity
   event.
2. Tool-free API-key Gemini 3.6 Flash returns silent, message, or verify.
3. Silent events stop immediately.
4. Only an unusual, consequential event may open one optional fresh
   Sol-medium Verifier with bounded redacted evidence and no project-write
   access. Routine work self-verifies.
5. The verifier returns continue with one direct next action, ask the user, or
   sleep. It then closes.
6. Tool-free Flash drafts an important human message only when the human
   orchestrator approved it or an automatic important-event rule fired.
7. Trusted service code performs Herdr control and posting; Flash cannot.

Automatic important events are limited to a required user decision, accepted
goal-relevant result, confirmed unusual lack of progress, failed long-running
process, no productive route after a bounded advisor attempt, or material
Codex/Claude weekly-capacity change. Routine status and unchanged heartbeats
stay silent.
