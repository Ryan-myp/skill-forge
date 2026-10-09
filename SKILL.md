---
name: skill-forge
description: Create high-quality agent skills by first interviewing the user about their real workflow (grill style, one question at a time), then scaffolding a standards-compliant skill (SKILL.md + scripts/ + references/) and verifying it against a quality gate. Use when the user wants to create, design, or upgrade a skill; says "make a skill", "build a skill for X", or asks how to turn their own workflow/repo/tooling into a skill.
---

# Skill Forge

Meta-skill: interview deeply first, then generate. A skill that skips the interview and just scaffolds from a one-liner request is a 60-point skill. This one doesn't.

## Workflow

### 1. Restate & scope

Restate the goal in one sentence. Confirm two things:
- What task will the **target** skill automate?
- How will it be triggered (user phrases, files, events)?

### 2. Grill (interview phase)

Load [references/interview.md](references/interview.md).
- Ask decisive questions **one at a time**, each with your recommended answer.
- If a question can be answered by exploring (reading the user's scripts, running their tool, checking a repo, checking `~/.agents/skills/`), **explore instead of asking**.
- Stop when every branch in interview.md's decision tree is resolved. Usually 5–10 questions, never more.

### 3. Spec confirmation

Present a one-page spec:
- skill name (legal) + trigger description draft
- workflow steps (imperative, executable)
- needed scripts/assets/references
- out-of-scope list

**Wait for approval before writing any files.**

### 4. Scaffold

Follow [references/anatomy.md](references/anatomy.md) and [references/template.md](references/template.md):
- Create `~/.agents/skills/<name>/` (or project `.agents/skills/<name>/` if the user asked for project scope)
- SKILL.md ≤ ~100 lines; depth moves to `references/`, code to `scripts/`
- name: lowercase `a-z 0-9` + single hyphens, no leading/trailing/consecutive hyphens, ≤ 64 chars
- description: what it does + when to use it + concrete user trigger phrases, ≤ 1024 chars
- Every referenced file must exist; every script must be executable and run at least once

### 5. Verify (quality gate)

Run [references/quality-checklist.md](references/quality-checklist.md) on the generated skill:
- frontmatter valid, name legal, description specific
- **trigger simulation**: given 3 real tasks the user performs, would the description cause the agent to load this skill?
- every referenced script exists and smoke-runs
- progressive disclosure: SKILL.md readable in < 30 seconds
- no step requires the agent to improvise (prose instructions it must guess = 60-point skill)

Score 0–100. Anything below 80 → fix and re-score before delivery.

### 6. Handoff

Tell the user:
- where the skill lives
- how to invoke it (`/skill:<name>` or natural language)
- one example trigger phrase they can test immediately

## Rules

- Never skip the grill phase for non-trivial skills. A trivial one-liner utility may jump straight to spec approval, but only after the user confirms triviality.
- Prefer executable commands over prose. "Run `./scripts/x.sh <input>`" beats "process the input appropriately".
- Keep the generated SKILL.md short. If it exceeds ~100 lines, split.
- The generated skill's description is its most important artifact — spend the most interview time on it.
