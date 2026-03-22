---
name: handbook-panel
description: >-
  Activate when working on the Agentic SDLC Handbook. This skill
  orchestrates an expert panel of 8 agents for iterative review,
  drafting, and quality assurance of handbook content. Use it for
  any handbook chapter creation, review, or structural decision.
---

# Handbook Panel — Expert Review Orchestration

## Agent roster

| Agent | Persona | Activate for |
|-------|---------|-------------|
| [Chief Editor](../../agents/chief-editor.agent.md) | Narrative Architect | Structural decisions, voice consistency, editorial review, bloat detection |
| [C-Suite Strategist](../../agents/csuite-strategist.agent.md) | Executive Communication Expert | Block 1 drafting, business outcome framing, executive scan-friendliness |
| [Practitioner Authority](../../agents/practitioner-authority.agent.md) | Senior AI-Native Developer | Block 2 drafting, technical credibility, battle-tested validation |
| [Market Analyst](../../agents/market-analyst.agent.md) | Industry/Competitive Intelligence | Vendor-neutral validation, competitive claims, analyst-grade framing |
| [Platform Strategist](../../agents/platform-strategist.agent.md) | Microsoft Vision Integrator | MS reference architecture translation, honest gap assessment |
| [CTO Proxy](../../agents/cto-proxy.agent.md) | Skeptical CTO Reader | Block 1 review — "so what?", "prove it", executive attention test |
| [Dev Lead Proxy](../../agents/dev-lead-proxy.agent.md) | Impatient Practitioner | Block 2 review — "can I use this Monday?", actionability test |
| [Thought Leadership](../../agents/thought-leadership.agent.md) | Personal Brand Strategist | Voice authenticity, credibility markers, positioning review |

## Panel workflow

### For corpus audit
1. Each specialist reviews their assigned source asset
2. Chief Editor synthesizes findings into content map + gap analysis
3. Surface to author for approval

### For chapter drafting
1. Primary writer drafts (C-Suite Strategist for Block 1, Practitioner Authority for Block 2)
2. Audience proxy reviews (CTO Proxy for Block 1, Dev Lead Proxy for Block 2)
3. Market Analyst checks vendor balance and claim validity
4. Chief Editor ensures voice consistency and cuts bloat
5. Surface to author for approval

### For integration review
1. Chief Editor reads full manuscript for arc and flow
2. Thought Leadership Advisor checks author positioning
3. Both audience proxies do final "would I read this?" check
4. Surface revision list to author for approval

## Handbook structure

```
Block 0: The Shift (shared foundation)
  Ch 1: The Agentic SDLC Thesis
  Ch 2: The Landscape

Block 1: For Leaders
  Ch 3: Why This Changes Everything
  Ch 4: The Context Moat
  Ch 5: Org Design for Agentic Teams
  Ch 6: Governance & Trust
  Ch 7: ROI & Adoption Playbook

Block 2: For Practitioners
  Ch 8: The Practice — Context Engineering
  Ch 9: Agent Primitives
  Ch 10: Execution — The Meta-Process
  Ch 11: Delegation & Orchestration
  Ch 12: Tooling & Distribution
  Ch 13: Team Scale
  Ch 14: Anti-Patterns & Failure Modes

Block 3: What's Next (shared closing)
  Ch 15: The Road Ahead
```

## Quality gates

Every chapter must pass:
- [ ] Chief Editor: voice consistency, no bloat
- [ ] Audience proxy: engagement and actionability
- [ ] Market Analyst: claim validity (for any competitive/vendor content)
- [ ] Author approval
