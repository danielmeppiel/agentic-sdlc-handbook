# Ch09 — Integration draft (the six substrate primitives)

## 1. Resolution summary

Shape A of C1 retitles the chapter "The Six Substrate Primitives" and adopts the Genesis runtime-role taxonomy (PERSONA SCOPING FILE, MODULE ENTRYPOINT, SCOPE-ATTACHED RULE FILE, CHILD-THREAD SPAWN, TRIGGER ORCHESTRATOR, PLAN PERSISTENCE) as canonical section headers. Each section opens with an "Industry terms:" mapping line so a reader who only knows "instruction file" or "AGENTS.md" or "skill" lands on the right primitive within one sentence. The current seven-block file-extension diagram demotes to an appendix titled "The seven file-shape view (legacy)"; the canonical composition diagram becomes the Genesis substrate graph. C4 Shape A splits the old §Memory: PLAN PERSISTENCE is its own substrate primitive (active plan, todos, checkpoints; reload-on-re-grounding); cross-session knowledge stays as a clearly labeled sub-section ("Cross-session memory: a separate bin") inside §PLAN PERSISTENCE. Prompts, which have no Genesis equivalent, are retired from Ch09's canonical list and cross-linked to Ch10. Body content (file format examples, design tests, instrumentation audit, before/after, feedback loop, annotated session, starting points) is preserved nearly verbatim — only headers, the lead-in mapping line, and the verbatim definition box are new.

## 2. Vocabulary mapping table (canonical, ships in the chapter)

| Genesis (canonical) | Industry terms | Old handbook section | Status |
|---|---|---|---|
| PERSONA SCOPING FILE | AGENTS.md, agent file, persona, mode, custom agent, subagent definition | §Agents | rename + absorb |
| MODULE ENTRYPOINT | skill (agentskills.io), plugin, command bundle, SKILL.md | §Skills | rename + reframe content as one kind of container content |
| SCOPE-ATTACHED RULE FILE | instruction file, rule, .mdc, always-load, applyTo glob | §Instructions | rename, preserve |
| CHILD-THREAD SPAWN | subagent thread, Task tool, dispatch, background agent | (new — not in Ch09 today) | new section, drawn from Ch12 dispatch mechanic |
| TRIGGER ORCHESTRATOR | hook, runtime trigger, gh-aw workflow, automation, scheduled job | §Hooks + part of §Orchestration | merge under one primitive; add SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE substrate fields |
| PLAN PERSISTENCE | scratchpad, plan.md, todos, checkpoints, session store | §Memory (active-plan portion) | extract from Memory; promote to its own primitive |
| MEMORY (cross-session) | memory, knowledge, .memory.md, context bank | §Memory (cross-session portion) | retain narrowed as sub-section inside §PLAN PERSISTENCE |
| Prompts | (no Genesis equivalent) | §Prompts | retire from canonical list; cross-link to Ch10 §Reusable Workflows; one-paragraph mention in appendix |
| Specification (.spec.md) | spec, plan-mode artifact | §Orchestration (content portion) | move out of Ch09; cross-link to Ch10 (PROSE specification chapter owns it) |

## 3. Section-by-section edit plan

**§Title and intro paragraph** — Rewrite. Title becomes "The Instrumented Codebase". Sub-heading "The six substrate primitives" replaces "It defines seven primitive types." The opening paragraph stays — it makes no taxonomy claim. The second paragraph changes from "seven primitive types" to "six substrate primitives" and adds one sentence: "Each primitive is named for its runtime role — what the harness does with the file — rather than its file extension. The same `SKILL.md` shape can serve as a MODULE ENTRYPOINT in one harness and as a TRIGGER ORCHESTRATOR's session bootstrap in another; the role is the substrate, the extension is the dialect."

**§What Instrumentation Means** — Keep verbatim. The argument is taxonomy-agnostic.

**§The Seven Primitive Types** — Rename to "The Six Substrate Primitives." Body fully re-spined under Genesis names. The seven-block `block-beta` diagram moves to the appendix; replace with a six-node mermaid graph using Genesis's composition shape (TRIGGER ORCHESTRATOR above, CHILD-THREAD SPAWN dispatching, three loaded primitives feeding the thread, PLAN PERSISTENCE as the durable artifact).

**§Instructions → §SCOPE-ATTACHED RULE FILE** — Rename. Body preserved including the API instructions example and the 40-50-line length heuristic. Add the verbatim definition box and the "Industry terms" lead-in.

**§Agents → §PERSONA SCOPING FILE** — Rename. Body preserved including the four-element list (domain expertise, named patterns, anti-patterns, tool boundaries) and the Python Architect example. Add definition box and lead-in. Add one paragraph clarifying the Genesis KEY PROPERTY: a persona is loaded *into* a thread; conflating persona with thread is the most common error.

