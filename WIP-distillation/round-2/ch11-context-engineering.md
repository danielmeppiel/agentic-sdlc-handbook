# Ch11 — Integration draft (ATTENTION ANCHOR as spine)

> Source decisions: `WIP/round-1/AUTHOR-DECISIONS.md` (C8 voice, C4 split, C1 Shape A).
> Source pattern: `skills/genesis/assets/design-patterns.md:617-683` (B8 ATTENTION ANCHOR).
> Source primitive: `skills/genesis/assets/primitives.md:192-208` (PLAN PERSISTENCE).
> Target chapter: `apm-handbook/handbook/ch11-context-engineering.qmd` (335 lines).

---

## 1. Integration thesis

Ch11 today is a budget chapter. Its central frame is "context window as fixed
capacity, allocated across segments." That frame is correct but incomplete. It
treats the window as a *static* resource, when in practice the dominant failure
mode of long agent sessions is *dynamic*: attention does not weight the window
uniformly, and the weight assigned to any given token decays as the session
extends. A turn-0 acceptance criterion does not get evicted from the window at
turn 30; it gets *ignored* there. Buffer accounting cannot describe this.
Behavioral re-injection can.

Genesis's B8 ATTENTION ANCHOR names this exact phenomenon and prescribes the
cure:

> CLASSICAL ANALOG: NONE. This pattern has no faithful classical
> counterpart -- it is induced by LLM physics (attention decay over
> distance / over turns) rather than by software-engineering structure.
> It is, however, the single most important behavioral pattern for any
> non-trivial agent task.
>
> -- `skills/genesis/assets/design-patterns.md:619-623`

Three properties qualify B8 as the chapter spine, not a sidebar:

1. **No classical counterpart.** Every other Ch11 concept (instruction
   hierarchy, scoping, retrieval, session reset) has a software-engineering
   ancestor a reader can pattern-match to. B8 does not. It is a pattern induced
   by LLM physics, and naming it is itself the contribution.
2. **It absorbs the existing chapter content as supporting structure.** The
   instruction hierarchy, the size discipline, the reset triggers, the
   retrieval rule — each is a *mechanism* for keeping the anchor effective.
   Recasting them as anchor-supporting machinery sharpens what they are *for*,
   without rewriting the underlying advice.
3. **Plant-the-flag window is open.** Per the thought-leadership review, "the
   most-named, least-claimed concept in the public agentic-dev conversation
   right now" (`WIP/round-1/thought-leadership.md:104`). The handbook is the
   right surface to claim it.

The reframe in one sentence: **context engineering is not buffer management;
it is attention-budget management, and the load-bearing primitive is the
ATTENTION ANCHOR.**

---

## 2. Existing chapter map -> proposed map (with B8 spine)

### Existing map (335 lines, 9 sections)

| # | Section                       | Frame                              |
|---|-------------------------------|------------------------------------|
| 1 | The Context Budget            | Static allocation across segments  |
| 2 | The Instruction Hierarchy     | 5-layer scoping                    |
| 3 | Agent Configuration           | Role, model, constraints           |
| 4 | Skill Design                  | Pattern-triggered playbooks        |
| 5 | Memory and Retrieval          | Stateless agents, three strategies |
| 6 | The Context Audit             | Inventory + categorize             |
| 7 | Before and After              | Worked example                     |
| 8 | Common Mistakes               | Anti-patterns                      |
| 9 | The Minimal Viable Context    | Starter kit                        |

The chapter's running metaphor is *spend* (budget, allocate, earn its space).
The footnote on lost-in-the-middle (`ch11:334`) is the single hint that
attention is not uniform, and it is buried.

### Proposed map (B8 spine; same 9-section count; one renamed section, two
new lead-in subsections, one new closing primer)

