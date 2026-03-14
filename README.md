# AI Fluency

A free, open learning path for knowledge workers — from first AI conversations to autonomous delegation. Bilingual (DE + EN), built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build).

**Live:** [janrummel.github.io/ai-fluency](https://janrummel.github.io/ai-fluency/)

## What It Covers

| Level | Topic | Lessons |
|-------|-------|---------|
| **L1** | First Steps with AI | What AI is, tools overview, first conversations, limits, do's & don'ts |
| **L2** | Intentional Prompting | Prompt anatomy, techniques, iteration, task types, good vs. bad prompts |
| **L3** | Context as Infrastructure | Persistent context, Claude Projects, Custom GPTs, M365 Copilot, system prompt design |
| **L4** | AI as Coworker | Delegation spectrum, Claude Cowork, ChatGPT Agent Mode, trust calibration, EU AI Act basics |

Plus a glossary with 27 key terms.

## Run Locally

```bash
npm install
npm run dev
```

Open [localhost:4321](http://localhost:4321).

## Build

```bash
npm run build
npm run preview
```

## Project Structure

```
src/
├── content/docs/
│   ├── de/           # German content
│   │   ├── start/
│   │   ├── l1-first-steps/
│   │   ├── l2-intentional-prompting/
│   │   ├── l3-context-infrastructure/
│   │   ├── l4-ai-coworker/
│   │   └── reference/
│   └── en/           # English content (same structure)
├── components/       # GlossaryTip, DosDonts
└── styles/           # Custom CSS
```

## Tech Stack

- [Astro 5](https://astro.build) + [Starlight 0.37](https://starlight.astro.build)
- Deployed via GitHub Actions to GitHub Pages
- No backend, no tracking, no cookies

## License

MIT
