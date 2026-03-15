# Visual Redesign Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform AI Fluency from a text-heavy default Starlight site into a dark-first, visually rich learning platform with level colors, custom components, illustrations, and icons.

**Architecture:** CSS-first dark theme via token swap, 6 new Astro components (LessonHeader, LevelHero, LevelCard, ToolLogo, LessonIllustration, Head override), Lucide icons via astro-icon, Storyset illustrations. All 40 lesson files get component additions (no content changes).

**Tech Stack:** Astro 5.18, Starlight 0.37.7, astro-icon, @iconify-json/lucide, CSS custom properties

**Spec:** `docs/superpowers/specs/2026-03-15-visual-redesign-design.md`

---

## Chunk 1: Foundation — Dark Theme + Level Colors + Dependencies

### Task 1: Install dependencies

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Install astro-icon and Lucide icons**

```bash
npm install astro-icon @iconify-json/lucide
```

- [ ] **Step 2: Verify build still works**

```bash
npm run build
```
Expected: Clean build, no errors.

- [ ] **Step 3: Commit**

```bash
git add package.json package-lock.json
git commit -m "chore: add astro-icon and lucide icon dependencies"
```

### Task 2: CSS dark-first token swap + level colors

**Files:**
- Modify: `src/styles/custom.css`

- [ ] **Step 1: Swap `:root` and `[data-theme='dark']` blocks**

`:root` gets dark values (new default), `[data-theme='light']` gets light values. Key changes:
- `--af-bg`: `#121214` (dark, deeper than before)
- `--af-surface`: `#1C1C1E`
- New token `--af-surface-raised`: `#2C2C2E`
- `--af-code-bg` and `--af-blockquote-bg` become aliases of `--af-surface-raised`

- [ ] **Step 2: Add level color tokens**

After surface tokens:
```css
/* Level Colors */
--af-l1: #2997FF;  --af-l1-bg: rgba(41,151,255,0.15);
--af-l2: #30D158;  --af-l2-bg: rgba(48,209,88,0.15);
--af-l3: #FF9F0A;  --af-l3-bg: rgba(255,159,10,0.15);
--af-l4: #BF5AF2;  --af-l4-bg: rgba(191,90,242,0.15);
```

Light mode equivalents:
```css
--af-l1: #0071E3;  --af-l1-bg: rgba(0,113,227,0.1);
--af-l2: #248A3D;  --af-l2-bg: rgba(36,138,61,0.1);
--af-l3: #E87400;  --af-l3-bg: rgba(232,116,0,0.1);
--af-l4: #8B5CF6;  --af-l4-bg: rgba(139,92,246,0.1);
```

- [ ] **Step 3: Add contextual level rules**

```css
body[data-level="1"] { --af-level-color: var(--af-l1); --af-level-bg: var(--af-l1-bg); }
body[data-level="2"] { --af-level-color: var(--af-l2); --af-level-bg: var(--af-l2-bg); }
body[data-level="3"] { --af-level-color: var(--af-l3); --af-level-bg: var(--af-l3-bg); }
body[data-level="4"] { --af-level-color: var(--af-l4); --af-level-bg: var(--af-l4-bg); }
```

- [ ] **Step 4: Update sidebar accent to use level color**

```css
nav.sidebar a[aria-current='page'] {
  color: var(--af-level-color, var(--af-accent));
  border-left-color: var(--af-level-color, var(--af-accent));
  background: color-mix(in srgb, var(--af-level-color, var(--af-accent)) 6%, transparent);
}
```

- [ ] **Step 5: Add gradient text utility**