| # | Section                                             | Status        |
|---|-----------------------------------------------------|---------------|
| 1 | The Attention Budget *(was: The Context Budget)*    | Reframed      |
| 1a| Attention is not uniform *(new sub)*                | New           |
| 1b| The ATTENTION ANCHOR *(new sub, verbatim def box)*  | New (B8)      |
| 2 | The Instruction Hierarchy                           | Light edit    |
| 3 | Agent Configuration                                 | Unchanged     |
| 4 | Skill Design                                        | Unchanged     |
| 5 | Memory and Retrieval                                | Reframed lead |
| 5a| Re-injection boundaries *(new sub)*                 | New (B8)      |
| 6 | The Context Audit                                   | Unchanged     |
| 7 | Before and After                                    | Unchanged     |
| 7a| Worked example: re-anchoring a long plan *(new)*    | New           |
| 8 | Common Mistakes                                     | + 3 entries   |
| 9 | The Minimal Viable Context                          | Light edit    |

The reframe is concentrated in §1, §1a, §1b, §5, §5a, §7a, §8. Sections 2-4,
6, 9 receive surgical cross-links but no structural change.

---

## 3. Section-by-section edit plan

**§1 The Attention Budget (rename + retarget).** Change the section title from
"The Context Budget" to "The Attention Budget." Keep the existing pie chart
and the table of segment percentages — they are correct as a starting
allocation. Add a one-paragraph hinge after the table: the segment view
answers *what you put in*; it does not answer *how the model weights what is
in*. That second question is where the chapter lives.

**§1a Attention is not uniform (new subsection, ~150 words).** Promote the
existing `[^ch11-middle]` footnote material into body text. State plainly: tokens
are not weighted uniformly across the window; early and late tokens dominate;
middle content degrades; the weighting is also a function of *distance from the
current turn* in multi-turn sessions. Cite Liu et al. once. End with: this is
the property that makes context engineering a discipline rather than an
allocation problem.

**§1b The ATTENTION ANCHOR (new subsection, with verbatim definition box).**
Introduce the named pattern. One verbatim definition box (per C8 voice rule),
then handbook prose around it explaining what re-injection looks like in
practice on the tools the reader already uses. Cross-link forward to §5a (the
re-injection boundaries) and to Ch09 §PLAN PERSISTENCE (the substrate where
the anchor lives).

**§2 The Instruction Hierarchy.** No structural change. Add a single sentence
to the closing paragraph: the hierarchy is the *static* half of attention
discipline; the ATTENTION ANCHOR (§1b) is the *dynamic* half. One reference
cite to Ch10 §E Explicit Hierarchy already exists; keep it.

**§5 Memory and Retrieval (reframed lead).** The current opening sentence —
"Agents are stateless" — stays. Add one paragraph after it: statelessness
within a session is solved by reset; statelessness *across* the window inside
a session is solved by re-injection. Then list the three existing strategies
unchanged, and add §5a.

**§5a Re-injection boundaries (new subsection, ~200 words).** State the five
B8 boundaries verbatim:

> - start of every meaningful step,
> - before any spawn,
> - after any spawn returns,
> - after any tool failure or error recovery,
> - at any natural pause in execution.
>
> -- `skills/genesis/assets/design-patterns.md:635-639`

Then explain in handbook register what each looks like for a reader using
Copilot CLI / Claude Code / Cursor: what "re-inject" means concretely (re-read
the plan file; re-state the goal at the top of the next turn; pass the goal
explicitly into a sub-agent prompt). Cross-link to Ch13 checkpoint discipline
(§Checkpoint Discipline at `ch13:215`) — checkpoints are the same boundaries
viewed from the execution side.

**§7a Worked example: re-anchoring a long plan (new, ~350 words + 1 mermaid).**
Concrete walkthrough: a 30-turn refactor session, plan file persisted, anchor
re-read at five marked points, attention budget visualised against token
distance with anchor positions. This is the chapter's worked-example slot for
the new spine, mirroring the role §7 plays for the instruction hierarchy.

**§8 Common Mistakes — add three entries.** The B8 anti-patterns map cleanly
onto the existing "Common Mistakes" section. Add ANCHOR DRIFT, OVER-ANCHORING,
IMPLICIT-ANCHOR as three new bolded items, each two-to-three sentences in
handbook register, with the verbatim Genesis names retained.

**§9 The Minimal Viable Context — one-line addition.** Append a fourth row to
the starter table: "Plan file with goal + acceptance criterion at top, re-read
at every step boundary." Cross-link Ch09 §PLAN PERSISTENCE.

---

## 4. Full draft of changed sections

