# skill-forge

A meta-skill for agent harnesses (Claude Code / pi / any Agent Skills-compatible harness) that creates **high-quality** skills instead of 60-point stubs.

The difference: it interviews first. It grills you about your real workflow (one question at a time, with recommended answers, exploring the environment instead of asking when it can), confirms a one-page spec, scaffolds a standards-compliant skill (`SKILL.md` + `scripts/` + `references/`), then runs the skill end-to-end on a minimal real task and gates it through a 5-axis quality rubric where the trigger test is confirmed by **you**, not the agent's self-grade. Below 80/100 means it's fixed before delivery.

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

- `SKILL.md` — 6-phase workflow: restate → grill → spec approval → scaffold → quality gate → handoff
- `references/interview.md` — 10-branch question bank (incl. B5a audience, B5b claim traceability, B5c craft notes with degradation paths)
- `references/anatomy.md` — Agent Skills standard + description formula
- `references/template.md` — scaffold templates
- `references/quality-checklist.md` — 0–100 scoring rubric

## License

MIT
