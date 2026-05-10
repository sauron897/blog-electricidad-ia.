import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    keywords: z.array(z.string()).optional(),
    heroImage: z.string().optional(),
    author: z.string().default('Editor'),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
