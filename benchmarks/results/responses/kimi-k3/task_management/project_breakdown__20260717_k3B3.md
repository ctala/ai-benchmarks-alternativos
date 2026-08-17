# Kimi K3 — task_management/project_breakdown

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 98.918s | tokens_per_second: 32.9
- input_tokens: 159 | output_tokens: 3251
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un desglose detallado y estructurado del proyecto con tareas, responsables y un cronograma realista.

## Respuesta completa

# Plan de lanzamiento: Landing page SaaS (4 semanas)

**Principio clave:** con 4 semanas y un equipo de 4, no puedes trabajar en cascada pura. Las fases se solapan: los devs empiezan setup e infraestructura mientras diseño y copy avanzan, y el desarrollo comienza sección por sección a medida que se aprueban diseños.

---

## Fase 0 — Estrategia y brief (Semana 1, días 1-2)

| Tarea | Responsable | Dependencia |
|-------|-------------|-------------|
| Definir objetivo de conversión principal (¿demo, trial, waitlist?) | Todo el equipo + decisor de producto | Ninguna — es la decisión #1 |
| Propuesta de valor y público objetivo | Copywriter (lidera), todos aportan | — |
| Benchmark rápido de competencia (3-5 referencias) | Diseñador + Copywriter | — |
| Arquitectura de la página: secciones y jerarquía (5-7 secciones máx.) | Copywriter + Diseñador | Propuesta de valor |

**Entregable:** brief aprobado + mapa de secciones. Sin esto, nada avanza.

---

## Fase 1 — Contenido y diseño (Semana 1 día 3 → Semana 2)

**Copywriter:**
- Draft completo de textos (Semana 1, días 3-5) → *depende de la arquitectura*
- Revisión y aprobación de copy (Semana 2, días 1-2)
- Microcopy: formularios, mensajes de éxito/error, CTAs (Semana 2, días 3-5)

**Diseñador:**
- Wireframes baja fidelidad (Semana 1, días 3-5) → *depende de la arquitectura*
- Diseño alta fidelidad desktop (Semana 2, días 1-3) → *depende de wireframes + draft de copy*
- Adaptación mobile, estados interactivos, assets (Semana 2, días 4-5)

**Devs (en paralelo):**
- Setup: repo, hosting, framework, CI/CD (Semana 1)
- Base del sistema de diseño: tipografía, colores, componentes (inicio de Semana 2, con wireframes)
- Decisión e implementación temprana de integraciones: formulario → CRM/herramienta de email (Semana 2)

---

## Fase 2 — Desarrollo (Semana 2 día 4 → Semana 3)

| Tarea | Responsable | Dependencia |
|-------|-------------|-------------|
| Header, hero, secciones superiores | Dev 1 | Diseño aprobado por sección |
| Secciones inferiores, footer, FAQ | Dev 2 | Diseño aprobado por sección |
| Formularios + integración CRM/email | Dev 2 | Decisión de herramienta (Sem 2) |
| Responsive + animaciones ligeras | Dev 1 | Componentes base |
| Analytics + eventos de conversión | Dev 2 | Objetivo de conversión definido |
| QA visual continuo y ajustes | Diseñador | Secciones implementadas |
| Metas SEO, OG tags, textos legales | Copywriter | — |

**Regla de oro:** no esperar al diseño completo. Aprobar y desarrollar por bloques (hero primero, footer al final).

---

## Fase 3 — QA y lanzamiento (Semana 4)

- **Días 1-2:** QA completo — browsers, dispositivos, formulario end-to-end (todos)
- **Días 1-3 (paralelo):** performance (imágenes, lazy loading, Core Web Vitals) — Dev 1; SEO técnico (sitemap, robots, redirects) — Dev 2
- **Día 3:** soft launch en producción sin promoción → verificar analytics y formularios en vivo
- **Día 4:** fixes finales *(buffer)*
- **Día 5:** lanzamiento oficial

---

## Vista semanal por persona

| Semana | Diseñador | Dev 1 | Dev 2 | Copywriter |
|--------|-----------|-------|-------|------------|
| **1** | Benchmark, wireframes | Setup, boilerplate | Setup, investigar integraciones | Estrategia, arquitectura, draft completo |
| **2** | Alta fidelidad + mobile | Componentes base, hero | Formularios, integraciones | Aprobación copy, microcopy |
| **3** | QA visual, assets | Secciones, responsive | Animaciones, analytics | Metas SEO, FAQ, legales |
| **4** | Fixes visuales | Performance, QA | SEO técnico, QA | Verificación final de textos |

---

## Ruta crítica

Brief → Arquitectura → Wireframes + Copy draft → Diseño alta fidelidad → Desarrollo por secciones → QA → Launch

## Riesgos principales y mitigación

1. **Aprobaciones lentas** — el riesgo #1 en proyectos así. Define un único decisor y feedback con deadline de 24h.
2. **Screenshots del producto** — si el SaaS no está listo para capturas, decide en Semana 1 si usas mockups o ilustraciones.
3. **Integraciones al final** — probar el formulario y analytics en Semana 2, no en la 4.
4. **Scope creep** — 5-7 secciones es lo realista. Todo extra va a una lista "post-launch".

¿Quieres que profundice en alguna fase, o que adapte el plan si el objetivo es waitlist vs. demo (cambia la integración y los eventos de conversión)?