# Agent system standard

This is the short map for selecting sessions, models, delegation, delivery,
observation, and human communication. The research onboarding and
orchestration contracts provide the detailed rules.

## Goal and delivery

- Begin from one explicit user-approved goal and the next observable state.
- Spend at least 90% of task slots and agent-hours changing code, data,
  experiments, evaluations, accepted results, or intended paper content.
- Planning, status, advice, broad checking, and waiting share the remaining
  10%. Never rename them as productive work.
- Until the user says otherwise: make the smallest coherent goal-moving
  change, do not schedule test suites or browser testing, commit it with a
  human-readable message, push the canonical branch, and hand control back.
- One task owns one branch, worktree, and named Herdr session. Accepted chunks
  are merged in dependency order; after integration, the canonical checkout
  and GitHub represent the same code.

## GPT-5.6 prompting

- Lead with the outcome. Give only the context that can change it, the hard
  constraints, the observable done condition, and the required handoff.
- State enduring rules once in `AGENTS.md` or this standard. A task prompt adds
  only its immediate goal and evidence; it does not repeat inherited contracts.
- Ask only when a material ambiguity or approval boundary prevents safe
  in-scope work. Otherwise proceed directly toward the requested outcome.
- Keep responses natural and compact: conclusion, necessary evidence, material
  caveat, and next action. Omit internal process language and generic filler.
- Do not copy generic advice such as always testing, always planning, or always
  using high reasoning. The user's no-test default and the model-selection
  rules below take precedence.

## Session and model selection

| Work | Session | Model |
| --- | --- | --- |
| Normal implementation or execution | Codex or Claudex | Sol, medium |
| Bounded difficult implementation or decision | Codex or Claudex | Sol, high |
| Independent alternative productive worker | Native Claude | Opus 5 |
| Mechanical or context-heavy alternative worker | OpenCode | GLM 5.2 |
| Deep research or evidence interpretation | Codex or Claudex | Terra |
| Cheap research observation | Codex or Claudex | Luna |
| Permanent event classification | OpenCode API key | Gemini 3.6 Flash |
| Strange-event verification | Visible Codex or Claudex | Sol, medium |
| Human message drafting | OpenCode API key | Gemini 3.6 Flash |

Claudex is the Claude Code interface backed by the local Codex gateway. It is
not native Anthropic Claude. Launch it through `claudex` with an explicit Codex
model. Native Claude is selected separately when Opus 5 is wanted.

Terra and Luna are research, interpretation, and observation models, not the
normal implementation workers. Never use Vertex; Gemini routes use the
OpenCode API-key provider.

## Native Herdr launch

- Launch every independent agent as a named visible Herdr tab with
  `herdr-agent <codex|claude|claudex> "Role · PersonName Goal" [directory]`.
- `codex` and `claudex` use the synchronized GPT-5.6 Sol medium default.
  `claude` selects native Claude Opus 5 at medium effort by default.
- Never replace these sessions with hidden subagents or ordinary background
  subprocesses. Open a separate session only for independent productive work.
- Shared personal skills live once in `~/.agents/skills`. Claude and Claudex
  load the same directories through `~/.claude/skills`; do not maintain
  divergent copies.
- Use `prompt-gpt-5p6-sol` when adapting instructions for Codex or Claudex and
  `prompt-claude-opus-5` when adapting instructions for native Opus 5.

## Human structure

- The operations orchestrator runs decomposition, workers, integration, and
  execution.
- The human orchestrator owns `HUMAN_PLAN.md`, user communication, and the
  messenger.
- `HUMAN_PLAN.md` stays at goal, milestone, measured reality, and workstream
  level. Worker cards remain in their named Herdr sessions.
- Human-facing names and messages use project and task words. Pane IDs,
  session IDs, hashes, phase codes, deduplication keys, and terms such as
  “gate” stay internal.
- Suborchestrators exist only for independent tracks containing at least three
  productive tasks. They may not create another suborchestrator layer.

## Watcher, verifier, messenger, and limits

The long-running system service performs waiting. A model turn never polls
indefinitely.

1. The service receives a Herdr, process, scheduler, silence, or capacity
   event.
2. Tool-free API-key Gemini 3.6 Flash returns silent, message, or verify.
3. Silent events stop immediately.
4. Verify opens one fresh named visible Sol-medium verifier with bounded
   redacted evidence and no project-write access.
5. The verifier returns continue with one direct next action, ask the user, or
   sleep. It then closes.
6. Tool-free Flash drafts an important human message only when the human
   orchestrator approved it or an automatic important-event rule fired.
7. Trusted service code performs Herdr control and posting; Flash cannot.

Automatic important events are limited to a required user decision, accepted
goal-relevant result, confirmed unusual lack of progress, failed long-running
process, no productive route after a bounded advisor attempt, or material
Codex/Claude weekly-capacity change. Routine status and unchanged heartbeats
stay silent.
