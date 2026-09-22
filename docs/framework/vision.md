# Framework Vision

## Purpose

Software effort estimation has always depended on incomplete information. Delivery systems also differ: traditional teams, AI-assisted teams, and workflows designed around AI agents may perform the same scope in materially different ways. AI can accelerate some tasks while review, validation, integration, governance, and recovery from plausible-but-wrong outputs add effort elsewhere. People, organizational constraints, business conditions, and commercial arrangements can change the feasible schedule and economic exposure even when engineering scope is unchanged.

The AI Effort Estimation Framework proposes a shared, extensible language and set of data contracts for:

1. describing the work and the delivery system for a software or digital engineering engagement;
2. producing an explainable effort distribution in Person-Hours (PH);
3. simulating elapsed duration without confusing it with effort;
4. transforming effort into cost, price, and commercial-risk views without conflating them;
5. recording actuals and contextual change over time;
6. evaluating estimates against observations; and
7. calibrating versioned models as evidence accumulates.

## Intended users

- delivery teams planning traditional, AI-assisted, or AI-native work;
- researchers studying software effort and AI-enabled development;
- tool builders implementing estimators, integrations, and visualizations;
- organizations comparing hypotheses across contexts without assuming universal effects.

## Non-goals

The framework is not an employee-ranking system, a productivity-surveillance mechanism, a guarantee of delivery dates, a pricing mandate, or proof that AI always reduces effort. It does not prescribe a single development process, engagement model, technology, or vendor.

## Status and evidence

This repository begins as a proposal. Its initial factors and equations are working hypotheses designed to be falsifiable and replaceable. Scientific validity requires transparent datasets, preregistered or clearly specified evaluation, independent replication, uncertainty analysis, and evidence across diverse contexts.

## Success criteria

The framework succeeds when independent parties can exchange compatible data, reproduce an estimate, distinguish effort from schedule and economics, understand which causal drivers changed an outcome, measure calibration and error, and substitute alternative models without rewriting the surrounding workflow.
