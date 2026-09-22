# Baseline Evaluation Protocol

## Status

Draft protocol for evaluating candidate estimators. It is not a claim of validation.

## Procedure

1. Freeze a versioned dataset and record its provenance and limitations.
2. Define the prediction timestamp and remove information unavailable at that time.
3. Split observations by time when possible; keep related projects in the same split.
4. Compare the candidate against at least a global median and a simple activity-sum baseline.
5. Report MAE in PH, signed mean error, percentage error with near-zero handling, range coverage, and range width.
6. Report sample size and metrics for preregistered cohorts.
7. Inspect large errors, missing data, sensitivity, and possible leakage.
8. Publish code, configuration, seeds, model identity, and an evaluation report.

Synthetic data may test this pipeline but cannot establish external validity.
