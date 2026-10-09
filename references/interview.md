# Interview Branches

Decision tree for the grill phase. Resolve each branch. Ask **one question at a time**, each with a recommended answer. Skip any question the environment already answers — explore first, ask only what you can't derive.

## B1. Scope
- Single task, or a family of related tasks?
- **Decides**: one skill vs. one skill with subcommands/args.
- Recommended default: one coherent workflow per skill; split only when triggers differ.
- *Skip if*: the user described exactly one input→output.

## B2. Trigger (most important — feeds the description)
- What does the user actually say/type before they'd want this?
- What file types, directory layouts, or repo states indicate the task is present?
- **Decides**: description wording. Collect 2–3 verbatim user phrases; these go into the skill's description.
- *Skip if*: user already quoted how they ask ("when I say 'grill me'…").

## B3. Automation level
- Fully autonomous, or must confirm before side effects (writes, deletes, network, spend)?
- **Decides**: where checkpoints go in the workflow.
- Recommended default: read-only steps auto; any mutation outside the target directory requires confirmation.
- *Skip if*: task is purely read-only or user explicitly wants fire-and-forget.

## B4. Execution mechanism
- Pure prompt instructions, helper scripts, or wrapping an existing CLI/tool?
- **Decides**: `scripts/` content and setup section.
- *Explore first*: check whether the user already has scripts, CLIs, or a repo this skill should wrap. If it exists, the skill should invoke it, not reinvent it.
- Recommended default: wrap existing tooling in thin, tested scripts; prompt-only when no tooling exists.

## B5. Inputs / outputs
- Exact data in (paths, formats, encodings) and artifact out (files, reports, commits)?
- **Decides**: usage examples in SKILL.md.
- *Skip if*: user showed a concrete example end-to-end.

## B6. Environment & credentials
- OS, language/runtime, dependencies? For any external API: where do credentials live today, and where should the skill read them from?
- **Decides**: `compatibility` frontmatter, Setup section, and the Guardrails secrets rule.
- *Explore first*: run `which`/version checks on needed binaries; check for existing config.
- **Never invent or persist secrets**: scripts read tokens from environment variables or the user's keychain at runtime; SKILL.md names the required variable, never its value.
- *Skip if*: skill is fully local with no external API.

## B7. Failure modes
- What can fail (auth expired, missing file, API down, partial state)? What should the skill do: retry, abort cleanly, or fall back?
- **Decides**: error-handling steps in the workflow.
- Recommended default: fail fast with a clear message; no silent fallbacks.

## B8. Reference material
- Which docs/charts/scripts exist that the skill should link to (progressive disclosure) instead of inlining?
- **Decides**: `references/` content.
- *Explore first*: look in the user's repo for READMEs, docs/, man pages of wrapped tools.

## B9. Success criteria
- How does the user know a run succeeded? (exit code, file diff, screenshot, metric)
- **Decides**: the verify step of the generated skill and the test phrase for handoff.
- *Skip if*: output is a deterministic file with obvious check.

## B10. Guardrails
- What must this skill NEVER do (touch prod, delete, spend money, **write or commit secrets**)?
- **Decides**: explicit "Never" section in the generated SKILL.md.
- Recommended default: inherit the host project's critical rules (secrets, injection, deletes) + B6's secrets rule.

## Termination & budget

- **Hard cap: 10 questions total.** Branches answered by exploration don't count, but anything still open at question 10 is resolved with your recommended defaults, listed as explicit assumptions in the spec, and the user approves once.
- **Order by blast radius**: B1 (scope forks — e.g. 公众号 vs 企业微信) first, then B2 (triggers), then B4 (execution mechanism) — these three decide the whole shape. B5/B6/B7 next; B8/B9/B10 last.
- If the user says "stop asking, just build it", immediately fold all remaining branches into the spec as assumptions.

Stop when B1–B10 are resolved (asked or answered by exploration). Then move to spec confirmation. If the user says "just build it" early, resolve the open branches yourself with recommended defaults, list your assumptions in the spec, and get one approval.
