---
name: goal-directed-repair
description: Repair a bug, failed command, broken implementation, or unexpected behavior by finding the causal root and making the smallest root-level change. Use when Codex, Claudex, or Claude Code is asked to fix or repair a concrete failure. Do not use for broad audits, speculative cleanup, general code review, or creating test suites.
---

# Goal-directed repair

Fix the concrete failure without widening the task. Root-cause work is useful
only when it produces the requested working state.

## Repair loop

1. Restate the intended result and the observed failure in one sentence each.
   Preserve the user's goal and scope.
2. Reproduce the failure once with the cheapest direct command or inspect the
   existing failing output when reproduction would be costly. Read the actual
   error and the nearest relevant code; do not begin with a repository audit.
3. Search the current project, recent relevant change, official upstream, and
   one known working neighboring implementation. Prefer repairing an existing
   working path over creating another abstraction or parallel implementation.
4. Identify one causal explanation that accounts for the observed failure.
   Distinguish the source from the visible symptom. If the cause is already
   unambiguous from the error and code, proceed immediately.
5. Make the smallest coherent change at that source. Delete bad, duplicated,
   misleading, or superseded code when removal is the clean root repair. Do not
   add wrappers, compatibility layers, fallback paths, instrumentation, or
   architecture unless the observed cause requires them.
6. Run only the task's direct reproduction or done check. Do not create a test
   suite, browser-testing round, review pass, or debugging report unless the
   user requested it or the check cannot otherwise establish the result.
7. If the check succeeds, commit and synchronize the coherent change, report
   the result, and stop. Do not continue into cleanup or general improvement.

## When the first repair fails

- Treat the new output as information, not as permission to give up or stack
  guesses. Remove or revise the failed change when it is not useful.
- Form one new causal explanation and make one new bounded repair while the
  work remains the same minimal package.
- If the next action requires a materially different design, another subsystem,
  or broader authority, return the exact observed difference to the owning
  suborchestrator or Operations Lead. They launch a fresh Sol-medium worker for
  the harder package while unrelated work continues.
- Do not declare an architectural problem merely because attempts failed. Raise
  architecture only when concrete coupling or incompatible requirements show
  that no local root repair can produce the requested state.
- An external dependency is waiting only when a named outside event is truly
  required. Record that event and continue independent goal-moving work.

## Output

Return only:

- the root cause in ordinary technical language;
- the change made;
- the observed done-check result;
- the commit or output, and any genuinely remaining action.

Do not produce phases, investigation diaries, speculative issue lists, or
recommendations unrelated to the requested result.
