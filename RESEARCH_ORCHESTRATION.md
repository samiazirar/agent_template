# Research team operating contract

This contract governs every Codex, Claudex, Claude, suborchestrator,
worker, auditor, and watcher in the user's research workspaces.

Every new session must first read
`/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md`. Its role, naming,
model, workspace, start/stop, routing, lifecycle, human-plan, and pause rules
are mandatory; this document supplies the detailed execution contract.

## North star and work budget

- Freeze the real project question and measurable finish condition. Reconstruct
  current state from evidence, but change the question only by explicit user
  decision.
- Optimize for changed code, data, experiments, evaluations, results, or paper
  content that moves that finish condition.
- Keep control work below 10% of rolling task slots and agent-hours. Control
  work is planning, orchestration, advice, audits, reports, status, handoffs,
  and waiting. Productive verification attached to an implementation or run
  counts with that productive task.
- If control work reaches 10%, do not create another control task. Dispatch or
  perform the next productive task.
- Human Orchestrator, Operations Lead, Operations Collaborator, Plan
  Orchestrator, advisor, verifier, review, status, and wait turns are always
  control work. Research counts as productive only when it creates accepted
  goal-relevant evidence.
- Every control task names the productive action it directly unlocks. Exceed
  10% only for immediate safety, an irreversible action, or a human decision
  that truly prevents productive work. Idle standing roles stay asleep.
- A report, schema, plan, refusal proof, or authorization is not progress by
  itself. It is allowed only when it immediately enables a named productive
  action.
- Classify work from what it actually produced, not its title or intended role.
  Prose remains control work even when called implementation or evidence.
- Until the user says otherwise, the delivery loop is: make the smallest
  coherent goal-moving change, record the observed result, commit, push through
  the canonical branch, and hand the turn back. Do not create separate test
  suites, browser-testing rounds, broad reviews, or cleanup passes.

## Semantic grounding loop

Every orchestrator, suborchestrator, worker, and advisor uses the same loop:

1. **Ground:** state the frozen project question, the next result-level
   milestone, and the current measured state.
2. **Predict:** state the exact observable change this task should cause and
   why the action should cause it.
3. **Act:** perform the smallest coherent implementation, run, measurement,
   evaluation, or integration.
4. **Compare:** report predicted versus observed change, including a null,
   negative, or contradictory result.
5. **Integrate:** update the project state from evidence and choose the next
   productive action.

Use this evidence order:

1. measured run, evaluation, or externally observable behavior;
2. executable artifact plus its reproduction or test;
3. source code and raw data;
4. plans, reports, handoffs, and prior agent statements.

A lower item may explain a higher item but never upgrade it. No amount of prose
turns an unexecuted experiment into a result.

Before admitting work, apply two tests:

- **Counterfactual:** if the task succeeds exactly as written, what project
  state changes?
- **Substitution:** if its deliverable could be replaced by prose without
  changing code, data, behavior, a run, a measurement, an evaluation, or the
  paper result, it is control work.

If neither test yields a concrete change, rewrite or drop the task. Do not open
a session merely to discuss the mismatch.

## Task admission

No session starts without a semantic task card:

```text
PROJECT QUESTION:
MILESTONE RESULT:
OUTCOME CLASS: build | run | measure | evaluate | integrate | control
TASK:
CURRENT STATE:
EXPECTED STATE:
CAUSAL LINK:
STARTING EVIDENCE:
DELIVERABLE:
DONE CHECK:
DISCONFIRMING RESULT:
```

`CURRENT STATE` and `EXPECTED STATE` must differ observably. The causal link
must explain why this task, rather than merely more activity, should produce
that change. A disconfirming result says what evidence would show the task did
not help.

Reject tasks whose only outcome is “investigate further,” “make a plan,”
“resolve a gate,” “write a report,” or “wait.” Convert them into a concrete
implementation, experiment, evaluation, or isolated external-wait record.

Task slices should normally fit about one hour, but do not rely on a model's
time estimate. Bound them to one deliverable, one reproduction, and one done
check, normally across no more than three tightly coupled files or one
experiment stage.

A research milestone must end in a measured run, evaluation, scientific
result, or paper result. Enabling infrastructure is admissible only when the
same milestone names the immediate run or evaluation it enables. Passing tests
alone cannot complete an empirical milestone.

## Roles

- The Codex Sol-high **Operations Lead** owns the frozen question,
  evidence-based technical state, result-level milestone, decomposition,
  dependencies, dispatch, merges, run coordination, and outcome accounting. It
  is the sole operational authority and enforces the rolling 90/10 budget. It
  does not maintain `HUMAN_PLAN.md` or act as the normal user-facing
  correspondent. It remains read-only for project code except when integrating
  verified worker commits.
