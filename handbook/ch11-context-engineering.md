# Chapter 11: Context Engineering

You have a codebase with 200,000 lines of code, a style guide nobody reads, three authentication patterns (two deprecated), and a logging convention that exists in the heads of two senior engineers who joined in 2019. An AI agent sees none of this. It sees whatever fits in its context window. Context engineering is the discipline of deciding what that is.

---

## The Context Budget

Every AI interaction operates within a fixed capacity. A context window is not a bucket you fill — it is a budget you allocate. Like any budget, the question is not "how much can I spend?" but "what do I spend it on?"

A typical agent session divides its context roughly as follows:

```
┌──────────────────────────────────────────────────┐
│  System prompt          ~5-10%                   │
│  (model behavior, safety, base instructions)     │
├──────────────────────────────────────────────────┤
│  Instructions & rules   ~15-25%                  │
│  (project conventions, scoped guidance)           │
├──────────────────────────────────────────────────┤
│  Code context           ~30-50%                  │
│  (source files, dependencies, types)             │
├──────────────────────────────────────────────────┤
│  Conversation history   ~20-30%                  │
│  (prior turns, agent reasoning, tool output)     │
├──────────────────────────────────────────────────┤
│  Working memory         remainder                │
│  (the agent's space to think and produce output) │
└──────────────────────────────────────────────────┘
```

You control two of these segments directly: instructions and code context. You influence a third — conversation history — through session discipline. The system prompt and working memory are largely fixed by the tool. This means your leverage is concentrated: what instructions load, which code is visible, and how long the session runs before you reset.

The budget model produces a simple decision rule. Before adding anything to an agent's context, ask: does this earn its space? Every instruction that loads is a line of code that doesn't. Every file that's visible is one that could have been more relevant. Context is not free, and attention within the window is not uniform — information at the beginning and end gets more weight; content in the middle degrades. This is not a theoretical concern. It is why a 40-line instruction file outperforms a 400-line one that covers the same material with less focus.

Two practical implications follow. First, shorter sessions produce better results than longer ones, because conversation history consumes progressively more of the budget. When a session has been running for 30 turns, the instructions you set at the beginning are competing with pages of accumulated dialogue. Second, loading instructions that aren't relevant to the current task is not neutral — it actively degrades performance on the task that matters.

## The Instruction Hierarchy

The most consequential context engineering decision is how you structure your instructions. The naive approach is a single document — one large file containing every convention, pattern, and constraint your team follows. This is the "flat instructions" anti-pattern, and it fails for the same reason a single 800-page employee handbook fails: nobody reads the chapter on database conventions when they're fixing a CSS bug, and neither does an agent. Worse, the agent can't skip sections — it loads everything, diluting its attention on what matters.

The solution is a hierarchy: instructions that increase in specificity as scope narrows, from project-wide to directory-level to file-level. Each layer loads only when relevant.

### Global scope: project-wide principles

The top layer defines principles that apply everywhere. These are your team's non-negotiable constraints — the things that are true regardless of which file an agent is editing.

```markdown
# Project Principles

## Error Handling
- All public API functions return Result types, never throw exceptions
- Log errors at the boundary where they're caught, not where they originate

## Security
- No credentials in source code. Use environment variables or secret managers.
- All user input is validated at the API boundary before reaching business logic.

## Testing
- Every public function has at least one test. No exceptions.
- Tests use the factory pattern for test data. No inline object construction.
```

Global instructions should be short. If your project-wide principles exceed 50 lines, you are almost certainly including domain-specific guidance that belongs in a narrower scope.

### Directory scope: domain-specific rules

The middle layer targets specific areas of the codebase. When an agent edits a file in `src/auth/`, it loads the auth-specific instructions. When it edits `src/frontend/`, it loads frontend rules. Neither set pollutes the other.

```markdown
# Authentication Module Rules
applyTo: "src/auth/**"

## Token Management
- All token operations go through AuthResolver. Never access tokens directly.
- Token refresh uses exponential backoff with a maximum of 3 retries.
- EMU (Enterprise Managed User) tokens use the standard `ghu_` prefix.

## Patterns
- Use the CredentialChain pattern for multi-source credential resolution.
- Order: environment variable → credential file → interactive prompt.
```

The `applyTo` pattern is the mechanism. When the agent's task involves files matching that glob, the instructions load. When it doesn't, they stay out of the context window. This is progressive disclosure at the instruction level — context arrives just-in-time, not just-in-case.

### File scope: surgical constraints

The narrowest layer targets specific files or file types. This is where you encode the knowledge that would otherwise require reading a file's git history to understand.

