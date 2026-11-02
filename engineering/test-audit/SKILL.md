---
name: test-audit
description: Audit unit tests for low-value, AI-style tests (restating, change-detector, never red) and prune them when asked. Use when the user wants to audit, prune or clean up specs, asks which tests are useless, or a review covers test files.
---

A test earns its upkeep when it states an input and checks the observable output: how the code reacts. Its expected value comes from an **oracle**, a source other than the code under test (the spec, a worked example, a known-good literal). A test that reads its answer off the code is a **change-detector**: red on every edit, red on no bug.

The rule: test inputs and outputs, and leave alone what is explicit in the code. Hard-coded values, config literals and defaults, constants, enum values, lookup tables entry by entry, one-line DI token factories, framework or language behaviour, state only a fake computed: each of these is already its own specification. Henry's canonical examples: a recorder-config spec asserting the default timings, and an error-key spec restating a code→key table.

The red question, asked of every test: **what one-line change to production code would make this fail usefully?** No answer means it is never red.

Reference, read before step 2:

- [SMELLS.md](SMELLS.md): the ten smells (S1–S10), how to spot each, and sources.
- [KEEPERS.md](KEEPERS.md): tests that look deletable but stay.
- [APPLYING.md](APPLYING.md): read before step 4; delete, merge, rewrite and the mutation proof.

## Process

### 1. Scope

Take the files the user names. Otherwise pin a fixed point (ask if none was given) and list the specs changed since it:

```bash
git diff <ref>...HEAD --name-only -- '*.spec.ts' '*.test.ts'
```

Read each spec and the production file it covers. Done when you hold a list of spec files, each with its test count.

### 2. Audit

Give every `it`/`test` one verdict: **keep**, **delete**, **merge** (into a named sibling or a short `it.each`), or **rewrite** (as a behaviour test, with the input and oracle stated). Cite the smell number and `file:line` for every non-keep verdict, and check KEEPERS.md before each delete.

Stay conservative: a simple input→output test with an independent expected value stays, however small. Doubt resolves to keep, with a one-line note. Done when every test in scope has a verdict.

### 3. Report

One table per file, then the counts:

```
### src/app/recording/recorder-config.spec.ts — 9 → 2
| Line | Test | Verdict | Smell | Why / replacement |
|------|------|---------|-------|-------------------|
| 12 | has default chunk timing | delete | S1 | asserts the literal in RECORDER_CONFIG |
| 40 | retries after a dropped socket | keep | | input → reconnect observed |
```

Close with totals (`files, tests now → after, deletes / merges / rewrites`) and the riskiest call. Stop here unless the user asked to apply.

### 4. Apply

Only when asked. Follow APPLYING.md: delete, merge, rewrite, and prove every rewritten or new assertion can go red by breaking the code once, then restore it byte for byte. Production code changes only when it becomes provably dead.

### 5. Verify

Run every affected spec and the repo's typecheck. Done when both are green and `git diff` shows production code untouched apart from provably dead deletions. A red spec after a rewrite means the rewrite or the code is wrong: find which and fix it, keeping the assertion as strong as you wrote it. Loosening an assertion to get green is never the fix.

## Large suites

Fan out one `general-purpose` sub-agent per folder, in parallel. Give each the folder, the principle above, the paths to SMELLS.md and KEEPERS.md, and the brief: "Run steps 1–3 of test-audit on these files; return the tables only." Merge their tables into one report. When applying, sub-agents may apply in disjoint folders; run step 5 yourself across the whole set.

## As a code-review axis

The `code-review` skill reviews on two parallel axes, Standards and Spec. When the diff touches `*.spec.ts` or `*.test.ts`, it (or a `reviewer` agent) can add **Tests** as a third parallel sub-agent with:

- the diff command and the changed spec list from step 1;
- the paths to SMELLS.md and KEEPERS.md;
- the brief: "Audit only: run test-audit steps 2–3 on these specs, judging only tests the diff adds or changes. Cite smell and file:line per finding. Under 400 words."

Its report sits under `## Tests`, beside the other two axes and unmerged. Fixes wait for a separate `/test-audit` run with apply.
