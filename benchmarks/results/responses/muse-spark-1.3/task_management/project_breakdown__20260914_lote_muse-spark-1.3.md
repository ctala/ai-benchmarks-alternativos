# Muse Spark 1.3 — task_management/project_breakdown

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 24.25s | tokens_per_second: 126.3
- input_tokens: 69 | output_tokens: 3062
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto con tareas, responsables y un cronograma realista.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Perfecto, con ese equipo y 4 semanas es totalmente viable si trabajas en paralelo y defines bien el camino crítico. Aquí tienes un plan realista para una landing SaaS de gestión de inventario.

### Objetivo y Alcance

**Objetivo:** Landing de alta conversión para captar early adopters / demos.
**Estructura de la landing:** Hero + Logos / Social Proof + Problema/Solución + Features (stock tiempo real, multi-almacén, alertas, reportes) + Cómo funciona + Integraciones + Pricing teaser + Testimonios + FAQ + CTA Final (Prueba 14 días / Agendar demo) + Footer.

**Stack recomendado para ir rápido:** Figma + Next.js / Webflow + Tailwind + Vercel + Form (HubSpot / Mailchimp) + GA4 + Hotjar/Clarity + CookieYes.

**Roles:**
* **PM (Tú):** Product Owner, decisiones y aprobaciones
* **D:** Diseñador UX/UI
* **DEV1:** Frontend
* **DEV2:** Backend / Integraciones / Performance / SEO técnico
* **CW:** Copywriter

---

### Plan por Fases y Timeline

**Hito clave:** No esperes a terminar una fase para empezar la siguiente. El copy y el diseño trabajan con borradores desde el día 2.

#### FASE 1: Estrategia y Fundación - Semana 1 (Día 1-7)
Objetivo: Que todos sepan QUÉ vender y A QUIÉN.

| Tarea | Responsable | Apoyo | Dependencia | Deadline |
| :--- | :--- | :--- | :--- | :--- |
| 1.1 Kickoff: propuesta de valor, buyer persona, CTA principal, KPIs (CVR >3%, LCP <2.5s) | PM | Todos | - | Día 1 |
| 1.2 Investigación: 5 competidores (Katana, Cin7, Fishbowl), keywords SEO "software gestión inventario" | CW | PM | 1.1 | Día 3 |
| 1.3 Arquitectura de la página y wireframe low-fi en Figma | D | CW | 1.1, 1.2 | Día 5 |
| 1.4 Setup técnico: repo, hosting Vercel, dominio staging, GA4, Search Console | DEV1 + DEV2 | - | 1.1 | Día 5 |
| 1.5 Copy V1: headlines, beneficios, FAQ, metatitles | CW | D | 1.2, 1.3 | Día 7 |
| **MILESTONE M1:** Wireframe + Copy V1 aprobados | PM | - | - | **Día 7** |

#### FASE 2: Diseño UI y Contenido Final - Semana 2 (Día 8-14)
Objetivo: Tener el diseño listo para desarrollar sin frenazos.

| Tarea | Responsable | Apoyo | Dependencia | Deadline |
| :--- | :--- | :--- | :--- | :--- |
| 2.1 Sistema visual: colores, tipografías, botones, ilustraciones / mockups del dashboard | D | - | 1.3 | Día 10 |
| 2.2 Diseño UI Desktop High-Fi en Figma (todas las secciones) | D | CW | 1.5, 2.1 | Día 12 |
| 2.3 Copy V2 final adaptado a diseño + prueba social (3 testimonios beta, logos) | CW | PM | 2.2 | Día 13 |
| 2.4 Diseño Responsive Mobile + prototipo navegable + handoff a devs | D | DEV1 | 2.2 | Día 14 |
| 2.5 Preparar assets: iconos, imágenes comprimidas, video demo 60s (si existe) | D | CW | 2.2 | Día 14 |
| **MILESTONE M2:** Diseño UI Aprobado y congelado | PM | - | - | **Día 14** |

> Regla de oro: A partir del día 14, **cero cambios de diseño** salvo bugs. Todo cambio va a backlog post-lanzamiento.

#### FASE 3: Desarrollo en Paralelo - Semana 2 a 3 (Día 10-21)
Los devs no esperan al día 14, empiezan con la base el día 10.

