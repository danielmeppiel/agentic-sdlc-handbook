# The Agentic SDLC Handbook

A comprehensive guide to AI-native software development for engineering leaders and practitioners.

**[Read online](https://danielmeppiel.github.io/agentic-sdlc-handbook/)** | **[Download PDF/EPUB](https://danielmeppiel.github.io/agentic-sdlc-handbook/download.html)**

By [Daniel Meppiel](https://www.linkedin.com/in/danielmeppiel/) — Global Black Belt at Microsoft, creator of [APM](https://github.com/microsoft/apm).

## What's Inside

```
Part I:   The Foundation — the agentic SDLC thesis
Part II:  For Leaders — strategy, ROI, governance, team structures
Part III: For Practitioners — techniques, workflows, tooling, patterns
Closing:  What Comes Next
```

15 chapters. 225+ pages. From "why AI-native development isn't just using Copilot" to the PROSE specification framework, multi-agent orchestration, and enterprise-scale governance.

---

## How This Book Was Made

This handbook practices what it preaches. It was produced using an **AI-native editorial pipeline** — the same agentic methodology the book teaches. Every claim, framework, and recommendation in these pages was shaped through a process that demonstrates the Agentic SDLC in action.

### The Author's Domain Context

The agents didn't work in a vacuum. They were grounded in the author's IP and field experience:

- **The [PROSE framework](https://danielmeppiel.github.io/agentic-sdlc-handbook/handbook/ch10-the-prose-specification.html)** — a specification methodology for writing AI agent instructions, developed through building APM
- **[APM](https://github.com/microsoft/apm) architecture and design** — lessons from building and maintaining a developer tool under the `microsoft` org (700+ stars, real-world adoption)
- **Enterprise adoption patterns** — drawn from strategic Agentic SDLC conversations with enterprise customers, GitHub Copilot adoption workshops, and AI-native development hackathons
- **Reference architecture research** — cross-vendor analysis of how AI-native development actually works at scale

The agents amplified a signal that already existed. They didn't manufacture one from noise.

### The Agent Team

11 specialist AI agent personas, each with a distinct role and editorial mandate. Defined as [PROSE agent specifications](.github/agents/) and orchestrated via the [`handbook-panel`](.github/skills/handbook-panel/) skill:

| Agent | Role | What They Do |
|-------|------|-------------|
| **Chief Editor** | Narrative Architect | Owns voice, arc, and flow. Cuts bloat. Enforces consistency across all 15 chapters |
| **C-Suite Strategist** | Executive Writer | Drafts the Leaders block. Frames everything in business outcomes and competitive moats |
| **Practitioner Authority** | Technical Writer | Drafts the Practitioners block. Ensures every technique is battle-tested, not theoretical |
| **CTO Proxy** | Skeptical Reader | Reviews leader chapters asking "so what?" and "prove it" — rejects fluff |
| **Dev Lead Proxy** | Impatient Reader | Reviews practitioner chapters asking "can I use this Monday?" — rejects theory without code |
| **Market Analyst** | Competitive Intel | Validates vendor claims against market reality. Enforces multi-vendor objectivity |
| **Platform Strategist** | Architecture Analyst | Evaluates reference architectures. Flags shipped vs. aspirational capabilities |
| **Fact & Ref Checker** | Claims Auditor | Hunts unverified claims, unsourced statistics, and assertions presented as fact |
| **Illustrator** | Visual Strategist | Identifies where diagrams accelerate comprehension. Specs Mermaid diagrams |
| **Thought Leadership** | Voice Reviewer | Ensures the author's voice stays distinctive — not generic "AI best practices" |
| **Publishing Advisor** | Distribution Strategist | Advises on publishing path, format decisions, and launch sequencing |

### The Pipeline

Each chapter went through a multi-stage pipeline where **agent personas were instantiated as parallel fleets** — the same persona running independently on different chapters simultaneously, then results synthesized:

```
┌─────────────────────────────────────────────────────────────┐
│  Stage 1: DRAFTING                                          │
│                                                             │
│  C-Suite Strategist ──→ Ch 2, 3, 4, 5, 6, 7  (parallel)   │
│  Practitioner Auth.  ──→ Ch 8, 9, 10, 11, 12, 13, 14       │
│                                                             │
│  Each chapter injected with:                                │
│  • PROSE framework spec    • APM design notes               │
│  • Enterprise field notes  • Workshop observations          │
├─────────────────────────────────────────────────────────────┤
│  Stage 2: ADVERSARIAL REVIEW                                │
│                                                             │
│  CTO Proxy fleet ──→ reviews all Leader chapters            │
│  Dev Lead Proxy fleet ──→ reviews all Practitioner chapters │
│                                                             │
│  "So what?" / "Prove it" / "Can I use this Monday?"        │
├─────────────────────────────────────────────────────────────┤
│  Stage 3: SPECIALIST AUDIT (parallel)                       │
│                                                             │
│  Market Analyst ──→ vendor balance + claim validity          │
│  Fact Checker   ──→ unverified claims + stat validation      │
│  Illustrator    ──→ visual opportunities + diagram specs     │
├─────────────────────────────────────────────────────────────┤
│  Stage 4: INTEGRATION REVIEW                                │
│                                                             │
│  Chief Editor ──→ full-manuscript arc, voice, bloat check   │
│  Thought Leadership ──→ author voice + positioning          │
│  Both proxies ──→ final "would I read this?" check          │
├─────────────────────────────────────────────────────────────┤
│  Stage 5: AUTHOR CHECKPOINT                                 │
│                                                             │
│  Author reviews all agent outputs, accepts/rejects/rewrites │
│  Agent recommendations ≠ final content                      │
│  Every word published is author-approved                    │
└─────────────────────────────────────────────────────────────┘
```

### The Artifacts

The review artifacts are in the repo — raw, unedited:

- [`handbook/reviews/ch*`](handbook/reviews/) — chapter-by-chapter editorial reviews from CTO Proxy, Dev Lead Proxy, and Chief Editor
- [`handbook/reviews/fact-check-*`](handbook/reviews/) — structured claim audits (Verified / Qualified / Unverified)
- [`handbook/reviews/visual-audit-*`](handbook/reviews/) — diagram specifications and visual density analysis
- [`handbook/reviews/integration-*`](handbook/reviews/) — full-manuscript consistency reviews

### Why Show This?

Because a book about AI-native development that hides its AI-native process would be dishonest.

The agents are the infrastructure. The methodology, opinions, and 14 years of field experience — from CERN to GitHub to founding an AI startup to Microsoft — are the author's. Every reader can inspect the full pipeline, see exactly how the editorial process worked, and judge the output on its merits.

---

## Development

This handbook is built with [Quarto](https://quarto.org) and uses [APM](https://github.com/microsoft/apm) to manage the agent team:

```bash
apm install    # Installs the handbook-agents panel
apm compile    # Compiles agent instructions
```

The agent team is distributed as the [`handbook-agents`](https://github.com/danielmeppiel/handbook-agents) APM package.

## License

The content of this book (prose, diagrams, images) is licensed under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
You are free to share it with attribution.

Build tooling and scripts are MIT licensed.

For commercial use, translations, or adaptations, please [reach out](https://www.linkedin.com/in/danielmeppiel/).
