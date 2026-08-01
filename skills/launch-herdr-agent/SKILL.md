---
name: launch-herdr-agent
description: "Launch and brief a lightweight visible Herdr project team with one native-Codex human-only Human Orchestrator in its own phone-friendly tab, a native-Codex Sol-high Operations Lead in a separate tab, Markdown-only Human Plan pane, default quiet Sol-medium task suborchestrators that never code, fresh Luna-max sessions for frozen atomic worker packages or direct tiny tasks, direct child-to-parent wake-ups, compact restart continuity, and sparse researchers, advisors, or verifiers under a strict 90/10 productive-work budget. Use when an Architect asks to launch or repair a worker, research chain, project, team, ecosystem, or role topology. Run this in a separate short-lived Launcher session."
---

# Launch Herdr sessions

Require `HERDR_ENV=1`. If it is absent, explain that launching must begin from
inside Herdr and stop.

## Launch-only boundary

Keep the roles distinct:

- The standing `Architect` owns the agent system. After a project team exists,
  normal project conversation goes through its `Human Orchestrator`.
- A separate named `Launcher` creates and briefs the requested sessions,
  reports the result to the Architect, then stops.
- A Researcher or worker gathers evidence only. It must not edit the
  system, turn its own findings into improvements, or redirect an
  implementation worker unless the Architect explicitly changes its role.

Do only the setup needed to hand the goal to visible sessions:

- create or select the requested folder, repository, worktree, workspace, and
  human-named tabs;
- launch native interactive sessions;
- send each session its role and task after it reaches its prompt;
- confirm every launched session accepted its prompt.

Do not investigate the domain, inspect external systems, edit project code,
download assets, run experiments, submit jobs, test, review results, poll
work, or solve any part of the project in the launcher conversation. The
launched sessions own all productive and support work.

After all requested sessions are launched and working, send the Architect a
short human-language summary of who is working on what, then end with:

`LAUNCH COMPLETE — launcher stopped.`

The Architect remains active. Do not tell the user to close the Architect
chat, summarize project findings, or wait for worker completion.

## One requested session

Use a human task name and the current workspace. Launch the session in a new
background tab at the requested working directory. Do not create a new
workspace or worktree unless the user explicitly requests one.

Run:

```bash
herdr-agent \
  <opencode|opencode-high|opencode-xhigh|opencode-max|opencode-luna-low|opencode-luna|codex-low|codex|codex-high|codex-xhigh|codex-max|claude|claudex|claudex-high|terra|terra-high|luna-low|luna|luna-max> \
  "Role · PersonName Goal" [working-directory]
```

The launcher opens only the selected interactive executable:

- OpenCode profiles are alternate-provider routes only. Use them when the task
  explicitly selects GLM 5.2 or another non-OpenAI provider; never use them as
  the default harness for OpenAI Sol or Luna.

- `codex` uses the configured GPT-5.6 Sol model and medium reasoning.
- `codex-low` uses GPT-5.6 Sol at low reasoning for bounded research or data
  crunching; `codex-max` is reserved for a task that explicitly needs max.
- `codex-high` uses GPT-5.6 Sol at high reasoning for the Human Orchestrator.
- `codex-xhigh` uses GPT-5.6 Sol at xhigh reasoning for one strategic question.
- `claudex` uses the Codex-synchronized GPT-5.6 Sol model through the local
  Claudex gateway at medium effort.
- `claudex-high` uses the same Claudex route at high effort only when explicitly selected.
- `claude` is legacy-archive-only: resume an old native Claude chat solely to
  run `/export`, save it, and close it. Never assign Claude project work.
- `terra` uses GPT-5.6 Terra at medium reasoning for research interpretation.
- `terra-high` uses GPT-5.6 Terra at high reasoning for one bounded productive
  task only when the human explicitly selects Terra as a worker.
- `luna` and `luna-max` use GPT-5.6 Luna at max reasoning for normal clear,
  repeatable coding or execution packages. `luna-low` is limited to cheap
  support or supervision and is never a coding default.

