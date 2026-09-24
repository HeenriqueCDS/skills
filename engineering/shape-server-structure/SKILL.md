---
name: shape-server-structure
description: Stage 4 of the shape chain. Grills the backend's internal structure (deep modules, seams, adapters, dependency rules, errors, transactions, test surface), then writes docs/architecture.md and AGENTS.md.
disable-model-invocation: true
---

Stage 4 of the chain in [CHAIN.md](../shape-project/CHAIN.md). Read it first: it governs upstream reading, amend mode, contradictions, doc conventions, diagrams, and closing for every stage.

This stage decides how the code is shaped: which modules exist, what each one's interface hides, where the seams are and which adapters sit at them, and the rules that keep that shape. It changes no rule, property, route, or table. It writes no application code.

Invoke `/codebase-design` before anything else and use its glossary exactly: **module**, **interface**, **implementation**, **depth**, **seam**, **adapter**, **leverage**, **locality**. The two tests that decide most answers here come from it: the **deletion test** and **two adapters make a real seam**.

## 1. Derive before asking

Build the candidate module list from the upstream docs and show it to the user before the first question:

- From the spec, the rules that are not plain create-read-update-delete (calculations, recurrences, state machines, privacy scoping). These are what a module must hide.
- From the contract, the operations grouped by shared language and consistency, not by URL noun. Each operation, including every agent tool, will name one method on one module's interface.
- From the schema, which tables each candidate owns, and the transactions that must span tables. A transaction that spans two candidates is evidence they are one module.

Apply the deletion test to every candidate and show the verdict: _keep_ (complexity would reappear across callers) or _merge_ (it only forwards). When upstream docs are missing, grill the operations and rules this stage needs, and record them under **Assumptions**.

## 2. Grill

Run `/grilling` with `/domain-modeling`. Walk these branches in order. Before the first question of a branch, read its entry in [BRANCHES.md](BRANCHES.md): what to decide and the default to recommend. After branches 4 and 10, revisit the module list: a cycle, or a port with one adapter, means merge.

1. Runtime and framework
2. Module boundaries
3. Module interfaces
4. Seams and adapters
5. Layering inside a module
6. Dependencies between modules
7. Composition root
8. Validation placement
9. Error model
10. Transaction boundaries
11. Test surface
12. Folders and naming
13. Enforcement

When a module's interface is contested, offer the **design it twice** pattern from `/codebase-design` (parallel sub-agents, radically different interfaces, compared on depth, locality, and seam placement).

Draw the module dependency diagram: driving adapters (HTTP, agent tools, jobs) into module interfaces, modules into their ports, ports to adapters, with every edge labelled by its port.

## 3. Write

Write `docs/architecture.md` from [TEMPLATE.md](TEMPLATE.md). It is done when:

- Every contract operation, including health checks and every agent tool, names one method on one module's interface.
- Every spec rule names the module that hides it.
- Every table names its owning module, and every figure that is not stored names the interface method that calculates it.
- Every module shows its deletion-test verdict.
- Every seam lists at least two adapters, or is internal to its module and absent from the module's interface.
- The dependency diagram is acyclic, and every cross-module edge is a named port that exchanges plain values.
- Every module interface states its inputs, its ownership-scope invariant, its errors, and any ordering constraint.
- Every contract error maps to one typed error, and domain code never mentions HTTP.
- Every multi-table write in the schema names the one module that owns its transaction.
- The test surface and the test adapters (clock, external services, persistence) are named.
- A lint rule or architecture test is named that fails the build on a forbidden import.

## 4. AGENTS.md

Invoke `/writing-for-agents`, then write or amend `AGENTS.md` at the project root. It carries only what every coding session needs: context pointers to each chain doc and `CONTEXT.md`, each worded with the condition for reading it, plus the few architecture rules that the enforcement in branch 13 does not already catch. `docs/architecture.md` stays the single source of truth. When the project also uses Claude Code, offer a `CLAUDE.md` that contains only `@AGENTS.md`.

Then close the stage as CHAIN.md describes. The next step is `/to-tickets`.
