---
name: interactive-plan
description: Interactive global implementation planning via iterative repo research + decision interview. Use when user asks to create/make an implementation plan, scope a feature/refactor/system change, or when requirements are unclear and decisions must be made.
---

# Interactive Global Implementation Planning

## Purpose

Create a high-quality implementation plan by alternating between:
1) **Research** (repo/docs investigation) and
2) **Interviewing** (eliciting decisions that research cannot answer).

This is a **single-agent** workflow. Do not spawn sub-agents or multi-agent workflows.

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
- You may write the final plan to `planned-changes/` **only when the user explicitly asks to finalize**.

## Hard constraints and guardrails

- **Research-first:** Do an initial repo scan before asking substantive questions.
- **Ask only what you cannot discover:** If the repo can answer it, research instead of asking.
- **Interactive:** Do not draft the entire plan in one pass. Build it through an interview loop.
- **2 questions max per turn** (unless the user asks for more).
- **Verify corrections:** If the user corrects you, validate via repo when possible.
- **No open questions in the final plan:** If uncertainties remain, keep interviewing.
- **Stop condition:** If the user says "stop"/"pause", stop the loop and summarize progress + next decisions.

## Persistent working artifacts (maintain continuously)

Maintain and update these throughout the session; include them in your progress updates:

1) **Goal** (1 sentence)
2) **Constraints** (bullets)
3) **Current State Findings** (with file references)
4) **Research Backlog** (what you'll investigate next)
5) **Decision Log** (decision → chosen option → rationale → evidence)
6) **Open Questions** (must be empty before finalizing)
7) **Mini-plan** (3–8 bullets, evolving phased outline)

## Workflow

### Step 1 — Intake + initial research pass (always)

If the user provided file paths:
- Read them **fully** first (never partially).

Then do an initial repo scan:
- Glob likely directories
- Grep for related keywords/similar features
- Read the most relevant files fully
- Identify patterns, conventions, constraints, tests, configuration, data flows

**Output after Step 1 (always):**
- **Current State (evidence):** 3–7 bullets, each with file path (and line refs if available)
- **Implications:** what this means for approach/scope
- **Mini-plan v0:** an initial outline (not final)
- **First Decision Card** (Step 2)

### Step 2 — Decision interview loop (dynamic research ↔ questions)

You will iterate:

1) Pick the **highest-leverage next decision** (one that affects architecture/phasing).
2) Present a **Decision Card**.
3) After the user answers:
   - Update Decision Log + Mini-plan
   - Decide whether targeted research is needed because of their answer
   - If needed: research immediately, report findings, then ask the next decision

**Decision Card format (required):**

**Decision #N — [short title]**
- Why it matters: [1 sentence]
- Options:
  - A) …
  - B) …
  - (C) … (only if necessary)
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

Draft the plan content in-chat first (do not write file yet).
If **any** Open Questions remain, continue the interview loop until resolved.

### Step 5 — Write the plan file (only when user says "finalize/write the plan")

Create: `planned-changes/YYYY-MM-DD-kebab-description.md`
- Use the user's timezone (Europe/London) to compute date (via Bash `date` if available).

## Planning document requirements (must be included)

When producing the plan (in-chat draft and in the saved file), use this structure:

```markdown
# [Feature/Task Name] Implementation Plan

## Overview
[Brief: what we're implementing and why]

## Current State Analysis
[What exists now, what's missing, key constraints/patterns discovered]

### Key Discoveries
- [Finding + file reference]
- [Pattern to follow + file reference]
- [Constraint + file reference]

## Desired End State
[Concrete specification of end behavior and how to verify it]

## What We're NOT Doing
[Explicit out-of-scope list to prevent scope creep]

## Implementation Approach
[High-level strategy and rationale, tied to discovered repo patterns]

## Phase 1: [Descriptive Name]

### Overview
[What this phase accomplishes]

### Changes Required
#### 1. [Component/File Group]
**File**: `path/to/file.ext`
**Changes**: [summary]

```[language]
# illustrative snippet only when helpful
```

### Open Implementation Tasks
- [ ] Task 1
- [ ] Task 2

### Success Criteria

#### Automated Verification:
- [ ] Unit tests pass: `yarn test` (or relevant command)
- [ ] Type checking passes: `npm run typecheck` (or relevant command)
- [ ] Linting passes: `yarn lint` (or relevant command)
- [ ] Integration tests pass: [relevant command]

#### Manual Verification:
- [ ] Feature works as expected when tested via UI
- [ ] Performance is acceptable under load
- [ ] Edge case handling verified manually
- [ ] No regressions in related features

**Implementation Note:** After completing this phase and all automated verification passes, pause for human confirmation that manual testing succeeded before starting the next phase.

---

## Phase 2: [Descriptive Name]

[Repeat same structure]

---

## Testing Strategy

### Unit Tests
- What to test
- Key edge cases

### Integration Tests
- End-to-end scenarios

### Manual Testing Steps
1. …
2. …
3. …

## Performance Considerations

[Perf risks, budgets, caching/indexing, hot paths]

## Migration Notes

[Data migration/backfill/compat steps, rollback plan, feature flags, staged rollout]

## References
- Source files examined
- Relevant internal docs/specs
```

## Progress update format (every turn)

Always show:
- **Mini-plan (current)**
- **Decision Log (new entries only)**
- **Research performed this turn**
- **Next Decision Card** (or "Ready to draft/finalize")

## Stop / Pause behavior

If user says "stop" or "pause":
- Stop interviewing immediately.
- Output:
  - Mini-plan
  - Decisions made
  - Open Questions (if any)
  - Next 1–2 recommended decisions to answer next time
