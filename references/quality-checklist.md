# Quality Gate (0–100)

Run after scaffolding, before delivery. **Below 80 = fix and re-score.**

## A. Standards compliance (25)
- [x]-level checks, 5 pts each:
  1. frontmatter: `name` + `description` present; name legal (lowercase/digits/hyphens, ≤64, no edge/consecutive hyphens)
  2. description ≤1024 chars
  3. every `[file](references/…)` / `./scripts/…` path in SKILL.md resolves to an existing file
  4. every script is executable and smoke-ran successfully at least once
  5. directory under a valid skill location, name unique (no collision with `ls ~/.agents/skills/`)

## B. Trigger accuracy (30) — the description is the router
Simulate routing with 3 tasks:
1. Two tasks the skill SHOULD handle (paraphrased from the user's B2 phrases) — would the description plausibly cause the agent to load it?
2. One similar-but-different task it should NOT handle — does the description stay specific enough to avoid false positives?
- 10 pts per task, award proportionally. Vague descriptions ("helps with X") cap this axis at 5/10.

## C. Executability (25)
For each workflow step:
- Is it imperative with an exact command/decision rule? (scored)
- Any step that says "as appropriate", "handle sensibly", "generally" → 0 for that step; the agent must never improvise a critical path.
- 25 × (non-improvising steps ÷ total steps)

## D. Progressive disclosure (10)
- SKILL.md body ≤ ~100 lines and readable in < 30 s: 5
- deep detail correctly offloaded to references/ (no 200-line SKILL.md): 5

## E. Safety & closure (10)
- Guardrails present where mutations/deletes/credentials/network are involved: 5
- success criteria verifiable (exit code, artifact, diff) — user can confirm a run worked: 5

## Deliverable format

Report the five scores + total + list of failed items. Fix fails, re-score, then handoff per SKILL.md step 6: location, `/skill:<name>` + natural-language trigger, one test phrase to try immediately.
