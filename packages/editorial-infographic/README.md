# editorial-infographic (APM package)

A self-contained APM package shipping a multi-agent panel pipeline for
producing single-page longform editorial infographics from authored
long-form content (book chapters, methodology specs, papers).

## What's inside

```
.apm/
├── agents/
│   ├── infographic-architect.agent.md     # information structure
│   ├── infographic-illustrator.agent.md   # visual + brand chrome
│   ├── infographic-skeptic.agent.md       # source fidelity (calibrated)
│   └── infographic-editor.agent.md        # orchestrator + arbiter
└── skills/
    └── editorial-infographic/
        ├── SKILL.md                       # entry point + roster
        ├── references/
        │   ├── PIPELINE.md                # phase recipes + invocations
        │   ├── BRAND_SYSTEM.md            # colors, fonts, chrome, SCALE
        │   ├── LAYOUT_PATTERNS.md         # 6 tested patterns (A–F)
        │   └── REVIEW_CHECKLIST.md        # ship gate + distribution
        └── assets/
            ├── starter_template.py        # the renderer (PIL, SCALE=2)
            └── ascii_mockup_template.md   # Phase 3 human-gate scaffold
```

## Use it

In the consuming repo's `apm.yml`:

```yaml
dependencies:
  apm:
    - ./packages/editorial-infographic       # local development
    # - danielmeppiel/editorial-infographic#v0.1.0   # once published
```

Then:

```bash
apm install
```

This deploys the agents to `.github/agents/` and the skill to
`.github/skills/editorial-infographic/` in the consuming repo. The
`canvas-design` skill (required for fonts) is pulled in automatically
as a transitive dependency.

## Provenance

Distilled from the Ch.7 LinkedIn pipeline of *The Agentic SDLC Handbook*
(one infographic, 8+ newsletter subscriptions in 24h). The methodology
itself is documented in `SKILL.md` and the four agent files.