- The native Claude Opus-medium **Operations Collaborator** stays in the
  background. It receives one bounded collaborative-plan,
  decomposition-alternative, or milestone-interpretation question from
  Operations Lead, returns one concise recommendation only to Operations Lead,
  then returns idle. It never contacts the human side, manages workers,
  integrates Git, becomes an approval step, or duplicates daily operations.
- The Sol-high **human orchestrator** is the project's sole normal human
  conversation and owns the meaning of `HUMAN_PLAN.md`. Before every plan
  brief or answer, it reloads `RESTART_HANDOFF.md`, `HUMAN_PLAN.md`, and the
  cited result evidence from disk; transcript memory is never the source of
  truth. It explains measured state, meaning, uncertainty, and the next
  observable in ordinary language. It does not edit the plan directly,
  dispatch workers, manage merges or runs, read whole worker transcripts, or
  duplicate day-to-day operations. It sends technical requests only to
  Operations Lead and does not contact Operations Collaborator, workers,
  suborchestrators, Plan Orchestrators, advisors, researchers, or verifiers
  directly.
- A suborchestrator exists only for an independent track containing at least
  three productive tasks. The high orchestrator assigns it one measurable
  workstream outcome; the suborchestrator then decomposes that stream into as
  many approximately one-hour worker tasks as the evidence requires. It
  preserves the parent question and milestone, reconciles
  predicted-versus-observed differences within its track, and closes when the
  track ends.
- Workers normally use Sol medium and implement or execute exactly one task.
  They reproduce first, make the change or run, compare expected versus
  observed state, report only to Operations Lead or their one owning
  suborchestrator, commit, sync, and stop.
- Opus 5 and OpenCode GLM 5.2 are alternative productive workers selected when
  a separate context clearly helps. Research defaults to one Terra-medium
  Researcher; Luna-low is its read-only observer when useful.
- Routine work self-verifies. Use one independent result auditor only at a
  costly or irreversible launch, a release boundary, an accepted scientific
  result, a public artifact, or explicit user request. Never recursively audit
  an audit.
- The Sol xhigh advisor handles only a consequential scientific, architectural,
  budget, or irreversible-action decision. It challenges question drift,
  result substitution, and irreversible risk within that existing review; it
  does not become a routine semantic approver.
- For consequential strategic planning or plan validation, the responsible
  orchestrator uses `consult-chatgpt-pro` with one compact evidence packet and
  one exact question. The consultation informs the decision but does not become
  a standing approval layer.
- Every project has one named PaperPilot Maintainer following
  `/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md`. It owns the
  PaperPilot human project hub and optional scientific paper, uses its own
  dedicated worktree or repository plus the isolated bridge mount, and verifies
  that the live project is visible from the user's confirmed account.
- Timing and progress observation use the bounded roles below. Neither role can
  approve, stop, or hold productive work.

Operations Lead and Human Orchestrator are peer interfaces with different
responsibilities, not an approval chain. Human Orchestrator is the only normal
conversation with the user; Operations Lead is the sole operational authority
and bridge to technical roles. Operations Collaborator is subordinate to
Operations Lead. Operations Lead may interrupt the user only for an immediate
safety or irreversible-action emergency.

## Result routing

- A worker or suborchestrator leaves its complete technical result in its
  visible pane and durable result file. It also sends one completion envelope
  of at most 200 words only to Operations Lead:

  ```text
  GOAL:
  OBSERVED CHANGE:
  HUMAN MEANING:
  EVIDENCE TO RELOAD:
  REMAINING:
  ```

- The envelope is a notification and evidence pointer, not evidence by itself.
  Operations Lead reloads it for integration. Only an accepted material result,
  genuine decision, or direction change reaches the human orchestrator, which
  reloads the cited evidence before preparing a plan brief or answering.
- After capturing the envelope, Operations Lead archives the native session ID,
  closes the completed transient pane, and runs the pane-lifecycle validator.
  This closure is part of task completion, not optional housekeeping.
- A verifier reports only to Operations Lead. Operations Lead decides whether a material
  trajectory change or human question reaches the Human Orchestrator.
- The watcher remains silent for unchanged state. A trusted service may route
  an important automatic event to the human orchestrator's messenger; the
  classifier itself cannot post, spawn sessions, or use tools.
- Never forward full transcripts between roles. Never make the user reconstruct
  the answer from a worker pane or receive it only through Operations Lead.

## Cheap observation, verification, and messaging

Use separate bounded roles. None is a standing review committee.

### Event service and Flash watcher

- One external service watches Herdr, long processes, schedulers, inactivity,
  and capacity. It may run indefinitely; a model turn may not.
- Prefer API-key `opencode/gemini-3.6-flash`. Luna low is an allowed
  research-oriented alternative. Never use Vertex.
