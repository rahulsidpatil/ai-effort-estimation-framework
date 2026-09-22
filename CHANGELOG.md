# Changelog

All notable changes will be documented here. This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and intends to use [Semantic Versioning](https://semver.org/) once versioned releases begin.

## [Unreleased]

### Added

- Initial repository scaffold.
- Draft framework documentation and terminology.
- Draft project, estimate, and actuals schemas.
- REEF reference-implementation architecture.
- Research, evaluation, synthetic-data, governance, and community artifacts.
- Canonical product definition for the first REEF proof of concept.
- Runnable REEF Step 0 FastAPI web application with health and readiness endpoints.
- Locked Python development environment, automated tests, linting, and type checking.
- Hardened non-root container and persistent local Docker Compose workflow.
- GitHub Actions CI plus release-driven multi-architecture GHCR publication, SBOM, and provenance attestation.
- REEF configuration, operations, persistence, recovery, and release-verification guidance.

### Changed

- Reframed REEF as a containerized, web-first Python modular monolith.
- Selected FastAPI, Pydantic, server-rendered templates, SQLite, pytest, and Docker as POC technology choices.
- Defined the independence boundary between public REEF and future organization-specific implementations.

### Removed

- CLI-first direction and Go-shaped implementation placeholders.
