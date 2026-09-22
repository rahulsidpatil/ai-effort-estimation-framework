# Framework Vision

## Purpose

Software effort estimation has always depended on incomplete information. AI-assisted and AI-native delivery adds further variability: generation can accelerate some tasks, while review, validation, integration, governance, and recovery from plausible-but-wrong outputs can add effort elsewhere.

The AI Effort Estimation Framework proposes a shared, extensible language and set of data contracts for:

1. describing a software initiative and its delivery context;
2. producing an explainable effort distribution in Person-Hours (PH);
3. recording actual human effort without confusing it with elapsed time;
4. evaluating estimates against observations; and
5. calibrating a versioned model as evidence accumulates.

## Intended users

- delivery teams planning AI-assisted work;
- researchers studying software effort and AI-enabled development;
- tool builders implementing estimators, integrations, and visualizations;
- organizations comparing hypotheses across contexts without assuming universal effects.

## Non-goals

The framework is not an employee-ranking system, a productivity-surveillance mechanism, a guarantee of delivery dates, or proof that AI always reduces effort. It does not prescribe a single development process or vendor.

## Status and evidence

This repository begins as a proposal. Its initial factors and equations are working hypotheses designed to be falsifiable and replaceable. Scientific validity requires transparent datasets, preregistered or clearly specified evaluation, independent replication, uncertainty analysis, and evidence across diverse contexts.

## Success criteria

The framework succeeds when independent parties can exchange compatible data, reproduce an estimate, understand why it changed, measure its calibration and error, and substitute alternative models without rewriting the surrounding workflow.
