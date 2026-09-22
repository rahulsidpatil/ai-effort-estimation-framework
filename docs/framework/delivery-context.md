# Delivery Context and Commercial Separation

## Purpose

REEF models an engagement as connected estimation planes rather than a single project-size score. The planes preserve the causes of effort, delay, and economic exposure so that an estimate can be explained, challenged, and recalibrated.

## Estimation planes

### 1. Work

The work plane describes what must be delivered. Scope is decomposed into traceable work packages with deliverables, activities, acceptance evidence, dependencies, complexity drivers, and non-functional obligations. A label such as `large` is not an adequate substitute for decomposition.

### 2. Delivery system

The delivery-system plane describes how each activity is performed. REEF supports traditional, AI-assisted, and AI-native modes, including mixed-mode engagements. AI participation is recorded by activity according to the [AI delivery taxonomy](ai-delivery-taxonomy.md), not as a project-wide productivity assumption.

The model keeps three quantities visible:

- reference effort before the modeled AI capability;
- gross AI benefit, expressed as avoided PH by activity; and
- AI-induced PH for specification and context preparation, orchestration, review, verification, correction, governance, and tool failure recovery.

Net AI effect is derived from gross benefit and AI-induced overhead. It is not an input claim.

### 3. People

The people plane describes roles, proficiency, domain and system familiarity, availability, location and working calendars, team topology, ramp-up, turnover assumptions, and collaboration needs. It supports role-level PH allocation and constrains the duration simulation. It must not be used to rank or surveil individuals.

### 4. Organization

Organizational friction is a first-class model, not a generic complexity multiplier. Inputs may contribute PH, elapsed time, capacity loss, or a combination of them:

| Category | Examples | Typical effects |
| --- | --- | --- |
| Onboarding | mandatory learning, identity activation, equipment readiness | enablement PH, start delay |
| Provisioning | repository, tool, data, platform, and workspace access | setup PH, queue time |
| Approvals and governance | architecture, security, privacy, compliance, procurement, change control | preparation PH, rework, decision latency |
| Collaboration overhead | recurring coordination, handoffs, distributed-team overlap | capacity loss, additional PH |
| External dependencies | upstream decisions, third-party inputs, other teams | blocked time, schedule uncertainty |
| Queues and windows | review queues, release windows, scheduled boards | wait time, constrained sequencing |
| Environment constraints | limited environments, contention, instability, deployment permissions | capacity loss, rework, wait time |

Each material friction driver should identify its source, affected work or role, unit, planning distribution or range, evidence, and whether work can continue in parallel. Duration impact must be calculated through sequencing and capacity rather than by converting wait days into PH.

### 5. Business context

Business context includes domain ambiguity, stakeholder complexity, criticality, regulatory or policy obligations, availability and resilience needs, time-to-market pressure, cost of delay, change frequency, and acceptance authority. These inputs affect work, validation, risk, priorities, and constraints; they do not directly determine a commercial price.

### 6. Uncertainty and evidence

Every material estimate input should distinguish known values, assumptions, ranges, and unknowns. Evidence records should identify their type, provenance class, observation date or validity period, relevance, and quality without embedding restricted source material. Confidence is reported with its rationale and dominant uncertainty drivers.

## Separate outcome layers

REEF applies the planes in a deliberate order:

```text
Work and context
      ↓
Engineering effort distribution (PH)
      ↓
Capacity, dependencies, queues, and calendars
      ↓
Elapsed-duration distribution
      ↓
Role mix, rates, tooling, infrastructure, and expenses
      ↓
Cost view
      ↓
Engagement terms, risk allocation, reserve, and margin policy
      ↓
Price and commercial-risk view
```

An upstream result remains visible when transformed downstream. Changing an engagement model must not silently change engineering PH for identical scope and delivery assumptions.

## Engagement models

### Time and Materials

T&M maps consumed effort and approved expenses to contracted rates and billing rules. Scope, duration, and cost uncertainty remain visible; the commercial view explains which party bears which exposure.

### Fixed Bid

Fixed Bid starts with the same engineering estimate, then explicitly models scope boundaries, confidence target such as P50 or P80, contingency or risk reserve, warranty and support obligations, contractual exposure, and margin policy. Price must not be presented as engineering effort multiplied by an unexplained factor.

### Managed Service and SRE

Managed Service and SRE are operating models, not development-effort multipliers. Their work model may include transition PH, steady-state roles and coverage, service windows, demand or incident profiles, service objectives, on-call constraints, reliability and automation backlogs, continuous improvement, and exit or handback obligations. One-time transition and recurring effort must remain separate.

## Causal-driver contract

A model may calculate aggregate factors for a specific algorithm, but it must retain the causal inputs and contribution trace. An output such as `organization factor = 1.25` is insufficient unless the estimate can show the underlying effort, capacity, and latency drivers and their evidence. See [ADR-0001](../architecture/decisions/0001-explicit-causal-drivers.md).
