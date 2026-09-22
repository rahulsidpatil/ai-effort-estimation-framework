# Case Studies

Case studies exercise the framework with publishable scenarios. They are examples and evaluation fixtures, not evidence that an estimator is accurate.

## Publication and sanitization contract

Every case study in this repository must be synthetic or based on material explicitly licensed for public redistribution. A private source may inform only abstract estimation characteristics; it must never be copied, lightly edited, or retained in the repository.

Before publication:

1. create a new scenario from generic domain concepts rather than redacting a source document in place;
2. remove or replace all organization, client, product, program, vendor, employee, and partner names;
3. remove internal identifiers, URLs, email addresses, repository paths, account details, ticket references, screenshots, and document metadata;
4. replace architecture-specific names, technology mandates, system topology, security controls, business rules, data models, and integrations with generic or independently authored constructs;
5. synthesize quantities, dates, rates, volumes, service levels, productivity claims, staffing, and performance measures instead of perturbing confidential values;
6. exclude source text, diagrams, images, wireframes, code, prompts, generated outputs, and embedded files;
7. retain only estimation-relevant shapes such as the presence of multiple delivery stages, integration boundaries, migration, non-functional work, human approvals, or AI governance;
8. inspect version history, generated artifacts, fixtures, logs, and file metadata for leakage;
9. record a review statement and provenance class without naming or describing a restricted source; and
10. obtain an independent publication review before merging when any private material informed the abstraction.

Search-and-replace anonymization is insufficient. If a reviewer could plausibly infer the source organization, product, proprietary architecture, or internal operating profile, the case study is not safe to publish.

## Canonical artifacts

- [Case Study 001 — AI-Native Domain Modernization](case-study-001-ai-native-domain-modernization.md) is the canonical POC scenario.
- [Case-study template](template.md) defines the minimum structure and sanitization declaration for future scenarios.
