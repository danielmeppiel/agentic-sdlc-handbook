# Chapter 10 Review — Dev Lead Proxy

**Verdict: REVISE**

I can use about 70% of this Monday. The constraint definitions are clean, the anti-patterns are real, and the before/after examples are genuinely helpful. But the chapter pulls its punches right where I need it to commit — the worked example is a sketch, the checklist is too abstract to score honestly, and two constraint sections feel like they're repeating Chapter 1 instead of deepening it.

---

## Can I use this Monday?

**Mostly yes.** The Progressive Disclosure link-vs-inline pattern is immediately actionable — I could refactor our instructions today. The Orchestrated Composition file layout is copy-pasteable. The anti-patterns match real failures I've debugged.

**What's not actionable:** The worked example gives me five bullet points when I need five diffs. The compliance checklist gives me questions I'd answer "sort of?" to, with no way to resolve the ambiguity.

## Best technique

Progressive Disclosure's "descriptive labels for relevance assessment" — the bad/good comparison of link text. That's the kind of thing I'd paste into a PR comment today. Tiny change, immediate payoff, teaches the principle through the fix.

## Most confusing part

The Interaction Effects section. I read it, nodded, and retained nothing. It's three paragraphs of "A + B = good property" without showing me a scenario where having A without B actually failed. The constraint math is correct but ungrounded. If you showed me a real case where someone had good hierarchy but no progressive disclosure and got burned, I'd remember it.

---

## Section-by-section

### The Constraint Model (table)
**Ship.** Clean, scannable, does its job. The three-column table is the right density for a reference chapter.

### P — Progressive Disclosure
**Ship.** Best section in the chapter. The markdown-links-as-lazy-loading pattern is concrete and the before/after is sharp. The skills metadata example earns its space. The "bad link vs. good link" comparison is the kind of micro-technique that sticks.

One nit: the "200,000-token context window" framing in "Why it matters" is already dated. Ground the argument in attention degradation, not token counts. That way it ages well.

### R — Reduced Scope
**Revise.** The phase decomposition pattern is fine but generic — it reads like project management advice ("separate planning from implementation") rather than agent-specific guidance. What I need: a heuristic for *how* to size a task. "Can the agent complete this without asking a follow-up question?" is good but it's one sentence buried in the section. That should be the headline, with 2-3 concrete examples of tasks that were too big and how they got split. The scope creep anti-pattern dialogue is effective — keep that.

### O — Orchestrated Composition
**Ship with minor trim.** The file tree is immediately useful. The workflow-as-composition example is good. The monolithic prompt anti-pattern is the most recognizable failure mode in the chapter — every team I've worked with has hit this. The "which instruction failed?" debugging frame is the right way to sell composition.

Minor: the "explicit contracts between agents" paragraph feels bolted on. It introduces multi-agent coordination (a big topic) in three sentences. Either give it a real example or cut it and let Chapter 13 own it.

### S — Safety Boundaries
**Revise.** This section leans too hard on the "non-deterministic therefore dangerous" framing. I get it — you established this in Chapter 1. Here I need the *implementation* spec. The tool whitelist YAML and validation gate markdown are good, but they're the only two patterns. Where's the graduated trust model? What does "minimum set of tools" actually look like for common agent roles (planning agent, implementation agent, review agent)? A table of 3-4 standard role/tool/boundary combinations would make this immediately usable. Right now I'd have to invent those boundaries from scratch.

The `applyTo` pattern is listed under Safety Boundaries but it's fundamentally an Explicit Hierarchy mechanism. It's doing double duty. Acknowledge the overlap or move it.

### E — Explicit Hierarchy
**Ship.** The directory-scoped walkup explanation is clear and the `applyTo` glob progression (*.py → api/**/*.py → api/auth/**/*.py) is the best illustration in the chapter of how specificity works. The compilation-for-portability paragraph is a smart addition — it answers "but what if my tool doesn't support this?" before I ask.

### Interaction Effects
**Rewrite.** Three paragraphs of constraint algebra that I can't use. The formulas are correct (P+E = precision loading, R+O = reliable workflows, S+R = auditability) but they read like the proof of a theorem I already believe. Replace each with a one-paragraph failure story: "Team X had hierarchy but no progressive disclosure. Here's what happened." That turns theory into a diagnostic tool.

### Worked Example (JWT auth)
**Revise significantly.** This is the section I was most interested in, and it's the thinnest. Five bullet points, one per constraint, each a sentence or two. It feels like a checklist applied to a scenario, not a worked example. A real worked example would show me:

1. The actual `AGENTS.md` content for `backend/auth/` (even 10 lines)
2. The actual task decomposition (not just "design the token schema" — what's in the prompt?)
3. One moment where a constraint prevented a real failure ("without the safety boundary, the agent modified the frontend auth state directly")

Right now this reads like "imagine applying the constraints." I want "here's what it looked like when we did."

### Compliance Checklist
**Revise.** The questions are reasonable but I can't score them honestly. Take P1: "Do instruction files use links to deeper content rather than inlining everything?" What if half of them do? What if they use links but the link text is vague? I'd mark "sort of" on most of these, which makes the scoring bands (12/12, 8-11, etc.) meaningless.

Two fixes: (a) make each question binary by being more specific ("Does every instruction file over 200 lines use links for subsections?" — I can grep for that), or (b) replace the score bands with a prioritized action list ("If you fail S1 or S2, start there regardless of total score").

---

## Top 3 revisions

1. **Expand the JWT worked example into an actual worked example.** Show file contents, show the task prompts, show one constraint preventing a specific failure. This is the section that converts "I understand the theory" into "I know how to do this." Budget: 400-600 more words with code blocks.

2. **Add a role/tool/boundary table to Safety Boundaries.** Three to four standard agent roles (planner, implementer, reviewer, deployer) with their tool whitelists, knowledge scopes, and approval gates. Make it a reference table I can adapt, not a principle I have to derive.

3. **Replace Interaction Effects prose with failure vignettes.** One paragraph each: what someone had, what they were missing, what broke. Turns abstract constraint math into a diagnostic tool that helps me identify which constraint I'm violating when things go wrong.

---

## Comparison to Chapter 1 voice

Chapter 1 earns its abstractions by grounding every claim in the Vibe Coding Cliff narrative — you *feel* the failures before you see the framework. Chapter 10 is more clinical, which is appropriate for a reference spec, but it over-indexes on "why it matters" preambles that retread Chapter 1's arguments. Trim those preambles to one sentence each ("Chapter 1 established that context is finite; here's how to implement that insight") and give the recovered space to implementation detail. The reader who's reached Chapter 10 doesn't need to be re-sold on the problem. They need the spec.
