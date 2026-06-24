# Search Strategy Reference

Use this when a research request is broad, vague, or likely to be answered poorly by a single search.

## Query expansion pattern

Start from the user's exact phrase, then expand across these dimensions:

1. **Concept**: synonyms, broader terms, narrower terms.
2. **Authority**: official, documentation, standard, manual, law, paper, dataset.
3. **Practicality**: guide, tutorial, case study, benchmark, postmortem, issue, troubleshooting.
4. **Negative evidence**: problems, limitations, mistakes, risks, deprecated, failure case, not working.
5. **Freshness**: latest, current year, version number, release name.
6. **Language**: Korean and English for Korean prompts unless local-only.

## Four-pass collection method

### Pass 1: Primary source

Goal: establish what is definitely true.

Search examples:

- `<topic> official documentation`
- `<topic> standard specification`
- `<topic> release notes latest`
- `<topic> law regulation official`
- `<topic> site:github.com <project> issue`

### Pass 2: Expert explanation

Goal: understand interpretation and best practice.

Search examples:

- `<topic> best practices`
- `<topic> maintainer explanation`
- `<topic> case study`
- `<topic> benchmark`
- `<topic> architecture guide`

### Pass 3: Field experience

Goal: find practical edge cases and what actually breaks.

Search examples:

- `<topic> reddit experience`
- `<topic> stackoverflow`
- `<topic> github issue workaround`
- `<topic> forum problem solution`
- `<topic> 후기 문제 해결`
- `<topic> 공략 팁 실전`

### Pass 4: Contradiction and risk

Goal: avoid giving confident but unsafe or outdated advice.

Search examples:

- `<topic> limitations`
- `<topic> deprecated`
- `<topic> failure case`
- `<topic> risk`
- `<topic> ban`
- `<topic> not recommended`
- `<topic> vs alternative`

## Korean-English bilingual strategy

For Korean user requests:

1. Search the original Korean query first to capture local terminology and context.
2. Translate the core concept into English and search official/global sources.
3. Compare Korean practical advice against English/official evidence.
4. If Korea-specific law, platform, product, geography, or culture matters, prioritize Korean official or primary sources.

## Evidence filtering

Keep a source only if it contributes at least one of these:

- authoritative fact
- current rule or specification
- reproducible method
- meaningful benchmark or data
- real-world failure case
- expert interpretation
- practical edge case
- direct comparison

Reject sources that merely repeat common claims without evidence.

## Minimum source set for substantial answers

For non-trivial research, aim for:

- 1-2 official or primary sources
- 1-2 expert or technical sources
- 1-3 community or field-experience sources when practical tactics matter
- 1 source showing limitations, risks, or disagreement

For low-stakes questions, fewer sources may be sufficient. For high-stakes questions, collect more and be explicit about uncertainty.
