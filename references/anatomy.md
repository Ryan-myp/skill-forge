# Skill Anatomy (Agent Skills standard)

## Directory layout

```
my-skill/
├── SKILL.md              # required: frontmatter + imperative workflow
├── scripts/              # helper scripts, smoke-tested
├── references/           # deep docs loaded on-demand
└── assets/               # templates, fixtures
```

## SKILL.md frontmatter

| Field | Required | Notes |
|---|---|---|
| `name` | yes | 1–64 chars, lowercase `a-z 0-9` + hyphens; no leading/trailing/consecutive hyphens |
| `description` | yes | ≤1024 chars. **What it does + when to use + verbatim user trigger phrases.** Missing description = skill not loaded. |
| `compatibility` | no | ≤500 chars, environment requirements |
| `license`, `metadata` | no | optional |
| `disable-model-invocation` | no | `true` = hidden from system prompt, only `/skill:name` works |

## Progressive disclosure (the core principle)

Only `name` + `description` are always in context. The agent reads SKILL.md on task match, and reads `references/` even later, only when needed. Consequences:

- **description is a router, not a summary** — it must contain enough signal to route correctly, including phrases users actually say.
- **SKILL.md is a workflow, not a manual** — imperative steps, exact commands. Split by kind, not count: reference material → `references/`, code → `scripts/`; the test is that a busy user skims the workflow in one sitting.
- **references/ is the manual** — specs, API details, edge cases, question banks.
- **scripts/ are the muscle** — deterministic work in code, not prose the agent improvises.

## Description formula

```
[What it does, concretely] + Use when [trigger conditions, files, user phrases in quotes].
```

Good: `Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents.`
Bad: `Helps with PDFs.`

## Good steps (what a well-written SKILL.md body looks like)

- `Run: ./scripts/convert.sh <in> <out>` — not "convert the input appropriately"
- Relative paths from the skill directory, e.g. `see [reference guide](references/REF.md)`
- Setup section for one-time init (`cd /path && npm install`)
- A "Never" guardrail list when safety matters

## Legal name check

Valid: `pdf-processing`, `code-review`, `skill-forge`
Invalid: `PDF-Processing`, `-pdf`, `pdf--processing`

## Secrets rule

A skill never contains credentials. Where any API is involved: the script reads tokens from environment variables or the user's keychain at runtime, SKILL.md names the required variable (never the value), and Guardrails includes "NEVER write, log, or commit secrets".

## Verify the loop is closed

Every reference in SKILL.md must resolve to an existing file. Every script must run. A skill that tells the agent to "improvise" a critical step is a 60-point skill.
