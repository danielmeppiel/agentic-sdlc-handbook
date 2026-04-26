# Ch10 — Integration draft (PROSE x pattern catalogue)

> Scope: weave Genesis design / architectural / refactor patterns under
> each PROSE constraint as worked examples. Bound by A4 author decisions
> at `WIP/round-1/AUTHOR-DECISIONS.md` (C1 Shape A, C8 voice rule, #10
> PROSE citation cleanup, B8 reserved for Ch11).

---

## 1. Integration thesis

PROSE is the constraint language: five letters that name what an agent
setup must do (disclose progressively, reduce scope, compose, bound,
hierarchize) and what it must not. Genesis is the pattern catalogue:
named, falsifiable shapes — with WHEN clauses and anti-patterns — that
satisfy those constraints in source. Today the two corpora are
complementary but unconnected: Ch10 specifies the WHAT, Genesis
catalogues the HOW, and a reader has to bridge them mentally. The
integration is to rewrite each PROSE section so the constraint comes
first (unchanged spec) and one canonical Genesis pattern follows under
it as the worked answer to "what does compliance look like in code?".
Per the C8 voice rule, pattern names appear ALL-CAPS verbatim with a
single verbatim definition box per pattern; surrounding prose stays in
the handbook register established by Ch08.

---

## 2. PROSE-constraint -> Genesis-pattern mapping table

| PROSE constraint | Canonical Genesis pattern | Section in Ch10 |
|---|---|---|
| **P** Progressive Disclosure | **C1 LAZY ASSET** (creational) — declare deferred-load; pair with **S5 LAZY PROXY** (structural reference shape) for the markdown link itself | `## P — Progressive Disclosure` (existing) — add definition box + worked example after "Skills metadata as capability indexes" |
| **R** Reduced Scope | **C3 THREAD SPAWN** (creational) — fresh execution unit with its own context window; bound by **B3 SUPERVISOR** to keep the spawn tree finite | `## R — Reduced Scope` (existing) — add definition box + worked example after "Session splitting across domains" |
| **O** Orchestrated Composition | **S1 COMPOSED MODULE** (structural) — orchestrator declares dependencies on leaf modules, no content duplication | `## O — Orchestrated Composition` (existing) — add definition box + worked example after "Primitive types as atomic units" |
| **S** Safety Boundaries | **S4 VALIDATION DECORATOR** (structural, gates an artifact) + **B10 HUMAN CHECKPOINT** (behavioral, gates an action). For the deterministic seam underneath: **S7 DETERMINISTIC TOOL BRIDGE** | `## S — Safety Boundaries` (existing) — add definition box for S4 after "Validation gates requiring human approval"; add B10 box after the standard role table |
| **E** Explicit Hierarchy | **S6 RULE BRIDGE** (structural) — extract rules into SCOPE-ATTACHED RULE FILEs; runtime auto-loads on path / context match | `## E — Explicit Hierarchy` (existing) — add definition box + worked example after "Pattern-scoped instruction files" |
| Cross-cutting: structural counterpart to PROSE | **G16 four-tier hierarchy** (substrate / affordances / design / architectural) + **G11 rejection-with-WHEN-clause discipline** | New short section `## The Pattern Catalogue Beneath PROSE` between "When Constraints Are Missing" and "Applying the Constraints" — names the catalogue PROSE constraints select from, and forwards detailed treatment to Ch12 |
| Cross-cutting: long-session attention decay | **B8 ATTENTION ANCHOR** | One-paragraph mention inside the Reduced-Scope section pointing forward to Ch11 (full treatment owned by Ch11 per A4 reservation) |

The Compliance Checklist (`ch10:532-552`) gains one column "Realized
by" listing the canonical pattern per row. No checklist questions
change.

---

## 3. Section-by-section edit plan

The constraint sections (`P`, `R`, `O`, `S`, `E`) keep their definition,
"why it matters", existing implementation patterns, and anti-pattern
prose unchanged. The integration is additive: each section gets a
"Realized by:" insertion containing one verbatim Genesis definition
box and one Monday-ready worked example. Six concrete edits:

1. **`## P — Progressive Disclosure` (`ch10:27-103`)** — after
   "Skills metadata as capability indexes" (`ch10:60-72`), insert
   "Realized by: C1 LAZY ASSET" subsection (definition box + worked
   example showing skill frontmatter as the deferred-load declaration).

