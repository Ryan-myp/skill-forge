# Scaffold Template

Fill per confirmed spec, then create at `~/.agents/skills/<name>/` (global) or `<repo>/.agents/skills/<name>/` (project).

## SKILL.md skeleton

````markdown
---
name: <name>
description: <what it does, concretely>. Use when <trigger conditions, file types, verbatim user phrases in quotes>.
---

# <Skill Name>

## Setup (if any one-time init)

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

## Rules when filling

1. SKILL.md body target: **≤ ~100 lines**. Over → split into `references/`.
2. Each step = one imperative sentence + one command. No "as appropriate", no "handle errors sensibly".
3. Every file referenced must be created in the same pass.
4. Every script: `chmod +x` + run once with a sample input; capture the exact output shape into the SKILL.md usage line.
5. Keep the description under 1024 chars; the last sentence should be a `Use when …` with user phrases.
