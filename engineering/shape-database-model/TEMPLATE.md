# `docs/database.md` template

```markdown
# Database schema

<Opening paragraph: the engine and what this doc decides (tables, columns, keys, constraints,
encryption, indexes, retention). It changes no rule in docs/spec.md, no property in
docs/non-functional-requirements.md, and no route in docs/api-contract.md.>

<Whimsical link to the table diagram, when drawn.>

## 1. Engine and conventions
Version floor, extensions, naming, id generation, timestamp and date types.

## 2. Tenancy and isolation
Owner column, composite foreign keys, row-level security decision.

## 3. Encrypted columns
Which columns, algorithm, plaintext format, key hierarchy, additional authenticated data, and the
rules that moved to the application because of it.

## 4. Enums and closed sets

## 5. Tables
One subsection per table: purpose, then
| Column | Type | Null | Notes |
then its constraints written as predicates, and its indexes.

## 6. Relationships
Mermaid erDiagram, then
| From | To | Cardinality | ON DELETE | ON UPDATE |

## 7. Access patterns
| Operation | Predicate and sort | Rows touched | Index or accepted scan |

## 8. Not stored
Each derived value and the read that recalculates it.

## 9. Required transactions
Multi-row writes the schema expects to commit together.

## 10. Application-enforced invariants
| Invariant | Why the database cannot hold it |

## 11. Retention and purge
| Table | Purge predicate | Index |

## 12. Scale
Users, rows per owner, rows per request, and the number that reopens the design.

## 13. Evolution
Migration rules and choices that constrain deferred features.

## 14. Open points
```

Leave out: ORM, migration tool, connection pool size, instance class, cache TTLs, domain formulas, and HTTP error bodies.
