# Applying

Step 4 of [test-audit](SKILL.md), reached only when the user asked to apply. Work file by file from the step 3 table.

## Delete, merge, rewrite

- **Delete**: remove the test and any setup, fixtures, spies or imports only it used.
- **Merge**: fold into the named sibling, or into one short `it.each` whose rows each carry a rule.
- **Rewrite**: state the input, drive the public interface, assert the observable output against an oracle. Name the test for the behaviour ("falls back to the generic key for an unknown code"), not the mechanism.

Edit test files only. The two exceptions to touching production code: the temporary mutation below, and deleting code the audit shows is provably dead (no references left once its tests go, and the typecheck still passes without it).

## Mutation proof

Every rewritten or new assertion must go red once before you trust it:

1. Save the production file to a scratch directory outside the repo: `cp src/app/x.ts "$SCRATCH/x.ts.orig"`.
2. Break the behaviour the assertion claims with one small edit (flip a branch, drop a fallback, return the wrong key). It must compile.
3. Run the spec. It must fail **on that assertion**, not on a compile or setup error.
4. Restore: `cp "$SCRATCH/x.ts.orig" src/app/x.ts`, then confirm with `cmp` against the copy or `git diff --exit-code -- src/app/x.ts`.
5. Run the spec again: green.

An assertion that stays green under the mutation is never red (S7): rewrite it or drop it. Record each mutation in one line for the final report (`errorKey: removed generic fallback → red`).

## Finish

Run every affected spec and the repo's typecheck, using the scripts in `package.json`. Report per file `tests now → after`, the mutations run, and any production code deleted as dead.
