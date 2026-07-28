---
name: restart-research-team
description: Restore paused Herdr research projects from RESTART_HANDOFF.md files, onboard one Human Orchestrator, a Codex Sol-high Operations Lead, and a background Claude Opus-medium Operations Collaborator, reconstruct the standard human-plan/orchestrators/strategic/suborchestrator/worker/progress/history layout under the 90/10 budget, and wait for user plan discussion without resuming research.
---

# Restart Research Team

Restore context and a productive team structure only. Do not resume research,
coding, experiments, scheduler activity, publication, or monitoring.

## Read first

1. Confirm `HERDR_ENV=1` and read the Herdr skill.
2. Read `/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md`,
   `/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md`, and
   `/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md`.
3. Read the master restart index and every selected project handoff. Require
   `CAN RESTART`.
4. Read each project's `HUMAN_PLAN.md`, `OLD_HISTORY.md`, `AGENTS.md`, and
   `CLAUDE.md`. Treat `HUMAN_PLAN.md` as an inherited draft, not evidence.
5. Verify current repositories and scheduler snapshots read-only. Treat every
   old Herdr ID as historical.

## Explain before rebuilding

Tell the user in plain language:

- the measurable project goal;
- what real evidence exists;
- what result does not yet exist;
- how much recent work was productive versus control work;
- the proposed first productive milestone;
- the one decision the fresh team should discuss with the user.

Never present pane IDs, hashes, internal phase codes, “gate,” “authority,” or
“blocker” terminology as the human explanation.

Do not declare the inherited plan correct. Fresh Operations Lead reconstructs
the technical state. The fresh Human Orchestrator reloads the handoff, plan,
and cited raw evidence, then preserves good human content and deepens only what
is missing. Operations Collaborator remains idle unless Operations Lead asks
one bounded planning question.

## Fixed workspace layout

For every selected project, create these tabs in this physical order:

1. `00 Human Plan`
2. `01 Orchestrators`
3. `02 Strategic Council`
4. `03 Suborchestrators`
5. `04 Workers`
6. `05 Progress Checks`
7. `99 Old History`

Create the first tab as an empty named shell until the human orchestrator has
updated and validated `HUMAN_PLAN.md`, then launch
`frogmouth HUMAN_PLAN.md`. Use `frogmouth OLD_HISTORY.md` in the final tab.
The history tab contains exactly one non-agent pane; native historical session
IDs remain dormant in the file.

Create:

- one fresh Claudex GPT-5.6 Sol-high Human Orchestrator, one fresh Codex
  GPT-5.6 Sol-high Operations Lead, and one native Claude Opus-medium
  Operations Collaborator in `01 Orchestrators`;
- one empty named shell bay in `02 Strategic Council`;
- empty named shell bays in `03 Suborchestrators`, `04 Workers`, and
  `05 Progress Checks`.

Strategic advisors are transient. Open Sol xhigh only for one bounded question
after the human plan is ready, capture the answer, archive the native session
ID, and close the pane. Prefer a yes/no verdict or one concrete recommendation.
Use `consult-chatgpt-pro` for consequential strategic planning or plan
validation. Operations Lead is the sole day-to-day coordinator. Operations
Collaborator stays in the background, reports only to Operations Lead, and has
no worker, Git, integration, or approval authority. The Human
Orchestrator is the sole normal human conversation and owns the meaning of
`HUMAN_PLAN.md`; it exchanges technical requests and human decisions only with
Operations Lead. A temporary Plan Orchestrator receives its brief from and
reports only to Operations Lead; it is an orchestrator, not a worker.

All restoration, collaborative planning, plan writing, advice, verification,
status, and waiting count inside the shared 10% control budget. At 10%,
Operations Lead opens no further control role unless safety, irreversibility,
or a required human decision prevents productive work.

Give every agent a human task name in the form
`Role · PersonName Task`. Do not expose raw pane IDs as names. Record all
superseded native session IDs in `OLD_HISTORY.md`, then close their live panes.
Every brief must include the required opening fields from the onboarding
contract and the canonical role block rendered by
`/home/user/azirar/agent_template/skills/launch-herdr-agent/scripts/validate_role_card.py`.
Validate the composed prompt before sending it. No worker or PaperPilot
maintenance session starts before the user has discussed the human plan.

