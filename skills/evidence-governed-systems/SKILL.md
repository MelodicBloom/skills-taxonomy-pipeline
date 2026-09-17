---
name: evidence-governed-systems
description: Apply evidence-governed, regenerative systems architecture to design, coding, repository, and handoff work. Use when a task requires provenance, explicit boundaries, recursive inquiry, lifecycle-aware decisions, or inspectable receipts.
metadata:
  short-description: Govern systems work with evidence, provenance, and recoverable handoffs
---

# Evidence-Governed Systems

Use this skill to turn ambiguous systems, product, design, and repository work into bounded, inspectable decisions. The goal is not to add ceremony to ordinary work; it is to prevent unsupported claims, hidden coupling, irreversible decisions, and presentation-only governance.

## Operating principles

- Treat every output as part of a larger system. Prefer reusable primitives, adapters, schemas, fixtures, records, and documentation over disposable one-off work.
- Make a change net-positive when practical: improve maintainability, observability, testability, performance, accessibility, semantic clarity, or recoverability alongside the immediate goal.
- Feed useful failures, friction, validation results, and decisions into the next discovery cycle.
- Separate observed facts, derived interpretations, proposals, historical context, and unverified claims.
- Preserve provenance: canonical repository, branch or revision, commit, source location, hashes, ownership, intent, rejected alternatives, validation receipts, and reopen conditions.
- Prefer changes that can be inspected, tested, reverted, superseded, or reconciled without rewriting authoritative history.

## Evidence labels

Label material claims and important artifacts with one of:

- `OBSERVED`: directly inspected or measured;
- `DERIVED`: reasoned from observed evidence;
- `PROPOSED`: suggested but not implemented or accepted;
- `UNVERIFIED`: plausible but not tested or confirmed;
- `PHYSICAL_UNRUN`: digital checks exist but physical execution has not occurred;
- `DESIGN_ONLY`: visual or conceptual work not connected to runtime state;
- `BLOCKED`: the required evidence, authority, dependency, or permission is unavailable.

Do not combine repository state, CI, screenshots, browser behavior, runtime checks, and physical tests into one undifferentiated proof claim. Each proves only the scope it actually covers.

## Authority and mutation gates

Before editing or making external changes:

1. Identify the exact canonical repository, source, branch, revision, or artifact.
2. Verify that authority using available repository evidence; never substitute a nearby project or similarly named source.
3. Refresh branch head, ancestry, working-tree state, remote state, CI, review, and provenance when the decision depends on them.
4. Separate technical readiness, approval, provenance correctness, and external mutation authorization.
5. Do not merge, push, deploy, publish, submit, or message externally unless the user explicitly authorizes that action.

Green CI, `mergeable: true`, connector write access, or a recommendation to approve is not authorization.

## Recursive inquiry

Treat the first request as a possible symptom. Before implementation, evaluate:

1. What is the cognitive, computational, organizational, or evidentiary load?
2. What existing system, contract, workflow, component, or decision does this duplicate, contradict, or bypass?
3. What changes at 10x the data, users, repositories, evidence volume, rendering complexity, or review burden?
4. Which claim would be unsafe if current evidence were incomplete?
5. What future decision becomes harder if this change is made now?

Ask the user only when an answer would materially change scope, authority, architecture, safety, or acceptance criteria. Otherwise state the assumption and proceed.

## Phased workflow

### Phase 1: Discovery and semantics

- Define the problem, intended outcome, ownership, authority, taxonomy, evidence classes, constraints, and unresolved questions.
- Distinguish immutable source material from observations, candidates, projections, decisions, and executable outputs.

### Phase 2: Architecture and wireframing

- Define contracts, state transitions, data flows, integration seams, acceptance criteria, validation surfaces, and failure modes.
- Keep domain ownership separate from reusable governance. A domain owns its semantics and evidence; governance owns criteria, approvals, workflows, and receipts; the target repository owns executable acceptance.

### Phase 3: Experimentation and motion

- Explore visual behavior, interaction, rendering, performance, edge cases, and divergent alternatives.
- Keep prototypes, screenshots, interaction tests, and physical outcomes bounded to what they prove.

### Phase 4: Synthesis and handoff

- Consolidate decisions, remove redundancy, record rejected alternatives, validate the result, identify remaining uncertainty, and produce a recoverable receipt.

Default execution posture:

`inspect → establish authority → classify evidence → define contract → implement smallest coherent unit → validate focused behavior → report boundaries → produce receipt`

## Architecture rules

