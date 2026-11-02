# Smells

The ten low-value test smells, for step 2 of [test-audit](SKILL.md). Each reads: what it is → why it is low value → how to spot it → what to do. A smell is a reason to look, then KEEPERS.md decides.

Framework-agnostic: `it`/`test`, `expect`, `toHaveBeenCalled`, `it.each`, `toMatchSnapshot` read the same in Jest, Jasmine, Vitest and Playwright unit tests.

## S1 Tautological / restating

Asserts a value the code states literally: a config default, a constant, an enum value, a lookup table entry.
→ Passes by construction; the only change that turns it red is an intended edit to the literal.
→ The expected value is copied from the production file.
→ Delete. If a value matters to a caller, test the behaviour it drives.

```ts
it('has default timings', () => {
  expect(RECORDER_CONFIG.chunkMs).toBe(250);
  expect(RECORDER_CONFIG.reconnectDelayMs).toBe(1000);
});
```

## S2 Mirrors the implementation

The test recomputes or re-lists what the code does: the same table, the same formula, the same branch order.
→ No oracle; a bug in the code is copied into the expectation.
→ `it.each` rows that match a production map row for row; expected values built with the code's own helpers.
→ Delete the restated rows; keep a test for each real decision (fallback for an unknown key, a boundary).

```ts
it.each([
  ['NETWORK', 'recorder.error.network'],
  ['MIC_DENIED', 'recorder.error.micDenied'],
])('%s maps to %s', (code, key) => expect(errorKey(code)).toBe(key));
```

Keep instead: `expect(errorKey('SOMETHING_NEW')).toBe('recorder.error.generic')`.

## S3 Tests the framework or language

Proves Angular, TypeScript, RxJS or the runtime work.
→ The framework has its own tests; ours add nothing.
→ `TestBed.inject(TOKEN)` returns its `useValue`; a one-line `InjectionToken` factory returns its default; `Object.isFrozen` after `Object.freeze`; a barrel exports a symbol; a signal holds what was `set`.
→ Delete.

## S4 Mock-heavy "was called"

Asserts that a collaborator we own was called, instead of what changed.
→ Couples to wiring; survives the bug where the call happens with the wrong effect.
→ `expect(store.dispatch).toHaveBeenCalled()`, `toHaveBeenCalledWith` on our own services, more spies than assertions on output.
→ Rewrite to assert the resulting state, emitted value or rendered output. Calls across a system boundary (HTTP, browser APIs, a third-party library) may stay.

## S5 Exhaustive combinatorial table

Every state × event (or input × flag) asserted back.
→ Restates the transition table; the handful of rules that matter drown.
→ A grid-shaped `it.each` with dozens of rows, most saying "ignored".
→ Merge to the rules: illegal transitions rejected, terminal states stay terminal, the one transition per state that matters.

## S6 Snapshot of everything

A snapshot of a whole component, DOM tree or large object.
→ Nobody reads the diff; it is re-accepted on every change.
→ `toMatchSnapshot()` on a full fixture or `fixture.nativeElement`.
→ Rewrite as targeted assertions on the text or attributes a user depends on, or a small inline snapshot.

## S7 Never red

No plausible code change makes it fail.
→ Pure cost.
→ Ask the red question. Classic shapes: `expect(component).toBeTruthy()` when other tests already create the component; `toBeDefined()` on a constructed object; assertions inside a `subscribe` that never emits; an async test that does not await.
→ Delete, or rewrite so it can fail. A lone "should create" in a file is a DI smoke test and stays.

## S8 Duplicated across layers

Re-asserts a mapping or rule a lower layer's spec already covers.
→ One change breaks two specs; the upper one adds no oracle.
→ A view-model or component spec re-listing what the mapper spec lists.
→ Delete the duplicate; keep the upper spec for what the upper layer adds (branching, composition).

## S9 Over-specified incidental detail

Pins detail no caller depends on: exact log text, call order, call counts, private field values.
→ Breaks on refactors that keep behaviour (Meszaros: Overspecified Software).
→ `toHaveBeenCalledTimes(3)`, `toHaveBeenNthCalledWith`, full log strings, `component['privateField']`.
→ Loosen to the observable contract, or delete.

## S10 Tests the test double

The assertion checks what a fake or stub computed, with no production code in between.
→ Proves the fake works.
→ Arrange the fake to return X, assert X; state only the fake's own logic produced.
→ Delete, or move the assertion to the production code's output.

## Sources

- Vladimir Khorikov, *Unit Testing Principles, Practices, and Patterns* (the four pillars: protection against regressions, resistance to refactoring, fast feedback, maintainability).
- Kent Beck, *Test Desiderata*.
- Google Testing Blog, "Change-Detector Tests Considered Harmful" (2015).
- Martin Fowler, "Mocks Aren't Stubs".
- Gerard Meszaros, *xUnit Test Patterns* (Overspecified Software).
- Kent C. Dodds, "Testing Implementation Details" and "Effective Snapshot Testing".
- Ouédraogo et al., "Test smells in LLM-generated unit tests", arXiv 2410.10628.
- Alshahwan et al., "Automated Unit Test Improvement using Large Language Models at Meta", arXiv 2402.09171.
- Checklist this catalogue comes from: https://claude.ai/artifact/LtZX8dS3rDoeWSZfMY3xvy
