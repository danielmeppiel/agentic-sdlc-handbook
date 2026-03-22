# Ch11 Review — Dev Lead Proxy

**Reviewer:** Dev Lead Proxy (The Impatient Practitioner)
**Chapter:** Chapter 11: Context Engineering
**Verdict:** **SHIP** — with 3 targeted revisions

---

## Can I use this Monday?

**Yes.** This is the most immediately actionable chapter I've read. The Minimal Viable Context section at the end (3 files, iterate from real failures) is exactly how I'd pitch this to my team in standup. The context audit steps are real — I could run Step 1 in a 30-minute team retro tomorrow.

## Best technique

The instruction hierarchy with `applyTo` scoping. I've been maintaining a single massive `INSTRUCTIONS.md` and watching agents ignore half of it. The idea that auth rules unload when the agent moves to frontend code is the "aha" moment. The 300 lines across 8 files vs. 100 lines in 1 file comparison makes the case concretely.

## Section-by-Section

### The Context Budget — STRONG
The ASCII diagram is immediately useful. I can point at it and say "we control these two bands." The decision rule ("does this earn its space?") is the kind of one-liner I'd paste in a team Slack channel. The observation about middle-of-window attention degradation is the kind of thing I'd otherwise learn the hard way.

One gap: no actual token numbers. You say "~15-25%" for instructions — 15-25% of *what*? Claude's 200k? Copilot's effective window? A single concrete example ("on a 128k-token window, your 50-line instruction file costs ~2k tokens, leaving you ~40-60k for code context") would make the budget metaphor actually budgetable. Right now it's a useful mental model but I can't do math with it.

### The Instruction Hierarchy — STRONGEST SECTION
This is the chapter's centerpiece and it delivers. The three-tier examples (global → directory → file) are concrete and copy-pasteable. The `applyTo` pattern is shown with real glob syntax. The composition example (editing `src/auth/token_resolver.py` loads layers 1+2+3) makes the mechanism click.

The file-scope example using `BaseIntegrator` is clearly drawn from a real project (APM itself), which adds credibility. The "the agent never has a second week" line is memorable and exactly right.

### Agent Configuration — GOOD, WANTS MORE
The YAML example is solid and real. The "You Never" section is the best idea in the chapter — encoding past mistakes as negative constraints. I'd use this immediately.

What's missing: how many agents is too many? You say "three to five" but don't say what happens when a team creates fifteen. Also, the model selection point ("complex decisions may warrant a more capable model") is hand-wavy. A sentence about *when* to pick Sonnet vs. Haiku vs. GPT-4.1 for specific task types would be more useful than the abstract guidance.

### Skill Design — GOOD
The three-question test (cross-file? more than a few rules? detectable trigger?) is a clean decision boundary. The CLI Logging UX example is real and demonstrates the "decision framework vs. rule list" distinction well.

The DRY argument for extracting skills from repeated instructions is convincing because it maps to something I already do with code.

### Memory and Retrieval — ADEQUATE
The three strategies (session, persistent, retrieval) are clearly laid out. The co-location argument is practical. The decision rule (always needed → instructions, sometimes → retrieval, once → prompt) is useful.

This section reads more like Block 1 theory than Block 2 practice. Compared to the hierarchy section which had copy-paste examples, this one stays at the conceptual level. What does "session discipline" look like in practice? When exactly should I reset? After 15 turns? 30? When the agent starts contradicting its earlier output? A concrete heuristic would help.

### The Context Audit — STRONG
Steps 1-5 are the kind of structured exercise I'd actually run. The "in code / in docs / in heads" classification is immediately clarifying — I know exactly which column my team's auth conventions fall into (heads, obviously). The priority-by-failure-cost matrix is pragmatic.

**Does it work on a 500k-line codebase?** Mostly. Steps 1-2 scale fine — you're listing conventions, not files. Step 4 (map to scope) could get overwhelming on a monorepo with 40 modules. A note about starting with the 3-5 most-edited directories (where agents will actually work) would keep this grounded.

### Before and After — EFFECTIVE BUT THIN
The Flask rate-limiting example works. The "same model, same task, different output" punch line lands. Three specific convention violations (custom rate limiter, env-based config, middleware.py registration) make the failure concrete rather than abstract.

What would make it stronger: show the actual instruction files that produced the good output. Right now you describe them in a bullet list ("a global instruction requiring..., a directory-scoped instruction..."). Showing the 10-15 lines of actual instruction content would close the loop — I'd see the input that produced the output, not just be told it exists. This is the chapter's thesis in miniature; the proof should be complete.

### Common Mistakes — GOOD
Every item maps to something I've done or seen. The "if you can't remember what's in your instruction file without re-reading it, the agent is having the same problem" line is a keeper. Practical, memorable, quotable.

### Minimal Viable Context — EXCELLENT CLOSER
This is exactly the right ending. Three files, real tasks, iterate from failure. The two-week timeline is credible. "Shaped by actual failure modes rather than theoretical completeness" is the right philosophy and the right sentence to end on.

---

## Top 3 Revisions

### 1. Add concrete token numbers to the Context Budget
The budget metaphor is the chapter's framing device, but it's un-budgetable without numbers. Add one worked example: pick a specific model context size, show how a real instruction set + code context + conversation history adds up, and show where the ceiling hits. This turns a useful analogy into a planning tool. Without it, a reader nods and moves on; with it, they open a spreadsheet.

### 2. Show the actual instruction files in the Before/After
The "after" example shows the *output* but only *describes* the inputs. Show the 3 instruction snippets (global, directory, skill) that produced the correct rate-limiting code. 15-20 lines total. This is the chapter's proof-of-concept — make it complete. A reader should be able to reconstruct the entire pipeline: "these instructions in, this code out."

### 3. Add a session reset heuristic to Memory and Retrieval
"Session discipline" is mentioned but never operationalized. Add a concrete rule of thumb: "Reset the session when [specific signal]. Carry forward [specific artifacts]." Something like "after 20+ turns or when the agent references files it read 15 turns ago — whichever comes first." Practitioners need a trigger, not a principle.

---

## Voice Comparison (vs. Ch01)

Ch01 is confident, opinionated, and builds tension before releasing it (the Vibe Coding Cliff → PROSE framework arc). Ch11 is more workmanlike — appropriately so for a "how-to" chapter, but it could use one or two of Ch01's sharper rhetorical moves. The opening paragraph is strong ("200,000 lines of code, a style guide nobody reads, three authentication patterns"). The closing paragraph is strong. The middle sections are clear but could occasionally punch harder. Not a rewrite issue — just a polish note for the editing pass.

Ch11 earns its place in the book. It delivers on Ch01's promise that Block 2 would answer "what to do Monday morning." Ship it with the three fixes above.
