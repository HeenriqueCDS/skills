---
name: shape-database-model
description: Stage 3 of the shape chain. Grills the relational schema (tenancy, keys, types, constraints, encryption, indexes, retention), then writes docs/database.md.
disable-model-invocation: true
---

Stage 3 of the chain in [CHAIN.md](../shape-project/CHAIN.md). Read it first: it governs upstream reading, amend mode, contradictions, doc conventions, diagrams, and closing for every stage.

This stage decides where data lives and what the database itself guarantees: tables, columns, keys, constraints, encrypted columns, indexes, and retention. It never changes a business rule, a quality property, or a route. It does not pick an ORM or a migration tool.

## 1. Derive before asking

Build two tables from the upstream docs before the first question, and show them to the user:

- **Entity map:** every spec entity becomes a table or is listed as _not stored_ (a pure function of stored rows). Each relationship becomes a foreign key with its cardinality.
- **Access-pattern table:** from the contract, every read by id, list filter plus sort, uniqueness check, "in use" delete check, token lookup, purge, and multi-row write, with the rows it touches.

When the spec or contract is missing, grill the entities or access patterns this stage needs, and record them under **Assumptions**.

## 2. Grill

Run `/grilling` with `/domain-modeling`. Walk these branches in order. Before the first question of a branch, read its entry in [BRANCHES.md](BRANCHES.md): what to decide and the default to recommend.

1. Engine and version floor
2. Tenancy and isolation
3. Entities and tables
4. Keys
5. Types
6. Database versus application enforcement
7. Derived data
8. Sensitive columns
9. Deletion
10. Auth and ephemeral state
11. Indexes
12. Volume and scale
13. Retention and purge
14. Evolution

Challenge every "where does this live" answer against the NFR doc's classification, its capacity numbers, and its cost ceiling. Scale answers use two axes: user count, and rows one owner's request must read.

Draw an entity-relationship diagram. In Whimsical, draw each table as a table with a distinct header colour, and connect foreign keys.

## 3. Write

Write `docs/database.md` from [TEMPLATE.md](TEMPLATE.md). It is done when:

- Every spec entity is a table, or is listed under _not stored_ with the read that recalculates it.
- Every spec invariant is a named constraint with its predicate, or an application rule with the reason the database cannot hold it (encrypted value, cross-row rule, external catalogue).
- Every row of the access-pattern table names its index, or an accepted sequential scan with the reason.
- Every foreign key states both `ON DELETE` and `ON UPDATE`, and every referencing column used by a delete check is indexed.
- Every contract promise about durability, replay, or destruction matches a column, or is written as a residual risk.
- Every encrypted column states its plaintext format, its key, and the rules that moved to the application.
- Scale states the user count and the rows per owner per request, and names the number that reopens the single-node decision.
- Every ephemeral table names its purge predicate and the index the purge uses.
- **Open points** holds only facts the spec left undecided.

Then close the stage as CHAIN.md describes. The next skill is `/shape-server-structure`.
