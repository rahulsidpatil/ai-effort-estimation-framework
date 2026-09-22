# REEF Reference Architecture

## Role and status

REEF (Reusable Effort Estimation Framework) is the vendor-neutral reference implementation of the AI Effort Estimation Framework. It makes the methodology executable without making application behavior the methodology.

The first implementation is a containerized, web-first proof of concept written in Python. It is an early-stage reference application, not a production service or a scientifically validated estimator.

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
Estimation domain core ───── Framework schemas and model definitions
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

## Planned module boundaries

```text
reef/
├── pyproject.toml
├── Dockerfile
├── compose.yaml
├── src/reef/
│   ├── domain/           Framework-aligned models and estimation behavior
│   ├── application/      Use cases and transaction orchestration
│   ├── infrastructure/   Persistence and external adapters
│   └── web/              FastAPI routes, templates, and static assets
└── tests/                Unit, contract, integration, and end-to-end tests
```

The domain layer must not import FastAPI, templates, SQLite adapters, or organization-specific integrations. It consumes and emits versioned data compatible with the repository schemas.

## POC capabilities

The POC exposes browser and HTTP API workflows to:

1. create or import a project;
2. enter baseline PH by activity and describe AI participation;
3. validate input against the public contracts;
4. generate and save an explainable three-point PH estimate;
5. record actual PH; and
6. compare estimated and actual effort.

Calibration is represented in the architecture and contracts but is not required for the first interactive POC.

## Extension points

Planned interfaces include estimators, factor catalogs, repositories, input/output adapters, identity providers, and reporters. Extensions must declare compatibility and may not silently reinterpret canonical fields.

An organization-specific product should be able to consume REEF as a Python package or implement the public contracts independently. Private authentication, infrastructure, delivery processes, integrations, data, and calibrated parameters do not belong in public REEF.

## Reproducibility and safety

Every estimate should identify the application, schema, and model versions plus a deterministic input digest. Logs must avoid source content, prompts, credentials, personal data, and confidential operational data by default. Calibration artifacts must retain lineage without embedding restricted observations.

The POC is designed for local or controlled evaluation. Production concerns such as multi-tenancy, enterprise identity, high availability, and regulated-data operation require separate design and threat review.

## Future interfaces

A CLI, Python SDK, alternate UI, external database, and background processing may be added after the web workflow establishes useful domain behavior. They should reuse the same application and domain interfaces rather than fork estimation logic.
