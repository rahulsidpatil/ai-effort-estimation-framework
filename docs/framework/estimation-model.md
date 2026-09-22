# Estimation Model Proposal

## Status

This is a model interface and research hypothesis, not a finalized scientific model. Numeric defaults must be treated as experimental until evaluated on suitable data.

## Required result

An estimator returns:

- total, role-level, activity-level, and work-package effort in PH;
- P50 and P80 effort, with any additional planning range clearly defined;
- expected elapsed duration and its range, separately from PH;
- organizational-friction impact separated into PH, capacity, and elapsed-time effects;
- gross AI benefit, AI-induced overhead, and net AI effect by affected activity;
- risk reserve and its treatment in each downstream view;
- cost and engagement-specific commercial views that remain distinct from effort;
- assumptions, confidence, evidence references, warnings, and dominant uncertainty drivers;
- causal contribution traces rather than only aggregate factors;
- model and schema versions; and
- a reproducibility record sufficient to rerun the estimate.

The current public schemas represent a smaller pre-POC contract. They must evolve before the full result above is implemented; until then, missing fields must not be implied or encoded into unrelated properties.

## Estimation pipeline

1. **Ingest and sanitize scope.** Accept a safe project description and declared context; reject or quarantine restricted material.
2. **Decompose work.** Produce traceable work packages, activities, deliverables, acceptance evidence, dependencies, and complexity drivers.
3. **Establish the reference.** Declare the delivery mode, team, environment, and other counterfactual assumptions used for baseline PH.
4. **Estimate base effort.** Estimate PH by work package, activity, and role before delivery-mode effects.
5. **Model delivery mode.** Apply activity-specific traditional, AI-assisted, or AI-native behavior; expose gross benefit and induced overhead independently.
6. **Model people and organization.** Add enablement and collaboration PH, constrain capacity, and add dependency, approval, queue, and environment latency.
7. **Quantify uncertainty.** Propagate input ranges and correlations, identify risks, and calculate declared percentiles such as P50 and P80.
8. **Simulate duration.** Schedule work using dependencies, role capacity, calendars, ramp-up, wait time, and constrained windows.
9. **Transform to economics.** Derive cost from role effort, rates, locations, tools, infrastructure, and expenses.
10. **Apply the engagement model.** Produce T&M, Fixed Bid, Managed Service, SRE, or other commercial views without rewriting engineering effort.
11. **Emit evidence and lineage.** Record model versions, assumptions, evidence references, confidence rationale, input digest, and contribution trace.

## Conceptual decomposition

For work packages \(w\), activities \(a\), and roles \(r\), an illustrative effort decomposition is:

```text
E_delivery = Σ_w,a,r B[w,a,r]
             + ContextDeltaPH
             - AIGrossBenefitPH
             + AIInducedOverheadPH
             + EnablementAndCollaborationPH
             + ExpectedReworkPH
```

Where:

- `B[w,a,r]` is reference PH for a work package, activity, and role;
- every delta retains its causal source and affected work or role;
- gross AI benefit is distinct from the work introduced by AI use; and
- risk reserve is reported separately unless a declared view intentionally includes it.

Elapsed duration is produced from work sequencing, role capacity, calendars, organizational queues, constrained windows, and stochastic dependencies. Cost is then derived from effort and expenses. Price and commercial exposure are produced by the selected engagement model. None of these is interchangeable with `E_delivery`.

This decomposition is illustrative. Implementations may use parametric, probabilistic, empirical, simulation-based, or hybrid estimators provided that inputs, assumptions, correlations, output semantics, and model identity remain explicit.

## Constraints

- Multipliers must never conceal the reference baseline or their causal components.
- Savings in one activity must not silently erase overhead in another.
- Percentile labels must match the estimator's actual statistical interpretation.
- Output effort must be non-negative.
- Rounding and aggregation rules must be deterministic and documented.
- Calendar duration must be modeled separately from PH.
- Identical engineering assumptions must produce the same engineering effort before engagement-specific commercial transformation.
- Wait time must not be converted to PH unless human effort is actually consumed.

## Uncertainty

An initial implementation may use expert-provided three-point inputs. Mature estimators should state how distributions, dependencies, and correlations are produced and evaluate percentile coverage. `P50` and `P80` mean the modeled 50th and 80th percentiles, respectively; a non-probabilistic planning range must not use those labels. Confidence must include an evidence-based rationale rather than a bare category.

## Extension contract

Alternative estimators should accept a versioned project document and emit a versioned estimate document. This allows REEF to compare models while retaining shared validation, reporting, and observation workflows.
