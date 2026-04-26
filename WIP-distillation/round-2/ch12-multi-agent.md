# Ch12 — Integration draft (named architectural patterns for multi-agent)

> Scope: integrate Genesis's named architectural patterns (A1 PANEL,
> B1 FAN-OUT + SYNTHESIZER, C3 THREAD SPAWN, over the CHILD-THREAD
> SPAWN primitive) into Ch12 without rewriting the chapter's voice or
> renaming any handbook role. Follows AUTHOR-DECISIONS.md (C7 Shape C,
> C8 voice rule, C9 bounded-rounds, C1 Shape A).

---

## 1. Integration thesis

Ch12 already delivers the *motivation* for multi-agent orchestration:
context budgets, specialization, wave ordering, conflict resolution,
and the coordination tax. What it does not yet do is *name the shapes*
that practitioners are building. Genesis names them, and the names are
useful: they let the reader recognize a topology in the wild, audit it
against three or four anti-patterns specific to that shape, and select
between alternatives by WHEN-clause rather than by analogy.

The integration goal is therefore narrow and additive:

1. Pair each handbook role/topology with the canonical Genesis
   pattern, by adding ONE second sentence per pattern section
   (Shape C from C7) -- never replacing the handbook header.
2. Insert a verbatim Genesis definition box per named pattern (C8
   voice rule), so readers who have only ever met "Writer / Reviewer
   / Tester" can map the same shape onto A1 PANEL when they read a
   review skill, a review GitHub Action, or a panel-style harness.
3. Make explicit that **CHILD-THREAD SPAWN is the primitive** under
   all three patterns (C1 Shape A): A1, B1, C3 are progressively
   higher-level shapes built on the same runtime affordance.
4. Replace the current rate-of-intervention prose at `ch12:317` with
   the handbook's existing **"two failed dispatches"** discipline
   (already used at `ch14:216`) so bounded rounds becomes one wording
   across the book, applied as **calibration, not measurement**
   (C9 / TL §4a).

The composition the chapter implies is now namable end-to-end:

> **CHILD-THREAD SPAWN** (primitive, runtime affordance) -- the unit.
> **C3 THREAD SPAWN** (design pattern) -- the discipline of using one
> child thread per scoped unit of work, with isolation as the goal.
> **B1 FAN-OUT + SYNTHESIZER** (design pattern) -- N parallel
> C3 spawns plus a synthesis pass.
> **A1 PANEL** (architectural pattern) -- a B1 fan-out where the N
> children are *specialized lenses* (personas) and the synthesis is
> itself a decision.

The chapter's existing Writer/Reviewer/Tester pattern is exactly an
A1 PANEL of N=3. The chapter's existing Domain Teams pattern is an
A1 PANEL of variable N specialised by area. The chapter's existing
Audit/Execute/Validate pattern is a PIPELINE whose audit stage is
itself a B1 fan-out. None of these need new prose -- only the
right name attached.

---

## 2. Pattern mapping table

| Handbook role / topology (Ch12 prose, unchanged) | Genesis pattern (canonical, ALL-CAPS verbatim) | Section in Ch12 |
|---|---|---|
| Writer / Reviewer / Tester | **A1 PANEL** (footnote-style second sentence + definition box) | §Pattern 1 (`ch12:53`) |
| Domain Teams (Architecture / Domain / Security / Docs) | **A1 PANEL** with variable N (cross-reference to §Pattern 1) | §Pattern 2 (`ch12:72`) |
| Concrete Dispatch ("dispatching the agent") | **C3 THREAD SPAWN** (over CHILD-THREAD SPAWN primitive) | §Pattern 2, "Concrete Dispatch" subsection (`ch12:85`) |
| Audit / Execute / Validate | **A2 PIPELINE** with **B1 FAN-OUT + SYNTHESIZER** at the audit stage (cross-link only; A2 owned by Ch13 deep-dive) | §Pattern 3 (`ch12:131`) |
| Wave-Based Parallelism | **A5 WAVE EXECUTION** (cross-link only; A5 owned elsewhere — out of scope here) | §Parallelization Strategies (`ch12:175`) |
| Session Isolation, "fresh session", "stateless workers" | **CHILD-THREAD SPAWN** primitive (Ch09 cross-link) | §Session Management (`ch12:381`) |
| Rate-of-intervention threshold (~25 dispatches, 12% rate) | **Bounded-rounds discipline** -- "two failed dispatches" wording (`ch14:216`) framed as **calibration not measurement** (`ch12:317`) | §Conflict Resolution → Design Conflicts (`ch12:311`) and §Escalation Protocol (`ch12:335`) |

