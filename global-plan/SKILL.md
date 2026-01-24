---
name: global-plan
description: Create detailed implementation plans through collaborative research and analysis. Use when user says "create a plan", "create an implementation plan", "make a plan for this feature", or provides a task/feature description that needs planning. This skill works through research, analysis, and documentation in a single-agent workflow, saving the final plan to the planned-changes folder.
version: 1.0.0
---

# Global Implementation Planning

## Purpose

- Guide users through creating comprehensive implementation plans for features, refactors, or system changes
- Research the codebase thoroughly to understand current state and patterns
- Collaboratively develop phased implementation plans with clear success criteria
- Save detailed plans to `planned-changes/` folder for future reference

## When to use this skill

- User asks to "create a plan", "create an implementation plan", or "make a plan for X"
- User provides a task/feature description that needs planning before implementation
- User needs to scope out work before starting implementation
- User says "I want to add X feature" without a clear implementation approach

## Inputs and environment

**Required from user:**
- Description of task or feature to implement (or file path to a description)
- Relevant context, constraints, or specific requirements (if available)
- Links to related research or previous implementations (if available)

**Environment:**
- Access to the full codebase for research
- Write permissions to `planned-changes/` directory
- Git repository context for understanding patterns and conventions

**Assumptions:**
- Working in Yarn 1 workspaces monorepo (React frontend, Firebase Functions backend)
- Standard tech stack: React 18, MUI v5, Redux Toolkit, Firebase (Auth, Firestore, Functions)
- Plans should follow existing patterns and conventions found in the codebase

## Workflow (step-by-step instructions)

### Step 1: Initial Input Gathering

**If parameters provided (file path or reference):**
- Immediately and completely read the provided file(s)
- Start research process without asking for more information

**If no parameters provided:**
- Ask user for:
  1. Description of task or feature to implement (or path to description file)
  2. Any relevant context, constraints, or specific requirements
  3. Links to related research or previous implementations (if available)

**Example initial response when no parameters:**
```
I'll help you create a detailed implementation plan. Let me start by understanding what we're building.

Please provide:
1. A description of the task or feature we need to implement (or a path to a description file)
2. Any relevant context, constraints, or specific requirements
3. Links to related research or previous implementations (if available)

I'll analyze this information and work with you to create a comprehensive plan.
```

### Step 2: Context Gathering & Initial Analysis

**Read all context files completely:**
- Task/feature description files
- Supporting research documents
- Related implementation plans
- Any data files or configuration files mentioned
- Never read files partially - always read completely

**Perform initial research:**
- Search the codebase for files related to the feature/task
- Look for: implementation files, tests, configuration, documentation
- Categorize findings (implementation code, tests, configs, patterns)
- Read relevant files to understand current implementation
- Trace data flow, note key functions, understand component interactions
- Look for existing patterns or similar implementations to serve as templates

**Analyze and verify understanding:**
- Cross-reference task requirements with what code currently does
- Identify discrepancies or gaps between desired behavior and existing implementation
- Note assumptions that need clarification
- Determine true scope of work based on analysis

**Present informed understanding with focused questions:**
```
Based on the task description and my research, I understand we need to [accurate summary].

I've found that:
- [Current implementation detail with file:line reference]
- [Relevant pattern or constraint discovered]
- [Potential complexity or edge case identified]

Questions that my research couldn't answer:
- [Specific technical question requiring human judgment]
- [Business logic clarification]
- [Design preference that affects implementation]
```

**Important:** Only ask questions you genuinely cannot answer through investigation.

### Step 3: Research & Discovery

**If user corrects any misunderstanding:**
- Do NOT accept correction blindly
- Re-read relevant files or sections they reference
- Verify information yourself before proceeding

**Maintain a research list:**
- Keep a simple list of items to investigate further
- Work through list one by one
- Update as new information is gathered

**Perform comprehensive research:**
- Continue searching codebase for additional relevant files/patterns
- Read any new important files
- Extract reusable patterns or examples
- Identify different design options based on findings

**Present findings and design options:**
```
Based on my research, here's what I found:

**Current State:**
- [Key discovery about existing code]
- [Pattern or convention to follow]

**Design Options:**
1. [Option A] – [pros/cons]
2. [Option B] – [pros/cons]

**Open Questions:**
- [Technical uncertainty]
- [Design decision needed]

Which approach aligns best with your vision?
```

