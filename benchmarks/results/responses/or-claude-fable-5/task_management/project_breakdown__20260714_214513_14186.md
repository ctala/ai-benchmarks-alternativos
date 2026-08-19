# Claude Fable 5 — task_management/project_breakdown

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.83 | quality: 9.8
- latency_total: 29.243s | tokens_per_second: 70.0
- input_tokens: 117 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Respuesta completa

# Plan de Lanzamiento: Landing Page SaaS de Gestión de Inventario

**Duración total:** 4 semanas | **Equipo:** 1 diseñador (DIS), 2 developers (DEV1, DEV2), 1 copywriter (COPY)

---

## Fase 1: Descubrimiento y Estrategia (Semana 1, días 1-3)

| Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|
| Definir propuesta de valor, buyer persona y objetivo de conversión (demo, trial, waitlist) | Todo el equipo (workshop) | 0.5 día | — |
| Análisis de competencia y benchmarks de landings SaaS | COPY + DIS | 1 día | Workshop |
| Definir estructura/arquitectura de la página (secciones: hero, features, pricing, social proof, FAQ, CTA) | COPY + DIS | 1 día | Análisis |
| Setup técnico inicial: repo, hosting, dominio, CI/CD, stack (ej. Next.js/Astro + Vercel) | DEV1 + DEV2 | 2 días | — (en paralelo) |
| Definir requisitos de integraciones: formulario, CRM/email (HubSpot, Mailchimp), analytics | DEV2 | 0.5 día | Workshop |

**Entregable:** Brief creativo + wireframe de bajo nivel + entorno técnico listo.

---

## Fase 2: Contenido y Diseño (Semana 1 día 4 – Semana 2)

| Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|
| Copywriting v1: hero, headlines, features, beneficios, CTAs, FAQ | COPY | 3 días | Wireframe aprobado |
| Diseño UI del sistema visual (tipografía, colores, componentes) | DIS | 2 días | Wireframe |
| Diseño de mockups desktop + mobile en alta fidelidad | DIS | 3 días | Sistema visual + copy v1 |
| Ilustraciones/screenshots del producto, mockups de la app | DIS | 2 días | Mockups (en paralelo con revisión) |
| Revisión y ajuste de copy sobre diseño final | COPY | 1 día | Mockups |
| DEV: construir componentes base y layout con contenido placeholder | DEV1 + DEV2 | 4 días | Sistema visual (no esperan mockups finales) |

**Entregable (fin semana 2):** Diseño aprobado + copy final + esqueleto de la página construido.

> ⚠️ **Clave:** los devs NO esperan al diseño final. Trabajan en paralelo con componentes, formularios e integraciones usando placeholders.

---

## Fase 3: Desarrollo e Integración (Semana 3)

| Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|
| Maquetación pixel-perfect de todas las secciones (responsive) | DEV1 | 4 días | Diseño final |
| Formulario de captura + integración con CRM/email + emails de confirmación | DEV2 | 2 días | Requisitos de integración |
| Analytics: GA4/Plausible, eventos de conversión, heatmaps (Hotjar) | DEV2 | 1 día | Página maquetada |
| SEO on-page: meta tags, Open Graph, schema markup, sitemap | DEV2 + COPY | 1 día | Copy final |
| Optimización de performance (imágenes, Core Web Vitals, Lighthouse >90) | DEV1 | 1 día | Maquetación |
| Preparar assets de lanzamiento: social media, email de anuncio | COPY + DIS | 2 días | — (en paralelo) |

**Entregable:** Landing funcional en entorno de staging.

---

## Fase 4: QA, Ajustes y Lanzamiento (Semana 4)

| Tarea | Responsable | Duración | Dependencias |
|---|---|---|---|
| QA cross-browser y cross-device (Chrome, Safari, Firefox, iOS, Android) | DEV1 + DEV2 | 1.5 días | Staging completo |
| Revisión de copy final en producción (typos, enlaces, tono) | COPY | 0.5 día | Staging |
| Revisión de diseño (QA visual vs. mockups) | DIS | 0.5 día | Staging |
| Test end-to-end del funnel: formulario → CRM → email | DEV2 | 0.5 día | QA |
| Corrección de bugs y ajustes finales | DEV1 + DEV2 | 1.5 días | QA completo |
| Configurar A/B test inicial (opcional: 2 variantes de hero) | DEV2 | 0.5 día | Ajustes |
| **Soft launch** (día 3 de semana 4): publicar sin anunciar, verificar en producción | DEV1 | 0.5 día | Todo lo anterior |
| **Lanzamiento oficial** (día 4-5): DNS final, anuncio en redes/email | Todo el equipo | 0.5 día | Soft launch OK |
| Monitoreo post-lanzamiento: errores, conversiones, velocidad | DEV1 + DEV2 | Continuo | Lanzamiento |

---

## Timeline Visual

```
Semana 1  |████ Estrategia ██|████ Copy v1 + Diseño UI ████████████|
          |██ Setup técnico ██|████ Componentes base (DEVs) ███████|
Semana 2  |████ Mockups alta fidelidad + Copy final ██████