# Claude Haiku 5.5 — task_management/project_breakdown

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 15.207s | tokens_per_second: 229.0
- input_tokens: 117 | output_tokens: 3482
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría implementar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un desglose del proyecto en 4 semanas, con fases, tareas, responsables, dependencias y timeline. Asumo que el equipo puede dedicar tiempo completo; si no es así, avísame y ajusto.

## Supuestos clave
- Stack web estándar (p. ej., Next.js/WordPress/Webflow) con formulario de captura de leads conectado a un CRM o email marketing.
- El producto ya tiene nombre, propuesta de valor y pricing definidos. Si no, eso es un bloqueo previo a la Semana 1.
- Sin analítica ni pruebas A/B complejas en el lanzamiento; se dejan para iteración posterior.

## Roles
- **D1 – Diseñador (UI/UX)**
- **DEV1 – Developer frontend** (implementación de la página, responsive, performance)
- **DEV2 – Developer backend/integraciones** (formularios, CRM, analítica, hosting/dominio, SEO técnico)
- **C1 – Copywriter** (mensajes, textos, FAQs, microcopy)
- **PM/Owner** (puede ser uno de los anteriores; coordina y aprueba)

---

## FASE 0 – Preparación (Días 1–2)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 0.1 | Definir objetivo de la landing (lista de espera, demo, trial) y KPI principal | PM | — |
| 0.2 | Brief de producto: propuesta de valor, público objetivo, competidores, diferenciadores | PM + C1 | 0.1 |
| 0.3 | Inventario de contenido disponible (screenshots, logos, testimonios, datos) | PM | — |
| 0.4 | Definir stack, hosting, dominio y herramientas (CRM/email/analítica) | DEV2 | 0.1 |
| 0.5 | Kickoff del equipo y calendario de revisiones | PM | — |

**Hito:** brief aprobado y stack decidido (fin Día 2).

---

## FASE 1 – Estrategia y contenido (Días 3–6)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 1.1 | Arquitectura de la página (secciones: hero, problema, solución, features, prueba social, pricing/CTA, FAQ) | C1 + D1 | 0.2 |
| 1.2 | Redacción de copy (headline, subheadline, secciones, CTAs, FAQ) | C1 | 1.1 |
| 1.3 | Wireframes de baja fidelidad | D1 | 1.1 |
| 1.4 | Revisión de wireframes y copy con PM | PM | 1.2, 1.3 |
| 1.5 | Definir eventos de tracking y campos del formulario | DEV2 + PM | 1.4 |
| 1.6 | Setup de repositorio, entorno de staging y dominio | DEV2 | 0.4 |

**Hito:** wireframes y copy aprobados (fin Día 6). Es el punto crítico: cualquier retraso aquí se come el buffer.

---

## FASE 2 – Diseño visual (Días 7–10)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 2.1 | Diseño UI de alta fidelidad desktop | D1 | 1.4 |
| 2.2 | Diseño versión mobile/responsive | D1 | 2.1 |
| 2.3 | Componentes y sistema visual (colores, tipografía, botones) | D1 | 2.1 |
| 2.4 | Ilustraciones/capturas de producto y assets optimizados | D1 | 2.1 |
| 2.5 | Maquetación de copy final en diseño | C1 + D1 | 1.2, 2.1 |
| 2.6 | Revisión de diseño con PM y C1 | PM | 2.2, 2.5 |
| 2.7 | Implementación de estructura base y componentes en código | DEV1 | 1.6, 2.3 (parcial) |
| 2.8 | Integración de formulario de captura (esqueleto) | DEV2 | 1.6 |

**Hito:** diseño aprobado (fin Día 10). DEV1 puede empezar a maquetar en paralelo desde los componentes ya definidos.

---

