# Chapter 14 Review — Dev Lead Proxy

**Reviewer:** Dev Lead Proxy (The Impatient Practitioner)
**Chapter:** Anti-Patterns and Failure Modes
**Verdict:** **REVISE** — strong bones, real patterns, but the recovery playbook is too generic and silent failure detection stops short of the hard part.

---

## Can I use this Monday?

**Yes, partially.** The taxonomy table is immediately useful as a team checklist. The decision tree is something I'd print and tape to a monitor. The five foundational anti-patterns (1–5) are things I've watched happen this quarter. The security section is short and actionable.

What I can't use Monday: the Recovery Playbook (too generic to follow under pressure) and the Silent Failure section (identifies the problem, doesn't give me tools to catch it).

## Best technique

The **Failure Mode Decision Tree.** This is the only thing in the chapter shaped like a diagnostic tool rather than a catalog. When something breaks at 4pm and I need to figure out *why*, a decision tree beats a taxonomy table. I'd want this expanded, not the catalog.

## Most confusing part

The "Nine Missing Failure Modes" section title. Missing from what? This framing implies the chapter has errata baked in — "we forgot these earlier." Just call them what they are: execution-level and session-level failure modes. The self-deprecating provenance note ("gaps in original documentation") weakens the authority of the entire catalog.

## Missing

1. **Frequency and cost data.** Which of these 16 do teams hit most? Which are most expensive? I'd triage differently if I knew #7 (Trust Fall) causes 40% of production incidents vs. #14 (Cost Runaway) being annoying but cheap. Even rough tiers (common/rare, cheap/expensive) would help.
2. **Tool-specific detection.** "Run `git diff`" is good. What about VS Code's diff view, Copilot's review mode, Claude Code's `--diff` flag? The chapter is tool-agnostic to the point of being under-specific.
3. **A real war story.** Chapter 1 has that 70-file PR as an anchor. This chapter has sixteen patterns with no throughline. One real incident traced through the decision tree — symptom → diagnosis → recovery → primitive fix — would make this chapter land.

---

## Section-by-Section

### The Taxonomy (table) — SHIP
The PROSE constraint mapping is genuinely useful. I can scan it in 30 seconds and find my failure. The grouping (foundational / execution / session) is natural. This is the best part of the chapter.

### Foundational Anti-Patterns (1–5) — SHIP with minor edits
These are real. Every one maps to something I've seen or done. The scenarios are specific enough to be recognizable. #4 (Flat Instructions) with the SQL injection scenario is the strongest — concrete, scary, memorable.

Minor issue: the prevention/recovery for each pattern reads like a pointer back to earlier chapters rather than standalone guidance. That's fine for a reference chapter but means this can't be read independently. Acceptable trade-off.

### Execution Anti-Patterns (6–10) — SHIP
Tight, practical, no filler. #7 (Trust Fall) flagged as "the most dangerous pattern in the chapter" — agree completely. #10 (Not Fixing the Primitives) is the one most teams skip, and calling it out as a distinct anti-pattern is valuable.

#6 (Solo Hero) and #8 (Same-File Parallel Edits) feel like they could be one pattern ("poor decomposition"), but separating them is defensible — the fixes differ.

### The Nine Missing Failure Modes (11–16) — REVISE
The format switch to tables is fine. The content is real. My issues:

- **The section title is bad.** "Nine Missing" is confusing (there are six, not nine — 11 through 16 is six patterns). Was the heading meant to cover a larger set that got cut? This is either a counting error or a leftover from a previous draft. Either way, it's sloppy for a chapter that's supposed to be a definitive catalog.
- **#11 (Context Window Exhaustion) overlaps heavily with #5 (Scope Creep).** The distinction is that #5 is about task scope growing and #11 is about context capacity silently degrading, but the symptoms and fixes are nearly identical. Consider merging or drawing the line more sharply.
- **#15 (The "Almost Done" Trap) is the most insightful pattern in the chapter.** The observation that 90% is flat and 10% is vertical — that's exactly right. This deserves expansion. Most teams I know have lost days here. The recovery ("accept the 90%, handle the rest manually") is honest advice that no other AI productivity content would give you.

### Silent Failure Problem — REVISE
This section correctly identifies the *categories* (convention violations, semantic drift, architectural erosion) but doesn't solve the actual hard problem: **how do I detect these in practice?**

"Primitive rules that encode conventions" — sure, but that's prevention, not detection. If I already had perfect primitives, I wouldn't have silent failures.