### Step 4: Plan Structure Development

**Draft initial plan outline:**
```
Here's my proposed plan structure:

## Overview
[1-2 sentence summary]

## Implementation Phases:
1. [Phase name] – [what it accomplishes]
2. [Phase name] – [what it accomplishes]
3. [Phase name] – [what it accomplishes]

Does this phasing make sense? Should I adjust the order or granularity?
```

**Get feedback on structure:**
- Adjust phases or granularity based on user input
- Ensure each phase is testable and has clear deliverables

### Step 5: Detailed Plan Writing

**Create plan file in planned-changes/ directory:**
- Use format: `YYYY-MM-DD-description.md`
- `YYYY-MM-DD` = today's date in user's timezone
- `description` = brief kebab-case summary of task
- Examples:
  - `2025-12-26-parent-child-tracking.md`
  - `2025-12-26-improve-error-handling.md`

**Use this template structure for the plan:**

```markdown
# [Feature/Task Name] Implementation Plan

## Overview

[Brief description of what we're implementing and why]

## Current State Analysis

[What exists now, what's missing, key constraints discovered]

### Key Discoveries:
- [Important finding with file:line reference]
- [Pattern to follow]
- [Constraint to work within]

## Desired End State

[Specification of desired end state after plan is complete, and how to verify it]

### Key Discoveries:
- [Important finding with file:line reference]
- [Pattern to follow]
- [Constraint to work within]

## What We're NOT Doing

[Explicitly list out-of-scope items to prevent scope creep]

## Implementation Approach

[High-level strategy and reasoning]

## Phase 1: [Descriptive Name]

### Overview
[What this phase accomplishes]

### Changes Required:

#### 1. [Component/File Group]
**File**: `path/to/file.ext`
**Changes**: [Summary of changes]

```[language]
// Specific code to add/modify
```

### Open Implementation Tasks
- [ ] [Working list of anticipated changes]
- [ ] [...]

### Success Criteria:

#### Automated Verification:
- [ ] Migration applies cleanly: `make migrate` (or relevant command)
- [ ] Unit tests pass: `yarn test` (or relevant command)
- [ ] Type checking passes: `npm run typecheck` (or relevant command)
- [ ] Linting passes: `yarn lint` (or relevant command)
- [ ] Integration tests pass: [relevant command]

#### Manual Verification:
- [ ] Feature works as expected when tested via UI
- [ ] Performance is acceptable under load
- [ ] Edge case handling verified manually
- [ ] No regressions in related features

**Implementation Note**: After completing this phase and all automated verification passes, pause here for manual confirmation from the human that manual testing was successful before proceeding to the next phase.

---

## Phase 2: [Descriptive Name]

[Similar structure with both automated and manual success criteria...]

---

## Testing Strategy

### Unit Tests:
- [What to test]
- [Key edge cases]

### Integration Tests:
- [End-to-end scenarios]

### Manual Testing Steps:
1. [Specific step to verify feature]
2. [Another verification step]
3. [Edge case to test manually]

## Performance Considerations

[Any performance implications or optimizations needed]

## Migration Notes

[If applicable, how to handle existing data/systems]

## References

[List any relevant documentation or source files]
```

### Step 6: Sync and Review

**Ensure planned-changes directory is synced** so plan is indexed and available

**Present draft plan location:**
```
I've created the initial implementation plan at:
`planned-changes/YYYY-MM-DD-description.md`

Please review it and let me know:
- Are the phases properly scoped?
- Are the success criteria specific enough?
- Any technical details that need adjustment?
- Missing edge cases or considerations?
```

**Iterate based on feedback:**
- Be ready to add missing phases
- Adjust technical approach
- Clarify success criteria
- Update scope
- Continue refining until user is satisfied

## Code execution / tools

**Preferred tools for research:**
- `grep` - search for code patterns
- `glob` - find files by pattern
- `read` - read complete file contents
- `lsp_*` - language server tools for code understanding

**When to use:**
- Use `grep` when searching for specific patterns or functions
- Use `glob` when finding files by name or extension pattern
- Use `read` when you need complete file contents (always read fully)
- Use `lsp_*` when you need symbol definitions, references, or diagnostics

**Search guidelines:**
- Always search comprehensively before asking questions
- Read relevant files completely before drawing conclusions
- Maintain a research list and work through it systematically
- Cite file:line references for all key findings

## Outputs and format

