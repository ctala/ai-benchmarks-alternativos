# Claude Opus 4.6 — task_management/project_breakdown

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.33 | quality: 9.52
- latency_total: 32.61s | tokens_per_second: 62.8
- input_tokens: 88 | output_tokens: 2047
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🚀 Plan de Proyecto: Landing Page SaaS de Gestión de Inventario

## Visión General

| Dato | Detalle |
|---|---|
| **Duración total** | 4 semanas (20 días hábiles) |
| **Equipo** | 1 Diseñador (DIS), 2 Developers (DEV1, DEV2), 1 Copywriter (COP) |
| **Entregable** | Landing page lista para producción y optimizada para conversión |

---

## FASE 0 — Kick-off y Estrategia
**📅 Semana 1: Días 1-2**

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|
| 0.1 | Reunión de kick-off: objetivos, público objetivo, propuesta de valor, tono de marca, referencias visuales | TODOS | 0.5 días | — |
| 0.2 | Definir estructura de secciones de la landing (wireframe conceptual en pizarra/Miro) | DIS + COP | 0.5 días | 0.1 |
| 0.3 | Investigar competencia directa (3-5 landings de SaaS de inventario) | COP | 0.5 días | 0.1 |
| 0.4 | Definir stack técnico, setup del repo, CI/CD, dominio, hosting | DEV1 + DEV2 | 1 día | 0.1 |
| 0.5 | Definir métricas de éxito (CTR, signups, bounce rate) y herramientas de tracking | TODOS | 0.5 días | 0.1 |

**✅ Entregable de fase:** Brief aprobado, repo creado, estructura de secciones definida.

---

## FASE 1 — Contenido y Diseño
**📅 Semana 1-2: Días 3-8**

### Track A: Copywriting (COP)

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|
| 1.1 | Redactar headline principal + subheadline (propuesta de valor) | COP | 0.5 días | 0.2, 0.3 |
| 1.2 | Redactar textos de secciones: features (4-6), beneficios, social proof, CTA | COP | 1.5 días | 1.1 |
| 1.3 | Redactar FAQ (6-8 preguntas) | COP | 0.5 días | 1.2 |
| 1.4 | Redactar textos legales (privacidad, términos básicos) | COP | 0.5 días | 0.1 |
| 1.5 | Redactar secuencia de email de bienvenida post-signup (2-3 emails) | COP | 1 día | 1.2 |
| 1.6 | Revisión y aprobación de todos los textos | COP + TODOS | 0.5 días | 1.2, 1.3 |

### Track B: Diseño (DIS)

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|
| 1.7 | Wireframes de baja fidelidad (mobile + desktop) | DIS | 1 día | 0.2 |
| 1.8 | Diseño UI alta fidelidad — Hero + Features | DIS | 1.5 días | 1.7, 1.1 |
| 1.9 | Diseño UI alta fidelidad — Pricing, Testimonios, FAQ, Footer | DIS | 1.5 días | 1.8, 1.2 |
| 1.10 | Diseño de assets: iconos de features, ilustraciones/mockups del producto | DIS | 1 día | 1.8 |
| 1.11 | Diseño responsive (adaptaciones mobile/tablet) | DIS | 0.5 días | 1.9 |
| 1.12 | Revisión de diseño con equipo + iteración | DIS + TODOS | 0.5 días | 1.9, 1.11 |

### Track C: Setup técnico en paralelo (DEVs)

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|
| 1.13 | Configurar proyecto (Next.js/Astro + TailwindCSS + componentes base) | DEV1 | 1 día | 0.4 |
| 1.14 | Configurar CMS headless o sistema de contenido si aplica | DEV2 | 0.5 días | 0.4 |
| 1.15 | Implementar estructura HTML semántica base según wireframes | DEV1 | 1 día | 1.7 |
| 1.16 | Configurar formulario de signup + backend (API, base de datos o integración con Mailchimp/HubSpot) | DEV2 | 1.5 días | 0.4 |
| 1.17 | Configurar analytics (GA4, Hotjar, Meta Pixel si aplica) | DEV2 | 0.5 días | 0.5 |

**✅ Entregable de fase:** Diseño aprobado en Figma, copy aprobado, infraestructura técnica lista, formulario funcional.

---

## FASE 2 — Desarrollo Frontend
**📅 Semana 2-3: Días 9-15**

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|
| 2.1 | Maquetar Hero section (headline, CTA, imagen/animación) | DEV1 | 1 día | 1.8, 1.15 |
| 2.2 | Maquetar sección de Features con iconos/ilustraciones | DEV2 | 1 día | 1.8, 1.10 |
| 2.3 | Maquetar sección de Beneficios / Cómo funciona | DEV1 | 0.5 días | 1.9 |
| 2.4 | Maquetar sección de Social Proof / Testimonios | DEV2 | 0.5 días | 1.9 |
| 2.5 | Maquetar sección de Pricing / Planes | DEV1 | 0.5 días | 1.9 |
| 2.6 | Maquetar FAQ (componente accordion) | DEV2 | 0.5 días | 1.9, 1.3 |
| 2.7 | Maquetar Footer + navegación + links legales | DEV2 | 0.5 días | 1.9 |
| 2.8 | Integrar formulario de signup en la landing | DEV1 | 0.5 días | 1.16, 2.1 |
| 2.9 | Implementar animaciones y micro-interacciones | DEV1 | 1 día | 2.1-2.7 |
| 2.10 | Responsive completo (mobile, tablet, desktop) | DEV2 | 1 día | 2.1-2.7 |
| 2.11 | Integrar analytics y eventos de tracking (click CTA, scroll, submit) | DEV2 | 0.5 días | 1.17, 2.8 |
| 2.12 | Revisión visual con Diseñador (pixel perfect) | DIS + DEV1 + DEV2 | 0.5 días | 2.9, 2.10 |

### COP en paralelo durante Fase 2:

| # | Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|---|