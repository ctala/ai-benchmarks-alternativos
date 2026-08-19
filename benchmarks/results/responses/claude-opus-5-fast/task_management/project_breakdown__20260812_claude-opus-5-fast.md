# Claude Opus 5 Fast — task_management/project_breakdown

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.56 | quality: 9.2
- latency_total: 11.043s | tokens_per_second: 185.4
- input_tokens: 117 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado del proyecto con fases, tareas, dependencias y responsables.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de lanzamiento — Landing Page SaaS de Inventario
**Duración:** 4 semanas (20 días hábiles, D1–D20) · **Equipo:** 1 Diseñador (DIS), 2 Devs (DEV1 frontend / DEV2 integraciones), 1 Copywriter (CW) + tú como PM/decisor

---

## 0. Bloqueantes a resolver en el Día 0 (antes de arrancar)

Si estos puntos no están cerrados, el plan de 4 semanas no se sostiene:

| Decisión | Por qué bloquea |
|---|---|
| Objetivo único de conversión (waitlist / demo agendada / free trial) | Define arquitectura de la página, formularios e integraciones |
| ¿Hay producto funcional para capturas/video? | Sin visuales reales, el diseño se detiene o se rellena con mockups genéricos |
| ¿Se publica pricing? | Una sección de pricing añade ~2 días entre diseño, copy y QA |
| Stack y dominio confirmados | DEV2 no puede montar infra el D1 |
| Un solo aprobador con SLA de 24h | Las revisiones lentas son la causa #1 de retraso en estos proyectos |

---

## 1. Alcance

**Dentro:** landing de una página (hero, problema/solución, 3–5 features, cómo funciona, prueba social, pricing, FAQ, CTA final, footer), página de gracias, formulario conectado a CRM, analítica y eventos, SEO on-page, legales (privacidad/cookies/términos), responsive, 2 variantes de hero para test posterior.

**Fuera (fase 2):** blog, multiidioma, portal de clientes, comparativas vs. competidores, calculadora de ROI, chat en vivo, integración de pagos.

Documenta esto por escrito. El scope creep es el riesgo dominante en un plan de 4 semanas.

---

## 2. Fases

| Fase | Días | Objetivo | Hito de salida |
|---|---|---|---|
| F1 · Estrategia y mensaje | D1–D3 | Posicionamiento, ICP, estructura | Mensaje y wireframe aprobados |
| F2 · Copy y diseño | D4–D9 | Copy final + UI alta fidelidad | Diseño congelado (design freeze) |
