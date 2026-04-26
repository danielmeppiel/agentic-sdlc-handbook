# Ch14 — Integration draft (partial anti-pattern absorption + R1-R4 refactor verbs)
# (with Ch15:23 tail extension: substrate-fields adoption)

> Scope: implements decisions C5 (partial absorption), C6 (Shape C — split
> BUNDLE LEAKAGE + DISPATCH CONTAMINATION as one war-storied entry, others
> as footnotes), C3 (Ch15:23 adopts substrate-field vocabulary), and C8
> (named patterns ALL-CAPS verbatim).
>
> Sources: `WIP/round-1/AUTHOR-DECISIONS.md`,
> `WIP/round-1/SYNTHESIS.md` §3 + §4 (C3, C5, C6),
> `WIP/round-1/cto-proxy.md` §4.1,
> `apm-handbook/handbook/ch14-anti-patterns-and-failure-modes.qmd`,
> `apm-handbook/handbook/ch15-what-comes-next.qmd:23`,
> Genesis assets: `architectural-patterns.md` (A5, A10),
> `composition-substrate.md` ("Anti-patterns flagged at this step"),
> `refactor-patterns.md` (R1-R4),
> `runtime-affordances/per-trigger-surface/gh-aw.md`.

---

## 1. Integration thesis (for Ch14)

Ch14 today is a 19-entry catalogue of run-time failure modes mapped to the
five PROSE constraints. Genesis ships a parallel-but-disjoint catalogue of
source-time and packaging anti-patterns plus four refactor verbs (R1 SPLIT,
R2 FUSE, R3 EXTRACT, R4 INLINE) that Ch14 currently has no equivalent for.
The handbook's reader gets symptoms and recovery; Genesis's reader gets the
restructuring move that fixes the underlying graph.

Partial absorption (C5) closes the gap that Ch14 is read as the complete
anti-pattern reference for AI-native development when in fact it omits the
governance-tier failures (TOKEN-LAUNDERING, INNER-LOOP MISCAST AS OUTER)
and the packaging failure that produces silent context contamination
(BUNDLE LEAKAGE -> DISPATCH CONTAMINATION). It also names the moves
(R1-R4) the recovery playbook hand-waves through under "Decompose."

Genesis remains the canonical reference for the source-time / packaging
catalogue; Ch14 absorbs the practitioner-grade entries and footnote-points
to Genesis for the rest. Ch14 grows ~30 percent, not ~100 percent.

---

## 2. Absorption table

