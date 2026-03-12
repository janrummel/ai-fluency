# AI Fluency — Design Spec

**Date:** 2026-03-12
**Status:** Final
**Author:** Jan Rummel + Claude

## Vision

AI Fluency is a comprehensive, open, and free learning journey that takes knowledge workers from casual AI chatting (L1) to designing their own AI orchestration systems (L7). It covers the full spectrum of AI usage maturity while offering parallel paths for different personas and a reference section inspired by Apple's Human Interface Guidelines.

## Problem Statement

Most knowledge workers today are stuck at L1/L2 — they chat with ChatGPT or Microsoft Copilot but don't leverage AI's full potential. The gap between "I chat with AI" and "I orchestrate AI systems" is enormous, spanning multiple paradigm shifts. No single learning resource currently covers this full spectrum in a structured, practical, and persona-aware way.

## Target Audience

All knowledge workers — from marketing professionals to developers to executives — who want to improve their AI fluency. The learning journey starts at L1 (casual chatting) and offers paths to different depth levels depending on the learner's role and ambition.

## Format & Platform

- **Tech Stack:** Astro + Starlight (proven pattern from AI Product Thinking and Level Up AI)
- **Languages:** Bilingual DE + EN (German as default locale)
- **Hosting:** GitHub Pages (free)
- **Content Format:** MDX with custom components
- **License:** Open and free
- **Monetization:** Optional donation button (e.g., Buy Me a Coffee) — legal/tax clarification pending

## Structure

### Overview

```
Gemeinsame Basis (L1-L4) → Pfade (Maker / Coworker / Leader) → Referenz
```

The learning journey has three layers:
1. **Shared Foundation (L1-L4):** Everyone goes through this. Tool-agnostic concepts with concrete examples in 2-3 tools per level. Each bullet point in the level descriptions represents a topic area that may span 1-2 lessons, not necessarily a single lesson. The exact lesson breakdown is determined during implementation planning.
2. **Paths after L4:** Three persona-specific tracks — Maker, Coworker, Leader.
3. **Reference Section (HIG-inspired):** Standalone, searchable, linked from lessons.

### Shared Foundation

#### L1: First Steps with AI
**Paradigm shift:** "AI is not Google"

- What is generative AI (without buzzwords, with analogies)
- ChatGPT, Claude, Gemini, Copilot — overview, no ranking
- First conversations — what works, what doesn't
- Understanding limits: hallucinations, knowledge cutoff, data privacy
- Do's & Don'ts: What to trust AI with and what not to

#### L2: Intentional Prompting
**Paradigm shift:** "From questions to instructions"

- Prompt anatomy: role, context, task, format, constraints
- Few-shot examples and chain-of-thought explained
- Iteration as method — the first output is a draft
- Different task types: writing, analyzing, summarizing, translating
- Do's & Don'ts: Good vs. bad prompts side by side

#### L3: Context as Infrastructure
**Paradigm shift:** "Invest once, benefit continuously"

- Claude Projects with custom instructions + knowledge files
- Building Custom GPTs
- Microsoft 365 Copilot in daily work
- Understanding and designing system prompts
- When persistent context pays off, when it doesn't
- Do's & Don'ts: Context design principles

#### L4: AI as Coworker
**Paradigm shift:** "From the text box to the task queue"

- Claude Cowork: setup, connectors, recurring tasks
- ChatGPT Agent Mode / Tasks
- Learning to delegate: What to delegate, what not
- Quality checking: AI output is not automatically correct
- Calibrating trust — when to verify, when to let run
- Agentic AI compliance (awareness level): liability basics, audit trails, human-in-the-loop
- Do's & Don'ts: Delegation anti-patterns

**Note on agentic AI compliance:** This topic appears at three depth levels: L4 (awareness — what to know as a user), Maker path (implementation — how to build compliant systems), and Reference/Regulation (full regulatory detail). Each level builds on the previous without repeating it.

### Paths After L4

All three paths are equally valid destinations after L4. No path is "higher" than another — they serve different goals.

#### Path: Maker
**For:** Technically interested people, developers, solo founders
**Estimated scope:** ~15-20 lessons across 3 modules

**Module: AI-Assisted Development**
- IDE integration: Cursor, Windsurf, GitHub Copilot — philosophies compared
- Claude Code: terminal agent, codebase context, edit/run/commit
- VS Code as a working environment
- Pair programming with AI — when it helps, when it hinders
- Git, GitHub, CLI basics (as needed)

**Module: Building Without Code**
- Lovable, Bolt, v0, Replit Agent — strengths and limits
- From idea to working app in natural language
- Understanding deployment (what happens when you click "publish")
- When no-code, when code, when both
- Design fundamentals from the HIG: Why UX matters, even for AI-built apps

