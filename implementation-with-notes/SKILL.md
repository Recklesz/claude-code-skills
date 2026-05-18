---
name: implementation-with-notes
description: Implement a specific plan, spec, or planned change while keeping a simple HTML notes file. Use when the user wants implementation work paired with a visual reminder of the implementation date, the thing being implemented, and the decisions, deviations, tradeoffs, and open questions that came up during implementation.
---

# Implementation With Notes

When implementing from a plan or spec, keep a simple HTML notes file near the planning file or planned-change directory.

The page only needs enough structure to be useful later:

- Implementation name: the thing being implemented.
- Implementation date: the current local date.
- Source plan/spec: the file or plan this came from, when available.
- Done / not done: a short visual reminder of what was completed and what was left out.

Keep the main focus on decisions made during implementation:

- Design decisions: choices made where the spec was ambiguous.
- Deviations: places where the implementation intentionally departs from the spec, and why.
- Tradeoffs: alternatives considered and why the selected approach was chosen.
- Open questions: anything the user should confirm or revise.

Update the notes as these decisions happen. Do not wait until the end and reconstruct them from memory.
