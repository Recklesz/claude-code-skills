---
name: interactive-plan
description: Interactive global implementation planning via iterative repo research + decision interview. Use when user asks to create/make an implementation plan, scope a feature/refactor/system change, or when requirements are unclear and decisions must be made.
---

# Interactive Global Implementation Planning

## Purpose

Create a high-quality implementation plan by alternating between:
1) **Research** (repo/docs investigation) and
2) **Interviewing** (eliciting decisions that research cannot answer).

Default to a single planning agent, but delegate **substantial research** to dedicated research agents.
When a research pass is broad, cross-cutting, or covers multiple distinct questions, read `references/research-agents.md` and follow it.

## When to use

Use when:
- User asks to "create a plan", "make an implementation plan", "plan this feature/refactor"
- User provides a task/feature description that needs scoping and sequencing
- Work requires decisions/tradeoffs (rollout, schema, UI/UX, migration, performance, risk)

## Inputs and environment

**Required from user (minimum):**
- Feature/task description (or file path(s) to description/spec)

**Optional from user:**
- Constraints (timeline, risk tolerance, backward compatibility, rollout requirements)
- Links to prior work or similar features

**Environment assumptions:**
- You have access to the full repo for research via Read/Grep/Glob/Bash.
- You may create and continuously update a working planning state file under `planned-changes/` during the interactive planning process.
- You may write the final implementation plan only when the user explicitly asks to finalize.

## Hard constraints and guardrails

- **Research-first:** Do an initial repo scan before asking substantive questions.
- **Ask only what you cannot discover:** If the repo can answer it, research instead of asking.
- **Interactive:** Do not draft the entire plan in one pass. Build it through an interview loop.
- **2 questions max per turn** (unless the user asks for more).
- **Verify corrections:** If the user corrects you, validate via repo when possible.
- **No open questions in the final plan:** If uncertainties remain, keep interviewing.
- **Stop condition:** If the user says "stop"/"pause", stop the loop and summarize progress + next decisions.
- **Delegate substantial research:** If the research phase is likely to be more than a quick local scan, use one or more research agents as described in `references/research-agents.md`.
- **Make research artifacts observable:** For every substantial research phase, explicitly state whether research agents were launched, which questions they own, and the exact `thoughts/` findings path each one must produce. Do not proceed to decision cards until each required findings path exists or you have documented why delegation was unavailable and written the findings yourself.
- **Resolve the repo root before writing artifacts:** Use the current project repo root, not the skill repo or a home config directory, for `thoughts/` artifacts and `planned-changes/` planning state.
- **Prioritize the highest-impact decisions first:** Order the interview by decisions that most affect architecture, data model, rollout, risk, user experience, or phase sequencing. Work downward from the most consequential unknowns to smaller implementation details.
- **Do not repeat state every turn:** Keep the evolving mini-plan, decision log, open questions, and research notes in the working planning state file. In chat, show only the current decision context, the trade-offs, any new evidence, and the next question.

## Persistent planning state file (maintain continuously)

Create and update one markdown state file for the planning session under the current project repo root:

- Preferred path: `planned-changes/YYYY-MM-DD-kebab-description.planning-state.md`
- If the repo already uses a different planning scratch convention under `planned-changes/`, follow that local convention.
- Create `planned-changes/` if it does not exist.
- Update this same file after every research pass and after every user decision.
- Treat this as the source of truth for evolving planning state; do not rely on repeated chat output to preserve state.

The planning state file must contain and maintain:

1) **Goal** (1 sentence)
2) **Constraints** (bullets)
3) **Current State Findings** (with file references)
4) **Research Artifacts** (`thoughts/` paths and summaries)
5) **Research Backlog** (what you will investigate next)
6) **Decision Log** (decision → chosen option → rationale → evidence)
7) **Open Questions** (must be empty before finalizing)
8) **Mini-plan** (3–8 bullets, evolving phased outline)

## Workflow

### Step 1 — Intake + initial research pass (always)

Resolve the current project repo root. Create or update the planning state file under `<repo-root>/planned-changes/` before asking the first decision question. Record the state file path in chat once, then update that same file silently on later turns unless the path changes.

