# Claude Fable 5.1 — task_management/project_breakdown

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.65 | quality: 9.8
- latency_total: 62.046s | tokens_per_second: 81.2
- input_tokens: 119 | output_tokens: 5037
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de lanzamiento: Landing Page SaaS de Gestión de Inventario

**Duración:** 4 semanas (20 días laborables)
**Equipo:** Diseñador (D), Developer 1 (Dev1), Developer 2 (Dev2), Copywriter (C)
**Supuesto clave:** Existe alguien (tú o un PM/fundador) que actúa como owner del producto para aprobar entregables. Lo llamaré **PO**.

---

## Visión general del timeline

| Semana | Fase | Foco principal |
|---|---|---|
| 1 | Descubrimiento y definición | Mensaje, estructura, wireframes, setup técnico |
| 2 | Diseño y copy | Diseño visual final + copy definitivo, desarrollo de base |
| 3 | Desarrollo e integración | Build completo, formularios, analítica, SEO |
| 4 | QA, optimización y lanzamiento | Testing, performance, ajustes, go-live |

---

## FASE 1 — Descubrimiento y definición (Semana 1, días 1–5)

**Objetivo:** Todos alineados en qué se construye, para quién y cómo se mide el éxito. Esta fase es la que más se tiende a saltar y la que más retrabajo evita.

| # | Tarea | Responsable | Días | Depende de | Entregable |
|---|---|---|---|---|---|
| 1.1 | Kickoff: objetivos, KPI (conversión a demo/trial), audiencia, propuesta de valor, competidores | PO + todos | 1 | — | Brief de 1 página |
| 1.2 | Investigación de mensaje: entrevistas rápidas o revisión de llamadas de ventas, pain points del cliente, análisis de competidores | C | 1–3 | 1.1 | Documento de posicionamiento (promesa principal, 3 beneficios, objeciones) |
| 1.3 | Definición de arquitectura de la página (secciones, jerarquía, CTAs) | C + D | 2–3 | 1.1 | Esquema de secciones con copy provisional |
| 1.4 | Wireframes de baja fidelidad (desktop + mobile) | D | 3–5 | 1.3 | Wireframes en Figma |
| 1.5 | Setup técnico: repo, stack, hosting, dominio, SSL, staging, CI/CD | Dev1 | 1–3 | 1.1 | Entorno de staging funcionando |
| 1.6 | Definir integraciones: CRM/email (HubSpot, Mailchimp…), analítica (GA4, Hotjar), formularios, calendario de demos | Dev2 + PO | 2–4 | 1.1 | Lista de integraciones con credenciales y endpoints |
| 1.7 | Revisión y aprobación de wireframes + estructura | PO | 5 | 1.4 | Wireframes aprobados |

**Hito fin de semana 1:** Wireframes aprobados + staging operativo + estrategia de mensaje cerrada.

---

## FASE 2 — Diseño visual y copy (Semana 2, días 6–10)

**Objetivo:** Diseño final y copy definitivo listos para desarrollo. Los devs no esperan: trabajan en componentes base en paralelo.

| # | Tarea | Responsable | Días | Depende de | Entregable |
|---|---|---|---|---|---|
| 2.1 | Copy definitivo: hero, beneficios, features, pricing, FAQ, CTAs, microcopy | C | 6–8 | 1.7 | Doc de copy final por sección |
| 2.2 | Sistema visual: tipografía, colores, componentes, iconografía (si no hay brand guide) | D | 6–7 | 1.7 | Mini design system en Figma |
| 2.3 | Diseño de alta fidelidad desktop | D | 7–9 | 2.2, 2.1 (copy parcial) | Mockups desktop |
| 2.4 | Diseño de alta fidelidad mobile | D | 9–10 | 2.3 | Mockups mobile |
| 2.5 | Assets visuales: mockups del producto, ilustraciones, capturas de la app | D | 8–10 | 2.3 | Assets exportados (SVG/WebP) |
| 2.6 | Construcción de componentes base (layout, grid, navbar, footer, botones, tipografía) a partir del design system | Dev1 | 7–10 | 2.2 | Componentes funcionales en staging |
| 2.7 | Backend de formularios + integración con CRM/email + anti-spam | Dev2 | 6–9 | 1.6 | Endpoint de formulario probado |
| 2.8 | Setup de analítica y tag manager, definición de eventos (clic CTA, envío de formulario, scroll) | Dev2 | 9–10 | 1.6 | Plan de medición implementado en staging |
| 2.9 | Revisión y aprobación de diseño + copy | PO | 10 | 2.3, 2.4, 2.1 | Diseño y copy congelados |

