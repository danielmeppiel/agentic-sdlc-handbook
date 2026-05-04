# Ch06 Team Topologies — Editorial Infographic v3 (LOCKED)

**Source:** `handbook/ch06-team-structures.qmd`
**Audience:** VP Eng / CTO / Eng Director scrolling LinkedIn — past the agent-pilot phase, planning the org shape.
**Output:** `assets/infographics/ch06-team-topologies.png` (2400 × 6656, SCALE=2)
**Renderer:** `assets/infographics/render_ch06.py`

---

## Locked content (post-v3 panel synthesis)

### Masthead (dark INK band)
- TL: `THE  AGENTIC  SDLC  HANDBOOK`
- TR: `BLOCK  II  ·  LEADERS    CH  06`
- BL: `The  Agentic  SDLC  Org  Chart`
- BR: `FREE  ONLINE  ·  PDF  ·  EPUB`

### Title block (cream)
- **Title (display, centered, no period):** *The Agentic SDLC Org Chart*
- **Subtitle (italic, centered, sentence case):** *The 10× team, not the 10× developer.*
- **Deck / standfirst (italic, LEFT-aligned, INK):** *Three seats at the table.*

### § 01 — DIAGNOSE  *(centered "opener vignette" — only centered section)*

- **Promoted display heading (sans-bold 28pt, centered, two lines):**
  - THE 10× DEVELOPER MYTH
  - vs.  THE 10× TEAM REALITY
- **Lede (centered italic, opens with chapter thesis):**
  *"The multiplier is in the system, not the individual."* — Ch 06, L69
- **Two-column verdict table (cells centered within each half):**

  | ▲ THE 10× DEVELOPER MYTH | ● THE 10× TEAM REALITY |
  |:---:|:---:|
  | One hero plus tools. | System designed for leverage. |
  | Productivity = velocity. | Productivity = working software shipped. |
  | Title-first reorgs. | Work-first role design. |

- **Section footer pull-quote (centered italic):**
  *"Create the role when the work exists, not when the title sounds innovative."* — Ch 06, L214

### § 02 — WHO OWNS THE NEW WORK?  *(no kicker — verb tells you what it's about)*

**Lede (left-aligned italic INK_SOFT):**
> Three areas of work that did not exist before agentic development.
> The seats may be filled by existing experts or by new hires.

**Three-column role cards (Pattern D, all 308px tall):**

| WHAT | HOW | OPERATIONS |
|---|---|---|
| **DOMAIN SPECIALIST** | **AGENTIC WORKFLOW ENGINEER** | **AGENT OPERATIONS SPECIALIST** |
| | *the "Context Engineer" role,* *at maturity* | |
| Owns what a Skill encodes. | Owns how a Skill composes. | Owns the eval and safety loop. |
| *Often an existing expert,* *newly in the engineering loop.* | *In small teams, the senior* *engineer wears the hat.* | *Production reliability for* *agents in the loop.* |
| Ch 06, L156 | Ch 06, L168 · L174 · L210 | Ch 06, L178 |

*(Bridge band between §02 and §03 was REMOVED in v3 — it broke the standalone-infographic contract.)*

### § 03 — RESHAPE   *(kicker: "existing roles, new center of gravity")*

**Three stacked role cards (verb-form labels, From X → to Y pattern):**

**SENIOR ENGINEERS** — Ch 06, L95
- *From* writing the hardest code → *to* shaping the system that writes the code.
- Time spent on: architecture · context engineering · review · mentoring.
- Less time on: heads-down implementation.

**JUNIOR ENGINEERS** — Ch 06, L97 · L103-105
- *From* writing code → *to* reviewing agent output, writing specs, diagnosing failures.
- Growth path is real — but it bypasses keyboard hours that built judgment.
- Mentorship is now a system problem, not a 1:1 problem.

**TECH LEADS** — Ch 06, L110-114
- *From* owning the critical path → *to* owning the agent fleet's judgment surface.

### § 04 — REBALANCE   *(kicker: "composition shift, not headcount cut")*