The launcher pins Claudex sessions to the matching Sol profile without changing
the user's current global Codex model. A main Codex session may therefore use
Terra or another selected model without silently changing Claudex leadership.

Terra and Luna launch with normal native permissions because the local
read-only sandbox may prevent all file reads. A Terra Researcher prompt must
make its read-only boundary absolute. A Luna prompt follows its assigned role:
a Worker may edit its own worktree and commit its one bounded result; a routine
research task remains read-only. Neither may broaden its task.

Do not pass a task to the native executable as an argv prompt. After the new
agent reaches its interactive prompt, send its task with `herdr agent prompt`.
Never use `send-text` for a task or message. Native Codex accepts steering
during an active turn and explicit next-turn queuing. Do not call `agent prompt`
while an OpenCode target is working unless deliberate interruption is
required. If it shows “Messages to be submitted after next tool call,” the
message is queued rather than accepted: do not claim delivery or duplicate it.

Use `herdr-agent` for every normal launch so cost registration arms before the
first model turn. For native Codex, Terra, and Luna it uses Herdr's built-in
`agent start` readiness path rather than shell-run plus lifecycle polling. If a
launcher must create a model pane directly in another
workspace, it must immediately arm the same registration before sending the
task:

```bash
nohup herdr-costs register --workspace TARGET_WORKSPACE --pane NEW_PANE \
  --parent-pane OWNING_PARENT --surface PROFILE --wait-seconds 86400 \
  </dev/null >/dev/null 2>&1 &
```

Do not defer registration to cleanup or reconstruct usage from transcripts.

## Complete project launch

When the user requests a space, project, team, ecosystem, or the whole setup,
launch the two standing roles below. Operational execution uses native Codex;
OpenCode is an explicit alternate-provider choice for one productive task.

Create the standing roles in separate full-width tabs: the Human Orchestrator
alone in `01 Human`, and the Operations Lead in `02 Operations`. Never split
the Human tab. This keeps the normal conversation readable and controllable on
a phone. Do not add a standing Operations Collaborator unless the Human
explicitly requests one; place it only in Operations.

1. `Human Orchestrator · PersonName Goal` — native Codex Sol high. This is the
   project's only normal conversation with the human. Confirm the goal and its
   meaning, ask or answer necessary human questions, explain material results,
   and own the intended human-plan content. Send every technical request to
   Operations Lead and return its questions that need human judgment to the
   human. Never contact workers, suborchestrators, Plan Orchestrators, advisors,
   researchers, or verifiers directly; dispatch
   workers; manage execution; integrate Git; or expose internal mechanics.
   Speak like a thoughtful human collaborator. Start with the answer or
   outcome, use the project's own words, explain what it means and what comes
   next, and ask only for a real choice. Never use all-caps process headings or
   expose terms such as “evidence,” “accepted meaning,” “observable,”
   “routing,” “completion envelope,” “pane,” “session,” “worker,”
   “lifecycle,” “verified,” “authority,” “blocker,” or `READY FOR HUMAN`
   unless the human explicitly asks how the system works.
   Send every technical instruction with
   `herdr-role-message operations "..."`. Never use native model-agent lookup.
   Its only other Herdr action is `herdr-project-save-close --close`, after the
   Human explicitly asks to save and close and Operations confirms the final
   handoff, role closure, Git commit, and synchronization are complete. Treat
   “do,” “go,” and “continue” as authorization for the already-discussed
   action and forward it immediately; do not answer with readiness alone.
2. `Operations Lead · PersonName Goal` — native Codex Sol high. Own decomposition,
   execution order, worktrees, worker and suborchestrator lifecycle,
   integration, commits, synchronization, technical state, and the rolling
   90/10 budget. Be the sole operational authority and normal bridge between
   the Human Orchestrator and every technical role.
   Never implement, patch, debug, broadly inspect project code, run an
   experiment, or SSH for technical work. Dispatch each such need to Luna and
   integrate only accepted worker commits.
   Use `herdr-role-message human "..."` for human questions or material results.
   When a forwarded confirmation arrives, start the named action instead of
   acknowledging it again.
