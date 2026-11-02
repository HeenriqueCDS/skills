# Looks deletable, stays

Check before every delete in step 2 of [test-audit](SKILL.md). A test stays when it guards a behaviour someone depends on, even if it matches a smell's shape. The tell: the red question has a real answer.

| Shape | Looks like | Stays because |
|-------|-----------|---------------|
| A getter re-read on every call (token, URL, config source) and a test that changes the source between calls | S1 / S3 | A refresh depends on it. Caching the value once is the one-line bug it catches. |
| A small table that is really a decision: which errors reconnect and which are fatal | S2 | Each row is a product rule; moving one code to the wrong side is a real bug. Keep the rows that carry the decision. |
| Exact issue strings from a parser for each malformed input | S9 | The string is the only proof each input fails for its own reason, not the first check catching everything. |
| Contract options passed to a library, e.g. the library's own reconnection disabled because ours owns it | S4 / S9 | Removing the option silently doubles behaviour; the assertion is the contract with the library. |
| A spec proving secrets, tokens or audio payloads never reach logs | S9 | Data-leak guard. Keep it however literal it looks. |
| A view-model table with branching (status + flags → label and actions) | S2 / S5 | Branching logic lives there. A pure label table (key → text, no branches) is S1 and goes. |

When a keeper is noisy, trim it to the rows or assertions that carry the decision rather than deleting it.
