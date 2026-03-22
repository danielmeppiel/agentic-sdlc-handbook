# Chapter 10: The PROSE Specification

Chapter 1 introduced five architectural constraints for human-AI collaboration and gave each a name. This chapter gives each a specification. By the end, you will know how to implement every constraint, how to recognize when one is violated, and how the five constraints interact to produce properties that none achieves alone.

This is the reference chapter. Return to it when you are designing your instruction hierarchy, sizing a task for an agent, or debugging why a workflow that used to be reliable has started producing inconsistent results.

---

## The Constraint Model

PROSE defines five constraints. Each addresses a structural property of language models — finite context, stateless reasoning, probabilistic output — and each induces a desirable property in the system that follows it. The constraints are independent in definition and interdependent in practice.

| Constraint | Addresses | Induces |
|---|---|---|
| **P**rogressive Disclosure | Context overload | Efficient context utilization |
| **R**educed Scope | Scope creep | Manageable complexity |
| **O**rchestrated Composition | Monolithic collapse | Flexibility, reusability |
| **S**afety Boundaries | Unbounded autonomy | Reliability, verifiability |
| **E**xplicit Hierarchy | Flat guidance | Modularity, domain adaptation |

The remainder of this chapter specifies each constraint in full: what it means, why it matters, how to implement it, what violation looks like, and how it interacts with the others.

---

## P — Progressive Disclosure

**Definition.** Structure information to reveal complexity progressively. Context arrives just-in-time — loaded when the agent needs it for the current task — not just-in-case, where everything is loaded upfront on the assumption it might be relevant.

**Why it matters.** Context windows are finite. Attention within those windows is not uniform — information competes for focus, and material far from the active task gets lost. Loading everything upfront does not ensure the agent sees everything. It ensures the agent sees nothing clearly.

A 200,000-token context window filled with architecture documents, coding standards, API specifications, and every source file that might be relevant is not a well-informed agent. It is a diluted one. The signal-to-noise ratio determines quality, not the volume of signal.

### Implementation patterns

**Markdown links as lazy-loading pointers.** The simplest mechanism for progressive disclosure is a link. When an instruction file references `[authentication patterns](../../docs/auth-patterns.md)` rather than inlining the full authentication guide, the agent loads that content only when the current task involves authentication. The link acts as a pointer — a declaration that deeper context exists, with a path to reach it.

```markdown
# API Development Guidelines

## Authentication
Follow the [authentication patterns](../../docs/auth-patterns.md) for all
protected endpoints. Token refresh logic is documented in
[token lifecycle](../../docs/token-lifecycle.md).

## Error Handling
Use the project's [error taxonomy](../../docs/errors.md). Every public
endpoint must return structured error responses.
```

The agent reads the guidelines. If the task involves authentication, it follows the link. If the task involves error handling, it follows a different link. Neither loads material for the other.

**Descriptive labels for relevance assessment.** Links work only when the agent can determine whether to follow them. Descriptive text — not just a filename, but a statement of what the linked content contains — enables the agent to assess relevance before loading.

Bad: `See [docs](./docs/auth.md).`

Good: `See [JWT validation and refresh token rotation patterns](./docs/auth.md) for all endpoints requiring authentication.`

The second version gives the agent enough information to decide whether the link is relevant to the current task without following it.

**Skills metadata as capability indexes.** A skill's frontmatter describes what it does and when to activate. This metadata acts as an index — the agent reads the description, determines relevance, and loads the full skill content only when the task matches.

```yaml
---
name: form-validation
description: >
  Activate when building or modifying form validation logic.
  Covers schema definition, error message formatting, and
  accessibility requirements for form feedback.
---
```

The agent working on a database migration sees this description and skips it. The agent building a user registration form loads the full content.

### Anti-pattern: Context dumping

The most common violation of Progressive Disclosure is loading everything upfront. A single instruction file that inlines the full coding standards, the complete API reference, the authentication guide, and the error taxonomy — all in one document — wastes context capacity on material that is irrelevant to most tasks. The agent's attention spreads across thousands of tokens of guidance, most of which do not apply.

**Before** — everything inlined in one file:

```markdown
# Project Rules

[2,000 words of coding standards]
[1,500 words of authentication patterns]
[800 words of error handling]
[1,200 words of deployment procedures]
[600 words of accessibility requirements]
```

**After** — pointers with descriptive labels:

