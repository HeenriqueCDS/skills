---
name: shape-project
description: Router for the shape chain (shape-system-design, shape-api-contract, shape-database-model, shape-server-structure). Shows where the project stands and which stage to run next.
disable-model-invocation: true
---

Read [CHAIN.md](CHAIN.md). It defines the stages, the docs each one writes, and how they hand off.

1. Locate the project's docs folder. For each stage, record whether its doc exists, and whether any earlier doc holds a **Downstream impact** entry aimed at it or an **Assumptions** entry it owns.
2. Report one line per stage: the skill, its doc paths, and a status of _missing_, _written_, or _flagged_ (with the flag's source).
3. Recommend the next skill: the earliest stage that is missing or flagged. When every stage is written and nothing is flagged, recommend `/to-tickets`.

You can only point. The user starts the stage by typing its name.

Done when every stage has a status and exactly one next step is named.
