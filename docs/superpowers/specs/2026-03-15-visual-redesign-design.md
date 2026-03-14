# AI Fluency — Visual Redesign Spec

**Date:** 2026-03-15
**Scope:** Full visual redesign — dark-first theme, level color system, custom components, illustrations, icons
**Branch:** `feat/visual-redesign` (off `feat/phase1-mvp`)

---

## 1. Design System

### Theme: Dark-First

Dark mode is the default. Light mode is supported but secondary.

**Implementation:** No Starlight config change needed. Starlight already defaults to `data-theme="dark"` and respects `prefers-color-scheme` via its ThemeProvider. Dark-first is achieved purely via CSS token swap: `:root` gets dark values, `[data-theme='light']` gets light values. Users with OS-level light mode preference still get light mode automatically.

### Level Colors (Apple Dark Mode System Colors)

| Level | Color | Dark Hex | Light Hex | Usage |
|-------|-------|----------|-----------|-------|
| L1 | Blue | `#2997FF` | `#0071E3` | Sidebar accent, badges, borders, hero gradient |
| L2 | Green | `#30D158` | `#248A3D` | Same |
| L3 | Orange | `#FF9F0A` | `#E87400` | Same |
| L4 | Purple | `#BF5AF2` | `#8B5CF6` | Same |

### Surface Tokens

| Token | Dark | Light | Usage |
|-------|------|-------|-------|
| `--af-bg` | `#121214` | `#FAFAFA` | Page background |
| `--af-surface` | `#1C1C1E` | `#FFFFFF` | Cards, sidebar |
| `--af-surface-raised` | `#2C2C2E` | `#F5F5F7` | Hover, code blocks, blockquotes |
| `--af-border` | `#38383A` | `#D2D2D7` | Dividers |
| `--af-border-subtle` | `#2C2C2E` | `#E8E8ED` | Subtle separators |
| `--af-text` | `#F5F5F7` | `#1D1D1F` | Primary text |
| `--af-text-secondary` | `#98989D` | `#6E6E73` | Secondary text |
| `--af-accent` | `#2997FF` | `#0071E3` | Global accent (links, focus rings) — unchanged, always blue |

### Token Migration

| Old Token | Action | New Token |
|-----------|--------|-----------|
| `--af-code-bg` | Alias to | `--af-surface-raised` |
| `--af-blockquote-bg` | Alias to | `--af-surface-raised` |
| `--af-blockquote-border` | Keep | (unchanged, still accent blue) |
| `--af-success`, `--af-danger` | Keep | (unchanged) |
| `--af-success-bg`, `--af-danger-bg` | Keep | (unchanged) |

Both `--af-code-bg` and `--af-blockquote-bg` become aliases of `--af-surface-raised` for backward compat:
```css
--af-code-bg: var(--af-surface-raised);
--af-blockquote-bg: var(--af-surface-raised);
```

### Level Color Tokens (CSS custom properties)

Static tokens per level (always available):
```css
--af-l1: #2997FF;  --af-l1-bg: rgba(41,151,255,0.15);
--af-l2: #30D158;  --af-l2-bg: rgba(48,209,88,0.15);
--af-l3: #FF9F0A;  --af-l3-bg: rgba(255,159,10,0.15);
--af-l4: #BF5AF2;  --af-l4-bg: rgba(191,90,242,0.15);
```

Contextual tokens set by `data-level` on `<body>`:
```css
body[data-level="1"] { --af-level-color: var(--af-l1); --af-level-bg: var(--af-l1-bg); }
body[data-level="2"] { --af-level-color: var(--af-l2); --af-level-bg: var(--af-l2-bg); }
body[data-level="3"] { --af-level-color: var(--af-l3); --af-level-bg: var(--af-l3-bg); }
body[data-level="4"] { --af-level-color: var(--af-l4); --af-level-bg: var(--af-l4-bg); }
```

`--af-accent` remains the global accent (blue) for links, focus rings, etc. Level colors are separate and only affect level-specific elements (sidebar accent, badges, heroes).

### data-level Injection

A small inline script in a custom Starlight Head override (`src/components/Head.astro`) parses `window.location.pathname` and sets `document.body.dataset.level`:

```js
const m = location.pathname.match(/\/l(\d)-/);
if (m) document.body.dataset.level = m[1];
```

This runs on every page load and sets `data-level="1"` through `"4"` based on the URL path. Pages outside L1–L4 (landing, glossary) get no `data-level`.

### Typography

No changes to font stack (system fonts). Addition:
- Gradient text utility: `.gradient-text { background: linear-gradient(...); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }`

---

## 2. Custom Components

### 2.1 LessonHeader

**File:** `src/components/LessonHeader.astro`
**Props:** `level: number`, `lesson: number`, `total: number`

**i18n:** The component reads the locale from `Astro.url.pathname` (checks for `/en/` prefix → English, otherwise German). No separate locale prop needed.

