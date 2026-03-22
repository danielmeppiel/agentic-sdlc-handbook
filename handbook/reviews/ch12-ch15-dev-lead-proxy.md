# Dev Lead Proxy Review — Chapters 12 & 15

Reviewer persona: Senior tech lead. Ships weekly. One year with Copilot. Zero patience for theory without Monday payoff.

---

## Chapter 12: Multi-Agent Orchestration

### Verdict: **SHIP** (with revisions)

### Can I use this Monday?
Yes — but only the wave model and the one-file-one-agent rule. I could plan a multi-agent refactor by lunchtime using the decision matrix and wave structure. The escalation protocol (L1–L4) maps directly to how I already triage agent failures, so it clicks immediately.

### Best technique
Wave-based parallelism with commit-and-test checkpoints between waves. This is the thing I'd actually draw on a whiteboard for my team. The diagram is clear, the PR #394 numbers are credible, and the "foundation before migration" ordering principle solves a problem I've hit — agents working against stale context — without me having to invent the fix.

### Most confusing part
The conflict resolution section is solid on *file* conflicts (planning error, just repartition) and *design* conflicts (escalate to human), but the *semantic* conflict treatment is too brief. "Foundation-before-migration wave ordering" is the answer, but that only works when you know ahead of time which changes establish patterns and which consume them. What happens when you discover a semantic conflict mid-wave? The chapter says "commit after each wave" but doesn't walk through the recovery: do you revert the conflicting agent's work? Redispatch with updated context? Merge manually? The PR #394 had a "recovery wave" (Wave 2b) which suggests this happened — but the recovery mechanics aren't explained.

### Top 3 Revisions

1. **Add a concrete semantic-conflict recovery walkthrough.** The chapter has one for file conflicts (repartition) and design conflicts (escalate). Semantic conflicts get a principle ("commit between waves") but no recovery procedure. Walk through the Wave 2b recovery from PR #394: what broke, how you detected it, what the redispatch looked like. This is the failure mode practitioners will actually hit, and "order your waves correctly" isn't enough when the ordering was wrong.

2. **Show the actual dispatch.** The specialization patterns are described structurally but never shown in action. What does dispatching an "architecture team" agent actually look like? A terminal command? A config file? A prompt pasted into Claude Code? The chapter has ASCII diagrams of session isolation and wave ordering but zero copy-pasteable artifacts. One concrete dispatch example — the prompt, the loaded instruction files, the file list — would make the Domain Teams pattern immediately usable instead of "sounds right, I'll figure it out."

3. **Quantify the coordination tax honestly.** The chapter says "coordination costs are real" but never prices them. PR #394 saved ~21 minutes of wall-clock time through parallelism, but how much time did planning, partitioning, monitoring, and resolving those 3 human interventions cost? If the human orchestrator spent 30 minutes managing the agents to save 21 minutes of agent time, the ROI story changes. A rough time breakdown (planning: X min, monitoring: X min, interventions: X min, total human time: X min) would let me decide whether multi-agent is worth it for my team's typical change sizes.

---

## Chapter 15: What Comes Next

### Verdict: **REVISE**

### Can I use this Monday?
The "Monday morning" section at the end — yes. The predictions — they're well-reasoned but they're not actionable. I read them, nodded, and didn't change any plans. That's the honest test: did reading this change what I'll do next week? The closing section did. The predictions didn't.

### Best technique
The "What Will Not Change" section. Four structural invariants (context is finite, output is probabilistic, explicit > implicit, human judgment is the bottleneck) that I'd actually reference when pushing back on leadership's "just wait for the next model" argument. This is the part I'd bookmark.

### Most confusing part
Nothing is confusing. The problem is different: the predictions section (near-term, medium-term, long-term) reads like a well-written analyst report, not a chapter in a practitioner book. It's all directionally correct and none of it is surprising to anyone who's been paying attention. "Context windows grow, context engineering matters more" — yes, that was the thesis of Chapter 1. "Standards converge" — sure. "Junior pipeline problem intensifies then resolves" — plausible, unfalsifiable. A tech lead skims this section looking for something they didn't already believe and doesn't find it.

### Top 3 Revisions

1. **Cut or compress the predictions sections by 40%.** Near-term, medium-term, and long-term together are ~1,200 words of well-argued conventional wisdom. The "three-tier honesty" table at the end already summarizes the predictions better than the prose does. Compress each tier to 2-3 punchy paragraphs. Reclaim the space for the "Monday morning" section, which is the part that actually closes the book.

2. **Expand "Monday morning" with specific first-week actions.** The current version says "audit using Chapter 9, write three primitives, test against real tasks." That's a good start but it's one paragraph for practitioners and one for leaders. This is the last thing the reader sees — it should be a concrete checklist they can print out. Day 1: audit one module. Day 2: write your first instruction file. Day 3: test it on a real task. Day 4: measure before/after. Day 5: share results with team. Give it the same specificity the rest of Block 2 earned. The closing line ("The methodology is the floor, not the ceiling. Build on it.") lands — but it lands harder if the reader already has their first week planned.

3. **The "What the Author Probably Got Wrong" section is good — make it braver.** Four hedges are listed, and they're all safe: "governance might lag," "human-in-the-loop might be too conservative," "orchestration might evolve," "organizations resist change." These are the hedges anyone would write. What's the one prediction in this book the author is *least* confident about but included anyway? What's the section that might embarrass them in 18 months? That kind of honesty would match the tone Chapter 1 set ("evidence, not a sales pitch") and would distinguish this from every other future-of-AI chapter that hedges symmetrically.

---

## Cross-Chapter Notes

- Ch12's rigor matches Ch1's voice. It earns the "discipline, not ceremony" tone by backing claims with PR #394 numbers. The chapter reads like it was written by someone who actually ran multi-agent workflows and got burned enough to develop the rules.
- Ch15 drifts toward analyst voice in the predictions sections, which is a register mismatch with Block 2's practitioner tone. The opening line ("Everything in this book will be partially obsolete within eighteen months") and the closing section are both strong. The middle needs to earn that frame.
- The REST parallel in Ch15's closing works. Don't oversell it, but it's an honest analogy and it ties back to Ch1 cleanly.