**Hito fin de semana 2:** Diseño y copy aprobados y congelados. Sin cambios estructurales a partir de aquí.

> ⚠️ **Riesgo principal:** el copy y el diseño se retroalimentan (un titular largo rompe el layout). Copywriter y diseñador deben trabajar en sesiones conjuntas los días 7–9, no en secuencia.

---

## FASE 3 — Desarrollo e integración (Semana 3, días 11–15)

**Objetivo:** Página completa, funcional y medible en staging.

| # | Tarea | Responsable | Días | Depende de | Entregable |
|---|---|---|---|---|---|
| 3.1 | Maquetación de secciones (hero, beneficios, features, social proof) | Dev1 | 11–13 | 2.9, 2.6 | Secciones superiores en staging |
| 3.2 | Maquetación de secciones (pricing, FAQ, CTA final, footer) + formularios en front | Dev2 | 11–13 | 2.9, 2.7 | Secciones inferiores en staging |
| 3.3 | Responsive y ajustes mobile/tablet | Dev1 + Dev2 | 13–14 | 3.1, 3.2 | Página responsive completa |
| 3.4 | Animaciones e interacciones (sutiles, sin afectar performance) | Dev1 | 14 | 3.3 | Interacciones implementadas |
| 3.5 | SEO técnico: meta tags, Open Graph, schema.org, sitemap, robots, URLs | Dev2 | 14 | 3.2 | Checklist SEO completado |
| 3.6 | Copy SEO: title, meta description, alt text, textos para redes (OG) | C | 11–12 | 2.9 | Doc de metadatos |
| 3.7 | Página de gracias / confirmación + emails transaccionales (si aplica) | C (texto) + Dev2 (build) | 12–14 | 2.7 | Thank-you page + email de confirmación |
| 3.8 | Preparar materiales de lanzamiento: posts para redes, email a lista de espera, nota para Product Hunt/LinkedIn | C | 13–15 | 2.9 | Kit de lanzamiento |
| 3.9 | QA visual: comparar build vs. diseño, reportar desviaciones | D | 14–15 | 3.3 | Lista de ajustes visuales |
| 3.10 | Página legal: privacidad, cookies, términos (texto puede ser plantilla revisada) | C + Dev2 | 15 | — | Páginas legales publicadas + banner cookies |

**Hito fin de semana 3:** Página completa en staging, con formularios funcionando end-to-end y analítica activa.

---

## FASE 4 — QA, optimización y lanzamiento (Semana 4, días 16–20)

**Objetivo:** Cero errores críticos, performance óptima, lanzamiento controlado.

| # | Tarea | Responsable | Días | Depende de | Entregable |
|---|---|---|---|---|---|
| 4.1 | Corrección de desviaciones visuales reportadas por D | Dev1 | 16 | 3.9 | Ajustes aplicados |
| 4.2 | Testing cross-browser y dispositivos (Chrome, Safari, Firefox, Edge; iOS, Android) | Dev2 + D | 16–17 | 4.1 | Reporte de bugs |
| 4.3 | Performance: Lighthouse > 90, optimización de imágenes, lazy loading, fuentes | Dev1 | 17 | 4.1 | Informe Lighthouse |
| 4.4 | Accesibilidad básica: contraste, navegación por teclado, etiquetas de formulario | Dev2 | 17 | 4.1 | Checklist a11y |
| 4.5 | Test end-to-end de conversión: enviar formulario → llega al CRM → email de confirmación → evento en analítica | Dev2 + PO | 18 | 4.2 | Flujo validado |
| 4.6 | Revisión final de copy en producción (typos, consistencia, enlaces rotos) | C | 18 | 4.1 | Copy aprobado en staging |
| 4.7 | Corrección de bugs de QA | Dev1 + Dev2 | 18 | 4.2, 4.4 | Bugs cerrados |
| 4.8 | Aprobación final (go/no-go) | PO | 19 | 4.5, 4.6, 4.7 | Luz verde |
| 4.9 | Deploy a producción, verificación DNS/SSL, smoke test en vivo | Dev1 | 19 | 4.8 | Página en producción |
| 4.10 | Lanzamiento: envío de emails, publicación en redes, activación de campañas | C + PO | 20 | 4.9 | Lanzamiento ejecutado |
| 4.11 | Monitoreo post-lanzamiento: errores, formularios, analítica, primeras conversiones | Dev2 + PO | 20 | 4.9 | Reporte día 1 |

