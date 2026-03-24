# Linguist Synthesis: Book-Wide Tone, Vocabulary & Readability Assessment

**Reviewer:** Linguist Synthesis Lead  
**Scope:** All 15 chapters (~66,500 words)  
**Sources:** Pod A (Ch01–05), Pod B (Ch06–10), Pod C (Ch11–15) + full-text quantitative scans  
**Gold standard test:** "A senior engineer explaining something at a whiteboard after 2 beers."

---

## 1. The Author's Voice DNA

### What makes this voice distinctive

The author has a **diagnostic voice** — at its best, the prose sounds like a staff engineer who has already debugged the problem you haven't hit yet, and is telling you what happened. The signature move is: **name the failure, explain the mechanism, hand you the fix.** When this pattern fires cleanly, the writing is among the best in the technical book genre.

**Five DNA markers:**

1. **The Myth-Bust Open.** Nearly every chapter opens by refuting a popular belief. Ch01: "Every AI coding tool demos beautifully on a blank project." Ch02: "Your developers are already using AI coding tools." Ch03: "'Our AI coding tools delivered a 10× productivity improvement.' No, they didn't." This is the author's strongest move — it earns trust immediately.

2. **The Concrete Escalation.** The author builds arguments through increasingly specific failure scenarios. Not "things go wrong" but "the agent confabulates plausible-looking method signatures that don't exist. The code compiles in the agent's imagination and fails at build time." This specificity is the voice's greatest asset.

3. **The Binary Reframe.** "The cliff is not about intelligence. It's about information." "The question isn't whether… it's whether you're driving it or reacting to it." Short. Clean. Memorable. The author does this well when it's earned, badly when it's formula.

4. **The Honest Caveat.** The voice is at its most distinctive when it admits uncertainty. The "Three-Tier Honesty" framework, the "What the Author Probably Got Wrong" section in Ch15, the "motivated reasoning risk" admission — this intellectual honesty is rare in technical books and should be amplified, not diluted.

5. **The Practitioner's Impatience.** When the author is in flow, there's a palpable "let me just show you" energy. Ch14's opening paragraph, Ch03's vendor myth-busting, Ch11's before/after examples — the best writing reads like someone who is slightly annoyed that you might waste time on the wrong approach.

### Where the voice breaks

The voice fractures when the author shifts from **diagnosing** to **prescribing**. Diagnostic sections (what goes wrong, why) are consistently practitioner-register. Prescriptive sections (frameworks, taxonomies, checklists) drift toward consultant-register. The author is a better diagnostician than framework-builder, and the prose reflects it.

---

## 2. The Tic List

Ranked by frequency × damage. Frequency from full-text scans; damage rated 1–5 (5 = most harmful to target register).