```markdown
# Integration Architecture
applyTo: "src/integration/**"

## Required structure
Every integrator MUST extend BaseIntegrator and return IntegrationResult.

## Base-class methods — use, don't reimplement
| Operation          | Use                          | Never                    |
|--------------------|------------------------------|--------------------------|
| Collision detection| self.check_collision()       | Custom existence checks  |
| File discovery     | self.find_files_by_glob()    | Ad-hoc os.walk           |
| Path validation    | BaseIntegrator.validate_path()| Inline "../" checks      |
```

This is the knowledge that a new human engineer would learn in their second week, after a senior teammate says "we don't do it that way here." The agent never has a second week. It needs this on day one, every time.

### How the hierarchy composes

When an agent edits `src/auth/token_resolver.py`, the effective context is:

1. Global principles (error handling, security, testing)
2. Auth module rules (token management, credential chain)
3. Any file-specific constraints matching `src/auth/token_*.py`

When the same agent later edits `src/frontend/dashboard.tsx`, the auth rules unload and frontend rules load. The global principles persist. This is the Explicit Hierarchy constraint in action: specificity increases as scope narrows, and irrelevant context is automatically excluded.

The practical benefit is measurable. A project with 300 lines of instructions split across 8 scoped files will produce more consistent agent output than a project with 100 lines in a single global file. The split version loads 30-50 relevant lines per task; the monolithic version loads all 100 regardless of relevance.

## Agent Configuration

Instructions tell agents what rules to follow. Agent configurations tell them who to be. The distinction matters because different tasks require different expertise, judgment, and constraints.

An agent configuration defines four things:

1. **Role and expertise.** What domain knowledge the agent brings to every task. An architecture agent knows about module boundaries and dependency management. A security agent knows about injection vectors and credential handling.
2. **Model selection.** Which language model runs the agent. Complex architectural decisions may warrant a more capable (and more expensive) model. Routine formatting tasks don't.
3. **Behavioral constraints.** What the agent prioritizes when making trade-offs. An agent configured with "KISS — simplest correct solution" makes different choices than one configured with "optimize for performance."
4. **Anti-patterns.** What the agent should never do. This is often more valuable than positive instructions, because it prevents the specific mistakes your team has seen before.

```yaml
# .github/agents/python-architect.agent.md
---
name: python-architect
description: >-
  Expert on Python design patterns, modularization, and scalable
  architecture. Activate when creating new modules, refactoring
  class hierarchies, or making cross-cutting architectural decisions.
model: claude-sonnet-4.5
---

# Python Architect

You are an expert Python architect specializing in CLI tool design.

## Design Philosophy
- Speed and simplicity over complexity
- Solid foundation that can be iterated on
- Pay only for what you touch — operations proportional to affected files

## Patterns You Enforce
- BaseIntegrator for all file-level integrators
- CommandLogger for all CLI output
- AuthResolver for all credential access

## You Never
- Add a new base class when an existing one can be extended
- Instantiate AuthResolver per-request (it's a singleton)
- Import from integration/ in the CLI layer (use the public API)
```

The "You Never" section is where institutional memory becomes operational. Every item in that list represents a mistake that happened at least once — possibly caught in code review, possibly caught in production. Encoding it in the agent configuration means it doesn't happen again, regardless of which human or AI writes the next change.

For a typical project, three to five agent configurations cover most tasks: an architect (structure and patterns), a domain expert (your core business logic), a documentation writer, and optionally a security reviewer and a test specialist. Start with fewer. Add agents when you observe the same correction being made repeatedly — that's the signal that a new specialization has earned its place.

## Skill Design

Skills occupy the space between instructions and agents. An instruction says "follow this rule." An agent says "be this expert." A skill says "when you encounter this situation, here's the complete playbook."

A skill is a reusable knowledge package that activates based on code patterns. When an agent touches logging code, the logging skill fires. When it touches authentication flows, the auth skill fires. The agent doesn't choose to activate a skill — the tooling detects the match and loads it.

The design test for a skill is: does this knowledge apply across multiple files, require more than a few rules to express, and get triggered by a detectable pattern? If all three are true, it's a skill. If the knowledge applies to one file, it's an instruction. If it's a general approach rather than pattern-specific guidance, it belongs in an agent configuration.

A well-designed skill has three sections:

```markdown
# CLI Logging UX Skill

## When This Activates
Code touches console helpers, DiagnosticCollector,
STATUS_SYMBOLS, or any user-facing terminal output.

## Decision Framework
1. The "So What?" Test — every warning must answer:
   what should the user do about this?
2. The Traffic Light Rule:
   | Color  | Helper           | Meaning            |
   |--------|------------------|--------------------|
   | Green  | _rich_success()  | Completed          |
   | Yellow | _rich_warning()  | User action needed |
   | Red    | _rich_error()    | Cannot continue    |
   | Blue   | _rich_info()     | Status update      |
3. The Newspaper Test — can the user scan output like headlines?

## Anti-Patterns
- Never use bare print() or click.echo() without styling
- Never emit a warning without an actionable suggestion
- Never mix Rich and colorama in the same output path
```