**Hito final (día 20):** Landing en producción, formularios recibiendo leads, analítica reportando.

---

## Mapa de dependencias críticas (ruta crítica)

```
Kickoff (1.1)
   └→ Posicionamiento (1.2) → Arquitectura (1.3) → Wireframes (1.4) → Aprobación (1.7)
                                                                              │
                              ┌───────────────────────────────────────────────┤
                              ↓                                               ↓
                    Copy final (2.1) ←──────────────→ Diseño HiFi (2.3, 2.4)
                              └──────────────┬────────────────────────────────┘
                                             ↓
                                  Aprobación diseño+copy (2.9)  ← PUNTO DE CONGELACIÓN
                                             ↓
                                  Maquetación (3.1, 3.2) → Responsive (3.3)
                                             ↓
                                   QA (4.2) → Fixes (4.7) → Go/No-go (4.8) → Deploy (4.9)
```

**Si algo se retrasa en la ruta crítica, el lanzamiento se mueve.** Las tareas con margen (slack) son: setup técnico, integraciones, kit de lanzamiento, páginas legales.

---

## Carga de trabajo por persona

| Persona | Sem 1 | Sem 2 | Sem 3 | Sem 4 |
|---|---|---|---|---|
| **Copywriter** | Investigación + arquitectura | Copy final (pico) | SEO copy + kit lanzamiento | Revisión + lanzamiento |
| **Diseñador** | Wireframes | Diseño HiFi (pico) | QA visual + assets | Testing dispositivos |
| **Dev1** | Setup infra | Componentes base | Maquetación superior (pico) | Performance + deploy |
| **Dev2** | Integraciones | Formularios + analítica | Maquetación inferior + SEO (pico) | QA + monitoreo |

---

## Riesgos y mitigaciones

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Cambios de copy/diseño después del día 10 | Alta | Punto de congelación explícito. Cambios post-freeze van a un backlog "v1.1" |
| Falta de social proof (testimonios, logos) para un producto nuevo | Alta | Decidir en semana 1: usar beta users, cifras del producto, o eliminar la sección |
| Aprobaciones del PO que tardan | Media | Agendar las 3 reuniones de aprobación (días 5, 10, 19) desde el kickoff |
| Integración con CRM más compleja de lo previsto | Media | Dev2 la valida en semana 1; fallback: formulario a hoja de cálculo + Zapier |
| Capturas del producto no listas (producto en desarrollo) | Media | Diseñador crea mockups estilizados en lugar de screenshots reales |
| Performance pobre por imágenes/animaciones | Baja | Presupuesto de peso definido desde diseño (< 1.5 MB página inicial) |

---

## Rituales recomendados

- **Daily de 10 min** (async en Slack vale): qué hice, qué haré, bloqueos.
- **Revisión de mitad de semana** (miércoles, 30 min): ajustar prioridades.
- **Demo de fin de semana** (viernes, 30 min): mostrar avance al PO y aprobar hitos.

---

## Qué dejar fuera del alcance (para proteger las 4 semanas)

- Blog o páginas secundarias (excepto legales)
- A/B testing (se configura post-lanzamiento con datos reales)
- Múltiples idiomas
- Chat en vivo (puede añadirse en 1 hora post-lanzamiento con un script)
- Calculadora de ROI o demos interactivas

---

¿Quieres que convierta esto en un formato específico (Notion, Trello, Gantt en hoja de cálculo) o que profundice en alguna fase, por ejemplo la estructura exacta de secciones y el copy del hero?