**Renders:**
- Level badge (colored pill: "L2")
- Text "Lektion X von Y" (DE) / "Lesson X of Y" (EN)
- ProgressBar: row of numbered circles (1–total) connected by lines. Current lesson circle uses level color fill, completed lessons use level color outline, future lessons use `--af-border` color.
- `aria-label="Lektion X von Y"` / `aria-label="Lesson X of Y"` on the progress container, `aria-current="step"` on the active dot.

**Replaces:** The blockquote pattern `> Lektion 1 von 5 — L2: Bewusst Prompten` in all 40 lesson files.

**Before/After example (DE lesson):**

Before:
```mdx
import GlossaryTip from '../../../../components/GlossaryTip.astro';

> Lektion 1 von 5 — L2: Bewusst Prompten

## Von Fragen zu Anweisungen
```

After:
```mdx
import GlossaryTip from '../../../../components/GlossaryTip.astro';
import LessonHeader from '../../../../components/LessonHeader.astro';

<LessonHeader level={2} lesson={1} total={5} />

## Von Fragen zu Anweisungen
```

### 2.2 LevelHero

**File:** `src/components/LevelHero.astro`
**Props:** `level: number`, `title: string`, `description: string`
**Renders:**
- Full-width gradient bar using level color (subtle, not overwhelming)
- Level number badge
- Title (large)
- Description (secondary text)

**Usage:** Manually added to the 8 first-lesson files only (4 levels × 2 languages: `01-*.mdx`). No auto-detection. Placed after `LessonHeader`, before the first `##` heading.

### 2.3 LevelCard

**File:** `src/components/LevelCard.astro`
**Props:** `level: number`, `title: string`, `description: string`, `lessons: number`, `href: string`, `icon: string`
**Renders:**
- Card with left border in level color
- Level number badge (circle with level-tinted background)
- Title, description, lesson count
- Lucide icon (via `astro-icon`)
- Hover: subtle elevation change (box-shadow transition)

### 2.4 ToolLogo

**File:** `src/components/ToolLogo.astro`
**Props:** `tool: 'chatgpt' | 'claude' | 'copilot' | 'gemini'`, `size?: number`
**Renders:** Inline SVG logo at specified size (default 24px). Falls back to colored text badge if SVG not available.

**Brand compliance:** Logo usage must be verified against each company's brand guidelines before publishing. If any logo cannot be used, the colored text badge fallback is the default.

### 2.5 LessonIllustration

**File:** `src/components/LessonIllustration.astro`
**Props:** `src: string`, `alt: string`
**Renders:** Centered SVG/image in a container with rounded corners (8px) and subtle border (`--af-border-subtle`). Max-width 600px. Responsive. `role="img"` with the provided `alt` text.

---

## 3. Page Structure Changes

### 3.1 Landing Pages (rewrite)

Three files affected:

| File | Content |
|------|---------|
| `src/content/docs/index.mdx` | Root language selector — minimal changes (dark theme compat) |
| `src/content/docs/de/start/index.mdx` | German landing: gradient title, LevelCard grid, Level Check link |
| `src/content/docs/en/start/index.mdx` | English landing: same structure, English content |

Both `de/start/index.mdx` and `en/start/index.mdx` get the full LevelCard grid layout. The root `index.mdx` is only adjusted for dark theme compatibility (if needed).

### 3.2 Lesson Pages (template changes, no content changes)

Each of the 40 lesson files (20 DE + 20 EN) gets:
1. `LessonHeader` component replaces the blockquote counter line
2. `LessonIllustration` component added after first heading (where illustration SVG exists)
3. The 8 first-lesson files (01-*) additionally get `LevelHero` between LessonHeader and first heading

**Content text is NOT modified.** Only component additions at top of each file.

**GlossaryTip links:** The existing `../../reference/glossary/#slug` relative paths remain valid because no directory structure changes. Verify after implementation that all GlossaryTip links still resolve.

### 3.3 Sidebar

- Level color as accent for active section: `nav.sidebar a[aria-current='page']` uses `var(--af-level-color)` instead of `var(--af-accent)` when `data-level` is set on body
- Fallback: blue accent (default) when no level is active (landing, glossary, etc.)

---

## 4. Plugins & Dependencies

### Install

| Package | Version | Purpose |
|---------|---------|---------|
| `astro-icon` | `^1.1.0` | Icon component for Astro (verify Astro 5 compat, upgrade to v2 if needed) |
| `@iconify-json/lucide` | `latest` | Lucide icon set for Iconify |

**Version check:** Before installing, verify `astro-icon` compatibility with Astro 5.18.0. If v1 is incompatible, use `astro-icon@^2.1.0` or inline SVGs as fallback.

### NOT installing

- `starlight-heading-badges` — can be added later
- `starlight-sidebar-topics` — too much restructuring

---

## 5. Illustrations & Icons

### Illustrations (20 SVGs — one per lesson)

Every lesson gets exactly one illustration. 20 unique SVGs total (shared between DE and EN — same illustration, different alt text).

