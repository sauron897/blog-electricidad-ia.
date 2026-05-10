import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://blog-electricidad-ia.vercel.app',
  integrations: [mdx()],
});
