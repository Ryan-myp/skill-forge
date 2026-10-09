# Scaffold Template

Fill per confirmed spec, then create at `~/.agents/skills/<name>/` (global) or `<repo>/.agents/skills/<name>/` (project).

## SKILL.md skeleton

````markdown
---
name: <name>
description: <what it does, concretely>. Use when <trigger conditions, file types, verbatim user phrases in quotes>.
# license: <MIT/Apache-2.0/…>   # required when the skill wraps or adapts external content; proprietary → rewrite, don't copy
---

# <Skill Name>

## Setup (if any one-time init)

```bash
# full dependency inventory: npm/python modules + system binaries, each with its install command
```
```bash
cd <skill-dir> && <init command>
```

## Workflow

### 1. <Step>
<imperative, exact command or decision rule>

### 2. <Step>
...

## Guardrails

- NEVER <forbidden action>
- NEVER write, log, or commit secrets (API tokens come from <env var name / keychain>)   # only when an external API is involved
- EVERY number or example in the artifact carries a source or a 示例/假设 label   # when B5b applies

## References
- <one-line pointer>: [detail](references/<file>.md)
````

## Directory layout

```
<name>/
├── SKILL.md
├── scripts/
│   └── <tool>.<ext>       # executable, smoke-tested
├── references/
│   └── <topic>.md         # loaded only when a step says so
└── assets/
    └── <template>.<ext>
```

## Craft notes (when B5c resolved anything)

- <what>: <one line of why> · **if it can't apply: <degradation path>**   # e.g. "角度要反直觉优先 — 套路三件套读者刷到第二就猜到；题材没反直觉空间时降级为一个尖锐具体的可检查事实"

## Rules when filling

1. Spec frontmatter must carry: **audience** (B5a, tone follows it), **data sources** (B5b allowed list), **craft notes** (B5c), in addition to name/description/workflow/scripts/references.
2. B5a/B5b/B5c answers become *content* rules in the generated SKILL.md, not just process rules — they are what separate a 60-point artifact from an 80-point one.

1. SKILL.md body = workflow only, skimmable in one sitting. No line quota — split by kind: reference material → `references/`, code → `scripts/`.
2. Each step = one imperative sentence + one command. No "as appropriate", no "handle errors sensibly".
3. Every file referenced must be created in the same pass.
4. Every script: `chmod +x` + run once with a sample input; capture the exact output shape into the SKILL.md usage line.
5. Keep the description under 1024 chars; the last sentence should be a `Use when …` with user phrases.
