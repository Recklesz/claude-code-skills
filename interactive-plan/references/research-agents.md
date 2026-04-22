# Research Agents

Use this reference whenever the planning workflow enters a research phase that is more substantial than a quick local scan.

## When to spawn research agents

Spawn a research agent when any of these are true:

- The research spans multiple areas of the repo.
- You need to compare several existing implementations or patterns.
- You need to answer more than one independent research question.
- The planning agent would otherwise spend a long turn just reading/searching.
- The user's request implies broad repo discovery before the next decision.

Keep quick, local fact-checks in the planning agent. Delegate only the heavier research work.

## Agent shape

For codebase research, use `agent_type="explorer"` unless there is a clear reason not to.

Use a high-capability model:

- Preferred: `gpt-5.4`
- Reasoning effort: `high`
- Use `xhigh` only for unusually tangled or high-risk investigations

Reuse the current conversation context only when it materially helps. Otherwise give the agent a tight, self-contained brief.

## How to split the work

If the research decomposes into distinct questions, spawn multiple research agents in parallel. Give each agent a separate ownership area, for example:

- direct implementation lookup for the exact feature being planned
- similar pattern search across the repo
- validation of tests, rollout mechanisms, or migration precedents

Do not send two agents after the same question unless you explicitly need competing independent reads.

## What each research agent should do

Each research agent should:

1. Investigate the exact thing you are looking for.
2. Also search for similar patterns elsewhere in the repo that could be reused.
3. Read the most relevant files fully, not just grep snippets.
4. Return evidence with file references.
5. Write a markdown findings document into the current repo's `thoughts/` folder.

## Findings document requirement

Every substantial research run must produce a `.md` file in `<repo>/thoughts/`.
If `thoughts/` does not exist yet, create it in the current repo root before writing the findings doc.

Use a descriptive, date-stamped filename. Prefer patterns like:

- `thoughts/implementation-analysis-<topic>-YYYY-MM-DD.md`
- `thoughts/pattern-analysis-<topic>-YYYY-MM-DD.md`
- `thoughts/<YYYY-MM-DD>-<topic>.md`

The document should include:

```markdown
# <Short Title>

## Question
[What this agent was asked to find]

## Scope
- Areas searched
- Keywords or concepts checked

## Key Findings
- Finding with file reference
- Finding with file reference

## Similar Patterns
- Existing implementation or pattern with file reference
- Reusable precedent with file reference

## Implications For The Plan
- What this changes or confirms

## Open Risks / Unknowns
- Any remaining uncertainty
```

## Integration back into the planning workflow

After the research agent finishes:

- Read the findings doc it wrote in `thoughts/`
- Fold the results into Current State Findings, the Decision Log, and the Mini-plan
- Cite the original repo files as primary evidence, using the thoughts doc as a research artifact
- Ask the next highest-leverage decision question

Wait for research agents only when their result is on the critical path for the next planning step.
