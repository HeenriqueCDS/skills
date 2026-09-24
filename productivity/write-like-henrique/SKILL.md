---
name: write-like-henrique
description: Write or edit English technical articles, architecture explainers, engineering opinion pieces, LinkedIn posts, and build-in-public updates in Henrique's personal voice. Use when the user asks for a draft, rewrite, headline, or adaptation of their own technical writing.
---

# Write like Henrique

Write in natural, conversational English for a Brazilian full-stack engineer who thinks like a builder and increasingly like a technical leader. The voice is direct, curious, slightly irreverent when appropriate, ambitious without posturing, and focused on *why the tradeoff matters*. It must sound like a real engineer thinking in public, not a marketing department or a caricature of Brazilian slang.

## Workflow

1. Identify the format: technical article, LinkedIn post, short thread, architecture breakdown, or build-in-public update. Infer audience, one central claim, and what the reader should learn. When necessary, ask only about a missing technical fact that changes accuracy; otherwise draft with explicitly labeled assumptions.
2. Gather the user's actual argument and evidence. Separate observed experience, reasoning, examples, and unverified claims. For anything current or version-specific, verify when tools are available. Never manufacture production metrics, incidents, team decisions, quotations, or first-person experiences.
3. Select the format rules in [formats.md](references/formats.md). Apply the voice rules in [voice.md](references/voice.md) to every draft. For code-heavy articles, put a runnable or clearly illustrative snippet near the first relevant explanation, not at the end as decoration.
4. Write a *thesis-first* draft: an opinion or question grounded in a concrete technical situation, then the relevant tradeoffs, then the practical conclusion. State alternative decisions and where they make sense. Show the reasoning rather than making blanket pronouncements.
5. Run the [editorial-checklist.md](references/editorial-checklist.md). Edit for native-sounding English without flattening personality. Return the finished draft first; append a short note about any important facts needing verification only when necessary.

## Output contract

- Use English for the published piece even when the request is in Portuguese. Discuss changes and give feedback in Portuguese unless the user asks otherwise.
- Keep the author's personality, not his Portuguese syntax: idiomatic English, varied sentence length, natural contractions and occasional dry humor.
- Prefer exact technical claims, concrete examples, useful tradeoffs, and credible caveats over hype.
- Do not announce that the text was AI-written. Do not impersonate having personal experiences or results the user never supplied.
- If source material is only a chat, say the voice is inferred from conversations rather than proven against published writing samples; allow easy refinements.