**Headline INK callout (verbatim L317):**
> *"The staffing question is about composition and capability, not reduction."* — Ch 06, L317

**Composition matrix (ratio first, size demoted to last row):**

| Dimension | Pre-Agentic | Agentic (Mature) † |
|---|---|---|
| **SENIOR : JUNIOR** | 1:2 to 1:3 | 1:1 to 2:1 |
| **CONTEXT ENGINEERING** | 0% | 10–20% of capacity |
| **REVIEW ALLOCATION** | 15–20% | 25–35% of capacity |
| Team size *(downstream)* | 6–10 engineers | 4–7 engineers |

† Projected from early-adopter signals. (Ch 06, L302–311)

**⚠ Guardrail callout (RED outline on CREAM_DEEP):**
> **WITHOUT A DELIBERATE REBALANCE,**
> **YOU LOSE TWICE.**
>
> *"The worst outcome is an accidental rebalance where juniors leave because they see no growth path, and seniors burn out because they are covering the gap."* — Ch 06, L329

**WHAT DOESN'T WORK (anti-patterns, cause/effect stacked):**
- ✗ Replace team roles with agents → lose the judgment layer. (L236)
- ✗ Title-first reorgs → roles without work to back them. (L214)
- ✗ Cut juniors to "afford" seniors → the pipeline collapses. (L329)

### LEAVE-WITH (closer — L78 verbatim, replaces hara-kiri L236)

> *"A team of solid engineers with a well-maintained context layer will outperform a team of exceptional engineers working in a knowledge vacuum."*
> — Daniel Meppiel, Ch 06, L78

### CTA FOOTER (dark INK band)
- Kicker: `READ THE FULL CHAPTER — AND THE REST.`
- Book: **The Agentic SDLC Handbook**
- Author: *by Daniel Meppiel*
- Format: `FREE ONLINE · PDF · EPUB`
- URL: `danielmeppiel.github.io/agentic-sdlc-handbook` (underlined — the loudest element)

---

## Invariants (do not re-litigate without panel)

- Brand chrome matches `practitioner-block-v2.png`. Dark bands ONLY in masthead + CTA footer.
- 4 sections only: DIAGNOSE / WHO OWNS THE NEW WORK? / RESHAPE / REBALANCE.
- §01 is the ONLY centered section (opener-vignette pattern). §02–§04 left-aligned for rhythm contrast.
- Closer = L78 verbatim. The L236 closer was rejected as hara-kiri (reads as "agentic SDLC = less working software" when extracted from failure-mode context).
- §04 guardrail headline = "WITHOUT A DELIBERATE REBALANCE, YOU LOSE TWICE." (paraphrase). Body = L329 verbatim. The earlier "losing the wrong ones" framing was rejected as not-inclusive.
- Bridge band between §02 and §03 = REMOVED in v3. Information is adequate via §02 card note ("In small teams, the senior engineer wears the hat").
- §02 middle card co-brands AWE with "Context Engineer" *at maturity* — flat "aka" misrepresents L210's split (Context Engineer → Domain Specialist + AWE).
- §03 uses verb-form labels (no Implementer/Code Writer noun pair, no "Context Architect" as bolded title).
- §04 leads with composition; team size is downstream row.
- Page title has no terminal period (matches `practitioner-block-v2.png`).

## Open chapter-level issue (not blocking)

- **L317 ↔ L327 contradiction:** L317 says staffing is "not reduction" but Path C at L327 says "don't backfill departures" = headcount reduction laundered through attrition. cto-proxy proposed a patch sentence at L317 (growing org = more teams; flat org = composition shift over 12-24mo). Fix in a follow-up chapter commit, not in the infographic.

## Editorial provenance

- v1 (rejected): noun-pair §03 labels, futurism closer, bridge band, "wrong ones" framing.
- v2 (rejected): retained L236 closer (hara-kiri), §02 kicker stole "three seats at the table", §04 callout too small + classifier framing.
- v3 (locked): title left-deck, §01 centered opener-vignette, AWE co-branded with Context Engineer at maturity, bridge cut, ⚠ headline rewritten + bumped, L78 closer.
