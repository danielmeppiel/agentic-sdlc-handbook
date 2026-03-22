# Dev Lead Proxy Review — Chapters 8, 9, 13

Reviewer persona: Senior tech lead, ships weekly, uses Copilot daily, zero patience for theory without Monday-morning payoff.

---

## Chapter 8: The Practitioner's Mindset

### Can I use this Monday?
Partially. The three-roles model (Architect / Reviewer / Escalation Handler) is immediately useful as a mental checklist — I can literally put those three words on a sticky note. The agent-vs-manual heuristic ("explain in two minutes → agent; thirty-minute whiteboard → manual") is the most practical thing in the chapter. But nothing here is *actionable* in the copy-paste sense. There's no checklist, no decision tree, no template. It's all prose about how to think differently.

### Best technique
The "specification would be longer than the implementation" heuristic. Concrete, memorable, instantly applicable. When I'm about to dispatch an agent, I can ask: "Would my instruction doc be longer than the code?" If yes, just write the code.

### Most confusing part
The "cost of over-reliance" section reads like a warning label stapled onto a power tool manual. Skill atrophy, context erosion, specification debt, the "almost done" trap — four sub-pathologies is too many for what is essentially one message: "don't stop writing code yourself." The 20–30% rework threshold is useful. The rest is padding.

### Missing
1. **A decision flowchart.** The agent-vs-manual section has all the inputs for a flowchart but delivers it as six paragraphs of prose. Give me a diagram: task arrives → is it well-specified? → is scope bounded? → is specification shorter than implementation? → delegate / code manually / split.
2. **Before/after of the mindset shift.** Ch1 nails tone by showing the Vibe Coding Cliff concretely. Ch8 says "your primary output shifts from code to context" but never shows a side-by-side of the same task done both ways with timing. The logging migration example in "From Writing Code to Engineering Context" is close but stays abstract.
3. **The roles in action.** The three roles are described but never demonstrated. Show me a 60-second timeline of a real task where the practitioner switches between Architect, Reviewer, and Escalation Handler. Even a short narrative sequence would ground this.

### Verdict: **SHIP** (with revisions)

The chapter does its job as a mental-model setter for Block 2. The three-roles framework and the agent-vs-manual heuristic are genuinely useful. But it's the weakest chapter in the practitioner block because it's the most theoretical and the least copy-pasteable.

