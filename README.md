# ai-research-agent-skills

Reusable agent skills for deep research, source collection, source scoring, and evidence-based strategy guides.

## Purpose

This repository gives Codex a repeatable research workflow for requests such as:

- 공략법 찾아줘
- 자료수집해줘
- 근거 기반으로 비교해줘
- best practice 조사해줘
- 최신 자료 기반으로 추천해줘

The goal is to make AI research less shallow by forcing a multi-source, multi-angle workflow: official sources, expert sources, community field experience, counterexamples, freshness checks, source scoring, and uncertainty reporting.

## Included skill

### `deep-research-collector`

Use this skill when the user asks for deep research, strategy guides, source-backed recommendations, comparison research, or high-quality 자료수집.

It helps the agent:

- expand vague research requests into concrete search plans
- search from official, expert, community, and negative-evidence angles
- score source quality from 1 to 5
- reject low-quality SEO or copied sources
- synthesize findings into actionable guidance
- produce evidence tables and clear recommendations
- state conflicts, assumptions, and uncertainty

## Repository structure

```text
ai-research-agent-skills/
  AGENTS.md
  README.md
  .agents/
    skills/
      deep-research-collector/
        SKILL.md
        references/
          source-quality-rubric.md
          search-strategy.md
          report-template.md
        scripts/
          source_table.py
```

## How to use with Codex

1. Open this repository in Codex, Codex CLI, or the Codex IDE extension.
2. Start from the repository root or a subdirectory under it.
3. Ask for the skill explicitly, or use a request that matches the skill description.

Example prompts:

```text
Use the deep-research-collector skill to find the best strategy for <topic>. Include official sources, expert sources, community experience, risks, and an evidence table.
```

```text
공략법 찾아줘. deep-research-collector 스킬을 사용해서 공식 자료, 실전 커뮤니티 팁, 실패 사례, 최신성 검증까지 포함해줘.
```

```text
A/B/C를 비교 조사해줘. 근거표, 신뢰도 점수, 최종 추천까지 정리해줘.
```

## How to reuse in another repository

Copy this folder into the target repository:

```text
.agents/skills/deep-research-collector/
```

Also copy or adapt `AGENTS.md` if you want repository-level guidance that tells Codex when to use the skill.

## Important note

This skill does not magically grant internet access. It improves the agent's research protocol when the active environment has web search, repository search, file search, connectors, or other retrieval tools available. Without retrieval access, it still helps structure the answer but cannot verify current facts.

## Official references

- Codex Agent Skills: https://developers.openai.com/codex/skills
- Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md

## License

MIT
