---
name: save-close-herdr-project
description: Save a multi-session research project for a clean later restart and close only its current Herdr workspace. Use when the Human explicitly asks the Human Orchestrator to save, park, archive, stop, end, or close the current project or its whole space. Coordinate the final save through Operations Lead, require RESTART_HANDOFF.md and synchronized Git, close all temporary roles, then self-close the current workspace.
---

# Save and close a Herdr project

Preserve enough real state to restart the project, then close the complete
current workspace. Do not stop the shared Herdr server or named session.

## Require explicit intent

Use this workflow only after the Human clearly asks to save and close, park,
archive, stop, or end the current project. A pause in conversation, idle time,
or finished task is not permission to close the workspace.

If the Human says only “save,” preserve state but do not close. If the Human
says “close” while work is running and it is unclear whether that work should
finish, stop, or continue elsewhere, ask one natural-language question.

## Ask Operations Lead to save

Send one request with `herdr-role-message operations` that tells Operations
Lead to:

1. stop admitting new work;
2. finish the smallest coherent in-flight chunk or record its exact unfinished
   state without discarding it;
3. capture the final short report and native session reference for every
   temporary role, then close every worker, watcher, verifier, researcher,
   advisor, Plan Orchestrator, PaperPilot Maintainer, and suborchestrator;
4. stop local long-running processes or move intentionally continuing
   observation outside this workspace; do not cancel remote jobs unless the
   Human asked to cancel them;
5. integrate accepted work, retire finished worktrees, commit coherent changes,
   and push the canonical branch when a remote exists;
6. update `HUMAN_PLAN.md` through one temporary Plan Orchestrator only if the
   human-level current state or next useful result materially changed;
7. update `OLD_HISTORY.md` with the standing native session references and the
   close date;
8. write project-root `RESTART_HANDOFF.md` last, using the exact structure
   below, commit it as the final save commit, and synchronize it;
9. run the normal pane-lifecycle check and tell the Human Orchestrator that the
   project is ready to close.

Do not perform Operations work yourself. Remain available for a real Human
choice and answer naturally while Operations saves.

## Require this handoff

`RESTART_HANDOFF.md` is the one required technical restart record. It is an
explicit exception to the no-side-artifact default. Keep it concise and
factual, and use these exact markers and headings:

```markdown
Status: CAN RESTART
Close state: READY TO CLOSE

## Goal
## Current state
## Continue from here
## Running outside this workspace
## Git and saved work
## Restart context
## Human choices
```

Record remote scheduler jobs, services, and outputs that remain active under
`Running outside this workspace`; write `None` when there are none. Under
`Git and saved work`, include `Remote: none` when the repository intentionally
has no remote. Put native agent session references under `Restart context`,
never in `HUMAN_PLAN.md` or a normal user message.

Do not mark `READY TO CLOSE` until the save is actually complete. The handoff
must state what exists now, the first useful action after restart, unfinished
work, external activity, repository synchronization, and any unresolved Human
choice. It does not authorize work to resume.

## Self-close

After Operations Lead reports that the final save is complete, tell the Human:
“Saved. I’m closing this project now. We can reopen it later from the saved
handoff.”

Then run:

```bash
herdr-project-save-close --close
```

This is the Human Orchestrator's only permitted Herdr action besides
`herdr-role-message operations`. The helper accepts no workspace argument. It
checks the caller role, required files and handoff markers, clean Git state,
upstream equality when a remote exists, absence of temporary roles and
foreground watcher processes, and then closes only
`$HERDR_WORKSPACE_ID`.

For an older project that predates the standing Operations Collaborator, do
not launch one only for closure. Require one Human Orchestrator and one
Operations Lead; the collaborator may be absent while closing.

If the helper refuses, do not bypass it or call `herdr workspace close`
directly. Translate the one reported issue into ordinary language, send the
repair to Operations Lead, and run the helper again after Operations confirms
the correction.

Closing a workspace terminates all of its panes, including the Human
Orchestrator. It is not a Herdr archive shelf. Later restoration uses
`RESTART_HANDOFF.md`, `HUMAN_PLAN.md`, `OLD_HISTORY.md`, the synchronized
repository, and the `restart-research-team` skill.
