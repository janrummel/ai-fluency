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
