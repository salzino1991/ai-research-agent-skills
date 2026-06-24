---
name: deep-research-collector
description: Use for 자료수집, 공략법, deep research, strategy guides, best practices, comparison research, source-backed recommendations, and high-quality evidence gathering. Do not use for casual replies, pure rewriting, or tasks where the user already supplied all needed material.
---

# Deep Research Collector

## Purpose

Turn vague research requests into source-backed, practical, and decision-ready guides.

This skill is optimized for Korean and English requests such as:

- "공략법 찾아줘"
- "자료수집해줘"
- "최선의 방법 조사해줘"
- "근거 기반으로 비교해줘"
- "best practice 알려줘"
- "which option should I choose?"

## Operating principles

- Do not stop at one search query, one language, or one source type.
- Prefer primary, official, original, and recent sources.
- Use expert and community sources to understand practical field experience.
- Separate fact, inference, opinion, and recommendation.
- Explicitly mark uncertainty, conflicts, assumptions, and freshness limits.
- Do not fabricate sources, dates, URLs, papers, quotes, metrics, or citations.
- Avoid SEO-style summaries. Produce actionable guidance.

## Workflow

### 1. Define the research target

Before collecting sources, restate the target in one sentence.

Identify:

- domain and subdomain
- user goal
- target user level
- geography or language constraints
- time sensitivity
- desired output format
- decision criteria such as cost, speed, risk, legality, performance, or reliability

Ask a clarifying question only when a missing constraint would materially change the answer. Otherwise, proceed with explicit assumptions.

### 2. Build a multi-angle search plan

When web search, repository search, file search, or other retrieval tools are available, use at least four angles:

1. **Primary / official**: official documentation, standards, laws, manuals, publisher notes, release notes, academic papers, original datasets.
2. **Expert / practitioner**: recognized experts, maintainers, vendor technical posts, case studies, postmortems, conference talks.
3. **Community / field experience**: issue threads, forums, Reddit, Stack Overflow, GitHub discussions, Korean community posts, Naver/Velog/Tistory only when practical experience matters.
4. **Critical / negative**: failure cases, drawbacks, outdated methods, risks, bans, legal issues, counterarguments, and limitations.
5. **Freshness check**: add version, current year, release number, or "latest" when the topic may have changed.

For Korean requests, search both Korean and English unless the topic is strictly Korea-specific.

### 3. Capture source metadata

For each candidate source, record:

- title
- URL, repository path, file path, or other locator
- publisher or author
- publication date or last updated date when available
- source type
- main claim or evidence
- reliability score from 1 to 5
- why the source is included or rejected

### 4. Evaluate sources

Use `references/source-quality-rubric.md`.

Reject or down-rank sources that are:

- copied from other sites without attribution
- primarily promotional
- outdated for the question
- unsupported by evidence
- internally inconsistent
- low-effort SEO content
- generated summaries without visible source trail

Cross-check important claims with at least two independent sources when possible.

### 5. Synthesize findings

Do not summarize source-by-source. Group findings by principle, tactic, decision factor, or workflow stage.

For each recommendation, explain:

- what to do
- why it works
- evidence supporting it
- when it fails
- how to verify it

### 6. Produce the answer

Use this default structure unless the user requested another format:

1. Executive summary
2. Best answer / 공략 핵심
3. Step-by-step action plan
4. Evidence table
5. Source conflicts and uncertainty
6. Common mistakes / traps
7. Final recommendation
8. Follow-up research checklist

## Evidence table format

| Rank | Source | Type | Date | Reliability | Key evidence | Use in answer |
|---:|---|---|---|---:|---|---|

## Reliability scale

- **5**: primary source, official documentation, law/standard, peer-reviewed paper, original dataset, maintainer release note.
- **4**: recognized expert, maintainer explanation, vendor technical docs, high-quality benchmark, reproducible case study.
- **3**: practical guide with transparent evidence, credible community consensus, issue thread with maintainers or reproducible examples.
- **2**: anecdotal post, opinion article, old content with uncertain applicability, weakly sourced comparison.
- **1**: SEO farm, copied content, unsourced claim, disguised promotion, hallucination risk.

## Handling weak evidence

If evidence is weak or incomplete:

- say so directly
- give the best provisional answer
- label it as provisional
- list exactly what must be verified next

## Citation policy

When the active environment supports citations, cite every non-obvious factual claim and every source-derived recommendation. When citation support is not available, include source locators in the evidence table.
