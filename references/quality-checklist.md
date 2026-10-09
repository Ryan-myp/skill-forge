# Quality Gate (0–100)

Run after scaffolding, **before** user acceptance. Agent scores A/C/D/E; **B counts only after the user confirms the trigger simulation** (SKILL.md step 6) — the agent proposes, the user disposes. Below 80 total = fix and re-score.

## A. Standards compliance (15)
5 pts × 3:
1. frontmatter: `name` + `description` present; name legal (lowercase/digits/hyphens, ≤64, no edge/consecutive hyphens); description ≤1024 chars
2. every `[file](references/…)` / `./scripts/…` path in SKILL.md resolves to an existing file; every script executable and smoke-ran
3. directory under a valid skill location, name unique (no collision with `ls ~/.agents/skills/`); **dependency inventory with install commands** (grep the scripts for implicit imports — original docs lie); **license**: external content carries the original's `license:` field, proprietary code is rewritten not copied

## B. Trigger accuracy (25) — agent-proposed, **user-confirmed**
Simulate routing with 3 tasks and present the reasoning to the user:
1. Two tasks the skill SHOULD handle (paraphrased from the user's B2 phrases) — would the description plausibly cause loading?
2. One similar-but-different task it should NOT handle — is the description specific enough to avoid the false positive?
- 10/10/5 split. Vague descriptions ("helps with X") cap this axis at 5/10.
- **No points until the user confirms.** A missed confirmation is not a score — it's a fail state back to SKILL.md step 2, open branches only.

## C. Executability (20)
- 10 pts: each workflow step is imperative with an exact command/decision rule. Any "as appropriate", "handle sensibly", "generally" → 0 for that step; 10 × (non-improvising steps ÷ total steps).
- **Pure-craft skills (no scripts)**: executability is carried by *checkable anchors* instead — an anti-cliché checklist, a self-critique pass with an observable output (screenshot, diff, re-read). A craft skill whose steps end in "be original" has no anchor: 0 on this sub-axis.
- 10 pts: **end-to-end trial performed** — the skill was invoked on the smallest plausible real task and completed (trial artifacts exist: output files, command logs). Trial not run = 0/10.

## D. Progressive disclosure & coverage (15)
- 5: SKILL.md skimmable in one sitting; depth correctly offloaded to `references/`
- 5: no step pushes a critical decision onto improvised prose
- 5: **script documentation coverage** — `ls scripts/` matches the documented command surface 1:1; an undocumented script = 0/5

## E. Safety, content & closure (25)
- 5: Guardrails present where mutations/deletes/credentials/network are involved; **interactive skills: each user gate carries a checkable exit condition + a decline path (B11)**
- 5: **secrets rule** — no credential value in any skill file; when an API is involved, SKILL.md names the env var/keychain source and Guardrails forbids writing/logging secrets
- 5: **claim traceability** (B5b) — no unlabeled invented specifics in the trial artifact; a 示例/假设-or-source rule exists in the skill
- 5: **craft notes** (B5c) — domain heuristics captured with what+why, not just process steps; 0 if the artifact's quality ceiling depends on unrecorded domain knowledge; **a craft note without a degradation path (what to do when the heuristic can't apply) also scores 0** — it will be violated at the topic boundary where it stops fitting
- 5: success criteria (B9) verifiable **and** the trial output actually matched them

## Deliverable format

Report the five axis scores (B marked "pending user confirmation" if not yet confirmed) + total + list of failed items. Fix fails, re-score, then walk SKILL.md steps 6 → 7: acceptance artifacts to the user, then handoff (location, `/skill:<name>` + natural-language trigger, one test phrase).