```markdown
# Project Rules

## Core Standards
- [Coding standards and naming conventions](./standards/coding.md)
- [Authentication patterns and token lifecycle](./standards/auth.md)
- [Error taxonomy and response formatting](./standards/errors.md)
- [Deployment procedures and environment configuration](./standards/deploy.md)
- [Accessibility requirements for user-facing components](./standards/a11y.md)
```

Same information. Fraction of the context cost per task.

---

## R — Reduced Scope

**Definition.** Match task size to context capacity. Complex work is decomposed into tasks sized to fit available context. Each sub-task operates with fresh context and focused scope.

**Why it matters.** Attention degrades with context length. A task that starts as "fix the authentication bug" and expands mid-session to include "also update the tests, refactor that utility, and add the new endpoint" will produce lower-quality output on every sub-task than if each had been handled independently. The agent does not forget earlier instructions in the way a human does — it deprioritizes them as newer, more recent content claims attention.

The practical consequence is that the best-sized task is one that an agent can complete without asking follow-up questions and without accumulating enough context to degrade its own attention. If you find yourself adding context mid-session to keep the agent on track, the task is too large.

### Implementation patterns

**Phase decomposition.** Separate planning from implementation from testing. Each phase gets a fresh context window with only the information relevant to that phase.

```
Phase 1: Diagnose
  Input: error logs, relevant source files
  Output: root cause analysis with 2-3 candidate fixes

Phase 2: Implement
  Input: chosen fix from Phase 1, relevant source files
  Output: code changes

Phase 3: Validate
  Input: changed files, test suite
  Output: test results, regression check
```

Each phase operates with a clean context. The diagnosis phase does not carry the implementation context. The validation phase does not carry the diagnosis context. Quality remains consistent across phases because attention is never split.

**The completeness test.** Before dispatching a task to an agent, ask: "Can the agent complete this without asking me a follow-up question?" If the answer is no, either the task is too large (decompose it) or the context is insufficient (add the missing information). Both are scope problems.

**Session splitting across domains.** When a change spans multiple domains — frontend, backend, database — use separate sessions for each. A backend agent does not need the frontend component tree in its context. A database migration agent does not need the UI routing logic.

### Anti-pattern: Scope creep

A session starts with a focused task. Mid-session, additional requests accumulate:

```
User: Fix the login timeout bug.
Agent: [analyzes, proposes fix]
User: Good, also update the session management tests.
User: While you're at it, refactor the token refresh logic.
User: And can you add the new /logout endpoint?
```

By the fourth request, the agent is operating with the accumulated context of four different tasks, attention split across all of them. The quality of the logout endpoint — the newest and least-contextualized task — is significantly lower than the quality of the original bug fix.

**Fix:** Each of those requests becomes its own session. The cost is four sessions instead of one. The benefit is four tasks done well instead of four tasks done poorly.

---

## O — Orchestrated Composition

**Definition.** Favor small, chainable primitives over monolithic frameworks. Build complex behaviors by composing simple, well-defined units.

**Why it matters.** Language models reason better with clear, focused instructions. A 3,000-word mega-prompt that covers role definition, coding standards, error handling, testing requirements, security rules, documentation format, and output structure is not a well-specified agent. It is an unpredictable one. Small changes to any section produce unexpected changes in behavior across all sections, because the model processes the entire block as a single context.

Composition preserves clarity. Each primitive is small enough to understand, test, and debug independently. Complex behavior emerges from combining primitives, not from making any single primitive more complex.

### Implementation patterns

**Primitive types as atomic units.** The building blocks are instruction files, skills, agents, prompts, and specifications. Each has a focused purpose:

```
.github/
├── instructions/
│   ├── frontend.instructions.md     # applyTo: "**/*.{tsx,jsx}"
│   ├── backend.instructions.md      # applyTo: "**/*.py"
│   └── testing.instructions.md      # applyTo: "**/test/**"
├── chatmodes/
│   ├── architect.chatmode.md        # Planning — cannot execute
│   └── backend-dev.chatmode.md      # Implementation — scoped tools
├── prompts/
│   └── feature-impl.prompt.md       # Multi-step workflow
└── skills/
    └── form-validation/
        └── SKILL.md                 # Auto-activated by relevance
```

Each file has a single responsibility. The frontend instructions do not contain backend rules. The architect agent does not have implementation tools. The feature workflow composes these primitives without duplicating their content.

**Workflows as compositions.** A prompt file orchestrates multiple primitives into a sequence:

