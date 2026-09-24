# `docs/architecture.md` template

```markdown
# Architecture

<Opening paragraph: what this doc decides (modules, seams, dependency rules, errors, transactions,
test surface, layout) in the vocabulary of deep modules; that behaviour, quality properties, the
contract, and the schema live in the upstream docs; which ADRs it builds on.>

<Whimsical link to the module dependency diagram, when drawn.>

## 1. Inherited decisions
Runtime, framework, and library choices, each citing its ADR.

## 2. Modules
Per module: its interface (operations, inputs, scope invariant, errors, ordering), what it hides,
the tables it owns, and its deletion-test verdict.

## 3. Dependency diagram
Mermaid flowchart: driving adapters → module interfaces → ports → adapters, edges labelled.

## 4. Seams and adapters
| Seam | Dependency category | Production adapter | Test adapter |

## 5. Layering and import rules

## 6. Composition root

## 7. Validation

## 8. Errors
| Contract identifier | Typed error | Status |

## 9. Transactions
| Write | Owning module | Tables |

## 10. Test surface
Where tests cross in, test adapters, test types, and what gets no test.

## 11. Folders and naming
The tree of one fully built module, as an example.

## 12. Enforcement
The rules that fail the build.

## 13. Operation map
| Contract operation or agent tool | Module | Interface method |

## 14. Deferred

## 15. Open points
```

ADRs hold rejected alternatives someone will reopen (few modules versus many, a framework choice). The operation map and the folder tree stay here.
