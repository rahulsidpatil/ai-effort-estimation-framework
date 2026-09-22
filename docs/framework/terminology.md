# Terminology

These definitions are normative for repository artifacts unless a document explicitly marks an alternative.

## Effort and time

- **Person-Hour (PH):** one hour of human effort. PH is the canonical effort unit.
- **Calendar duration:** elapsed clock or working time between start and finish. It is not interchangeable with PH.
- **Wait or queue time:** elapsed time during which work is blocked or awaiting a dependency, approval, resource, or scheduled window. It may add little or no PH.
- **Capacity loss:** productive capacity displaced by collaboration, interruptions, mandatory activity, contention, or other constraints.
- **Baseline effort:** estimated PH under a declared reference delivery mode and assumptions.
- **Adjusted effort:** estimated PH after applying context, AI-assistance, risk, and overhead effects.
- **Enablement effort:** PH spent making productive delivery possible, such as onboarding, training, access setup, environment preparation, or governance preparation.
- **Actual effort:** observed PH attributed to the defined scope and measurement window.
- **Planning range:** lower, expected, and upper effort values representing uncertainty; it is not automatically a statistical confidence interval.

## Economics and engagement

- **Cost:** the delivery organization's economic consumption, normally derived from PH, role mix, rates, locations, tooling, infrastructure, and other expenses.
- **Price:** the amount charged under a commercial arrangement. Price is not synonymous with cost or effort.
- **Risk reserve:** an explicit provision for quantified uncertainty or identified risks. Its unit and ownership must be stated.
- **Commercial risk:** exposure created by contractual allocation of uncertainty, obligations, service levels, warranties, penalties, or margin assumptions.
- **Engagement model:** the commercial and operating structure applied after engineering estimation, such as Time and Materials (T&M), Fixed Bid, Managed Service, or Site Reliability Engineering (SRE).

## Delivery modes

- **AI-assisted development:** humans remain responsible for the delivery workflow while AI supports selected activities.
- **AI-native development:** the workflow is intentionally designed around AI agents or AI-mediated execution, with explicit human oversight and controls.
- **Traditional development:** the declared delivery workflow does not materially rely on AI for the activity being estimated.
- **Reference mode:** the stated counterfactual used for a baseline, such as the same team and scope without a specified AI capability.

## Model concepts

- **Activity:** a category of delivery work, such as discovery, implementation, verification, integration, or governance.
- **Factor:** a measurable or declared attribute expected to influence effort.
- **Adjustment:** a model-produced change to baseline effort attributable to one or more factors.
- **Overhead:** additional effort required to use or govern a capability, including prompting, review, validation, and remediation.
- **Organizational friction:** observable effort loss, wait time, or schedule constraint introduced by onboarding, provisioning, approvals, governance, collaboration, external dependencies, queues, or environment limitations.
- **Evidence strength:** an assessment of the relevance, recency, representativeness, and quality of evidence supporting an input or parameter.
- **Confidence:** a qualified judgment about estimate reliability based on uncertainty and evidence; it is not a statistical probability unless the model establishes that meaning.
- **Observation:** an immutable record of actual effort and relevant context.
- **Calibration:** a versioned process that estimates model parameters from observations.
- **Estimator:** a model implementation that transforms a project description into an estimate.
- **Model version:** an immutable identifier for equations, parameters, and relevant behavior.
- **Schema version:** an immutable identifier for a data contract.

## Evaluation concepts

- **Error:** the difference between estimated and observed effort under a declared metric.
- **Bias:** systematic over- or under-estimation across observations.
- **Coverage:** the proportion of observations contained within their predicted ranges.
- **Cohort:** observations grouped by a predeclared characteristic for analysis.
- **Data leakage:** use of information during estimation or training that would not have been available at the prediction time.
