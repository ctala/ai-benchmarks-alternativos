# Muse Spark 1.2 — task_management/project_breakdown

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 11.01s | tokens_per_second: 224.9
- input_tokens: 69 | output_tokens: 2476
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Para lanzar en 4 semanas con ese equipo, este es el plan más realista y sin cuellos de botella. Está pensado para trabajar en paralelo y con solapamiento de fases.

### Plan Maestro: Landing SaaS Gestión de Inventario
**Duración:** 28 días | **Equipo:** 1 Diseñador, 2 Developers, 1 Copywriter
**Metodología:** Sprints semanales + Daily de 15 min

#### FASE 1: ESTRATEGIA Y PLANIFICACIÓN - Semana 1 [Día 1 al 7]
Objetivo: Alinear a todo el equipo antes de diseñar o programar nada.

| Tarea | Responsable | Dependencia | Entregable |
| :--- | :--- | :--- | :--- |
| 1.1 Kickoff: Definir Buyer Persona, Propuesta de Valor y Objetivo de la landing | Todos | Ninguna | Brief del proyecto |
| 1.2 Benchmark de competencia y definición de estructura | Diseñador + Copywriter | 1.1 | Sitemap y Wireframes en baja |
| 1.3 Definir arquitectura, secciones y CTAs | Copywriter + Diseñador | 1.2 | Wireframe final validado |
| 1.4 Definir Stack Técnico, dominio, hosting y herramientas | Dev 1 + Dev 2 | 1.1 | Stack definido: Ej. Next.js/Webflow + HubSpot/Mailchimp + GA4 |
| 1.5 Keyword research y estructura SEO base | Copywriter | 1.1 | Lista de keywords y metadatos |

> **HITO 1 - Día 7:** Wireframes aprobados y stack listo. Si esto se atrasa, todo se atrasa.

#### FASE 2: CONTENIDO Y DISEÑO - Semana 2 [Día 8 al 14]
Objetivo: Tener todo el material visual y textual listo. Aquí copy y diseño trabajan en paralelo con feedback diario.

| Tarea | Responsable | Dependencia | Duración |
| :--- | :--- | :--- | :--- |
| 2.1 Copywriting: Headlines, beneficios, features, pricing, FAQ, CTAs | Copywriter | 1.3 | Día 8-11 |
| 2.2 Diseño UI en Figma: Desktop, Mobile y Sistema de Diseño | Diseñador | 1.3 y 2.1 | Día 8-14 |
| 2.3 Revisión y aprobación de copy + diseño | Todos | 2.1 y 2.2 | Día 13-14 |
| 2.4 Preparación de assets: Iconos, ilustraciones, mockups del producto | Diseñador | 2.2 | Día 12-14 |
| 2.5 Setup inicial del proyecto por Devs | Dev 1 + Dev 2 | 1.4 | Día 12-14 |

> **Ruta Crítica:** El Copy `2.1` debe entregarse el Día 11 como máximo. Si el copy se atrasa, el diseño se bloquea.

#### FASE 3: DESARROLLO Y CONSTRUCCIÓN - Semana 3 [Día 15 al 21]
Objetivo: Maquetar y conectar todo. Es la fase más intensa.

| Tarea | Responsable | Dependencia | Duración |
| :--- | :--- | :--- | :--- |
| 3.1 Maquetación Front-end responsive | Dev 1 | 2.3 | Día 15-19 |
| 3.2 Integraciones Back-end: Formulario, CRM, Email Marketing, Automatizaciones | Dev 2 | 2.3 | Día 15-19 |
| 3.3 Implementación de Analytics, Pixel, GA4, Hotjar, SEO técnico | Dev 2 | 3.1 | Día 19-20 |
| 3.4 Animaciones, optimización de carga y efectos | Dev 1 | 3.1 | Día 20-21 |
| 3.5 Carga de contenido final y optimización de imágenes | Dev 1 + Copywriter | 2.3 y 3.1 | Día 20-21 |

> **Trabajo en paralelo:** Dev 1 se encarga del Front, Dev 2 de integraciones. No deben esperar el uno al otro.

#### FASE 4: QA, OPTIMIZACIÓN Y LANZAMIENTO - Semana 4 [Día 22 al 28]
Objetivo: Pulir, probar y lanzar sin errores. Deja 2 días de colchón.

| Tarea | Responsable | Dependencia | Duración |
| :--- | :--- | :--- | :--- |
| 4.1 Testing QA: Cross-browser, responsive, velocidad, formularios | Dev 1 + Dev 2 + Diseñador | 3.5 | Día 22-23 |
| 4.2 Test de conversión y UX: Test A/B de Headline/CTA, prueba con 5 usuarios | Diseñador + Copywriter | 4.1 | Día 23-24 |
| 4.3 Ajustes finales de copy, diseño y performance | Todos | 4.2 | Día 24-25 |
| 4.4 Checklist Legal y SEO: Política privacidad, cookies, sitemap, Search Console | Dev 2 + Copywriter | 4.1 | Día 25 |
| 4.5 **SOFT LAUNCH + Lanzamiento Oficial** | Todos | 4.3 y 4.4 | Día 26-27 |
| 4.6 Monitoreo post-lanzamiento y plan de iteración | Todos | 4.5 | Día 28 |

### Timeline Visual - Diagrama Gantt Simplificado

```
Semana 1 [PLAN]      |███████|
Semana 2 [DISEÑO]    |       |████████|
Semana 3 [DEV]       |               |████████|
Semana 4 [QA+LAUNCH] |                       |███████|
Tareas               D1  D7  D11 D14 D19 D21 D28
Hitos                    ^H1      ^H2      ^H3  ^LANZAMIENTO
```

### 3 Reglas para que no se retrase

1.  **Validación en 24h:** Toda entrega de copy o diseño debe ser aprobada en máximo 24 horas. Sin aprobación, no se avanza.
2.  **Copy primero, diseño después:** El diseñador no puede diseñar una sección sin el copy final de esa sección.
3.  **Colchón de 2 días:** Los días 26-27 son para imprevistos. Si todo va bien, los usas para preparar campaña de ads/email.

### Herramientas Recomendadas
*   **Gestión:** Notion / Trello / Asana
*   **Diseño:** Figma
*   **Comunicación:** Slack + Daily de 15 min a las 9:00 AM
*   **Desarrollo:** Webflow para lanzar rápido o Next.js + Vercel si necesitas escalabilidad

¿Quieres que te convierta este plan en una plantilla lista para importar a Notion o Trello con todas las tareas asignadas y fechas automáticas?