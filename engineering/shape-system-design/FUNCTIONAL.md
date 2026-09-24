# Functional branches

One entry per branch of Part 1, in interview order. Each gives what to **decide**, the **default** to recommend when the user has no view, and the **probe** that stress-tests the answer. An unanswered branch parks under **Open points**. It is never invented in a later branch.

## 1. Problem and scope fence

- **Decide:** the status quo in one story, what success changes, and the appetite (how much product this is).
- **Default:** a problem statement short enough that every later answer can be checked against it.
- **Probe:** for any feature proposed later, ask which part of the problem it serves. If none, it is a no-go candidate.

## 2. Actors

- **Decide:** who acts, who is affected, who must never act. Include non-human actors: the calendar rolling over, a scheduled job, an external agent calling the product.
- **Default:** one human actor until a second one is named with a distinct goal.
- **Probe:** "Can anyone else ever see or change this?" asked for each actor pair.

## 3. Ownership and privacy

- **Decide:** the unit of ownership (user, household, organisation), what never crosses it, and whether sharing exists.
- **Default:** everything belongs to exactly one owner, and sharing is a no-go until someone needs it.
- **Probe:** invent a couple, a shared device, and a deleted owner. Ask what each one sees.

## 4. Language

- **Decide:** one canonical term per concept, with its forbidden aliases, written to `CONTEXT.md` before any rule uses it.
- **Default:** the word the user reaches for first, unless it is overloaded.
- **Probe (glossary trap):** restate a rule using a forbidden alias ("account", "budget", "transaction"). If the sentence still sounds right to the user, the term is not sharp yet. One spelling for two concepts is a conflict, not a synonym.

## 5. Entities, commands, and states

- **Decide:** for each entity, how it is created, its states, the legal transitions, and which entity owns which. Phrase what happens as past-tense events, what triggers them as commands, and automatic reactions as policies ("whenever X, then Y").
- **Default:** the fewest states that the rules need.
- **Probe (transition attack):** from every state, try every command. Done back to pending, rename onto an existing name, delete the last item of a list, edit across a period boundary.

## 6. Invariants

- **Decide:** the rules, each atomic: facts, constraints (what is refused), action enablers (what a state allows), inferences (what follows from what). Cascades live here: rename propagates, delete is blocked while in use, deleting an owner deletes its dependents.
- **Default:** refuse the ambiguous case rather than guess.
- **Probe (rule, example, counterexample):** state the rule, give an accepted example and a refused one. When the outcome of an example cannot be stated, it is a question, not an example. A rule that needs many examples is several rules.

## 7. Calculations

- **Decide:** every derived number: its formula, its inputs, and the inputs that deliberately do not participate. Whether it is recalculated from current data or frozen once computed.
- **Default:** derived from the data that exists now, never stored as an independent fact that can drift.
- **Probe (decision table):** build a table of entity kind by state, with which figures each cell moves. An empty cell is an unasked question.

## 8. Boundaries

- **Decide:** every threshold: amounts, counts, lengths, dates, horizons.
- **Default:** a closed range with both ends stated.
- **Probe (boundary set):** for each threshold, one value just below, one on, one just above. Add the date edges: end of month, leap day, time zone midnight. Pick the smallest set that covers each rule, not every combination.

## 9. Defaults

- **Decide:** what a new owner starts with, before any command runs.
- **Default:** the minimum that lets the first real action succeed without setup.
- **Probe:** check each default against every invariant. A default that can be renamed, deleted, or emptied needs its own correction rule.

## 10. Correction: edit, rename, delete, revert

- **Decide:** which fields are editable and which are immutable, what rename does to everything that shows the name, what delete does to dependents, and whether each state change can be undone. What each correction does to derived figures.
- **Default:** edits recalculate everything derived. Delete is refused while something depends on the item.
- **Probe:** pick an item referenced by many others, then edit, rename, and delete it, one at a time.

## 11. No-gos

- **Decide:** the behaviour deliberately declined, each named precisely enough that a later reader cannot mistake it for an oversight.
- **Default:** everything raised and not agreed.
- **Probe:** state that behaviour outside the spec is undefined, and ask whether any legacy behaviour must survive. Each yes becomes a rule with an example.

## Sources

ISO/IEC/IEEE 29148 (requirement and set characteristics). Wiegers, _Software Requirements_ (business-rule taxonomy). Wake, INVEST; Cohn, acceptance criteria. Wynne, Example Mapping. Adzic, _Specification by Example_ and key examples. Evans, ubiquitous language. Brandolini, EventStorming. Shape Up, appetite and no-gos.
