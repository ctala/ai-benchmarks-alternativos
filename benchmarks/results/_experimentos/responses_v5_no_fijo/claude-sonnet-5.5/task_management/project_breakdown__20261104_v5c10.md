# Claude Sonnet 5.5 — task_management/project_breakdown

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.06 | quality: 9.8
- latency_total: 50.435s | tokens_per_second: 136.6
- input_tokens: 119 | output_tokens: 6888
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de proyecto: Landing page SaaS de gestión de inventario

## Supuestos

- Landing de una sola página (8-10 secciones) con CTA principal (demo, trial o waitlist).
- Alguien del equipo actúa como **PM/Decisor** (probablemente tú). Es el único que aprueba, porque con 4 semanas no hay margen para aprobaciones por comité.
- Tienes capturas o mockups del producto para la semana 2.
- Stack ligero (Next.js/Astro o Webflow), con hosting tipo Vercel o Netlify.
- 20 días hábiles (D1-D20).

**Roles:** DIS = Diseñador · DEV1 = Frontend · DEV2 = Integraciones/Infra · COP = Copywriter · PM = tú

---

## Visión general del timeline

| Semana | Foco | Hito de salida |
|---|---|---|
| **S1 (D1-5)** | Estrategia, mensajes, wireframes, setup técnico | Wireframes + messaging aprobados |
| **S2 (D6-10)** | Diseño UI, copy v1, base de desarrollo | **Design freeze** (D10) |
| **S3 (D11-15)** | Desarrollo completo, integraciones, copy final | **Feature complete en staging** (D15) |
| **S4 (D16-20)** | QA, optimización, lanzamiento | **Go-live D19**, D20 de buffer |

---

## Fase 1: Descubrimiento y estrategia (D1-D5)

| ID | Tarea | Resp. | Duración | Depende de |
|---|---|---|---|---|
| 1.1 | Kickoff: objetivo, KPI (ej. % conversión), ICP, CTA principal, fecha, canales de lanzamiento | PM (todos) | D1 | - |
| 1.2 | Análisis de 5-8 competidores (mensajes, estructura, pricing, CTAs) | COP + DIS | D1-2 | 1.1 |
| 1.3 | Messaging framework: propuesta de valor, beneficios, objeciones, tono de voz | COP | D2-3 | 1.1, 1.2 |
| 1.4 | Estructura de la página (secciones y orden) | COP + DIS | D3 | 1.3 |
| 1.5 | Decisiones técnicas: stack, hosting, CRM/email, analytics, cookie consent | DEV1 + DEV2 | D1-2 | 1.1 |
| 1.6 | Setup de repo, CI/CD, staging, dominio/DNS | DEV2 | D2-4 | 1.5 |
| 1.7 | Plan de tracking (eventos: clic CTA, envío de form, scroll, etc.) | DEV2 + PM | D3-4 | 1.1 |
| 1.8 | Wireframes low-fi desktop + mobile | DIS | D3-5 | 1.4 |
| 1.9 | **Hito:** aprobación de wireframes y messaging | PM | D5 | 1.3, 1.8 |

## Fase 2: Diseño y contenido (D6-D10)

| ID | Tarea | Resp. | Duración | Depende de |
|---|---|---|---|---|
| 2.1 | Copy v1 de todas las secciones (hero, problema, features, beneficios, social proof, pricing/CTA, FAQ, footer) | COP | D4-7 | 1.3, 1.4 |
| 2.2 | Design system mínimo: colores, tipografía, botones, cards, formularios | DIS | D6-7 | 1.9 |
| 2.3 | UI hi-fi desktop, entregada por secciones (hero + nav primero) | DIS | D6-9 | 1.9, 2.1 |
| 2.4 | UI mobile | DIS | D8-10 | 2.3 |
| 2.5 | Assets: capturas del producto, iconos, ilustraciones, OG image, favicon | DIS | D8-10 | Capturas del producto (PM) |
| 2.6 | Scaffolding del frontend: layout, tokens de diseño, componentes base | DEV1 | D6-7 | 1.6, 2.2 |
| 2.7 | Formulario + integración con CRM/email (con confirmación) | DEV2 | D6-10 | 1.5, 1.7 |
| 2.8 | Páginas legales: privacidad, términos, cookies | COP + PM (legal) | D6-10 | - |
| 2.9 | **Hito: Design freeze.** Después solo se aceptan cambios críticos | PM | D10 | 2.3-2.5 |

## Fase 3: Desarrollo (D8-D15)