If the user provided file paths:
- Read them **fully** first (never partially).

Then do an initial repo scan:
- Glob likely directories
- Grep for related keywords/similar features
- Read the most relevant files fully
- Identify patterns, conventions, constraints, tests, configuration, data flows

If this initial research expands into a substantial investigation:
- Read the research-agent workflow in `references/research-agents.md` before delegating
- Resolve and announce the current project repo root where `thoughts/` will be written
- Spawn a dedicated research agent instead of doing all of it in the planning agent
- Use multiple research agents when the questions are meaningfully different
- Tell the user which research agents were launched and the exact question each one owns
- Require each research agent to write a findings doc into `<repo-root>/thoughts/` and return that path in its final response
- After agents finish, read the findings docs before asking the next decision question
- If sub-agents are unavailable or not launched despite a substantial research trigger, state that explicitly and write the required findings doc yourself in `<repo-root>/thoughts/` before continuing

**Output after Step 1 (always):**
- **Research Artifact Status:** either `quick local scan only` or the exact `thoughts/...md` path
- **Current State (evidence):** 3–7 bullets, each with file path (and line refs if available)
- **Implications:** what this means for approach/scope
- **Planning State File:** exact `planned-changes/...planning-state.md` path
- **Decision Focus:** why this is the highest-impact next decision
- **First Decision Card** (Step 2)

### Step 2 — Decision interview loop (dynamic research ↔ questions)

You will iterate:

1) Pick the **highest-leverage remaining decision** first (one that affects architecture, data model, rollout, risk, UX, or phasing).
2) Present a **Decision Card** with enough context for the user to make the trade-off without rereading the whole plan.
3) After the user answers:
   - Update the planning state file's Decision Log + Mini-plan
   - Decide whether targeted research is needed because of their answer
   - If needed: research immediately, report findings, then ask the next decision
   - If that research is substantial, delegate it via `references/research-agents.md`

**Decision Card format (required):**

**Decision #N — [short title]**
- Context: [repo evidence, constraints, and current plan state relevant to this decision]
- Why it matters: [impact on architecture, sequencing, risk, UX, migration, or implementation cost]
- Trade-offs:
  - A) [benefit, cost, risk]
  - B) [benefit, cost, risk]
  - (C) [benefit, cost, risk] (only if necessary)
- Recommendation: [only if supported by repo evidence; cite files]
- Question: [single concrete question]

**Question discipline:**
- Ask at most **2** questions per turn.
- Prefer decisions like: data model, API contract, rollout strategy, migration approach, feature flagging, error handling, telemetry, performance budgets, UI/UX constraints.

### Step 3 — Phase structure checkpoint (after key decisions)

Once the major decisions are set (or enough to shape work), propose phase structure:

- Phase names + what each accomplishes
- Dependencies between phases
- Identify which phases require manual validation

Ask:
- "Does this phasing and ordering make sense?"
- (If needed) one additional question about granularity or rollout.

### Step 4 — Draft plan (still interactive)

Use the planning state file as the source for the draft. Read `references/planning-document.md`, then draft the plan content in-chat first (do not write the final plan file yet).
If **any** Open Questions remain, continue the interview loop until resolved.

### Step 5 — Write the plan file (only when user says "finalize/write the plan")

Create: `planned-changes/YYYY-MM-DD-kebab-description.md`
- Use the user's timezone (Europe/London) to compute date (via Bash `date` if available).
- Read and follow `references/planning-document.md` before writing the final file.

## Chat update format (every turn)

Do not repeat the full mini-plan or full decision log every turn. Those belong in the planning state file.

Always show:
- **State file:** only if newly created, moved, or materially important to mention
- **Research performed this turn:** concise, with artifact paths when applicable
- **Decision context:** why this decision is next and what evidence constrains it
- **Trade-offs:** practical pros, cons, risks, and implementation impact for each option
- **Next Decision Card** (or "Ready to draft/finalize")

## Stop / Pause behavior

If user says "stop" or "pause":
- Stop interviewing immediately.
- Update the planning state file first.
- Output:
  - Planning state file path
  - Decisions made since the last user-visible summary
  - Open Questions (if any)
  - Next 1–2 recommended decisions to answer next time
