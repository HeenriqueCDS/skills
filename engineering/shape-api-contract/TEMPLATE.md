# `docs/api-contract.md` template

```markdown
# API contract

<Opening paragraph: the clients and transports this contract serves; business rules live in
docs/spec.md, quality properties in docs/non-functional-requirements.md; this doc decides routes,
payloads, and error behaviour and changes no domain rule.>

<Whimsical link to the flow diagrams, when drawn.>

## 1. Conventions
1.1 Base path and transport · 1.2 Ownership scoping and non-disclosure · 1.3 Formats (ids, casing,
dates, money) · 1.4 Field behaviour (omission, null, unknown fields) · 1.5 Lists (sort, pagination
or maximum) · 1.6 Errors (body shape, identifier, validation detail) · 1.7 Idempotency ·
1.8 Concurrency · 1.9 Versioning · 1.10 Limits, CORS, and headers

## 2. Authentication
Token transport, the `401` challenge, each auth operation, and a Mermaid sequence diagram per flow.

## 3.–N. One section per resource
The resource shape, then a table: method | path | auth | body | success. Then behaviour: field
rules, invariants copied from the spec, and the errors each operation returns.

## N+1. Custom actions
Only those not already listed under their resource.

## N+2. Error catalogue
| Status | Identifier | When | Returned by |

## N+3. Agent tools
| Tool | Input | REST equivalent | Hints |
Plus what is deliberately not exposed.

## N+4. Traceability
| Story | Operation or "no operation" | Reason |

## N+5. Deferred
Decided-later items, each with the v1 behaviour meanwhile.

## N+6. Open points
Only values that change no path, type, or error code.
```

Leave out: tables, indexes, encryption mechanics, frameworks, module layout, infrastructure, and screens.