**§Skills → §MODULE ENTRYPOINT** — Rename and reframe. The decision-framework framing is retained but explicitly marked as one kind of *content* a MODULE ENTRYPOINT can hold (per FR's M4 wording). The directory layout, the four-rule activation/description discipline, and the design test (multi-file? framework? code-pattern-triggered?) all stay. The cli-logging-ux example stays. Cross-link to agentskills.io for the container surface; cross-link to Genesis for the broader taxonomy.

**§Prompts** — Retire from canonical list. Replace with a one-paragraph "Reusable workflows: see Chapter 10" pointer; move the `.prompt.md` example and prose to Ch10 §Reusable Workflows (note for Ch10 deep-dive author: this content arrives unchanged). Keep one short appendix entry with the example so Ch09 remains self-contained for readers landing here from a search.

**§Memory** — Split per C4. The cross-session example (Authentication / API Versioning / Performance Decisions blocks) stays under a labelled sub-section "Cross-session memory: a separate bin" inside §PLAN PERSISTENCE. The active-plan / todos / checkpoint discipline becomes the §PLAN PERSISTENCE main body. Preserve the staleness / quarterly-review prose and the "Memory Storage Varies by Tool" callout under the sub-section.

**§Orchestration** — Split. The `.spec.md` example and the spec-as-context discussion move to Ch10 (cross-link in Ch09). The dispatch-mechanic content (which Ch12 also owns) is captured in the new §CHILD-THREAD SPAWN. The orchestration-of-events content merges into §TRIGGER ORCHESTRATOR.

**§Hooks → §TRIGGER ORCHESTRATOR** — Rename and expand. The three-bullet "Examples of what hooks automate" list stays as a starting-points sidebar. Add the substrate-fields sub-list (SANDBOXING, CAPABILITY_GATING, AUDIT_SURFACE) per C3, with gh-aw safe-outputs cited as the existing-today reference implementation. Add the "trigger surface IS the matcher" point from primitives.md to disambiguate from MODULE ENTRYPOINT's dispatcher matching.

**(new) §CHILD-THREAD SPAWN** — Net-new section. Three short paragraphs: definition box, the context-isolation argument (loaded as text only, stateless across spawns, hand off via explicit artifacts), and the COMPOUNDING GAIN observation (a MODULE ENTRYPOINT dispatched in a fresh child thread converts SoC into context-isolation for free). Cross-link forward to Ch12 for orchestration topologies.

**§Tool Support and Portability** — Keep as-is structurally. Re-label the "Primitive" column with Genesis names; the body cells (Copilot / Cursor / Claude Code / Windsurf / OpenCode) need no change. Update the three observations: replace "Instructions are the universal context file" with "SCOPE-ATTACHED RULE FILEs are the universal context file"; replace "Agent configurations are the least portable" with "PERSONA SCOPING FILE activation is the least portable layer." Drop the Prompts row.

**§Directory Structure** — Keep verbatim. The `.github/instructions/`, `.github/agents/`, `.github/skills/` layout matches MODULE / SCOPE-ATTACHED RULE / PERSONA SCOPING file conventions. Update the in-text labels to use Genesis names alongside the directory names.

**§How Primitives Compose** — Rewrite the seven-layer hierarchy diagram as the Genesis substrate composition graph (from primitives.md:213-228). Preserve the worked example ("when an agent is asked to modify `src/api/users.py`"); update the layer labels to Genesis names.

**§The Instrumentation Audit** — Keep verbatim. Update the "If the knowledge..." mapping table to use Genesis primitive names in the right column.

**§Before and After / §What the numbers look like / §The Feedback Loop / §What It Looks Like (Annotated Session) / §Starting Points / §From primitives to frameworks** — Keep verbatim. Light terminology touch-ups: "agent config" → "PERSONA SCOPING FILE (`.agent.md`)" on first mention, then back to natural language; "instruction file" → "SCOPE-ATTACHED RULE FILE (`.instructions.md`)" on first mention. The annotated session prose does NOT need its developer's words changed — those are quoted verbatim. Only the chapter's connective prose around the quotes adopts Genesis vocabulary.

**(new) Appendix A: The seven file-shape view** — One-page appendix containing the original `block-beta` diagram and a paragraph: "The file-shape view groups primitives by extension and use-case. It is the reader's shortest path from a `.cursor/rules/auth.mdc` they already see in their tree to the substrate role it plays. The substrate view in the body of this chapter is the more durable cut." Map the seven file shapes to the six substrate roles in a small table (Prompts is the eighth row, marked as Ch10-adjacent).

## 4. New chapter spine (proposed TOC)

1. (intro) The instrumented codebase
2. What instrumentation means
3. The six substrate primitives
   3.1 PERSONA SCOPING FILE
   3.2 MODULE ENTRYPOINT
   3.3 SCOPE-ATTACHED RULE FILE
   3.4 CHILD-THREAD SPAWN
   3.5 TRIGGER ORCHESTRATOR
   3.6 PLAN PERSISTENCE (with sub-section: Cross-session memory: a separate bin)
4. Tool support and portability
5. Directory structure
6. How the substrate composes
7. The instrumentation audit
8. Before and after
9. The feedback loop
10. What it looks like: an annotated session
11. Starting points
12. From primitives to frameworks
13. Appendix A: The seven file-shape view (legacy diagram + mapping)

## 5. Full draft of changed sections

### 5.1 Revised intro (replaces lines 1-9 of ch09)

```
---
title: "The Instrumented Codebase"
---

Open any repository that uses AI agents reliably and you'll notice
something before you read a single line of application code: the
project is full of markdown files that aren't documentation. They're
instruction sets, persona definitions, capability bundles, plan
artifacts, and event-triggered workflows, scattered through `.github/`
directories and woven into the source tree. These files don't ship
to production. They don't appear in the build output. But they
determine whether an AI agent produces code that respects the
project's architecture or code that confidently violates it.

This chapter catalogs those files. It defines six substrate primitives
named for their runtime role — what the harness actually does with
each file — rather than for the extension on disk. The same `SKILL.md`
shape can act as a MODULE ENTRYPOINT in one harness and as a TRIGGER
ORCHESTRATOR's session bootstrap in another; the role is the substrate,
the extension is the dialect. Chapter 10 specifies the constraints
these primitives implement. Chapter 11 teaches the context engineering
discipline that makes them effective. This chapter answers the prior
question: what, specifically, are you building?
```

### 5.2 Revised §What instrumentation means (no body changes)

Preserved verbatim from current ch09 lines 11-19.

### 5.3 §The six substrate primitives (replaces "The Seven Primitive Types")

Lead-in paragraph:

> Six primitives cover what every modern agent harness loads, spawns, or
> persists. Each is named for the role it plays at runtime, not for the
> file extension that carries it. Different harnesses use different
> dialects — `.instructions.md`, `.cursor/rules/*.mdc`, `CLAUDE.md`
> sections, AGENTS.md — but a SCOPE-ATTACHED RULE FILE is a SCOPE-ATTACHED
> RULE FILE in all of them. Naming the substrate once means the vocabulary
> outlives any one tool.

Replacement composition diagram (replaces the `block-beta` figure at lines 27-41):

```{mermaid}
%%| label: fig-six-primitives
%%| fig-cap: "The six substrate primitives and how they compose"
%%| fig-alt: "Composition graph: TRIGGER ORCHESTRATOR at the top spawns CHILD-THREAD SPAWNs. Each thread loads three primitives at startup (PERSONA SCOPING FILE, MODULE ENTRYPOINT, SCOPE-ATTACHED RULE FILE). All threads read and write a single PLAN PERSISTENCE artifact."
flowchart TD
    T["TRIGGER ORCHESTRATOR<br/>workflow / hook / schedule"]
    C1["CHILD-THREAD SPAWN<br/>fresh context window"]
    C2["CHILD-THREAD SPAWN<br/>fresh context window"]
    P["PERSONA SCOPING FILE<br/>who the agent is"]
    M["MODULE ENTRYPOINT<br/>capability + lazy assets"]
    R["SCOPE-ATTACHED RULE FILE<br/>path-matched constraints"]
    PP[("PLAN PERSISTENCE<br/>active plan / todos / checkpoints")]

    T -->|spawns| C1
    T -->|spawns| C2
    P -.->|loaded into| C1
    M -.->|loaded into| C1
    R -.->|loaded into| C1
    P -.->|loaded into| C2
    M -.->|loaded into| C2
    R -.->|loaded into| C2
    C1 <-->|reads / writes| PP
    C2 <-->|reads / writes| PP
```

#### 5.3.1 PERSONA SCOPING FILE

*Industry terms: AGENTS.md, agent file, persona, mode, custom agent, subagent definition.*

::: {.callout-note title="Genesis definition"}
> A markdown document loaded at session start to scope WHO the
> agent is. Sets voice, expertise lens, hard constraints, anti-patterns
> it flags. It has no execution life of its own — it is text loaded
> into a context window.
>
> *Source: `genesis/assets/primitives.md:14-19`.*
:::

A PERSONA SCOPING FILE answers "who should work on this?" — not in terms of a human team member, but in terms of what expertise, priorities, and constraints the task requires.

**File format:** `.agent.md` (Copilot), agent-mode rule (Cursor), `/commands` definition (Claude Code), `AGENTS.md` (universal). Frontmatter typically declares the model, the tool surface, and a short activation description.

```yaml
---
description: "Backend architecture specialist for Python services"
tools: ["changes", "codebase", "editFiles", "runCommands",
        "search", "problems", "testFailure"]
model: claude-sonnet-4.5
---
```

```markdown
# Python Architect

You are an expert Python architect specializing in CLI tool design
and modular service architecture.

## Design Philosophy
- Speed and simplicity over complexity
- Solid foundation that can be iterated on
- Operations proportional to affected files, not workspace size

## Patterns You Enforce
- BaseIntegrator for all file-level integrators
- CommandLogger for all CLI output
- AuthResolver for all credential access

## You Never
- Add a new base class when an existing one can be extended
- Instantiate AuthResolver per-request (it is a singleton)
- Import from integration/ in the CLI layer (use the public API)
```

Four elements make a PERSONA SCOPING FILE effective: domain expertise specific enough to constrain the solution space, named patterns the agent can reference in its reasoning, anti-patterns that encode institutional memory, and tool boundaries that make safety boundaries concrete.

The substrate property to internalize: a persona is loaded *into* a thread; a thread is not a persona. Conflating the two is the most common error in this domain. When you see a "panel review" implemented as one persona switching voices inside one context window, that is the conflation showing up as PANEL-IN-ONE-CONTEXT (Chapter 12 catalogues the failure mode).

Start with three to five PERSONA SCOPING FILEs — an architect, a domain expert for your core business logic, and a documentation writer cover most tasks. Add files when you observe repeated corrections; that is the signal that a new specialization has earned its place.

#### 5.3.2 MODULE ENTRYPOINT

*Industry terms: skill (agentskills.io), plugin, command bundle, SKILL.md.*

::: {.callout-note title="Genesis definition"}
> A bundled, self-contained capability with its own assets and a
> contract (frontmatter description = function signature; body =
> process; assets = lazy-loaded knowledge). The unit of REUSE.
>
> *Source: `genesis/assets/primitives.md:32-36`.*
:::

A MODULE ENTRYPOINT is a *container*. The agentskills.io specification owns the container surface — the SKILL.md frontmatter fields, the 1024-character description cap, the directory layout (`scripts/` + `references/` + `assets/`), the body-size budget. What goes *inside* the container is the question this chapter has historically answered with "decision frameworks." That answer is correct, and it is one kind of content among several. A MODULE ENTRYPOINT can hold a decision framework, an evaluation playbook, an extraction procedure, or a packaging recipe. The container is the same; the content shape varies.

**File format:** A directory containing a `SKILL.md` entrypoint plus optional `assets/` and `scripts/` subtrees. The frontmatter `description` field is preloaded by the harness's dispatcher; treat it as a function signature, not as marketing copy.

```
.github/skills/
└── cli-logging-ux/
    ├── SKILL.md
    └── examples/
        ├── good-warning.py
        └── bad-warning.py
```

```markdown
---
name: cli-logging-ux
description: >
  Activate whenever code touches console helpers, DiagnosticCollector,
  STATUS_SYMBOLS, or any user-facing terminal output.
---

# CLI Logging UX

## Decision Framework

### The "So What?" Test
Every warning must answer: what should the user do about this?
A warning without a suggested action is noise.

### The Traffic Light Rule
| Color  | Helper           | Meaning            |
|--------|------------------|--------------------|
| Green  | _rich_success()  | Completed          |
| Yellow | _rich_warning()  | User action needed |
| Red    | _rich_error()    | Cannot continue    |
| Blue   | _rich_info()     | Status update      |

### The Newspaper Test
Can a user scan the output like headlines?
If they have to read paragraphs to understand status, restructure.

## Anti-Patterns
- Never use bare print() or click.echo() without styling
- Never emit a warning without an actionable suggestion
- Never mix Rich and colorama in the same output path
```

The design test for a MODULE ENTRYPOINT is three criteria: does this knowledge apply across multiple files, does it require more than a few rules to express, and is it triggered by a detectable code pattern? If all three are yes, the knowledge belongs in a module. If it applies to a single directory, it is a SCOPE-ATTACHED RULE FILE. If it is a general disposition, it is a PERSONA SCOPING FILE.

A MODULE ENTRYPOINT differs from a SCOPE-ATTACHED RULE FILE in an important way: it provides a *decision framework*, not just rules. A rule says "use `_rich_warning()` for warnings." A framework says "every warning must answer 'what should the user do about this?'" The framework generalizes to situations the author did not anticipate. Rules cover known cases. Frameworks cover unknown ones.

For the canonical specification of the container surface — frontmatter fields, body size budget, evaluation discipline, the trigger-eval split (~20 queries 60/40 train/val) — refer to agentskills.io. For the broader taxonomy of how MODULE ENTRYPOINTs compose with other primitives, this chapter and the Genesis substrate are the source of truth.

#### 5.3.3 SCOPE-ATTACHED RULE FILE

*Industry terms: instruction file, rule, .mdc, always-load, applyTo glob.*

::: {.callout-note title="Genesis definition"}
> A constraint that auto-applies whenever the agent operates on a
> matching path or context. Cross-cutting rules ride along instead
> of needing to be re-stated in every persona.
>
> *Source: `genesis/assets/primitives.md:132-136`.*
:::

SCOPE-ATTACHED RULE FILEs are the most granular primitive. They tell an agent: "when you touch code in this scope, follow these rules." The harness controls when they load — by path match or context predicate. The author does not call them; the runtime injects them.

**File format:** `.instructions.md` with frontmatter specifying scope (Copilot), `.cursor/rules/*.mdc` with glob (Cursor), per-directory `CLAUDE.md` (Claude Code), `.windsurfrules` cascade (Windsurf).

```markdown
---
applyTo: "src/api/**"
description: "API layer conventions for endpoint implementation"
---

# API Development Rules

## Middleware Registration
- All middleware decorators are registered in `middleware.py`, never inline on routes.
- Route files define endpoint logic only.

## Rate Limiting
- Use `app.rate_limiter.RateLimiter`, not third-party libraries.
  The internal implementation integrates with the metrics pipeline.
- Rate limit values come from environment variables, never hardcoded.

## Error Responses
- All error responses use `APIError.from_exception()` for consistent format.
- Never return raw exception messages to clients.
```

The design test: can you state the scope in one `applyTo` pattern? Does every rule in the file apply to that scope? If you find yourself writing rules that apply to two unrelated domains, split the file. If you cannot express the scope as a glob, the knowledge probably belongs in a PERSONA SCOPING FILE or a MODULE ENTRYPOINT instead.

What distinguishes a good SCOPE-ATTACHED RULE FILE from a bad one is length. If your file exceeds 40-50 lines, it is trying to do too much. The reason is mechanical: every line of rule competes for attention with the source code the agent needs to read. A 200-line rule file does not give an agent more to work with — it gives it more to get lost in.

#### 5.3.4 CHILD-THREAD SPAWN

*Industry terms: subagent thread, Task tool, dispatch, background agent.*

::: {.callout-note title="Genesis definition"}
> A runtime affordance that creates a new execution unit with its
> OWN fresh context window. Returns a value to the parent. Multiple
> may run in parallel.
>
> *Source: `genesis/assets/primitives.md:149-153`.*
:::

CHILD-THREAD SPAWN is the only mechanism for parallelism and context isolation a harness offers. The spawning thread suspends (or continues, if the harness supports async); the child runs with a fresh window seeded only by the task description and any primitives the parent loaded into it; the child returns a value as text or structured data.

**File format:** None. CHILD-THREAD SPAWN is a runtime affordance, not a file you author. Most harnesses surface it as a tool call (`task` in Copilot CLI, the Task tool in Claude Code, subagent dispatch in Cursor). Chapter 12 covers the orchestration topologies — A1 PANEL, A2 PIPELINE, A4 STAFFED PLAN — that compose CHILD-THREAD SPAWNs into multi-agent workflows.

The substrate property to internalize: a child thread is stateless across spawns. Anything not loaded as text into the child thread does not exist for that thread. Hand off via explicit artifacts — a slice of PLAN PERSISTENCE, a frozen pointer to a MODULE ENTRYPOINT — not assumed memory. The most expensive failure mode in this primitive is treating the child thread as if it inherits the parent's context implicitly. It does not.

The compounding gain worth naming: a MODULE ENTRYPOINT dispatched in a fresh child thread converts a Separation-of-Concerns win into a context-isolation win for free. This is the core argument for splitting a god-module into specialized siblings — each split unlocks an independently spawnable thread.

#### 5.3.5 TRIGGER ORCHESTRATOR

*Industry terms: hook, runtime trigger, gh-aw workflow, automation, scheduled job.*

::: {.callout-note title="Genesis definition"}
> A declarative pipeline that spawns sessions in response to events
> (schedule, push, comment, label, manual). Lives ABOVE the thread,
> deciding when work begins and what initial context it carries.
>
> *Source: `genesis/assets/primitives.md:174-178`.*
:::

TRIGGER ORCHESTRATORs make instrumentation reactive. Without them, every primitive is passive — it waits for an agent to be invoked and for the right context to load. With them, the substrate responds to events: a file save runs a check, a new file scaffolds a test, a merged PR updates a memory file, a label applied to an issue dispatches a triage agent.

**File format:** Configured via tool-specific orchestration mechanisms. GitHub Agentic Workflows (gh-aw) is the canonical realization shipping today; Copilot hooks, Cursor task runners, and Claude Code's pre/post commands are alternative surfaces. The trigger surface, not an in-session dispatcher, is the matcher: an event filter, a slash command, a schedule.

The substrate property to internalize: TRIGGER ORCHESTRATOR is the only primitive whose execution surface is fully declarative. It does not carry a context window itself; it dispatches others that do.

**Substrate fields** (present when the trigger surface provides them — GitHub Agentic Workflows safe-outputs is the existing-today reference implementation):

- **SANDBOXING.** Substrate-enforced isolation around the spawned session: network firewall, per-tool container, scoped filesystem. When absent, the session inherits whatever ambient access the invoking environment has. This is the property that makes "let the agent run on push" safe rather than reckless.
- **CAPABILITY_GATING.** The session does not hold write tokens to external systems. Effects are buffered and externalized by a deterministic post-stage that the session cannot bypass. This is the runtime-enforced form of A9 SUPERVISED EXECUTION (see Chapter 12). An agent that wants to comment on a PR emits a structured request; the orchestrator validates and posts. The agent never holds the GitHub token.
- **AUDIT_SURFACE.** A durable log of what triggered, what ran, what was externalized; survives the session and is reviewable by third parties. This is the property that lets "agents touched production" become an after-the-fact claim with evidence rather than a folk story.

These three fields are the vocabulary the predicted governance category will be measured against (Chapter 15). A TRIGGER ORCHESTRATOR that ships SANDBOXING, CAPABILITY_GATING, and AUDIT_SURFACE is governance-ready. A trigger surface that ships none of them is a webhook with delusions.

Start with one or two TRIGGER ORCHESTRATORs: a linting check on save and a test prompt on new file creation cover the highest-leverage triggers. Add more only when you observe a repeated manual step that a hook could eliminate.

#### 5.3.6 PLAN PERSISTENCE

*Industry terms: scratchpad, plan.md, todos, checkpoints, session store.*

::: {.callout-note title="Genesis definition"}
> A stable artifact (file or structured store) holding the active
> plan, todos, and checkpoints across turns and across spawns. The
> cure for attention decay over long sessions.
>
> *Source: `genesis/assets/primitives.md:192-196`.*
:::

The underlying problem PLAN PERSISTENCE addresses is mechanical: tokens far from the current focus point exert weaker influence on inference. As a session grows, earlier decisions, todos, and constraints fade from the model's effective recall even though they remain technically in-context. A 200-turn session whose plan is buried in turn 3 is a session that has forgotten the plan.

The discipline is straightforward: write the plan once, early, before drafting modules or spawning workers; reload it at every re-grounding boundary — start of each step, return from a spawn, after a tool failure, whenever uncertainty rises. A written-once-never-read plan is dead weight. The discipline is *write-then-reload*, not *write-then-trust-recall*.

**File format:** `plan.md` in a session directory (Copilot CLI), structured todos in the harness's session store, embedded checkpoint blocks in `CLAUDE.md` (Claude Code). The substrate guarantees the slots exist; the syntax varies.

A PLAN PERSISTENCE artifact has up to four slots: a free-form plan capturing problem statement and approach, a structured todo list with per-step status, an optional checkpoint slot for milestone snapshots, and an optional files slot for cross-step artifacts that must outlive any single step's context. Spawned child threads receive a *pointer* to the relevant slice of the plan in their task description; they do not inherit the parent's context.

Use PLAN PERSISTENCE when the work spans more than three dependent steps, more than one file, or one or more child-thread spawns. Skip it for single-shot one-step work where the entire instruction set fits comfortably in the prompt.

##### Cross-session memory: a separate bin

PLAN PERSISTENCE captures the active plan — the work in flight. A separate bin captures the durable, cross-session knowledge the project has accumulated: which authentication pattern is current and which is deprecated, why the logging module wraps Rich, the migration history that explains a half-deprecated class. This is what the previous edition of this chapter called §Memory, and it remains a distinct concept.

**File format:** `.memory.md` (portable), SQLite store (Copilot), notepads (Cursor), `CLAUDE.md` sections (Claude Code).

```markdown
# Project Decisions

## Authentication (last updated: 2025-06-15)
- Migrated from session-based to JWT auth in Q1 2025
- Token refresh uses exponential backoff, max 3 retries
- EMU (Enterprise Managed User) tokens use standard PAT prefixes
  (`github_pat_` / `ghp_`); `ghu_` is OAuth, not EMU.
- The `SessionAuth` class is deprecated but not yet removed.
  Do NOT use it for new code. Migration tracked in JIRA-4521.
```

Cross-session memory captures knowledge that does not fit in a SCOPE-ATTACHED RULE FILE because it is not a rule; it is context. "Use JWT for authentication" is a rule. "We migrated from sessions to JWT in Q1, and the old SessionAuth class is still in the code but deprecated" is context. An agent that knows only the rule might accidentally use the deprecated class. An agent that also has the memory will not.

Cross-session memory is the most likely primitive to drift from reality. Include dates. Review quarterly. If a section has not been updated in six months, verify or remove it.

::: {.callout-note}
## Memory storage varies by tool
While this section describes cross-session memory as markdown files for portability, some tools implement memory as structured databases. GitHub Copilot, for example, stores memory in a database system rather than flat files. The principles are the same — persistence, discoverability, staleness management — regardless of the storage mechanism.
:::

The two bins serve different attention horizons. PLAN PERSISTENCE survives the current session's attention decay. Cross-session memory survives the current session entirely. Conflating the two — putting JIRA-4521-style historical context into the live plan, or treating the live plan as durable knowledge — is the most common authoring mistake in this primitive.

### 5.4 §How the substrate composes (replaces "How Primitives Compose")

The hierarchy diagram (currently a nested ASCII outline at lines 436-444) is replaced with the Genesis composition graph. Worked example prose ("when an agent is asked to modify `src/api/users.py`") preserved with Genesis names substituted at first mention.

```
TRIGGER ORCHESTRATOR (workflow / hook / schedule)
        |
        v  spawns
  CHILD-THREAD SPAWN ----- spawns more child threads ----+
        |                                                |
        | loads at startup                               |
        |   PERSONA SCOPING FILE  (who)                  |
        |   MODULE ENTRYPOINT     (capability)           |
        |   SCOPE-ATTACHED RULE   (path-matched)         |
        |                                                |
        v                                                v
   reads + writes                              reads + writes
        |                                                |
        +--------> PLAN PERSISTENCE  (single source of truth)
                   + cross-session memory (separate bin)
```

When an agent is asked to modify `src/api/users.py`, the effective context assembles from:

1. **Global SCOPE-ATTACHED RULE FILE** — error handling, security, testing rules that apply everywhere
2. **API-scoped SCOPE-ATTACHED RULE FILE** — the `applyTo: "src/api/**"` file loads; the frontend file does not
3. **API middleware MODULE ENTRYPOINT** — activates because the task involves an API route
4. **Backend-dev PERSONA SCOPING FILE** — provides the lens, the model selection, and the tool boundaries
5. **Cross-session memory** — the API versioning decisions, the deprecated authentication class, the rate-limit timeout
6. **PLAN PERSISTENCE** — the current step, the prior turn's findings, the checkpoint that survives a child-thread spawn

Each layer adds specificity. None contradicts the layer above; more specific primitives refine general guidance, they do not override it. If a conflict exists, it indicates a design error in the instrumentation, not a resolution the agent should attempt.

This composition is the Explicit Hierarchy constraint made concrete (Chapter 10).

### 5.5 Updated Tool Support and Portability table

Re-label the Primitive column with Genesis names; drop the Prompts row (cross-link to Ch10 instead).

| Primitive | GitHub Copilot (VS Code) | Cursor | Claude Code | Windsurf | OpenCode |
|---|---|---|---|---|---|
| **SCOPE-ATTACHED RULE FILE** | `.instructions.md` + `applyTo`; `copilot-instructions.md` | `.cursor/rules/*.mdc` + glob | `CLAUDE.md` per directory | `.windsurfrules`; cascade rules | `.opencode/instructions.md` |
| **PERSONA SCOPING FILE** | `.agent.md` with model + tools | rules and agent modes | `/commands` and agent configs | — | — |
| **MODULE ENTRYPOINT** | `SKILL.md` dirs with examples | embedded in rules with examples | embedded in `CLAUDE.md` sections | embedded in rules | — |
| **CHILD-THREAD SPAWN** | `task` tool; subagent dispatch | subagent dispatch | Task tool | — | — |
| **TRIGGER ORCHESTRATOR** | Copilot hooks; VS Code tasks; gh-aw workflows | task runners; `.cursor/hooks/` | hooks (`hooks` in settings); pre/post commands | — | — |
| **PLAN PERSISTENCE** | `plan.md` + SQLite session store; `.memory.md` portable | notepads; project rules | `CLAUDE.md` sections; persistent memory | embedded in rules | — |

(Cross-link: reusable workflows — formerly §Prompts — see Chapter 10.)

Three observations:

**SCOPE-ATTACHED RULE FILEs are the universal substrate.** Every major tool reads markdown from predictable locations and applies it as scoped context. File naming and matching differ; the underlying concept transfers without loss. This is where to invest first, regardless of tooling.

**PERSONA SCOPING FILE activation is the least portable layer.** Mode selection, model binding, and tool boundaries are defined differently in every tool and do not transfer. The knowledge inside the file (domain expertise, named patterns, anti-patterns) is just markdown and moves freely. The activation mechanism does not.

**The three major harnesses now support most substrate primitives natively.** Copilot, Cursor, and Claude Code each cover the majority of the six. As of this writing, Copilot has the most extensive native format support; Cursor and Claude Code are narrowing the gap quickly. OpenCode and Windsurf trail. The methodology described here is portable across all of them — the knowledge transfers even when the wiring differs.

### 5.6 Headers updated in §Directory Structure

Add Genesis-name annotations to the directory tree comments, e.g.:

```
project/
├── .github/
│   ├── copilot-instructions.md          # Global SCOPE-ATTACHED RULE FILE
│   ├── instructions/                     # SCOPE-ATTACHED RULE FILEs
│   │   ├── api.instructions.md           # applyTo: "src/api/**"
│   │   └── ...
│   ├── agents/                           # PERSONA SCOPING FILEs
│   │   ├── architect.agent.md
│   │   └── ...
│   ├── skills/                           # MODULE ENTRYPOINTs
│   │   └── cli-logging-ux/
│   │       └── SKILL.md
│   └── workflows/                        # TRIGGER ORCHESTRATORs
│       └── on-pr-opened.lock.yml
├── plan.md                               # PLAN PERSISTENCE (active)
├── .memory.md                            # cross-session memory
├── AGENTS.md                             # PERSONA SCOPING FILE (root discovery)
└── ...
```

### 5.7 Updated §Instrumentation audit mapping table

Step 4 mapping (replaces table at lines 495-503):

| If the knowledge... | It belongs in a... |
|---|---|
| Is a constraint scoped to specific files or directories | SCOPE-ATTACHED RULE FILE |
| Requires a specific lens, model, or tool surface | PERSONA SCOPING FILE |
| Is a reusable, dispatcher-discoverable capability with its own assets | MODULE ENTRYPOINT |
| Coordinates multiple specialists in fresh context windows | CHILD-THREAD SPAWN (see Chapter 12) |
| Should run automatically on a repository event | TRIGGER ORCHESTRATOR |
| Is the active plan or todo state for the current work | PLAN PERSISTENCE |
| Is a durable decision, deprecation, or historical fact | cross-session memory (sub-bin of PLAN PERSISTENCE) |
| Is a repeatable multi-step workflow specification | (Chapter 10 — reusable workflow) |
| Is a feature spec with components and success criteria | (Chapter 10 — PROSE specification) |

### 5.8 Annotated session — terminology touch-ups only

The developer's verbatim quotes are preserved (see C8 voice rule, applied to handbook text not just Genesis-derived text). Connective prose updates to first-mention Genesis names:

- "the auth-expert.agent.md" → "the auth-expert PERSONA SCOPING FILE (`.agent.md`)" on first mention; subsequent mentions revert to natural language.
- "the logging skill" → "the logging MODULE ENTRYPOINT" on first mention; subsequent mentions revert.
- "instruction file" → "SCOPE-ATTACHED RULE FILE (`.instructions.md`)" on first mention.

Net delta: roughly six sentences touched across the annotated-session section.

### 5.9 Appendix A: The seven file-shape view (legacy)

One-page appendix preserving the original `block-beta` figure and adding a mapping table:

| File-shape (legacy view) | Substrate primitive (canonical) |
|---|---|
| `.instructions.md` | SCOPE-ATTACHED RULE FILE |
| `.agent.md` | PERSONA SCOPING FILE |
| `SKILL.md` | MODULE ENTRYPOINT |
| `.prompt.md` | (Chapter 10 — reusable workflow) |
| `.memory.md` | PLAN PERSISTENCE > cross-session memory |
| `.spec.md` | (Chapter 10 — PROSE specification) |
| Hook config | TRIGGER ORCHESTRATOR |
| (no file) | CHILD-THREAD SPAWN (runtime affordance) |

The file-shape view is the reader's shortest path from a `.cursor/rules/auth.mdc` they already see in their tree to the substrate role it plays. The substrate view in the body of this chapter is the more durable cut: it survives extension renames, frontmatter dialect drift, and cross-harness migration. Two views, one taxonomy.

## 6. Cross-link audit

Internal links in Ch09 to update:

- `§Skills` → `§MODULE ENTRYPOINT` (4 occurrences in current file: lines 121, 325, 394, 558)
- `§Instructions` → `§SCOPE-ATTACHED RULE FILE` (5 occurrences: 43, 323, 348, 384, 549)
- `§Agents` → `§PERSONA SCOPING FILE` (3 occurrences: 75, 324, 389)
- `§Memory` → `§PLAN PERSISTENCE` (and sub-section "Cross-session memory") (4 occurrences: 217, 327, 339, 442)
- `§Hooks` → `§TRIGGER ORCHESTRATOR` (3 occurrences: 294, 329, 443)
- `§Prompts` → `Chapter 10 §Reusable Workflows` (3 occurrences: 174, 326, 441)
- `§Orchestration` (specs) → `Chapter 10 §PROSE Specification` (3 occurrences: 256, 328, 440)

Cross-chapter outbound link refresh (notify deep-dive authors):

- **Ch10 deep-dive**: receives §Prompts (`.prompt.md` example + workflow prose, lines 174-215) and §Orchestration spec content (`.spec.md` example, lines 256-292). Should land as Ch10 §Reusable Workflows + §Specification Artifacts.
- **Ch11 deep-dive**: §The Instruction Hierarchy currently links to old §Instructions / §Memory; refresh to §SCOPE-ATTACHED RULE FILE / §PLAN PERSISTENCE + cross-session memory.
- **Ch12 deep-dive**: §CHILD-THREAD SPAWN is the substrate primitive Ch12 patterns sit on. Add a one-sentence forward ref from Ch09 §CHILD-THREAD SPAWN to Ch12 §Pattern 1 (A1 PANEL); update Ch12's introductory paragraph to cite Ch09 §CHILD-THREAD SPAWN as the substrate definition.
- **Ch13 deep-dive**: §Checkpoint Discipline references "plan.md" — refresh to "PLAN PERSISTENCE (Chapter 9)."
- **Ch14 deep-dive**: anti-patterns referencing "skill" or "memory" should align to Genesis names. SILENT SEMANTIC FAILURE entry at Ch14 line 1xx references "instrumentation files" — concrete to "SCOPE-ATTACHED RULE FILE / PERSONA SCOPING FILE."
- **Ch15 deep-dive**: governance prediction at ch15:23 commits to SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE vocabulary (per A4 decision #2). Cite Ch09 §TRIGGER ORCHESTRATOR as the chapter that introduces the vocabulary.

External link refresh:

- agentskills.io — kept as authority for MODULE ENTRYPOINT container surface (frontmatter, body budget, eval discipline).
- gh-aw safe-outputs — cited under §TRIGGER ORCHESTRATOR substrate fields as the existing-today reference implementation of CAPABILITY_GATING.
- danielmeppiel.github.io/awd-cli/.../anatomy-of-an-apm-package/ — replace per §7 below.

## 7. APM URL verification

Cited URL: `https://danielmeppiel.github.io/awd-cli/introduction/anatomy-of-an-apm-package/`
Source location: `genesis/assets/module-system-adapters/apm.md:34`. Same URL form referenced in `genesis/assets/primitives.md:230-231` as the PROSE corpus root (separate concern — that one resolves cleanly to `danielmeppiel.github.io/awesome-ai-native/`, returns 200, no action needed).

```
$ curl -sIL -o /dev/null -w "%{http_code} %{url_effective}" \
    "https://danielmeppiel.github.io/awd-cli/introduction/anatomy-of-an-apm-package/"
404 https://danielmeppiel.github.io/awd-cli/introduction/anatomy-of-an-apm-package/

$ curl -sIL -o /dev/null -w "%{http_code} %{url_effective}" \
    "https://microsoft.github.io/apm/introduction/anatomy-of-an-apm-package/"
200 https://microsoft.github.io/apm/introduction/anatomy-of-an-apm-package/
```

**Status:** OLD URL DEAD (404). NEW URL LIVE (200) at the microsoft/apm canonical location.

**Recommendation:** Replace `https://danielmeppiel.github.io/awd-cli/introduction/anatomy-of-an-apm-package/` with `https://microsoft.github.io/apm/introduction/anatomy-of-an-apm-package/` in `genesis/assets/module-system-adapters/apm.md:34`. One-line edit. No ambiguity — the new URL is at the canonical microsoft/apm doc site, the old URL is a transitional `awd-cli`-era artifact that no longer resolves. This satisfies A4 decision #11 ("Verify... OR update to microsoft/apm location"); update is the action.

(Note: the PROSE citation in `primitives.md:230-231` is a *separate* fix tracked under A4 decision #10 — replace the blog cite with a Ch10 cite, keep the blog as secondary provenance. Out of scope for Ch09 deep-dive but flagged here so the cleanup PR can batch both edits.)

## 8. Impact summary

**Word count delta** (Ch09 file `ch09-the-instrumented-codebase.qmd`, currently ~52 KB / ~801 lines):

- §The seven primitive types (heading, intro, fig) → §The six substrate primitives: roughly +40 lines (six definition boxes, six "Industry terms:" lead-ins, expanded TRIGGER ORCHESTRATOR with substrate fields, new CHILD-THREAD SPAWN section, PLAN PERSISTENCE with sub-section).
- §Skills body → §MODULE ENTRYPOINT body: net flat (~5 lines added for container/content distinction).
- §Memory split → §PLAN PERSISTENCE + sub-section: net flat (active-plan paragraphs added; cross-session content moved under sub-heading).
- §Prompts → cross-link + appendix: roughly -25 lines from main body, +15 in appendix.
- §Orchestration body → cross-link to Ch10: roughly -25 lines from main body.
- New Appendix A: roughly +30 lines.
- Header / table-cell terminology touch-ups across portability table, directory tree, audit mapping, annotated session: roughly +20 lines net.

**Net delta:** approximately +50 to +70 lines of body, +30 lines of appendix. Total chapter grows by roughly 8-10%. Voice register matches Ch08 (handbook prose around verbatim Genesis definition boxes per C8 rule).

**Appendix additions:**

- Appendix A: The seven file-shape view (legacy diagram + mapping table).

**Cross-coupling needs from sibling deep-dives:**

- **Ch10 deep-dive:** must accept §Prompts content and §Orchestration spec content as new sections. Coordinate the landing — Ch09 will cross-link before Ch10 has the destination sections. Suggest a placeholder section in Ch10 with current content moved verbatim, then the Ch10 author refines.
- **Ch11 deep-dive:** confirm §Five-Layer Hierarchy refers to Genesis names; otherwise the Ch09 → Ch11 cross-link reads as a bait-and-switch.
- **Ch12 deep-dive:** confirm A1 PANEL section adds the "(architecturally: A1 PANEL — see Genesis architectural-patterns.md)" second sentence per C7 Shape C, AND accepts a forward-ref from Ch09 §CHILD-THREAD SPAWN.
- **Ch13 deep-dive:** confirm §Checkpoint Discipline points back to Ch09 §PLAN PERSISTENCE rather than redefining the primitive.
- **Ch14 deep-dive:** SILENT SEMANTIC FAILURE entry already referenced from Ch09 annotated session. Confirm the cross-link target survives Ch14's restructure.
- **Ch15 deep-dive:** vocabulary commitment at ch15:23. Ch09 §TRIGGER ORCHESTRATOR introduces SANDBOXING / CAPABILITY_GATING / AUDIT_SURFACE; Ch15 must use the same three names without paraphrase.

**Risk register:**

- C8 voice rule discipline: every new section header is ALL-CAPS. The `block-beta` to `flowchart TD` mermaid switch is also a small visual change — the substrate composition view does not fit the 4×2 grid the original used.
- Chapter title — "The Instrumented Codebase" is preserved (no rename to "The Six Substrate Primitives"). The sub-heading "The six substrate primitives" carries the taxonomy claim; the chapter title remains the user-facing artifact title. This honors C1 Shape A's Ch09 retitle phrasing while not breaking any existing inbound links from sibling chapters that say "see Chapter 9: The Instrumented Codebase."