Normal communication must follow:
`Human ↔ Human Orchestrator ↔ Operations Lead ↔ technical role`. Operations
Lead is the sole technical authority. No technical role may bypass it.
The messenger adds a compact target-specific boundary reminder on every routed
message; do not repeat the full role contract in routine communication.

Before launching, require `command -v herdr-role-message`,
`command -v herdr-emergency-wake`, `command -v herdr-project-save-close`, and
`command -v herdr-costs`. After launch,
perform one real round trip: ask Human Orchestrator to send a short route-check
message to Operations Lead through the helper; Operations Lead replies through
the helper; Human Orchestrator confirms naturally. If either leg fails, repair
the route or replace the failed standing session before reporting readiness.
When Operations Lead is intentionally working on the forwarded instruction,
run the live-team validator with `--allow-active-standing`; do not force it idle
merely to satisfy a readiness-only check.

Never use `herdr pane report-agent`, `report-metadata`, or `release-agent` to
polish standing-role status. Native integration owns status. A standing pane in
`done` has completed its latest turn and remains valid.

## Enforce the 90/10 budget

Operations Lead classifies observed outputs, not role names:

- productive contribution is an observed action whose result is necessary and
  causally advances the approved goal. It includes implementation, runs,
  measurement, evaluation, integration, and the minimum useful human
  instruction, clarification, decision, decomposition, dispatch, recovery,
  synchronization, or closure needed to move that work;
- overhead consumes time or tokens without materially changing the next
  action or result, such as repetition, detached planning, status-only turns,
  waiting or polling, duplicate reading, and unnecessary checking or review;
- drift or waste advances a different goal, violates the assigned role or
  scope, overengineers beyond the requested result, or continues a failed path
  after disconfirming evidence. Leave genuinely ambiguous work unclassified;
- attached reproduction and verification remain part of the productive task.

No role, model, or session label is inherently productive or overhead. A Human
Orchestrator can make a productive clarification, and a Worker can drift. Use a
bounded Luna transcript analysis against `HUMAN_PLAN.md` and the frozen task
goal for semantic percentages; the deterministic cost ledger must leave
unanalyzed work unclassified instead of using a role-name proxy.

Before opening a session expected to produce only support or overhead,
Operations Lead checks the rolling share of active task slots and agent-hours.
At or above 10% overhead/drift, launch the next independent
productive task instead. Exceed 10% only for immediate safety, an irreversible
action, or a human decision that truly prevents productive work. Every proposed
overhead action must name the productive action it directly unlocks. Idle standing roles
consume no turns and must not be woken for routine status.

Do not put the Human Orchestrator in `00 Human Plan`. That tab contains exactly
one non-agent pane rendering the canonical Markdown:

```bash
frogmouth HUMAN_PLAN.md
```

If the plan is missing or its meaning changed, leave the viewer shell in place
until the Human Orchestrator has accepted the goal. Operations Lead then launches
one temporary `Plan Orchestrator · PersonName Update` using Sol medium in
`02 Operations`. This is an orchestrator, not a worker. The Human
Orchestrator gives accepted meaning to Operations Lead; Operations Lead gives
the Plan Orchestrator that meaning plus checked evidence. The Plan Orchestrator
edits only `HUMAN_PLAN.md` in an isolated worktree, commits, reports only to
Operations Lead, and stops. Operations Lead asks the Human Orchestrator to
check meaning, integrates, synchronizes, refreshes the viewer, and closes the
Plan Orchestrator.

The plan writer uses the same natural human voice: “what we know,” “results,”
“measurements,” and “next useful result.” It removes internal terms such as
“evidence,” “observable,” “accepted meaning,” “durable,” “routing,”
“verified,” “lifecycle,” completion-envelope language, pane/session/worker
language, and all-caps readiness labels.