## Initial briefs

Operations Lead reads the operating contract, inherited plan, restart handoff, and
only the raw evidence needed to verify current reality. Ask it to:

1. preserve the user-approved question; surface ambiguity instead of silently
   reinterpreting it;
2. reconstruct current state using the evidence hierarchy in the operating
   contract;
3. make the first milestone end in an observable project result rather than
   enabling infrastructure;
4. assign any workstream containing at least three productive tasks to one
   named suborchestrator, which later decomposes it into approximately one-hour
   semantic worker cards;
5. keep at least 90% of task slots and agent-hours directly productive and
   classify every control-role turn honestly;
6. default research to Terra-medium and keep verification optional and
   minimal;
7. emit a compact current-state envelope for the human orchestrator;
8. emit `OPERATIONS_READY` and wait without executing.

Operations Collaborator reads only the operating contract, restart handoff, and
Operations Lead's bounded question. Ask it to acknowledge that it is native
Claude Opus 5 medium, reports only to Operations Lead, has no worker, Git,
integration, human-contact, or approval authority, and otherwise remains idle.

The Human Orchestrator reads the operating contract, `RESTART_HANDOFF.md`,
`HUMAN_PLAN.md`, the operations envelope, and each cited evidence item itself.
Ask it to:

1. preserve good existing human content and avoid a broad rewrite;
2. define every acronym, count, dataset nickname, and project noun at first use;
3. add or deepen a `Data and evidence map` that states, for every relevant
   dataset or evidence source, what it contains, why it matters, its present
   evidence stage, and the next observable;
4. omit paths, hashes, pane/session/job IDs, phase codes, and worker manifests;
5. make the current reality, missing result, next observable, and one user
   decision understandable after one reading;
6. reload the handoff, plan, and cited evidence before every future plan update
   or user answer rather than relying on transcript memory;
7. emit one accepted human-plan brief for a temporary writer, then
   `HUMAN_HANDOFF_READY`;
8. remain the only human conversation while never dispatching workers,
   integrating Git, managing execution, or contacting technical roles other
   than Operations Lead.

Reject the plan unless a reader unfamiliar with the repository can state what
the project is testing, what exists now, what would disconfirm the direction,
and what observable result comes next. “36 locked cells” is invalid until
translated into the systems, tasks, repetitions, and scientific purpose.

After both readiness messages, Operations Lead launches one temporary
`Plan Orchestrator · PersonName Restore Plan` in `01 Orchestrators` with an
isolated worktree. It receives accepted meaning and checked evidence from
Operations Lead, edits only `HUMAN_PLAN.md`, commits, and reports only to
Operations Lead. Operations Lead asks Human Orchestrator to check meaning,
integrates and synchronizes, closes Plan Orchestrator, then launches or
refreshes Frogmouth. Do not open a strategic session merely to confirm
restoration.

The xhigh advisor receives only one exact question and the minimum decision
context. It checks only whether the frozen question was preserved, evidence
supports the current state, the milestone is a real result rather than a proxy,
or one proposed action should be taken. It must not inspect broadly, implement,
manage workers, contact the Human Orchestrator or user, invent process, or
become a routine approver. It reports only to Operations Lead.

After either strategic answer is durably captured, close that pane immediately.

## After user approval

- Use as many concurrent productive worker sessions as independent subtasks
  justify.
- One worker owns exactly one admitted subtask, one task branch, and one Git
  worktree. Never combine unrelated subtasks in one worker.
- Every new role reads the mandatory onboarding contract before its task card.
- Put workers and subworkers in `04 Workers`; put only multi-task track owners
  in `03 Suborchestrators`.
- Put optional minimal verifiers and Luna observers in `05 Progress Checks`.
  A Terra Researcher is the default research role. Derive every pane name from
  the immediate goal.
