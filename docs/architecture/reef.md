# REEF Reference Architecture

## Role and status

REEF (Reusable Effort Estimation Framework) is the vendor-neutral reference implementation of the AI Effort Estimation Framework. It serves traditional, AI-assisted, and AI-native software and digital engineering engagements and makes the methodology executable without making application behavior the methodology.

The first implementation is a containerized, web-first proof of concept written in Python. It is an early-stage reference application, not a production service or a scientifically validated estimator. Step 0 of that implementation—the runnable application shell, SQLite readiness boundary, container packaging, and CI/release delivery baseline—is implemented.

## Architectural style

REEF starts as a modular monolith deployed as one application container:

```text
Browser
   │
   ▼
Web UI and HTTP API
   │
   ▼
Application services
   │
   ▼
Estimation domain core ───── Work, delivery, people, organization,
   │                         uncertainty, duration, and economics
   │
   ▼
Repository interfaces ───── SQLite reference adapter
```

This keeps the POC easy to run and demonstrate while preserving boundaries needed by later CLI, SDK, alternate-storage, and organization-specific implementations.

## Technology choices

- **Python** is the implementation language.
- **FastAPI** provides the web and HTTP API boundary.
- **Pydantic** provides typed application models and validation aligned with the public schemas.
- **Server-rendered templates, enhanced with HTMX where interactivity is needed,** provide the initial browser experience; a separate frontend application is not required for the POC.
- **SQLite** is the reference persistence adapter for local and single-instance evaluation.
- **pytest** provides unit, contract, integration, and end-to-end tests.
- **Docker** is the canonical POC packaging and execution boundary. The runtime should use a non-root user and externalized configuration.
- **`pyproject.toml`** is the canonical Python project and dependency configuration.

Specific dependency versions will be selected and locked during implementation. These choices do not become framework requirements.

## Delivery architecture

The repository uses GitHub Actions for continuous integration and release delivery. Pull requests and the default branch must pass Python quality checks, tests, public-schema example validation, an image build, and a live-container smoke test. Published GitHub releases produce multi-architecture OCI images in GitHub Container Registry with immutable version and source-revision tags, SBOM and provenance metadata, and a build attestation.

The registry is the Step 0 delivery boundary. Automatic deployment to a shared runtime is deferred until a hosting environment, identity boundary, secrets model, backup policy, and threat model are explicitly selected. Operational behavior and recovery constraints are documented in [`docs/operations/reef.md`](../operations/reef.md).

The `/product-experience` route is a presentation-only simulation used to validate the complete user journey before its domain behavior exists. Its structured content, server-rendered template, and static interaction assets may describe domain concepts but must not calculate or persist estimates. Production slices replace simulations behind stable user concepts rather than moving prototype logic into the domain.

## Planned module boundaries

```text
reef/
├── pyproject.toml
├── Dockerfile
├── compose.yaml
├── src/reef/
│   ├── domain/           Framework-aligned models and estimation behavior
│   │   ├── work/         Work packages, activities, roles, dependencies
│   │   ├── delivery/     Traditional and AI participation effects
│   │   ├── context/      People, organization, business, and evidence
│   │   ├── simulation/   Uncertainty and elapsed-duration behavior
│   │   └── commercial/   Cost and engagement-specific transformations
│   ├── application/      Pipeline use cases and transaction orchestration
│   ├── infrastructure/   Persistence and external adapters
│   └── web/              FastAPI routes, templates, and static assets
└── tests/                Unit, contract, integration, and end-to-end tests
```

The domain layer must not import FastAPI, templates, SQLite adapters, or organization-specific integrations. It consumes and emits versioned data compatible with the repository schemas.

## POC capabilities

The POC exposes browser and HTTP API workflows to run the canonical pipeline:

```text
Sanitized specification and context
              ↓
      Work decomposition
              ↓
 Reference PH by package/activity/role
              ↓
 Delivery-mode and explicit AI effects
              ↓
 People and organizational-friction model
              ↓
  Uncertainty propagation and risk reserve
              ↓
  Capacity/dependency duration simulation
              ↓
        Cost transformation
              ↓
 Engagement-specific commercial view
              ↓
 Evidence, confidence, lineage, and actuals
```

The pipeline is staged so that a user can inspect each transformation. It follows the [delivery-context contract](../framework/delivery-context.md) and [ADR-0001](decisions/0001-explicit-causal-drivers.md). P50 and P80 are produced only by an estimator with probabilistically meaningful outputs.

Calibration in the POC demonstrates versioning and comparison using synthetic actuals. Fitting and validating a real-world model remains outside the first interactive POC.

## Extension points

Planned interfaces include scope decomposers, effort estimators, factor catalogs, uncertainty models, duration simulators, cost models, engagement models, repositories, input/output adapters, identity providers, and reporters. Extensions must declare compatibility and may not silently reinterpret canonical fields or collapse distinct units.

An organization-specific product should be able to consume REEF as a Python package or implement the public contracts independently. Private authentication, infrastructure, delivery processes, integrations, data, and calibrated parameters do not belong in public REEF.

## Reproducibility and safety

Every estimate should identify the application, schema, scenario, component-model, and parameter versions plus a deterministic input digest and random seed where relevant. Logs must avoid source content, prompts, credentials, personal data, and confidential operational data by default. Calibration artifacts must retain lineage without embedding restricted observations. Case-study ingestion and fixtures must follow the [publication and sanitization contract](../case-studies/README.md#publication-and-sanitization-contract).

The POC is designed for local or controlled evaluation. Production concerns such as multi-tenancy, enterprise identity, high availability, and regulated-data operation require separate design and threat review.

## Future interfaces

A CLI, Python SDK, alternate UI, external database, and background processing may be added after the web workflow establishes useful domain behavior. They should reuse the same application and domain interfaces rather than fork estimation logic.
