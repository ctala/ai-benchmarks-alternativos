# Claude Sonnet 5 — task_management/project_breakdown

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.14 | quality: 9.8
- latency_total: 21.096s | tokens_per_second: 97.1
- input_tokens: 117 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de Lanzamiento: Landing Page SaaS Inventario
## Timeline: 4 semanas | Equipo: 1 Diseñador, 2 Devs, 1 Copywriter

---

## 📋 FASE 0: Kickoff y Definición (Día 1-2)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Definir propuesta de valor, buyer persona, mensajes clave | Copywriter + Founder/PM | 1 día | Ninguna |
| Research de competencia (3-5 landings de referencia) | Diseñador + Copywriter | 1 día | Ninguna |
| Definir estructura de secciones (wireframe conceptual) | Diseñador | 1 día | Propuesta de valor |
| Setup técnico: repo, stack, dominio, hosting | Dev 1 | 1 día | Ninguna |

**Entregable:** Brief aprobado + estructura de secciones definida.

---

## ✍️ FASE 1: Contenido y Diseño (Semana 1)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Copywriting: hero, beneficios, features, CTA, FAQ | Copywriter | 3 días | Brief aprobado |
| Wireframes de baja fidelidad (todas las secciones) | Diseñador | 2 días | Estructura definida |
| Selección de paleta, tipografía, sistema visual | Diseñador | 1 día | En paralelo con wireframes |
| Revisión copy + ajuste con diseño (mensajes cortos que encajen en UI) | Diseñador + Copywriter | 1 día | Copy + wireframes listos |

**Entregable:** Wireframes aprobados + copy final (v1).

⚠️ **Riesgo crítico:** Si el copy se retrasa, todo se retrasa. Dar prioridad absoluta aquí.

---

## 🎨 FASE 2: Diseño UI Final (Semana 2, días 1-3)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Diseño UI alta fidelidad (desktop) | Diseñador | 2 días | Wireframes + copy aprobados |
| Diseño UI responsive (mobile/tablet) | Diseñador | 1 día | UI desktop aprobado |
| Preparar assets (iconos, ilustraciones, exportables) | Diseñador | Paralelo | — |
| Setup de componentes/estructura de código base | Dev 1 + Dev 2 | 2 días | En paralelo (no bloqueante) |

**Entregable:** Diseño Figma final aprobado por stakeholders.

---

## 💻 FASE 3: Desarrollo (Semana 2 día 4 - Semana 3)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Maquetación secciones estáticas (hero, features, pricing) | Dev 1 | 3 días | Diseño UI aprobado |
| Maquetación secciones interactivas (FAQ, testimonios, formularios) | Dev 2 | 3 días | Diseño UI aprobado |
| Integración formulario (waitlist/demo) + CRM o email tool | Dev 2 | 1 día | Formularios maquetados |
| Responsive + cross-browser testing | Dev 1 + Dev 2 | 2 días | Maquetación completa |
| Integración analytics (GA4, Hotjar/Clarity, Pixel) | Dev 1 | 1 día | En paralelo |
| SEO técnico básico (meta tags, sitemap, OG images) | Dev 1 + Copywriter | 1 día | Copy final |

**Entregable:** Landing funcional en staging.

---

## 🚀 FASE 4: QA y Pre-Launch (Semana 4, días 1-3)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| QA visual (pixel-perfect vs diseño) | Diseñador | 1 día | Staging listo |
| QA funcional (links, forms, CTAs, tracking) | Dev 1 + Dev 2 | 1 día | Staging listo |
| Revisión final de copy (typos, tono, legal/disclaimers) | Copywriter | 1 día | En paralelo |
| Test de velocidad (PageSpeed, Core Web Vitals) | Dev 1 | 0.5 día | QA funcional |
| Ajustes finales post-QA | Todo el equipo | 1 día | Feedback QA |

**Entregable:** Landing lista para producción, sin bugs críticos.

---

## 🎯 FASE 5: Lanzamiento (Semana 4, días 4-5)

| Tarea | Responsable | Duración | Dependencia |
|---|---|---|---|
| Deploy a producción | Dev 1 | 0.5 día | QA aprobado |
| Verificación final post-deploy (smoke test) | Dev 2 | 0.5 día | Deploy completo |
| Configurar redirecciones/dominio final | Dev 1 | 0.5 día | Deploy completo |
| Preparar anuncios (social, email, comunidad) | Copywriter | Paralelo (semana 3-4) | — |
| **LANZAMIENTO 🎉** | Todo el equipo | Día 20 | Todo lo anterior |

---

## 📅 Timeline Visual (Gantt simplificado)

```
Semana 1: [Kickoff][Copy+Wireframes.....][Revisión]
Semana 2: [Diseño UI Final...][Dev Setup][Desarrollo inicia →]
Semana 3: [Desarrollo continúa..............][Testing]
Semana 4: [QA][Ajustes][Deploy][🚀 LAUNCH]
```

---

## ⚠️ Riesg