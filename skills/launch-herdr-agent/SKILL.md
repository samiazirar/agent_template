---
name: launch-herdr-agent
description: Launch a named interactive Codex, native Claude Opus 5, or Claudex GPT-5.6 Sol session as a visible native Herdr tab. Use only when the user explicitly asks to launch, open, start, or create one of these agents in Herdr. Do not use for hidden delegation, ordinary shell subprocesses, status-only sessions, or work that does not benefit from a separate context.
---

# Launch a Herdr agent

Require `HERDR_ENV=1`. If it is absent, explain that launching must begin from
inside Herdr and stop.

Use a human task name and the current workspace. Launch the agent in a new
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

Do not pass a task as an argv prompt. After the new agent reaches its native
interactive prompt, send its task with `herdr pane run` only when the user
provided one.

All three agents inherit the global execution standard. Codex loads shared
personal skills from `~/.agents/skills`; native Claude and Claudex load the same
skill directories through `~/.claude/skills`.

Use human names in reports. Keep Herdr's internal identifiers internal. Do not
leave a failed launch tab behind.