```markdown
# Feature Implementation Workflow

1. Review the [project specification](${specFile})
2. Analyze [existing patterns](./src/patterns/) for consistency
3. Implement changes following active instructions
4. Run validation: tests pass, linting clean, no regressions
5. **STOP** — present implementation summary for human review
```

The workflow does not restate the coding standards — the instruction files handle that. It does not redefine the agent's role — the agent configuration handles that. It composes existing primitives into a sequence.

**Explicit contracts between agents.** When multiple agents work in parallel, each must have a defined output contract. Agent A produces a diagnosis. Agent B consumes that diagnosis and produces an implementation. The contract between them — the format and content of the diagnosis — is specified, not assumed.

### Anti-pattern: Monolithic prompt

All guidance in a single block. Role, rules, examples, constraints, output format — everything in one prompt:

```markdown
You are an expert Python developer who follows PEP 8 and uses type hints
everywhere. Always use the BaseIntegrator pattern for new integrators.
Never use os.walk — use find_files_by_glob instead. Log all errors with
_rich_error(). Write tests for every public method. Use pytest fixtures,
not setUp/tearDown. Document all public APIs with Google-style docstrings.
Format output as JSON when returning structured data. Never modify files
outside the src/ directory. Always run the linter before committing...
```

This works until it does not. When the agent produces incorrect output, which instruction failed? Which rule contradicted which other rule? A monolithic prompt is impossible to debug because every instruction interacts with every other instruction in ways the model resolves internally, without explanation.

**Fix:** Each concern becomes its own primitive file. The Python conventions go in `python.instructions.md`. The integrator architecture goes in `integrators.instructions.md` with `applyTo: "src/**/integration/**"`. The testing standards go in `testing.instructions.md`. Each is independently testable, independently debuggable, and independently versioned.

---

## S — Safety Boundaries

**Definition.** Every agent operates within explicit boundaries: what tools are available (capability), what context is loaded (knowledge), and what requires human approval (authority).

**Why it matters.** Language models are non-deterministic. The same input can produce different outputs. This is a fundamental property, not a quality issue to be resolved with better training. When a non-deterministic system has unbounded authority — access to every tool, permission to modify any file, no requirement to seek approval — the variance in its outputs translates directly into variance in its effects. A deterministic system with a bug produces the same bug every time; you can find it and fix it. A non-deterministic system with unbounded authority produces different failures each time, making debugging impractical.

Boundaries do not reduce the agent's usefulness. They constrain its variance. An agent that can modify backend code but not frontend assets, that can run tests but not deploy to production, that must pause for approval before deleting files — this agent is both more useful and more trustworthy than one with no restrictions.

### Implementation patterns

**Tool whitelists per agent.** Each agent configuration declares the specific tools it can access:

```yaml
---
description: "Backend development specialist"
tools: ["editFiles", "runCommands", "search", "testFailure"]
---
```

The backend agent cannot access deployment tools. It cannot modify CI/CD configuration. Its capability boundary is explicit and auditable.

**Validation gates requiring human approval.** Critical decisions — architectural changes, security-sensitive modifications, data migrations — require the agent to stop and present its plan before proceeding:

```markdown
## Validation Gate
Before modifying any authentication logic:
1. Present the proposed changes with rationale
2. **STOP** and wait for explicit human approval
3. Do not proceed until approval is received
```

The gate is part of the instruction, not an external enforcement mechanism. The agent's context includes the requirement to pause.

**Knowledge scoping with `applyTo` patterns.** Instructions load only when the agent is working on matching files. Backend security rules do not load when the agent edits CSS. Frontend accessibility requirements do not load during database migrations:

```yaml
---
applyTo: "src/auth/**"
description: "Security patterns for authentication module"
---
```

The `applyTo` pattern is a knowledge boundary — it determines what the agent knows, not just what it can do.

**Deterministic tools as truth anchors.** When an agent claims a test passes, a boundary-constrained system requires the agent to actually run the test and report the deterministic result. Code execution, API calls, file system operations — these are deterministic tools that ground probabilistic generation in verifiable reality.

### Anti-pattern: Unbounded agent

An agent with access to every tool, every file, and no approval requirements:

```yaml
---
description: "General development assistant"
tools: ["*"]
---
```

This agent can modify production configuration, delete test fixtures, rewrite CI pipelines, and access credentials — all without human oversight. When (not if) it produces an unexpected output, the blast radius is the entire repository.

