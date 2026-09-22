# Calibration

Calibration adapts an estimator using observations while preserving reproducibility and guarding against overfitting.

Because delivery systems evolve, calibration must be time-aware. Tool versions, AI models, delivery practices, team composition, organization policies, environments, scope definitions, and engagement conditions can all change the relationship between drivers and outcomes. Historical actuals are evidence, not timeless coefficients.

## Required properties

- Input datasets, filters, code, seeds, and parameter outputs are versioned.
- Training observations are separated from evaluation observations.
- Time-aware splits are preferred when the model will predict future work.
- Small cohorts and missing data are reported rather than hidden.
- Global and cohort-level accuracy, bias, and coverage are compared.
- A calibrated model can be rolled back and reproduced.
- Each observation records the delivery context and validity period needed to detect change.
- Model training applies declared recency, comparability, and cohort rules rather than pooling incompatible eras silently.
- Material process or tool changes trigger drift review and, when justified, a new model version or cohort.

## Proposed workflow

1. Validate and freeze eligible observations, including actual PH, elapsed time, realized friction, scope change, and delivery-mode facts.
2. Compare estimate-time assumptions with actual context and record material changes rather than rewriting the original estimate.
3. Declare inclusion, exclusion, segmentation, recency, comparability, and evaluation rules.
4. Detect drift in inputs, residuals, and outcome distributions before fitting.
5. Fit candidate parameters on training data while retaining causal feature definitions.
6. Evaluate on later held-out data against simple baselines and the previous model version.
7. Review stability, bias, percentile coverage, cohort effects, and sensitivity.
8. Publish a model card, immutable model version, applicable context, and rollback path.

Calibration is not justified merely because a fitted model reduces training error. Evidence should show improved out-of-sample behavior and acceptable failure characteristics.
