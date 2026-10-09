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

**Spec source check**: is this a fresh request (user's words) or a **port of an existing skill** (its SKILL.md + scripts are the source of truth)? If a port: skip the grill in step 2, go to **porting mode** instead — extract fidelity facts from the original (gotcha count, command surface, script inventory, license) and rebuild the instruction layer only. Description is **derived, not inherited**: keep the routing intent, rewrite the wording with concrete trigger phrases. Never wholesale-copy content you don't have the license to copy (check LICENSE first; proprietary → port the *methodology*, rewrite the code).

### 2. Grill (interview phase)

Load [references/interview.md](references/interview.md).
- Ask decisive questions **one at a time**, each with your recommended answer.
- If a question can be answered by exploring (reading the user's scripts, running their tool, checking a repo, checking `~/.agents/skills/`), **explore instead of asking**.
- Stop when every branch in interview.md's decision tree is resolved. Usually 5–10 questions, never more.

### 3. Spec confirmation

Present a one-page spec:
- skill name (legal) + trigger description draft
- workflow steps (imperative, executable)
- **audience** the artifact serves (B5a) + tone rule that follows
- **data/claim sources** allowed (B5b) — user-provided / cited / labeled 示例-假设, nothing else
- **craft notes** (B5c) — the domain heuristics, each as what + why
- needed scripts/assets/references
- out-of-scope list

**Wait for approval before writing any files.**

### 4. Scaffold

Follow [references/anatomy.md](references/anatomy.md) and [references/template.md](references/template.md):
- Create `~/.agents/skills/<name>/` (or project `.agents/skills/<name>/` if the user asked for project scope)
- SKILL.md stays a workflow, not a manual: reference material → `references/`, code → `scripts/` (split by kind, not by line quota)
- name: lowercase `a-z 0-9` + single hyphens, no leading/trailing/consecutive hyphens, ≤ 64 chars
- description: what it does + when to use it + concrete user trigger phrases, ≤ 1024 chars
- Every referenced file must exist; every script must be executable and run at least once

### 5. Verify (quality gate)

Run [references/quality-checklist.md](references/quality-checklist.md) on the generated skill:
- frontmatter valid, name legal, description specific
- every referenced script exists and smoke-runs
- **end-to-end trial**: invoke the skill on the smallest plausible real task (a 100-word article, one file, one item). Observe the full workflow; fix every break, then re-trial until the trial completes.
- no step requires the agent to improvise (prose instructions it must guess = 60-point skill)

Score the 5 axes with the rubric; below 80 → fix and re-score before acceptance.

### 6. User acceptance (never self-grade the router)

Present to the user: the trigger simulation (3 tasks, including the negative one) and the trial-run artifacts. The user confirms:
- would this description load the skill for the right tasks — and not the wrong ones?
- does the trial output meet their success criteria (B9)?

Axis B points count **only after the user confirms** — the agent proposes, the user disposes. Any fail → resolve only the still-open branches (back to step 2, not a full re-interview), then re-verify.

### 7. Handoff

Tell the user:
- where the skill lives
- how to invoke it (`/skill:<name>` or natural language)
- one example trigger phrase they can test immediately
- **improvement log**: list what the trial exposed and what it feeds back into skill-forge itself (a new B-branch, a guardrail, a craft-note pattern). A meta-skill that doesn't log its test findings stays one version behind.

## Rules

- Never skip the grill phase for non-trivial skills. A trivial one-liner utility may jump straight to spec approval, but only after the user confirms triviality.
- Prefer executable commands over prose. "Run `./scripts/x.sh <input>`" beats "process the input appropriately".
- Split by kind, not by count: workflow stays in SKILL.md; reference material to references/; code to scripts/. Readability test: a busy user skims the workflow in one sitting.
- **Credentials are a first-class guardrail**: no secret ever enters a skill file. Scripts read tokens from environment variables or the user's keychain at runtime; SKILL.md names the variable, never its value; whenever an API is involved, Guardrails says so explicitly.
- **Dependency inventory**: every runtime dep (npm/python/binary) gets a line with its install command; a trial that hits a missing dep reports it honestly, never silently skips the step it blocked. (Example found in testing: `playwright` pip-installed but browsers not downloaded — the dep line must cover `playwright install chromium`, not just the package.)
- **Context hygiene**: helper scripts > ~200 lines are documented by contract, not source — first step is `--help`, the doc says *when* to read the source (only after --help proves the contract insufficient). A skill that says "read the script" for a 500-line helper is leaking its own quality: the agent's context dies before the task does.
- **Contamination gate**: when the skill's domain has close look-alikes (another provider's SDK, another vendor's CLI, a similarly named tool), the skill must open with a *detect → stop → ask* rule: a concrete grep/markers list for the foreign domain, and an explicit "do not mix foreign calls into this domain's files" line. A skill that quietly edits an OpenAI project with Anthropic calls has failed the task even if the code runs.
- **Drift table**: a skill wrapping a fast-moving API must carry a short table of the *most-changed* fields (stale prior → current) and state "this skill's data beats your training memory". Without it, the agent's 18-month-old priors silently overwrite the skill's fresher facts.
- **Subcommand surface**: when users can invoke the skill with bare flag-style words (`/skill migrate`), ship a subcommand table mapping each bare word to its deterministic action, marking which are interactive (confirm-scope-first) and which are non-interactive — so a bare command is never misread as prose. A skill that says "read the script" for a 500-line helper is leaking its own quality: the agent's context dies before the task does.
- **Script documentation coverage**: every shipped script is documented somewhere (SKILL.md or references/); an undocumented script is a coverage bug, scored 0 on axis D.
- The generated skill's description is its most important artifact — spend the most interview time on it.
