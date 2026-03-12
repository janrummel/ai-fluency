# AI Fluency — Phase 1 (MVP) Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a bilingual (DE+EN) learning journey covering L1-L4 (from casual AI chatting to AI as coworker) with a glossary skeleton and landing page, hosted on GitHub Pages.

**Architecture:** Astro + Starlight static site, identical stack to ai-product-thinking and level-up-ai. Content in MDX, i18n via Starlight's built-in locale routing, custom CSS for HIG-inspired visual design. Custom components for Do/Don't cards and glossary tooltips.

**Tech Stack:** Astro 5.x, @astrojs/starlight, sharp, MDX, GitHub Actions for deployment.

**Spec:** `docs/superpowers/specs/2026-03-12-ai-fluency-design.md`

**Scope:** Phase 1 only — L1-L4 shared foundation + glossary skeleton + landing page. Paths (Maker/Coworker/Leader) and full reference section are Phase 2+.

---

## Important Conventions

**i18n directory names:** Both `de/` and `en/` use **identical directory and file names** (English names). This is required by Starlight's `autogenerate` sidebar — it resolves one directory name for all locales. This matches the pattern from ai-product-thinking and level-up-ai.

**Content quality:** Every page MUST have `title` and `description` in frontmatter (Starlight uses these for OpenGraph/SEO automatically). After completing each level's content (DE+EN), run a quality check: verify lesson pattern consistency, factual accuracy, and completeness against spec topics.

**Translations:** Not literal — adapt examples and cultural references where needed. Keep the same structure, components, and Try It exercises. German text uses English technical terms inline (Prompt, Token, Agent — not translated).

**Progress indicator:** Each lesson includes a simple text note at the top: `> Lektion 3 von 5 — L1: Erste Schritte` (DE) / `> Lesson 3 of 5 — L1: First Steps` (EN). No custom component needed for MVP.

**No screenshots in MVP.** Tool-specific lessons describe UIs in text. Screenshots are ephemeral and will be added in a maintenance pass.

---

## File Structure

```
ai-fluency/
├── .gitignore
├── astro.config.mjs
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── content.config.ts
│   ├── content/docs/
│   │   ├── index.mdx                          # Root redirect
│   │   ├── de/                                # SAME directory names as en/
│   │   │   ├── start/
│   │   │   │   ├── index.mdx                  # Landing page (splash)
│   │   │   │   └── level-check.mdx            # Self-assessment
│   │   │   ├── l1-first-steps/
│   │   │   │   ├── 01-what-is-ai.mdx
│   │   │   │   ├── 02-tools-overview.mdx
│   │   │   │   ├── 03-first-conversations.mdx
│   │   │   │   ├── 04-understanding-limits.mdx
│   │   │   │   └── 05-dos-and-donts.mdx
│   │   │   ├── l2-intentional-prompting/
│   │   │   │   ├── 01-prompt-anatomy.mdx
│   │   │   │   ├── 02-prompting-techniques.mdx
│   │   │   │   ├── 03-iteration-as-method.mdx
│   │   │   │   ├── 04-task-types.mdx
│   │   │   │   └── 05-good-vs-bad-prompts.mdx
│   │   │   ├── l3-context-infrastructure/
│   │   │   │   ├── 01-persistent-context.mdx
│   │   │   │   ├── 02-claude-projects.mdx
│   │   │   │   ├── 03-custom-gpts.mdx
│   │   │   │   ├── 04-m365-copilot.mdx
│   │   │   │   └── 05-system-prompt-design.mdx
│   │   │   ├── l4-ai-coworker/
│   │   │   │   ├── 01-from-chat-to-delegation.mdx
│   │   │   │   ├── 02-claude-cowork.mdx
│   │   │   │   ├── 03-chatgpt-agent-mode.mdx
│   │   │   │   ├── 04-calibrating-trust.mdx
│   │   │   │   └── 05-compliance-basics.mdx
│   │   │   └── reference/
│   │   │       └── glossary.mdx
│   │   └── en/                                # SAME directory names as de/
│   │       ├── start/
│   │       ├── l1-first-steps/
│   │       ├── l2-intentional-prompting/
│   │       ├── l3-context-infrastructure/
│   │       ├── l4-ai-coworker/
│   │       └── reference/
│   ├── components/
│   │   ├── DosDonts.astro                      # HIG-style Do/Don't cards
│   │   └── GlossaryTip.astro                   # Tooltip linking to glossary
│   └── styles/
│       └── custom.css                          # HIG-inspired design system
├── .github/
│   └── workflows/
│       └── deploy.yml
└── docs/
    ├── research/                               # Working artifacts, not in build
    │   ├── l1-research.md
    │   ├── l2-research.md
    │   ├── l3-research.md
    │   └── l4-research.md
    └── superpowers/
        ├── specs/2026-03-12-ai-fluency-design.md
        └── plans/2026-03-12-ai-fluency-phase1-mvp.md
```