```css
.gradient-text {
  background: linear-gradient(135deg, var(--af-l1), var(--af-l4));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

- [ ] **Step 6: Verify build + visual check**

```bash
npm run build && npm run preview
```

Expected: Site renders dark by default, light mode still works via toggle.

- [ ] **Step 7: Commit**

```bash
git add src/styles/custom.css
git commit -m "feat: dark-first theme with level color system"
```

### Task 3: Head override for data-level injection

**Files:**
- Create: `src/components/Head.astro`
- Modify: `astro.config.mjs`

- [ ] **Step 1: Create Head component**

```astro
---
import type { Props } from '@astrojs/starlight/props';
import Default from '@astrojs/starlight/components/Head.astro';
---
<Default {...Astro.props}><slot /></Default>
<script is:inline>
(function(){var m=location.pathname.match(/\/l(\d)-/);if(m)document.body.dataset.level=m[1]})();
</script>
```

- [ ] **Step 2: Register Head override in astro.config.mjs**

Add to starlight config:
```js
components: {
  Head: './src/components/Head.astro',
},
```

- [ ] **Step 3: Verify build + check data-level attribute in browser**

```bash
npm run build
```

- [ ] **Step 4: Commit**

```bash
git add src/components/Head.astro astro.config.mjs
git commit -m "feat: add Head override for level-based color injection"
```

---

## Chunk 2: Custom Components

### Task 4: LessonHeader component

**Files:**
- Create: `src/components/LessonHeader.astro`

- [ ] **Step 1: Create component**

Props: `level: number`, `lesson: number`, `total: number`
- Reads locale from `Astro.url.pathname` (checks `/en/` prefix)
- Renders: level badge pill, "Lektion X von Y" / "Lesson X of Y", progress dots
- ARIA: `aria-label` on container, `aria-current="step"` on active dot
- Uses `--af-lN` tokens for level color

- [ ] **Step 2: Verify by adding to one test file, build, check**

- [ ] **Step 3: Commit**

```bash
git add src/components/LessonHeader.astro
git commit -m "feat: add LessonHeader component with progress dots"
```

### Task 5: LevelHero component

**Files:**
- Create: `src/components/LevelHero.astro`

- [ ] **Step 1: Create component**

Props: `level: number`, `title: string`, `description: string`
- Full-width gradient bar using level color (subtle)
- Level number badge, large title, secondary description
- Responsive

- [ ] **Step 2: Commit**

```bash
git add src/components/LevelHero.astro
git commit -m "feat: add LevelHero component with gradient header"
```

### Task 6: LevelCard component

**Files:**
- Create: `src/components/LevelCard.astro`

- [ ] **Step 1: Create component**

Props: `level: number`, `title: string`, `description: string`, `lessons: number`, `href: string`, `icon: string`
- Card with left border in level color
- Number badge with tinted background
- Lucide icon via astro-icon
- Hover elevation

- [ ] **Step 2: Commit**

```bash
git add src/components/LevelCard.astro
git commit -m "feat: add LevelCard component for landing page grid"
```

### Task 7: LessonIllustration + ToolLogo components

**Files:**
- Create: `src/components/LessonIllustration.astro`
- Create: `src/components/ToolLogo.astro`

- [ ] **Step 1: Create LessonIllustration**

Props: `src: string`, `alt: string`
- Centered container, max-width 600px, rounded corners, subtle border
- `role="img"` with alt text

- [ ] **Step 2: Create ToolLogo**

Props: `tool: 'chatgpt' | 'claude' | 'copilot' | 'gemini'`, `size?: number`
- Maps tool name to SVG path in `/logos/`
- Falls back to colored text badge

- [ ] **Step 3: Commit**

```bash
git add src/components/LessonIllustration.astro src/components/ToolLogo.astro
git commit -m "feat: add LessonIllustration and ToolLogo components"
```

---

## Chunk 3: Landing Pages + Lesson Integration

### Task 8: Rewrite landing pages

**Files:**
- Modify: `src/content/docs/de/start/index.mdx`
- Modify: `src/content/docs/en/start/index.mdx`

- [ ] **Step 1: Rewrite DE landing page**

Replace existing content with:
- Gradient title "Von Chat zu Kompetenz"
- Subtitle
- 2×2 LevelCard grid (L1–L4) with Lucide icons
- Level Check link

- [ ] **Step 2: Rewrite EN landing page**

Same structure, English text.

- [ ] **Step 3: Build and verify**

- [ ] **Step 4: Commit**

```bash
git add src/content/docs/de/start/index.mdx src/content/docs/en/start/index.mdx
git commit -m "feat: redesign landing pages with LevelCard grid"
```

### Task 9: Add LessonHeader to all 40 lesson files

**Files:**
- Modify: all 20 DE lesson files (`src/content/docs/de/l1-*/01-*.mdx` through `l4-*/05-*.mdx`)
- Modify: all 20 EN lesson files (same pattern)

- [ ] **Step 1: Replace blockquote counters with LessonHeader in all DE files**

For each file: add `import LessonHeader`, replace `> Lektion X von 5 — LN: ...` with `<LessonHeader level={N} lesson={X} total={5} />`

- [ ] **Step 2: Same for all EN files**

- [ ] **Step 3: Add LevelHero to 8 first-lesson files (01-*)**

4 DE + 4 EN first-lesson files get `import LevelHero` and `<LevelHero>` between LessonHeader and first heading.

- [ ] **Step 4: Build and verify**

```bash
npm run build
```
Expected: 48+ pages, no errors.

- [ ] **Step 5: Commit**

```bash
git add src/content/docs/
git commit -m "feat: add LessonHeader and LevelHero to all lesson files"
```

---

## Chunk 4: Illustrations + Final Polish

### Task 10: Download and integrate illustrations

**Files:**
- Create: `public/illustrations/*.svg` (20 files)

- [ ] **Step 1: Download 20 SVGs from Storyset (Rafiki style)**

Use search terms from spec table. Color-adjust each to match its level color.

- [ ] **Step 2: Save to `public/illustrations/` with naming convention**

`l1-01-what-is-ai.svg` through `l4-05-compliance.svg`

- [ ] **Step 3: Add LessonIllustration to all 40 lesson files**

Each file gets: `import LessonIllustration` and `<LessonIllustration src="/illustrations/lN-XX-name.svg" alt="..." />`

- [ ] **Step 4: Build and verify**

- [ ] **Step 5: Commit**

```bash
git add public/illustrations/ src/content/docs/
git commit -m "feat: add Storyset illustrations to all lessons"
```

### Task 11: Tool logos

**Files:**
- Create: `public/logos/*.svg` (up to 4)

- [ ] **Step 1: Source or create tool logos**

ChatGPT, Claude, Gemini, Copilot — verify brand guidelines. Use colored text badges as fallback.

- [ ] **Step 2: Commit**

```bash
git add public/logos/
git commit -m "feat: add tool logos for ChatGPT, Claude, Gemini, Copilot"
```

### Task 12: Final build verification + GlossaryTip link check

- [ ] **Step 1: Full build**

```bash
npm run build
```

- [ ] **Step 2: Verify GlossaryTip links resolve**

Check that `../../reference/glossary/#slug` links still work from lesson pages to glossary.

- [ ] **Step 3: Visual review in browser**

```bash
npm run preview
```

Check: dark theme, level colors in sidebar, landing page cards, lesson headers, progress dots, illustrations, hover states, light mode toggle.

- [ ] **Step 4: Final commit**

```bash
git commit -m "feat: complete visual redesign — dark-first theme with level colors"
```