### §1 The Attention Budget *(retitled; closing hinge added)*

> Edit instruction: rename section header from "The Context Budget" to "The
> Attention Budget." Keep paragraphs at `ch11:11-50` unchanged. After the
> existing closing sentence at `ch11:50` (`...it actively degrades performance
> on the task that matters.`), append the following hinge paragraph:

The segment view answers a question of *spend*: of the tokens you load, what
fraction goes to instructions, to code, to history. It does not answer the
deeper question of *weight*: of the tokens already in the window, which ones
the model is actually attending to right now. Treating the window as a flat
buffer hides this. The rest of the chapter treats it as an attention budget
instead — a resource that decays with distance and must be actively renewed.

### §1a Attention is not uniform *(new subsection)*

Tokens in a context window are not weighted equally. Material at the start of
the window and material near the current turn carry disproportionate
influence; material in the middle degrades.[^ch11-middle] In a long session,
the same effect operates across turns: instructions issued at turn 0 lose
influence by turn 30, not because they have been evicted from the window, but
because the model's attention is preferentially anchored to the recent end of
the conversation. The token is still there. It is just no longer load-bearing.

This is the property that makes context engineering a discipline rather than
an allocation problem. If attention were uniform, "fit it in the window" would
be a complete strategy. Because attention decays with distance, the question
shifts: how do you keep the goal, the hard constraints, and the acceptance
criterion *load-bearing* at turn 30, when they were stated at turn 0?

### §1b The ATTENTION ANCHOR *(new subsection, verbatim definition box)*

Genesis names the cure for this failure mode the **ATTENTION ANCHOR**. The
definition is worth quoting in full, because the property the pattern relies on
has no classical software-engineering counterpart:

> **B8. ATTENTION ANCHOR**
>
> CLASSICAL ANALOG: NONE. This pattern has no faithful classical
> counterpart -- it is induced by LLM physics (attention decay over
> distance / over turns) rather than by software-engineering structure.
> It is, however, the single most important behavioral pattern for any
> non-trivial agent task.
>
> WHEN: any session that will exceed roughly a few dozen turns, or any
> plan whose acceptance criterion / hard constraints were established at
> turn 0 and must still hold at turn N. Long-running tasks WITHOUT
> periodic re-injection of the goal and hard constraints DRIFT silently
> from initial intent. This is the dominant failure mode of agentic
> work past trivial scope.
>
> MECHANISM: the goal, the hard constraints, and the acceptance criterion
> are RE-INJECTED into context at scheduled boundaries:
>
> - start of every meaningful step,
> - before any spawn,
> - after any spawn returns,
> - after any tool failure or error recovery,
> - at any natural pause in execution.
>
> -- Genesis, B8 ATTENTION ANCHOR
> (`skills/genesis/assets/design-patterns.md:617-639`)

Three things to read out of that definition. First, the cure is *behavioral*,
not architectural — no new file format solves this; the operator (or the
orchestrator) has to actively re-state the goal at the listed boundaries.
Second, the anchor's source of truth lives outside the context window, so it
cannot itself decay. In practice this is a plan file, persisted on disk and
re-read on demand — the primitive Chapter 9 catalogs as PLAN PERSISTENCE.
Third, the anchor is the goal plus the hard constraints, *not the full plan
body*. Re-injecting too much defeats the savings of the original
decomposition. The discipline is concise, deliberate restatement, performed
often.

The rest of this chapter is organised around making that discipline
sustainable: §2-§4 keep the *static* anchor (the instruction hierarchy)
relevant and small; §5-§5a make the *dynamic* anchor (re-injection at
boundaries) cheap to perform; §7a walks through one full session to show what
the discipline looks like in practice.

### §5 Memory and Retrieval *(reframed lead — insert after the existing
opening "Agents are stateless..." paragraph at `ch11:201`)*

Statelessness has two forms, and they have different cures. The form most
readers think of first — context vanishes when the session ends — is solved by
session discipline (when to reset, what to carry forward; covered below). The
second form is subtler and operates *inside* a single session: tokens stated
early lose attention weight as the session extends, even though they remain
nominally in the window. The cure for the second form is not retrieval; it is
re-injection. The next subsection makes that concrete.

