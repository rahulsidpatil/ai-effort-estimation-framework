# REEF POC

## Product decision

The first REEF proof of concept is a containerized, web-first Python application built around the fully synthetic [Case Study 001 — AI-Native Domain Modernization](../case-studies/case-study-001-ai-native-domain-modernization.md). Its purpose is to make the broader framework tangible, test an end-to-end estimation workflow, and validate public contracts for traditional, AI-assisted, and AI-native software and digital engineering engagements.

The case study preserves only generic estimation characteristics such as staged modernization, multiple work types, integration boundaries, migration, non-functional obligations, governed AI use, and human approval. It contains no copied or lightly anonymized private content. The POC is not a production-ready enterprise platform or proof that the proposed estimation model is scientifically valid.

## Target user

The primary construction user is an estimation lead, solution architect, or accountable delivery lead who must produce a defensible estimate under time pressure and incomplete information. Engineering and delivery contributors supply context; engineering and delivery reviewers challenge the estimate; commercial leads derive engagement views; delivery leads record actuals; and researchers or model owners evaluate learning. These roles, their jobs, and their handoffs are defined in the [REEF product experience](reef-product-experience.md).

## Primary journey

1. Create a project in the browser or import a schema-compatible, sanitized project document.
2. Decompose the specification into work packages, activities, roles, dependencies, and acceptance evidence.
3. Declare the reference mode and traditional, AI-assisted, or AI-native participation by activity.
4. Describe people, organizational friction, business context, uncertainty, evidence, and engagement assumptions.
5. Review validation errors, assumptions, unknowns, and warnings.
6. Generate an explainable PH distribution and duration simulation.
7. Inspect role and work-package effort, P50/P80, organizational effects, AI gross benefit and induced overhead, risk reserve, cost, and commercial views.
8. Save, retrieve, and reproduce the estimate.
9. Record actual PH, duration, realized context, and scope change during or after delivery.
10. Compare estimate with observations and show how future calibration would respond without altering the original record.

## POC requirements

- A browser-based interface and documented HTTP API expose the same application use cases.
- Project, estimate, and actuals data conform to versioned public schemas.
- PH is the canonical effort unit throughout the domain and stored artifacts.
- Effort, elapsed duration, cost, price, and commercial risk remain separate, named outputs.
- The estimate retains reference PH, P50/P80, assumptions, evidence, confidence rationale, model identity, warnings, and causal contribution breakdown.
- Delivery inputs cover the six estimation planes: work, delivery system, people, organization, business context, and uncertainty/evidence.
- Organizational friction explicitly covers onboarding, provisioning, approvals, governance, collaboration overhead, external dependencies, queue or wait time, and environment constraints.
- AI outputs separate gross benefit from specification, orchestration, review, verification, correction, governance, and recovery overhead.
- T&M, Fixed Bid, and Managed Service/SRE views transform a shared engineering estimate rather than redefine it.
- The estimator exposes PH by role, activity, and work package, plus duration constraints and risk reserve.
- The application stores POC data through a repository abstraction with SQLite as the reference adapter.
- The complete POC runs as a container with externalized configuration and a non-root runtime user.
- Estimation logic remains testable without a web server or database.
- All bundled examples and fixtures are synthetic, independently authored, and compliant with the [case-study publication contract](../case-studies/README.md#publication-and-sanitization-contract).
- The UI clearly states that initial coefficients and outputs are experimental and unvalidated.

## Acceptance criteria

The POC is complete when a new user can start it using the documented container workflow, complete the primary journey for Case Study 001 without editing source code, export or inspect schema-compatible artifacts, and reproduce results for the same scenario, model version, seed, and inputs.

The user must be able to trace a material PH or duration outcome to causal inputs; compare traditional, AI-assisted, and AI-native delivery assumptions; switch engagement views without silently changing engineering effort; and ingest synthetic actuals into an evolution-aware calibration demonstration. Automated tests must cover domain behavior, decomposition contracts, percentile semantics, dimensional separation, schema compatibility, persistence, HTTP workflows, sanitization fixtures, and the critical browser journey.

## Deferred

- Automated extraction of confidential specifications.
- Statistical claims from real-world datasets; the POC demonstrates mechanics using synthetic observations only.
- Multi-user collaboration and multi-tenancy.
- Enterprise authentication and authorization.
- Production-grade scalability, availability, and disaster recovery.
- Organization-specific delivery methods, integrations, rates, calibration parameters, or reporting.
- A dedicated JavaScript frontend application.
- CLI and SDK product experiences.

## Public and private boundary

Public REEF is independent and vendor-neutral. Future organization-specific tools may reuse the Python package, extend its interfaces, or independently implement its public schemas. Proprietary methods, internal systems, client data, employee data, private calibration parameters, source case-study material, and organization-specific branding remain outside this repository.