For productive work, Operations Lead normally launches one owning Sol-medium
suborchestrator. That owner freezes one atomic card and launches one fresh
named native-Codex Luna-max session for it, then closes it before launching a
new Luna session for the next atomic card. The suborchestrator never codes,
edits project files, or executes experiments, and stays quiet while its worker
runs. It also never searches project code, debugs, reproduces, or inspects a
remote system itself; those are Luna packages. One worker owns one deliverable, one
reproduction or run, one done check, normally no more than three tightly
coupled files or one experiment stage, one branch, and one worktree. Launch multiple
workers concurrently when their subtasks are independent. Never give one
worker several unrelated subtasks. When it finishes, capture its final short
report and native session reference, close its pane immediately, and then
integrate or reject the saved result. Retire its worktree after merge or
rejection. Every later package or correction uses a fresh worker chat. A worker receives its task from and
reports only to Operations Lead or its one owning suborchestrator; it never contacts
the Human Orchestrator or user.

The parent never waits inside its model turn. After launching a child, arm
`herdr-emergency-wake` with the child pane, a realistic maximum-silence interval,
and one recovery action, then finish the parent turn after dispatching any
other independent work. The child reports with `herdr-role-message`, which
wakes or steers the parent, and stops without waiting for acknowledgement.
Closing the child pane disarms the emergency wake. Never run `herdr agent wait`,
`sleep`, or a polling loop in Operations Lead or a suborchestrator.
When maximum silence actually fires, the emergency helper also uses Herdr's
native notification surface before waking the owning role; no messenger model
or polling watcher is needed for that alert.
If Herdr reports an implausible lifecycle state, use `herdr agent explain` to
inspect the active detection rule without spending a model turn on self-diagnosis.

Luna self-verifies against the attached done check. Give a harder package to a
fresh native-Codex Sol-medium worker when Luna cannot choose between materially different approaches,
its first coherent repair fails, the work expands beyond its bounded
subsystem, tool results contradict the task premise, or the result cannot be
reproduced. Do not open a verifier or spend a Sol turn after every successful
Luna task.

For one meaningful task, Operations Lead launches one native-Codex Sol-medium
named suborchestrator in `04 Suborchestrators`. Give it one measurable task goal
and observed finish condition. It does no coding or experiment execution. It
turns only the next useful work into a frozen atomic task card, launches one fresh
native-Codex Luna-max worker per normal coding package or native-Codex Sol-medium worker for a harder
package, absorbs only compact child results, reports the finished task to
Operations Lead, and closes when the task ends. Operations may launch a direct Luna-max worker only
for an explicit tiny atomic task. Sol-medium coding workers are harder-package
escalations after Luna. It communicates only with Operations
Lead and its own workers. It may not contact the Human Orchestrator, create
another suborchestrator, or add a review turn after every successful task.

Do not launch standing advisors, watchers, reviewers, progress checkers, Plan
Orchestrators, verifiers, or suborchestrators. Open each only for its immediate
bounded purpose; classify the actual action rather than charging the role by
name.

When the Human explicitly asks where time or tokens went, open one temporary
native-Codex Luna-max `Usage Analyst · PersonName Project Usage` in
`06 Progress Checks`. It runs `herdr-costs` first, reads the relevant
`HUMAN_PLAN.md`, and may launch fresh Luna-low Usage Readers for disjoint,
bounded current or archived transcript batches. It reports the expensive
agents and tasks, cache use, repetition, context growth, drift, and actual plan
contribution, then closes every reader and itself. It creates no report file
and never implements its recommendation.

Create one compact project-root `RESTART_HANDOFF.md` at launch and keep it
restart-ready after every material result, active-task change, external wait,
or decision. It contains only the goal, current result/code state, running
external work, exact next action, and Git state. `HUMAN_PLAN.md` remains the
only human-facing plan. Do not create further status artifacts.

Ordinary child completion needs no model watcher: the child message wakes its
parent and `herdr-emergency-wake` covers maximum silence. A native-Codex
Luna-low watcher is reserved for genuinely long processes or scheduler events;
its card names success, failure, maximum silence, owner, recovery action, and
terminal event. Never leave an active task represented only by an idle or
waiting pane.

`herdr-agent` registers every session automatically. The lightweight
terminal command `herdr-costs report` shows today's human-named hierarchy with
own and aggregate time, Luna-max token share, tokens, and API-equivalent cost.
It labels semantic overhead/drift unavailable until bounded Luna transcript
analysis is run. `herdr-costs report --all` adds every used agent across
projects; `--all-time` is the explicit lifetime view. Do not
launch an agent to measure usage and do not create a manual dashboard.

