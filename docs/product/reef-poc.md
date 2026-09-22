# REEF Web POC

## Product decision

The first REEF proof of concept is a containerized, web-first Python application. Its purpose is to make the framework tangible, test the end-to-end estimation workflow with users, and validate the public contracts. It is not a production-ready enterprise platform or proof that the proposed estimation model is scientifically valid.

## Target user

The initial user is a software-delivery practitioner or researcher who wants to construct an explicit PH estimate, understand its assumptions and contributors, and later compare it with observed effort.

## Primary journey

1. Create a project in the browser or import a schema-compatible project document.
2. Enter baseline PH by delivery activity.
3. Record AI participation and selected context factors.
4. Review validation errors, assumptions, and warnings.
5. Generate an explainable lower, expected, and upper PH estimate.
6. Save and retrieve the estimate.
7. Record actual PH by activity after or during delivery.
8. View an estimate-versus-actual comparison.

## POC requirements

- A browser-based interface and documented HTTP API expose the same application use cases.
- Project, estimate, and actuals data conform to versioned public schemas.
- PH is the canonical effort unit throughout the domain and stored artifacts.
- The estimate retains its baseline, planning range, assumptions, model identity, warnings, and contribution breakdown.
- The application stores POC data through a repository abstraction with SQLite as the reference adapter.
- The complete POC runs as a container with externalized configuration and a non-root runtime user.
- Estimation logic remains testable without a web server or database.
- All bundled examples and fixtures are synthetic and safe to publish.
- The UI clearly states that initial coefficients and outputs are experimental and unvalidated.

## Acceptance criteria

The POC is complete when a new user can start it using the documented container workflow, complete the primary journey without editing source code, export or inspect schema-compatible artifacts, and see deterministic results for the same model version and inputs. Automated tests must cover domain behavior, schema compatibility, persistence, HTTP workflows, and the critical browser journey.

## Deferred

- Statistical calibration from real-world datasets.
- Multi-user collaboration and multi-tenancy.
- Enterprise authentication and authorization.
- Production-grade scalability, availability, and disaster recovery.
- Organization-specific delivery methods, integrations, or reporting.
- A dedicated JavaScript frontend application.
- CLI and SDK product experiences.

## Public and private boundary

Public REEF is independent and vendor-neutral. Future organization-specific tools may reuse the Python package, extend its interfaces, or independently implement its public schemas. Proprietary methods, internal systems, client data, employee data, private calibration parameters, and organization-specific branding remain outside this repository.