| ID | Tarea | Resp. | Duración | Depende de |
|---|---|---|---|---|
| 3.1 | Implementar secciones responsive, a medida que DIS las entrega | DEV1 | D8-14 | 2.3, 2.6 |
| 3.2 | Animaciones y microinteracciones | DEV1 | D13-15 | 3.1 |
| 3.3 | Implementar analytics y eventos, cookie consent | DEV2 | D11-12 | 1.7, 2.7 |
| 3.4 | SEO técnico: meta tags, sitemap, robots, schema, OG tags | DEV2 | D12-13 | 2.1 |
| 3.5 | Optimización de performance: imágenes, fuentes, lazy load | DEV2 | D13-15 | 3.1 |
| 3.6 | Copy v2 final (ajustado al diseño) + microcopy + meta descriptions | COP | D8-11 | 2.1, 2.3 |
| 3.7 | Integración del copy final y páginas legales | DEV1 | D12-13 | 3.6, 2.8 |
| 3.8 | Design QA en staging (fidelidad al diseño) | DIS | D12-15 | 3.1 |
| 3.9 | **Hito: Feature complete en staging** | PM | D15 | 3.1-3.8 |

## Fase 4: QA y optimización (D16-D18)

| ID | Tarea | Resp. | Duración | Depende de |
|---|---|---|---|---|
| 4.1 | QA cross-browser y dispositivos (Chrome, Safari, Firefox, iOS, Android) | DEV2 | D16-17 | 3.9 |
| 4.2 | Auditoría de Lighthouse (>90) y accesibilidad (contraste, teclado, alt text) | DEV1 | D16-17 | 3.9 |
| 4.3 | Test end-to-end: form → CRM → email → evento en analytics | DEV2 | D16 | 3.3 |
| 4.4 | Revisión final de copy (ortografía, consistencia, links) | COP | D16 | 3.9 |
| 4.5 | Ronda de bugs y ajustes | DEV1 + DEV2 | D17 | 4.1-4.4 |
| 4.6 | **Code y content freeze** (fin de D17) | PM | D17 | 4.5 |
| 4.7 | UAT con stakeholders y Go/No-Go | PM | D18 | 4.6 |

## Fase 5: Lanzamiento (D19-D20)

| ID | Tarea | Resp. | Duración | Depende de |
|---|---|---|---|---|
| 5.1 | Deploy a producción, DNS/SSL, redirects, verificación de analytics | DEV2 | D19 AM | 4.7 |
| 5.2 | Smoke test en producción | DEV1 + DEV2 | D19 | 5.1 |
| 5.3 | **Go-live** y comunicación (email, redes, anuncios) | PM + COP | D19 | 5.2 |
| 5.4 | Monitoreo y hotfixes | DEV1 + DEV2 | D19-20 | 5.3 |
| 5.5 | Buffer y primer reporte de métricas | PM | D20 | - |

---

## Ruta crítica

**Kickoff → Messaging → Estructura → Wireframes → Aprobación (D5) → UI hi-fi → Design freeze → Desarrollo de secciones → Feature complete (D15) → QA → Go/No-Go → Launch**

Cualquier retraso en esta cadena mueve el lanzamiento. Las tareas fuera de ella (legal, SEO técnico, tracking) tienen holgura.

## Balance de carga

- **Diseñador:** cuello de botella en S1-S2. Mitigación: entregar por secciones, usar un UI kit o design system existente y limitar el número de rondas de revisión.
- **Developers:** S1 con carga baja. Aprovéchala para infra, tracking, CRM y prototipos de componentes.
- **Copywriter:** carga baja en S3-S4. Que prepare los emails de lanzamiento, posts sociales, textos para ads y el email de bienvenida.

## Riesgos principales

| Riesgo | Prob. | Mitigación |
|---|---|---|
| Aprobaciones lentas | Alta | SLA de 24h y un único decisor |
| Cambios de copy tras el design freeze | Alta | Content freeze en D10 para estructura y longitud. Solo se permiten ajustes de palabras |
| Faltan capturas o mockups del producto | Media | Pedirlos en D1 y usar mockups genéricos como plan B |
| Textos legales a última hora | Media | Usar plantillas desde D6 y revisión legal en paralelo |
| Integración con CRM o email falla | Baja-Media | Empezar en D6, con un fallback simple (Google Sheets o Formspree) |
| Scope creep (blog, pricing interactivo, chatbot) | Alta | Lista "Fase 2" fuera del lanzamiento |
| Lanzar en viernes sin margen | Media | Go-live en D19 y D20 de buffer |

## Alcance recomendado (MVP vs. post-lanzamiento)

**Incluido:** hero, problema/solución, 3-6 features, beneficios, social proof (o waitlist count/logos/beta), pricing o CTA, FAQ, formulario, legales, analytics y SEO básico.

**Para después:** blog, A/B testing, multi-idioma, calculadora de ROI, chat en vivo, video producido, animaciones complejas.

## Ritmo de trabajo sugerido

- **Daily** de 10 min (async si es posible).
- **Demo/revisión** los viernes (D5, D10, D15) con aprobación explícita.
- **Un solo canal** de feedback (por ejemplo, Figma comments + un tablero en Linear o Notion).
- **Definition of Done por tarea:** aprobada por PM y sin dependencias abiertas.

---

Si me confirmas el stack (¿Webflow o código?), el objetivo del CTA (demo, trial o waitlist) y si ya tienes capturas del producto y branding definido, puedo ajustar el plan y convertirlo en un tablero listo para importar (Notion, Linear o Jira).