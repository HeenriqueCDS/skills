# `docs/spec.md` template

Organise rules by functional area, not as a backlog. Stories name what the user wants and are numbered so later docs can trace them (the API contract maps each story to an operation). Rules are normative: when a story and a rule disagree, fix the story.

```markdown
# <Product name>

<Opening paragraph: what this spec decides (behaviour and business rules), what it leaves to
docs/non-functional-requirements.md, docs/api-contract.md, docs/database.md, and
docs/architecture.md, and that vocabulary lives in CONTEXT.md.>

## 1. Problem and outcome
The status quo, from the user's side, and what changes when this ships.

## 2. Actors
Who acts, who is affected, who must never act.

## 3. Scope
What is in. No-gos go in §12.

## 4. Ownership and privacy
The unit of ownership and what never crosses it.

## 5. User stories
1. As a <actor>, I want <capability>, so that <benefit>. (Rules: §7.2, §7.5)

## 6. Entities and lifecycle
Per entity: owner, states, legal transitions, the commands that cause them, editable and immutable
attributes. A kind-by-state decision table wherever kinds and states combine.

## 7. Rules
One subsection per functional area. Each rule is one sentence, followed by its examples:
- Accepted: <inputs> → <outcome>
- Refused: <inputs> → <refusal>
- Boundaries: below / on / above

## 8. Calculations
Formula, inputs, excluded inputs, recalculation trigger. One worked fixture with numbers,
including a zero, a negative, and an empty case.

## 9. Defaults
What a new owner starts with.

## 10. Correction
Edit, rename, delete, and revert semantics, and their effect on calculations.

## 11. Cross-cutting scenarios
A short confirmation suite that combines rules ("the one where rent is paid two months early").

## 12. No-gos
Declined behaviour, each named precisely.

## 13. Handoff
Answers that belong to later stages, grouped by the stage that owns them.

## 14. Open points
Empty when the spec is done.
```

Leave out: frameworks, authentication mechanisms, encryption, schema, routes, payloads, screens, and test-runner design.
