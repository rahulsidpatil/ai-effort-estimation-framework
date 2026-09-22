# Calibration

Calibration adapts an estimator using observations while preserving reproducibility and guarding against overfitting.

## Required properties

- Input datasets, filters, code, seeds, and parameter outputs are versioned.
- Training observations are separated from evaluation observations.
- Time-aware splits are preferred when the model will predict future work.
- Small cohorts and missing data are reported rather than hidden.
- Global and cohort-level accuracy, bias, and coverage are compared.
- A calibrated model can be rolled back and reproduced.

## Proposed workflow

1. Validate and freeze eligible observations.
2. Declare inclusion, exclusion, segmentation, and evaluation rules.
3. Fit candidate parameters on training data.
4. Evaluate on held-out data against simple baselines.
5. Review stability, bias, coverage, and sensitivity.
6. Publish a model card and immutable model version.

Calibration is not justified merely because a fitted model reduces training error. Evidence should show improved out-of-sample behavior and acceptable failure characteristics.