**Top 3 revisions:**
1. **Add a decision flowchart** for "agent vs. manual vs. split." Convert the six prose paragraphs into a visual. This is the single highest-value addition.
2. **Collapse the over-reliance section.** Four sub-pathologies → two (skill atrophy + the "almost done" trap). Cut context erosion (it's a restatement of Ch6 governance) and specification debt (it's covered better in Ch9's feedback loop). Save ~400 words.
3. **Add a "roles in action" sidebar.** A concrete 5-step narrative showing one task where the practitioner moves through all three roles. Doesn't need to be long — 150 words with timestamps would do it.

---

## Chapter 9: The Instrumented Codebase

### Can I use this Monday?
Yes. The six primitives are concrete enough that I could start writing instruction files and an agent config this afternoon. The "Before and After" section is excellent — it shows exactly what the same agent task produces with and without instrumentation. The "Starting Points" section (Week 1/2/3 ramp) is realistic.

### Best technique
The instrumentation audit (Steps 1–5). "Spend 30 minutes with your team, list every convention a new engineer needs" → classify by visibility → rank by failure cost → map to primitive type. I could run this in my next team meeting. It's the fastest path from "we should try this" to "here's our starter set."

### Most confusing part
The boundary between Skills and Instructions is fuzzy in practice. The chapter says "a rule says use `_rich_warning()` for warnings; a decision framework says every warning must answer what should the user do." But in my codebase, that distinction often collapses — most of my "decision frameworks" are just 5–8 rules with context. The "three criteria" test (cross-file? more than a few rules? triggered by code pattern?) helps, but a borderline example showing the same knowledge as an instruction vs. a skill would nail it.

### Missing
1. **How tools actually load these files.** The chapter describes the primitives but never says which tools support which file formats. Does Copilot read `.instructions.md` today? Does Claude Code read `.agent.md`? Does Cursor read `SKILL.md`? A compatibility matrix — even a partial one — would save me an hour of experimentation.
2. **Maintenance cost.** The feedback loop section is good. But how much time does this take per week once you're past the initial setup? The "review quarterly" for memory files is the only maintenance guidance. For a team of five shipping weekly, I need to know: is this 30 minutes/week or 3 hours/week?
3. **When primitives conflict.** The composition hierarchy says "more specific primitives refine general guidance, they don't override it" and "if a conflict exists, it indicates a design error." In practice, conflicts will happen. What do I do when my API instruction says "always return standard envelope" but a specific endpoint needs a streaming response? A conflict resolution pattern — even a simple "most-specific wins, log a warning" — is needed.

### Verdict: **SHIP** (with revisions)

This is the strongest chapter of the three. The six primitives are well-defined, the before/after is convincing, the audit process is immediately actionable. The file trees match real project structures — I recognize the `.github/` layout. The 40–50 line instruction file guideline is the kind of specific, practical constraint that makes me trust the author has actually done this.

**Top 3 revisions:**
1. **Add a tool compatibility note** (even a brief one) indicating which primitives are supported by which major tools today. This is the #1 question a dev lead will have. It doesn't need to be exhaustive — a footnote saying "Instructions are supported by GitHub Copilot and Cursor; agent configs vary by tool; skills are tool-specific" saves readers from guessing.
2. **Show a borderline skill-vs-instruction example.** Take one piece of knowledge and show it as both an instruction file and a skill, with a paragraph explaining why one is better for this case. This resolves the fuzziest concept in the chapter.
3. **Add a "maintenance budget" paragraph** to the feedback loop section. Something like: "In the reference project, primitive maintenance averaged X minutes per week after the initial 3-week setup." Give readers a number to plan against.

---

## Chapter 13: The Execution Meta-Process

### Can I use this Monday?
Yes — if Monday involves a change touching more than ~15 files. For smaller changes, the "Small Changes" adaptation section is honest: the full wave structure is overhead. The five-phase model (Audit → Plan → Wave → Validate → Ship) is immediately adoptable, though the wave structure requires tooling that supports parallel agent dispatch.

### Best technique
The ADAPT loop. Most process descriptions are linear: do A, then B, then C. This one explicitly builds in recovery. "When a wave fails, you don't start over — you diagnose, adjust the plan, and re-execute." The PR #394 Wave 2b recovery (agent stalled → split work across two replacement agents, 7 minutes total) is exactly the kind of real failure that makes a methodology credible.

### Most confusing part
The PR #394 timeline is compressed in a way that hides important details. "Audit (3 minutes)" — how? Two explore agents in 3 minutes produced severity-ranked findings with file-and-line citations across a codebase touching 70 files? Either the agents were pre-loaded with a lot of context, or "3 minutes" includes significant prior familiarity. The timeline reads like a best-case run by an expert who has done this before. That's fine — but say so. A first-timer should expect 3× these numbers.

### Missing
1. **Tooling.** The chapter says "the meta-process works regardless of which AI coding tool you use" but never names a single tool that can orchestrate parallel agent dispatch with wave-level coordination. Can I do this in Copilot CLI? Claude Code? Cursor? What's the minimum tooling? Even a sentence like "the reference case used Tool X for orchestration" would ground this.
2. **Wave decomposition worked example.** The rules are clear (dependency ordering, one-file-one-agent, self-sufficiency test). But the PR #394 wave structure is described, not shown. Show me the actual wave plan — which files in which wave, which agent persona assigned to each — so I can pattern-match against my own projects.
3. **Cost of getting it wrong.** What happens when you decompose waves badly? The chapter says "poorly decomposed waves produce merge conflicts, stale context, and cascading failures" but doesn't show an example. A short "anti-pattern: what a bad wave plan looks like" would be as instructive as the good example.

### Verdict: **SHIP** (with revisions)

The PR #394 case study is convincing. It's honest about limitations ("zero regressions detected by the test suite" ≠ zero regressions), it shows real failures and recovery, and the three interventions are categorized in a way that generalizes. The wave decomposition rules are practical — the one-file-one-agent rule alone is worth the chapter. The scaling guidance (small/large changes) is realistic.

**Top 3 revisions:**
1. **Add a first-timer calibration note** to the PR #394 timeline. Something like: "These times reflect an experienced practitioner with mature primitives. First attempts on an uninstrumented codebase should budget 2–3× for audit and planning." Without this, readers will try it once, take 4 hours, and conclude the process doesn't work.
2. **Show the wave plan.** Expand the PR #394 example with a table: Wave | Files | Agent persona | Dependencies. Even a simplified version with 8–10 representative files across 4 waves would make the decomposition rules concrete.
3. **Name the orchestration tooling** used in the reference case — or at minimum, list the capabilities a tool needs to support this meta-process (parallel agent dispatch, session isolation, test gate integration). "Tool-agnostic" is fine as a design principle, but "we used X and here's the minimum you need" is what a practitioner needs to get started.

---

## Cross-Chapter Notes

- **Ch8 → Ch9 handoff is clean.** Ch8 says "your job is to externalize knowledge" and Ch9 immediately shows the six primitive types. The transition works.
- **Ch8 → Ch13 gap.** Ch8 introduces the three roles but Ch13 never maps back to them explicitly. The "three human interventions" in PR #394 are clearly Architect (scope decision), Escalation Handler (agent recovery), and Reviewer (test triage) — but the chapter doesn't say so. One sentence connecting the interventions to the Ch8 roles would strengthen both chapters.
- **Consistent voice.** All three chapters maintain the Ch1 voice: direct, evidence-backed, no hedging. Ch9 is the tightest. Ch8 is the loosest (more theory per paragraph). Ch13 is the most engaging because it has a real story.