**Module: Designing Your Own AI Systems**
- CLAUDE.md as a "constitution" for AI behavior
- Skills as reusable capabilities
- Memory architecture: short-term, mid-term, long-term
- Project state management
- MCP: What it is, why it matters
- Quality gates and verification
- Context engineering as a discipline
- Agentic AI in enterprise: compliance, governance, audit trails

#### Path: Coworker
**For:** Knowledge workers who want to maximize AI integration without coding
**Estimated scope:** ~10-15 lessons across 3 modules

**Module: Cowork Mastery**
- Advanced connector usage (Slack, Notion, Drive, CRM)
- Multi-tool workflows: chaining connectors for complex tasks
- Recurring tasks: setup, monitoring, refinement
- Troubleshooting: when automation breaks or produces bad output

**Module: Productivity Systems**
- Building your own prompt libraries and templates
- AI in meetings: preparation, notes, follow-ups
- AI in documentation: drafting, reviewing, maintaining
- AI in communication: email, reports, presentations

**Module: Team Enablement**
- Helping colleagues get started (peer coaching)
- Sharing best practices within the organization
- Building team-wide prompt libraries and standards
- Measuring and communicating AI impact

#### Path: Leader
**For:** Executives, decision makers, strategists
**Estimated scope:** ~10-15 lessons across 3 modules

**Module: AI Strategy**
- Build vs. buy: When to adopt tools, when to build custom
- Vendor selection: Evaluation criteria, proof of concepts
- ROI assessment: Measuring AI impact beyond "time saved"
- AI readiness: Assessing organizational maturity

**Module: Governance & Compliance**
- EU AI Act: Risk classes, obligations, timeline for enterprises
- Data privacy: GDPR implications for AI tool usage
- Agentic AI compliance: Liability when agents act autonomously, approval processes, data access governance
- Risk management: Frameworks for responsible AI deployment

**Module: Culture & Enablement**
- Driving adoption: From "am I allowed to?" to "how do we do this right?"
- Understanding resistance: Why people hesitate, how to address it
- Responsibility: Who is liable when AI makes mistakes
- Building AI fluency across the organization

### Reference Section (HIG-Inspired)

Each entry is self-contained — understandable without having completed the learning journey.

#### Glossary (A-Z)
- Every technical term used in the learning journey, explained
- Short, clear, with context ("where you'll encounter this")
- Tooltips in lessons link here
- Examples: Prompt, Token, Context Window, Hallucination, RAG, Fine-Tuning, MCP, LLM, Agent, System Prompt, API, SDK, IDE, CLI, etc.

#### Principles
- Design fundamentals from Apple HIG (adapted for AI context): Clarity, Consistency, Feedback, Accessibility
- UX principles for AI products: Transparency, controllability, error tolerance
- Prompt design principles: Specificity, context, iteration
- Each principle with Do's & Don'ts and visual examples

#### Regulation
- EU AI Act: Risk classes, obligations, timeline — explained practically
- GDPR in the AI context: What can be uploaded, what can't
- Copyright: AI-generated content, training data debate
- Agentic AI in enterprise: Compliance requirements for autonomous systems, human-in-the-loop mandates, audit trail requirements
- Industry-specific where relevant (healthcare, finance)

#### Ethics
- Bias and fairness: Where bias comes from, how to recognize it
- Transparency: Labeling AI-generated content
- Responsibility: Humans remain responsible — what that means practically
- Sustainability: Energy consumption, resources

#### Tool Catalog
- Explicitly marked as **ephemeral** — date stamp on every entry
- Categorized by level (L1 tools, L4 tools, etc.)
- Per tool: What it can do, what it costs, for whom, alternatives
- No ranking, but classification

## Lesson Pattern

Every lesson across all levels and paths follows this structure:

| Element | Description |
|---------|-------------|
| **What & Why** | Concept + relevance, max 3-4 sentences |
| **How It Works** | Explanation with visual examples, screenshots, diagrams |
| **Do's & Don'ts** | HIG-style, visually juxtaposed |
| **Try It** | Practical exercise the learner can do immediately |
| **Think Further** | Reflection question, connection to the next topic |

## Navigation & Orientation

- **Progress indicator** in the shared foundation (L1-L4)
- **Path selection** after L4: Explanation of which path is for whom, with self-assessment
- **Cross-references** between lessons and reference section via tooltips and links
- **Level assessment** on the landing page: "Where do you stand?" — simple self-test leading to the right entry point

## Visual Design

