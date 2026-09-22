# Roadmap

This roadmap is directional. Milestones may change as evidence and community feedback improve the proposal.

## Phase 0 — Proposal and contracts

- Establish scope, terminology, principles, and canonical PH unit.
- Publish draft project, estimate, and actuals schemas.
- Define reproducible synthetic examples and an evaluation protocol.
- Record hypotheses and known limitations.

## Phase 1 — Containerized REEF web POC

- Establish the Python package and domain/application boundaries.
- Implement the FastAPI web and HTTP API adapters.
- Provide a server-rendered project, estimation, actuals, and comparison journey.
- Persist POC data through a repository interface with a SQLite adapter.
- Package the application as a non-root Docker container with a documented local startup workflow.
- Emit schema-compatible artifacts with model and schema versions.
- Add domain, contract, persistence, HTTP, and critical-browser-journey tests.
- Preserve extension points for estimators, repositories, identity providers, and import/export adapters.

## Phase 2 — Observation and evaluation maturity

- Harden actual-effort ingestion, including schema-compatible bulk import and scope-change handling.
- Expand estimate-versus-actual analysis beyond the POC comparison view.
- Add data-quality checks and privacy-preserving aggregation guidance.
- Report error, bias, interval coverage, and cohort metrics.

## Phase 3 — Calibration experiments

- Implement versioned, reversible calibration workflows.
- Evaluate calibration on synthetic and consented public datasets.
- Publish model cards, benchmark limitations, and reproducibility artifacts.

## Phase 4 — Community validation

- Invite independent replication and alternative estimator plug-ins.
- Stabilize schemas based on interoperability experience.
- Define release maturity and compatibility guarantees.

## Explicitly out of scope for early releases

- Claims of universal productivity improvement from AI.
- Automated employee performance scoring or surveillance.
- A single authoritative model for all organizations or delivery contexts.
- Ingestion of proprietary or client-specific data into this repository.
- Enterprise-specific identity, processes, infrastructure, integrations, branding, or calibrated models.
- Production multi-tenancy, high availability, and regulated-data operation in the initial POC.
