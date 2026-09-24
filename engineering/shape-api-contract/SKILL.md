---
name: shape-api-contract
description: Stage 2 of the shape chain. Grills the HTTP contract (resources, payloads, errors, auth transport, idempotency, agent tools), then writes docs/api-contract.md.
disable-model-invocation: true
---

Stage 2 of the chain in [CHAIN.md](../shape-project/CHAIN.md). Read it first: it governs upstream reading, amend mode, contradictions, doc conventions, diagrams, and closing for every stage.

This stage decides what crosses the wire: routes, payloads, status codes, error bodies, and the transport rules around them. It never changes a business rule (that is `docs/spec.md`) or a quality property (that is `docs/non-functional-requirements.md`). It never names tables, frameworks, or modules.

## 1. Derive before asking

Build the **traceability table** from the spec before the first question: for every user story, the operation that serves it, or "no operation" with the reason (a vocabulary story, a figure defined only in the spec, a no-go). For every entity, which stories create, read, update, delete, or forbid it. Show the user the candidate operations, then grill. When the spec is missing, grill the entities and their commands first, and record them under **Assumptions**.

## 2. Grill

Run `/grilling` with `/domain-modeling`. Walk these branches in order. Before the first question of a branch, read its entry in [BRANCHES.md](BRANCHES.md): what to decide and the default to recommend.

1. Clients and transports
2. Auth transport
3. Resource model
4. Field behaviour
5. Standard methods
6. Custom actions
7. Lists: filters, sort, pagination
8. Errors
9. Idempotency and concurrency
10. Versioning and change
11. Formats: ids, casing, money, dates
12. Limits, CORS, and headers
13. Agent tools (only when agents are a client)
14. Machine-readable description

Copy every invariant the spec attaches to an entity onto the operations that can break it (amount sign, required fields per kind, unique names, blocked deletes), each with the error it returns.

Draw a sequence diagram for every flow with more than one round trip or a hidden state change: sign-in, token refresh and reuse detection, idempotent replay, and any multi-step custom action.

## 3. Write

Write `docs/api-contract.md` from [TEMPLATE.md](TEMPLATE.md). It is done when:

- Every user story maps to an operation, or to "no operation" with a reason, in the traceability table.
- Every operation states method, path, auth, every request field (required, optional, immutable, output-only, and what `null` means), success status and body, and every error it can return.
- Every error in the catalogue is returned by at least one operation, and every operation's errors are in the catalogue.
- Every collection states its filters, its sort order, and either pagination or a hard maximum size.
- Every non-idempotent create states the idempotency key's scope, fingerprint, replay behaviour, mismatch response, and in-flight duplicate response, or states why none is needed.
- Money and dates are exact on the wire, including what a client's JSON parser must preserve.
- Auth transport, the `401` challenge, refresh rotation, and agent sign-in are decided, or **Deferred** states the v1 behaviour while they stay open.
- Every agent tool names its input schema, its REST equivalent, and its read-only or destructive hint.
- **Open points** holds only values that change no path, type, or error code.
- A client can be written from this doc alone, without the schema or the source tree.

Then close the stage as CHAIN.md describes. The next skill is `/shape-database-model`.