### §5a Re-injection boundaries *(new subsection)*

The ATTENTION ANCHOR (§1b) prescribes five boundaries at which the goal and
hard constraints should be re-injected into the active context:

> - start of every meaningful step,
> - before any spawn,
> - after any spawn returns,
> - after any tool failure or error recovery,
> - at any natural pause in execution.
>
> -- `skills/genesis/assets/design-patterns.md:635-639`

In a tool like Copilot CLI, Claude Code, or Cursor, the practical translation
is direct. *Start of every meaningful step* means the operator (or the agent,
when self-directing) re-reads the plan file before opening a new file or
calling a new tool, and quotes the relevant goal back at the top of the
prompt. *Before any spawn* means a sub-agent prompt is constructed by copying
the goal and the acceptance criterion verbatim into the dispatch — never
relying on the parent's already-decayed context to be inherited. *After any
spawn returns* means the parent re-states the goal before integrating the
child's output, because the parent has just spent N turns watching unrelated
work. *After any tool failure* covers the case where a stack trace, a long
diff, or a long error message has just consumed the last several thousand
tokens of attention; the goal has been pushed to the middle of the window and
needs to be brought back to the front. *At any natural pause* is the cheap
move: when the next step is uncertain, re-read the plan rather than
extrapolate from the conversation tail.

These boundaries are the same boundaries Chapter 13 calls *checkpoints* (see
§Checkpoint Discipline at `ch13:215`). The execution chapter views them as the
moments when validation happens; this chapter views them as the moments when
attention is renewed. They are the same moments. Both views are correct.

### §7a Worked example: re-anchoring a long plan *(new section)*

Consider a session whose goal is `Refactor the authentication module to use
the AuthResolver chain; do not break the legacy basic-auth path; ship with
parity tests green.` The plan file lives at `plan.md` in the working
directory. It contains, at the top, the goal verbatim, two hard constraints
(`do not modify token storage schema`, `parity tests must remain green`), and
an ordered todo list of seven steps.

The naive execution runs straight through, accumulating context as it goes.
By turn 25 the model has read four files, modified three, hit two test
failures, and watched a long stack trace go by. The original goal is still in
the window — somewhere around turn 0 — but its attention weight has decayed.
The model now proposes a refactor of token storage, because the local context
of turn 25 makes that refactor look reasonable. The goal said *do not modify
token storage schema*. The constraint is no longer load-bearing.

The anchored execution looks different. The plan file is re-read at each of
the five B8 boundaries. Mechanically, the re-injection is one cheap action:
the operator (or the orchestrator) prepends a four-line block to the next
prompt — `Goal: ...` / `Hard constraints: ...` / `Acceptance: ...` / `Current
step: 4 of 7` — drawn from the plan file. The token cost is small. The effect
is to push the goal back to the high-attention end of the window. The
proposal to refactor token storage now lands against an active constraint
rather than a decayed one, and is correctly rejected.

The diagram below shows the same session in attention-weight terms: token
distance from the current turn on the x-axis, an informal attention weight on
the y-axis, with the five anchor positions marked as the points where the
goal is renewed.

```{mermaid}
%%| fig-width: 5.5
%%| fig-cap: "Attention weight versus token distance in a 30-turn session, with ATTENTION ANCHOR re-injection points marked. Without re-injection, the goal stated at turn 0 decays into the low-weight middle of the window. Each anchor point copies the goal back to the high-weight recent end."
%%| fig-alt: "Flowchart with five labeled anchor positions across a 30-turn session. Turn 0 begins with goal and constraints at full attention weight. By turn 10, attention to early tokens has decayed and an anchor re-injection at turn 10 restores the goal. Turn 16 shows a pre-spawn anchor before dispatching a sub-agent. Turn 21 shows a post-spawn anchor when the parent recovers focus. Turn 25 shows a post-failure anchor after a tool error consumed attention. Turn 30 shows the acceptance check reading from the same anchor source. Across the bottom, an arrow labeled PLAN PERSISTENCE indicates the on-disk plan file as the substrate that all five anchors read from."
%%| label: fig-attention-anchor
flowchart LR
    T0["turn 0<br/>GOAL + CONSTRAINTS<br/>injected fresh"] --> T10
    T10["turn 10<br/>anchor: re-inject<br/>at step boundary"] --> T16
    T16["turn 16<br/>anchor: pre-spawn<br/>copy goal to child"] --> T21
    T21["turn 21<br/>anchor: post-spawn<br/>parent recovers focus"] --> T25
    T25["turn 25<br/>anchor: post-failure<br/>after error recovery"] --> T30
    T30["turn 30<br/>acceptance check<br/>reads same anchor"]

    PP["PLAN PERSISTENCE<br/>(on-disk plan.md — survives the window)"]
    PP -. "re-read" .-> T10
    PP -. "re-read" .-> T16
    PP -. "re-read" .-> T21
    PP -. "re-read" .-> T25
    PP -. "re-read" .-> T30
```

