# CTO Proxy Review: Chapters 5 & 7

**Reviewer:** VP Engineering / CTO persona — 400–2,000 engineers, board reporting obligations, seen every hype cycle.

---

## Chapter 5: Governance for AI-Assisted Delivery

### Would I finish this?

Yes. The opening paragraph — "An AI agent on your team just merged a pull request that touches your payment processing code" — is the exact scenario keeping me up at night. It earned the next 10 minutes of my time. The chapter stays concrete throughout; I never felt lectured.

### Strongest claim

The knowledge atrophy section. The aviation parallel (mandatory manual-flying requirements) is the first time I've seen this risk articulated with a mitigation model that isn't "just be careful." This is the section I'd forward to my VP of People and my architecture council. It names a real long-term risk that no other AI adoption material I've read treats seriously.

### Weakest claim

The governance readiness checklist looks good in a slide deck and will collapse on contact with a real legal/compliance team. Three problems:

1. **No prioritization logic.** Six capability areas, three maturity levels — that's 18 cells. The text says "start with audit trails and access controls," but a CISO will ask: *which* audit trail gaps matter for *our* regulatory posture? The checklist doesn't connect capabilities to specific compliance frameworks. I need a mapping: "If you're SOC 2 scoped, prioritize rows 1, 2, 6. If you handle PCI data, prioritize rows 3, 4." Without that, the checklist is a conversation starter, not a decision tool.

2. **"Enterprise" column is aspirational vapor.** "Full provenance chain… all queryable and linked to compliance artifacts" — with what tooling? At what cost? Over what timeline? The chapter never acknowledges that the Enterprise column may not be achievable with current-generation tools. A CTO who shows this to their compliance team will get asked "when do we get to Enterprise?" and have no answer.

3. **Missing: incident response.** What happens when agent-generated code causes a production incident? The risk taxonomy identifies failure modes but there's no runbook, no escalation model, no "who's accountable when the agent's code breaks prod at 2 AM." This is the first question my on-call team would ask.

### Missing

- **The risk taxonomy is incomplete.** Four categories (IP/data, quality, dependency, atrophy) miss two that my legal team would flag immediately: (a) **regulatory liability for autonomous decision-making** — when an agent makes an implementation choice that has compliance implications (e.g., choosing a data retention approach), who owns that decision legally? and (b) **supply chain risk** — agent-generated code as a vector for supply chain attacks (prompt injection, poisoned context, compromised instruction files). These aren't theoretical; they're in my threat model today.

- **The board reporting template is usable but shallow.** I'd actually use a version of it — the four-quadrant structure (adoption, value, cost, risk) maps to how my board thinks. But it's missing the one thing boards actually care about: **trend lines and targets.** "Number of developers using agent tools" is a snapshot. "60% adoption against a target of 80% by Q3, up from 40% last quarter" is a board-ready metric. The template needs a "Target" and "Trend" column or it reads like a status update, not a governance artifact.

- **No mention of insurance/liability implications.** If agent-generated code causes a breach, does our E&O policy cover it? Does our cyber insurance? This is not a niche concern — it's a question my CFO will ask in the first board meeting where this template appears.

### Verdict: **REVISE**

### Top 3 Revisions

1. **Add a compliance-framework mapping to the governance checklist.** For each major framework (SOC 2, PCI DSS, HIPAA, EU AI Act), indicate which capability rows are critical. Turn the checklist from a self-assessment into a compliance gap analysis tool. Add a sentence acknowledging that the "Enterprise" column represents a target state that may require tooling that doesn't exist yet.

2. **Expand the risk taxonomy to six categories.** Add "Regulatory liability for autonomous decisions" and "Supply chain / context integrity risk." Both are real, both are being discussed in security and legal communities now, and both are conspicuously absent from a chapter titled "Governance."

3. **Upgrade the board template with targets and trends.** Add "Target" and "Trend" columns to every metric row. Add an "Insurance & Liability" row to the risk section. A board reporting artifact without targets is a status email, not a governance tool.

---

## Chapter 7: Planning the Transition

### Would I finish this?

Yes — and I'd hand it to my Chief of Staff to operationalize. The opening scenario (pilot goes well → inconclusive rollout → executive asking for ROI evidence) is a verbatim description of what I've seen at two previous companies. The chapter earned trust in the first three paragraphs.

### Strongest claim

The Productivity Paradox section is the best articulation I've read of why naive productivity metrics are dangerous for AI tool adoption. The specific insight — "some organizations discover, after months of 'increased productivity,' that their total cost per feature has stayed flat" — is something I've observed but never seen written down this clearly. This section alone justifies the chapter.

