# Evaluation

## Questions

- Is the estimator more accurate than simple declared baselines?
- Is it systematically optimistic or pessimistic?
- Do P50, P80, and other declared ranges achieve their intended empirical coverage?
- How stable are results across time and relevant cohorts?
- Does calibration improve held-out performance without unacceptable subgroup degradation?
- Are effort, elapsed duration, friction, and AI-effect components accurate enough to support their intended decisions?

## Minimum metrics

- Mean absolute error (MAE) in PH.
- Median absolute percentage error, with handling for near-zero actuals declared.
- Signed mean error for bias.
- Planning-range coverage and average range width.
- P50 and P80 coverage when the estimator emits probabilistic percentiles.
- Duration error and organizational-friction attribution error, reported separately from PH error.
- Error and coverage by preregistered cohort.

## Protocol requirements

Define the prediction timestamp, information available at prediction time, scope-change handling, missing-data policy, dataset splits, baseline estimators, and statistical uncertainty before interpreting results. Prevent data leakage and duplicate or highly related projects across splits.

Use the protocol in [`research/evaluation-protocols/baseline.md`](../../research/evaluation-protocols/baseline.md) as the initial reproducibility checklist.

## Interpretation

No single aggregate metric establishes validity. Results should include distributions, failure cases, sample sizes, sensitivity analysis, and limitations. Synthetic-data results validate mechanics only; they do not demonstrate real-world accuracy.