Anti-pattern callouts to attach (from Genesis, verbatim names, all
HIGH severity in Ch14's catalogue once the panel cross-references
them):

- **PANEL-IN-ONE-CONTEXT** -- running N lenses sequentially in a
  single window. The Ch12 §Session Isolation prose already implies
  this; naming it makes the failure searchable.
- **PANEL-WITHOUT-SYNTHESIS** -- N lenses, then a concatenation. The
  user reads N reports instead of one decision.
- **IMBALANCED PANEL** -- N-1 agree, 1 dissents, the synthesis follows
  the majority without examining the dissent.
- **FAN-OUT-IN-ONE-CONTEXT** -- the same failure as PANEL-IN-ONE-
  CONTEXT, generalized to any B1 shape.
- **UNBOUNDED SPAWN** -- letting any thread spawn any depth of
  descendants. Couples to bounded-rounds discipline below.

These five names live in Ch14 (per C5 partial-absorption decision);
Ch12 cross-links them inline at the points they are most relevant.

---

## 3. Section-by-section edit plan

The edits are surgical. Every change is additive except (a) the
intervention-rate paragraph at `ch12:317`, which is reworded to align
with `ch14:216`, and (b) the L2/L3 protocol lines, which gain one
half-sentence each. No section is deleted or reordered.

### Edit 1. §Pattern 1: Writer / Reviewer / Tester (`ch12:53`)

- Keep the heading "Pattern 1: Writer / Reviewer / Tester" verbatim.
- Insert a SECOND sentence after the first paragraph: "(architecturally:
  this is the **A1 PANEL** pattern -- see Genesis
  `architectural-patterns.md` §A1.)"
- After the existing mermaid figure (`fig-writer-reviewer-tester`),
  insert a verbatim **A1 PANEL definition box** (see §4 below).
- After the "anchored by the writer's reasoning" paragraph, append one
  sentence naming **PANEL-IN-ONE-CONTEXT** as the most common failure,
  and cross-linking the Ch14 entry (added by the Ch14 deep-dive).
- Add a single-line bounded-rounds reminder at the end of the section:
  "If the reviewer rejects twice on the same finding, change the
  approach -- decompose, add context, or escalate -- rather than
  re-dispatching the writer a third time at the same level
  (`ch14:216`)."

### Edit 2. §Pattern 2: Domain Teams (`ch12:72`)