- **Source:** Storyset.com, "Rafiki" style
- **Process:** Download SVG, color-adjust to level color, save to `public/illustrations/`
- **Naming:** `l1-01-what-is-ai.svg`, `l1-02-tools-overview.svg`, ..., `l4-05-compliance.svg`
- **Review:** Each illustration is reviewed before integration

| Level | Lesson | Search Term (Storyset) |
|-------|--------|----------------------|
| L1-01 | Was ist AI | "Artificial intelligence" |
| L1-02 | Tool-Überblick | "Apps" / "Mobile apps" |
| L1-03 | Erste Gespräche | "Conversation" / "Chat" |
| L1-04 | Grenzen verstehen | "Warning" / "Alert" |
| L1-05 | Do's und Don'ts | "Checklist" / "Rules" |
| L2-01 | Prompt-Anatomie | "Writing" / "Document" |
| L2-02 | Prompting-Techniken | "Strategy" / "Plan" |
| L2-03 | Iteration | "Process" / "Cycle" |
| L2-04 | Aufgabentypen | "Task management" |
| L2-05 | Gute vs. schlechte Prompts | "Comparison" / "Quality" |
| L3-01 | Persistenter Kontext | "Memory" / "Database" |
| L3-02 | Claude Projects | "Workspace" / "Project" |
| L3-03 | Custom GPTs | "Customization" / "Settings" |
| L3-04 | M365 Copilot | "Office" / "Integration" |
| L3-05 | System Prompt Design | "Blueprint" / "Architecture" |
| L4-01 | Delegation | "Teamwork" / "Delegation" |
| L4-02 | Claude Cowork | "Desktop" / "Computer work" |
| L4-03 | ChatGPT Agent | "Web browsing" / "Internet" |
| L4-04 | Trust Calibration | "Security" / "Verification" |
| L4-05 | Compliance | "Legal" / "Regulation" |

### Tool Logos (4 SVGs)

- ChatGPT, Claude, Gemini, Microsoft Copilot
- Saved to `public/logos/`
- **Brand compliance:** Verify each company's brand guidelines before use. Default to colored text badges until verified.

### Lucide Icons

- Via `astro-icon` + `@iconify-json/lucide`
- Used in: LevelCards (`brain` for L1, `pen-tool` for L2, `layers` for L3, `users` for L4)
- No emoji anywhere in the site

---

## 6. CSS Changes

### custom.css — Major Changes

1. **Swap dark/light tokens:** `:root` gets dark values, `[data-theme='light']` gets light values. `--af-bg` dark changes from `#1C1C1E` to `#121214` (intentionally deeper).
2. **Add level color tokens:** `--af-l1` through `--af-l4` + `--af-l1-bg` through `--af-l4-bg`
3. **Add contextual level tokens:** `body[data-level="N"]` rules setting `--af-level-color` and `--af-level-bg`
4. **Add `--af-surface-raised`:** New token, with `--af-code-bg` and `--af-blockquote-bg` as aliases
5. **Update component styles:** GlossaryTip, DosDonts, blockquote, code, table for dark surfaces
6. **Add gradient text utility:** `.gradient-text` class
7. **Add sidebar level color:** `nav.sidebar a[aria-current='page']` uses `var(--af-level-color, var(--af-accent))`

### Starlight config (astro.config.mjs)

- No `defaultTheme` setting (does not exist in Starlight 0.37.7)
- Add Head component override for data-level script (if using component overrides)
- Register `astro-icon` integration if required by the package

---

## 7. Accessibility

- **prefers-color-scheme:** Preserved. Starlight's ThemeProvider handles OS-level preference. Our CSS swap does not override it.
- **prefers-reduced-motion:** Already in CSS, preserved.
- **ProgressBar:** `aria-label` on container, `aria-current="step"` on active dot.
- **LessonIllustration:** `role="img"` with descriptive `alt` text.
- **Color contrast:** All level colors on dark background meet WCAG AA for large text. Verify body text contrast ratios after token swap.

---

## 8. File Changes Summary

### New Files (29)
- `src/components/LessonHeader.astro`
- `src/components/LevelHero.astro`
- `src/components/LevelCard.astro`
- `src/components/ToolLogo.astro`
- `src/components/LessonIllustration.astro`
- `src/components/Head.astro` (Starlight override for data-level script)
- `public/illustrations/*.svg` (20 files)
- `public/logos/*.svg` (up to 4 files, pending brand verification)

### Modified Files (44+)
- `src/styles/custom.css` (major: dark-first + level colors + token migration)
- `src/content/docs/de/start/index.mdx` (rewrite: landing page with LevelCards)
- `src/content/docs/en/start/index.mdx` (rewrite: English landing)
- `src/content/docs/index.mdx` (minor: dark theme compat)
- 20 DE lesson files (add LessonHeader, LessonIllustration, LevelHero on 01-*)
- 20 EN lesson files (same)
- `astro.config.mjs` (Head override registration, astro-icon if needed)
- `package.json` (add astro-icon + iconify deps)

### Not Modified
- Lesson text content (no editorial changes)
- Glossary content (only dark-theme CSS adjustments)
- Research files
- GitHub Actions deploy workflow