**Fix:** Define the minimum set of tools, the minimum scope of knowledge, and the explicit approval points for each agent role. A planning agent gets read-only tools. An implementation agent gets write tools for its domain only. A deployment agent requires human approval at every stage.

---

## E — Explicit Hierarchy

**Definition.** Instructions form a hierarchy from global to local. Local context inherits from and may override global context. Agents resolve context by walking from the most specific scope to the most general.

**Why it matters.** Different domains require different guidance. The coding standards for a React frontend are not the coding standards for a Python backend. The security rules for an authentication module are not the security rules for a static content page. Flat guidance — the same rules everywhere — either over-generalizes (rules too vague to be useful) or over-specifies (rules for every domain loaded into every context, polluting attention with irrelevant material).

Hierarchy solves both problems. Global rules establish consistency: naming conventions, commit message format, documentation standards. Local rules enable specialization: the authentication module gets security-specific instructions, the frontend gets accessibility-specific instructions, the database layer gets migration-specific instructions. Each domain inherits the global rules and adds or overrides with local ones.

### Implementation patterns

**Directory-scoped context files.** The `AGENTS.md` standard uses directory placement to define scope. A file at the project root applies everywhere. A file in `frontend/` applies only to frontend code. A file in `frontend/components/` applies only to components:

```
project/
├── AGENTS.md                    # Global: naming, commits, documentation
├── frontend/
│   ├── AGENTS.md               # Frontend: React patterns, accessibility
│   └── components/
│       └── AGENTS.md           # Components: prop conventions, testing
└── backend/
    ├── AGENTS.md               # Backend: API design, error handling
    └── auth/
        └── AGENTS.md           # Auth: security patterns, token handling
```

An agent editing `backend/auth/token.py` resolves context by walking up: `auth/AGENTS.md` + `backend/AGENTS.md` + root `AGENTS.md`. An agent editing `frontend/components/Button.tsx` resolves: `components/AGENTS.md` + `frontend/AGENTS.md` + root `AGENTS.md`. Neither loads the other's domain-specific rules.

**Pattern-scoped instruction files.** The `applyTo` frontmatter targets instructions by file pattern, achieving hierarchical specificity without requiring directory-level files:

```yaml
# General Python rules
---
applyTo: "**/*.py"
---

# Stricter rules for the public API surface
---
applyTo: "src/api/**/*.py"
---

# Most specific: authentication module security rules
---
applyTo: "src/api/auth/**/*.py"
---
```

More specific patterns override or extend less specific ones. The authentication module inherits general Python rules and general API rules, then adds its own security requirements.

**Compilation for portability.** Instruction files authored in tool-specific formats (`.instructions.md` with `applyTo`) can be compiled into hierarchical `AGENTS.md` files for universal portability. The source of truth is the authored instructions. The compiled output is the portable delivery format. This separation means the hierarchy works regardless of which AI coding tool the developer uses.

### Anti-pattern: Flat instructions

A single instruction file at the project root containing every rule for every domain:

```markdown
# Project Instructions

## Python
Use type hints. Follow PEP 8...

## React
Use functional components. Follow accessibility guidelines...

## Authentication
Use JWT with RS256. Rotate refresh tokens...

## Database
Use migrations for all schema changes...

## CSS
Use CSS modules. Follow BEM naming...
```

Every agent, regardless of what it is working on, loads all of this. The Python backend agent processes CSS naming conventions. The database migration agent processes React accessibility guidelines. Attention is wasted. Worse, rules from unrelated domains can interfere — the agent might apply the "use modules" CSS guidance to Python module organization, producing unexpected results.

**Fix:** Split by scope. Python rules in a Python-scoped file. React rules in a frontend-scoped file. Authentication rules in an auth-scoped file. Each agent loads only what applies to its current task.

---

## Interaction Effects

The five constraints are defined independently but produce their strongest effects in combination. Three interactions are particularly important.

**Progressive Disclosure + Explicit Hierarchy = Precision context loading.** Hierarchy determines which rules could apply to a given task. Progressive Disclosure determines which of those rules actually load. Together, they produce an agent that receives exactly the guidance it needs — the right rules, at the right specificity level, loaded at the right time. Neither constraint alone achieves this. Hierarchy without progressive disclosure loads all rules at all levels. Progressive disclosure without hierarchy loads the right amount of context but cannot distinguish between domains.

