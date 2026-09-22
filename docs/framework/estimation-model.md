# Estimation Model Proposal

## Status

This is a model interface and research hypothesis, not a finalized scientific model. Numeric defaults must be treated as experimental until evaluated on suitable data.

## Required result

An estimator returns:

- lower, expected, and upper effort in PH;
- the reference mode and assumptions;
- factor and adjustment contributions;
- uncertainty and data-quality notes;
- model and schema versions; and
- a reproducibility record sufficient to rerun the estimate.

## Conceptual decomposition

For activities \(a\), the expected adjusted effort may be represented as:

```text
E_adjusted = Σ_a (B_a × C_a × A_a) + O_review + O_integration + O_governance + R
```

Where:

- `B_a` is baseline PH for activity `a`;
- `C_a` is a non-AI context multiplier;
- `A_a` is the net AI-assistance multiplier for that activity;
- `O_*` terms are explicit PH overheads; and
- `R` is expected rework or risk allowance in PH.

This equation is illustrative. Implementations may use parametric, probabilistic, empirical, or hybrid estimators provided that inputs, assumptions, output semantics, and model identity remain explicit.

## Constraints

- Multipliers must never conceal the reference baseline.
- Savings in one activity must not silently erase overhead in another.
- The expected value must lie within the planning range.
- Output effort must be non-negative.
- Rounding and aggregation rules must be deterministic and documented.
- Calendar duration must be modeled separately from PH.

## Uncertainty

An initial implementation may use expert-provided three-point inputs. Mature estimators should state how ranges are produced and evaluate interval coverage. A planning range must not be labeled a confidence or credible interval unless its statistical interpretation is valid.

## Extension contract

Alternative estimators should accept a versioned project document and emit a versioned estimate document. This allows REEF to compare models while retaining shared validation, reporting, and observation workflows.
