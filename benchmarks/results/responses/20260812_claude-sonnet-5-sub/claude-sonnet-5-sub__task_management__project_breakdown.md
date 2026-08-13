# Claude Sonnet 5 (suscripción) — task_management/project_breakdown

- model_id: `claude-sonnet-5`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 48.735s | tokens_per_second: 63.4
- input_tokens: 2 | output_tokens: 3090
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto con responsabilidades y dependencias claras.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Landing page SaaS inventario — Plan de lanzamiento (4 semanas)

Con 4 personas y 20 días hábiles, el cuello de botella real es la **aprobación secuencial** (copy→diseño→dev→QA en cadena mata el plazo). La estructura de abajo corre cosas en paralelo desde el día 1 y deja el diseño como bloqueador único de dev.

## Fase 0 — Brief y alineación (Día 1, medio día)

| Tarea | Responsable | Depende de |
|---|---|---|
| Definir propuesta de valor, ICP, objeción principal, CTA único | Tú + copywriter | — |
| Definir stack técnico (framework, hosting, form/CRM destino) | Devs | — |
| Referencias visuales / competencia (3-5 landings SaaS inventario) | Diseñador | — |

Sin esto todo lo demás se hace a ciegas. No lo saltes aunque presione el plazo.

## Fase 1 — Estrategia y contenido base (Días 2-5)

| Tarea | Responsable | Dependencia | Entregable |
|---|---|---|---|
| Wireframe de baja fidelidad (estructura, no visual) | Diseñador | Fase 0 | Wireframe aprobado día 5 |
| Copy draft (headline, subheads, bullets, FAQ, CTAs) | Copywriter | Fase 0 (en paralelo con wireframe) | Doc de copy v1 |
| Setup técnico: repo, CI/CD, dominio, analytics, boilerplate | Devs | Fase 0 | Entorno dev listo |

**Dependencia crítica:** el wireframe necesita saber cuánto copy va en cada sección, así que copywriter y diseñador deben sincronizar a mitad de esta fase (día 3-4), no al final.

## Fase 2 — Diseño visual + copy final (Días 6-10)

| Tarea | Responsable | Dependencia |
|---|---|---|
| UI hi-fi (desktop + mobile) sobre wireframe aprobado | Diseñador | Wireframe |
| Copy final integrado al diseño (ajuste de longitud real) | Copywriter | UI hi-fi en progreso |
| Componentes base reutilizables (nav, footer, botones, form) | Dev 1 | Setup técnico |
| Integración de form → CRM/waitlist + tracking events | Dev 2 | Setup técnico |

Aquí los devs NO esperan el diseño final — construyen la capa técnica que es agnóstica al visual definitivo. Esto es lo que compra los días.

**Gate obligatorio, fin de día 10:** diseño hi-fi aprobado. Si no está aprobado, la Fase 3 arranca con riesgo de retrabajo.

## Fase 3 — Build (Días 11-16)

| Tarea | Responsable | Dependencia |
|---|---|---|
| Maquetación completa sobre diseño aprobado | Dev 1 + Dev 2 | Gate Fase 2 |
| Copy cargado + microcopy (errores de form, estados vacíos, confirmaciones) | Copywriter | Build en progreso |
| Responsive + estados (hover, loading, error) | Diseñador (QA visual) + devs | Build |
| SEO técnico básico (meta tags, OG image, schema, sitemap) | Dev 2 | Build |

## Fase 4 — QA y pre-lanzamiento (Días 17-19)

| Tarea | Responsable | Dependencia |
|---|---|---|
| QA funcional (form, tracking, links, cross-browser) | Devs | Build completo |
| QA visual (pixel-check vs diseño, mobile real device) | Diseñador | Build completo |
| Proofread final de copy (ortografía, consistencia de tono, CTAs) | Copywriter | Build completo |
| Test de carga/performance (Lighthouse, Core Web Vitals) | Dev | Build completo |
| Staging → aprobación final tuya | Todos | QA pasado |

## Fase 5 — Lanzamiento (Día 20)

| Tarea | Responsable |
|---|---|
| Deploy a producción | Dev |
| Verificación post-deploy (form real, analytics disparando, dominio) | Dev + tú |
| Anuncio / activación de canales de tráfico | Tú |

## Timeline resumido

```
Semana 1: Brief + Wireframe + Copy draft + Setup técnico
Semana 2: Diseño hi-fi + Copy final + Componentes/integraciones
Semana 3: Build completo
Semana 4: QA + Pre-lanzamiento + Deploy
```

## Riesgos reales de este plan

1. **El gate de fin de Fase 2 (día 10) es el punto de mayor riesgo.** Si el diseño no está aprobado ese día, cada día de atraso ahí se lo come directo la Fase 3 — no hay margen para absorberlo en 4 semanas. Si sientes que va a atrasarse, la decisión se toma el día 8, no el día 10.
2. **No hay buffer explícito.** El plan usa los 20 días completos. Si necesitas margen real, corta scope (ej. FAQ o testimonios se agregan post-lanzamiento) antes que correr timeline.
3. **Aprobaciones tuyas son parte del camino crítico.** Si tardas 2 días en aprobar wireframe o diseño hi-fi, el plan completo se corre 2 días. Define de antemano un SLA de 24h para tus propias aprobaciones.
4. **Nadie está asignado como QA de contenido cruzado con negocio** (¿el copy dice lo que el producto realmente hace?). Si no lo revisas tú en Fase 2, ese gap sale recién en QA — muy tarde para reescribir sin atrasar.

¿Quieres que arme esto como tablero (Notion/Trello/Linear) con fechas calendario exactas, o prefieres que ajustemos el scope si el equipo tiene otras cosas corriendo en paralelo estas 4 semanas?