| Genesis entry | Ch14 treatment |
|---|---|
| R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE (refactor verbs) | Full absorb as new "The Refactor Moves" section between Recovery Playbook and Failure Mode Decision Tree. Genesis-verbatim definitions in inline boxes; handbook-register prose around them. |
| A5 WAVE EXECUTION anti-patterns (WAVE-WITHOUT-GATE, EVERY-TASK-IS-A-WAVE) | Full absorb as new entry in Execution Anti-Patterns section. |
| TOKEN-LAUNDERING (A10 anti-pattern) | Full absorb as new entry in Team-Level / Governance section. |
| INNER-LOOP MISCAST AS OUTER (A10 anti-pattern) | Full absorb as new entry in Team-Level / Governance section. |
| BUNDLE LEAKAGE + DISPATCH CONTAMINATION | Full absorb as ONE war-storied entry in Session and Resource Failure Modes (sits next to #19 Prompt Injection via Dependencies; same family — untrusted text reaching the model). |
| Trust-Fall <-> VERIFY-WITH-LLM-ONLY / PLAN-AND-PRAY | Cross-link insertion in existing "The Trust Fall" entry pointing to Genesis design-patterns. |
| PHANTOM DEPENDENCY, DUPLICATED LEAF, HIDDEN EXTERNAL, UNPINNED CRITICAL DEP | Footnote-reference only (Round 2 evidence pending per C6 Shape C). |
| Source-time / packaging detail (full set) | Genesis remains canonical authority; Ch14 carries an authority footnote at end of Taxonomy table. |

---

## 3. Section-by-section edit plan for Ch14

1. **Taxonomy table (lines 17-41).** Append four rows: #20 BUNDLE LEAKAGE,
   #21 WAVE-WITHOUT-GATE, #22 TOKEN-LAUNDERING, #23 INNER-LOOP MISCAST AS
   OUTER. Update opening prose ("19 distinct ways" -> "23 distinct ways").
   Add an authority footnote on the table caption pointing to Genesis as
   canonical reference for source-time / packaging anti-patterns not
   absorbed here.

2. **The Trust Fall entry (lines 127-133).** Insert a cross-link sentence
   at end: "The Genesis corpus names the same failure shape under two
   handles: PLAN-AND-PRAY (the agent claims it will do the thing) and
   VERIFY-WITH-LLM-ONLY (a second agent vouches for the first without
   running tests). Same disease, three names; the cure is the same — run
   the test suite, read the diff."

3. **Execution Anti-Patterns section (after line 154).** New entry:
   WAVE-WITHOUT-GATE (with cousin EVERY-TASK-IS-A-WAVE). Treats wave
   execution explicitly as the pattern Ch14 already operates inside (#9
   Skipping Checkpoints, #18 Cross-Wave Merge Conflicts) but never named.

4. **Session and Resource Failure Modes section (after line 294, between
   #19 Prompt Injection and the Silent Failure callout).** New entry:
   BUNDLE LEAKAGE + DISPATCH CONTAMINATION. War-storied via the APM
   scanner.

5. **New section: "The Refactor Moves" (insert between line 396 — end of
   Recovery Playbook narrative — and line 397 — Worked Example header).**
   R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE. Frames these as the
   restructuring vocabulary the Recovery Playbook's step 4 ("Decompose")
   delegates to. Each move gets a Genesis-verbatim definition box and a
   handbook-register paragraph of when-to-fire.

6. **Team-Level Anti-Patterns (lines 360-376).** Append two entries
   between "Cargo-culting complexity" and "Abandoned governance":
   TOKEN-LAUNDERING and INNER-LOOP MISCAST AS OUTER. Both belong here
   because both are organizational decisions about credential placement
   and substrate choice, not code-level patterns.

7. **Footnote block at chapter end.** Add a footnote section listing four
   referenced-but-deferred Genesis anti-patterns (PHANTOM DEPENDENCY,
   DUPLICATED LEAF, HIDDEN EXTERNAL, UNPINNED CRITICAL DEP) with a
   one-line description and a Genesis citation, marked "Round 2: pending
   evidence."

---

## 4. Full draft of new + changed Ch14 sections

### 4.1 Taxonomy table — appended rows

```
| 20 | BUNDLE LEAKAGE   | Safety Boundaries | Maintainer-only files (eval prompts, dev fixtures) ship inside the user-facing distribution and get pulled into agent context as if they were real instructions |
| 21 | WAVE-WITHOUT-GATE | Orchestrated Composition | Topologically sorted task DAG executed without a check between waves; drift compounds silently and surfaces with no localizable cause |
| 22 | TOKEN-LAUNDERING  | Safety Boundaries | The agent step holds a write token for its declared externalization target "because the post-stage is too fiddly"; the substrate's capability gate is bypassed by design |
| 23 | INNER-LOOP MISCAST AS OUTER | Reduced Scope | A single-developer laptop task is promoted to a governed, event-triggered workflow because "governance sounds good"; trigger-surface lock-in paid for properties that are never needed |
```

Caption footnote (new):

> [^ch14-genesis-source-time]: This taxonomy covers run-time and
> session-level failures the practitioner encounters during an
> agent-augmented session. The complementary catalogue of source-time
> and packaging failures — module-graph anti-patterns flagged when
> primitives are authored, distributed, or composed — is maintained in
> the Genesis corpus (see `architectural-patterns.md`,
> `composition-substrate.md`, `design-patterns.md`). Where Ch14 names
> a Genesis pattern verbatim (e.g. BUNDLE LEAKAGE, TOKEN-LAUNDERING,
> WAVE-WITHOUT-GATE, INNER-LOOP MISCAST AS OUTER, R1-R4 refactor
> moves), Genesis remains canonical for the long form.

### 4.2 The Trust Fall — cross-link insertion

The existing entry (lines 127-133) ends with "One line of diff output is
worth a thousand words of agent narrative." Insert one paragraph after:

> The Genesis corpus catalogues two source-time variants of the same
> failure: PLAN-AND-PRAY (the agent declares an intention as if the
> intention were the artifact) and VERIFY-WITH-LLM-ONLY (a second agent
> vouches for the first without running the tests or reading the diff).
> Three names, one disease, one cure. The cure does not change with the
> name: run the suite, read the diff, treat agent narrative as a
> hypothesis until ground truth confirms it.

### 4.3 New entry: WAVE-WITHOUT-GATE

(Place in Execution Anti-Patterns section, after "Not Fixing the
Primitives" and before the section break at line 155.)

```
### Wave-Without-Gate

The team adopts the wave execution pattern from Chapter 12 — topologically
sort the task DAG, group independent tasks at the same depth into a
wave — and ships waves back-to-back without a check between them. Wave 1
finishes; wave 2 dispatches against wave 1's output without anyone asking
"do wave 1's outputs satisfy the assumptions wave 2 was planned under?"
By wave 4, the integration test fails and the cause cannot be localized:
each wave passed its own tests, the regression lives in the join.

This is the same disease as #9 Skipping Checkpoints, named at the
architectural level. Genesis records it as the canonical anti-pattern
of the A5 WAVE EXECUTION pattern: WAVE-WITHOUT-GATE -- "topologically
sorting tasks but not gating between waves; drift compounds silently;
failure surfaces at the end with no localizable cause."[^ch14-a5]

The dual is EVERY-TASK-IS-A-WAVE: every task gets its own gate; the
gates degenerate into noise; the supervisor pays orchestration cost for
zero parallelism. The right grain is one gate per WAVE, not per task and
not per release.

**Fix.** Run a check between waves whose pass criterion is concrete: do
wave N's outputs satisfy the inputs wave N+1 was planned against? Re-read
files modified by wave N before assembling wave N+1's context. On gate
failure, re-plan from the failed wave, not from the start of the run.

[^ch14-a5]: Genesis, `architectural-patterns.md`, A5 WAVE EXECUTION,
ANTI-PATTERNS section.
```

### 4.4 New entry: BUNDLE LEAKAGE + DISPATCH CONTAMINATION

(Place in Session and Resource Failure Modes, after #19 Prompt Injection
via Dependencies and before the "File Presence Is Execution" callout at
line 296. This is the war-storied entry per C6 Shape C.)

```
### Bundle Leakage and Dispatch Contamination

::: {tbl-colwidths="[20,80]"}

| | |
|---|---|
| **Symptom** | An agent in a team's pipeline gives an unexpectedly bizarre answer to a routine request — the response reads like it is solving a different problem than the one asked. The team initially flags it as a model regression. The actual cause is that the harness's file picker matched against a maintainer-scope file (an evaluation scenario, a dev fixture, a contributor README) that ships INSIDE the user-facing module's distribution and pulled it into the active context. The session is now reasoning against the wrong text. |
| **Root cause** | Two scopes — ship-time and run-time — are not the same scope. A module that publishes correctly may still publish too much. Maintainer-only files (evaluation prompts especially — they LOOK LIKE real user requests by construction) inside the distribution boundary get matched by over-eager harness loaders, asset-discovery routines, or LLM-driven file pickers. Genesis names this BUNDLE LEAKAGE; the failure shape that hits the practitioner is its consequence: DISPATCH CONTAMINATION. The other shape is PAYLOAD BLOAT — distribution cost without distribution benefit; cosmetic, not dangerous on its own. |
| **Constraint violated** | Safety Boundaries (the same family as #19 Prompt Injection via Dependencies — both are untrusted-or-misaddressed text reaching the model). |
| **Severity** | High. Hallucination amplifier, not just an aesthetic issue.[^ch14-bundle-leakage] |
| **Prevention** | Maintain a strict separation between ship-time scope and run-time scope. Maintainer-only assets live OUTSIDE the user-facing module entrypoint AND outside any directory the package manager auto-publishes. The APM convention is a contributor-only directory (e.g. `dev/skills/<module>-<role>/`) whose distribution boundary excludes it. NOTE: APM's local-content scanner treats `.apm/skills/` as a publishable source root regardless of devDep marker; dev-only primitives must live OUTSIDE `.apm/`. |
| **Recovery** | Identify the leaking file by reading the contaminated session's tool-call log — which files did the loader actually read? Move those files outside the distribution boundary. Re-publish. Audit other modules in the same package for symmetric leaks. |

:::

This is the symmetric counterpart of PHANTOM DEPENDENCY (the
referenced-but-not-bundled failure, where a module body cites a peer the
distribution does not include). Both are SHIP-TIME / RUN-TIME scope
violations; both are flagged by the APM publish scanner as part of
the lockfile validation pass. PHANTOM DEPENDENCY and three other related
packaging failures are tracked in the Genesis corpus with Round 2
evidence pending.[^ch14-phantom-and-friends]

[^ch14-bundle-leakage]: Genesis, `composition-substrate.md`,
"Anti-patterns flagged at this step", BUNDLE LEAKAGE entry.

[^ch14-phantom-and-friends]: PHANTOM DEPENDENCY, DUPLICATED LEAF,
HIDDEN EXTERNAL, UNPINNED CRITICAL DEP — operational packaging failures
documented in `composition-substrate.md`. Round 2 evidence pending; treat
the Genesis entries as canonical.
```

### 4.5 New section: The Refactor Moves

(Insert between end of Recovery Playbook narrative at line 396 and the
"Worked Example: Recovering from the 'Almost Done' Trap" header at line
397. This is the largest absorption — R1-R4 promote the recovery
playbook's hand-waved "Decompose" step into a named vocabulary.)

```
---

## The Refactor Moves

The Recovery Playbook's step 4 — "Decompose" — is the most common move
and the least specified. Decompose how, exactly? Genesis names the four
refactor verbs that operate on the module graph at SOURCE TIME — the
shapes of what to do when you have a primitive that is doing too many
jobs, or two primitives that should be one, or content that has grown
into a primitive but has not been promoted yet. Apply them BEFORE
re-picking a Tier-2 or Tier-3 architectural shape. Restructuring the
graph often dissolves the need for a more elaborate runtime topology.

The verbs come in two pairs of duals: R1 SPLIT and R2 FUSE govern
module count; R3 EXTRACT and R4 INLINE govern primitive granularity.

### R1 SPLIT — decomposition

::: {.callout-note}
## R1 SPLIT (Genesis-verbatim definition)
A module has grown to do more than one job, OR the dispatcher cannot
route cleanly because the module's signature names two capabilities.
Triggers: description conjunction (`...and...` between trigger
noun-phrases); fragment callers (real call sites need a strict subset
of the body); body over budget; multi-lens body; divergent change
cadence.[^ch14-r1]
:::

When a primitive's frontmatter description reads "format reviews and
draft release notes," the seam is already there in language. Split
along it: one module per trigger noun-phrase, one lens per module. The
original entrypoint either becomes a thin orchestrator that dispatches
to the new modules, or it goes away. Do not leave both; the dispatcher
will guess.

The compounding gain: a split skill becomes individually invocable; its
body runs in a fresh context window instead of competing for tokens
with the parent's session. Splits with this dual payoff — separation of
concerns AND context isolation — are the highest-priority candidates.

The trap is the inverse, PREMATURE SPLIT: splitting a 50-line
single-trigger skill into five skills is the agentic analogue of
writing 10 functions for a 50-line program. Overhead exceeds benefit;
the dispatcher pays the cost forever.

### R2 FUSE — consolidation

::: {.callout-note}
## R2 FUSE (Genesis-verbatim definition)
Two or more sibling modules whose descriptions overlap or whose bodies
are short and always co-invoked. Triggers: dispatch collision (trigger
nouns / verbs overlap; the dispatcher guesses, misses go silent);
lockstep co-invocation; tiny siblings sharing one lens.[^ch14-r2]
:::

R2 is R1's dual. Two siblings that always co-invoke, or whose
descriptions trigger each other's dispatch — merge them, then sharpen
the description on the merged module. Confirm the merge does not
re-trigger an R1 signal (no new conjunction, no multi-lens body); if
it does, the symptom is a wrong original split, not a missing fusion.

The trap is FORCED FUSION: merging two modules that genuinely serve
different lenses just to reduce dispatcher entries. The dispatcher
collision was the symptom; the disease was a too-broad description on
one of them. Sharpen the description first.

### R3 EXTRACT — promote to module

::: {.callout-note}
## R3 EXTRACT (Genesis-verbatim definition)
Content lives INLINE inside a module body that should be its own
primitive (a persona, a rule file, a sibling skill, an asset).
Triggers: duplicated inline content (the same paragraph in N modules);
wrong-lens inline (a skill body inlines a persona); reuse pressure;
maintainer-only content shaped like a real primitive.[^ch14-r3]
:::

R3 is the move behind step 5 of the Recovery Playbook ("Fix the
primitive"). When the same correction has to be made in three modules,
extract it to one. The cleanup step Genesis is strict about: if the
extracted module crosses a project boundary, declare the dependency at
the dependent module's distribution surface — manifest entry, body
reference, tool-call probe at the use-site. Skip this step and the
module ships with a PHANTOM DEPENDENCY, which is a SHIP-TIME / RUN-TIME
scope violation in the symmetric direction to BUNDLE LEAKAGE (#20).

The trap is PROMOTION-WITHOUT-NEED: extracting content whose only
caller is and will remain the original module. Wait for the rule of
three to fire before paying the extraction cost.

### R4 INLINE — collapse a thin proxy

::: {.callout-note}
## R4 INLINE (Genesis-verbatim definition)
A primitive exists only as a thin proxy that always loads exactly one
other primitive's content. Triggers: single-caller / single-content;
dead variation (extracted in anticipation of N variants; only one
ever existed).[^ch14-r4]
:::

R4 is R3's dual. A primitive whose body is exclusively a reference to
one other primitive, with one caller, is a load step and a maintenance
file paid for nothing. Inline it back. The exception: if the proxy
exists for portability across harnesses or for a planned variant
fan-out, leave it (RUSHED INLINE).

### How the moves relate

```{mermaid}
%%| fig-cap: "The four refactor moves and their dual relationships."
%%| fig-alt: "Two horizontal pairs. Top pair: R1 SPLIT and R2 FUSE labeled as duals governing module count. Bottom pair: R3 EXTRACT and R4 INLINE labeled as duals governing primitive granularity. R1 SPLIT lists triggers cohesion / dispatch / context-budget. R2 FUSE lists triggers collision / lockstep / tiny-siblings. R3 EXTRACT lists triggers duplication / wrong-lens / reuse pressure. R4 INLINE lists triggers single-caller proxy / dead variation."
flowchart LR
  subgraph PAIR1["module count"]
    direction LR
    R1[R1 SPLIT<br/>cohesion<br/>dispatch<br/>context-budget] <-- duals --> R2[R2 FUSE<br/>collision<br/>lockstep<br/>tiny-siblings]
  end
  subgraph PAIR2["primitive granularity"]
    direction LR
    R3[R3 EXTRACT<br/>duplication<br/>wrong-lens<br/>reuse pressure] <-- duals --> R4[R4 INLINE<br/>single-caller proxy<br/>dead variation]
  end
```

Run R-pattern triggers across the existing module graph BEFORE
re-picking a Tier-3 architectural pattern (see Chapter 13). A common
trap: skipping the refactor pass and reaching for a more elaborate
runtime topology when the real fix was an R1 SPLIT of an over-broad
existing module.

[^ch14-r1]: Genesis, `refactor-patterns.md`, R1 SPLIT.
[^ch14-r2]: Genesis, `refactor-patterns.md`, R2 FUSE.
[^ch14-r3]: Genesis, `refactor-patterns.md`, R3 EXTRACT.
[^ch14-r4]: Genesis, `refactor-patterns.md`, R4 INLINE.
```

### 4.6 Two new Team-Level entries: TOKEN-LAUNDERING, INNER-LOOP MISCAST AS OUTER

(Append to the Team-Level Anti-Patterns section between "Cargo-culting
complexity" and "Abandoned governance" at lines 370-372.)

```
**Token-Laundering.** A team builds an event-triggered agent workflow
that posts comments on pull requests. The "correct" architecture
buffers the agent's outputs, runs them through a deterministic
post-stage, and only then writes to the system of record — the agent
itself never holds the write token. The team finds the post-stage
"too fiddly" and grants the agent step a write token directly. The
externalization works on the happy path. It also works on every
unhappy path the agent reaches, including ones the team did not
anticipate. The substrate's capability gate is the WHOLE POINT of a
governed workflow; bypassing it reduces the design to plain
event-driven automation with extra ceremony and a strictly worse
threat model. The cure is to either extend the post-stage to cover
the desired write, or re-classify the work as in-session
(non-governed) automation.[^ch14-token-laundering]

**Inner-Loop Miscast As Outer.** The inverse failure: a team promotes
a single-developer laptop task to a governed, event-triggered
pipeline because "governance sounds good." The work didn't need
event-triggering, didn't need an audit trail, didn't need
sandboxing — it needed a developer to run it locally. The cost is
trigger-surface lock-in: the workflow is now portable only across
substrates that supply the same governance fields. Pay this cost only
when the governance properties (event-triggered execution, sandboxed
runtime, capability-gated externalization, durable audit trail) are
actually needed.[^ch14-inner-loop-miscast]

[^ch14-token-laundering]: Genesis, `architectural-patterns.md`,
A10 GOVERNED OUTER LOOP, ANTI-PATTERNS / TOKEN-LAUNDERING.
[^ch14-inner-loop-miscast]: Genesis, `architectural-patterns.md`,
A10 GOVERNED OUTER LOOP, ANTI-PATTERNS / INNER-LOOP MISCAST AS OUTER.
See also Ch15:23 (the substrate fields these failures violate are
the same fields the predicted governance category is built from).
```

### 4.7 Footnote-reference list (Round 2 deferred)

(Already wired via `[^ch14-phantom-and-friends]` in 4.4. Final form, to
be placed in the chapter's footnote block:)

```
[^ch14-phantom-and-friends]: Four packaging anti-patterns are tracked
in the Genesis corpus and not yet absorbed into Ch14, pending Round 2
operational evidence:

- PHANTOM DEPENDENCY -- a module body cites a peer the distribution
  does not include. The runtime "just happens" to resolve it, until it
  doesn't. Symmetric counterpart of BUNDLE LEAKAGE (#20). See
  Genesis, `composition-substrate.md`, HIDDEN EXTERNAL.
- DUPLICATED LEAF -- the same content inlined in N primitives where
  one EXTERNAL MODULE would do; cured by R3 EXTRACT.
- HIDDEN EXTERNAL -- a primitive depends on content not declared as a
  dependency edge; the runtime loads it by accident.
- UNPINNED CRITICAL DEP -- an external module whose drift would
  silently change behavior, with no pin.

Source: `composition-substrate.md` "Anti-patterns flagged at this step".
Each will be promoted to a full Ch14 entry once a war-story-grade
incident is on file.
```

---

## 5. Ch15:23 tail extension (separate output section)

### 5.1 Existing prediction (verbatim, `ch15:23`)

> **Agent governance becomes a first-class engineering discipline.**
> Today, governance of agent output is handled through existing
> processes: pull requests, CI, manual approval. This works at current
> volumes. As output scales and multi-agent orchestration becomes
> common, dedicated governance infrastructure will emerge: audit trails
> for agent decisions, policy engines that enforce constraints at
> execution time rather than review time, cost controls that manage
> token spend across teams. The governance frameworks in Chapter 5
> anticipate this, but the tooling barely exists. Within three years,
> agent governance platforms will be a category — the way CI/CD became
> a category over the past decade.

### 5.2 Rewritten prediction (decision C3 — Adopt)

> **Agent governance becomes a first-class engineering discipline.**
> Today, governance of agent output is handled through existing
> processes: pull requests, CI, manual approval. This works at current
> volumes. As output scales and multi-agent orchestration becomes
> common, the category will consolidate around three substrate
> properties — properties of the runtime the agent runs inside, not of
> the review pass after it has run. The first is SANDBOXING: the trigger
> surface that fires the agent run controls its network and filesystem
> reach. The second is CAPABILITY_GATING: the agent never holds the
> write tokens for its declared externalization targets; a deterministic
> post-stage mediates every write to a system of record. The third is
> AUDIT_SURFACE: the entire run — what fired it, what ran, what was
> written — survives the session in durable form an auditor can
> reconstruct after the fact. These are not aspirational properties;
> the cheapest existing-today realization is GitHub Agentic Workflows
> running on GitHub Actions runners, where the trigger surface supplies
> all three: sandboxing via the firewall + MCP gateway + per-tool
> containers, capability-gating via the `safe-outputs:` subsystem, and
> audit via Actions logs. The pattern is vendor-agnostic; the
> realization, at this writing, is uneven. Within three years, agent
> governance platforms will be a category in the way CI/CD became a
> category over the past decade — and what the category will deliver,
> measurably, is those three substrate fields, populated.[^ch15-a10]

[^ch15-a10]: This prediction commits to the substrate-field vocabulary
maintained in the Genesis corpus under A10 GOVERNED OUTER LOOP
(`architectural-patterns.md`). The two governance failure modes that
fall directly out of these substrate fields — TOKEN-LAUNDERING and
INNER-LOOP MISCAST AS OUTER — are catalogued in Ch14 (Team-Level
Anti-Patterns). Ch15:17 already cites the same canonical realization
(`gh-aw`, plugin.json, Spec-Kit) as a stack-convergence signal; the
reuse here makes the prediction falsifiable: a governance platform
that does not deliver SANDBOXING, CAPABILITY_GATING, and AUDIT_SURFACE
is not in the category.

(Tail-extension scope: ~1 paragraph rewrite + 1 footnote. No other
Ch15 paragraphs touched.)

---

## 6. Cross-link audit

| Direction | From | To | Purpose |
|---|---|---|---|
| Internal | Ch14 §The Refactor Moves / R3 EXTRACT | Ch14 §BUNDLE LEAKAGE (#20) | Names PHANTOM DEPENDENCY as the symmetric SHIP-TIME / RUN-TIME scope violation. |
| Internal | Ch14 §BUNDLE LEAKAGE (#20) | Ch14 §Prompt Injection via Dependencies (#19) | Same family — untrusted-or-misaddressed text reaching the model. |
| Internal | Ch14 §WAVE-WITHOUT-GATE | Ch14 §Skipping Checkpoints (#9) and §Cross-Wave Merge Conflicts (#18) | Same disease, named at the architectural level. |
| Internal | Ch14 §The Trust Fall (#7) | Genesis design-patterns (PLAN-AND-PRAY / VERIFY-WITH-LLM-ONLY) | Three names, one disease, one cure. |
| Internal | Ch14 §TOKEN-LAUNDERING / §INNER-LOOP MISCAST AS OUTER | Ch15:23 (rewritten) | Substrate fields the failures violate are the same fields the predicted category is built from. |
| External | Ch14 §The Refactor Moves intro | Ch13 §Tier-3 architectural patterns | R-pattern triggers run BEFORE Tier-3 selection. |
| External | Ch14 §BUNDLE LEAKAGE prevention | Ch09 §TRIGGER ORCHESTRATOR (substrate fields) | Distribution boundary lives there. |
| External | Ch14 §WAVE-WITHOUT-GATE | Ch12 bounded-rounds (calibration N) | Wave gating is the bounded-rounds discipline applied per wave. |
| External | Ch15:23 footnote | Genesis A10 GOVERNED OUTER LOOP | Substrate-field vocabulary source. |
| External | Ch15:23 footnote | Ch14 §TOKEN-LAUNDERING / §INNER-LOOP MISCAST AS OUTER | Failure modes downstream of the substrate fields. |
| Authority | Ch14 Taxonomy table caption | Genesis corpus (anti-pattern reference) | Genesis remains canonical for source-time / packaging entries not absorbed here. |

---

## 7. Impact summary

- **Ch14 length:** +~30 percent (vs. ~100 percent under C5 Shape A
  wholesale absorption). Four new taxonomy rows, four new entries
  (BUNDLE LEAKAGE, WAVE-WITHOUT-GATE, TOKEN-LAUNDERING, INNER-LOOP
  MISCAST AS OUTER), one new section (The Refactor Moves with R1-R4),
  one cross-link insertion, four new footnotes (R1-R4) plus three
  ancillary footnotes (A5 cite, BUNDLE LEAKAGE cite, deferred-four cite),
  and one authority footnote on the Taxonomy table.
- **Ch15:23 length:** +~50 percent in that paragraph only (single
  rewrite). One new footnote. Other Ch15 paragraphs untouched.
- **Voice rule (C8):** All absorbed Genesis names ALL-CAPS verbatim
  (R1 SPLIT, R2 FUSE, R3 EXTRACT, R4 INLINE, BUNDLE LEAKAGE, DISPATCH
  CONTAMINATION, WAVE-WITHOUT-GATE, EVERY-TASK-IS-A-WAVE, TOKEN-
  LAUNDERING, INNER-LOOP MISCAST AS OUTER, PHANTOM DEPENDENCY,
  SANDBOXING, CAPABILITY_GATING, AUDIT_SURFACE, A10 GOVERNED OUTER
  LOOP). Existing handbook entries (Title Case: The Trust Fall,
  Hallucinated Edits, etc.) keep their casing — Ch14 already has its
  own naming convention, and C8's "verbatim" rule applies to the
  Genesis vocabulary being absorbed, not to retroactive rewrites of
  pre-existing handbook entries.
- **Falsifiability gain (Ch15:23):** the prediction now commits to
  three named substrate fields a future governance platform either
  delivers or does not. CTO-proxy verdict ("the prediction is too
  vague to act on; either ship the vocabulary or footnote it") is
  resolved.
- **Genesis authority preserved:** Ch14 absorbs the practitioner-grade
  set; Genesis stays canonical for source-time / packaging detail.
  The four un-evidenced packaging anti-patterns (PHANTOM DEPENDENCY,
  DUPLICATED LEAF, HIDDEN EXTERNAL, UNPINNED CRITICAL DEP) remain
  Genesis-only until Round 2 evidence promotes them.
- **Reader impact:** the Ch14 reader who diagnoses "Decompose" in step
  4 of the Recovery Playbook now has a four-verb vocabulary to apply.
  The Ch14 reader who has the BUNDLE LEAKAGE story at hand recognizes
  why the eval-prompts-look-like-real-requests problem is a
  hallucination amplifier, not an aesthetic issue. The Ch15 reader
  who reaches the governance prediction now knows what the category
  must deliver to count.
- **Risks held:** Ch14 picks up Genesis vocabulary; if the Genesis
  corpus stops being maintained, Ch14 either re-imports the missing
  long-form or footnotes the gap. C5 partial-absorption keeps this
  risk bounded — the long form lives in Genesis; Ch14 owns the
  practitioner-grade summary only.

---

Output written to:
`/Users/danielmeppiel/Repos/genesis-skill/WIP/round-2/ch14-anti-patterns-refactors.md`