The cadence in the diagram is roughly one anchor per ten turns of unstructured
work, with extra anchors triggered by spawn boundaries and error recovery. On
a 128K-token window with average turn cost of ~1K tokens, that is an anchor
every ~10K tokens of accumulated session context — a useful default to start
from, not a benchmark. Calibrate based on observed drift: if the agent
proposes work that violates a stated constraint, the previous anchor was too
far back.

The substrate that makes all of this cheap is the plan file. The anchor
itself is short — three or four lines — but the *source of truth* for the
anchor lives outside the window so it cannot itself decay. Chapter 9 catalogs
that file as a primitive in its own right (§PLAN PERSISTENCE). The anchor is
the discipline; the plan file is the substrate the discipline reads from.

### §8 Common Mistakes *(append three entries after the existing six)*

**ANCHOR DRIFT.** Silently rewriting the goal or the acceptance criterion
mid-session to match emerging results. The anchor is now a description of
what the agent is doing, not a constraint on what it should be doing. If the
goal genuinely needs to change, change it explicitly — escalate to a human,
update the plan file, and re-state the new goal as a fresh anchor. Quiet
edits to the anchor are how long sessions converge on the wrong deliverable.

**OVER-ANCHORING.** Re-injecting the entire plan body on every turn. The
anchor is meant to be the goal plus the hard constraints, not the full plan.
Re-injecting too much defeats the savings of the original decomposition and
crowds out the working context the model needs to actually take the next
step. Three or four lines is usually enough. If the anchor has grown past
half a screen, the plan itself probably needs to be split.

**IMPLICIT-ANCHOR.** Assuming the model "remembers" the goal because it was
stated at turn 0. Attention decays with distance; early tokens lose
influence. There is no implicit anchor in a long session — there is either an
explicit re-injection at the boundaries listed in §5a, or there is silent
drift. The choice is binary.

### §9 The Minimal Viable Context *(append one row)*

> Edit instruction: append a fourth row to the table at `ch11:325-328`:

| File | Scope | Contains |
|------|-------|----------|
| Plan file (`plan.md`) | Per-session | Goal + hard constraints + acceptance criterion at the top; ordered todo list below; re-read at every step boundary (see §1b ATTENTION ANCHOR; Ch09 §PLAN PERSISTENCE) |

---

## 5. Cross-link audit

| From                                                  | To                                                  | Direction | Status         |
|-------------------------------------------------------|-----------------------------------------------------|-----------|----------------|
| Ch11 §1b ATTENTION ANCHOR                             | Ch10 §E Explicit Hierarchy (`ch10:292`)             | outbound  | New, add       |
| Ch11 §1b ATTENTION ANCHOR                             | Ch09 §PLAN PERSISTENCE (post-C4-split)              | outbound  | New, add       |
| Ch11 §5a Re-injection boundaries                      | Ch13 §Checkpoint Discipline (`ch13:215`)            | outbound  | New, add       |
| Ch11 §7a Worked example                               | Ch09 §PLAN PERSISTENCE                              | outbound  | New, add       |
| Ch11 §9 MVC table row                                 | Ch11 §1b; Ch09 §PLAN PERSISTENCE                    | inbound   | New, add       |
| Ch10 PROSE-axis closing (axis-to-primitive table)     | Ch11 §1b ATTENTION ANCHOR (Explicit Hierarchy axis) | inbound   | Recommend add  |
| Ch13 §Checkpoint Discipline                           | Ch11 §5a Re-injection boundaries                    | inbound   | Recommend add  |
| Ch14 anti-patterns (when ANCHOR DRIFT lands there)    | Ch11 §8 (ANCHOR DRIFT, OVER-ANCHORING, IMPLICIT)    | inbound   | Defer to Ch14  |