- Decompose complex systems into atomic primitives: tokens, schemas, validators, adapters, selectors, state transitions, pure functions, fixtures, and presentational components.
- Favor loose coupling, high cohesion, narrow interfaces, explicit ownership, and versioned contracts.
- Keep UI presentation separate from business logic, evidence reconciliation, persistence, approval state, and external integrations.
- Centralize state transitions and validation rules. Pass explicit typed data into presentational components.
- Use negative fixtures and failure-mode tests; happy paths alone do not establish correctness or governance.
- Preserve graceful degradation: the core behavior must remain understandable and useful at the lowest supported technology, evidence, and cognitive tier.
- Treat generated indexes, receipts, projections, caches, and reports as derived unless explicitly designated canonical.
- A feature is not complete because it renders. Its inputs, outputs, state transitions, validation, ownership, and evidence status must be inspectable.

## Semantic taxonomy and naming

- Use explicit domain-bound names: verb-noun actions, state-based predicates, semantic tokens, and lifecycle-role records.
- Prefer lifecycle terms such as `Source`, `Observation`, `Candidate`, `Decision`, `Gate`, `Receipt`, `Projection`, `Approval`, and `Reconciliation`.
- Avoid unqualified names such as `wrapper`, `container`, `misc`, `thing`, `data`, `helper`, or `manager`. Qualify them by semantic role when they are necessary.
- Use stable identity rather than positional or presentation-derived identity.
- Distinguish `raw`, `candidate`, `canonical`, `derived`, `superseded`, `quarantined`, and `rejected` states explicitly.
- Preserve revision, hash, timestamp, source reference, and relation verb when the system must reason about change over time.
- Use explicit lifecycle statuses such as `candidate-only`, `validated`, `review-required`, `approved`, `rejected`, `superseded`, `quarantined`, and `unverified` rather than ambiguous booleans.
- Treat naming conventions as `RECOMMENDED` until repeated evidence justifies making them mandatory.

## State and data flow

Use this lifecycle as the default model when applicable:

`source → observation → candidate → transformation → validation receipt → review decision → canonical or rejected outcome`

For every state transition, define:

- trigger;
- precondition;
- resulting state;
- actor or system owner;
- validation evidence;
- receipt or audit record;
- supersession or rollback behavior.

Fail closed when identity is ambiguous, duplicate, missing, or contradictory. Do not let a UI label, optimistic state, or explanatory copy imply a transition that the underlying data model has not made.

## Motion grammar

When the work includes interactive motion, treat objects as having mass, friction, velocity, and inertia. Use the damped oscillator as the conceptual model:

\[
m\frac{d^2x}{dt^2}+c\frac{dx}{dt}+kx=0
\]

- Prefer spring-based motion when supported.
- Do not use linear easing for spatial movement except for intentional color interpolation or opacity fades.
- Use `cubic-bezier(0.2, 0.8, 0.2, 1)` as an entrance fallback and `cubic-bezier(0.8, 0, 1, 1)` as an exit fallback when a spring is unavailable.
- Keep micro-interactions generally within `150–200ms` and macro-interactions within `300–400ms`.
- Use approximately `50ms` stagger intervals only when they establish useful directional hierarchy.
- State duration, delay, easing or spring parameters, trigger, interruption behavior, reduced-motion fallback, and semantic intent.
- Respect reduced motion and do not let animation obscure controls, delay essential feedback, or cause focus loss.
- Interaction tests prove behavior only within their tested environment; they do not automatically prove visual fidelity, device parity, load performance, or physical-world behavior.

## Handoff receipts

Every completed phase must produce a concise receipt answering:

1. What changed?
2. Why was this path chosen?
3. What evidence proves the stated result?
4. What remains unknown or unverified?
5. What should happen next, and what evidence would reopen the decision?

Use the receipt appropriate to the work:

```markdown
## Decision Receipt

- Status: `complete | partial | blocked`
- Scope:
- Intent: `exploratory | candidate-only | operational | production-bound`
- Canonical authority:
- Working branch or revision:
- Chosen path:
- Rejected alternative:
- Constraint that forced the decision:
- Evidence supporting the result:
- Validation performed:
- Remaining unknowns:
- Authorization boundary:
- Immediate next action:
- Reopen condition:
```

For code, additionally report changed paths, contracts and invariants, time and space complexity, dependencies, validation commands and results, and known environment limitations.

For design, additionally report semantic tokens, component ownership, information hierarchy, state model, motion parameters, reduced-motion fallback, accessibility status, and whether the result is `DESIGN_ONLY`, screenshot-verified, interaction-verified, runtime-verified, or production-connected.

For strategic decisions, explicitly state the chosen path, rejected alternative, forcing constraint, evidence still missing, reversibility, and the next piece of evidence worth obtaining.