**Primary output:**
- Detailed implementation plan saved to `planned-changes/YYYY-MM-DD-description.md`
- Plan includes: overview, current state, desired end state, out-of-scope items, phased implementation, testing strategy, performance considerations, migration notes, references

**Progress updates during planning:**
- Present initial understanding and questions after Step 2
- Present design options after Step 3
- Present plan outline after Step 4
- Present draft plan location after Step 5

**Final summary format:**
```
## Planning Complete

**Plan Location:** `planned-changes/YYYY-MM-DD-description.md`

**Key Phases:**
1. [Phase 1] – [summary]
2. [Phase 2] – [summary]
3. [Phase 3] – [summary]

**Success Criteria:**
- [Automated verification methods]
- [Manual verification methods]

**Estimated Complexity:** [low/medium/high]
**Risk Areas:** [identified risks if any]

Ready for implementation when you approve the plan.
```

## Style and guardrails

**Tone:**
- Collaborative and inquisitive
- Clear and structured
- Cite specific file:line references for all findings
- Be skeptical of vague requirements

**Behavioral guidelines:**
- Be Interactive: Work collaboratively; don't draft entire plan in one go
- Be Thorough: Read all context files completely
- Be Practical: Focus on incremental, testable changes
- Be Skeptical: Question vague requirements, identify issues early

**Critical behaviors:**
- Always read files completely - never partially
- Verify information yourself when user provides corrections
- Maintain and update your own research and planning list
- Resolve ALL uncertainties before finalizing the plan
- Stop and get feedback at each major step

**Hard constraints:**
- Do NOT spawn sub-agents or multi-agent workflows
- Do NOT create external tickets (Jira, GitHub, etc.)
- Do NOT leave open questions in the final plan
- Do NOT assume patterns exist without finding them in the codebase
- Do NOT skip research phases to move faster

**When to pause and get feedback:**
- After initial understanding and questions (Step 2)
- After presenting design options (Step 3)
- After proposing plan structure (Step 4)
- After writing initial draft (Step 5)

## Examples

### Example 1: Feature with existing pattern

**User request:**
"I want to add a new field to the user profile that tracks their subscription status."

**Skill actions:**
1. Search for existing user profile fields and patterns
2. Find `packages/org-model-schema/src/index.js` and understand current structure
3. Search for how other fields are added to profiles
4. Present findings: "Current profiles use [pattern]. I found subscription tracking in [file]."
5. Ask: "Do you want to follow this existing pattern or create a new approach?"
6. Create plan with single phase for schema update, backend migration, and UI changes
7. Save as `planned-changes/YYYY-MM-DD-user-subscription-status.md`

### Example 2: Complex refactor

**User request:**
"We need to refactor the error handling in the Cloud Functions to be more consistent."

**Skill actions:**
1. Read `apps/functions/` directory structure
2. Search for existing error handling patterns using grep for "throw", "catch", "error"
3. Categorize findings: some functions use try/catch, some don't; inconsistent error messages
4. Present findings and design options:
   - Option A: Centralize error handler utility
   - Option B: Add try/catch to each function
5. Get user preference
6. Create multi-phase plan:
   - Phase 1: Create error handler utility
   - Phase 2: Migrate 10 critical functions
   - Phase 3: Migrate remaining functions
7. Save as `planned-changes/YYYY-MM-dd-error-handling-refactor.md`

### Example 3: New feature with dependencies

**User request:**
"I want to add a dark mode toggle to the app."

**Skill actions:**
1. Search for theme-related code in `apps/web/src/`
2. Find `apps/web/src/assets/theme/index.js` and current MUI theme setup
3. Check if any existing dark mode patterns exist
4. Search for MUI v5 dark mode patterns online (via librarian if needed)
5. Present findings: "Currently using MUI v5 with custom theme. No dark mode exists."
6. Outline phases: theme setup, toggle component, state management, implementation across pages
7. Create detailed plan with file changes and success criteria
8. Save as `planned-changes/YYYY-MM-dd-dark-mode-feature.md`

## References

- [planned-changes/](../../../planned-changes/) - Directory where plans are saved
- [commands/global-plan.md](../../../commands/global-plan.md) - Original command this skill is based on
- [AGENTS.md](../../../AGENTS.md) - Technical context about the codebase
- [docs/how-to-create-a-skill-v3.md](../../../docs/how-to-create-a-skill-v3.md) - Skill creation guide
