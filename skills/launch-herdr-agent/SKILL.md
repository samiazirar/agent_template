---
name: launch-herdr-agent
description: "Launch and brief a visible Herdr project team with a human-only Human Orchestrator, execution-owning Operations Orchestrator, Markdown-only Human Plan pane, one temporary worker per subtask, optional multi-step suborchestrators, and sparse Sol-xhigh strategic advisors. Use when an Architect asks to launch or repair a worker, research chain, project, team, ecosystem, or role topology. Run this in a separate short-lived Launcher session; never replace the standing Architect or project Human Orchestrator."
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
- A research lead or worker gathers evidence only. It must not edit the
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
  <codex|codex-high|codex-xhigh|claude|claudex|claudex-high|terra|luna> \
  "Role · PersonName Goal" [working-directory]
```

The launcher opens only the native interactive executable:

- `codex` uses the configured GPT-5.6 Sol model and medium reasoning.
- `codex-high` uses GPT-5.6 Sol at high reasoning for project leadership.
- `codex-xhigh` uses GPT-5.6 Sol at xhigh reasoning for one strategic question.
- `claudex` uses the Codex-synchronized GPT-5.6 Sol model through the local
  Claudex gateway.
- `claudex-high` uses the same Claudex route at high effort for the Human
  Orchestrator.
- `claude` uses native Claude Opus 5 at medium effort unless
  `HERDR_CLAUDE_EFFORT` explicitly selects another supported effort.
- `terra` uses GPT-5.6 Terra at medium reasoning for research interpretation.
- `luna` uses GPT-5.6 Luna at low reasoning for cheap research observation.

Terra and Luna launch with normal native permissions because the local
read-only sandbox may prevent all file reads. Their prompt must make the
evidence-only boundary absolute: inspect only the named sources, run no broad
repository or filesystem audit, and never edit, commit, push, test, retry
unrelated work, or implement findings.

Do not pass a task to the native executable as an argv prompt. After the new
agent reaches its interactive prompt, send its task with `herdr pane run`.

## Complete project launch

When the user requests a space, project, team, ecosystem, or the whole setup,
launch a mixed GPT-5.6 Sol team. Use Codex and Claudex; do not substitute
Claude unless the user explicitly asks for Opus.

Create these standing roles in `01 Orchestrators`:

1. `Human Orchestrator · PersonName Goal` — Claudex Sol high. This is the
   project's only normal conversation with the human. Confirm the goal and its
   meaning, ask or answer necessary human questions, explain material results,
   and own the intended human-plan content. Send every technical request to
   Operations and return Operations questions that need human judgment to the
   human. Never contact workers, suborchestrators, writers, advisors, or
   verifiers directly; dispatch workers; manage execution; integrate Git; or
   expose internal mechanics.
2. `Operations · PersonName Goal` — Codex Sol high. Own decomposition,
   execution order, worktrees, worker and suborchestrator lifecycle,
   integration, commits, synchronization, and technical state. Be the sole
   normal bridge between the Human Orchestrator and every technical role.
   Route only accepted material results, genuine decisions, direction changes,
   and questions needing human judgment to the Human Orchestrator.

Normal communication must follow:
`Human ↔ Human Orchestrator ↔ Operations ↔ technical role`. No technical role
may bypass Operations to contact the Human Orchestrator or user.

Do not put the Human Orchestrator in `00 Human Plan`. That tab contains exactly
one non-agent pane rendering the canonical Markdown:

```bash
frogmouth HUMAN_PLAN.md
```

If the plan is missing or its meaning changed, leave the viewer shell in place
until the Human Orchestrator has accepted the goal. Operations then launches
one temporary `Human Plan Writer · PersonName Update` worker. The Human
Orchestrator gives the accepted meaning to Operations; Operations briefs the
writer; the writer edits only `HUMAN_PLAN.md` in an isolated worktree, commits,
and reports only to Operations. Operations asks the Human Orchestrator to check
meaning, checks evidence, integrates, synchronizes, refreshes the viewer, and
closes the writer.

For productive work, Operations launches one named worker for each concrete
subtask. One worker owns one deliverable, branch, and worktree. Launch multiple
workers concurrently when their subtasks are independent. Never give one
worker several unrelated subtasks. Integrate or reject its result, then close
its session and retire its worktree. A worker receives its task from and
reports only to Operations or its one owning suborchestrator; it never contacts
the Human Orchestrator or user.

For a genuinely independent multi-step workstream, Operations may launch one
named suborchestrator in `03 Suborchestrators`. Give it one measurable
workstream. It decomposes that stream, launches one temporary worker per
subtask, integrates the stream for Operations, and closes itself when the
workstream ends. It communicates only with Operations and its own workers. It
may not contact the Human Orchestrator or create another suborchestrator.

Do not launch standing advisors, watchers, reviewers, progress checkers, plan
writers, or suborchestrators. Open each only for its immediate bounded purpose.

When the Architect explicitly requests a research chain, launch a named Terra
research lead and a named Luna read-only worker. Luna reports evidence to
Terra; Terra consolidates it for the Architect. Neither session implements the
result.

For a new project explicitly requesting isolation:

- create one canonical project folder and Git repository;
- create one task worktree per productive worker;
- create a background Herdr workspace with human-readable tabs;
- keep Herdr identifiers out of prompts and user messages.

Use these fixed organizational tabs when the user asks for the full research
structure:

- `00 Human Plan`
- `01 Orchestrators`
- `02 Strategic Council`
- `03 Suborchestrators`
- `04 Workers`
- `05 Progress Checks`
- `99 Old History`

Tabs may remain empty when no justified role exists.

## Strategic advice

Keep `02 Strategic Council` empty until an orchestrator has one exact
consequential question. Then launch one temporary `Strategic Advisor ·
PersonName Question` using `codex-xhigh`.

Operations gives the advisor only the decision context needed for that
question. Prefer a yes/no verdict; otherwise request one concrete recommended
approach. The advisor reports only to Operations and does not contact the Human
Orchestrator or user, inspect broadly, implement, manage, or create more agents.
Capture the answer, let Operations route its material meaning, and close the
advisor immediately.

For consequential strategic planning or plan validation, the responsible
orchestrator must use `consult-chatgpt-pro` with one compact evidence packet
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
- the working directory or worktree;
- the relevant shared standards and project `AGENTS.md`;
- the instruction to coordinate through visible Herdr sessions;
- the instruction to stop and report its completion envelope when done.

The Human Orchestrator prompt must identify it as the sole human conversation
and require all technical communication to pass through Operations. The
Operations prompt must require one worker per subtask, concurrent independent
workers, prompt closure, and sole-bridge routing to the Human Orchestrator.
Worker prompts must forbid hidden delegation, unrelated work, and direct
human-side contact. Suborchestrator prompts must define one multi-step
workstream, report only to Operations, and forbid another orchestration layer.
Advisor prompts must contain one bounded question, report only to Operations,
and forbid implementation.

Require the launched session to acknowledge, in one concise message, its role,
who it receives from, who it reports to, and its main forbidden boundary.
Reject and resend a corrected prompt if that acknowledgement contradicts the
canonical role block. Do not open a separate checker agent.

After prompting, wait only for each session to become working. If a launch
fails, close only the failed tab, retry once with the same surface, and report
the concrete launch failure if the retry also fails.

All three agents inherit the global execution standard. Codex loads shared
personal skills from `~/.agents/skills`; native Claude and Claudex load the same
skill directories through `~/.claude/skills`.

Use human names everywhere visible to people. Keep Herdr's internal identifiers
internal. Do not perform project work while launching and do not leave a failed
launch tab behind.