2. **`## R — Reduced Scope` (`ch10:107-156`)** — after
   "Session splitting across domains" (`ch10:139-140`), insert
   "Realized by: C3 THREAD SPAWN" subsection (definition box +
   worked example mapping the JWT-auth five-session decomposition
   already present at `ch10:506-520` to one C3 spawn per session).
   Add one short paragraph forwarding long-session goal-drift
   handling to Ch11's B8 ATTENTION ANCHOR treatment.

3. **`## O — Orchestrated Composition` (`ch10:159-218`)** — after
   "Primitive types as atomic units" (`ch10:166-200`), insert
   "Realized by: S1 COMPOSED MODULE" subsection (definition box +
   worked example showing how `python.instructions.md`,
   `integrators.instructions.md`, `testing.instructions.md` compose
   without the orchestrator inlining their content).

4. **`## S — Safety Boundaries` (`ch10:221-289`)** — two insertions:
   (a) after "Validation gates requiring human approval"
   (`ch10:257-267`), insert "Realized by: S4 VALIDATION DECORATOR"
   definition box and tie the existing `**STOP**` gate to the named
   pattern; (b) after "Knowledge scoping" (`ch10:269-272`), insert
   "Realized by: B10 HUMAN CHECKPOINT" definition box covering the
   capability / authority axis. Optional pointer to S7 DETERMINISTIC
   TOOL BRIDGE for the existing "Deterministic tools as truth
   anchors" paragraph (`ch10:273`).

5. **`## E — Explicit Hierarchy` (`ch10:292-367`)** — after
   "Pattern-scoped instruction files" (`ch10:317-336`), insert
   "Realized by: S6 RULE BRIDGE" subsection (definition box +
   worked example showing the cascading `applyTo` files as a Rule
   Bridge that keeps voice independent of constraint).

6. **New section: `## The Pattern Catalogue Beneath PROSE`** (insert
   between `## When Constraints Are Missing` (`ch10:371`) and
   `## Applying the Constraints` (`ch10:403`)). 8-10 lines naming
   the four-tier pattern catalogue (substrate / affordances / design
   / architectural) PROSE constraints select from, plus one
   paragraph on the rejection-with-WHEN-clause discipline that
   makes pattern selection auditable. Forwards detailed treatment
   to Ch12.

7. **`## Compliance Checklist` (`ch10:532-552`)** — add a "Realized
   by" column listing the canonical pattern for each row (P1/P2 ->
   C1 LAZY ASSET + S5 LAZY PROXY, R1/R2 -> C3 THREAD SPAWN, O1/O2
   -> S1 COMPOSED MODULE, S1/S2/S3 -> S4 + B10 + S7, E1/E2 -> S6
   RULE BRIDGE).

