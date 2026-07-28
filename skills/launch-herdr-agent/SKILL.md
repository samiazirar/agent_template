---
name: launch-herdr-agent
description: "Launch and brief named Codex, Claudex, Claude, Terra, or Luna sessions as visible native Herdr tabs when an Architect asks for a worker, research chain, project team, ecosystem, or set of roles. Use this in a separate short-lived Launcher session; never convert the standing Architect or user-facing session into the disposable launcher. The Launcher creates the requested topology, reports readiness to the Architect, and stops without doing project work."
---

# Launch Herdr sessions

Require `HERDR_ENV=1`. If it is absent, explain that launching must begin from
inside Herdr and stop.

## Launch-only boundary

Keep the roles distinct:

- The standing `Architect` keeps the user conversation, owns system changes,
  interprets research reports, and remains open.
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
herdr-agent <codex|claude|claudex> "Role · PersonName Goal" [working-directory]
```

The launcher opens only the native interactive executable:

- `codex` uses the configured GPT-5.6 Sol model and medium reasoning.
- `claudex` uses the Codex-synchronized GPT-5.6 Sol model through the local
  Claudex gateway.
- `claude` uses native Claude Opus 5 at medium effort unless
  `HERDR_CLAUDE_EFFORT` explicitly selects another supported effort.

Do not pass a task to the native executable as an argv prompt. After the new
agent reaches its interactive prompt, send its task with `herdr pane run`.

## Complete project launch

When the user requests a space, project, team, ecosystem, or the whole setup,
launch a mixed GPT-5.6 Sol team. Use Codex and Claudex; do not substitute
Claude unless the user explicitly asks for Opus.

Create only roles with immediate ownership:

1. `Operations · PersonName Goal` — Codex. Own execution, task cards,
   integration order, commits, sync, and session lifecycle.
2. `Human Orchestrator · PersonName Goal` — Claudex. Own `HUMAN_PLAN.md`,
   human-language status, and user-facing decisions; do not manage daily
   execution.
3. One named productive worker per independent first task. Alternate Codex and
   Claudex so both surfaces are represented. Give each worker one deliverable
   and one working directory or worktree.

Do not launch standing advisors, watchers, reviewers, progress checkers, or
suborchestrators. Operations may launch them later only when the project
standard and live work justify them.

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

## Prompt every role

Wait only until each native session is idle, then send a concise prompt. Every
prompt must include:

- the preserved project goal in plain language;
- the role's differing current and expected states;
- one directly productive deliverable;
- the working directory or worktree;
- the relevant shared standards and project `AGENTS.md`;
- the instruction to coordinate through visible Herdr sessions;
- the instruction to stop and report its completion envelope when done.

Leadership prompts must say they may launch additional visible sessions when
justified. Worker prompts must forbid hidden delegation and unrelated work.

After prompting, wait only for each session to become working. If a launch
fails, close only the failed tab, retry once with the same surface, and report
the concrete launch failure if the retry also fails.

All three agents inherit the global execution standard. Codex loads shared
personal skills from `~/.agents/skills`; native Claude and Claudex load the same
skill directories through `~/.claude/skills`.

Use human names everywhere visible to people. Keep Herdr's internal identifiers
internal. Do not perform project work while launching and do not leave a failed
launch tab behind.