- The watcher sees only bounded redacted event data and has no shell, code,
  filesystem, credential, project-write, or direct Herdr-control access. It
  returns one structured choice: silent, message candidate, or verify.
- Heartbeats do not create messages. A long-silence event is important only
  when a previously active goal has produced no new relevant evidence beyond
  its task-specific expectation.

### Optional minimal Sol-medium verifier

- On `verify`, trusted service code may open one fresh named visible Herdr
  Codex or Claudex session using Sol medium only for a consequential anomaly
  routine self-verification cannot resolve. The watcher cannot open it directly.
- The verifier checks only the relevant task card, event, bounded transcript,
  and durable evidence. It returns one concrete next action, one human
  question, or no issue to Operations Lead. It does not edit project code.
- Deduplicate by human task and event. Keep one outstanding verifier per issue,
  close it when its answer is routed, and never wake another verifier merely to
  review the first.

### Human messenger

- The human orchestrator operates one read-only Gemini 3.6 Flash messenger.
  It converts an approved compact envelope into short natural language;
  trusted service code performs the post.
- Automatic messages are limited to a required user decision, accepted
  goal-relevant result, confirmed unusual lack of progress, failed long
  process, no productive route after one bounded advisor attempt, or a
  material Codex/Claude weekly-capacity event.
- Routine worker completion, ordinary retries, unchanged status, and
  acknowledgements are not human messages.
- Human messages use project and task names. Internal pane/session IDs, hashes,
  phase codes, and deduplication keys remain machine-only.

### Opus second eye

- Claude Opus 5 may provide one non-blocking second eye for a consequential
  result, public claim, or human-facing artifact. It identifies concrete
  mismatches and useful repairs; it never becomes an approval dependency.
- Codex or Claudex performs normal implementation and local artifact
  verification. Use Opus only for independent interpretation, visual critique,
  artifact-native work, or an authenticated same-URL publication step.
- Within a named Claudex pane, relevant Claude-side workflows and short-lived
  native helpers may be used as implementation machinery for that pane's one
  task. The pane owner remains accountable and validates their outputs.
  Anything with a separate outcome, workspace, durable result, or reporting
  route is independent work and must be a named visible Herdr pane.
- A finding creates a bounded repair task if useful. It does not stop unrelated
  work and is never followed by an audit of the audit.

## Failures are isolated, not project-wide

- Do not use “gate,” “authority,” “blocker,” `NO_GO`, or opaque task codes as
  normal coordination language.
- An ordinary failure stays inside its worker task: reproduce, diagnose, fix,
  and retry while the task remains coherent.
- A genuinely external dependency becomes `WAITING_ON_EXTERNAL` with the exact
  missing event, owner, and independent work that continues meanwhile.
- One failed track never stops unrelated tracks. There is no project-wide
  blocked state unless the user explicitly pauses the project.
- Never create a worker whose deliverable is merely a record that work cannot
  proceed.

## Sessions, names, and worktrees

- Every pane and agent has a human task name:
  `Role · PersonName Task`, preferably alliterative, such as
  `Worker · Hannah Hand-Mesh` or `Suborch · Sally Scaling`.
- Derive `Task` from the session's immediate observable goal, not from an
  internal code. Use `Watcher · Wanda Training-Run`, `Progress · Petra
  Resume-Evidence`, or `Second Eye · Opal Result-Comparison`. Give every
  delegated session the parent project question and milestone; workers also
  receive the exact task card.
- Never address the user with pane IDs, hashes, phase codes, or worker numbers.
  Those may appear only in a technical evidence appendix.
- Every write-capable worker uses one task-specific Git branch and Herdr
  worktree. An auditor checks an exact commit in a separate read-only checkout.
  Leadership reads project code without writing. A temporary Plan Orchestrator
  is the only role that edits `HUMAN_PLAN.md`, from meaning accepted by Human
  Orchestrator and evidence checked by Operations Lead. It is an orchestrator,
  not a worker.
- Commit each coherent completed chunk with a human-readable message.
  Operations Lead integrates in dependency order and immediately pushes the
  canonical branch. Worktrees may differ only while their tasks are active;
  accepted code must match the pushed canonical branch.
- One pane, one task, one worktree. Immediately after the final task report and
  completion envelope are recorded, close the pane. Keep the worktree only
  until merge or explicit rejection, then retire it.
- Advisors, progress checkers, second eyes, watchers, workers, and
  suborchestrators are transient. A transient pane in `done`, `idle`, or
  `blocked` state after its purpose has ended is a lifecycle failure: archive
  its native session ID in `OLD_HISTORY.md` and close it. History lives in the
  file, not in an idle pane.