---

## Chunk 1: Project Scaffolding & Technical Foundation

### Task 1: Initialize Astro + Starlight Project

**Files:**
- Create: `.gitignore`
- Create: `package.json`
- Create: `astro.config.mjs`
- Create: `tsconfig.json`
- Create: `src/content.config.ts`

- [ ] **Step 1: Create .gitignore**

```
dist/
.astro/
node_modules/
npm-debug.log*
.env
.env.production
.DS_Store
```

- [ ] **Step 2: Create package.json**

```json
{
  "name": "ai-fluency",
  "type": "module",
  "version": "0.1.0",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/starlight": "^0.37.7",
    "astro": "^5.6.1",
    "sharp": "^0.34.2"
  }
}
```

- [ ] **Step 3: Create tsconfig.json**

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}
```

- [ ] **Step 4: Create src/content.config.ts**

```typescript
import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};
```

- [ ] **Step 5: Create astro.config.mjs**

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const site = process.env.GITHUB_ACTIONS
  ? 'https://janrummel.github.io'
  : 'http://localhost:4321';

const base = process.env.GITHUB_ACTIONS ? '/ai-fluency' : '';

export default defineConfig({
  site,
  base,
  redirects: {
    '/': `${base}/de/start/`,
    '/de/': `${base}/de/start/`,
    '/en/': `${base}/en/start/`,
  },
  integrations: [
    starlight({
      title: 'AI Fluency',
      defaultLocale: 'de',
      locales: {
        de: { label: 'Deutsch', lang: 'de' },
        en: { label: 'English', lang: 'en' },
      },
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Start',
          translations: { de: 'Start' },
          items: [{ slug: 'start' }, { slug: 'start/level-check' }],
        },
        {
          label: 'L1 — First Steps',
          translations: { de: 'L1 — Erste Schritte' },
          autogenerate: { directory: 'l1-first-steps' },
        },
        {
          label: 'L2 — Intentional Prompting',
          translations: { de: 'L2 — Bewusst Prompten' },
          autogenerate: { directory: 'l2-intentional-prompting' },
        },
        {
          label: 'L3 — Context as Infrastructure',
          translations: { de: 'L3 — Kontext als Infrastruktur' },
          autogenerate: { directory: 'l3-context-infrastructure' },
        },
        {
          label: 'L4 — AI as Coworker',
          translations: { de: 'L4 — AI als Coworker' },
          autogenerate: { directory: 'l4-ai-coworker' },
        },
        {
          label: 'Reference',
          translations: { de: 'Referenz' },
          autogenerate: { directory: 'reference' },
        },
      ],
    }),
  ],
});
```

- [ ] **Step 6: Install dependencies and verify build**

