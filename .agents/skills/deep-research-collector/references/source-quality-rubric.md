# Source Quality Rubric

Use this rubric to decide which sources deserve weight in a deep research answer.

## Reliability score

| Score | Label | Use case | Typical examples |
|---:|---|---|---|
| 5 | Primary / authoritative | Use as the backbone for factual claims. | Official docs, standards, laws, original papers, original datasets, maintainer release notes. |
| 4 | Expert / high-confidence secondary | Use for interpretation, implementation detail, and best practices. | Maintainer blog posts, recognized experts, vendor engineering posts, reproducible case studies, credible benchmarks. |
| 3 | Practical / field-tested | Use for tactics, edge cases, and experience reports after cross-checking. | Detailed forum posts, GitHub issues with reproduction, community guides with evidence, Stack Overflow answers with consensus. |
| 2 | Anecdotal / weak support | Use only as a lead or minor supporting context. | Personal blogs, old posts, unsourced opinions, incomplete comparisons. |
| 1 | Low trust / reject by default | Avoid unless discussing misinformation or bad advice. | SEO farms, copied content, promotional pages, AI-generated summaries without sources, fake benchmark pages. |

## Required checks

For every important source, check:

1. **Authority**: Who published it? Are they the primary party, a maintainer, a domain expert, or an unknown aggregator?
2. **Freshness**: Is the date/version appropriate for the question?
3. **Evidence**: Does it provide data, examples, reproducible steps, citations, or only assertions?
4. **Independence**: Is it independent from other sources, or does it copy the same claim?
5. **Bias**: Is the source selling something or incentivized to overstate benefits?
6. **Specificity**: Does it address the exact user question or only a broad neighboring topic?
7. **Risk**: Could following it cause legal, financial, safety, account-ban, security, or operational harm?

## Red flags

Down-rank or reject a source when it has any of these issues:

- no author, date, or source trail
- obvious SEO keyword stuffing
- no examples or verification path
- claims that conflict with official documentation
- outdated version or deprecated method
- hidden affiliate incentive or sales funnel
- copied wording across multiple sites
- sensational language without evidence
- unverifiable benchmark charts
- community advice that may violate terms of service or law

## Cross-checking policy

- One source is enough only for low-stakes background context or official primary facts.
- Two independent sources are preferred for technical, financial, legal, health, product, or current-event claims.
- Three or more sources are preferred when recommendations depend on conflicting practical experience.
- When sources disagree, report the disagreement instead of forcing a false consensus.

## Source type weighting

Use this general order unless the task requires otherwise:

1. Official / primary source
2. Standards, laws, academic papers, original datasets
3. Maintainer or recognized expert explanation
4. Reproducible benchmark or case study
5. Detailed issue thread or forum discussion
6. Community guide
7. Anecdote or opinion
8. SEO summary

## Final evidence test

Before finalizing the answer, ask:

- Would I trust this source enough to act on it?
- Can the user verify the claim independently?
- Is the source current enough?
- Did I distinguish evidence from interpretation?
- Did I disclose uncertainty and conflicts?
