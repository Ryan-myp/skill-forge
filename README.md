# skill-forge

A meta-skill for agent harnesses (Claude Code / pi / any Agent Skills-compatible harness) that creates **high-quality** skills instead of 60-point stubs.

The difference: it interviews first. It grills you about your real workflow (one question at a time, with recommended answers, exploring the environment instead of asking when it can), confirms a one-page spec, scaffolds a standards-compliant skill (`SKILL.md` + `scripts/` + `references/`), then runs the skill end-to-end on a minimal real task and gates it through a 5-axis quality rubric where the trigger test is confirmed by **you**, not the agent's self-grade. Below 80/100 means it's fixed before delivery. Two more modes: **porting** (an existing skill is the source of truth; license gate decides copy vs rewrite) and **wild-audit** (5 deterministic checks on a skill you already have — external surface, path truthfulness, domain traps, unbounded/destructive loops, version consistency — patch in place, no rebuild).

## Install

```bash
# Claude Code / OpenAI Codex / other Agent Skills harnesses
git clone https://github.com/Ryan-myp/skill-forge ~/.claude/skills/skill-forge

# pi (global)
git clone https://github.com/Ryan-myp/skill-forge ~/.agents/skills/skill-forge

# project-scoped
git clone https://github.com/Ryan-myp/skill-forge .agents/skills/skill-forge
```

## Use

Natural language — "make a skill for X", "turn my qguard workflow into a skill" — or force with:

```
/skill:skill-forge 把 weread 读书笔记导出流程做成 skill
```

## Structure

- `SKILL.md` — 7-step workflow + **porting mode** (existing skill as source, license gate) + **wild-audit mode** (5 deterministic checks on existing skills, patch in place)
- `references/interview.md` — grill question bank (B0 license, B1–B10 scope/triggers/mechanism, B5a/b/c audience & claims & craft notes with degradation + provenance tags)
- `references/rules.md` — 22 rules as one-line statements + the evidence chain behind each (incident → rule)
- `references/anatomy.md` — Agent Skills standard + description formula
- `references/template.md` — scaffold templates
- `references/quality-checklist.md` — 5-axis 0–100 rubric (A15+B25+C20+D15+E25)
- `scripts/trigger_score.py` — P/R/F1 trigger scorer with baseline delta
- `tests/` — per-skill trigger baselines (`tests/<skill>/prompts.json` + `baseline.json`)
- `TESTLOG.md` — 13-row incident→rule evidence chain (v0.1–v1.4), every rule traces to a real failure

## License

MIT