8. **Citation update (#10):** at the closing-section paragraph
   (`ch10:562`) and across the chapter, the Genesis cite to PROSE
   should land on this chapter rather than the personal blog. The
   downstream edit lives in `genesis/skills/genesis/assets/
   primitives.md:230-231`; see §6 below for the exact replacement
   text.

No paragraph in Ch10 is deleted. No PROSE letter is renamed. No
existing example is rewritten. The chapter grows by approximately
110-140 lines (six definition boxes at ~10 lines each, three short
worked examples at ~12-18 lines each, one new short section at ~25
lines, one checklist column).

---

## 4. Full draft of changed sections

The drafts below show only the inserted / modified content in the
context of the section it joins. Existing handbook prose around them
is unchanged and is not reproduced here unless required for clarity.

---

### 4.1 Insertion under `## P — Progressive Disclosure`

(Insert after `ch10:72`, before `### Anti-pattern: Context dumping`.)

**Realized by: C1 LAZY ASSET.** The progressive-disclosure constraint
has a named pattern that satisfies it at source. Genesis defines it
verbatim:

> C1. LAZY ASSET. WHEN: a MODULE ENTRYPOINT bundles knowledge that only
> some invocations need. Loading it eagerly inflates every session.
> MECHANISM: the SKILL.md body names the asset by relative path; the
> agent loads it only when the process step that needs it executes. The
> asset stays out of context until then. ANTI-PATTERN: EAGER BLOAT —
> inlining the asset into SKILL.md "for convenience". Every dispatch
> hit pays the load cost.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:47-60`.

The skill frontmatter shown earlier is the LAZY ASSET declaration. The
description is read at session start; the body, and any assets the body
references, are read only when the dispatcher activates the skill for a
matching task. The structural counterpart — the link itself — is
S5 LAZY PROXY: a relative-path placeholder the runtime materializes on
demand. The two compose: declare with C1, reference with S5.

The "before / after" pair earlier in this section is, in Genesis terms,
a refactor from EAGER BLOAT to LAZY ASSET + LAZY PROXY. Naming the
pattern lets a reviewer point at a specific deviation ("this skill
inlines its 800-line evaluation rubric — convert to LAZY ASSET")
instead of restating the full constraint each time.

---

### 4.2 Insertion under `## R — Reduced Scope`

(Insert after `ch10:140`, before `### Anti-pattern: Scope creep`.)

**Realized by: C3 THREAD SPAWN.** The pattern Genesis catalogues for
the Reduced-Scope constraint:

> C3. THREAD SPAWN. WHEN: a unit of work benefits from a fresh context
> window — isolation from siblings, full attention on its own scope.
> MECHANISM: parent invokes the harness's spawn affordance with a task
> description and (optionally) a persona / module to load at startup.
> Child runs, returns a value, exits. ANTI-PATTERN: UNBOUNDED SPAWN —
> letting any thread spawn any depth of descendants. Couple with
> SUPERVISOR (B3) to bound the tree.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:88-102`.

The five-session JWT-auth decomposition shown later in this chapter
(see "Applying the Constraints") is one C3 THREAD SPAWN per session.
Each child receives a task description, a fresh context window, and a
narrow set of files. None of the children inherit the parent's
accumulated trace. The orchestrator that issues the spawns is the
SUPERVISOR (B3) referenced above; bounding the spawn tree prevents
"the agent that spawned an agent that spawned an agent" — the most
common failure mode of decomposition without a supervisor.

**A note on long sessions.** Reduced Scope handles drift caused by
context-load size. A second, related drift mode — attention decay over
turn count — is the subject of B8 ATTENTION ANCHOR, the LLM-physics-
native pattern Chapter 11 covers as its spine. Where Reduced Scope says
"keep the session small enough that the goal still fits", ATTENTION
ANCHOR adds "and re-inject the goal at scheduled boundaries when the
session must run long". The two are complementary; Ch11 specifies the
re-injection schedule and anti-patterns (see §The Long-Session Problem
in Chapter 11).

---

### 4.3 Insertion under `## O — Orchestrated Composition`

(Insert after `ch10:200`, before `### Anti-pattern: Monolithic prompt`.)

**Realized by: S1 COMPOSED MODULE.** Composition is the structural
constraint; Genesis names the structural shape that satisfies it:

> S1. COMPOSED MODULE. WHEN: a high-order module's behavior is "load
> these N existing modules and orchestrate them". MECHANISM: the
> orchestrator module declares dependencies on the leaf modules and
> loads them at the relevant process step. No content is duplicated;
> each leaf evolves independently. ANTI-PATTERN: HIDDEN COUPLING —
> copying a leaf's content into the orchestrator instead of depending
> on it. Drift is guaranteed.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:195-209`.

The decomposed setup at the end of this section — `python.instructions
.md`, `integrators.instructions.md`, `testing.instructions.md` — is one
COMPOSED MODULE arrangement: a project-level orchestrator declares the
leaves, and each leaf is independently testable, debuggable, and
versioned. The Monolithic-Prompt anti-pattern shown above is HIDDEN
COUPLING in disguise: every concern is inlined into one file, so
editing one rule risks unintended interaction with every other rule
in the same context.

The naming matters because the reverse refactor has a name too:
when two leaves should never have been split (lockstep co-invocation,
overlapping descriptions), Genesis catalogues R2 FUSE as the
correction. The full source-time refactor verbs (R1 SPLIT / R2 FUSE /
R3 EXTRACT / R4 INLINE) are the topic of Chapter 14.

---

### 4.4 Insertions under `## S — Safety Boundaries`

(Insert after `ch10:267`, before `**Knowledge scoping.**`.)

**Realized by: S4 VALIDATION DECORATOR.** The named pattern behind the
`**STOP**` gate shown above:

> S4. VALIDATION DECORATOR. WHEN: a procedure produces an artifact
> whose correctness can be checked deterministically before downstream
> steps consume it. MECHANISM: wrap the producing step with a
> deterministic gate (linter, test run, schema validator, checklist
> invocation). The gate decides pass / revise. The decorated step
> keeps its single responsibility; the decorator owns the verification
> concern. ANTI-PATTERN: WRAPPING WITHOUT BLOCKING — recording
> violations to a log without halting. Non-blocking gates degrade to
> noise.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:251-264`.

The anti-pattern is the discipline that matters in practice: a "stop"
that does not stop — a checklist the agent is asked to complete after
the fact, a comment-only review with no merge gate — is WRAPPING
WITHOUT BLOCKING. The decorator must own the verdict.

(Insert after `ch10:272`, before `**Deterministic tools as truth anchors.**`.)

**Realized by: B10 HUMAN CHECKPOINT.** Where the validation decorator
gates an artifact, B10 gates an action that requires authority the
agent does not have:

> B10. HUMAN CHECKPOINT. WHEN: a step is irrecoverable, expensive, or
> requires authority the agent does not have. Common examples:
> shipping a release; merging to main; deleting persistent state;
> making any decision that the agent's self-confidence cannot resolve
> (drift detection; suspected hallucination; tie between equally-fit
> patterns). MECHANISM: the procedure halts at a named checkpoint. The
> agent emits a structured prompt to the human (current state,
> options, recommended choice with rationale, escape hatches).
> Execution does not resume until the human responds. The response IS
> the gate verdict.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:722-749`.

The "must STOP before" entries in the Standard Role Boundaries table
(`ch10:235-238`) are HUMAN CHECKPOINTs by another name. The named
anti-patterns to watch for: SILENT DRIFT (the agent suspects
misalignment but powers through), CHATTY GATE (checkpointing on every
minor decision so the human rubber-stamps), and POST-HOC CHECKPOINT
(asking for approval after the action — that is a notification, not a
gate).

The "Deterministic tools as truth anchors" paragraph that follows
this insertion describes S7 DETERMINISTIC TOOL BRIDGE: the structural
seam between probabilistic LLM reasoning and deterministic execution.
Where the boundary crosses out of the LLM layer entirely (apply a
migration, post a comment, deploy a service), S7 is the named pattern;
its full treatment lives in Chapter 12 alongside the multi-agent
patterns it composes with.

---

### 4.5 Insertion under `## E — Explicit Hierarchy`

(Insert after `ch10:336`, before `**Compilation for portability.**`.)

**Realized by: S6 RULE BRIDGE.** The pattern that turns directory- and
pattern-scoped instruction files into a coherent hierarchy:

> S6. RULE BRIDGE. WHEN: many personas share the same hard rules
> (encoding, secrets, review etiquette) but each persona has its own
> voice. Inlining the rules into every persona couples voice to rules;
> updating one rule requires editing N persona files. MECHANISM:
> extract the rules into SCOPE-ATTACHED RULE FILEs. The runtime
> auto-loads them on path / context match. Personas now vary along the
> LENS axis; rules vary along the CONSTRAINT axis; neither edits the
> other. ANTI-PATTERN: BAKED-IN RULES — repeating the encoding rule
> inside every persona. Drift, then contradiction.
>
> Source: `genesis/skills/genesis/assets/design-patterns.md:299-316`.

The cascading `applyTo` files shown above are the Rule Bridge in
practice: the specific authentication rules at `src/api/auth/**/*.py`
load on path match, the general API rules at `src/api/**/*.py` load on
the broader match, and the language-level rules at `**/*.py` load
universally. An agent editing an authentication file inherits all
three layers; an agent editing CSS inherits none of them. The
hierarchy is real because the runtime resolves it, not because a
human re-reads the rules each session — the bridge is a runtime
contract, not editorial discipline.

The Flat-Instructions anti-pattern that closes this section is
BAKED-IN RULES at file scale: the entire repository's rules in one
document, with no scope discrimination. Every agent loads every rule
on every task; drift surfaces as cross-domain interference (the Python
backend agent applying CSS naming guidance to module organization).

---

### 4.6 New section: `## The Pattern Catalogue Beneath PROSE`

(Insert between `ch10:399` (end of When-Constraints-Are-Missing) and
`ch10:403` (start of Applying-the-Constraints).)

The five PROSE constraints answer the question "what must my setup
do?". A separate, parallel question — "what shapes do I have to
choose from when satisfying them?" — is the topic of the pattern
catalogue. Genesis organizes that catalogue in four tiers:

| Tier | What it names | Examples |
|---|---|---|
| Tier 0 — Substrate primitives | The six file shapes every agent harness implements under different folder names and frontmatter dialects. | PERSONA SCOPING FILE, MODULE ENTRYPOINT, SCOPE-ATTACHED RULE FILE, CHILD-THREAD SPAWN, TRIGGER ORCHESTRATOR, PLAN PERSISTENCE. |
| Tier 1 — Per-harness affordances | Tool-specific syntax (`apm.yml`, `.cursor/rules`, `.github/workflows`). Loaded only at codegen time. | Adapter files per harness. |
| Tier 2 — Design patterns | GoF-style creational / structural / behavioral patterns realized in agent setups. | C1 LAZY ASSET, S1 COMPOSED MODULE, S6 RULE BRIDGE, B8 ATTENTION ANCHOR. |
| Tier 3 — Architectural patterns | System-shape compositions of Tier-2 patterns: the AI-native equivalents of Microservices, Pipes-and-Filters, Saga. | A1 PANEL, A2 PIPELINE, A4 STAFFED PLAN, A10 GOVERNED OUTER LOOP. |

The constraints in this chapter are independent of which tier a
solution lives at: a Progressive Disclosure win can come from a
Tier-2 LAZY ASSET pattern in one repository or from a Tier-3 STAFFED
PLAN topology in another. Naming the catalogue gives reviewers a
shared vocabulary for "which pattern realizes this constraint here?"
The full Tier-2 / Tier-3 catalogue, with WHEN clauses and
anti-patterns, is the content of Chapter 12.

**Selection produces an audit trail.** Each pattern in the catalogue
carries a WHEN clause — the conditions that make it the right answer.
Selection is therefore not a single pick but a comparison: the patterns
considered, the patterns rejected, and the WHEN clause that cut the
choice. A handoff packet that names the rejected patterns alongside the
selected one is auditable in a way a single answer is not. This
discipline, captured by Genesis as "rejection-with-WHEN-clause", is
the structural counterpart to PROSE: PROSE constrains what counts as a
valid answer; the rejection trail constrains what counts as a valid
process for choosing one.

---

### 4.7 Compliance Checklist column update

(Modify table at `ch10:538-551`, adding one column.)

| # | Constraint | Question | Realized by | Pass |
|---|---|---|---|---|
| P1 | Progressive Disclosure | Does every instruction file over 100 lines use links (not inline content) for subsidiary topics? | C1 LAZY ASSET + S5 LAZY PROXY | |
| P2 | Progressive Disclosure | Does every cross-reference link include a description of what the target contains (not just a filename)? | C1 LAZY ASSET (description discipline) | |
| R1 | Reduced Scope | Can you state each agent task in one sentence with a single deliverable? | C3 THREAD SPAWN | |
| R2 | Reduced Scope | Do multi-step workflows start each phase with a fresh context (no accumulated session state)? | C3 THREAD SPAWN + B3 SUPERVISOR | |
| O1 | Orchestrated Composition | Does each instruction file address exactly one concern (check: could you name the file after its single topic)? | S1 COMPOSED MODULE | |
| O2 | Orchestrated Composition | Do workflow prompts reference shared instruction files by link rather than pasting their content? | S1 COMPOSED MODULE (no HIDDEN COUPLING) | |
| S1 | Safety Boundaries | Does every agent configuration have an explicit `tools` list (no wildcards)? | S7 DETERMINISTIC TOOL BRIDGE (capability) | |
| S2 | Safety Boundaries | Is there a `**STOP**` gate before every operation that modifies auth, database schemas, or production config? | S4 VALIDATION DECORATOR + B10 HUMAN CHECKPOINT | |
| S3 | Safety Boundaries | Does every agent have a file-path boundary (explicit list of directories it may modify)? | S6 RULE BRIDGE (knowledge scoping via `applyTo`) | |
| E1 | Explicit Hierarchy | Do instructions exist at three or more specificity levels (e.g., root -> domain -> module)? | S6 RULE BRIDGE | |
| E2 | Explicit Hierarchy | Can you add module-specific rules without editing any file above that module's scope? | S6 RULE BRIDGE (no BAKED-IN RULES) | |

---

## 5. ATTENTION ANCHOR cross-link to Ch11

B8 ATTENTION ANCHOR is the first pattern Genesis catalogues without a
classical analog: it is induced by LLM physics (attention decay over
turns) rather than by software-engineering structure, and it is the
single most important behavioral pattern for any non-trivial agent
task that runs long. Per the A4 reservation it earns a chapter spine
slot in Ch11, not a definition box here.

The cross-link Ch10 carries lives in §4.2 above (Reduced Scope),
phrased as one paragraph: Reduced Scope handles drift caused by
context-load size; ATTENTION ANCHOR handles drift caused by attention
decay over turn count. The two are complementary, and Ch11 specifies
the re-injection schedule (start of every meaningful step, before / after
every spawn, after any tool failure) and the three anti-patterns
(ANCHOR DRIFT, OVER-ANCHORING, IMPLICIT-ANCHOR) that destroy the
discipline (see §The Long-Session Problem in Chapter 11). No further
B8 treatment is duplicated in Ch10.

---

## 6. Citation update

Per A4 decision #10, the citation at `genesis/skills/genesis/assets/
primitives.md:230-231` should land on this chapter rather than the
personal blog. The current text reads:

> Each primitive earns its keep against PROSE
> ([danielmeppiel.github.io/awesome-ai-native](https://danielmeppiel.github.io/awesome-ai-native/)):
>
> Source: `genesis/skills/genesis/assets/primitives.md:230-231`.

Replacement (one-line edit):

> Each primitive earns its keep against PROSE — the canonical
> specification of the five constraints (Progressive Disclosure,
> Reduced Scope, Orchestrated Composition, Safety Boundaries,
> Explicit Hierarchy) is Chapter 10 of *Architecting Codebases for AI*
> (apm-handbook, `handbook/ch10-the-prose-specification.qmd`). The
> blog post at
> [danielmeppiel.github.io/awesome-ai-native](https://danielmeppiel.github.io/awesome-ai-native/)
> remains the original public statement and stays as secondary
> provenance.

The mapping table that follows (`primitives.md:233-239`) is unchanged;
its five rows are the same five rows that Ch10 §2 above cross-references
in the constraint -> pattern mapping. The handbook is now the canonical
source; the blog is the historical first statement.

---

## 7. Impact summary

- **Ch10 grows by ~110-140 lines.** No paragraph is deleted; all
  insertions are additive. Six verbatim definition boxes (one per
  canonical pattern), three short worked examples, one new short
  section ("The Pattern Catalogue Beneath PROSE"), one column added
  to the Compliance Checklist.
- **Voice rule (C8) honored.** Every Genesis pattern name appears
  ALL-CAPS verbatim. Every definition box is a verbatim quotation
  with `>` blockquote and source path:line. Surrounding prose
  matches the Ch08 register.
- **No reservation violated.** B8 ATTENTION ANCHOR keeps its Ch11
  spine slot; Ch10 gets one cross-link paragraph only. Tier-3
  architectural patterns (A1, A2, A4, A9, A10) are named in the
  Pattern Catalogue section but their full treatment stays in Ch12 /
  Ch15. Refactor verbs (R1-R4) are named once and forwarded to Ch14.
- **Cross-corpus loop closed.** PROSE was the only constraint
  language without a named pattern catalogue underneath it; Genesis
  was the only pattern catalogue without a constraint language above
  it. Ch10 is now the single page that connects them — letter to
  pattern, constraint to mechanism.
- **Citation cleanup (#10) lands.** One-line edit to
  `primitives.md:230-231` moves the canonical PROSE cite from the
  personal blog to this chapter; the blog remains as secondary
  provenance.
- **Downstream effects.** Ch11's B8 spine acquires an upstream
  anchor (Ch10 §4.2 forwards to it explicitly). Ch12's pattern
  treatment acquires an upstream anchor (Ch10 §4.6 forwards the
  full catalogue to it). Ch14's refactor verbs acquire an upstream
  anchor (Ch10 §4.3 names them once in the COMPOSED MODULE
  insertion).
- **Reader payoff.** A reviewer can now point at a specific Ch10
  paragraph and say "this skill violates LAZY ASSET" rather than
  restating the Progressive-Disclosure prose; an author can build
  the Compliance Checklist into a code-review template by citing
  the pattern column.
