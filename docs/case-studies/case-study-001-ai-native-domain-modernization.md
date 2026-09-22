# Case Study 001 — AI-Native Domain Modernization

> **Status:** Canonical REEF POC scenario; synthetic specification to be developed
>
> **Provenance class:** Estimation characteristics abstracted into a newly authored scenario; no source content retained
>
> **Evidence status:** Suitable for workflow and model-mechanics testing, not for real-world accuracy claims

## POC research question

Can REEF derive a transparent, reproducible, and continuously refinable estimate from a specification for an AI-native software delivery engagement while keeping effort, duration, economics, and commercial exposure distinct?

## Synthetic scenario

A generic organization is replacing a mature, tightly coupled business capability with a modular service-based platform. The POC scope contains several domain slices, user and API interactions, asynchronous integration boundaries, data migration, security and resilience obligations, deployment foundations, and operational readiness. Delivery is specification-driven and uses governed AI agents within explicit human approval and verification boundaries.

The scenario is intentionally independent of any real organization, product, system, or proprietary architecture. Its eventual detailed specification must be authored from the [case-study template](template.md) and pass the [publication and sanitization contract](README.md#publication-and-sanitization-contract).

## Synthetic work model

The POC should decompose at least these estimation shapes:

1. **Foundation and delivery harness:** repository structure, engineering standards, specification and evaluation harness, CI/CD, environments, observability, and shared controls.
2. **Domain slices:** several independently named synthetic capabilities, each spanning presentation or consumer interfaces, service/API behavior, domain logic, persistence, tests, and integration.
3. **Read and query capabilities:** search, detail, history, and export patterns with distinct performance and data-access concerns.
4. **Integration:** inbound and outbound asynchronous flows, contracts, failure handling, replay or recovery, and dependency coordination.
5. **Migration:** discovery, mapping, rehearsal, reconciliation, cutover, fallback, and acceptance evidence.
6. **Cross-cutting quality:** security, privacy, performance, resilience, accessibility where applicable, auditability, and test automation.
7. **Release and operational readiness:** deployment, monitoring, runbooks, support transition, reliability work, and acceptance.

Detailed feature names, counts, technologies, volumes, metrics, and rules must be newly synthesized. The POC should use enough variation to exercise estimation behavior without imitating a private source.

## Required inputs

- sanitized synthetic specification and acceptance boundaries;
- work packages, dependencies, complexity drivers, and non-functional obligations;
- traditional reference mode and activity-level AI-native delivery assumptions;
- role mix, skill and familiarity bands, availability, ramp-up, and calendars;
- onboarding, provisioning, approvals, governance, collaboration, external dependencies, queues or windows, and environment constraints;
- business criticality, ambiguity, stakeholder and change context;
- evidence references, strength, uncertainty distributions, correlations, and explicit unknowns;
- T&M and Fixed Bid views for the build phase, plus a distinct Managed Service or SRE transition and steady-state view; and
- rates and other economic assumptions supplied only as synthetic scenario data.

## Required pipeline behavior

REEF ingests and validates the scenario, decomposes the specification into work, estimates reference PH, models activity-level AI effects, applies people and organizational constraints, propagates uncertainty, simulates elapsed duration, derives cost, and then applies the selected engagement model. Every stage retains assumptions, evidence, model identity, and causal contributions.

## Required outputs

The POC result must include:

- total PH and PH by role, activity, and work package;
- P50 and P80 effort with their statistical meaning;
- elapsed-duration distribution and critical constraints, separate from PH;
- organizational-friction impact split into added PH, capacity loss, and wait or queue time;
- gross AI benefit, AI-induced overhead, and net AI effect;
- explicit risk reserve and dominant risk contributions;
- cost view and engagement-specific commercial view, including commercial-risk ownership;
- assumptions, exclusions, warnings, confidence rationale, and evidence register; and
- model, schema, scenario, and input versions sufficient for reproduction.

Outputs must prefer honest ranges and traceable explanations over false precision.

## Actuals and evolution-aware calibration

The scenario will include synthetic actuals generated independently of the estimator. Observations will record actual PH, elapsed time, realized friction, dependency and approval latency, AI use and correction effort, scope changes, cost outcomes, and evidence quality.

Calibration compares estimate-time assumptions with observed context. Changes in AI models, tools, specifications, team composition, organization policy, environments, or delivery practices form a new cohort or model context rather than silently rewriting history. A new calibrated model must be versioned, evaluated on later held-out observations, and compared with both a simple baseline and the prior model.

## POC acceptance evidence

The case succeeds as a POC when a user can reproduce the estimate, inspect the causal chain for material outcomes, compare delivery and engagement modes without conflating their semantics, record synthetic actuals, and explain how those observations would affect a future model version. It does not succeed merely by producing a plausible single number.
