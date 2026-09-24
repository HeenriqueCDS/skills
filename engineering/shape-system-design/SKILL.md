---
name: shape-system-design
description: Stage 1 of the shape chain. Grills the product's functional and non-functional requirements, then writes docs/spec.md and docs/non-functional-requirements.md.
disable-model-invocation: true
---

Stage 1 of the chain in [CHAIN.md](../shape-project/CHAIN.md). Read it first: it governs upstream reading, amend mode, contradictions, doc conventions, diagrams, and closing for every stage.

This stage decides **what** the product does and **how well** it must do it. Routes, tables, frameworks, and modules belong to later stages. When an answer drifts there, record it under the doc's **Handoff** section for the stage that owns it, and return to the branch.

Both parts run as `/grilling` with `/domain-modeling`. In amend mode, ask first which part changed, and run only that part.

## Part 1: functional requirements

Walk these branches in order. Before the first question of a branch, read its entry in [FUNCTIONAL.md](FUNCTIONAL.md): what to decide, the default to recommend, and the probes that stress-test it. A branch closes only when every rule it produced has an example.

1. Problem and scope fence
2. Actors
3. Ownership and privacy
4. Language
5. Entities, commands, and states
6. Invariants
7. Calculations
8. Boundaries
9. Defaults
10. Correction: edit, rename, delete, revert
11. No-gos

Write `docs/spec.md` from [SPEC-TEMPLATE.md](SPEC-TEMPLATE.md). It is done when:

- Every entity has an owner, and every command on it (create, edit, rename, delete, each state transition) has an accepted example, plus a refused example wherever a guard exists.
- Every rule is atomic and carries at least one example with concrete inputs and outcome. Every numeric threshold has examples below, on, and above it.
- Every kind-by-state decision table has no empty cell, and the defaults satisfy every invariant.
- Every calculation has one worked fixture that includes a zero, a negative, and an empty case.
- Every term used is in `CONTEXT.md` with the same meaning, and no _Avoid_ alias appears.
- No external artifact (a spreadsheet, a legacy app) is left as a silent source of unstated rules.
- **Open points** is empty.

## Part 2: non-functional requirements

Starts once the spec exists, because the data the spec defines decides what must be protected. Walk these branches in order, reading each entry in [NON-FUNCTIONAL.md](NON-FUNCTIONAL.md) first.

1. Context and threat actors
2. Data classification
3. Tenancy and authorization
4. Authentication
5. Sessions and tokens
6. Confidentiality at rest and in transit
7. Keys and secrets
8. Privacy, retention, and erasure
9. Abuse and rate limits
10. Reliability, backup, and restore
11. Performance and capacity
12. Cost ceiling
13. Observability and redaction
14. Portability and internationalisation

Write every requirement as a **quality attribute scenario** with a numeric response measure, or as an OWASP ASVS requirement id. State the property here. When the mechanism behind it is expensive to reverse (envelope encryption, token transport, password hash), offer an ADR through `/domain-modeling` and link it.

Draw the **system context**: actors, the system, every external system, and the trust boundaries between them.

Write `docs/non-functional-requirements.md` from [NFR-TEMPLATE.md](NFR-TEMPLATE.md). It is done when:

- Every quality characteristic is in scope with at least one scenario carrying a number, or out of scope with a reason.
- Every data class states confidentiality, integrity, retention, deletion, log rule, and backup fate.
- For every threat actor, the doc says whether they can read each confidential data class.
- The ASVS level is named, and every requirement at that level in the chapters listed in NON-FUNCTIONAL.md is _adopted_, _not applicable_, or _waived_. A waiver names the accepted threat and its compensating control.
- Availability, latency, and recovery each have an indicator, an objective, and a window, plus "no SLA" or the consequence.
- The cost ceiling is a monthly number at a stated load.
- Erasure names what disappears, by when, what backups still hold and for how long.
- Libraries and cloud products appear only as labelled constraints linking an ADR.
- **Open points** is empty, or each one names who settles it before the API contract.

Then close the stage as CHAIN.md describes. The next skill is `/shape-api-contract`.
