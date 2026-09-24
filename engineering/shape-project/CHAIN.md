# The shape chain

Shared reference for the four stage skills and the `shape-project` router. Each stage grills the user, then writes one layer of the design. Each layer is optional input to the next.

## Stages

| # | Skill | Writes | Reads when present |
| --- | --- | --- | --- |
| 1 | `/shape-system-design` | `docs/spec.md`, `docs/non-functional-requirements.md` | `CONTEXT.md`, `docs/adr/`, existing code |
| 2 | `/shape-api-contract` | `docs/api-contract.md` | everything above, plus stage 1 |
| 3 | `/shape-database-model` | `docs/database.md` | everything above, plus stages 1–2 |
| 4 | `/shape-server-structure` | `docs/architecture.md`, `AGENTS.md` | everything above, plus stages 1–3 |

Every stage also keeps `CONTEXT.md` (glossary) and `docs/adr/` current through `/domain-modeling`. Paths are relative to the project root. When the project keeps its docs somewhere else (a service folder in a monorepo, an umbrella workspace), ask once at the start of the session and use that location for every doc.

## Upstream docs

Earlier docs are settled decisions. Read every one that exists before the first question, and treat what they state as looked-up facts, never as questions to re-ask.

When an earlier doc is missing, grill only the upstream facts this stage cannot proceed without, and record each one in this stage's doc under **Assumptions**, naming the stage that owns it. When that stage runs later, it confirms or overturns each assumption and removes it.

## Amend mode

When this stage's doc already exists:

1. Read it, then ask what changed and why the stage is running again.
2. Grill only the branches that change touches. Everything else stands.
3. Edit the doc in place. Keep section numbers stable, because other docs cite them (`docs/api-contract.md` §1.6).

## Contradictions

- **Upstream.** When an answer contradicts an earlier doc, stop and ask which wins. When the new answer wins, edit the earlier doc (and `CONTEXT.md`, if a term moved) in the same session.
- **Downstream.** Never edit a later doc. Instead, append each contradiction to a **Downstream impact** section at the end of this stage's doc: the later doc and section, what now disagrees, and the skill to rerun.
- **Clearing flags.** On entry, every stage reads the **Downstream impact** sections of earlier docs for entries aimed at it, resolves each one during the session, and deletes it from the earlier doc. Delete the section when it empties.

## Doc conventions

- Open with one paragraph: what the doc decides, what it deliberately leaves to other docs, and the paths of the upstream docs it builds on.
- Use `CONTEXT.md` terms exactly. An alias from the glossary's _Avoid_ list is a bug.
- Number sections so other docs can cite them.
- End with **Open points**: values still undecided that must be settled before implementation, each naming which stage or person settles it.
- Write decisions, not implementation. No code, except where a snippet states a decision more precisely than prose (a payload shape, a DDL constraint).

## Diagrams

Every stage draws. A Mermaid diagram inside the doc is always written, so the diagram is reviewed in git beside the text. A Whimsical diagram is recommended on top of it:

- Check whether the Whimsical MCP is connected. When it is not, or the user declines, keep the Mermaid diagram only and move on.
- Follow the MCP's own instructions for the diagram type (it requires a `how_to` call before flowcharts).
- Put the Whimsical link directly under the doc's opening paragraph.

## Closing a stage

1. Run the stage's completion criterion and fix every gap it finds.
2. Report downstream impact, if any, in the final message as well as in the doc.
3. Name the next skill in the chain. After stage 4, the next step is `/to-tickets`.
