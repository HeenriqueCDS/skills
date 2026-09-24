# Server structure branches

One entry per branch, in interview order. Each gives what to **decide** and the **default** to recommend, in the `/codebase-design` vocabulary. Defaults are stack-agnostic; the user's stack arrives through branch 1 and existing ADRs.

## 1. Runtime and framework

- **Decide:** language, runtime, HTTP framework, dependency-injection approach, validation library, test runner, and one deployable or several. An existing ADR settles any of these: cite it, never reopen it.
- **Default:** one deployable (a modular monolith). Modularity is a property of the code, not of the deployment. A framework or library choice that is hard to reverse becomes an ADR.

## 2. Module boundaries

- **Decide:** the modules, from the derived candidates and their deletion-test verdicts.
- **Default:** cluster by shared language and one synchronous consistency scope (Evans: a model holds inside a bounded context). Few deep modules beat many shallow ones. Split entities that share a language and a transaction only when the deletion test says keep. Liveness checks are a route, not a module.

## 3. Module interfaces

- **Decide:** for each module, its small interface: the operations callers use, their inputs, the ownership-scope invariant, errors, ordering constraints.
- **Default:** the interface speaks the glossary and plain values. Internal types (entities, repositories) stay behind it. Ask of each: fewer methods? simpler parameters? more hidden inside?

## 4. Seams and adapters

- **Decide:** every seam, and the adapters at each one.
- **Default:** a seam is real only with two adapters. Classify each dependency (`/codebase-design` DEEPENING.md): in-process computation gets no port; persistence is local-substitutable (a real or embedded database in tests, or an in-memory adapter); third-party services (key management, email, payments) get a port with a production and a fake adapter. The clock is a seam whenever a rule depends on "now" or "this month". A one-method "is this id in use?" port between modules is usually a sign the modules should merge.

## 5. Layering inside a module

- **Decide:** the layers each module needs.
- **Default:** only layers that are different abstractions. Domain rules, then orchestration where a use case actually coordinates a transaction and ports. HTTP and persistence are adapters around the module. Layer depth varies per module; a pass-through layer is a red flag.

## 6. Dependencies between modules

- **Decide:** call style between modules and the dependency direction.
- **Default:** synchronous in-process calls through the provider's interface, or through a port the consumer owns, joined only in the composition root. Plain values cross the seam, never another module's entities. The graph is acyclic. Domain code imports nothing outward. Messaging only when a real need for autonomy exists.

## 7. Composition root

- **Decide:** where adapters are chosen and wired.
- **Default:** one composition root for production and one for tests, over the same source. Each module exports its own registrations. No module builds its own dependencies.

## 8. Validation placement

- **Decide:** where input shape is checked, and where business rules are checked.
- **Default:** a schema library parses shape only at driving adapters (HTTP, agent tools, environment). Business invariants live inside the module and are checked once, there.

## 9. Error model

- **Decide:** how failures travel from domain to client.
- **Default:** typed errors carrying the contract's stable identifier; one error-mapping adapter per transport turns them into status codes and problem details. HTTP status is not a domain concept. Unknown errors become `500` with no internals leaked, and are logged.

## 10. Transaction boundaries

- **Decide:** who opens and commits each transaction, especially the multi-table writes listed in the schema.
- **Default:** one transaction per call on a module interface. A write that spans two modules means the boundary is wrong, or one module owns the transaction and the other joins through a port.

## 11. Test surface

- **Decide:** where tests cross into the code, which adapters they use, and which test types exist.
- **Default:** the module interface is the test surface. Tests assert observable state through in-memory or embedded adapters with a fixed clock; mocks only for true externals without a fake. A few transport-level tests cover authentication scope, error mapping, and wiring. Each second adapter gets a thin contract test proving it satisfies the interface. Tests on internal parts that the interface already locks are waste (DEEPENING.md: replace, don't layer).

## 12. Folders and naming

- **Decide:** folder layout and file naming.
- **Default:** package by module (`src/modules/<module>/`), one entry file that is the module's interface, internal layout hidden. File and symbol names follow the glossary.

## 13. Enforcement

- **Decide:** what fails the build when the structure is broken.
- **Default:** compiler first, then a lint rule or architecture test that forbids deep imports into another module and forbids domain code from importing the framework, validation library, container, or database driver. Prose and review come last.

## Sources

Ousterhout, _A Philosophy of Software Design_ (deep modules, pass-through layers, design it twice). Cockburn, Hexagonal Architecture. Feathers, _Working Effectively with Legacy Code_ (seams). Evans, _DDD Reference_. Fowler: PresentationDomainDataLayering, TestPyramid, Mocks Aren't Stubs. Grzybek, modular monolith series. Brown, package by component.
