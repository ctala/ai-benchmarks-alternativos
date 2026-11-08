# Claude Sonnet 5.5 — task_management/project_breakdown

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.98 | quality: 9.7
- latency_total: 50.483s | tokens_per_second: 139.3
- input_tokens: 119 | output_tokens: 7033
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de proyecto: Landing page SaaS de gestión de inventario

## 1. Supuestos

- 20 días laborables (4 semanas). **Listo para producción el día 18**, con 2 días de colchón.
- Alguien (probablemente tú) actúa como **PM/decisor único**: aprueba entregables y desbloquea al equipo. Si no, asigna ese rol explícitamente.
- Landing de **una sola página** con formulario de demo o waitlist.
- Stack sugerido: Next.js o Astro, con hosting en Vercel o Netlify. Si el equipo domina Webflow o similar, puede ahorrar 3-4 días.
- El producto tiene al menos una UI navegable de la que sacar capturas (si no, ver Riesgos).

**Alcance MVP:** Hero, social proof, problema/solución, features, cómo funciona, pricing o CTA, FAQ, footer, formulario de captación, páginas legales.
**Fuera de alcance (post-lanzamiento):** blog, multi-idioma, demo interactiva, A/B tests.

---

## 2. Fases y tareas

**Responsables:** PM = tú, DIS = diseñador, DEV1/DEV2 = developers, COP = copywriter.

### Fase 0 · Estrategia y kickoff (Semana 1, días 1-3)

| ID | Tarea | Resp. | Días | Depende de |
|---|---|---|---|---|
| A1 | Kickoff y brief (objetivo, audiencia, KPI, CTA principal) | PM + todos | D1 | - |
| A2 | Análisis rápido de competencia y posicionamiento | COP + DIS | D1-2 | - |
| A3 | Documento de messaging: propuesta de valor, objeciones, pruebas, tono | COP | D2-3 | A1, A2 |
| A4 | Sitemap y estructura de secciones | COP + DIS | D3 | A3 |
| A5 | Decisión de stack, repo, CI/CD, hosting, dominio, staging | DEV1 | D1-2 | A1 |
| A6 | Plan de analítica (eventos, conversiones, UTM) | DEV2 + PM | D2-3 | A1 |

**Entregable:** brief aprobado, messaging doc, estructura de la página.

### Fase 1 · Diseño y contenido (Semana 1-2, días 3-10)

| ID | Tarea | Resp. | Días | Depende de |
|---|---|---|---|---|
| B1 | Wireframes low-fi (desktop + mobile) | DIS | D3-4 | A4 |
| B2 | **Aprobación de wireframes** | PM + COP + DEVs | D5 (mañana) | B1 |
| B3 | UI kit: tipografía, colores, botones, componentes | DIS | D5-6 | B2 |
| B4 | Copy v1 completo por sección | COP | D4-8 | A3, B1 |
| B5 | Diseño hi-fi: hero, features, CTA | DIS | D6-8 | B3 |
| B6 | Diseño hi-fi: resto de secciones + mobile | DIS | D8-10 | B5 |
| B7 | Visuales de producto (capturas, mockups, iconos) | DIS | D7-10 | acceso a UI del producto |
| B8 | Revisión de copy con stakeholders y v2 | COP + PM | D9-10 | B4 |
| B9 | **Aprobación de diseño (design freeze)** | PM | D10 | B6, B7 |
| B10 | Páginas legales (privacidad, cookies, términos) | PM / legal | D6-10 | - |

**Entregable:** diseño final aprobado y copy v2.

### Fase 2 · Desarrollo (Semana 1-3, días 3-15)

| ID | Tarea | Resp. | Días | Depende de |
|---|---|---|---|---|
| C1 | Base del proyecto: layout, rutas, componentes base, design tokens | DEV1 | D3-6 | A5, B3 (parcial) |
| C2 | Formulario + integración CRM/email (HubSpot, Mailchimp, etc.) + email de confirmación | DEV2 | D3-8 | A5, A6 |
| C3 | Implementación lote 1: nav, hero, social proof, features | DEV1 | D7-10 | B5, C1 |
| C4 | SEO técnico: meta, OG, sitemap, robots, schema, favicon | DEV2 | D8-10 | A4 |
| C5 | Banner de cookies + carga condicional de analítica | DEV2 | D9-10 | A6, B10 |
| C6 | Implementación lote 2: cómo funciona, pricing/CTA, FAQ, footer | DEV1 | D11-13 | B6, B9 |
| C7 | Integración de copy final | DEV1 + COP | D11-14 | B8 |
| C8 | Eventos de analítica y tracking de conversión | DEV2 | D11-13 | C2, A6 |
| C9 | Responsive fino, animaciones, optimización de imágenes | DEV1 + DEV2 | D13-15 | C6 |
| C10 | Design QA en staging (revisión pixel a pixel) | DIS | D12-15 | C3, C6 |
| C11 | **Feature complete + content freeze** | PM | D15 | C6-C10 |

### Fase 3 · QA y optimización (Semana 4, días 16-18)

| ID | Tarea | Resp. | Días | Depende de |
|---|---|---|---|---|
| D1 | QA funcional: formulario, links, CTAs, emails, tracking | DEV2 | D16-17 | C11 |
| D2 | Cross-browser y dispositivos (Chrome, Safari, Firefox, iOS, Android) | DEV1 + DIS | D16-17 | C11 |
| D3 | Performance y accesibilidad (Lighthouse >90, contraste, teclado, alt) | DEV1 | D16-17 | C11 |
| D4 | Corrección ortográfica y de tono, revisión de microcopy | COP | D16 | C11 |
| D5 | Corrección de bugs | DEVs | D17-18 | D1-D4 |
| D6 | **Sign-off final** | PM | D18 | D5 |

