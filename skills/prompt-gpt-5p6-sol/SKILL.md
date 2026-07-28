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

- Direct at least 90% of effort toward changing the goal-relevant state.
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
  pass through Operations. Forbid direct contact with workers,
  suborchestrators, plan writers, advisors, or verifiers, plus worker,
  execution, Git, and tool management.
- For Operations, require one temporary worker per concrete subtask, concurrent
  workers for independent subtasks, integration and synchronization, and
  closure after every accepted or rejected result. Make Operations the sole
  normal bridge between the Human Orchestrator and every technical role.
- For a Human Plan Writer, provide the Human Orchestrator's accepted meaning,
  restrict the worker to `HUMAN_PLAN.md`, and require one commit and immediate
  handoff only to Operations.
- For a worker, require one task from Operations or its owning
  suborchestrator, one result back to that owner, and no contact with the Human
  Orchestrator or user.
- For a suborchestrator, assign one independent multi-step workstream, one
  worker per subtask, reporting only to Operations, and no further
  orchestration layer.
- For a strategic advisor, use Sol xhigh and ask one bounded question with only
  the context needed to answer yes/no or recommend one approach. For
  consequential strategic planning or plan validation, direct the responsible
  orchestrator to `consult-chatgpt-pro`; the advisor reports only to Operations
  and never implements.

When the user asks for current or latest guidance, check the official
[GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6)
before rewriting the prompt.

Return the adapted prompt first. Add a brief note only for a material choice,
removed contradiction, or unresolved ambiguity.