OpenCode alternate-provider usage comes from its native database. Native Codex
usage is collected by the Herdr integration. Claudex uses the zero-context `SessionStart` command hook
`herdr-costs register-hook`, so new and resumed Herdr sessions remain attached
to the ledger even when the native Claude harness recreates its session. The
report also shows actual skill uses with associated tokens and cost. Keep
Pyright LSP enabled for automatic Python diagnostics. Keep Superpowers, Code
Review, and Code Simplifier available but never make them automatic stages;
invoke one only when it directly advances the current package and keep its
work inside the 10% control budget. Concrete failures use
`goal-directed-repair` to preserve the original user problem, trace structural
behavior when needed, repair the causal source, and stop after the direct done
check.

Bounded research and data crunching use Sol at the lowest sufficient effort,
from low through max. Use a named Terra-medium `Researcher` by default for an
open-ended question requiring synthesis
or interpretation. Both report to Operations Lead for project research or the
Architect for agent-system research. Research is productive only when it
creates accepted goal-relevant evidence; otherwise charge it to the 10%
control budget. A Researcher does not implement findings unless the Architect
explicitly changes the assigned role.

When the human explicitly selects Terra-high for productive work, launch
`terra-high` as a `Worker`, not a Researcher. Give it one bounded deliverable,
one worktree, the normal worker write and completion rules, and no authority to
delegate or broaden the task.

For a new project explicitly requesting isolation:

- create one canonical project folder and Git repository;
- create one task worktree per productive worker;
- create a background Herdr workspace with human-readable tabs;
- keep Herdr identifiers out of prompts and user messages.

Use these fixed organizational tabs when the user asks for the full research
structure:

- `00 Human Plan`
- `01 Human`
- `02 Operations`
- `03 Strategic Council`
- `04 Suborchestrators`
- `05 Workers`
- `06 Progress Checks`
- `99 Old History`

Tabs may remain empty when no justified role exists.

## Strategic advice

Keep `03 Strategic Council` empty until an orchestrator has one exact
consequential question. Then launch one temporary `Strategic Advisor ·
PersonName Question` using `codex-xhigh`.

Operations Lead gives the advisor only the decision context needed for that
question. Prefer a yes/no verdict; otherwise request one concrete recommended
approach. The advisor reports only to Operations Lead and does not contact the Human
Orchestrator or user, inspect broadly, implement, manage, or create more agents.
Capture the answer, let Operations Lead route its material meaning, and close the
advisor immediately.

For consequential strategic planning or plan validation, the responsible
Operations Lead must use `consult-chatgpt-pro` with one compact evidence packet
and one bounded question. It reconciles Pro's advice against project evidence;
Pro does not approve work or replace the orchestrator. If the configured Pro
transport is unavailable, record that once and continue from project evidence
unless the decision is unsafe without external advice.

## Prompt each role

Wait only until each native session is idle, then send a concise role-specific
prompt. Before sending it, render the canonical role block with
`scripts/validate_role_card.py <role> --print`, include that block unchanged in
the prompt, and validate the composed prompt with
`scripts/validate_role_card.py <role> --check <prompt-file>`.

Every task-bearing prompt must include:

- the preserved project goal in plain language;
- the role's differing current and expected states;
- one role-appropriate outcome;
- the explicitly selected model and effort, using native-Codex Luna-max below
  a Sol-medium suborchestrator or directly from Operations for one tiny atomic
  task, and native-Codex Sol-medium only for a harder-package escalation;
- the working directory or worktree;
- the concise `AGENT_SYSTEM_STANDARD.md` and project `AGENTS.md`; only standing
  leaders and suborchestrators load the long onboarding and orchestration
  manuals;
- the instruction to coordinate through visible Herdr sessions;
- the instruction to stop and report its completion envelope when done.
- the existing implementation to reuse or the concrete reason no suitable one
  exists;