- Keep the heading verbatim.
- After the opening paragraph, insert: "Structurally, Domain Teams is
  the same shape as Writer / Reviewer / Tester -- an **A1 PANEL** --
  with N varying by the number of concerns and each lens specialized
  by domain rather than by workflow stage. The synthesis step is
  performed by the orchestrator (the human, in PR #394) at the wave
  checkpoint, not by an N+1 agent."
- In the "Concrete Dispatch" subsection (`ch12:85`), add ONE sentence
  to the lead-in: "The dispatch itself is a **C3 THREAD SPAWN** over
  the **CHILD-THREAD SPAWN** primitive -- a fresh execution unit with
  its own context window, loaded with this prompt and these
  instruction files (see Ch09 for the primitive)."

### Edit 3. §Pattern 3: Audit / Execute / Validate (`ch12:131`)

- Keep heading verbatim.
- Append one sentence at end of the opening paragraph: "Architecturally
  this is an **A2 PIPELINE** whose audit stage is itself a **B1 FAN-OUT
  + SYNTHESIZER** -- multiple read-only audit children running in
  parallel, fanning in to a synthesis step (typically the human
  decision point, sometimes a synthesizer agent). The execute stage
  is then a series of C3 THREAD SPAWNs scoped per file group."
- After the "human decision...is the highest-leverage point" paragraph
  (`ch12:148`), insert a verbatim **B1 FAN-OUT + SYNTHESIZER
  definition box** (see §4 below).

### Edit 4. §Parallelization Strategies → §Wave-Based Parallelism (`ch12:175`)

- Status: cross-link only. Add ONE sentence: "Wave-Based Parallelism
  is the chapter's realization of Genesis's **A5 WAVE EXECUTION**
  pattern; the gate-between-waves discipline below is the same
  S4 VALIDATION DECORATOR Genesis describes."
- No definition box here -- A5 is owned by a different deep-dive (or
  by future work); a single named cross-link is sufficient.

### Edit 5. §Conflict Resolution → §Design Conflicts (`ch12:311-317`)

The current text has two issues the integration is allowed to fix:

1. The "12%" / "15-20%" / "above 20% / below 5%" thresholds read as
   measurements but are explicitly flagged as not validated. C9
   says state these as **calibration not measurement** and mirror
   the handbook's existing wording.
2. The handbook already has a tighter, more actionable wording at
   `ch14:216` ("After **two failed dispatches** for the same task,
   change the approach: decompose further, add context, or
   escalate. Don't loop at the same level.") That phrasing is
   the canonical bounded-rounds discipline; Ch12 should use it.

Edit: keep the "human-intervention frequency is itself a metric"
paragraph, but rewrite the threshold sentences as calibration and
adopt the `ch14:216` wording. Full revised paragraph in §4 below.

### Edit 6. §The Escalation Protocol (`ch12:335-352`)

- Keep the four-level table verbatim.
- L2 row: append to the Response cell -- "Re-dispatch with refined
  prompt, **bounded to two attempts** at the same level
  (`ch14:216`)."
- After the table, insert ONE sentence: "Bounded rounds is a
  calibration, not a measurement: at two failed dispatches for the
  same task, the right move is to change the level (decompose, add
  context, or escalate to L3) rather than spend a third dispatch on
  the same approach."

### Edit 7. §Session Management → §Session Isolation (`ch12:385`)

- Keep the prose verbatim.
- Append to the existing "feature, not a limitation" paragraph: "The
  runtime affordance underneath is the **CHILD-THREAD SPAWN**
  primitive: each agent session is a fresh execution unit with its
  own context window, returning a value (commits + plan-file updates)
  to the orchestrator. The isolation Ch09 describes as the primitive's
  KEY PROPERTY is exactly the property the wave model relies on."

### Edit 8. New diagram: A1 PANEL topology with bounded-rounds gate

Insert one new mermaid figure right after the verbatim A1 PANEL
definition box in §Pattern 1 (Edit 1). Renders the topology in the
shape Genesis uses, explicitly carrying the bounded-rounds counter
that aligns with the §Escalation Protocol L2 row.

### Edit 9. Cross-link audit (footer + inline)

- Add ONE footnote near the top of §Pattern 1 cross-linking Ch09
  §CHILD-THREAD SPAWN (per C1 Shape A: Genesis names appear as Ch09
  headers).
- Add ONE footnote in §Conflict Resolution cross-linking Ch14's
  upcoming **DISPATCH CONTAMINATION** entry (per C6 Shape C: this is
  the named anti-pattern Wave 1's `ValueError` slip-through is an
  instance of, even though the recovery prose stays in Ch12).

No other footnotes are added -- the chapter's existing footnote
discipline (`^ch12-coordination`, `^ch12-autonomy`) is preserved.

---

## 4. Full draft of changed sections

The verbatim Genesis definition boxes below carry the patterns by
their canonical names exactly as Genesis defines them (C8 voice
rule). Surrounding prose is in the handbook register.

---

### 4.1 §Pattern 1 (revised opening + definition box + diagram)

> ### Pattern 1: Writer / Reviewer / Tester
>
> The most common pattern separates code production from code
> validation. One agent writes the code. A second agent reviews it.
> A third writes or updates tests. Architecturally, this is the
> **A1 PANEL** pattern -- a topology of independent specialized
> lenses with a synthesis step that produces one decision.[^ch12-a1]
>
> [Existing mermaid figure `fig-writer-reviewer-tester` unchanged.]
>
> **A1 PANEL (multi-lens deliberation) -- definition (verbatim from
> Genesis `architectural-patterns.md` §A1):**
>
> > **WHEN:** A decision benefits from >=3 specialized lenses (security,
> > cost, UX, architecture, etc.). The lenses are independent; no
> > shared state during evaluation. The synthesis is itself a
> > decision, not a concatenation.
> >
> > **MECHANISM:** the parent (orchestrator) dispatches one
> > CHILD-THREAD per lens, each loading its own persona / instruction
> > set. Each child returns a finding. The parent runs a synthesis
> > pass that produces ONE verdict.
> >
> > **ANTI-PATTERNS:** PANEL-WITHOUT-SYNTHESIS (N reports instead of
> > one decision), PANEL-IN-ONE-CONTEXT (running all N lenses in a
> > single window -- the dominant failure mode for senior engineers
> > stepping into agent design), IMBALANCED PANEL (the synthesis
> > follows the majority without examining the dissent; the
> > dissenting lens is usually the highest-information signal).
>
> *(End definition box.)*
>
> This pattern maps directly to the human workflow of author,
> reviewer, and QA -- and for the same reason. The writer optimizes
> for correctness and completeness. The reviewer optimizes for
> catching what the writer missed. The tester optimizes for
> verifiable behavior. These are different cognitive tasks that
> benefit from different contexts.
>
> In practice, the reviewer agent receives the diff plus the original
> source, not the writer's full conversation history. This is
> deliberate. The reviewer should evaluate the output on its own
> merits, not be anchored by the writer's reasoning. If the writer
> had a good reason for a decision but the code doesn't reflect it,
> that is a signal, not an excuse. Running the reviewer in the
> writer's session is the **PANEL-IN-ONE-CONTEXT** failure: the
> reviewer inherits the writer's attention drift and stops being an
> independent lens. (See Ch14 for the full anti-pattern entry.)
>
> If the reviewer rejects twice on the same finding, change the
> approach -- decompose further, add context, or escalate -- rather
> than re-dispatching the writer a third time at the same level. This
> is the same bounded-rounds discipline used elsewhere in the book
> (`ch14:216`).
>
> [^ch12-a1]: The runtime affordance underneath every lens in an
> A1 PANEL is the **CHILD-THREAD SPAWN** primitive (Ch09): a fresh
> execution unit with its own context window, returning a value to
> the parent. C3 THREAD SPAWN is the design-level discipline of
> using one child per scoped lens; B1 FAN-OUT + SYNTHESIZER is the
> N-lens topology; A1 PANEL specializes B1 by requiring the N lenses
> be persona-specialized and the synthesis be itself a decision.

#### New diagram: A1 PANEL topology with bounded-rounds gate

```{mermaid}
%%| fig-cap: "A1 PANEL with bounded-rounds gate"
%%| fig-alt: "Flowchart showing the orchestrator dispatching three
%%|   parallel CHILD-THREAD SPAWNs (Writer lens, Reviewer lens, Tester
%%|   lens), each in its own isolated context window. All three
%%|   children return findings to a synthesis gate, which either emits
%%|   one verdict (the panel decision) or, on disagreement, increments
%%|   a bounded-rounds counter and re-dispatches. After two failed
%%|   rounds for the same finding, the flow exits to a human
%%|   checkpoint rather than dispatching a third time at the same
%%|   level."
%%| label: fig-a1-panel-bounded
flowchart TD
    O["Orchestrator"]
    O -->|"CHILD-THREAD SPAWN"| W["Writer lens<br/>(fresh context)"]
    O -->|"CHILD-THREAD SPAWN"| R["Reviewer lens<br/>(fresh context)"]
    O -->|"CHILD-THREAD SPAWN"| T["Tester lens<br/>(fresh context)"]
    W --> S{"Synthesis gate"}
    R --> S
    T --> S
    S -->|"Converged"| V["One verdict"]
    S -->|"Diverged<br/>(round &lt; 2)"| O
    S -->|"Diverged<br/>(round = 2)"| H["Escalate (L3)<br/>human decides"]
```

The bounded-rounds branch is the operational form of the discipline
in §Escalation Protocol below: at two failed dispatches for the same
task, change the level rather than the seat. Three round-trips at
the same level is a signal that the panel cannot resolve the
question on its own (`ch14:216`).

---

### 4.2 §Pattern 2: Domain Teams (revised opening + Concrete Dispatch lead-in)

> ### Pattern 2: Domain Teams
>
> For cross-cutting changes, organize agents by area of expertise
> rather than by workflow stage. Each team owns a concern and is
> responsible for all files related to that concern.
>
> Structurally, Domain Teams is the same shape as Writer / Reviewer
> / Tester -- an **A1 PANEL** -- with N varying by the number of
> concerns, each lens specialized by domain rather than by workflow
> stage, and the synthesis step performed by the orchestrator (the
> human, in the PR #394 case) at the wave checkpoint rather than by
> an N+1 synthesizer agent.
>
> [Existing Architecture / Domain table unchanged.]
>
> [Existing PR #394 paragraph unchanged.]
>
> [...]
>
> #### Concrete Dispatch: What It Actually Looks Like
>
> The Domain Teams pattern describes structure. Here is what a
> dispatch actually looks like in practice [...]. The dispatch
> itself is a **C3 THREAD SPAWN** over the **CHILD-THREAD SPAWN**
> primitive (Ch09): a fresh execution unit with its own context
> window, loaded with this prompt and these instruction files,
> stateless across spawns by construction.
>
> [Rest of subsection unchanged.]

---

### 4.3 §Pattern 3: Audit / Execute / Validate (revised opening + B1 box)

> ### Pattern 3: Audit / Execute / Validate
>
> For exploratory work where the scope is not fully known in
> advance, separate the agents that discover what needs to change
> from the agents that make the changes. Architecturally this is an
> **A2 PIPELINE** whose audit stage is itself a **B1 FAN-OUT +
> SYNTHESIZER** -- multiple read-only audit children running in
> parallel, fanning in to a synthesis step (typically the human
> decision point, sometimes a synthesizer agent). The execute stage
> is then a sequence of C3 THREAD SPAWNs scoped per file group; the
> validate stage is a B1 fan-out of read-only validators.
>
> [Existing mermaid figure `fig-audit-execute-validate` unchanged.]
>
> The critical property of this pattern is the separation between
> read-only and read-write operations. [...unchanged...]
>
> The human decision between audit and execution is the
> highest-leverage point in the entire process. [...unchanged...]
>
> **B1 FAN-OUT + SYNTHESIZER -- definition (verbatim from Genesis
> `design-patterns.md` §B1):**
>
> > **WHEN:** >=3 independent lenses with no shared state, where
> > each lens benefits from a fresh context window.
> >
> > **MECHANISM:** parent spawns one CHILD-THREAD per lens (each
> > loading its own PERSONA PRELOAD). Each child returns a finding.
> > Parent runs a synthesis pass (often loading an arbitrator
> > persona) that produces ONE verdict.
> >
> > **ANTI-PATTERN:** FAN-OUT-IN-ONE-CONTEXT -- running all N lenses
> > sequentially inside a single window. Each lens contaminates the
> > next; later lenses inherit attention drift from earlier ones.
>
> *(End definition box.)*
>
> A1 PANEL is B1 specialized for decision-making: B1 names the
> topology, A1 adds the requirement that the N children be
> persona-specialized lenses and the synthesis be itself a decision.
> The audit stage of Audit / Execute / Validate is a B1 that may or
> may not also be an A1, depending on whether the audit children are
> distinct *personas* (architecture, security, UX) or instances of
> the same audit prompt sharded across files.

---

### 4.4 §Pattern 2/Concrete Dispatch -- C3 THREAD SPAWN definition box

(Inserted at the very end of the Concrete Dispatch subsection,
right before the wave timeline section. One paragraph plus the
verbatim box.)

> The dispatch above is one realization of the **C3 THREAD SPAWN**
> design pattern. The same shape underlies every example in this
> chapter -- one writer dispatch, one reviewer dispatch, one
> migration dispatch, one validator dispatch.
>
> **C3 THREAD SPAWN -- definition (verbatim from Genesis
> `design-patterns.md` §C3):**
>
> > **WHEN:** a unit of work benefits from a fresh context window --
> > isolation from siblings, full attention on its own scope.
> >
> > **MECHANISM:** parent invokes the harness's spawn affordance
> > with a task description and (optionally) a persona / module to
> > load at startup. Child runs, returns a value, exits.
> >
> > **ANTI-PATTERN:** UNBOUNDED SPAWN -- letting any thread spawn
> > any depth of descendants. Couple with SUPERVISOR (B3) to bound
> > the tree.
>
> *(End definition box.)*
>
> The wave model in the next section is exactly the supervisor that
> bounds the spawn tree: a wave is a finite set of C3 spawns whose
> depth is one and whose breadth is fixed before dispatch.

---

### 4.5 §Conflict Resolution → §Design Conflicts (rewritten threshold paragraph)

Replace the existing paragraph at `ch12:317` (everything after the
"3 human interventions were needed across ~25 agent dispatches"
sentence) with:

> The frequency of design conflicts is itself a metric. In the
> PR #394 execution ([case study](../case-study-apm-overhaul.qmd)),
> 3 human interventions were needed across ~25 agent dispatches.
> None were design conflicts between agents; all were judgment calls
> that the plan could not automate. We use that ratio as a
> **calibration**, not a measurement: a well-planned execution on a
> non-trivial change should expect *some* L3+ interventions, not
> zero. An intervention rate that is implausibly low warrants the
> same scrutiny as one that is implausibly high -- the work may be
> too simple for multi-agent orchestration, or review may not be
> happening.
>
> Inside any single conflict, the bounded-rounds discipline applies:
> after **two failed dispatches** for the same task, change the
> approach -- decompose further, add context, or escalate -- rather
> than spending a third dispatch at the same level (`ch14:216`).
> Three rounds at the same level is the signal that the failure is
> categorical, not random; a third dispatch will fail the same way
> the first two did.

---

### 4.6 §Escalation Protocol (revised L2 row + appended sentence)

Keep the four-level table; revise the L2 row's Response cell from:

> Re-dispatch with refined prompt

to:

> Re-dispatch with refined prompt, **bounded to two attempts** at
> the same level (`ch14:216`).

Append one sentence after the table:

> Bounded rounds is a calibration, not a measurement: at two failed
> dispatches for the same task, the right move is to change the
> level (decompose, add context, or escalate to L3) rather than
> spend a third dispatch on the same approach. The intent is to
> catch categorical failures early -- if the second dispatch fails
> the way the first did, the third almost certainly will too.

---

### 4.7 §Session Isolation (one appended paragraph)

Append after the existing "feature, not a limitation" paragraph
(`ch12:387`):

> The runtime affordance underneath is the **CHILD-THREAD SPAWN**
> primitive (Ch09): each agent session is a fresh execution unit
> with its own context window, returning a value -- commits, plan
> updates, escalation messages -- to the orchestrator. The isolation
> Ch09 describes as the primitive's KEY PROPERTY ("anything not
> loaded as text into the child thread does not exist for that
> thread") is exactly the property the wave model relies on for the
> "shared filesystem, not shared sessions" rule above.

---

## 5. Cross-link audit

Two cross-links land outside this chapter; both are owned by other
deep-dives but are placed here so they are tracked.

### 5.1 Ch09 §CHILD-THREAD SPAWN reference

- Inserted in: §Pattern 1 footnote `^ch12-a1`; §Pattern 2 Concrete
  Dispatch lead-in; §Session Isolation appended paragraph.
- Form: "(Ch09)" inline; full chapter cross-link in the footnote.
- Owner: Ch09 deep-dive (per C1 Shape A) is responsible for the
  destination header. If Ch09 lands its CHILD-THREAD SPAWN section
  under a different name, this chapter's three references update in
  one pass.

### 5.2 Ch14 anti-pattern cross-links

This chapter mentions FIVE Genesis anti-patterns by name:

| Name (verbatim) | First mention in Ch12 | Owns full entry |
|---|---|---|
| PANEL-IN-ONE-CONTEXT | §Pattern 1 (after "anchored by the writer's reasoning") | Ch14 (per C5/C6 Shape C) |
| PANEL-WITHOUT-SYNTHESIS | A1 PANEL definition box | Ch14 |
| IMBALANCED PANEL | A1 PANEL definition box | Ch14 |
| FAN-OUT-IN-ONE-CONTEXT | B1 FAN-OUT + SYNTHESIZER definition box | Ch14 |
| UNBOUNDED SPAWN | C3 THREAD SPAWN definition box | Ch14 |

Each name appears here only once outside its definition box, and
each is followed by "(see Ch14)" or appears inside a verbatim Genesis
box that itself names the anti-pattern. No new Ch12 prose duplicates
Ch14's upcoming entries.

The PR #394 Wave 1 `ValueError` slip-through is now a worked
instance of **DISPATCH CONTAMINATION** (per C6 Shape C). The
recovery walkthrough at `ch12:288-309` stays in Ch12 as the
detailed worked example; Ch14's DISPATCH CONTAMINATION entry will
back-reference it. Add one inline cross-link in the
"Diagnosis" paragraph at `ch12:298`:

> The orchestrator reviewed the failures and identified the root
> cause in under two minutes: the Wave 1 dispatch prompt loaded the
> logging context but not the error-handling context. The agent had
> no visibility into the pattern change. (This is the named
> **DISPATCH CONTAMINATION** failure -- see Ch14.)

### 5.3 Forward / lateral cross-links also touched

- §Wave-Based Parallelism gains a one-sentence cross-link to
  **A5 WAVE EXECUTION** (Genesis architectural-patterns §A5). No
  definition box; A5 is owned by other deep-dives.
- §Audit / Execute / Validate gains a one-sentence cross-link to
  **A2 PIPELINE** (Genesis architectural-patterns §A2). Same
  treatment -- name only, no box.

These two are deliberate: the chapter cannot absorb every Genesis
pattern it touches; A1, B1, and C3 are the three that map directly
to Ch12's Specialization Patterns section and earn full definition
boxes, while A2 and A5 are named and cross-linked only.

---

## 6. Impact summary

**What changes (concrete diff scope):**

- Three verbatim definition boxes inserted (A1, B1, C3).
- One new mermaid diagram (`fig-a1-panel-bounded`).
- One footnote added (`^ch12-a1`).
- Six second-sentences inserted (one per pattern section + Audit/Execute/
  Validate, Wave-Based Parallelism, Concrete Dispatch, Session Isolation).
- Five Genesis anti-pattern names introduced inline (each cross-linked
  to Ch14, no new prose duplicates Ch14's upcoming entries).
- One paragraph at `ch12:317` rewritten to align with the handbook's
  existing "two failed dispatches" wording (`ch14:216`) and to frame
  the intervention rate as **calibration, not measurement** (C9).
- One half-sentence appended to the L2 row of the escalation protocol
  table; one sentence appended below the table.

**What does NOT change:**

- No section headers renamed. Writer/Reviewer/Tester, Domain Teams,
  and Audit/Execute/Validate stay verbatim (C7 Shape C).
- No existing prose deleted except the rewritten paragraph at
  `ch12:317`, and that rewrite preserves the case-study facts
  (3 interventions, ~25 dispatches) -- only the framing changes.
- No existing figure modified; the new figure is additive.
- No footnote renumbered; `^ch12-coordination` and `^ch12-autonomy`
  keep their positions.

**Estimated word-count delta:** ~+1,100 words against ~5,300 in the
current chapter (~21% growth), almost all of it in the three
verbatim definition boxes and the rewritten threshold paragraph.
Within the +20% growth tolerance the synthesis discusses.

**Decisions consumed:**

- **C7 Shape C** -- handbook headers preserved; second-sentence
  bridge to Genesis names. Applied to §Pattern 1, §Pattern 2,
  §Pattern 3.
- **C8 voice rule** -- A1, B1, C3 named ALL-CAPS verbatim; one
  verbatim definition box per pattern; surrounding prose in handbook
  voice; no buzzword translation.
- **C9** -- "two failed dispatches" wording adopted from `ch14:216`;
  framed as calibration (mirrors `ch12:317`'s prior framing of
  thresholds as "calibration points").
- **C1 Shape A** -- CHILD-THREAD SPAWN named as the underlying
  primitive; A1/B1/C3 introduced as patterns built on it. Three
  Ch09 cross-links inserted.

**Decisions NOT consumed:**

- C5 (Ch14 absorption scope), C6 (BUNDLE LEAKAGE / DISPATCH
  CONTAMINATION) are referenced but their full entries land in the
  Ch14 deep-dive. This chapter only cross-links into them.
- C3 (Ch15 governance vocabulary) and C4 (Memory split) do not
  surface in Ch12.
- The `ch15-squad` footnote forward-date issue is unrelated.

**Downstream readiness:**

- The Ch14 deep-dive can now assume Ch12 names PANEL-IN-ONE-CONTEXT,
  PANEL-WITHOUT-SYNTHESIZED, IMBALANCED PANEL, FAN-OUT-IN-ONE-CONTEXT,
  UNBOUNDED SPAWN, and DISPATCH CONTAMINATION at first mention.
  Ch14 owns the full entries; Ch12 owns the worked examples.
- The Ch09 deep-dive (C1 Shape A) can rely on Ch12 referencing
  CHILD-THREAD SPAWN by exactly that name in three places.
- The doc-site Resources/External-corpus page (B2.1) can deep-link
  to the three definition boxes for readers arriving from the
  Genesis side.

**Risks / open items:**

- If the Ch09 deep-dive lands the primitive under a different header
  (e.g., "subagent thread" instead of "CHILD-THREAD SPAWN"), this
  chapter's three Ch09 cross-links update in one pass. No structural
  rework.
- If the Ch14 deep-dive narrows the absorption scope (C5 reversal),
  some inline anti-pattern names here may need to be footnoted
  rather than cross-linked. Single-pass fix.
- The threshold-paragraph rewrite at `ch12:317` is the most
  substantive prose change. The author MAY prefer to keep the
  numeric thresholds and only append the bounded-rounds wording. If
  so, the rewrite is reduced to a one-paragraph append; the
  calibration framing at `ch14:216` still imports cleanly.

---
