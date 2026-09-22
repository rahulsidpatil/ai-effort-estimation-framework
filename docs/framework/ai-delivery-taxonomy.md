# AI Delivery Taxonomy

## Purpose

The taxonomy describes where AI participates in delivery without assuming a productivity effect. Effects are empirical questions, not category definitions. REEF can use the same activity model for traditional, AI-assisted, AI-native, and mixed-mode delivery.

## Delivery modes

- **Traditional:** no material AI participation in the modeled workflow.
- **AI-assisted:** humans own the workflow while AI participates in selected activities.
- **AI-native:** the workflow is intentionally designed around AI-mediated or agentic execution with explicit human authority and controls.
- **Mixed:** participation differs materially by activity or work package and is recorded at that level.

These modes describe a delivery system; they do not encode a productivity multiplier.

## Activity categories

1. **Discovery and planning:** requirements exploration, decomposition, estimation, and design.
2. **Implementation:** code, configuration, infrastructure, migrations, and content generation.
3. **Verification:** tests, review, static analysis, security checks, and acceptance evidence.
4. **Integration and release:** dependency integration, deployment, rollout, and operational readiness.
5. **Operations and maintenance:** monitoring, incidents, upgrades, debugging, and change.
6. **Governance:** risk assessment, approvals, auditability, privacy, legal, and policy controls.

## Participation levels

- **None:** no material AI use in the activity.
- **Advisory:** AI suggests or explains; a human performs the work.
- **Generative:** AI produces material artifacts; humans review and integrate them.
- **Agentic:** AI plans or executes multi-step work within bounded authority; humans supervise and approve consequential outcomes.

Record participation per activity. A project-wide label alone is too coarse.

For each materially AI-enabled activity, record gross avoided PH and induced human PH independently. Induced work can include specification and context preparation, orchestration, review, verification, correction, governance, and recovery from tool or model failure.

## Context dimensions

Candidate dimensions include novelty, ambiguity, system coupling, quality criticality, regulatory burden, team familiarity, tool maturity, verification cost, and reversibility. Each factor requires an operational definition before it is used for calibration.

## Human work that remains visible

Prompt or context preparation, output review, fact checking, test design, security analysis, integration, exception handling, governance, and rework must be attributed to an activity rather than treated as free automation.