What I need: a concrete detection checklist. Something like:
- After every wave: `git diff --stat` (scope check), test suite (functional check), `grep` for known anti-patterns (convention check)
- After every PR: architecture boundary test, dependency graph diff, human review of business logic changes
- Weekly: token cost trending, recurring failure audit, primitive coverage gap analysis

The section gestures at these but doesn't make them operational.

### Team-Level Anti-Patterns — SHIP (barely)
These are real and worth including. "Cargo-culting complexity" is the one I'd highlight — I've seen teams build four-wave orchestration plans for a 200-line change. The observation that disciplines scale *down* is important.

However, this section is thin. Five short paragraphs, no scenarios, no detection criteria. Either expand each with a recognizable scenario (like the foundational patterns have) or compress into a callout box. The current length says "we included this for completeness" rather than "this matters."

### Recovery Playbook — REVISE
Six steps. All correct. None specific enough to follow under pressure.

"Stop and assess" — yes, but *how*? The decision tree helps, but it's in a separate section. Link them.

"Fix the primitive" — the single most important step, buried at #5 with one sentence. This should be expanded. *Which* primitive? How do I identify the right one? What's the minimum viable fix?

"Re-dispatch with constraints" — this is the step where most teams will ask "but how?" A before/after example of a failed dispatch → constraint addition → successful re-dispatch would make this actionable.

### Decision Tree — SHIP
Best diagnostic tool in the chapter. Print-worthy. The branching logic is sound and matches how I'd actually debug an agent failure.

One gap: the tree ends with "Probably fine. Verify edge cases." That endpoint needs more — *which* edge cases? The answer is "the ones your domain requires," but a prompt like "Check: error paths, empty inputs, concurrent access, auth boundaries" would make the leaf actionable.

### Security Practices — SHIP
Short, specific, non-obvious. Prompt injection via dependency code is a risk most teams haven't thought about. Scope escalation through CI pipeline edits — yes, I've seen this. Credential exposure — table stakes but worth restating.

Good that this exists. Doesn't need expansion.

---

## Top 3 Revisions

### 1. Fix the "Nine Missing" heading and count
The section says "nine" but contains six patterns (11–16). This is either a counting error or refers to a previous draft structure. Fix the heading, verify the count, and drop the "missing from original documentation" framing. Just call them "Session and Resource Failure Modes" or similar. The self-deprecating provenance note ("gaps in original documentation") undermines the chapter's authority as a definitive catalog. **Severity: High** — this is the kind of error that makes a reader question whether the rest was carefully edited.

### 2. Make the Recovery Playbook specific with a worked example
The six steps are correct but too generic to follow under pressure. Add one concrete scenario: a real (or realistic) failure traced through the playbook. Something like: "Agent in wave 3 produces code that calls a deprecated API. Step 1: Symptom matches #10 (Not Fixing the Primitives) + #13 (Stale Context). Step 2: Commit waves 1–2 (passing). Step 3: Revert wave 3. Step 4: Decompose — the agent needed the API migration guide in context. Step 5: Add `api-v2-migration.instructions.md` scoped to the affected module. Step 6: Re-dispatch wave 3 with updated context." That's 6 sentences and transforms the section from advice to a usable protocol.

### 3. Operationalize silent failure detection
The categories (convention violations, semantic drift, architectural erosion) are correct. The detection methods are too vague. Replace the current paragraph-level descriptions with a concrete checklist tied to workflow checkpoints: what to check after each wave, after each PR, and weekly. Even a simple table (checkpoint → check → tool → catches) would convert this from problem identification to problem solving. This is the section where the chapter either earns its place as a reference or stays a cautionary list.

---

## Voice Calibration

Chapter 1 sets a high bar: assertive, specific, builds an argument with evidence, doesn't waste words. Chapter 14 matches this voice in the foundational anti-patterns and the decision tree. It drops below that bar in the recovery playbook (generic advice where Ch1 would give a specific example) and the silent failure section (identifies the problem without solving it, where Ch1 would push through to the structural answer).

The opening paragraph is strong — "every technique in this book was born from a failure" has the right energy. Maintain that standard throughout. The chapter's weakest moments are when it reads like a reference card instead of hard-won operational knowledge.

---

**Bottom line:** This chapter is 75% ready. The catalog is real, the taxonomy works, the decision tree is immediately useful. The three revisions above — fix the counting error, add a worked example to the playbook, operationalize silent failure detection — would make this a chapter teams actually reference during incidents. Right now it's a chapter teams read once and don't come back to.
