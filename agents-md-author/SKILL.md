---
name: agents-md-author
description: Create or update AGENTS.md files by inspecting the repository structure, conventions, and workflows. Research first, ask questions if missing info, then generate agent-focused documentation with CLAUDE.md symlink.
---

# AGENTS.md Author Skill

## When to Use
Use this skill when:
- Creating a new AGENTS.md file for a repository
- Updating an existing AGENTS.md to reflect new conventions or tools
- Standardizing agent workflows across a team or project

## Workflow

### Phase 1: Research (Always First)
Before writing anything, thoroughly inspect the repository:

1. **Inspect the repo root**
   - Look for existing AGENTS.md, CLAUDE.md, README.md
   - Check for package managers: `package.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `Makefile`, `justfile`, `.tool-versions`
   - Identify CI configuration: `.github/workflows/`, `.gitlab-ci.yml`, `buildkite.yml`, `circleci/`
   - Look for configuration files: `.prettierrc`, `.eslintrc`, `ruff.toml`, `mypy.ini`, `.editorconfig`

2. **Explore directory structure**
   - Identify key directories (`src/`, `lib/`, `tests/`, `docs/`, `scripts/`, etc.)
   - Note any special-purpose directories
   - Look for monorepo indicators (packages/, apps/, etc.)

3. **Extract build/test commands**
   - Read `package.json` scripts section
   - Read `pyproject.toml` or `Makefile` for commands
   - Note lint, typecheck, test, build, and dev commands
   - Identify any pre-commit hooks

4. **Capture conventions**
   - Check for code style configs (formatting, linting)
   - Look at existing code patterns in key files
   - Note any CONTRIBUTING.md, CODE_STYLE.md, or similar docs

### Phase 2: Assess and Decide
After research:

- **If you found sufficient information**: Proceed to Phase 3 with your findings
- **If information is missing or unclear**: Use the question tool to ask the user before proceeding

### Phase 3: Generate AGENTS.md
Write an AGENTS.md with these sections (adapt based on findings):

1. **Scope** - What agents should do in this repo
2. **Setup commands** - Install, dev, build, test, lint commands
3. **Repo map** - Key directories and where to add new code
4. **Conventions** - Code style, patterns, naming, testing expectations
5. **Security/privacy** - Secrets handling, stop-and-ask triggers
6. **PR hygiene** - Required checks, PR template expectations
7. **Non-coding workflows** - If relevant (docs, specs, reports)
8. **Unknowns/TODO** - List any missing info and who can resolve

### Phase 4: Create CLAUDE.md Symlink
After AGENTS.md is complete:
1. Create `CLAUDE.md` as a symlink to `AGENTS.md` using bash:
   ```bash
   ln -sf AGENTS.md CLAUDE.md
   ```
2. Verify the symlink was created correctly

## Writing Guidelines
- Prefer short bullet points and explicit commands over prose
- Include concrete examples for outputs (PR descriptions, commit messages)
- Avoid vague rules; use verifiable checks
- Keep agent-focused (operational instructions, not human-oriented docs)
- Do not include credentials, tokens, or internal secrets
- If monorepo, consider nested AGENTS.md files for subprojects

## Non-Coding Repos
If this is a non-coding repository (docs, specs, marketing, etc.):
- Adjust Scope to reflect documentation/workflows instead of code
- Omit build/test commands; focus on edit/preview/publish workflows
- Include conventions for the relevant format (voice, tone, accessibility)
- Note any review/approval requirements
