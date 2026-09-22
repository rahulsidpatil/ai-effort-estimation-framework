# REEF

REEF (Reusable Effort Estimation Framework) is the vendor-neutral reference software implementation of the [framework](../docs/framework/vision.md) for traditional, AI-assisted, and AI-native software and digital engineering engagements.

> **Status:** Step 0 delivery foundation implemented. The runnable web shell, SQLite readiness boundary, container packaging, automated validation, and release-image publication are in place. Estimation workflows remain to be implemented.

## Responsibilities

REEF will provide a containerized Python web application that validates framework documents, runs an inspectable estimation pipeline, produces explainable PH and duration distributions, derives separate economic and engagement views, stores estimates and observations, compares estimates with actuals, and supports reproducible evaluation and calibration workflows.

REEF does not define the meaning of canonical concepts independently. Normative methodology belongs under `docs/framework/`; shared data contracts belong under `schemas/`. Implementation-specific decisions belong here and in the [architecture document](../docs/architecture/reef.md).

The first POC is defined in [`docs/product/reef-poc.md`](../docs/product/reef-poc.md) and uses the synthetic [Case Study 001](../docs/case-studies/case-study-001-ai-native-domain-modernization.md). Its implementation architecture is defined in [`docs/architecture/reef.md`](../docs/architecture/reef.md).

## Planned Python layout

```text
reef/
├── pyproject.toml
├── Dockerfile
├── compose.yaml
├── src/reef/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   └── web/
└── tests/
```

The estimation domain remains independent of FastAPI, templates, and persistence. Public schemas are the interoperability boundary. CLI and SDK interfaces are later possibilities, not the primary POC experience.

## Run the Step 0 application

Docker is the canonical runtime:

```sh
cd reef
docker compose up --build
```

Open <http://localhost:8000>. The page identifies the build as the delivery foundation and does
not imply that estimation behavior is complete. See the [operations guide](../docs/operations/reef.md)
for configuration, health endpoints, persistence, release artifacts, and recovery constraints.

For Python development, install the locked environment and run the checks from `reef/`:

```sh
uv sync --frozen
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest
```

## Public-project boundary

REEF must not contain proprietary organization processes, private integrations, internal identity configuration, client or employee data, private source case studies, or privately calibrated models. An organization-specific implementation can depend on REEF or implement its public contracts while keeping those concerns private. Public case studies must follow the [sanitization contract](../docs/case-studies/README.md#publication-and-sanitization-contract).
