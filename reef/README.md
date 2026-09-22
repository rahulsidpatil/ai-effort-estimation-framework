# REEF

REEF (Reusable Effort Estimation Framework) is the planned vendor-neutral reference software implementation of the [AI Effort Estimation Framework](../docs/framework/vision.md).

> **Status:** Architecture and product definition only. The planned web application is not implemented yet.

## Responsibilities

REEF will provide a containerized Python web application that validates framework documents, runs interchangeable estimators, produces explainable PH ranges, stores estimates and observations, compares estimates with actuals, and supports reproducible evaluation workflows.

REEF does not define the meaning of canonical concepts independently. Normative methodology belongs under `docs/framework/`; shared data contracts belong under `schemas/`. Implementation-specific decisions belong here and in the [architecture document](../docs/architecture/reef.md).

The first POC is defined in [`docs/product/reef-poc.md`](../docs/product/reef-poc.md). Its implementation architecture is defined in [`docs/architecture/reef.md`](../docs/architecture/reef.md).

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

## Public-project boundary

REEF must not contain proprietary organization processes, private integrations, internal identity configuration, client or employee data, or privately calibrated models. An organization-specific implementation can depend on REEF or implement its public contracts while keeping those concerns private.
