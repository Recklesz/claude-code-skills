# Planning Document Requirements

Use this reference when drafting the implementation plan in chat and when writing the finalized plan file.

The plan must be concrete enough for a separate implementation agent to execute without re-discovering major decisions. It should cite source files, carry forward the decision log, and make validation expectations explicit.

## Required Structure

````markdown
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
1. ...
2. ...
3. ...

## Performance Considerations

[Perf risks, budgets, caching/indexing, hot paths]

## Migration Notes

[Data migration/backfill/compat steps, rollback plan, feature flags, staged rollout]

## References
- Source files examined
- Relevant internal docs/specs
````

## Requirements

- Use the planning state file as the source of truth for decisions, open questions, and the mini-plan.
- Include the decision rationale that led to the chosen implementation approach.
- Keep phases independently reviewable where possible.
- Include both automated and manual verification for each phase.
- Call out migrations, rollout controls, compatibility risks, and rollback steps when relevant.
- Do not leave unresolved open questions in the finalized plan.
