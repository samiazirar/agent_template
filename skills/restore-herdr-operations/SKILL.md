---
name: restore-herdr-operations
description: Restore a missing or unreachable Operations Lead from the current Herdr Human Orchestrator while preserving the same Human chat. Use only when the Human-to-Operations helper reports that no live Operations Lead exists or the Operations role has disappeared. This is the Human Orchestrator's sole agent-launch exception.
---

# Restore Herdr Operations

Run exactly:

```bash
herdr-restore-operations
```

The helper resolves the current project even when this Human chat was moved,
starts one short-lived Sol-medium Launcher, and returns immediately. The
Launcher preserves this Human chat, restores exactly one native-Codex Sol-high
Operations Lead, performs a Human-to-Operations-to-Human route check, reports
the result here, and closes itself.

Do not use `herdr-agent`, raw Herdr launch commands, or any other control
command. Do not retry while the helper says a restore is already active. If an
Operations Lead is already live, continue through `herdr-role-message
operations` instead.
