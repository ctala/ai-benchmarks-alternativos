// Motor del sitio (change motor-sitio, DECISIONES 11-nov-2026). Estático, mismas URLs que hoy
// (`/slug/`): `directory` + `trailingSlash: "always"`. Compila a `dist`; `sitio/legado/` no se toca
// hasta el corte (design.md D1).
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://benchmarks.cristiantala.com',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
  outDir: './dist',
  compressHTML: false,
});