The two **Recommend add** rows are not strictly required for Ch11's
self-sufficiency, but they close the loop with adjacent chapters. The Ch10
inbound is the cleanest reciprocal — the PROSE-axis-to-primitive table at
`primitives.md:233-239` already maps Explicit Hierarchy to a Genesis
primitive; Ch10's closing should mirror that mapping and point forward to
§1b. The Ch13 inbound is a one-sentence cross-reference: the checkpoint
discipline already names the moments; naming them as anchor moments costs
nothing and reinforces both chapters.

The Ch14 row is deferred. Per AUTHOR-DECISIONS C5 (partial absorption), Ch14
is the home for practitioner-grade anti-pattern entries; if ANCHOR DRIFT et
al. graduate from §8 entries to full Ch14 entries in a later round, the
inbound link adds itself naturally. Round 2 keeps them in §8 only.

---

## 6. Impact summary

**Net structural change.** Chapter goes from 9 sections (335 lines) to 9
sections (~470-490 lines projected). Three new subsections (§1a, §1b, §5a),
one new worked example (§7a), three new anti-pattern entries in §8, one new
table row in §9. One section rename (§1). Sections 2-4, 6, 7 unchanged in
substance.

**Net thesis change.** The chapter's load-bearing concept shifts from
*context-as-buffer* to *context-as-attention-budget*. The instruction
hierarchy, scoping, retrieval, and reset discipline retain all their existing
content but are now *in service of* keeping the ATTENTION ANCHOR effective,
rather than free-standing recommendations. This is the highest-impact
positioning change in the corpus per `WIP/round-1/SYNTHESIS.md:39` and
`WIP/round-1/thought-leadership.md:104`.

**Voice compliance (C8).** One verbatim definition box in §1b. Pattern name
ATTENTION ANCHOR retained ALL-CAPS verbatim throughout. Anti-pattern names
ANCHOR DRIFT, OVER-ANCHORING, IMPLICIT-ANCHOR retained verbatim. Surrounding
prose in handbook register. Genesis citations carry source path and line
range.

**Primitive cross-links (C4 split).** §1b, §7a, §9 cross-link Ch09 §PLAN
PERSISTENCE as the substrate primitive. This is the load-bearing link that
makes the C4 split visible to Ch11 readers — without it, the anchor's source
of truth has no named home.

**Canonical naming (C1 Shape A).** ATTENTION ANCHOR, PLAN PERSISTENCE used as
canonical names. No buzzword translation. No alternate names introduced.

**Reading-time delta.** Estimated +4-5 minutes of reading time for the new
material, against a current chapter that already runs ~18-20 minutes. The new
material is dense by design (pattern definition + worked example) but the
existing sections are not lengthened, so the marginal cost lands on readers
who care about the spine and not on readers skimming for the budget table.

**Risk.** The single risk is over-quoting Genesis in the surrounding prose
and drifting out of handbook register. Mitigated by the C8 rule: one verbatim
box per pattern, surrounding prose in handbook voice. The draft above keeps
verbatim quotation to two locations (§1b definition box, §5a boundary list),
both clearly delimited, both attributed with source path and line.

**Downstream chapter impact.**
- *Ch09:* needs the C4 split landed (PLAN PERSISTENCE as its own §) before
  the §1b and §7a cross-links resolve. Already scheduled per AUTHOR-DECISIONS
  decision #3.
- *Ch10:* recommended one-line addition in the PROSE-axis closing to
  cross-link Explicit Hierarchy axis to ATTENTION ANCHOR. Optional; chapter
  is self-sufficient without it.
- *Ch13:* recommended one-sentence cross-reference from §Checkpoint
  Discipline. Optional; Ch11 is self-sufficient without it.
- *Ch14:* no required change in this round. ANCHOR DRIFT et al. live in §8.
  May graduate to Ch14 in a later round if practitioner evidence warrants.