- Apple HIG as style reference: Generous whitespace, clear typography, Do/Don't cards
- Diagrams as generated SVGs (leveraging lessons from Level Up AI)
- Tool screenshots where necessary, with ephemeral notice
- Bilingual: English technical terms stay English in German text

## Differentiation from Existing Projects

| Project | Focus | Target Audience |
|---------|-------|----------------|
| **AI Product Thinking** | PM discipline with AI | Product Managers |
| **Level Up AI** | AI Engineering Skills | Developers |
| **AI Fluency** | AI usage from 0 to 100 | All knowledge workers |

The three projects complement each other — AI Fluency is the broadest entry point, from which learners can branch into the specialized projects.

## Quality & Research

- Systematic research before writing any lesson (research-pipeline skill)
- Sources cited and evaluated (peer-reviewed > official docs > preprint > blog > claim)
- Quality gates on all outputs (signal-check, challenge)
- Agentic AI compliance content reviewed against current EU AI Act text and enterprise governance frameworks

## Phasing Plan

The project scope is significantly larger than either prior project. To ensure shippable increments:

| Phase | Scope | Estimated Size | Shippable? |
|-------|-------|---------------|------------|
| **Phase 1 (MVP)** | L1-L4 + Glossary skeleton + Landing page with level assessment | ~25-30 DE lessons + EN | Yes — covers the biggest gap (L1→L4) |
| **Phase 2** | Maker path (3 modules) + Principles reference | ~15-20 DE lessons + EN | Yes — adds technical depth |
| **Phase 3** | Coworker + Leader paths | ~20-30 DE lessons + EN | Yes — completes all paths |
| **Phase 4** | Full reference section (Regulation, Ethics, Tool Catalog) | ~15-25 DE pages + EN | Yes — completes the reference |

**Total estimate:** ~80-110 DE pages, ~160-220 pages including EN translation.

Each phase is a complete, valuable product on its own. No phase depends on a later phase being completed.

## Content Volume Estimate

| Component | Estimated DE Lessons/Pages |
|-----------|---------------------------|
| L1-L4 (shared foundation) | ~20-25 |
| Maker path | ~15-20 |
| Coworker path | ~10-15 |
| Leader path | ~10-15 |
| Reference section | ~15-25 |
| Landing, navigation, meta pages | ~3-5 |
| **Total DE** | **~80-110** |
| **Total with EN** | **~160-220** |

## Content Maintenance

- Every lesson and reference entry carries a **"Last reviewed"** date
- The Tool Catalog is reviewed **quarterly** (tools change fast)
- Level content (L1-L4) is reviewed **biannually** (concepts are more stable)
- Regulation content is reviewed when **major regulatory milestones** occur (EU AI Act enforcement dates)
- Screenshots of tools are marked as ephemeral and replaced during reviews

## Cross-Project Linking

AI Fluency links to the specialized projects at natural branching points:

| From | To | Context |
|------|----|---------|
| Maker path → AI-Assisted Development | **Level Up AI** | "Go deeper into AI engineering skills" |
| Leader path → AI Strategy | **AI Product Thinking** | "Learn the full PM discipline for AI products" |
| L3 → System Prompts | **claude-orchestrator-starter** | "See a real-world orchestrator setup" |

Links are explicit "Go Deeper" callouts, not inline. Each linked project has a brief description so learners know what to expect.

## Accessibility

- Starlight's built-in accessibility features (semantic HTML, keyboard navigation, screen reader support) as baseline
- Custom components (tooltips, Do/Don't cards, progress indicator) must meet WCAG 2.1 AA
- All diagrams have alt text
- Color is never the only way to convey information (Do's & Don'ts use icons + color)

## SEO & Discoverability

- Meta descriptions for every page
- OpenGraph / social sharing cards
- Structured lesson titles for search ("AI Fluency — L2: Intentional Prompting")
- Custom domain considered for later (initially `janrummel.github.io/ai-fluency`)

## Open Questions

- Landing page level assessment: Format and question design (deferred to implementation)
- Interactive components scope (glossary tooltips vs. embedded AI chat — start minimal, extend later)
- Donation button platform and legal setup (deferred until content is live)
- Contributor model: Solo-authored initially, contributor guidelines added if demand arises
- Project name for the GitHub repo: `ai-fluency`

## Technical Notes

- Astro + Starlight with MDX
- Default locale: `de`, secondary: `en`
- GitHub Pages deployment with GitHub Actions
- Custom components: Glossary tooltips, Do/Don't cards, progress indicator
- SVG diagram generation (pattern from Level Up AI)
- Optional later: Giscus (GitHub Discussions), Plausible analytics, Sandpack embeds