| Rank | Tic | Frequency | Damage | Location | Action |
|------|-----|-----------|--------|----------|--------|
| 1 | **Em-dash parentheticals** | 913 across 15 chapters (avg 61/chapter) | 2/5 | Everywhere | Cap at ~35/chapter. The voice uses em-dashes well for asides, but at 913 total they become a visual tic. Ch09 (89) and Ch13 (88) are worst. |
| 2 | **"structural"** | 31× across 12 chapters | 4/5 | Ch01 (4), Ch07 (5), Ch15 (4), Ch12 (3) | Kill 60%. Keep only where "structural" means literally architectural. Replace with "inherent," "built-in," "fundamental," or just cut. |
| 3 | **"primitives"** | 54× across 10 chapters | 3/5 | Ch09 (18), Ch10 (8), Ch14 (8), Ch15 (10) | This is the book's core vocabulary. Keep in technical chapters (Ch09–13). Kill in C-suite chapters (Ch02–07) where it reads as jargon. |
| 4 | **"X is not about Y. It is about Z."** | 4 explicit instances + variants | 3/5 | Ch01, Ch07, Ch08, Ch11 | Keep the two best (Ch01: "The cliff is not about intelligence. It's about information." and Ch15's closing). Kill or vary the others. Pattern loses power through repetition. |
| 5 | **"highest-leverage"** | 4× | 4/5 | Ch09, Ch12 (2×), Ch13 | Replace with "most important," "where you get the most out of," or "the decision that matters most." Consulting vocabulary. |
| 6 | **"buying motion"** | 3× (all in Ch02) | 5/5 | Ch02 lines 77, 79, section header | **Kill everywhere.** Pure sales vocabulary. Replace with "how developers choose" / "how organizations buy." |
| 7 | **"machine-readable"** | 10× across 5 chapters | 3/5 | Ch02–05, Ch09 | Reduce to 4–5 uses max. Replace with "that agents can actually use" or "in a format agents understand." |
| 8 | **"reference case study"** | 4× | 3/5 | Ch12 (4×) | Replace 3 of 4 with "the PR #394 example" or "the worked example." |
| 9 | **"in our experience"** | 3× | 4/5 | Ch03, Ch07 (2×) | Kill. Either state the claim directly or cite evidence. "In our experience" is consulting hedge language. |
| 10 | **"at scale"** | ~8× | 3/5 | Scattered | Kill half. Usually adds nothing. "X works at scale" → "X works for 200-file changes." |
| 11 | **Fragment-then-pivot ("Not X. Y.")** | ~12× across Ch06–10 | 2/5 | Pod B chapters | Keep the 4 best. Vary the rest — use "instead" or restructure as single sentences. |
| 12 | **Academic setup sentences** | ~15× | 4/5 | Ch01, Ch02, Ch04, Ch05 | "Three structural dynamics explain the acceleration" — this is a slide title spoken aloud. Rewrite as direct claims. |

---

## 3. Tone Map

**Rating scale:** 1/10 = pure practitioner (whiteboard after 2 beers). 10/10 = pure consultant (Gartner Magic Quadrant prose).

| Ch | Title | Tone | Trend | Notes |
|----|-------|------|-------|-------|
| 01 | The Agentic SDLC Thesis | 3/10 | Opens practitioner, drifts to framework | "Vibe Coding Cliff" = great naming. REST/PROSE parallel is the academic peak. Last third recovers. |
| 02 | The AI-Native Landscape | 3.5/10 | Alternates paragraph by paragraph | "buying motion" is the worst single phrase in the book. Market analysis sections are clean; evaluation framework section is consulting deck. |
| 03 | The Business Case | **2/10** | Consistently practitioner | 🥇 **Best C-suite chapter.** "No, they didn't" opening is the book's best myth-bust. Sounds like someone in the room when the CFO asks. |
| 04 | The Reference Architecture | 4/10 | Framework-heavy opening, practitioner back half | "ontologies" is academic. "Context moat" is the best strategic concept in the book — Stratechery-register, exactly on target. |
| 05 | Governance | 4.5/10 | Hardest topic to keep practitioner | "exercises a form of discretion" is legal register. Risk taxonomy has structural fatigue (6× same pattern). "From Restriction to Enablement" is a consulting reframe header. |
| 06 | Team Structures | 3.5/10 | Good practitioner energy, consulting clichés in headers | "force multipliers" and "capability maturity" are consulting. "The 10x Team, Not the 10x Developer" header is good reframing. |
| 07 | Planning the Transition | 4/10 | Most consulting-heavy chapter in the book | "capability maturity," "scale factor," "phased adoption" — the whole chapter has consulting DNA. But "Compressing this timeline produces shallow adoption that looks like compliance and functions like resistance" is a killer line. |
| 08 | The Practitioner's Mindset | **2/10** | 🥇 **Best Block 2 opener** | Consistent practitioner throughout. "From Writing Code to Engineering Context" captures the thesis in one header. |
| 09 | The Instrumented Codebase | 3/10 | Clean technical prose, some spec-doc drift | Heavy "primitives" usage justified by topic. Before/after structure is excellent. Gets slightly spec-doc in the directory structure section. |
| 10 | The PROSE Specification | 3.5/10 | Technical reference register | Reads more like documentation than prose — appropriate for a specification chapter. Anti-pattern examples bring practitioner voice back. |
| 11 | Context Engineering | **2/10** | Near-perfect practitioner | Zero consultant-speak. Before/after is structural backbone. Code examples feel real, not manufactured. |
| 12 | Multi-Agent Orchestration | 2/10 | Pattern-heavy but concrete | "One-file-one-agent rule" is memorable and practitioners will repeat it. "Sweet spot" slightly worn. PR #394 example grounds everything. |
| 13 | The Execution Meta-Process | 2/10 | Process-focused, human judgment emphasis | "Independently verifiable unit" slightly stiff, but the concept is sound. The ADAPT loop is well-named. |
| 14 | Anti-Patterns & Failure Modes | **1/10** | 🥇🥇 **BEST CHAPTER IN THE BOOK** | "Merge conflict graveyard," "expensive AI-assisted typing," "collective scar tissue" — precise AND evocative. Zero consultant-speak. Every technique born from a failure story. This is the voice the whole book should aspire to. |
| 15 | What Comes Next | 2/10 | Reflective, intellectually honest | "Table stakes" is minor residue. The "Got Wrong" section is the book's most distinctive feature. Author → "the author" shift is deliberate and effective. |

### The Tonal Journey

```
Consulting ─────────────────────────────────────────────────
 5 │          ·Ch05
   │    ·Ch02    ·Ch04
 4 │                    ·Ch07
   │ ·Ch01  ·Ch06          ·Ch09  ·Ch10
 3 │
   │   ·Ch03   ·Ch08    ·Ch11·Ch12·Ch13  ·Ch15
 2 │
   │                                ·Ch14
 1 │
Practitioner ───────────────────────────────────────────────
    Part I   Part II (Leaders)    Part III (Practitioners)  Close
```

**The pattern:** The book has a consultant-register hump in Part II (the C-suite block) that clears as soon as it enters practitioner territory. Part III is consistently excellent. The voice finds its true register in Ch08 and never fully loses it again.

**Implication:** Part II doesn't need to be rewritten — it needs the academic setup sentences and consulting vocabulary surgically removed. The diagnostic energy is already there under the surface.

---

## 4. The Consultant-Speak Index

Every term/phrase that should be replaced, organized by severity.

### Tier 1: Kill on sight (pure consulting/academic, no practitioner would say these)

| Term | Ch | Replacement |
|------|-----|------------|
| "buying motion" | Ch02 (3×) | "how developers/orgs choose tools" |
| "exercises a form of discretion" | Ch05 | "makes judgment calls" |
| "minimal sufficient set" | Ch01 | "the smallest set that works" or just "together, they cover the failure modes" |
| "Three structural dynamics explain the acceleration" | Ch02 | "Three things are driving this:" |
| "ontologies" | Ch04 (2×) | "domain models" or "business logic maps" |
| "capability maturity" | Ch07 | "how ready your teams actually are" |
| "platform convergence" | Ch02 | "tools expanding into each other's territory" |
| "in our experience" | Ch03, Ch07 | Cut. State the claim directly. |
| "From Restriction to Enablement" (header) | Ch05 | "Making Governance Work For Teams, Not Against Them" |
| "scale factor" | Ch07 (3×) | "the thing that changes the timeline" or "what stretches this" |

### Tier 2: Reduce frequency (useful concept, consultant packaging)

| Term | Ch | Action |
|------|-----|--------|
| "structural" (as adjective for anything) | 12 chapters | Keep 10 of 31 uses. Kill the rest. |
| "machine-readable" | 5 chapters | Keep 4, replace rest with "that agents can use" |
| "highest-leverage" | Ch09, 12, 13 | Use once max. Replace others with "most impactful" or "where the biggest gains are" |
| "reference case study" | Ch12 | Use once, then "the PR #394 example" |
| "at scale" | scattered | Kill half. Be specific: "for teams of 50+" or "across 200 files" |
| "force multipliers" | Ch06 | "they make the whole team faster" |
| "primitives" (in C-suite chapters) | Ch01, Ch07 | "building blocks" or "the foundational files" |

### Tier 3: Minor residue (one instance each, low damage)

| Term | Ch | Action |
|------|-----|--------|
| "confabulates" | Ch01 | Replace with "invents" or "makes up" |
| "table stakes" | Ch15 | Replace with "the new baseline" or "expected, not exceptional" |
| "sweet spot" | Ch12 | Replace with "where this works best" |
| "tribal knowledge" | Ch06 | Keep — widely understood, even if originally consulting-adjacent |

---

## 5. Readability Dashboard

### Em-Dash Density (per 1,000 words)

| Chapter | Words | Em-dashes | Per 1K words | Assessment |
|---------|-------|-----------|-------------|------------|
| Ch01 | 3,204 | 60 | 18.7 | 🟡 High |
| Ch02 | 4,056 | 56 | 13.8 | 🟢 Fine |
| Ch03 | 4,201 | 56 | 13.3 | 🟢 Fine |
| Ch04 | 4,045 | 37 | 9.1 | 🟢 Best |
| Ch05 | 5,357 | 77 | 14.4 | 🟡 High |
| Ch06 | 4,280 | 62 | 14.5 | 🟡 High |
| Ch07 | 5,080 | 62 | 12.2 | 🟢 Fine |
| Ch08 | 4,061 | 59 | 14.5 | 🟡 High |
| Ch09 | 5,605 | 89 | 15.9 | 🔴 Overuse |
| Ch10 | 5,216 | 70 | 13.4 | 🟢 Fine |
| Ch11 | 3,832 | 37 | 9.7 | 🟢 Best |
| Ch12 | 5,497 | 58 | 10.6 | 🟢 Fine |
| Ch13 | 4,037 | 88 | 21.8 | 🔴 Overuse |
| Ch14 | 5,364 | 63 | 11.7 | 🟢 Fine |
| Ch15 | 2,663 | 39 | 14.6 | 🟡 High |
| **TOTAL** | **66,498** | **913** | **13.7 avg** | Target: ≤12/1K |

### Passive Voice Estimate (grep-based approximation)

| Chapter | Passive constructions | Words | Passive rate | Assessment |
|---------|----------------------|-------|-------------|------------|
| Ch01 | ~7 | 3,204 | ~2.2/1K | 🟢 Low |
| Ch02 | ~7 | 4,056 | ~1.7/1K | 🟢 Low |
| Ch03 | ~9 | 4,201 | ~2.1/1K | 🟢 Low |
| Ch04 | ~3 | 4,045 | ~0.7/1K | 🟢 Excellent |
| Ch05 | ~18 | 5,357 | ~3.4/1K | 🟡 Elevated |
| Ch06 | ~6 | 4,280 | ~1.4/1K | 🟢 Low |
| Ch07 | ~10 | 5,080 | ~2.0/1K | 🟢 Low |
| Ch08 | ~10 | 4,061 | ~2.5/1K | 🟢 Low |
| Ch09 | ~14 | 5,605 | ~2.5/1K | 🟢 Low |
| Ch10 | ~10 | 5,216 | ~1.9/1K | 🟢 Low |
| Ch11 | ~12 | 3,832 | ~3.1/1K | 🟢 Low |
| Ch12 | ~12 | 5,497 | ~2.2/1K | 🟢 Low |
| Ch13 | ~18 | 4,037 | ~4.5/1K | 🟡 Elevated |
| Ch14 | ~9 | 5,364 | ~1.7/1K | 🟢 Low |
| Ch15 | ~8 | 2,663 | ~3.0/1K | 🟢 Low |

**Passive voice verdict:** Not a systemic problem. Elevated in Ch05 (governance — regulatory language naturally pulls toward passive) and Ch13 (process description — "the wave is committed" etc.). Passive is strategic, not lazy.

### Long Sentence Count (40+ words, estimated from samples)

| Chapters | Estimated 40+ word sentences | Assessment |
|----------|------------------------------|------------|
| Ch01–05 | ~25 | 🟡 Part II has the most bloat |
| Ch06–10 | ~20 | 🟢 Improving |
| Ch11–15 | ~12 | 🟢 Tightest writing |

**Long sentence verdict:** The book gets tighter as it progresses. Part II (C-suite block) has the most complex sentence structures — understandable for business audiences but some sentences try to do too much in one breath.

---

## 6. The Golden Lines

The 15 best-written sentences in the entire book. Criteria: vivid, memorable, practitioner-register, quotable.

1. **"The cliff is not about intelligence. It's about information."** (Ch01)
   — Binary reframe. Six words per sentence. Crystalline. The thesis in miniature.

2. **"Every AI coding tool demos beautifully on a blank project. The question this book answers is why those same tools break on your actual codebase — and what to do about it."** (Ch01)
   — The book's best opening sentence. Escalating tension. Clear promise.

3. **"'Our AI coding tools delivered a 10× productivity improvement.' No, they didn't."** (Ch03)
   — Immediate authority. Two sentences that destroy a myth.

4. **"Raw speed metrics count code produced. They don't count code reworked, reverted, or debugged downstream."** (Ch03)
   — Parallel structure. The cumulative verb list ("reworked, reverted, or debugged") builds to the real cost.

5. **"Your competitors have access to the same AI models you do. They can license the same coding tools. What they cannot replicate is your organization's accumulated engineering knowledge — if you have made it machine-readable."** (Ch04)
   — The "context moat" concept crystallized. Competitive urgency without consulting smell.

6. **"A brilliant developer with poor team context will get worse results than a competent developer with excellent team context. The multiplier is in the system, not the individual."** (Ch06)
   — Counterintuitive. Memorable. The kind of line a VP Eng pins to Slack.

7. **"Not failure — something worse. Inconclusive results that neither justify expanding the investment nor provide grounds for canceling it."** (Ch07)
   — The worst outcome named. Executives will recognize this immediately.

8. **"Compressing this timeline produces shallow adoption that looks like compliance and functions like resistance."** (Ch07)
   — "Looks like compliance and functions like resistance" is the best phrase in Part II.

9. **"A transition plan without a kill switch is an escalation of commitment."** (Ch07)
   — Behavioral economics reference, perfectly applied. One sentence, unforgettable.

10. **"Session resets are cheap; accumulated drift is expensive."** (Ch11)
    — Semicolon structure. Punchy reversal of conventional thinking. Practitioners will quote this.

11. **"Every technique in this book was born from a failure. In our early experiments, the wave execution model emerged because a developer tried to run 15 agents at once and got a merge conflict graveyard."** (Ch14)
    — Origin story. "Merge conflict graveyard" is the single most vivid image in the book.

12. **"The uncomfortable truth: AI failures don't crash. They produce plausible wrong output."** (Ch14)
    — This is the sentence I'd put on the book jacket.

13. **"Learning to see these failures before they ship is the skill that separates effective AI-native development from expensive AI-assisted typing."** (Ch14)
    — "Expensive AI-assisted typing" will enter the vocabulary of every team that reads this book.

14. **"These 19 patterns represent the collective scar tissue of early agentic development practice — the failures that wasted the most time, burned the most tokens, and eroded the most trust."** (Ch14)
    — "Collective scar tissue." Tricolon ("wasted... burned... eroded") with escalating emotional weight.

15. **"There is a motivated reasoning risk in any book that argues humans are indispensable, written by a human who wants that to be true."** (Ch15)
    — The most intellectually honest sentence in any technical book published this decade.

---

## 7. The Kill List

The 10 worst sentences that should be rewritten or cut. Criteria: consultant-register, academic, or structurally broken.

| # | Sentence | Ch | Problem | Suggested Fix |
|---|----------|----|---------|---------------|
| 1 | "Three structural dynamics explain the acceleration:" | Ch02 | Slide title spoken aloud. No engineer talks like this. | "Three things are driving this:" |
| 2 | "PROSE occupies the same position for AI-native development. It defines five architectural constraints for human-AI collaboration that, applied together, address the structural failures described above. It is not a tool, not a file format, not a prompting technique. It is an architectural style." | Ch01 | Four sentences of framework-positioning. "Occupies the same position" is academic. Triple negation is overwrought. | "PROSE is a set of five constraints for working with AI agents. Applied together, they prevent the failures above. Think of it the way REST works for APIs — not a tool, but a style." |
| 3 | "The buying motion is bottom-up." / "The buying motion is top-down." | Ch02 | Sales vocabulary. No engineer or CTO says "buying motion." | "Developers pick these — adoption is grassroots." / "Orgs buy these — it's a top-down decision." |
| 4 | "It exercises a form of discretion, and your governance framework almost certainly has no category for that." | Ch05 | Legal register. "Exercises a form of discretion" is what a lawyer writes. | "It makes judgment calls, and your governance rules probably have no category for that." |
| 5 | "Together, they form a minimal sufficient set." | Ch01 | Math PhD language. | "Together, they cover the failure modes. Drop any one, and a gap opens." |
| 6 | "This chapter is the bridge between the strategic foundations of Chapters 2 through 6 and the implementation disciplines of Block 2." | Ch07 | Pure consulting. "Strategic foundations," "implementation disciplines," "bridge" — the whole sentence is framework plumbing. | Cut entirely. Just start the chapter. The reader knows where they are. |
| 7 | "Plan it around capability maturity — your organization's ability to use these tools reliably and at scale." | Ch07 | "Capability maturity" is CMM-speak. | "Plan it around how ready your teams actually are — can they use these tools reliably, or are they still experimenting?" |
| 8 | "The models below are informed hypotheses, not proven patterns. No organization has run any of these for a full cycle — 12+ months — with measured outcomes on engineer competency development." | Ch06 | Honest, but over-hedged. The double caveat drains authority. | "These models are early. No one has run them for a full year with real measurements. Use them as starting points, not blueprints." |
| 9 | "REST's statelessness constraint meant servers didn't maintain session state between requests — which seemed limiting, but induced scalability. PROSE's Reduced Scope constraint means each agent session handles a focused task..." | Ch01 | Forced academic parallel. "Induced scalability" is paper-speak. | Keep the REST parallel but land it faster. "REST's statelessness seemed limiting but made systems scale. PROSE's scope limits seem restrictive but make agent output reliable." |
| 10 | "Business intelligence, domain models, analytics, ontologies" | Ch04 | "Ontologies" is academic jargon that adds nothing. | "Business intelligence, domain models, analytics" (just cut "ontologies") |

---

## 8. Register Consistency Map

### Where the book successfully maintains practitioner register

**Strong zones (consistently on-target):**

- **Ch03 (The Business Case)** — The best C-suite chapter. Sounds like someone who has built business cases and knows when the math is being gamed. The "No, they didn't" opening sets a tone that never wavers.
- **Ch08 (The Practitioner's Mindset)** — Clean bridge into Part III. "From Writing Code to Engineering Context" is the right framing. Decision tables are practical, not theoretical.
- **Ch11 (Context Engineering)** — Code examples feel real. Before/after structure is the book's strongest pedagogical move. Zero consulting vocabulary.
- **Ch12 (Multi-Agent Orchestration)** — "One-file-one-agent rule" is the kind of naming practitioners adopt immediately. PR #394 grounds everything.
- **Ch14 (Anti-Patterns)** — The gold standard. Every pattern born from a specific failure. Metaphors are precise ("graveyard," "scar tissue," "expensive typing"). This chapter could stand alone as a conference talk.
- **Ch15 (What Comes Next)** — The "Got Wrong" section is the book's most distinctive feature. Intellectual honesty is the ultimate practitioner register — consultants never admit uncertainty.

### Where register breaks

**Fracture zones (drift into consultant/academic):**

- **Ch01 lines 55–80:** The REST/PROSE parallel section. The concept is right but the language shifts into academic framing ("architectural style," "induced properties," "coherent set of constraints"). Fix: keep the parallel, shorten the explanation, use practitioner language.
- **Ch02 lines 73–100:** "Buying motion" section + capability evaluation framework. Two different registers fighting each other — market analysis (fine) and consulting taxonomy (not fine).
- **Ch04 lines 9–55:** The "Three Layers" opening is framework-heavy before it earns the reader's trust. The chapter gets good once it hits the "Context Moat" section.
- **Ch05 lines 96–220:** The Risk Taxonomy. Six identical structural patterns in a row. The information is necessary, but the repetitive format creates fatigue. Vary the structure: some as scenarios, some as checklists, some as "here's what happened to a team that ignored this."
- **Ch07 entire chapter:** The most consulting-flavored chapter. "Phased Adoption," "Capability Maturity," "Scale Factor" — the vocabulary of management consultants. The content is sound but needs a language pass. Every "Scale factor:" could be "What changes the timeline:" and the whole chapter shifts register.
- **Ch09 lines 311–415:** Directory structure section drifts into specification-document register. Appropriate for reference material but breaks the narrative flow.
- **Ch10 throughout:** Reads like a specification (which it is). Acceptable, but the anti-pattern examples are the moments that bring the practitioner voice back — consider leading with them.

### The register gradient

```
REGISTER MAP (simplified)
─────────────────────────────────────────────────────────────────
Part I (Ch01):    ████████░░  Practitioner 80% | Consultant 20%
Part II (Ch02-07): ██████░░░░  Practitioner 60% | Consultant 40%
Part III (Ch08-14): █████████░  Practitioner 90% | Consultant 10%
Close (Ch15):     █████████░  Practitioner 90% | Consultant 10%
─────────────────────────────────────────────────────────────────
```

---

## Executive Summary: The Three Actions That Matter Most

### 1. Do a vocabulary pass on Part II (Ch02–07)

Part II is where the book's voice wavers. The content is strong but the language periodically sounds like a consulting engagement. A targeted pass replacing ~30 specific terms (see Consultant-Speak Index Tier 1) would shift the entire block from 60/40 to 80/20 practitioner/consultant.

### 2. Make Ch14's voice the north star for revision

Chapter 14 is the book's voice at its purest: diagnostic, concrete, metaphor-rich, zero consulting residue. When revising any sentence in the book, the test should be: "Could this sentence appear in Ch14 without sounding wrong?" If not, it needs work.

### 3. Break the structural pattern fatigue in Ch05

The Risk Taxonomy's six identical subsection structures create the single worst readability problem in the book. Vary the format: scenario → checklist → "what happened when a team ignored this" → data table → scenario. Same information, dramatically better reading experience.

### What NOT to fix

- The em-dash habit is the author's voice. Reduce in the worst chapters (Ch09, Ch13) but don't eliminate. An em-dash-less version of this book would sound like someone else wrote it.
- "Primitives" is the book's core vocabulary. It's fine in practitioner chapters. Just reduce in C-suite chapters where it reads as jargon.
- The REST/PROSE parallel in Ch01 is conceptually valuable. Fix the language, keep the structure.
- The intellectual honesty (Three-Tier framework, "Got Wrong" section) is the book's most distinctive feature. Amplify it. More books should do what Ch15 does.

---

*Assessment complete. 66,498 words audited. 913 em-dashes counted. 1 "merge conflict graveyard" celebrated.*