- permission to delete clearly bad, dead, duplicate, or superseded code; and
- a no-side-artifact rule forbidding reports, manifests, dashboards, project
  hubs, review files, duplicate documentation, and status files.
- for a concrete failure, the shared `goal-directed-repair` skill and its
  smallest causal repair boundary; never a broad debugging workflow.

The Human Orchestrator prompt must identify it as the sole human conversation
and require all technical communication to pass through Operations Lead. It
must include the human-voice rules above and request a natural opening sentence,
not a role-contract recital. It must name `herdr-role-message operations` as
the only valid technical route, name `save-close-herdr-project` and
`herdr-project-save-close --close` as the sole explicit project-closing
exception, require a continuously current compact `RESTART_HANDOFF.md`, and
forbid native Agent lookup. The Operations Lead prompt must
require a quiet Sol-medium suborchestrator by default, one new fresh Luna-max
session per frozen atomic package, and direct Luna-max only for a tiny atomic task, concurrent
independent workers, closure immediately after a transient final report is
captured and before integration, sole-bridge routing, and active enforcement of
the 90/10 budget. It must forbid `herdr agent wait`, `sleep`, and polling for child
roles; require direct child wake messages and one armed emergency wake per
child.
Worker prompts must give one Luna-sized result and forbid hidden delegation,
unrelated work, and direct human-side contact. Suborchestrator prompts use Sol
medium through native Codex, define one task and finish condition, forbid coding,
repository inspection, debugging, reproduction, SSH, and experiment execution,
make Luna launch the first technical action, issue minimal packages to fresh
workers, report only to Operations Lead, and forbid another
orchestration layer.
Plan Orchestrator prompts must limit writes to `HUMAN_PLAN.md`, report only to
Operations Lead, and stop after one commit. Bounded research/data prompts use
selected Sol effort; open-ended synthesis uses Terra. Verifier prompts are optional, minimal,
read-only, and only for one
consequential anomaly. Advisor prompts must contain one bounded question,
report only to Operations Lead, and forbid implementation.
Usage Analyst prompts use Luna max and the canonical `usage-analyst` block;
their bounded Luna-low transcript readers use `usage-reader`. Both are
read-only, on-demand, and close after one answer.

Require technical sessions to acknowledge, in one concise message, their role,
who they receive from, who they report to, and their main forbidden boundary.
The Human Orchestrator instead opens naturally, for example: “I’m ready. I’ll
keep our conversation focused on the outcome you want and bring you only the
choices that need you.” Validate its contract from the rendered prompt; never
make it recite internal routing to the human. Reject and resend a corrected
prompt if an acknowledgement contradicts the canonical role block. Do not open
a separate checker agent.

After prompting, wait only for each session to become working. Use
`herdr agent prompt TARGET TASK --wait --until working --until idle --until done
--until blocked --timeout 10000` after the target reports `idle` or `done`.
Herdr returns `agent_prompt_stalled` when submission produces no lifecycle
change. This is the mechanical send check; text merely visible in an input box
or queue is not an accepted prompt. If a launch fails, close only the failed tab, retry once with
the same surface, and report the concrete launch failure if the retry also
fails.

Do not count a process, TUI, or `working` transition as a successful start by
itself. Inspect the first real model response or task action. Authentication,
provider, permission, and immediate-exit messages are failed launches. Repair
the cause and retry once. If recovery requires the Human or an outside event,
save the current state and exact recovery action in `RESTART_HANDOFF.md` and
attach one bounded event watcher instead of assuming the work will resume.

Both standing agents inherit the global execution standard. OpenCode and Codex
load shared personal skills directly from `~/.agents/skills`; Claudex loads
the same skill directories through `~/.claude/skills` when explicitly used.

Use human names everywhere visible to people. Keep Herdr's internal identifiers
internal. Do not perform project work while launching and do not leave a failed
launch tab behind.

For repairs, inspect leadership history before rebriefing. If a standing
session has compacted, shows a blocked internal goal, or failed the real route
check, archive its native session reference and replace it with a fresh session.
Do not preserve a stale session merely to keep the pane count unchanged.