| Tarea | Responsable | Apoyo | Dependencia | Deadline |
| :--- | :--- | :--- | :--- | :--- |
| 3.1 Maquetación base: header/footer, grid, responsive, CMS para FAQ/pricing | DEV1 | DEV2 | 1.3, 1.4 | Día 14 |
| 3.2 Secciones principales: Hero, Features, Cómo funciona, Integraciones | DEV1 | D | 2.2 | Día 18 |
| 3.3 Integraciones críticas: formulario demo/prueba, HubSpot/Mailchimp, Calendly, GA4 eventos, pixel | DEV2 | CW | 1.4 | Día 18 |
| 3.4 SEO técnico + performance: metatags, Open Graph, schema FAQ, sitemap, compresión imágenes, lazy load | DEV2 | CW | 2.3 | Día 20 |
| 3.5 Animaciones, A/B test Hero (2 variantes headline), legal RGPD/cookies | DEV1 + DEV2 | D | 3.2 | Día 21 |
| **MILESTONE M3:** Beta en staging lista para QA | DEVs | - | - | **Día 21** |

#### FASE 4: QA, Optimización y Lanzamiento - Semana 4 (Día 22-28)

| Tarea | Responsable | Apoyo | Dependencia | Deadline |
| :--- | :--- | :--- | :--- | :--- |
| 4.1 QA funcional: cross-browser (Chrome/Safari/mobile), formularios, links, 404 | DEV2 | D | M3 | Día 23 |
| 4.2 QA contenido y UX: proofreading, test con 5 usuarios (hotjar), test velocidad PageSpeed | CW + D | DEV1 | M3 | Día 24 |
| 4.3 Fix de bugs y congelación de código | DEV1 + DEV2 | - | 4.1, 4.2 | Día 25 |
| 4.4 Pre-launch: checklist SEO, analytics test, backup, dominio final, SSL | DEV2 | PM | 4.3 | Día 26 |
| 4.5 Soft Launch + anuncio (LinkedIn, Product Hunt draft, email a waitlist) | PM + CW | Todos | 4.4 | Día 27-28 |
| **MILESTONE M4: GO-LIVE** | PM | - | - | **Día 28** |

### Mapa de Dependencias (Camino Crítico)

```
1.1 Kickoff -> 1.3 Wireframe -> 2.2 Diseño UI -> 3.2 Maquetación secciones -> 4.1 QA -> GO-LIVE
             -> 1.5 Copy V1 -> 2.3 Copy Final -> 3.3 Formularios/CRM -> 4.1 QA -> GO-LIVE
```

Si se retrasa el **Diseño UI (Día 14)** o el **Copy Final (Día 13)**, se retrasa todo. Esas son tus tareas a proteger.

### Cadencia de Trabajo Realista

Para no quemar al equipo pequeño:
* **Lunes 15 min:** Planning semanal (PM)
* **Daily 15 min async por Slack:** Ayer / Hoy / Bloqueo
* **Viernes 30 min:** Demo + Aprobación (Día 7, 14, 21, 28). El PM debe aprobar en <24h.
* Diseñador carga pico Semana 2. Devs carga pico Semana 3. Copywriter carga pico Semana 1-2, luego solo QA.

### Riesgos y Cómo Mitigarlos

1.  **Cambios de scope de última hora:** Congela diseño el día 14.
2.  **Formulario / CRM falla:** DEV2 lo prueba el día 18 con emails reales, no el 27.
3.  **Sin testimonios reales:** CW prepara placeholders con datos beta / "diseñado con 20 gestores de almacén" + logos de integraciones (Shopify, WooCommerce, SAP).
4.  **Performance pobre:** Presupuesto: <1.5MB total, sin video autoplay pesado.

### Checklist Día 28 - Go/No-Go
[ ] Formulario envía y llega a CRM + email confirmación
[ ] GA4 mide clic en CTA principal
[ ] Mobile perfecto (test en iPhone + Android real)
[ ] PageSpeed >90 móvil
[ ] Títulos SEO + OG image para LinkedIn
[ ] Aviso cookies + política privacidad
[ ] Plan rollback listo

¿Quieres que te lo convierta en un tablero Trello/Notion con fechas exactas a partir del próximo lunes y te redacte el brief de la Fase 1 para el kickoff?