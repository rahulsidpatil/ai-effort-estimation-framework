# REEF

REEF (Reusable Effort Estimation Framework) is the planned reference software implementation of the [AI Effort Estimation Framework](../docs/framework/vision.md).

> **Status:** Architecture and directory scaffold only. The CLI examples are a target interface, not currently available behavior.

## Responsibilities

REEF will validate framework documents, run interchangeable estimators, produce explainable PH ranges, compare estimates with observations, and execute reproducible calibration and evaluation workflows.

REEF does not define the meaning of canonical concepts independently. Normative methodology belongs under `docs/framework/`; shared data contracts belong under `schemas/`. Implementation-specific decisions belong here and in the [architecture document](../docs/architecture/reef.md).

## Planned layout

```text
reef/
├── cmd/reef/       CLI entry point
├── internal/       Private application and adapter code
├── pkg/            Reusable domain and extension APIs
├── configs/        Safe example configuration
└── tests/          Contract and end-to-end fixtures
```

The programming language and module boundaries will be confirmed with the first implementation proposal. Empty implementation areas currently contain README files so their intent is versioned.
