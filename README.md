# AI Effort Estimation Framework

An extensible, open-source framework for estimating, tracking, evaluating, and continuously calibrating traditional, AI-assisted, and AI-native software and digital engineering engagements.

> **Project status:** Early-stage proposal and reference implementation. The concepts, equations, schemas, and software in this repository are drafts for research and community evaluation; they are not a finalized or scientifically validated estimation model.

## What is in this repository?

This repository deliberately keeps two related concerns separate:

- **The AI Effort Estimation Framework** defines the methodology, terminology, data contracts, calibration approach, and evaluation protocol.
- **REEF (Reusable Effort Estimation Framework)** is the reference software implementation of that framework, under [`reef/`](reef/README.md).

They live together while the proposal evolves so that changes to the methodology can remain traceable to schemas, examples, experiments, and implementation behavior.

## Guiding principles

- **Person-Hours (PH)** is the canonical effort unit. A PH is one hour of human effort, regardless of calendar duration or team composition.
- Effort, elapsed duration, cost, price, and commercial risk are distinct outputs connected by explicit transformations.
- Estimates are ranges with assumptions and uncertainty, not promises or single-point truths.
- AI can reduce, shift, or add effort. Review, verification, integration, governance, and rework remain visible.
- People, organizational friction, business context, and engagement model are first-class inputs.
- Causal drivers remain explicit; aggregate coefficients may summarize them but may not replace or hide them.
- Estimates should improve through observations and calibration, not undocumented intuition.
- Inputs, transformations, outputs, and model versions should be auditable.
- Extension points should allow different organizations and research groups to test alternative models without changing the core contracts.
- Public artifacts must not contain proprietary, confidential, client-specific, or personally identifiable information.

## Repository map

```text
.
├── docs/framework/          Canonical framework proposal
├── docs/architecture/       REEF reference architecture
├── docs/product/            REEF product scope and acceptance criteria
├── schemas/                 Draft interoperable data contracts
├── examples/                Illustrative, non-production inputs
├── datasets/synthetic/      Safe synthetic observations
├── research/                Hypotheses, experiments, and evaluation protocols
├── reef/                    Containerized reference web application
└── .github/                 Community health and contribution templates
```

Start with the [framework specification index](docs/framework/README.md), [terminology](docs/framework/terminology.md), and [estimation model](docs/framework/estimation-model.md). The [roadmap](ROADMAP.md) describes the path from proposal to evaluated releases.

## REEF direction

REEF begins as a containerized, web-first Python application. The first proof of concept is a modular monolith with a browser interface and HTTP API around an interface-independent estimation domain.

The initial user journey is built around the fully synthetic [Case Study 001 — AI-Native Domain Modernization](docs/case-studies/case-study-001-ai-native-domain-modernization.md). A user imports or decomposes scope, describes the delivery system, people, organizational constraints, business context, uncertainty, evidence, and engagement model, then generates an explainable estimate that keeps PH, duration, economics, and commercial exposure separate. See the [REEF POC definition](docs/product/reef-poc.md), [delivery-context model](docs/framework/delivery-context.md), and [reference architecture](docs/architecture/reef.md).

CLI and SDK interfaces may be added later, but they are not the primary POC experience.

The REEF Step 0 delivery foundation is runnable with Docker Compose and validated through GitHub
Actions. See the [REEF README](reef/README.md) to run it and the
[operations guide](docs/operations/reef.md) for its delivery and runtime contract.

The presentation-only [REEF product experience](docs/product/reef-product-experience.md) lets
estimation and delivery practitioners evaluate the intended journey before estimation logic is
implemented.

## Public-project boundary

REEF is an independent, vendor-neutral open-source reference implementation. Organization-specific products may adopt or extend its public methodology and contracts, but proprietary processes, data, integrations, identity systems, and calibrated models remain outside this repository.

## Contributing

Contributions to the methodology, schemas, datasets, evaluation design, documentation, and REEF are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

For security-sensitive reports, follow [SECURITY.md](SECURITY.md).

## License

Licensed under the [Apache License 2.0](LICENSE).