The decision framework is what distinguishes a skill from a list of rules. Rules tell you what to do. A decision framework tells you how to think about the problem, which means it generalizes to situations the author didn't anticipate.

Skills vs. one-off instructions: if you find yourself writing the same instructional content in three different instruction files, extract it into a skill. The instruction files then reference the skill by name rather than duplicating the content. This mirrors the same DRY principle you apply to code — and for the same reason. When the logging convention changes, you update one skill file instead of hunting through every instruction that mentions logging.

## Memory and Retrieval

Agents are stateless. Every session starts with an empty context window, and every session's accumulated knowledge vanishes when it ends. This is a fundamental constraint, not a bug to work around.

Three strategies address it.

**Session context.** Within a single session, the agent accumulates information through conversation turns. Tool outputs, file reads, and your corrections all become part of the working context. This is the most natural form of memory, and the most fragile — it degrades as the session grows, and it disappears when the session ends. Session discipline means recognizing when the accumulated context has grown large enough to dilute the instructions. At that point, start a fresh session. Carry forward the relevant findings; leave the exploration history behind.

**Persistent instructions.** The instruction hierarchy described above is a form of persistent memory. It survives across sessions because it lives in files, not in conversation history. When you correct an agent's mistake and then update the instruction file that led to the mistake, you've converted session knowledge into persistent knowledge. This is the feedback loop: observe failure, diagnose root cause, fix the primitive, verify on the next task. Over time, this accumulation is what makes your codebase increasingly AI-ready.

**External knowledge retrieval.** For codebases too large to fit relevant context in the window, retrieval mechanisms — code search, semantic index, documentation search — bring specific information into context on demand. The agent requests what it needs rather than having everything preloaded. This is progressive disclosure at the knowledge level. The practical implementation varies by tool: some offer built-in retrieval, others use tool calls to search, and some require you to structure your codebase so that relevant information is co-located with the files that need it. The principle is consistent: give the agent a way to pull specific knowledge rather than pushing everything.

Co-location deserves specific attention. If your authentication logic is in `src/auth/` and your authentication documentation is in `docs/auth-guide.md`, an agent working on auth code may never see the documentation unless explicitly pointed to it. If instead the module-level README or instruction file references the key decisions — or better, if the decisions are encoded as scoped instructions — the knowledge is available where it's needed. Structure your repository so that the knowledge an agent needs is either scoped to the directory it's working in or discoverable through the instruction hierarchy. This is an architectural choice, not a tooling choice.

The decision of what to externalize vs. what to keep in instructions follows a simple rule: if the knowledge is needed on every task in a given scope, it goes in instructions (it's always loaded). If the knowledge is needed occasionally, it goes in retrievable storage (it's loaded on demand). If the knowledge is needed once, it lives in the session prompt.

## The Context Audit

Before you write your first instruction file, you need to know what knowledge your codebase depends on and where it currently lives. This is the context audit — a systematic assessment of the gap between what your team knows and what an agent can see.

**Step 1: List your conventions.** Take 30 minutes with your team and write down every convention, pattern, and constraint that a new engineer would need to learn in their first two weeks. Error handling patterns. Naming conventions. Module boundaries. Authentication flows. Deployment requirements. Testing conventions. Which base classes to extend. Which methods are deprecated but not yet removed. Which directories own which concerns. Don't filter. Don't organize. Just list.

You'll typically get 30-60 items. Most teams are surprised by the volume. If you get fewer than 15, you're either working on a very small project or you're not being thorough enough.

**Step 2: Classify each item.** For every convention on your list, mark where it currently lives:

| Location | What it means |
|----------|---------------|
| **In code** | Expressed in the implementation itself (types, naming, structure) |
| **In docs** | Written down somewhere — README, wiki, ADR, style guide |
| **In heads** | Known by team members but never documented |

The "in heads" column is your context debt. These are the conventions an agent will violate because it has no way to know about them. They are also the conventions most likely to cause the kind of subtle, plausible-looking failures described in Chapter 1 — code that compiles, passes basic tests, and silently breaks an invariant.

**Step 3: Prioritize by failure cost.** Not every convention is equally important. Rank your context debt by what happens when it's violated:

- **Critical:** Security vulnerabilities, data corruption, production outages
- **High:** Architectural violations that create technical debt
- **Medium:** Convention violations that require rework in review
- **Low:** Style preferences that don't affect correctness

**Step 4: Map to instruction scope.** For each critical and high-priority item, determine where it belongs in the hierarchy:

- Applies everywhere → global instruction
- Applies to a specific module → directory-scoped instruction
- Requires a decision framework → skill
- Needs a specialist perspective → agent configuration

**Step 5: Write your starter set.** Begin with 3-5 instruction files covering your critical items. Don't aim for completeness. The feedback loop — observe agent output, identify what went wrong, improve the primitive — will guide you to what's actually needed. Most teams over-engineer their first attempt and under-engineer what actually matters.

## Before and After

Consider a concrete task: "Add rate limiting to the `/api/users` endpoint."

**Without structured context**, the agent sees the endpoint file and whatever the tool's default context provides. It produces:

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/users')
@limiter.limit("100/hour")
def get_users():
    ...
```

This looks reasonable. It also violates three conventions that exist only in the team's heads: the project uses a custom rate limiter that integrates with the metrics pipeline, rate limit configuration lives in the environment (not hardcoded), and all middleware decorators are applied in `middleware.py`, not inline on routes.

**With structured context**, the agent loads:

- A global instruction requiring all middleware to be registered in `middleware.py`
- A directory-scoped instruction for `src/api/` that references the custom rate limiter and environment-based configuration
- A skill for API middleware that includes the registration pattern

The agent produces:

```python
# middleware.py
from app.rate_limiter import RateLimiter

rate_limiter = RateLimiter.from_env("API_RATE_LIMIT_USERS")
rate_limiter.register("/api/users", methods=["GET"])
```

```python
# No changes to the route file — middleware is external
```

Same model. Same task. Different output. The difference is entirely in what the agent knew before it started.

This pattern repeats across every category of work. Adding a new API endpoint without context produces generic boilerplate; with context, it follows the project's existing patterns for validation, error response format, and middleware registration. Writing a test without context produces isolated assertions; with context, it uses the project's test factories, follows the naming convention, and respects the fixture hierarchy. Modifying a configuration file without context produces plausible syntax; with context, it respects the deployment pipeline's expectations about which values come from environment variables vs. which are hardcoded.

The critical point is that none of these failures are model failures. The model is capable of doing the right thing in every case. It does the wrong thing because it lacks the information. Context engineering closes that gap.

## Common Mistakes

**Over-stuffing context.** The instinct to provide more information is strong and almost always counterproductive. A 400-line instruction file doesn't give the agent "more to work with." It gives it more to get distracted by. Instructions should be the minimum sufficient guidance for their scope. If you can't remember what's in your instruction file without re-reading it, the agent is having the same problem.

**Flat instructions without scoping.** A single global instruction file that covers everything — API conventions, frontend patterns, database rules, deployment procedures — forces every agent session to load every rule. The backend agent spends context budget on frontend rules. The documentation agent loads database conventions. Scope your instructions. If an instruction doesn't apply to the current task, it shouldn't be in the context window.

**Duplicating knowledge across files.** When the same convention appears in three different instruction files, you've created a maintenance problem. When the convention changes, you update one file and forget the others. The agent gets contradictory guidance and produces inconsistent output. Extract shared knowledge into skills. Reference, don't repeat.

**Mixing concerns in a single primitive.** An instruction file that covers both "how to write error messages" and "how to structure database migrations" is serving two unrelated domains. When either domain changes, you risk destabilizing the other. One concern per primitive. This mirrors the single-responsibility principle in code, and for the same reasons.

**Ignoring the feedback loop.** Writing instruction files once and never updating them is like writing tests once and never running them. The value of context engineering compounds through iteration: agent makes a mistake, you trace it to a context gap, you fix the primitive, the mistake doesn't recur. Teams that skip this loop find their context artifacts drift from reality within weeks.

**Treating context engineering as a one-time setup.** It is not. It is a continuous discipline, like testing or code review. Your codebase evolves. Your conventions evolve. Your context artifacts must evolve with them. Budget time for primitive maintenance the way you budget time for dependency updates — small, regular investments that prevent large, painful corrections.

---

## The Minimal Viable Context

If the audit feels like a large undertaking, start smaller. The minimum viable context for any project is three files:

| File | Scope | Contains |
|------|-------|----------|
| Global instructions | Project-wide | 5-10 non-negotiable principles (error handling, security, testing) |
| One domain instruction | Your most-edited module | The patterns and constraints specific to where agents will work most |
| One agent configuration | Your most common task type | The expertise and behavioral constraints for the work agents do daily |

Write these three files. Use the agent on a real task. Observe what goes wrong. Fix the primitives. Repeat. In two weeks you'll have a context architecture that's shaped by actual failure modes rather than theoretical completeness — and that architecture will be more effective than any comprehensive upfront design.

Context engineering is not about making agents smarter. It is about making the information available to agents accurate, relevant, and proportional to the task. The model doesn't change. The context does. And that is where the leverage is.
