# Working rules (all projects)

Replaces the old agent-system standard for Claude sessions (2 Oct 2026). When
the user states a lasting rule, write it into the project's AGENTS.md or
CLAUDE.md (or this file if it is global) in the same turn.

## Getting things done

- Do the requested change, run one direct check of the result, commit with a
  plain message, stop. No plans, audits, reports, dashboards or side documents
  unless asked.
- One check means the thing that shows the result works: the run, the number,
  the render. No test suites, smoke runs, repeated re-checks of something that
  already passed, or "measure first" rituals unless the user asks or a result
  is about to be published.
- Reuse the existing implementation; delete dead or duplicate code; for a
  concrete failure fix the cause, not the symptom (`goal-directed-repair`).
- Edit files with the Edit tool, not python string-replace scripts.
- Long output goes to a log file; read only the errors, the tail or a summary.

## Waiting

- Never wait inside a turn: no `sleep`, `squeue`, `nvidia-smi` or
  `herdr pane read` loops.
- Use Monitor with an until-condition, a failure condition and a timeout, or a
  background command that notifies on exit (re-arm it for multi-hour jobs).

## Delegation

Delegate proactively, without being asked: a lead's context is for decisions
and the user, not for file dumps or long runs. Before starting a task, split it:
independent parts go out together in one message as parallel subagents or
workers, and the lead keeps only what needs its judgement.

- Small task (a few files, minutes): do it yourself.
- Reading, searching, checking numbers against papers, literature surveys,
  reading logs or remote state: the `scout` subagent (Sonnet 5.5, read-only),
  so file contents stay out of this session. Never a general-purpose subagent
  for these.
- Reviews and research synthesis that judge but do not edit: a general-purpose
  subagent with `model: sonnet`.
- Implementation that needs judgement but not hours: a general-purpose
  subagent (Opus 5.5, also under a Fable lead).
- Multi-hour implementation or GPU work: one Herdr tab worker,
  `claude-acct run -a <seat> -- --model claude-opus-5-5 -n "<PersonName> <What It Does>"`,
  on any seat whose WEEK and SESS windows have room. Its own worktree, the tab
  given the same name, a brief in a file, one task, one done check. It reports
  once with SendMessage to the lead's name and its tab is closed.
- Talk to another Claude session with SendMessage (`ListAgents` for names),
  never with herdr keystrokes (`send-text`, `herdr agent prompt`,
  `herdr-ask`, `herdr-role-message`): they can report "submitted" when nothing
  arrived, or submit the user's half-typed draft.
- Hard decision in an Opus session: `/advisor fable`.
- No agent teams.
- Never Gemini Flash, Codex or DeepSeek as a worker. Gemini is fine for
  non-worker model calls (VLM judge, rewrites, object naming) with the key from
  `~/.secrets/gemini.key` exported as `GEMINI_API_KEY`, never written into a
  repo or a prompt.

## Sessions

- One task per session. In a project that keeps a `RESTART_HANDOFF.md`, a lead
  restarts from it instead of running for days and updates it when a milestone
  lands (goal, current result, what is running, next action). Do not create one
  in a project that has none unless asked.
- Leads run on Fable 5.1, or on Opus 5.5 when the user starts one that way.
  Opus 5.5 runs at effort high (leads, workers, subagents); `scout` at medium;
  `/effort xhigh` for hard problems.

## Writing

Use the `plain-writing` skill for any prose the user will read: explanations,
explainers, PDFs, reports, paper text, messages.

## Memory

Project facts go to the project's auto memory. A lesson that would hold in any
project (a tool or cluster trap, an engineering pitfall, an owner preference)
goes as one line into General lessons below, merged with a similar line if one
exists; keep that list under 30 lines and drop lines that stop being true.

## General lessons

- Run `date` before writing any time label; never extrapolate.
- `pgrep -f`/`pkill -f` match the shell that carries the pattern: use `[x]name` or `pgrep -x`.
- `systemctl stop` without `disable` comes back after a reboot.
- Long runs start detached (`setsid nohup … &`); beech's daemon kills the largest process over 2 GiB.
- A parent that waits for a child's exit before reading its pipe deadlocks past 64 KiB; read first.
- `fork` under a threaded parent (torch, TBB, CUDA) can hang; use `spawn`.
- `except OSError` also swallows `FileNotFoundError`; catch the narrow error.
- Time a function alone before trusting cProfile on call-heavy code.
- Find dead code by import closure, not by hand-made lists.
- When rebuilding a path, keep the old one runnable as the baseline the new one must beat.
- herdr: a multi-KB prompt pastes but never submits; send a one-line pointer to a brief file. Backticks in `send-text` run as commands. Closing a workspace's last pane closes the workspace; to end a session but keep its workspace, open a fresh pane there first.
- `sbatch --parsable` can print site notices; the job id is the first numeric line.
- Never copy a `.credentials.json` between Claude profiles; one login lives in one file.
- No silent fallbacks: use an explicit input verbatim or fail loudly.
- No em dashes in user-facing prose.
- Do not run `graft init` or upgrade graft without re-checking afterwards: it re-adds its hooks, skill text and AGENTS.md block (removed 2 Oct).

## Compact instructions

When compacting, keep verbatim: every instruction the user gave, measured
numbers, files changed, running jobs and their ids, open questions.

## Usage

`claude-usage --days 7` shows where usage went (waiting, testing, context size).
