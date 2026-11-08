# Grok 4.7 — task_management/project_breakdown

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 36.517s | tokens_per_second: 49.7
- input_tokens: 1308 | output_tokens: 1816
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

**Plan de 4 semanas** para una landing de lanzamiento de SaaS de inventario, con 1 diseñador, 2 developers y 1 copywriter. El alcance realista es una página de conversión (hero, problema, producto, features, social proof, pricing, FAQ, CTA, formulario/waitlist o trial), no un sitio completo ni el producto en sí.

## Supuestos
- Dominio, hosting y analytics básicos disponibles en la semana 1.
- No hay brand book cerrado: el diseñador define un sistema mínimo.
- El copywriter escribe en el idioma de lanzamiento; legal (privacidad, términos) es un borrador corto, no un contrato final.
- Developers: uno en frontend/página, otro en formularios, tracking, CMS ligero o deploy.
- Fuera de alcance: app del producto, blog, A/B testing avanzado, integraciones complejas.

## Roles
| Rol | Foco |
|---|---|
| Diseñador | Estructura, UI, assets, handoff |
| Dev A | Landing, responsive, performance |
| Dev B | Formulario, email, analytics, deploy, SEO técnico |
| Copywriter | Mensaje, secciones, microcopy, SEO on-page |

## Fases, tareas y dependencias

### Fase 0 — Alineación (días 1–2)
| Tarea | Responsable | Depende de |
|---|---|---|
| Objetivo único (trial, demo o waitlist) y métrica norte (signups) | Todos, lead informal | — |
| ICP, propuesta de valor, 3 objeciones, competidores | Copywriter + equipo | Objetivo |
| Sitemap de una página y jerarquía de CTAs | Diseñador + copy | Mensaje base |
| Stack: framework, hosting, dominio, herramienta de forms/email | Dev A + Dev B | — |
| Checklist legal mínima (privacidad, cookies) | Copy + Dev B | Stack |

### Fase 1 — Mensaje y estructura (días 2–6)
| Tarea | Responsable | Depende de |
|---|---|---|
| Outline por sección y titulares | Copywriter | Fase 0 |
| Wireframe low-fi (desktop + mobile) | Diseñador | Outline |
| Inventario de prueba social (logos, quotes, métricas reales o “coming soon” honesto) | Copywriter | ICP |
| Copy v1 de todas las secciones + meta title/description | Copywriter | Wireframe aprobado |
| Definir eventos: pageview, CTA click, form submit, error | Dev B | Objetivo |

**Gate:** wireframe + copy v1 aprobados antes de UI final. Si no, el diseño se rehace.

### Fase 2 — Diseño (días 6–12)
| Tarea | Responsable | Depende de |
|---|---|---|
| UI kit mínimo (tipo, color, botones, cards, form) | Diseñador | Wireframe |
| Diseño desktop de la landing | Diseñador | Copy v1 |
| Mobile y estados (hover, error, success, loading) | Diseñador | Desktop |
| Assets: ilustración o screenshots del producto, OG image, favicon | Diseñador | UI |
| Handoff (medidas, componentes, assets exportados) | Diseñador | Mobile listo |

En paralelo, Dev A puede montar el esqueleto técnico desde el wireframe (no esperar al pixel-perfect).

### Fase 3 — Build (días 8–18, solapada)
| Tarea | Responsable | Depende de |
|---|---|---|
| Repo, CI, preview deploys, dominio staging | Dev B | Stack |
| Layout, secciones, responsive | Dev A | Wireframe; luego handoff |
| Componentes reutilizables y accesibilidad básica (contraste, focus, labels) | Dev A | UI kit |
| Formulario, validación, doble opt-in o CRM, página de gracias | Dev B | Copy de form + eventos |
| Analytics, pixels si aplican, consentimiento de cookies | Dev B | Eventos definidos |
| SEO técnico: title, meta, OG, canonical, sitemap, velocidad | Dev B | Copy final de metas |
| Performance (imágenes, fonts, LCP) | Dev A | Assets |

### Fase 4 — Contenido final e integración (días 16–22)
| Tarea | Responsable | Depende de |
|---|---|---|
| Copy v2 tras ver el diseño real (cortar, no añadir secciones) | Copywriter | Build en staging |
| Microcopy: botones, errores, emails de confirmación | Copywriter | Formulario |
| Revisión visual pixel y estados vacíos | Diseñador | Staging |
| QA funcional cruzado (Chrome, Safari, Firefox; móvil real) | Dev A + Dev B | Staging estable |
| Revisión de claims: nada que el producto no haga el día 1 | Copywriter | — |

### Fase 5 — Launch (días 23–28)
| Tarea | Responsable | Depende de |
|---|---|---|
| Freeze de contenido (día 23) | Copywriter | QA de copy |
| Bugfix solo P0/P1 | Devs | QA |
| DNS, SSL, redirects, monitoreo de uptime | Dev B | Freeze |
| Smoke test en producción (formulario real, eventos) | Dev B + Copy | Go-live |
| Página de gracias y email de bienvenida activos | Dev B + Copy | Formulario |
| Retro de 30 min y backlog post-launch (no antes del día 28) | Todos | Launch |

## Timeline

| Semana | Qué termina | Quién está al límite |
|---|---|---|
| **1** | Mensaje, wireframe, copy v1, repo y staging vacío, plan de tracking | Copywriter y diseñador |
| **2** | UI desktop + mobile, esqueleto implementado, form en staging | Diseñador; Dev A arranca build |
| **3** | Página completa en staging, analytics, copy v2, QA mayor | Los dos devs |
| **4** | Freeze día 23, fixes, go-live día 26–27, buffer día 28 | Devs en contención; copy solo typos |

Hitos duros: **fin semana 1** (mensaje cerrado), **fin semana 2** (diseño aprobado), **día 23** (content freeze), **día 26–27** (producción). El día 28 es buffer, no feature day.

## Dependencias críticas
1. Copy v1 bloquea UI final.
2. UI + assets bloquean pulido visual, no el esqueleto.
3. Eventos y destino del formulario bloquean “launch de verdad”: una landing sin captura no lanza.
4. Claims del producto bloquean el freeze: si inventario aún no tiene una feature, no se promete en el hero.
5. DNS/SSL no se dejan para el mismo día del anuncio.

## Riesgos y recortes si se atrasa
- **Semana 2 sin diseño aprobado:** lanzar con sistema visual más simple; no abrir secciones nuevas.
- **Sin testimonios reales:** usar captura de producto y beneficios concretos; no inventar logos ni cifras.
- **Formulario inestable:** priorizar email de espera antes que integraciones (Slack, CRM complejo).
- **Scope creep:** blog, calculadora, chat y multi-idioma quedan para después del día 28.
- **Un dev enfermo:** Dev A se queda con la página; Dev B con form + deploy. El diseñador no entra a código salvo exports.

## Definición de hecho
Landing en producción, móvil usable, un CTA principal, formulario que entrega el lead, email de confirmación, eventos básicos visibles, privacidad enlazada, LCP razonable y cero claims falsos. Con este equipo, eso cabe en 4 semanas si el freeze del día 23 se respeta.