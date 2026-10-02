---
name: prompt-claude-opus-5
description: Write or shorten prompts, worker briefs, CLAUDE.md/AGENTS.md instructions and handoffs for Claude Opus 5.x in Claude Code. Use when the target is an Opus worker or session; not for ordinary task execution or GPT prompts.
---

# Prompt Claude Opus 5.x

Produce a complete but compact prompt for Claude Opus 5.5 (and 5.x). Preserve the user's
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

- Deliver exactly the requested scope through the smallest coherent change,
  run one direct check of the result, commit with a plain message, and stop.
- Do not add test suites, smoke runs, repeated re-checks, "measure first"
  steps, browser testing, broad review, cleanup, abstractions, files, or
  features unless requested or necessary for the done condition.
- Resolve routine details directly. Ask only when different interpretations
  would cause materially different work or before destructive, costly,
  unrelated external, or scope-expanding action.
- Reuse the strongest existing implementation; delete dead, duplicated or
  superseded code rather than wrapping it.
- For concrete failures, require `goal-directed-repair`: fix the causal source
  with the smallest change and run only the direct done check.
- Create no side artifacts unless they are the deliverable: no plans, reports,
  manifests, dashboards, review files, or status files. Keep an existing
  `RESTART_HANDOFF.md` compact and current at milestones.
- Never wait inside a turn: no sleep or polling loops; use Monitor with an
  until-condition and timeout, a background command, or a watcher that sends
  `herdr-role-message`.

## Tune for Claude Opus 5.x

- Explicitly request focused, brief user-facing responses; effort controls
  thinking volume, not visible response length.
- Ask for one short initial intent, updates only for important findings or a
  changed direction, and a final response that leads with the outcome.
- Remove blanket instructions to double-check, re-verify, run a separate final
  verification, or create a verifier subagent. Opus 5.x verifies its own work and
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

## Worker briefs

- A Herdr tab worker is Opus 5.5 (`claude-acct run -a <seat> -- --model
  claude-opus-5-5`) with its own worktree, one task, one done check, and a brief
  in a file. Read-only surveys go to the `scout` subagent instead.
- Forbid new agents, unrelated work, and scope expansion.
- The worker reports once to its parent with `herdr-role-message` and stops.
  Do not ask it to poll, wait for acknowledgement, or write a usage report.

When the user asks for current or latest guidance, check the official
[Claude Opus 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
before rewriting the prompt.

Return the adapted prompt first. Add a brief note only for a material choice,
removed contradiction, or unresolved ambiguity.
