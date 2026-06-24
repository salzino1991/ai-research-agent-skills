# AGENTS.md

## Project purpose

This repository stores reusable Codex Agent Skills for deep research, source collection, source scoring, and evidence-based strategy guides.

## Default response language

Use Korean by default when the user writes in Korean. Use English when the user writes in English or explicitly requests English.

## When to use the research skill

Use the `deep-research-collector` skill for requests that include or imply any of the following:

- 자료수집, 조사, 리서치, 근거 찾기
- 공략법, 전략, 최적 루트, best practice
- 비교, 추천, 랭킹, 장단점 분석
- source-backed answer, citations, evidence table
- troubleshooting where current documentation or community reports may matter

Do not use the skill for casual conversation, pure rewriting, translation, or tasks where the user already supplied all necessary source material.

## Research quality rules

- Prefer official, primary, and original sources first.
- Then use recognized expert, maintainer, vendor, field-practitioner, and community sources as supporting evidence.
- Search in both Korean and English for Korean user requests unless the topic is strictly local or language-specific.
- Distinguish fact, inference, opinion, and recommendation.
- State uncertainty, source conflicts, freshness limits, and assumptions explicitly.
- Cite sources when the active environment supports citations.
- Do not invent URLs, papers, quotes, dates, metrics, benchmarks, or source names.
- Avoid shallow link lists. Produce synthesized, actionable guidance.

## Repository conventions

- Skill packages live under `.agents/skills/<skill-name>/`.
- Every skill must contain `SKILL.md` with `name` and `description` metadata.
- Put long rubrics, templates, and background docs under `references/`.
- Put optional helper scripts under `scripts/`.
- Scripts must be optional; the skill should remain usable without running code.
- Never commit secrets, API keys, private personal data, or scraped copyrighted full text.
