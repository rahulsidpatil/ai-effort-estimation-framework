# REEF Reference Architecture

## Role

REEF (Reusable Effort Estimation Framework) is the reference implementation of the AI Effort Estimation Framework. It should make the methodology executable without making the software itself the methodology.

```text
Framework docs ── define meaning and rules
      │
Schemas ───────── define interoperable contracts
      │
REEF core ─────── validates, estimates, compares, calibrates
      │
CLI / API / SDK ─ expose workflows
      │
Artifacts ─────── versioned estimates, observations, evaluations
```

## Architectural boundaries

- `cmd/` contains thin user-facing command wiring.
- `internal/` contains application orchestration and private adapters.
- `pkg/` contains stable, reusable domain types and extension interfaces when they emerge.
- `configs/` contains non-secret example configuration.
- `tests/` contains contract, integration, and end-to-end fixtures.

The domain core should not depend on CLI presentation, storage vendors, telemetry vendors, or a specific estimator. It consumes and emits documents conforming to the repository schemas.

## Target commands

- `reef init`: create a documented project template.
- `reef validate`: validate inputs and report precise diagnostics.
- `reef estimate`: create a versioned, explainable PH estimate.
- `reef compare`: compare an estimate with actual PH.
- `reef calibrate`: produce a versioned candidate model from observations.

## Extension points

Planned extension interfaces include estimators, factor catalogs, input/output adapters, storage backends, and reporters. Plug-ins must declare compatibility and may not reinterpret canonical fields silently.

## Reproducibility and safety

Every result should identify tool, schema, and model versions plus a deterministic input digest. Logs should avoid source content, prompts, credentials, and personal data by default. Calibration artifacts must retain lineage without embedding restricted observations.

## Evolution

The initial implementation should be a small CLI and domain core. Network services, persistent backends, and user interfaces should be added only when validated workflows require them.
