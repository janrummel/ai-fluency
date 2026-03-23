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
    '/': `${base}/en/start/`,
    '/en/': `${base}/en/start/`,
    '/de/': `${base}/de/start/`,
  },
  integrations: [
    starlight({
      title: 'AI Fluency',
      defaultLocale: 'en',
      locales: {
        en: { label: 'English', lang: 'en' },
        de: { label: 'Deutsch', lang: 'de' },
      },
      customCss: ['./src/styles/custom.css'],
      components: {
        Head: './src/components/Head.astro',
        Footer: './src/components/Footer.astro',
      },
      head: [
        { tag: 'meta', attrs: { property: 'og:type', content: 'website' } },
        { tag: 'meta', attrs: { property: 'og:site_name', content: 'AI Fluency' } },
        { tag: 'meta', attrs: { property: 'og:title', content: 'AI Fluency — From Chat to Competency' } },
        { tag: 'meta', attrs: { property: 'og:description', content: 'A free, open learning path for knowledge workers — from first AI conversations to autonomous delegation. 4 levels, 20 lessons, bilingual (EN + DE).' } },
        { tag: 'meta', attrs: { property: 'og:url', content: 'https://janrummel.github.io/ai-fluency/' } },
        { tag: 'meta', attrs: { property: 'og:image', content: 'https://janrummel.github.io/ai-fluency/og-image.png' } },
        { tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
        { tag: 'meta', attrs: { name: 'twitter:title', content: 'AI Fluency — From Chat to Competency' } },
        { tag: 'meta', attrs: { name: 'twitter:description', content: 'A free, open learning path for knowledge workers — from first AI conversations to autonomous delegation.' } },
      ],
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/janrummel/ai-fluency' },
      ],
      sidebar: [
        {
          label: 'Start',
          translations: { de: 'Start' },
          items: [{ slug: 'start' }, { slug: 'start/curriculum' }, { slug: 'start/level-check' }],
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