### Weakest claim

The phased adoption model is **realistic in structure but optimistic in timeline.** Three specific problems:

1. **Phase 1 at "Months 1–3" assumes the team already has documentation.** The readiness assessment correctly identifies that most teams have oral-tradition codebases. But Phase 1 says "build the minimum viable context layer" as a bullet point inside a 3-month phase that also includes baseline measurement, tool setup, training, observation, and retrospectives. For a team starting from zero documentation, building even a minimal context layer is a 4–6 week effort by itself. Phase 1 is realistically 4–5 months for most organizations I've led.

2. **Phase 2's "pilot members become coaches" model breaks at scale.** If I have 2 pilot teams and need to expand to 5, I'm pulling senior people off delivery to coach. The chapter doesn't address the capacity cost or suggest when to hire/assign dedicated enablement roles. In my experience, the coaching model works for Phase 2 but you need a dedicated platform/enablement function by Phase 3. This gap means Phase 3's "self-service onboarding" is aspirational without the investment the chapter never mentions.

3. **Phase 3 "months 6–12" is aggressive for an org of 400+ engineers.** Getting remaining teams (including those initially "not ready") onboarded, with self-service documentation, continuous context maintenance, and advanced workflows — in 6 months? At 2,000 engineers, this is an 18–24 month Phase 3. The chapter should acknowledge that timelines scale with org size and provide multipliers or ranges.

### Missing

- **The metrics are genuinely useful — but the generation-to-review ratio needs operationalization.** The chapter calls it "the single most important metric" and then doesn't explain how to measure it. What tooling captures this? Is it self-reported? Derived from PR timestamps? Estimated from task tracking? A metric you can't measure is a vanity metric in disguise. The chapter needs a "how to instrument" paragraph for this metric specifically.

- **The skill development paths are role-accurate but ignore team dynamics.** The paths describe what each role needs individually. They don't address: (a) what happens when a senior engineer refuses to learn context engineering ("that's not my job"), (b) how to handle the politics of juniors who adopt faster than seniors, (c) the very real scenario where your best architect thinks this is all hype and becomes a blocker. These aren't edge cases — they're the default in every tooling transition I've led. A "Common resistance patterns and responses" subsection would be more valuable than another role description.

- **No budget template.** The chapter plans every dimension of the transition except the financial one. I need a rough cost model: tool licenses per seat, estimated API/token costs per developer per month, enablement investment (coaching hours, documentation time), infrastructure. Chapter 3 covers ROI, but the transition plan should include a "what to budget for each phase" section. Without it, I can't write the proposal that gets this funded.

- **No failure/rollback criteria.** The exit signals tell me when to advance. Nothing tells me when to stop, scale back, or abandon. What if Phase 1 metrics show the tools aren't producing value on our codebase? What's the kill criteria? A transition plan without rollback conditions is an escalation of commitment waiting to happen.

### Verdict: **REVISE**

### Top 3 Revisions

1. **Add realistic timeline ranges scaled to org size.** Replace fixed "Months X–Y" with ranges: "Months 1–3 for orgs under 200 engineers; 2–5 months for 200–1,000; 3–6 months for 1,000+." Acknowledge that Phase 1 duration depends heavily on existing documentation maturity. Add a note that Phase 3 for large enterprises is 12–24 months, not 6–12.

2. **Operationalize the generation-to-review ratio metric.** Add a concrete paragraph: how to measure it (PR metadata + task tracking timestamps), what tooling supports it, what the expected range looks like (e.g., "healthy teams see 3:1 generation-to-review; below 1.5:1 indicates context quality problems"). Without instrumentation guidance, the "single most important metric" is the single most likely to be ignored.

3. **Add rollback criteria and a resistance-patterns section.** For each phase, define conditions under which you pause or revert ("If Phase 1 review rejection rate exceeds 60% after 6 weeks, pause and invest in context quality before continuing"). Add a short section on common human resistance patterns (senior refusal, junior over-trust, architect skepticism) with concrete responses. These are the dynamics that actually determine whether a transition succeeds or fails.

---

## Summary

| Chapter | Verdict | Key Gap |
|---|---|---|
| Ch 5 — Governance | **REVISE** | Checklist needs compliance-framework mapping; risk taxonomy incomplete; board template needs targets |
| Ch 7 — Transition | **REVISE** | Timelines optimistic for large orgs; key metric not operationalized; no rollback criteria |

Both chapters are strong drafts — among the best I've seen on these topics for AI-assisted development. The writing is tight, the frameworks are actionable, and the tone respects my time. The revisions above are the difference between "useful reference" and "something I'd actually implement from."