Run: `cd /Users/janrummel/Projects/ai-fluency && npm install`
Run: `npm run build`
Expected: Build succeeds (may warn about missing content, that's fine)

- [ ] **Step 7: Commit**

```bash
git add .gitignore package.json tsconfig.json astro.config.mjs src/content.config.ts
git commit -m "feat: initialize Astro + Starlight project with i18n config"
```

---

### Task 2: Create Custom CSS (HIG-Inspired Design System)

**Files:**
- Create: `src/styles/custom.css`

Design tokens and styles inspired by Apple HIG: generous whitespace, clean typography, muted color palette. Light and dark mode support.

- [ ] **Step 1: Create the CSS file with design tokens and base overrides**

The CSS should include:
- Color tokens: `--af-bg`, `--af-text`, `--af-accent` (a professional blue, not orange like level-up-ai), `--af-border`, `--af-surface`, `--af-success` (green for Do's), `--af-danger` (red for Don'ts)
- Light and dark mode via `:root[data-theme='light']` and `:root[data-theme='dark']`
- Override Starlight CSS vars (`--sl-color-*`, `--sl-text-*`) to match HIG aesthetics
- Generous whitespace on headings and sections
- Clean, readable body text (larger line-height than default)
- Styled blockquotes for callouts (used for progress indicators)
- Table styling consistent with HIG
- Sidebar styling

Key visual goals:
- More whitespace than both existing projects
- Professional, not playful (no emojis in section markers, unlike level-up-ai)
- Color accent used sparingly — primarily for links and interactive elements
- Visual target: Apple HIG pages (e.g., developer.apple.com/design/human-interface-guidelines/color)

- [ ] **Step 2: Verify dev server renders with custom styles**

Run: `npm run dev`
Check: `http://localhost:4321` loads with custom styling applied

- [ ] **Step 3: Commit**

```bash
git add src/styles/custom.css
git commit -m "feat: add HIG-inspired custom CSS design system"
```

---

### Task 3: Create Custom Components

**Files:**
- Create: `src/components/DosDonts.astro`
- Create: `src/components/GlossaryTip.astro`

#### 3a: Do's & Don'ts Component

- [ ] **Step 1: Create DosDonts.astro**

An Astro component that renders side-by-side Do and Don't cards in HIG style. Usage in MDX:

```mdx
import DosDonts from '../../../components/DosDonts.astro';

<DosDonts
  dos={[
    "Give AI a clear role and context",
    "Specify the desired output format",
    "Iterate on the first result"
  ]}
  donts={[
    "Expect perfect output on the first try",
    "Share sensitive personal data",
    "Trust AI output without verification"
  ]}
/>
```

Implementation:
- Two-column layout (stacks on mobile)
- Green header/icon for Do's, red for Don'ts
- Checkmark icon for Do's, X icon for Don'ts (SVG inline, plus color — never color alone)
- Clean card styling with subtle border, no heavy shadows
- Accessible: icons are decorative (aria-hidden), text carries meaning

- [ ] **Step 2: Test in a scratch MDX page, then delete the test page**

- [ ] **Step 3: Commit**

```bash
git add src/components/DosDonts.astro
git commit -m "feat: add HIG-style Do's & Don'ts component"
```

#### 3b: Glossary Tooltip Component

- [ ] **Step 4: Create GlossaryTip.astro**

An Astro component that renders an inline term with a tooltip and links to the glossary. Usage in MDX:

```mdx
import GlossaryTip from '../../../components/GlossaryTip.astro';

Ein <GlossaryTip term="LLM" definition="Large Language Model — ein neuronales Netz, das auf grossen Textmengen trainiert wurde." /> kann Texte generieren.
```

Implementation:
- Renders the `term` as inline text with dotted underline
- On hover: shows `definition` as tooltip (CSS-only, no JS)
- Links to the glossary page anchor (`/reference/glossary#term-slug`)
- Accessible: tooltip content available via `aria-describedby`

- [ ] **Step 5: Test in a scratch MDX page, then delete the test page**

- [ ] **Step 6: Commit**

```bash
git add src/components/GlossaryTip.astro
git commit -m "feat: add glossary tooltip component"
```

---

### Task 4: GitHub Actions Deployment

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create deploy.yml**

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: add GitHub Pages deployment workflow"
```

---

## Chunk 2: Landing Page & Navigation

### Task 5: Create Landing Page (DE + EN)

**Files:**
- Create: `src/content/docs/index.mdx`
- Create: `src/content/docs/de/start/index.mdx`
- Create: `src/content/docs/en/start/index.mdx`

- [ ] **Step 1: Create root index.mdx** (language selector splash)

- [ ] **Step 2: Create DE landing page**

Splash page with:
- Hero: Title "AI Fluency", tagline about the learning journey (1 sentence)
- Two CTA buttons: "Mit L1 starten" (primary), "Wo stehst du?" (secondary) → level-check
- Brief overview: What is AI Fluency, who is it for, the L1-L4 progression
- Frontmatter: `title`, `description`, `template: splash`

- [ ] **Step 3: Create EN landing page** (mirror of DE)

- [ ] **Step 4: Verify and commit**

```bash
git add src/content/docs/
git commit -m "feat: add landing pages (DE + EN) with hero and navigation"
```

---

### Task 6: Create Level Check Page (DE + EN)

**Files:**
- Create: `src/content/docs/de/start/level-check.mdx`
- Create: `src/content/docs/en/start/level-check.mdx`

- [ ] **Step 1: Create DE level check**

5-6 yes/no questions, each with a recommendation. No JavaScript. Clean, scannable layout.

- [ ] **Step 2: Create EN level check**

- [ ] **Step 3: Commit**

```bash
git add src/content/docs/de/start/level-check.mdx src/content/docs/en/start/level-check.mdx
git commit -m "feat: add level check self-assessment (DE + EN)"
```

---

## Chunk 3: L1 Content — First Steps with AI

**Pre-requisite: Research.** Before writing L1 content, use `research-pipeline` skill to research:
- Current AI chatbot landscape (ChatGPT, Claude, Gemini, Copilot) — features, pricing, limitations
- Common beginner misconceptions, hallucination examples, data privacy policies
- Beginner-friendly explanations of generative AI (analogies, mental models)

Save to `docs/research/l1-research.md`.

### Task 7: L1 Lessons (DE)

**Files:** Create 5 files in `src/content/docs/de/l1-first-steps/`

Each lesson follows: What & Why → How It Works → Do's & Don'ts → Try It → Think Further. Each starts with progress indicator blockquote. Each has `title` + `description` in frontmatter.

- [ ] **Step 1: Write 01-what-is-ai.mdx** — What is Generative AI (analogy-based, no jargon, GlossaryTip: LLM, Token, Generative AI)
- [ ] **Step 2: Write 02-tools-overview.mdx** — ChatGPT, Claude, Gemini, M365 Copilot overview (neutral, pricing with date stamp)
- [ ] **Step 3: Write 03-first-conversations.mdx** — 3 example conversations (good/medium/bad) with annotations, 3 exercises
- [ ] **Step 4: Write 04-understanding-limits.mdx** — Hallucinations, knowledge cutoff, data privacy, bias
- [ ] **Step 5: Write 05-dos-and-donts.mdx** — L1 synthesis, comprehensive DosDonts component, link to L2
- [ ] **Step 6: Verify all pages render, components work**
- [ ] **Step 7: Commit**

```bash
git add src/content/docs/de/l1-first-steps/
git commit -m "feat: add L1 content (DE) — First Steps with AI"
```

### Task 8: L1 Lessons (EN)

- [ ] **Step 1: Translate all 5 L1 lessons** (adapt, don't translate literally)
- [ ] **Step 2: Verify and commit**

```bash
git add src/content/docs/en/l1-first-steps/
git commit -m "feat: add L1 content (EN) — First Steps with AI"
```

### Task 8b: L1 Quality Check

- [ ] **Step 1: Review all L1 lessons** for: lesson pattern consistency, factual accuracy, component usage (DosDonts, GlossaryTip), progress indicators present, description in frontmatter, cross-references to glossary

---

## Chunk 4: L2 Content — Intentional Prompting

**Pre-requisite: Research.** Research prompt engineering best practices (Anthropic guide, OpenAI guide, Google guide), academic research on prompt effectiveness, real-world examples. Save to `docs/research/l2-research.md`.

### Task 9: L2 Lessons (DE)

**Files:** Create 5 files in `src/content/docs/de/l2-intentional-prompting/`

- [ ] **Step 1: Write 01-prompt-anatomy.mdx** — Role, context, task, format, constraints. Visual breakdown, before/after. GlossaryTip: System Prompt, User Prompt, Role Prompting
- [ ] **Step 2: Write 02-prompting-techniques.mdx** — Few-shot, chain-of-thought, role-play with concrete examples. GlossaryTip: Few-Shot, Chain-of-Thought, Zero-Shot
- [ ] **Step 3: Write 03-iteration-as-method.mdx** — 3-step text refinement, the editing conversation
- [ ] **Step 4: Write 04-task-types.mdx** — Writing, analyzing, summarizing, translating, brainstorming, coding — one example each
- [ ] **Step 5: Write 05-good-vs-bad-prompts.mdx** — L2 synthesis, 5-6 side-by-side comparisons, link to L3
- [ ] **Step 6: Verify and commit**

```bash
git add src/content/docs/de/l2-intentional-prompting/
git commit -m "feat: add L2 content (DE) — Intentional Prompting"
```

### Task 10: L2 Lessons (EN)

- [ ] **Step 1: Translate all 5 L2 lessons** (adapt, don't translate literally)
- [ ] **Step 2: Verify and commit**

```bash
git add src/content/docs/en/l2-intentional-prompting/
git commit -m "feat: add L2 content (EN) — Intentional Prompting"
```

### Task 10b: L2 Quality Check

- [ ] **Step 1: Review all L2 lessons** (same criteria as Task 8b)

---

## Chunk 5: L3 Content — Context as Infrastructure

**Pre-requisite: Research.** Research Claude Projects features, Custom GPTs, M365 Copilot, system prompt best practices, real-world persistent context setups. Save to `docs/research/l3-research.md`.

### Task 11: L3 Lessons (DE)

**Files:** Create 5 files in `src/content/docs/de/l3-context-infrastructure/`

- [ ] **Step 1: Write 01-persistent-context.mdx** — Paradigm shift ("explain your job once, not every morning"). What persistent context is, compound returns, AND when it doesn't pay off (simple one-off tasks, rapidly changing contexts). GlossaryTip: Context Window, System Prompt, Custom Instructions
- [ ] **Step 2: Write 02-claude-projects.mdx** — Step-by-step creation, custom instructions examples, knowledge file strategies
- [ ] **Step 3: Write 03-custom-gpts.mdx** — Step-by-step, differences from Claude Projects, when to use which
- [ ] **Step 4: Write 04-m365-copilot.mdx** — How it differs (integrated, organizational data), use cases per app, limitations
- [ ] **Step 5: Write 05-system-prompt-design.mdx** — L3 synthesis, anatomy of a great system prompt, 3 real examples, anti-patterns, link to L4
- [ ] **Step 6: Verify and commit**

```bash
git add src/content/docs/de/l3-context-infrastructure/
git commit -m "feat: add L3 content (DE) — Context as Infrastructure"
```

### Task 12: L3 Lessons (EN)

- [ ] **Step 1: Translate all 5 L3 lessons** (adapt, don't translate literally)
- [ ] **Step 2: Verify and commit**

```bash
git add src/content/docs/en/l3-context-infrastructure/
git commit -m "feat: add L3 content (EN) — Context as Infrastructure"
```

### Task 12b: L3 Quality Check

- [ ] **Step 1: Review all L3 lessons** (same criteria as Task 8b)

---

## Chunk 6: L4 Content — AI as Coworker

**Pre-requisite: Research.** Research Claude Cowork (features, connectors, pricing), ChatGPT Agent Mode, agentic AI compliance (EU AI Act for autonomous systems), trust calibration research, enterprise case studies. Save to `docs/research/l4-research.md`.

### Task 13: L4 Lessons (DE)

**Files:** Create 5 files in `src/content/docs/de/l4-ai-coworker/`

- [ ] **Step 1: Write 01-from-chat-to-delegation.mdx** — Delegation spectrum (asking → instructing → delegating → autonomy), task decomposition. GlossaryTip: Agent, Agentic AI, Human-in-the-Loop
- [ ] **Step 2: Write 02-claude-cowork.mdx** — Desktop agent deep dive, connectors, recurring tasks, setup walkthrough
- [ ] **Step 3: Write 03-chatgpt-agent-mode.mdx** — How it works, comparison with Cowork, task scheduling
- [ ] **Step 4: Write 04-calibrating-trust.mdx** — When to verify vs. trust, quality signals, verification spectrum
- [ ] **Step 5: Write 05-compliance-basics.mdx** — Agentic AI compliance (awareness level): liability, audit trails, human-in-the-loop, EU AI Act basics. Links to Reference for full detail. Note: Phase 2+ paths go deeper.
- [ ] **Step 6: Verify and commit**

```bash
git add src/content/docs/de/l4-ai-coworker/
git commit -m "feat: add L4 content (DE) — AI as Coworker"
```

### Task 14: L4 Lessons (EN)

- [ ] **Step 1: Translate all 5 L4 lessons** (adapt, don't translate literally)
- [ ] **Step 2: Verify and commit**

```bash
git add src/content/docs/en/l4-ai-coworker/
git commit -m "feat: add L4 content (EN) — AI as Coworker"
```

### Task 14b: L4 Quality Check

- [ ] **Step 1: Review all L4 lessons** (same criteria as Task 8b)

---

## Chunk 7: Glossary & Final Polish

### Task 15: Glossary Skeleton (DE + EN)

**Files:**
- Create: `src/content/docs/de/reference/glossary.mdx`
- Create: `src/content/docs/en/reference/glossary.mdx`

- [ ] **Step 1: Create DE glossary**

~30-40 terms used in L1-L4. Each entry: h3 with anchor ID, 1-2 sentence definition, "Begegnet dir in: L1" link.

Key terms: Agent, Agentic AI, AI Act (EU), API, Bias, Chain-of-Thought, Claude, Claude Cowork, Compliance, Context Window, Custom GPT, Datenschutz, Few-Shot, Fine-Tuning, Generative AI, GPT, Halluzination, Human-in-the-Loop, KI, Knowledge Cutoff, LLM, M365 Copilot, MCP, Modell, Prompt, Prompt Engineering, RAG, Rolle (Role), System Prompt, Temperature, Token, Zero-Shot.

- [ ] **Step 2: Create EN glossary** (adapted definitions)
- [ ] **Step 3: Verify GlossaryTip links resolve to correct anchors**
- [ ] **Step 4: Commit**

```bash
git add src/content/docs/de/reference/ src/content/docs/en/reference/
git commit -m "feat: add glossary skeleton (DE + EN) with L1-L4 terms"
```

---

### Task 16: Build Verification & Final Polish

- [ ] **Step 1: Full build test** — `npm run build`, expect clean build
- [ ] **Step 2: Verify all navigation paths** — Landing → L1 → L2 → L3 → L4, level check, glossary links, language switching, sidebar order
- [ ] **Step 3: Add last-reviewed dates** to all content pages: `*Last reviewed: 2026-XX-XX*`
- [ ] **Step 4: Create README.md** — What AI Fluency is, live site link, how to run locally, project structure, license
- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: complete Phase 1 MVP — L1-L4 + glossary + landing page"
```

- [ ] **Step 6: Create GitHub repository and push**

```bash
gh repo create janrummel/ai-fluency --public --source=. --push
```

Verify: GitHub Pages deployment triggers and site is live at `https://janrummel.github.io/ai-fluency/`

---

## Post-Phase 1: What Comes Next

- **Phase 2:** Maker path (3 modules) + Principles reference section
- **Phase 3:** Coworker + Leader paths
- **Phase 4:** Full reference section (Regulation, Ethics, Tool Catalog)

Each phase gets its own implementation plan when the time comes.