- Operations Lead decomposes the milestone into independent workstreams. A named
  suborchestrator owns only a substantial independent multi-step stream with at
  least three productive subtasks. It launches one temporary worker per
  subtask, integrates its stream for Operations Lead, and closes when the stream
  ends. It may not create another suborchestrator.
- Claudex may use relevant native workflows and short-lived helpers inside one
  named pane's assigned task and worktree. Independent work with its own task
  card, workspace, durable result, or reporting route must be opened as a named
  visible Herdr pane.
- Every completed worker sends its completion envelope to its owning
  orchestrator. Operations Lead routes only an accepted material result, genuine
  decision, or direction change to the Human Orchestrator. Full technical
  detail remains internal; never forward a transcript to the human interface.
- Before opening a pane, serialize the semantic task card and run:

  ```bash
  python3 /home/user/azirar/.codex/skills/restart-research-team/scripts/validate_task_card.py TASK_CARD_FILE
  ```

- A task starts and ends with the semantic grounding and
  predicted-versus-observed templates in the operating contract.
- If a worker cannot state the observable goal delta, the orchestrator rewrites
  the card without opening another review session.
- Ordinary failures remain in the owning task. Isolate external waits while
  unrelated work continues.
- Use one `gpt-5.6-luna` low-reasoning session for the active project batch. It
  starts one event-driven or at-least-ten-minute blocking watcher and wakes the
  orchestrator only at a real event or roughly 25/50-minute evidence check.
  Never create one polling model per worker.
- Before launching that watcher, validate its exact condition, owner, cadence,
  and model with:

  ```bash
  python3 /home/user/azirar/.codex/skills/restart-research-team/scripts/validate_watcher_card.py WATCHER_CARD_FILE
  ```

- At a due check, the orchestrator may create a fresh read-only
  `gpt-5.6-terra` medium checker. Require a task-specific observable delta,
  validate its short report with:

  ```bash
  python3 /home/user/azirar/.codex/skills/restart-research-team/scripts/validate_progress_check.py REPORT_FILE
  ```

  The checker advises one useful recovery action when evidence has not
  advanced. It cannot stop, approve, edit, or recursively audit.
- Routine work self-verifies. Use one independent audit only at an expensive
  launch, release, public artifact, or accepted-result boundary.
- Claude Opus 5 is an optional non-blocking second eye for consequential
  results and existing human-facing artifacts. Codex or Claudex does normal
  source work and local verification. Reuse the exact existing artifact and
  canonical URL; follow the artifact-update skill before publication.
- Close a worker immediately after its concrete result is integrated or
  rejected. Retire its worktree at the same boundary.
- Close every suborchestrator, advisor, progress checker, second eye, and
  watcher as soon as its bounded purpose and durable result are complete.
  Record its native session ID in `OLD_HISTORY.md`; do not retain an idle
  history pane.
- After every transient completion and at the end of each batch, Operations Lead
  must run:

  ```bash
  python3 /home/user/azirar/.codex/skills/restart-research-team/scripts/validate_pane_lifecycle.py WORKSPACE_ID
  ```

  A failure means closure is still part of the current task; do not open more
  control panes until it is repaired.
- Classify the completed task from its observed output. Prose-only output is
  control work regardless of its original name.
- Operations Lead integrates each completion into technical state. Human
  Orchestrator receives the compact envelope and reloads cited evidence only
  after a material measured change. A temporary Plan Orchestrator performs the
  actual `HUMAN_PLAN.md` update. No standing role wakes merely to acknowledge
  unchanged status.
- After material evidence or a progress-check finding, update any existing
  progress artifact in place using
  `/home/user/azirar/.agents/PROGRESS_ARTIFACT_STANDARD.md`. Do not refresh on
  unchanged timer polls or create a replacement artifact.
- Roll over leadership before automatic compaction.

## Validation

Run:

```bash
python3 /home/user/azirar/.codex/skills/restart-research-team/scripts/validate_live_team.py WORKSPACE_ID PROJECT_DIR
```

Do not declare restoration complete until the validator passes and every agent
other than the two standing orchestrators has been closed, with no research
worker active.
