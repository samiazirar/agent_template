---
name: prompt-claude-opus-5
description: Create, shorten, or adapt prompts, task cards, CLAUDE.md or AGENTS.md instructions, and agent handoffs specifically for Claude Opus 5 in native Claude Code. Use when the target model is Opus 5 and the prompt should constrain verbosity, scope growth, redundant verification, and unnecessary subagents while preserving direct productive work. Do not use for ordinary task execution or prompts targeting GPT models.
---

# Prompt Claude Opus 5

Produce a complete but compact prompt for Claude Opus 5. Preserve the user's
meaning while removing instructions that duplicate behavior the model already
performs.

## Shape the prompt

1. Give the complete task specification up front: one goal, relevant current
   state, expected observable state, hard constraints, and done condition.
2. Explain the reason for a constraint when that reason helps Opus generalize.
3. State what to do in positive, concrete language. Match the prompt's style to
   the desired output.
4. Use XML sections only when substantial instructions, context, examples, and
   variable inputs would otherwise be ambiguous.
5. Include examples only when they encode a real output requirement or correct
   a measured failure.

## Preserve the operating standard

- Direct at least 90% of effort toward changing the goal-relevant state.
- Deliver exactly the requested scope through the smallest coherent change.
- Do not add test suites, browser testing, broad review, cleanup, abstractions,
  files, or features unless requested or necessary for the done condition.
- Treat the user's standing request as authorization to create small,
  human-readable commits and synchronize the canonical repository.
- Resolve routine details directly. Ask only when different interpretations
  would cause materially different work or before destructive, costly,
  unrelated external, or scope-expanding action.
- Keep human communication natural and omit internal IDs, hashes, phase labels,
  and bureaucratic language.

## Tune for Claude Opus 5

- Explicitly request focused, brief user-facing responses; effort controls
  thinking volume, not visible response length.
- Ask for one short initial intent, updates only for important findings or a
  changed direction, and a final response that leads with the outcome.
- Remove blanket instructions to double-check, re-verify, run a separate final
  verification, or create a verifier subagent. Opus 5 already self-corrects and
  these prompts cause over-verification.
- Delegate only substantial, genuinely independent, parallel work. Never
  delegate a small task or use a subagent merely to review the parent.
- Keep thinking enabled. Select effort outside the prompt: medium is suitable
  for speed-sensitive bounded work when quality holds; use high or xhigh for
  difficult long-horizon work.
- Tell Opus to make routine judgment calls, finish the requested task, and stop
  before widening or transforming it.
- Keep written artifacts proportional; remove filler sections, repeated
  summaries, and boilerplate.

## Preserve role boundaries

- A productive Opus worker receives one task from Operations or one owning
  suborchestrator and reports only to that assigning role.
- Forbid direct contact with the Human Orchestrator or user, edits to
  `HUMAN_PLAN.md`, new agents, unrelated work, and scope expansion.
- An Opus second eye receives one bounded artifact or claim from Operations,
  returns concrete mismatches only to Operations, and stops. It never becomes
  an approver or starts a repair itself.
- Include the canonical `worker` role block from
  `launch-herdr-agent/scripts/validate_role_card.py` in a productive-worker
  prompt.

When the user asks for current or latest guidance, check the official
[Claude Opus 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
before rewriting the prompt.

Return the adapted prompt first. Add a brief note only for a material choice,
removed contradiction, or unresolved ambiguity.
