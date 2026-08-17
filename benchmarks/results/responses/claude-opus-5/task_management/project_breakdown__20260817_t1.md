# Claude Opus 5 — task_management/project_breakdown

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.69 | quality: 9.7
- latency_total: 80.148s | tokens_per_second: 71.6
- input_tokens: 117 | output_tokens: 5737
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de lanzamiento — Landing Page SaaS de Inventario (4 semanas)

## Supuestos (valídalos el Día 1; cambian el plan si son falsos)

1. **Alcance:** landing de 1 página (+ 2 legales: privacidad y términos). No hay app, login ni dashboard en este scope.
2. **Objetivo del CTA:** captar leads (demo o trial). Si el trial requiere self-serve signup + billing, **el plan no cabe en 4 semanas** con este equipo.
3. **Marca:** existe logo y paleta básica. Si hay que crear identidad desde cero, suma 1 semana.
4. **Stack:** Next.js + Tailwind + Vercel, formularios a CRM (HubSpot/Pipedrive), analítica GA4 + Hotjar. Sin CMS o con CMS ligero.
5. **Pricing definido antes del Día 3.** Es el bloqueador silencioso #1 de este tipo de proyectos.
6. **Un único decisor** aprueba diseño y copy en <24h.

---

## Equipo y foco

| Rol | Alias | Responsabilidad principal |
|---|---|---|
| Diseñador | **DIS** | UX, wireframes, UI hi-fi, assets, design system mínimo |
| Developer 1 | **DEV1** | Frontend / maquetado / componentes / responsive |
| Developer 2 | **DEV2** | Infra, CI/CD, integraciones (CRM, analytics), SEO técnico, performance |
| Copywriter | **COP** | Research, mensaje, copy, microcopy, SEO on-page |
| Product Owner | **PO** | Decisiones de scope, pricing, aprobaciones (tú) |

**Cuello de botella del proyecto: DIS.** Todo el build depende de su output. Por eso el diseño se entrega **por secciones**, no en un único paquete final.

---

## Ruta crítica

```
Oferta + pricing → Mensaje/value prop → Wireframe → UI hi-fi → Maquetado → QA → Deploy
```

Cualquier retraso aquí se traslada 1:1 a la fecha de lanzamiento. Todo lo demás (infra, analytics, assets, legales) es paralelizable y **no debe bloquear**.

---

## SEMANA 1 — Estrategia y estructura
**Meta:** salir del viernes con mensaje y estructura congelados.

| Día | Tarea | Resp. | Depende de |
|---|---|---|---|
| D1 | Kickoff: objetivo, ICP, KPI, CTA primario, competidores de referencia | Todos | — |
| D1 | Definir oferta y **pricing** (o decisión explícita de "pricing = contactar ventas") | PO | — |
| D1–D2 | Research: 3–5 competidores, entrevistas con ventas/soporte, extracción de dolores reales | COP | D1 |
| D1–D2 | Setup técnico: repo, CI/CD, staging, dominio, tokens de diseño base | DEV2 | — |
| D2–D3 | Message house: promesa principal, 3 beneficios, objeciones, prueba social | COP | Research |
| D3 | **Aprobación de mensaje** (30 min, PO) | PO | Message house |
| D3–D5 | Wireframes lo-fi de todas las secciones + jerarquía de página | DIS | Mensaje aprobado |
| D3–D5 | Copy v1 de secciones críticas: hero, beneficios, cómo funciona, pricing, FAQ | COP | Mensaje aprobado |
| D3–D5 | Elegir librería de componentes, definir arquitectura, formulario dummy funcional en staging | DEV1 | Setup |
| D5 | **Review conjunta + freeze de estructura y copy v1** | Todos | — |

> **Riesgo D1–D3:** si no hay screenshots reales del producto, DIS y DEV quedan sin assets clave en Semana 3. Pide capturas o mockups del producto **el Día 1**.

---

## SEMANA 2 — Diseño hi-fi y arranque del build
**Meta:** hero y beneficios ya maquetados el viernes.

| Día | Tarea | Resp. | Depende de |
|---|---|---|---|
| D6–D7 | UI hi-fi: hero + navegación + beneficios (desktop y mobile) | DIS | Wireframes |
| D8–D9 | UI hi-fi: cómo funciona, pricing, testimonios, FAQ, footer | DIS | — |
| D6–D8 | Copy v2 final + microcopy (botones, labels, estados de error, thank-you page) | COP | Freeze D5 |
| D6–D8 | Integraciones: CRM, GA4 + eventos, consentimiento de cookies, email de confirmación | DEV2 | Setup |
| D8–D10 | Maquetado de hero + beneficios (secciones ya aprobadas) | DEV1 | Hi-fi parcial |
| D9 | Meta títulos, descripciones, keywords, estructura de H1–H3 | COP | Copy v2 |
| D10 | **Design freeze.** Cambios posteriores entran a un backlog post-lanzamiento | PO / DIS | — |

**Regla de oro:** DIS entrega secciones aprobadas de forma incremental (D7 y D9), no un archivo completo el D10. Sin esto, DEV1 arranca tarde y la Semana 4 se rompe.

---

## SEMANA 3 — Build completo
**Meta:** code complete el viernes, sitio navegable en staging.

