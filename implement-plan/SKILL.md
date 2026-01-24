---
name: implement-plan
description: Execute approved implementation plans from the planned-changes directory, performing each phase sequentially with automated verification and manual review checkpoints. Use when the user provides a plan path or says "implement this plan", "execute the plan", or references a plan in planned-changes/.
---

# Implement Plan

## Purpose

- Execute approved implementation plans saved in the `planned-changes/` directory
- Perform each phase sequentially with proper verification
- Track progress by updating the plan file with completed tasks
- Maintain code quality while adapting to real codebase constraints

## When to use this skill

- User provides a path to a plan file in `planned-changes/` (e.g., `planned-changes/YYYY-MM-DD-description.md`)
- User says "implement this plan", "execute the plan", "work on this plan"
- User references a specific plan that needs to be executed
- There is an approved plan with phases and success criteria to follow

## Inputs and environment

**Required from user:**
- Path to plan file in `planned-changes/` directory (e.g., `planned-changes/2025-12-26-feature.md`)
- Or ask for the path if not provided

**Environment assumptions:**
- Plans are stored in `planned-changes/` directory
- Plan files use markdown format with checkboxes for progress tracking (`- [ ]` for incomplete, `- [x]` for complete)
- Plans contain phases, files to modify, and success criteria
- You have access to all tools needed for the implementation (edit, read, bash, etc.)

**No multi-agent architecture:**
- Do NOT spawn sub-tasks or other agents
- Do NOT rely on external agents
- Perform all research and implementation yourself

## Workflow

### Step 1: Verify Plan Path

If a plan file path is provided:
- Read it completely (no partial reads)
- Understand the phases, changes, and success criteria

If no plan path is provided:
- Ask the user to supply the path to a plan file in the `planned-changes/` directory
- Example: `planned-changes/YYYY-MM-DD-description.md`

### Step 2: Read All Referenced Files

For each file mentioned in the plan:
- Open it and read it completely
- You need full context to modify the code correctly
- Do not make assumptions about file contents

### Step 3: Prepare to Implement

Look for existing checkmarks (`- [x]`) in the plan:
- These indicate completed tasks
- Build a personal to-do list of the unchecked items and phases
- Think through how the phases relate to each other
- If anything is unclear, ask the user for clarification

### Step 4: Execute Phases Sequentially

For each phase in the plan:

#### 4.1 Review Phase Instructions
- Understand the goals
- Identify files to change
- Review success criteria (both automated and manual)
- If the plan includes code snippets, decide where they need to be inserted or modified

#### 4.2 Apply Changes
- Modify the codebase according to the plan
- Update configuration, tests, and documentation as described
- Keep the code style consistent with existing patterns in the codebase

#### 4.3 Run Automated Verification
- Execute the commands listed under automated success criteria
- Examples: `make test-component`, `npm run typecheck`, `yarn lint`, `yarn test`
- Fix any issues until all automated checks pass

#### 4.4 Mark Progress
- Update your personal to-do list
- In the plan file itself, check off the tasks you completed
- Convert `- [ ]` to `- [x]` for completed items

#### 4.5 Request Manual Verification
When automated checks pass:
- Pause and notify the user
- Use this format:

```
Phase [N] Complete – Ready for Manual Verification

Automated verification passed:
- [list of checks that passed]

Please perform the manual verification steps listed in the plan (e.g., UI tests, performance checks, edge cases).
Let me know when manual testing is complete so I can proceed to Phase [N+1].
```

#### 4.6 Wait for User Confirmation
- Wait for the user to confirm manual testing before starting the next phase
- If the user wants multiple phases executed at once, only pause after the final specified phase
- Do not proceed without user approval

### Step 5: Handle Discrepancies

If you find a mismatch between the plan and the code:

1. Pause and analyze why the instructions don't align
2. Present the issue to the user clearly:

```
Issue in Phase [N]
- Expected: [what the plan says]
- Found: [what you discovered in the code]
- Why this matters: [why it blocks progress or causes concern]
- Proposed next step or question for the user
```

3. Wait for guidance before proceeding

**Never:** blindly implement a plan that doesn't match the actual codebase

## Code execution and verification

**Automated checks:**
- Always run the automated checks specified in the plan
- Fix all failures before continuing to the next phase
- Do not skip verification steps

**Manual checks:**
- Wait for user confirmation that manual tests pass
- Do not mark manual checks as complete yourself
- Trust the user's feedback on manual testing

**Complete context:**
- Always read entire files, not just snippets
- Understanding full context reduces mistakes
- When in doubt, read the file again

## Resuming Work

If some items in the plan are already marked complete:
- Trust that checked items are done
- Start from the first unchecked item
- If something seems inconsistent, verify earlier work
- Avoid redoing tasks unnecessarily

## Error handling

If you hit a roadblock:
1. Ensure you have read all relevant code and documentation
2. Consider whether the code has evolved since the plan was written
3. Present mismatches to the user using the issue format above
4. Debug and explore on your own (do not create sub-tasks)
5. Ask for guidance if you can't resolve the issue

## Style and guardrails

**Implementation philosophy:**
- Follow the plan's intent while adapting to the actual codebase
- Finish each phase completely before moving to the next
- Use your judgment to resolve discrepancies, but consult the user when necessary
- Remember: You're implementing a solution, not just checking boxes

**Hard constraints:**
- Do NOT spawn sub-tasks or other agents
- Do NOT rely on external ticket systems or the thoughts folder
- Do NOT mark manual verification checks as complete yourself
- Do NOT proceed to the next phase without user confirmation after manual checks

**When to ask for clarification:**
- When the plan instructions are ambiguous
- When multiple interpretations are possible
- When the codebase doesn't match the plan's expectations
- When a phase has unclear success criteria

## Examples

### Example 1: Fresh plan execution

**User request:**
"Implement the plan at planned-changes/2025-12-26-feature-x.md"

**Skill actions:**
1. Read `planned-changes/2025-12-26-feature-x.md` completely
2. Identify all files mentioned and read them completely
3. Build a to-do list of all unchecked items
4. Execute Phase 1:
   - Make code changes
   - Run automated checks (e.g., `yarn lint`, `yarn test`)
   - Mark Phase 1 tasks as complete in the plan file
   - Request manual verification
5. Wait for user to confirm manual testing
6. Proceed to Phase 2 (repeat until all phases complete)
7. Report final status with summary of completed work

### Example 2: Resuming a partially-completed plan

**User request:**
"Continue with the plan at planned-changes/2025-12-25-feature-y.md"

**Skill actions:**
1. Read the plan file
2. Notice that Phase 1 is already marked complete (`- [x]`)
3. Identify that Phase 2, Task 1 is the first incomplete item
4. Start from Phase 2, Task 1 (do not redo Phase 1)
5. Execute remaining phases with proper verification checkpoints
6. Update progress in the plan file as work is completed

### Example 3: Plan with discrepancies

**User request:**
"Implement planned-changes/2025-12-26-feature-z.md"

**Skill actions:**
1. Read plan and all referenced files
2. Discover that Phase 3 references a function that doesn't exist
3. Present issue:

```
Issue in Phase 3
- Expected: Modify function `getUserName()` in src/users.js
- Found: Function `getUserName()` does not exist; there is only `getUserDisplayName()`
- Why this matters: Cannot complete Phase 3 without understanding which function to modify
- Proposed next step: Should I modify `getUserDisplayName()` instead, or is the plan outdated?
```

4. Wait for user guidance
5. Proceed based on user's response

## References

- [commands/implement-plan.md](../../../commands/implement-plan.md) - Original command that this skill is based on
- [planned-changes/](../../../planned-changes/) - Directory containing implementation plans
- [AGENTS.md](../../../AGENTS.md) - Project context, coding standards, and development philosophy
