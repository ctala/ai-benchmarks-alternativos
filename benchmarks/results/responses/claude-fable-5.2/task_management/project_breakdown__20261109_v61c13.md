# Claude Fable 5.2 — task_management/project_breakdown

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.6 | quality: 9.5
- latency_total: 58.724s | tokens_per_second: 105.4
- input_tokens: 119 | output_tokens: 6188
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de lanzamiento de la landing page (4 semanas)

Este plan cubre 20 días laborables (D1–D20), con el equipo dedicado casi a tiempo completo.

**Supuestos:**
- La identidad de marca ya existe (logo, colores).
- El alcance es una sola landing con formulario, página de gracias y páginas legales.
- Alguien actúa como PM y aprobador, que supongo que eres tú. Sin un único responsable de aprobaciones, el plan se retrasa.

## Resumen por semana

| Semana | Diseñador | Copywriter | Dev A (frontend) | Dev B (integraciones) | Hito |
|---|---|---|---|---|---|
| 1 | Assets, wireframe | Brief de mensajes, copy v1 | Stack, repo, staging | Formulario + CRM | **D5:** wireframe y copy aprobados |
| 2 | Diseño visual desktop y móvil | Copy final, SEO, emails | Estructura base, hero | Analítica, cookies | **D10:** diseño aprobado |
| 3 | Assets finales, revisión en staging | Emails, redes, textos legales | Secciones, responsive | Página de gracias, SEO, rendimiento | **D15:** página completa en staging |
| 4 | QA visual | Revisión de textos | Bugs, deploy | QA, prueba end-to-end | **D20:** lanzamiento |

## Fase 1: Estrategia (D1–D2)

| ID | Tarea | Responsable | Días | Depende de |
|---|---|---|---|---|
| 1.1 | Kickoff: objetivo, público, CTA único (demo, trial o lista de espera), KPI | Todos (lidera PM) | D1 | — |
| 1.2 | Brief de mensajes: propuesta de valor, beneficios, objeciones | Copywriter | D1–D2 | 1.1 |
| 1.3 | Elegir stack, hosting, dominio, CRM/email y analítica | Dev A + Dev B | D1–D2 | 1.1 |
| 1.4 | Reunir assets: marca, capturas del producto, testimonios, logos de clientes | Diseñador | D1–D3 | 1.1 |

## Fase 2: Contenido y wireframe (D2–D5)

| ID | Tarea | Responsable | Días | Depende de |
|---|---|---|---|---|
| 2.1 | Estructura de secciones (hero, beneficios, funcionalidades, prueba social, FAQ, CTA) | Copywriter + Diseñador | D2–D3 | 1.2 |
| 2.2 | Wireframe desktop y móvil | Diseñador | D3–D4 | 2.1 |
| 2.3 | Copy v1 completo | Copywriter | D3–D5 | 2.1 |
| 2.4 | Repo, CI/CD y entorno de staging | Dev A | D2–D4 | 1.3 |
| 2.5 | Formulario e integración con CRM/email | Dev B | D3–D7 | 1.3 |
| 2.6 | Aprobación de wireframe y copy v1 (Hito 1) | PM | D5 | 2.2, 2.3 |

## Fase 3: Diseño visual (D6–D10)

| ID | Tarea | Responsable | Días | Depende de |
|---|---|---|---|---|
| 3.1 | Hero y sistema de estilos (tipografía, colores, componentes) | Diseñador | D6–D7 | 2.6 |
| 3.2 | Resto de secciones en desktop | Diseñador | D8–D9 | 3.1 |
| 3.3 | Versión móvil y estados (hover, errores de formulario) | Diseñador | D9–D10 | 3.2 |
| 3.4 | Copy final, microcopy y meta SEO | Copywriter | D6–D8 | 2.6 |
| 3.5 | Maquetación de la estructura base con el copy aprobado | Dev A | D6–D8 | 2.4, 2.6 |
| 3.6 | Aprobación del diseño (Hito 2) | PM | D10 | 3.3 |

## Fase 4: Desarrollo (D8–D15)

El desarrollo se solapa con el diseño. El hero se entrega en D7 para que Dev A no espere al diseño completo.

| ID | Tarea | Responsable | Días | Depende de |
|---|---|---|---|---|
| 4.1 | Implementar hero y estilos base | Dev A | D8–D10 | 3.1, 3.5 |
| 4.2 | Implementar el resto de secciones | Dev A | D11–D13 | 3.6 |
| 4.3 | Responsive e interacciones | Dev A | D13–D15 | 4.2 |
| 4.4 | Analítica, eventos de conversión, píxeles, banner de cookies | Dev B | D8–D10 | 2.4 |
| 4.5 | Emails de confirmación y lanzamiento, posts de redes, textos legales | Copywriter | D9–D14 | 3.4 |
| 4.6 | Página de gracias, email automático, páginas legales | Dev B | D11–D13 | 2.5, 4.5 |
| 4.7 | SEO técnico, rendimiento, etiquetas OG | Dev B | D13–D15 | 4.2 |
| 4.8 | Exportar assets, imágenes OG, revisión de diseño en staging | Diseñador | D11–D15 | 3.6 |

**Hito 3 (D15):** página completa en staging.

## Fase 5: QA y lanzamiento (D16–D20)

| ID | Tarea | Responsable | Días | Depende de |
|---|---|---|---|---|
| 5.1 | QA en navegadores y dispositivos | Dev B + Diseñador | D16–D17 | Hito 3 |
| 5.2 | Revisión de textos en staging | Copywriter | D16 | Hito 3 |
| 5.3 | Corrección de bugs | Dev A + Dev B | D17–D18 | 5.1, 5.2 |
| 5.4 | Prueba end-to-end: formulario → CRM → email → analítica | Dev B | D18 | 5.3 |
| 5.5 | Go/no-go y congelación de cambios | PM | D18 | 5.4 |
| 5.6 | Deploy a producción, DNS, SSL (soft launch) | Dev A | D19 | 5.5 |
| 5.7 | Lanzamiento público y monitorización | Todos | D20 | 5.6 |

## Ruta crítica

Kickoff → brief → estructura → wireframe → aprobación → diseño visual → aprobación → maquetación → QA → deploy.

El diseñador es el cuello de botella, porque cualquier retraso suyo entre D3 y D10 desplaza todo lo demás. El único colchón real es D19, así que conviene protegerlo.

## Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Aprobaciones lentas | Un solo aprobador, con 24 h máximo de respuesta y como mucho dos rondas de cambios por hito |
| Capturas del producto no disponibles | Confirmarlo en D1. Si el producto no está listo, usar mockups desde el principio |
| Ampliación del alcance (más páginas, blog, animaciones complejas) | Lo que no esté en este plan pasa a una versión posterior al lanzamiento |
| Textos legales y cookies (RGPD o normativa local) | Encargarlos en la semana 1, no en la 4 |
| Cambios de copy tras el diseño | Congelar la estructura en D5 y admitir después solo ajustes de texto |

Si me dices el stack previsto (Webflow/Framer o código a medida) y el CTA principal, puedo ajustar el plan. Con una herramienta no-code, la fase de desarrollo se acorta varios días y ganas margen para QA.