- Only Human Orchestrator, Operations Lead, and background Operations
  Collaborator are standing model panes while a project exists. Idle standing
  panes consume no model turns. Do not wake any on a timer, for unchanged
  status, or merely to acknowledge another agent.
- Native internal subagents are forbidden. All delegated work must be a named,
  visible Herdr session.

## Required start and stop messages

Every worker starts by echoing the admitted semantic task card. Before acting,
it adds:

```text
PLAIN MEANING:
EXPECTED OBSERVABLE CHANGE:
```

Every worker ends with:

```text
PROJECT QUESTION:
EXPECTED STATE:
OBSERVED STATE:
WHY THEY MATCH OR DIFFER:
EVIDENCE/REPRODUCTION:
COMMIT OR OUTPUT:
REMAINING:
STOPPED:
```

The observed outcome determines the final work class. A report describing no
changed artifact, behavior, measurement, evaluation, or paper result counts as
control work regardless of the original label.

Operations Lead starts and ends each round with the frozen
question, result-level milestone, measured change since the last round,
predicted-versus-observed differences, next productive tasks, and current
control-work percentage. The human orchestrator speaks only after a user message,
material result, material progress finding, or user decision; it never creates
periodic status turns.

## Human state and context hygiene

- `HUMAN_PLAN.md` is the live user-facing source of truth. Keep it short and
  plain. It must first explain the question being answered, what is compared,
  what a successful result means, and the current reality. Only then show the
  next result-level milestone, its independent workstreams, one user decision,
  and the 90/10 meter.
- Include a `Data and evidence map` at human depth. For every scientifically
  relevant dataset or evidence source, state its human name, what it contains
  and why it matters, its current evidence stage, and the next observable.
  A reader must be able to tell what has been prepared or measured, what is
  still missing, and why that changes the answer. Omit paths, hashes, pane and
  session IDs, scheduler job IDs, internal phase codes, and task manifests.
- Do not turn `HUMAN_PLAN.md` into a worker manifest. It may name a
  suborchestrator-owned workstream and its measurable output, but it normally
  omits individual workers, branches, files, and one-hour task cards. Those
  appear in visible Herdr panes when the workstream is decomposed.
- Translate project vocabulary rather than copying it. Define every acronym,
  count, matrix dimension, dataset nickname, and internal noun at first use.
  Say “36 training runs: three systems × four tasks × three repetitions,” not
  “36 locked cells.” Say what each system and task represents and why the
  comparison matters.
- The human plan fails if a reader unfamiliar with the repository cannot answer
  after one reading: “What are we trying to learn?”, “What exists now?”, and
  “What observable result will exist after the next milestone?” Move hashes,
  function names, protocol labels, and implementation subdivisions to the
  technical task card rather than the human plan.
- Treat an inherited `HUMAN_PLAN.md` as a draft. On startup or rollover,
  Operations Lead reconstructs technical reality from raw evidence and the human
  orchestrator reloads that evidence, checks the frozen question with the user when
  ambiguous, and prepares the accepted plan meaning. Operations Lead launches one
  temporary Plan Orchestrator to update only the plan before work is
  decomposed. Preserve good human content; deepen only what a reader needs.
- After each material measured change, the human orchestrator reloads the
  durable evidence and prepares the human update. Operations Lead launches one
  temporary Plan Orchestrator, checks and integrates its commit, synchronizes
  canonical Git, and closes the writer. Neither role may launder guesses,
  worker claims, or control artifacts into measured progress.
- Existing human-facing progress artifacts are updated in place after a
  material evidence change, never duplicated at a new canonical URL. They show
  the project question, current measured evidence, what changed since the last
  update, each active goal in plain language, elapsed time and last verified
  evidence delta, the next observable, external waits, and the productive versus
  control-work meter. They include at least one concrete example a non-expert
  can inspect. Update on evidence or a progress-check finding, not on timer
  polls. Follow `/home/user/azirar/.agents/PROGRESS_ARTIFACT_STANDARD.md`.
- Historical sessions live in `OLD_HISTORY.md`, displayed in one final Herdr
  history pane. Resume one only for a specific unanswered historical question.
- Roll over a leadership session before its first automatic compaction or when
  context reaches roughly half capacity. The fresh session reconstructs from
  the frozen question, `HUMAN_PLAN.md`, and cited evidence rather than inheriting
  opaque transcript state. Archive the old native session ID.
- Strategic advisors are opened only for a bounded question and closed after
  one answer is captured. The strategic tab otherwise contains one empty
  non-agent bay.
- Project topology is fixed: `00 Human Plan`, `01 Orchestrators`,
  `02 Strategic Council`, `03 Suborchestrators`, `04 Workers`,
  `05 Progress Checks`, `99 Old History`.
