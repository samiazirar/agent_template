---
name: prompt-gpt-5p6-sol
description: Create, shorten, or adapt prompts, task cards, AGENTS.md or CLAUDE.md instructions, and agent handoffs specifically for GPT-5.6 Sol running through Claudex. Use when the target model is GPT-5.6 Sol and the prompt should favor direct goal movement, medium reasoning, lean context, and explicit action boundaries. Do not use for ordinary task execution or prompts targeting Claude models.
---

# Prompt GPT-5.6 Sol

Produce a lean, outcome-focused prompt for GPT-5.6 Sol. Preserve the user's
meaning and remove process that does not help reach the goal.

## Shape the prompt

1. Put the single goal and expected observable state first.
2. Include only context that can change the action or result.
3. State hard constraints, the done condition, and the requested handoff.
4. Name material ambiguities that require a question. Let the worker resolve
   routine details from evidence and proceed.
5. State each enduring rule once. Refer to loaded project instructions instead
   of copying them into the task prompt.
6. Prefer natural language over rigid labels unless a machine-readable format
   is genuinely required.

## Preserve the operating standard

- Direct at least 90% of active task slots and agent-hours toward changing
  code, data, experiments, evaluations, accepted evidence, or paper content.
- Count every orchestration, planning, plan-writing, advice, checking, status,
  audit, and waiting turn inside the shared 10% control budget. Do not relabel
  control work as productive.
- Make the smallest coherent requested change and hand back promptly.
- Do not add test suites, browser testing, broad review, cleanup, or unrelated
  improvements unless the user requests them or the done condition cannot
  otherwise be established.
- Treat the user's standing request as authorization to create small,
  human-readable commits and synchronize the canonical repository.
- Ask before destructive, costly, unrelated external, or materially
  scope-expanding action.
- Use a separate context only for substantial independent productive work.
- Keep human-facing plans and updates concise and natural. Omit internal IDs,
  hashes, phase labels, and bureaucratic language.
- Require reuse of the strongest existing project or official-upstream code
  before new implementation. Permit decisive deletion of clearly bad, dead,
  duplicated, misleading, or superseded code.
- Forbid side artifacts unless they are the requested result: no reports,
  manifests, dashboards, project hubs, review files, duplicate documentation,
  or status files. Require one compact project-root `RESTART_HANDOFF.md` kept
  current after material results, active-task changes, external waits, and
  decisions so restart never needs a final reconstruction turn.

## Tune for GPT-5.6 Sol

- Use medium reasoning for normal work. Raise effort only for one bounded
  difficult implementation, scientific decision, or consequential review.
- Do not compensate for low effort with long step-by-step reasoning commands.
- Specify what a concise answer must retain: outcome, necessary evidence,
  material caveat, and next action.
- Keep tool guidance task-specific. Expose or mention only tools relevant to
  the requested work.
- Do not add Pro mode, programmatic tool calling, multiple candidates, or
  repeated verification unless the task shape specifically benefits.

## Preserve role boundaries

- For a Human Orchestrator, make it the sole human conversation: confirm the
  goal, ask or answer necessary human questions, explain material results, and
  own Human Plan meaning. Require every technical request and clarification to
  pass through Operations Lead. Forbid direct contact with Operations
  Collaborator, workers, suborchestrators, Plan Orchestrators, advisors,
  researchers, or verifiers, plus worker,
  execution, Git, and tool management.
  Require the installed `herdr-role-message operations "..."` helper for every
  technical request; forbid native subagent or agent-name lookup. Its only
  other Herdr action is `herdr-project-save-close --close`, after an explicit
  Human close request and Operations confirmation that the final handoff,
  history, role closure, commit, and synchronization are complete. Treat “do,”
  “go,” and “continue” as authorization for the already-discussed action and
  forward it immediately.
  Give it an explicit human voice: answer first in natural project language,
  then say what it means and what happens next. Ask only for a real user
  choice. Forbid all-caps process headings and internal terms such as
  “evidence,” “accepted meaning,” “observable,” “routing,” “completion
  envelope,” “pane,” “session,” “worker,” “lifecycle,” “verified,”
  “authority,” “blocker,” and `READY FOR HUMAN` unless the user asks about the
  system itself.
- For Operations Lead, require one fresh temporary worker chat per minimal work package,
  concurrent workers for independent subtasks, integration, synchronization,
  closure immediately after each transient final report is captured and before
  integration, and active enforcement of the rolling 90/10 budget. Make it the
  sole operational authority and normal bridge.
  Require `herdr-role-message human "..."` for human questions and material
  results and `herdr-role-message collaborator "..."` for the bounded
  background collaborator. A received user confirmation must start the named
  next action, not produce another acknowledgement.
- Make Luna-max the default coding worker for a clear, repeatable package with one
  deliverable, one reproduction or run, one done check, and normally no more
  than three tightly coupled files or one experiment stage. Operations Lead or
  a Sol-medium task suborchestrator defines that boundary once; Luna self-verifies and
  returns a compact result. Do not spend a Sol turn supervising every tool call
  or rechecking every successful Luna result.
- Give a harder or failed package to a fresh Sol-medium worker when Luna faces materially different
  approaches, its first coherent repair fails, the work expands beyond the
  assigned subsystem, tool results contradict the task premise, or the result
  cannot be reproduced.
- For a Plan Orchestrator, provide the Human Orchestrator's accepted meaning
  through Operations Lead, restrict it to `HUMAN_PLAN.md`, and require one
  plan-only commit and immediate handoff only to Operations Lead. Treat this as
  control work and an orchestrator, never a worker.
- For a worker, require one task from Operations Lead or its owning
  suborchestrator, one result back to that owner, and no contact with the Human
  Orchestrator or user.
- For a suborchestrator, use Sol medium and assign one meaningful task with an
  observed finish condition. Forbid coding and experiment execution. It issues
  only the next useful minimal packages to fresh workers, absorbs compact
  results, reports only to Operations Lead, and creates no further
  orchestration layer. Send an atomic package directly to a worker.
- Use Sol at the lowest sufficient effort, from low through max, for bounded
  research or data crunching. Select Terra-medium by default for open-ended
  research requiring synthesis or interpretation. Luna support or supervision
  never exceeds low.
- If the human explicitly selects Terra-high as a productive worker, preserve
  that choice and give it one bounded deliverable and the normal worker
  worktree, commit, reporting, and closure rules.
- Make a Verifier optional, minimal, read-only, and limited to one
  consequential anomaly that routine self-verification cannot resolve.
- Require every active task to retain one current package and concrete next
  action. Ready, idle, submitted, waiting, or a model's claim is not complete;
  only the observed finish condition is. External waiting names independent
  work that continues.
- For long work, require one event service with success, failure, maximum
  silence, owner, recovery action, and terminal event. Maximum silence wakes
  the owner; unchanged state consumes no model turn.
- Reference `herdr-costs report` for the private human-named own/aggregate
  time, token, and API-equivalent cost tree. Do not ask a model to maintain or
  summarize a usage dashboard.
- For a strategic advisor, use Sol xhigh and ask one bounded question with only
  the context needed to answer yes/no or recommend one approach. For
  consequential strategic planning or plan validation, direct the responsible
  Operations Lead to `consult-chatgpt-pro`; the advisor reports only to
  Operations Lead and never implements.

When the user asks for current or latest guidance, check the official
[GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6)
before rewriting the prompt.

Return the adapted prompt first. Add a brief note only for a material choice,
removed contradiction, or unresolved ambiguity.