## FASE 3 – Desarrollo (Días 11–17)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 3.1 | Maquetación completa responsive (desktop + mobile) | DEV1 | 2.6 |
| 3.2 | Animaciones e interacciones ligeras | DEV1 | 3.1 |
| 3.3 | Formulario conectado a CRM/email marketing, validaciones y página de gracias | DEV2 | 2.8 |
| 3.4 | Tracking: analítica, eventos de conversión, píxeles | DEV2 | 1.5, 3.1 |
| 3.5 | SEO on-page: meta tags, Open Graph, schema, sitemap, robots | DEV2 + C1 | 3.1 |
| 3.6 | Optimización de performance (imágenes, lazy load, Core Web Vitals) | DEV1 | 3.1 |
| 3.7 | Cookie banner y política de privacidad / legal | DEV2 + PM | — |
| 3.8 | Páginas legales (términos, privacidad) | C1 + PM | 3.7 |
| 3.9 | Primera revisión interna en staging | PM + D1 | 3.1–3.4 |

**Hito:** versión funcional en staging (fin Día 15). Días 16–17 son para correcciones de la revisión interna.

---

## FASE 4 – QA y pulido (Días 18–21)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 4.1 | QA funcional: formularios, enlaces, CTAs, flujo de conversión | DEV2 | 3.9 |
| 4.2 | QA visual cross-browser y cross-device | D1 + DEV1 | 3.9 |
| 4.3 | Pruebas de performance y accesibilidad (WCAG básico) | DEV1 | 3.6 |
| 4.4 | Revisión final de copy (ortografía, tono, claims legales) | C1 | 3.9 |
| 4.5 | Pruebas de envío de emails transaccionales y entrega en CRM | DEV2 | 3.3 |
| 4.6 | Correcciones priorizadas (bugs críticos y bloqueantes) | Todos | 4.1–4.5 |
| 4.7 | Congelación de código (code freeze) | PM | 4.6 |

**Hito:** code freeze (fin Día 21). A partir de aquí solo bugs críticos.

---

## FASE 5 – Pre-lanzamiento (Días 22–24)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 5.1 | Configuración de producción: dominio, SSL, DNS, redirects | DEV2 | 4.7 |
| 5.2 | Despliegue a producción y verificación | DEV2 | 5.1 |
| 5.3 | Verificación de tracking y conversiones en producción | DEV2 | 5.2 |
| 5.4 | Preparación de materiales de lanzamiento (email, redes, press kit) | C1 + D1 | 4.7 |
| 5.5 | Prueba de carga básica | DEV1 | 5.2 |
| 5.6 | Plan de contingencia (rollback, contacto de soporte, responsable de guardia) | PM | — |

**Hito:** sitio en producción y tracking verificado (fin Día 23). Día 24 es buffer.

---

## FASE 6 – Lanzamiento y post-lanzamiento (Días 25–28)
| # | Tarea | Responsable | Dependencia |
|---|---|---|---|
| 6.1 | Go-live y anuncio | PM + C1 | 5.3 |
| 6.2 | Monitoreo en tiempo real: errores, conversiones, performance | DEV1 + DEV2 | 6.1 |
| 6.3 | Publicación de contenido en canales (email, LinkedIn, etc.) | C1 | 6.1 |
| 6.4 | Recolección de feedback inicial | PM | 6.1 |
| 6.5 | Retrospectiva y backlog de mejoras v2 | PM | 6.4 |

---

## Ruta crítica
**Copy aprobado → Diseño aprobado → Maquetación → Integraciones → QA → Code freeze → Producción.**
Cualquier retraso en la aprobación de copy o diseño afecta directamente al lanzamiento, porque DEV1 depende del diseño final.

## Riesgos principales y mitigación
1. **Aprobaciones lentas** → fechas de revisión fijas en el kickoff y un único decisor.
2. **Dependencia de DEV1 de un diseño incompleto** → trabajar con componentes base desde el Día 7.
3. **Integraciones de CRM que fallan** → probarlas en la Semana 2, no al final.
4. **Legal/privacidad de último minuto** → iniciar 3.7 y 3.8 temprano y no dejarlos para la Semana 4.
5. **Scope creep** → congelar el alcance en la Fase 0; todo lo nuevo va al backlog v2.

## Resumen de hitos
- **Día 2:** brief y stack aprobados
- **Día 6:** wireframes y copy aprobados
- **Día 10:** diseño aprobado
- **Día 15:** staging funcional
- **Día 21:** code freeze
- **Día 23:** producción verificada
- **Día 28:** lanzamiento y monitoreo

Si me dices el stack exacto, el objetivo de la página (lista de espera, demo o trial) y si ya tienes copy o diseño, puedo ajustar el plan y los tiempos.