| Día | Tarea | Resp. | Depende de |
|---|---|---|---|
| D11–D14 | Maquetado del resto de secciones + responsive + estados hover/focus | DEV1 | Design freeze |
| D11–D13 | Assets finales: screenshots del producto, iconografía, ilustraciones, OG image, favicon | DIS | Hi-fi |
| D11–D13 | SEO técnico: sitemap, robots, schema (Organization, Product, FAQ), redirects | DEV2 | — |
| D12–D14 | Formulario en producción: validaciones, anti-spam, thank-you page, tracking de conversión | DEV2 | Integraciones |
| D13–D14 | Optimización: imágenes WebP, lazy load, fuentes, Core Web Vitals | DEV2 | Maquetado parcial |
| D13–D15 | Revisión de copy implementado (typos, saltos de línea, viudas, coherencia) | COP | Maquetado |
| D14 | Textos legales: privacidad, términos, aviso de cookies | PO / COP | — |
| D15 | **Code complete → staging estable.** Feature freeze | DEV1 / DEV2 | — |
| D11–D15 | *Trabajo paralelo COP:* secuencia de emails de bienvenida, copy de ads, post de anuncio, guion de video corto | COP | Copy v2 |

---

## SEMANA 4 — QA, pulido y lanzamiento
**Meta:** lanzar el D20 por la mañana, con 2 días de colchón ya integrados.

| Día | Tarea | Resp. | Depende de |
|---|---|---|---|
| D16 | QA funcional: formularios, links, CTAs, tracking end-to-end, email recibido | DEV2 + PO | Staging |
| D16 | QA visual: Chrome/Safari/Firefox/Edge, iOS, Android, 320px–1920px | DIS + DEV1 | Staging |
| D16 | QA accesibilidad: contraste, foco, alt text, navegación por teclado, jerarquía semántica | DIS + DEV1 | Staging |
| D17 | Triage de bugs (P0/P1/P2) + fixes P0 y P1 | DEV1 / DEV2 | QA |
| D17 | Lighthouse: objetivo ≥90 performance, ≥95 SEO y a11y en mobile | DEV2 | Fixes |
| D18 | **Aprobación final de stakeholders** (sesión única, 1h, lista cerrada de cambios) | PO | — |
| D18 | Últimos ajustes de copy y pulido visual | COP / DIS | Aprobación |
| D19 | **Buffer / ensayo de deploy:** DNS, SSL, deploy a producción con noindex, smoke test completo | DEV2 | — |
| D19 | Pre-launch checklist firmada | Todos | — |
| **D20 AM** | **LANZAMIENTO:** quitar noindex, Search Console, verificación de analítica, smoke test en producción | DEV2 | Checklist |
| D20 PM | Monitoreo activo, hotfixes, activación de ads/email/redes | Todos | Launch |
| D21 | Retro + backlog v1.1 + primer reporte de métricas | Todos | Launch |

> Lanza **martes o miércoles por la mañana**. Nunca un viernes: si algo se rompe, nadie estará disponible.

---

## Riesgos principales y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Pricing no definido a tiempo | Alto — bloquea copy y diseño | Deadline D3. Plan B: sección "Solicitar cotización" |
| Sin screenshots del producto | Alto — hero sin visual | Pedir D1. Plan B: mockups ilustrados por DIS |
| Aprobaciones lentas / stakeholders tardíos | Alto | Ventanas fijas de review (D3, D10, D18). Silencio = aprobado |
| DIS saturado (único diseñador) | Alto | Entrega incremental + design system mínimo, no pixel-perfect |
| Scope creep (blog, chat, calculadora ROI, multi-idioma) | Alto | Freeze D10. Todo lo nuevo va a backlog v1.1 |
| Sin testimonios ni logos reales | Medio | Usar métricas del producto o beta-testers; nunca inventar |
| Integración CRM más compleja de lo previsto | Medio | Prototipo funcional en D8, no en D14 |

---

## Si vas tarde, recorta en este orden

1. Animaciones y microinteracciones → CSS estático
2. Ilustraciones custom → librería de ilustraciones licenciadas
3. Video demo → GIF o screenshots anotados
4. Sección de comparativa con competidores → post-lanzamiento
5. CMS → contenido hardcodeado
6. Blog / recursos → v1.1

**No recortes nunca:** QA mobile, tracking de conversión, velocidad de carga, textos legales.

---

## Definition of Done (por tarea)

- **Diseño:** desktop + mobile, todos los estados, tokens documentados, aprobado por PO
- **Copy:** revisado, sin typos, con meta tags, aprobado por PO
- **Dev:** responsive, cross-browser, Lighthouse ≥90 mobile, sin errores en consola, PR revisado por el otro dev

---

## Métricas a medir desde el D20

| Métrica | Referencia inicial |
|---|---|
| Conversión visitante → lead | 2–5% (landing SaaS B2B) |
| Bounce rate | <60% |
| Scroll depth al pricing | >40% |
| LCP mobile | <2.5s |
| Lead → demo agendada | >30% |

Instrumenta eventos de: click en CTA (hero, medio, footer), envío de formulario, scroll 50%/90%, click en pricing.

---

## Los 3 puntos de control que determinan si llegas

- **D3** — mensaje y pricing aprobados
- **D10** — design freeze
- **D15** — code complete

Si fallas cualquiera de los tres, mueve la fecha de lanzamiento el mismo número de días. No comprimas la Semana 4: es donde se detecta lo que rompería el lanzamiento.

¿Quieres que profundice en alguna fase, o que ajuste el plan asumiendo self-serve signup con billing en lugar de captación de leads?