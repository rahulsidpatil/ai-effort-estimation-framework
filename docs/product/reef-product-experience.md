# REEF Product Experience

## Purpose and status

The `/product-experience` route is a guided, interactive simulation of the intended REEF POC.
It exists to validate whether real estimation participants can understand, challenge, and use the
proposed journey before production estimation behavior is implemented.

The tour is an experience contract, not a working estimator. It must never imply that an action
has imported a specification, calculated or accepted an estimate, recorded actuals, calibrated a
model, or submitted feedback. All displayed values are synthetic and illustrative.

## User hierarchy

REEF serves a workflow with several participants, but it does not treat them as one generic user.

### Primary user: estimation lead

Usually a solution architect, estimation lead, or accountable delivery lead. This person must
produce a defensible estimate under time pressure and incomplete information. They own the
accepted scope decomposition, assumptions, evidence, warnings, and estimate version.

Their core jobs are to:

- clarify the decision and scope boundary;
- identify missing information that could materially change the result;
- correct proposed work decomposition and delivery assumptions;
- compare scenarios without losing their causal assumptions;
- explain the range, dominant drivers, and limitations; and
- prepare an estimate that can survive engineering and commercial review.

### Contributing and reviewing users

- **Engineering and delivery contributors** provide delivery-mode, AI-participation, role,
  dependency, environment, and organizational-friction evidence.
- **Engineering or delivery reviewers** challenge scope, feasibility, evidence, and uncertainty
  before an exact estimate version is accepted.
- **Commercial leads** transform an accepted engineering estimate into an engagement view while
  keeping effort, price, contingency, and risk ownership distinct.
- **Delivery leads** record actual effort, elapsed time, realized context, scope change, and AI
  correction effort without turning variance into employee scoring.
- **Researchers or model owners** evaluate observations, cohorts, drift, and candidate model
  versions without rewriting historical estimates.

Executives and clients may consume exported views, but they are not the primary construction user
for the initial POC.

## Representative journey

Before the journey begins, a dedicated overview must orient a first-time user. Without requiring
prior estimation knowledge, it explains:

- what REEF is and who it helps;
- the outputs REEF is intended to produce;
- that the tour follows one fictional project through the complete workflow;
- what the user should understand after completing the tour; and
- that the current experience is an interactive preview using illustrative data, not a working
  estimator or system of record.

The overview is not one of the workflow stages. Its primary action starts with the project brief;
its secondary action exposes the complete ten-stage journey for an experienced user.

The tour then follows the synthetic Case Study 001 through ten decision-centered stages:

1. An estimation lead receives an incomplete engagement brief and clarifies the decision.
2. REEF identifies material unknowns and recommends the next evidence-gathering action.
3. The estimation lead and a domain specialist review the proposed work decomposition.
4. Delivery contributors describe AI effects, people, dependencies, and organizational friction.
5. The team reviews evidence strength, assumptions, correlations, and uncertainty.
6. The estimation team compares traditional, AI-assisted, and AI-native scenarios.
7. A reviewer challenges material assumptions and resolves or explicitly accepts warnings.
8. A commercial lead switches engagement views without changing the engineering baseline.
9. A delivery lead records synthetic actuals and explains variance through realized context.
10. A model owner preserves the original estimate while evaluating future learning, and the user
    records local experience feedback.

## Experience principles

- Orient a newcomer before asking them to make an estimation decision.
- Start with the decision being supported, not a factor-entry form.
- Use delivery language first and expose methodological detail progressively.
- Prefill a sanitized synthetic example so a new user can explore before creating anything.
- Distinguish facts, evidence, assumptions, defaults, unknowns, model outputs, and observations.
- Rank missing inputs by decision consequence rather than presenting all fields as equally urgent.
- Keep gross AI benefit and AI-induced overhead separate.
- Keep added PH, capacity loss, and elapsed wait time separate.
- Keep effort, duration, cost, price, and commercial-risk ownership separate.
- Make causal trace and scenario comparison central to review.
- Preserve exact versions and make unresolved warnings visible at acceptance.
- Treat variance as evidence about scope, context, and the model—not as an employee score.
- Prefer honest uncertainty and recommended next actions over false precision.

## Interaction contract

- The tour opens on the overview before stage one, unless the user resumes a stage in the same
  browser session.
- The overview offers both a guided start and direct access to the complete journey navigation.
- A persistent journey rail shows all stages, the current stage, and visited state.
- Previous, next, direct-stage, and left/right keyboard navigation are supported.
- A narrow viewport exposes an accessible journey drawer rather than compressing the rail.
- Representative controls provide immediate simulated feedback without calling domain,
  persistence, estimation, actuals, or calibration APIs.
- Changing a delivery scenario updates illustrative P50, P80, duration, gross AI benefit, AI
  overhead, and net effect together.
- Changing an engagement view leaves the displayed engineering baseline unchanged.
- Simulation labels remain visible at both tour and representative-screen levels.
- Semantic headings, native controls, visible focus, status announcements, readable contrast, and
  reduced-motion behavior support keyboard and assistive-technology evaluation.
- The current tour stage may be stored in session storage and safely discarded.

## Feedback and privacy contract

The final stage asks for the user's role, comprehension confidence, most valuable element, and
anything confusing or missing. Until a reviewed feedback service exists:

- feedback is stored only in browser local storage;
- the user can clear the local copy;
- the page repeatedly states that nothing was submitted;
- the user may copy or download a plain-text response;
- the page makes no feedback network request; and
- request logs never receive the response body.

A networked feedback service requires an explicit retention, privacy, authentication, and abuse
prevention design.

## Usability validation

Evaluation should recruit people who currently create or review software-delivery estimates. Ask
them to complete these tasks without explaining the interface first:

1. Identify the most consequential missing input and the recommended next action.
2. Explain why the AI-assisted scenario's net effect differs from its gross benefit.
3. Determine whether approval latency changes PH, duration, or both.
4. Switch from T&M to Fixed Bid and explain what changed and what remained stable.
5. Find why observed duration exceeded the estimate without attributing it to individual
   performance.
6. Explain whether later observations changed the original accepted estimate.

Record task completion, misconceptions, terminology problems, missing evidence, and moments where
the interface creates unjustified confidence. Visual preference alone is not sufficient evidence.

## Acceptance criteria

The product experience is ready for evaluation when:

1. a first-time visitor can state what REEF is, what it is intended to produce, what the tour will
   demonstrate, and what is simulated before entering stage one;
2. all ten stages are reachable through the rail, sequential controls, and keyboard navigation;
3. the user hierarchy and handoffs are visible in the narrative;
4. every required POC input and output category appears at least once;
5. scenario comparison preserves causal distinctions and clearly uses illustrative values;
6. commercial views visibly preserve one engineering baseline;
7. feedback survives refresh locally and can be copied or downloaded without submission;
8. the layout is usable at representative desktop and mobile widths;
9. automated route, content-model, security-header, and asset-boundary tests pass; and
10. a human completes the usability tasks and records material findings before simulated stages are
   treated as stable implementation contracts.

## Implementation boundary

The current tour is a presentation adapter composed of structured stage content, a server-rendered
template, and static browser assets. It does not import the estimation domain or application layer
and introduces no new persistence. Future vertical slices should replace simulation behind stable
user concepts one stage at a time rather than moving prototype calculations into the domain.