**Reduced Scope + Orchestrated Composition = Reliable complex workflows.** Reduced Scope ensures each task fits in a context window. Orchestrated Composition chains those tasks into a sequence that accomplishes complex goals. A 70-file refactor is not one task — it is a planned sequence of scoped tasks, each composed from simple primitives. The scope constraint keeps each step reliable. The composition constraint keeps the sequence coherent.

**Safety Boundaries + Reduced Scope = Auditable agent behavior.** When an agent has a narrow task and explicit capability limits, every action it takes is inspectable. What did it change? Was it authorized to change it? Did it stay within its knowledge scope? An agent with a broad task and no boundaries produces output that is difficult to audit because the reviewer cannot determine what the agent should and should not have done.

The general pattern: each constraint addresses one failure mode, and each pair of constraints closes a gap that neither addresses alone.

---

## Applying the Constraints: A Worked Example

Consider a team adding JWT authentication to an existing application. Without PROSE constraints, this is a single task given to a single agent with all project documentation loaded.

With PROSE constraints applied:

**Explicit Hierarchy.** The team creates `backend/auth/AGENTS.md` with security-specific instructions: token signing algorithms, refresh token rotation policy, rate limiting requirements. These inherit from `backend/AGENTS.md` (API design patterns, error handling) and root `AGENTS.md` (naming conventions, commit format). The frontend agent adding the login form never sees the token rotation policy.

**Progressive Disclosure.** The auth instructions reference `[OWASP token best practices](./docs/security/owasp-tokens.md)` and `[existing session management](./src/services/session.ts)` by link, not by inline content. The agent loads these only when implementing the specific components that need them.

**Reduced Scope.** The work is decomposed: (1) design the token schema, (2) implement the middleware, (3) add the refresh endpoint, (4) write integration tests, (5) update the login form. Each is a separate session with fresh context.

**Orchestrated Composition.** The middleware task uses `backend-dev.chatmode.md` for the agent role, `auth.instructions.md` for domain rules, and `implement-from-spec.prompt.md` for the workflow. None of these primitives was written for this task — they compose to serve it.

**Safety Boundaries.** The backend agent has tools to modify `src/` and run tests. It cannot modify the frontend. It cannot deploy. It must present its middleware design for human approval before writing code.

The result is five focused sessions, each producing auditable output, each operating within explicit limits, none polluting the others with irrelevant context.

---

## Compliance Checklist

Use this checklist to evaluate whether your current setup satisfies PROSE constraints. A "no" answer identifies a specific gap to address.

| # | Constraint | Question | Pass |
|---|---|---|---|
| P1 | Progressive Disclosure | Do instruction files use links to deeper content rather than inlining everything? | |
| P2 | Progressive Disclosure | Can the agent assess relevance before loading detailed context? | |
| R1 | Reduced Scope | Is every agent task completable without mid-session scope expansion? | |
| R2 | Reduced Scope | Do multi-step workflows use fresh context per phase? | |
| O1 | Orchestrated Composition | Is each instruction file focused on a single concern? | |
| O2 | Orchestrated Composition | Do workflows compose existing primitives rather than restating their content? | |
| S1 | Safety Boundaries | Does every agent have an explicit tool whitelist? | |
| S2 | Safety Boundaries | Are human approval gates defined for high-risk operations? | |
| S3 | Safety Boundaries | Is knowledge scoped to relevant domains via `applyTo` or directory placement? | |
| E1 | Explicit Hierarchy | Do instructions exist at multiple specificity levels (global, domain, module)? | |
| E2 | Explicit Hierarchy | Can local rules override or extend global rules without editing the global file? | |

**12/12:** Fully PROSE-compliant. Your setup addresses all five failure modes.

**8–11:** Substantially compliant. Review the failing items — each represents a specific failure mode that is not yet addressed.

**4–7:** Partially compliant. The gaps are likely producing inconsistent agent behavior. Prioritize Safety Boundaries and Explicit Hierarchy — these have the highest impact on reliability.

**0–3:** Ad-hoc. Agent behavior is unpredictable because the structural constraints that produce reliability are not in place. Start with Explicit Hierarchy (it is the fastest to implement) and Reduced Scope (it requires no file changes, only discipline in how you assign tasks).

---

The five constraints are the specification. The chapters that follow — context engineering, agent primitives, execution, delegation — are the implementation. Every technique in those chapters traces back to one or more constraints defined here. When a technique works, it is because it satisfies the relevant constraint. When it fails, the constraint it violates tells you where to look.
