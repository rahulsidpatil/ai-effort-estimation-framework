# ADR-0001: Preserve Explicit Causal Drivers

- **Status:** Accepted
- **Date:** 2026-09-22

## Context

Effort estimators often compress team, organization, delivery-mode, and uncertainty effects into broad multipliers. Such coefficients can be convenient for calculation, but they hide why an estimate changed, mix PH with elapsed time, make calibration brittle, and prevent users from challenging individual assumptions.

REEF must explain outcomes across traditional, AI-assisted, and AI-native delivery and across T&M, Fixed Bid, Managed Service, and SRE engagements. That requires stable semantic distinctions even when estimator implementations differ.

## Decision

REEF retains material causal inputs and their contribution trace. An estimator may compute aggregate coefficients internally, but its persisted result and explanation must preserve, at an appropriate level of granularity:

- the affected work package, activity, role, capacity, dependency, or commercial term;
- whether the effect changes PH, elapsed time, cost, price, commercial risk, or more than one;
- the direction and magnitude or distribution of the effect;
- the assumption or evidence supporting it; and
- the model rule and version that performed the transformation.

AI gross benefit and AI-induced overhead remain separate. Organizational friction remains decomposed into effort, capacity, and latency effects. Engagement-model transformations occur after the engineering estimate.

## Consequences

- Estimates are more explainable, comparable, auditable, and suitable for evolution-aware calibration.
- Models and schemas need richer provenance and contribution structures.
- Data collection and user interfaces require more care than a single questionnaire score.
- Algorithms remain replaceable; this decision constrains output semantics, not the statistical technique.

## Rejected alternative

A canonical set of opaque project-level multipliers was rejected because it would erase causal detail and conflate effects with different units.