### Fase 4 · Lanzamiento (días 18-20)

| ID | Tarea | Resp. | Días | Depende de |
|---|---|---|---|---|
| E1 | DNS, SSL, redirects, monitorización (uptime, errores) | DEV1 | D18 | D6 |
| E2 | Preparar comunicación de lanzamiento (email, LinkedIn, anuncio) | COP + DIS | D15-18 | B8 |
| E3 | **Go-live** y smoke test en producción | DEVs + PM | D19 | E1 |
| E4 | Anuncio y difusión | COP + PM | D19-20 | E3, E2 |
| E5 | Colchón para imprevistos / hotfixes | Todos | D20 | - |

---

## 3. Vista de carga por semana

| | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
|---|---|---|---|---|
| **PM** | Brief, KPIs, aprobar wireframes | Revisiones, legales, aprobar diseño | Desbloquear, content freeze | Sign-off, go-live |
| **COP** | Messaging, estructura, copy v1 | Copy v2, revisión | Integración, SEO copy, microcopy | Proofreading, comunicación de lanzamiento |
| **DIS** | Wireframes, UI kit, inicio hi-fi | Hi-fi completo, mobile, visuales | Design QA, assets finales, OG images | QA visual, material de lanzamiento |
| **DEV1** | Infra, base del proyecto | Lote 1 de secciones | Lote 2, responsive | Performance, bugs, DNS |
| **DEV2** | Analítica, formulario/CRM | SEO técnico, cookies | Eventos, tracking, animaciones | QA funcional, bugs |

---

## 4. Ruta crítica

**Messaging (A3) → Wireframes (B1-B2) → UI kit y hi-fi (B3-B6) → Aprobación de diseño (B9) → Desarrollo lote 2 (C6) → Feature complete (C11) → QA (D1-D5) → Go-live**

Cualquier retraso en esta cadena mueve el lanzamiento. Las tareas de infraestructura, integraciones, legales y SEO técnico tienen holgura.

## 5. Hitos de control

| Día | Hito | Criterio |
|---|---|---|
| D3 | Messaging y estructura aprobados | Documento firmado por el PM |
| D5 | Wireframes aprobados | Sin cambios estructurales después |
| D10 | **Design freeze** | Cambios posteriores solo por bug |
| D15 | **Feature complete + content freeze** | Todo en staging |
| D18 | Sign-off | Checklist de QA al 100% |
| D19 | **Go-live** | Smoke test OK |

---

## 6. Riesgos y mitigaciones

| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| Feedback de stakeholders lento o contradictorio | Alta | Alto | Un único decisor y ventana de feedback de 24h. Los cambios tras un freeze requieren aprobación explícita |
| No hay capturas reales del producto a tiempo | Media | Alto | Pedir acceso a la UI el D1. Plan B: mockups ilustrados y reemplazo posterior |
| El diseñador es cuello de botella (D5-D10) | Alta | Alto | Entregar por lotes (hero primero), reutilizar un UI kit simple y que los devs empiecen con componentes base |
| Scope creep (blog, pricing complejo, idiomas) | Alta | Medio | Mantener la lista "fuera de alcance" y revisarla cada viernes |
| Integración con CRM/email más compleja de lo esperado | Media | Medio | Empezar el D3, con webhook o Zapier como plan B |
| Claims sin pruebas (testimonios, métricas) | Media | Medio | Pedir testimonios o datos beta desde la semana 1. Si no hay, usar propuesta de valor y garantías en lugar de social proof inventado |
| Problemas legales (cookies, RGPD) | Baja | Alto | Plantillas estándar en la semana 2 y revisión legal antes del D15 |
| Bugs de última hora | Media | Medio | QA iniciado el D16 y colchón de 2 días |

---

## 7. Checklist de lanzamiento

- [ ] Formulario envía datos al CRM y llega el email de confirmación
- [ ] Analítica y conversiones verificadas en producción
- [ ] Banner de cookies y páginas legales activos
- [ ] Meta tags, OG image y favicon correctos (probar al compartir en LinkedIn/Slack)
- [ ] Lighthouse >90 en mobile
- [ ] Probado en iOS Safari y Android Chrome
- [ ] SSL, redirects (www/no-www) y 404 configurados
- [ ] Monitorización de uptime activa
- [ ] Copy de anuncio listo
- [ ] Plan de rollback definido

---

## 8. Recomendaciones

1. **Dedica el D1 a cerrar el KPI y el CTA.** Una landing sin un único objetivo de conversión se diluye.
2. **Evita lanzar en viernes.** Si la fecha es fija, haz go-live el D19 y usa el D20 para monitorizar.
3. **Reuniones:** daily de 10 minutos, revisión de entregables los miércoles y demo interna los viernes.
4. **Aprovecha la holgura:** los devs tienen margen en la semana 1 (úsalo para infraestructura y componentes) y el copywriter en las semanas 3-4 (úsalo para SEO, emails de lanzamiento y contenido post-lanzamiento).
5. **Post-lanzamiento (semana 5):** revisa los datos de conversión, mapas de calor y preguntas frecuentes, y planifica el primer A/B test (normalmente el titular del hero).

Si me dices el stack preferido, si hay pricing público y si tienes ya branding, puedo ajustar el plan o convertirlo en un tablero listo para Notion, Jira o Trello.