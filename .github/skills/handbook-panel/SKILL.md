---
name: handbook-panel
description: >-
  Activate when working on the Agentic SDLC Handbook. This skill
  orchestrates an expert panel of 11 agents for iterative review,
  drafting, visual design, fact-checking, publishing strategy, and
  quality assurance of handbook content. Use it for any handbook
  chapter creation, review, illustration, publishing, or structural decision.
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
| [Illustrator](../../agents/illustrator.agent.md) | Visual Strategist | Diagram specification, visual audit, information design, Mermaid/ASCII specs |
| [Fact & Ref Checker](../../agents/fact-ref-checker.agent.md) | Claims Auditor | Unverified claim detection, statistic validation, consistency audit |
| [Publishing Advisor](../../agents/publishing-advisor.agent.md) | First-Time Author Strategist | Publishing path selection, monetization, launch strategy, distribution |

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

### For visual audit
1. Illustrator scans each chapter for complexity signals and visual opportunities
2. Produces Mermaid/ASCII specs for each recommended visual
3. Flags existing visuals that fail the "faster than prose" test
4. Chief Editor reviews visual density and cross-chapter consistency
5. Surface visual specs to author for approval

### For fact-checking
1. Fact & Ref Checker audits each chapter for unverified claims
2. Classifies claims as Verified / Qualified / Unverified
3. Runs cross-chapter consistency audit (numbers, frameworks, case study details)
4. Produces structured report with recommendations
5. Surface flagged claims to author for resolution

### For publishing strategy
1. Publishing Advisor assesses author profile, audience, and content characteristics
2. Produces path comparison matrix with honest tradeoffs
3. Recommends specific path with launch timeline
4. CTO Proxy validates enterprise buyer perspective
5. Thought Leadership Advisor validates positioning implications
6. Surface recommendation to author for decision

### For integration review
1. Chief Editor reads full manuscript for arc and flow
2. Thought Leadership Advisor checks author positioning
3. Both audience proxies do final "would I read this?" check
4. Illustrator does cross-manuscript visual consistency check
5. Fact & Ref Checker does final cross-chapter consistency audit
6. Surface revision list to author for approval

## Handbook structure

```
Block 0: Foundation
  Ch 1: The Agentic SDLC Thesis

Block 1: For Leaders
  Ch 2: The AI-Native Landscape
  Ch 3: The Business Case
  Ch 4: The Agentic SDLC Reference Architecture
  Ch 5: Governance for AI-Assisted Delivery
  Ch 6: Team Structures for AI-Augmented Delivery
  Ch 7: Planning the Transition

Block 2: For Practitioners
  Ch 8: The Practitioner's Mindset
  Ch 9: The Instrumented Codebase
  Ch 10: The PROSE Specification
  Ch 11: Context Engineering
  Ch 12: Multi-Agent Orchestration
  Ch 13: The Execution Meta-Process
  Ch 14: Anti-Patterns and Failure Modes

Closing
  Ch 15: What Comes Next
```

## Quality gates

Every chapter must pass:
- [ ] Chief Editor: voice consistency, no bloat
- [ ] Audience proxy: engagement and actionability
- [ ] Market Analyst: claim validity (for any competitive/vendor content)
- [ ] Illustrator: visual audit — appropriate diagrams where they accelerate comprehension
- [ ] Fact & Ref Checker: all claims verified, qualified, or flagged
- [ ] Author approval
