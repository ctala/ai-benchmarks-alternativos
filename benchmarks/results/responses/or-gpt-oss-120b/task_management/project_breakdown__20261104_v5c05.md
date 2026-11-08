# GPT-OSS 120B — task_management/project_breakdown

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.71 | quality: 9.8
- latency_total: 88.118s | tokens_per_second: 33.0
- input_tokens: 117 | output_tokens: 2904
- judge_score: 5 | justificación: La respuesta es precisa, relevante, detallada, clara y extremadamente útil, proporcionando un desglose exhaustivo del proyecto con tareas, responsables y tiempos realistas.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## 🚀 Plan de lanzamiento de la **Landing Page** para el SaaS de gestión de inventario  
**Duración total:** 4 semanas (28 días)  
**Equipo:** 1 Diseñador (D), 2 Developers (Dev 1 & Dev 2), 1 Copywriter (C)

---

## 1. Visión general del proyecto

| Fase | Objetivo principal | Duración estimada | Entregable clave |
|------|--------------------|-------------------|-------------------|
| **Fase 0 – Kick‑off & planificación** | Alinear expectativas, definir alcance y métricas | 0.5 días | Brief de proyecto, Roadmap y backlog en herramienta (Jira/Asana) |
| **Fase 1 – Investigación & estrategia** | Conocer al público, definir mensaje y mapa de contenidos | 2 días | Personas, value proposition, arquitectura de la página |
| **Fase 2 – Creación de contenidos** | Redactar copy, crear assets (imágenes, iconos, videos) | 4 días | Texto final, guiones de video, paquetes de imágenes |
| **Fase 3 – Diseño UI/UX** | Diseñar mockups de alta fidelidad y prototipo interactivo | 5 días | Mockups (desktop + mobile) y prototipo clickable (Figma) |
| **Fase 4 – Desarrollo Front‑end** | Convertir el diseño en código HTML/CSS/JS, integrar formularios | 7 días | Landing page en staging, código versionado (Git) |
| **Fase 5 – QA & Optimización** | Test funcional, de rendimiento, SEO y accesibilidad | 3 días | Checklist de QA firmado, mejoras aplicadas |
| **Fase 6 – Preparación de lanzamiento** | Configurar dominio, tracking, pruebas finales | 2 días | Landing live en producción, tags de analytics |
| **Fase 7 – Go‑Live & seguimiento** | Publicar, monitorizar métricas y resolver incidencias | 1 día + 2 días de “hyper‑care” | Dashboard de KPIs, reporte de lanzamiento |

> **Total:** 27 días laborables → ~4 semanas calendario (incluye fines de semana y buffers).

---

## 2. Detalle de tareas, dependencias y responsables

| # | Tarea | Responsable(s) | Duración | Dependencia |
|---|-------|----------------|----------|--------------|
| **0.1** | Reunión Kick‑off (objetivos, timelines, canales de comunicación) | PM (puede ser Lead dev) + todo el equipo | 2 h | - |
| **0.2** | Crear backlog y asignar prioridades en herramienta de gestión | PM | 2 h | 0.1 |
| **1.1** | Definir **personas** (perfil del buyer) | C + D | 1 día | 0.2 |
| **1.2** | Analizar competencia y benchmark de landing pages SaaS | D + Dev 1 | 1 día | 1.1 |
| **1.3** | Definir arquitectura de la página (wireframes low‑fi, mapa de secciones) | D | 0.5 día | 1.1‑1.2 |
| **2.1** | Redactar **headline**, sub‑headline, beneficios, CTA y FAQ | C | 2 días | 1.3 |
| **2.2** | Revisar y aprobar copy con el diseñador (tone‑of‑voice, longitud) | D + C | 0.5 día | 2.1 |
| **2.3** | Crear guión y producir **video hero** (30‑60 s) | C (guion) + recurso externo (si se subcontrata) | 2 días | 2.2 |
| **2.4** | Seleccionar y/o crear imágenes, iconos y micro‑ilustraciones | D | 2 días | 2.2 |
| **3.1** | Diseñar mockup **desktop** (Figma) | D | 3 días | 2.1‑2.4 |
| **3.2** | Adaptar a **mobile** (responsive) | D | 2 días | 3.1 |
| **3.3** | Prototipo clickable y pruebas de usabilidad interna | D + C | 0.5 día | 3.1‑3.2 |
| **4.1** | Configurar repositorio Git + CI (GitHub Actions) | Dev 1 | 0.5 día | 3.3 |
| **4.2** | Convertir layout a **HTML5 + SCSS** (estructura base) | Dev 2 | 2 días | 3.3 |
| **4.3** | Implementar interacciones (scroll‑animations, modal, video embed) | Dev 2 | 1.5 días | 4.2 |
| **4.4** | Integrar **formulario de captura** (HubSpot/Marketo) y **reCAPTCHA** | Dev 1 | 1 día | 4.2 |
| **4.5** | Añadir **tracking** (Google Analytics, FB Pixel, Hotjar) | Dev 1 | 0.5 día | 4.4 |
| **5.1** | QA funcional: enlaces, formularios, responsividad | Dev 2 + C (pruebas de contenido) | 1 día | 4.5 |
| **5.2** | Pruebas de rendimiento (Lighthouse) y SEO on‑page | Dev 1 | 0.5 día | 5.1 |
| **5.3** | Accesibilidad (WCAG 2.1 AA) y pruebas de cross‑browser | Dev 2 | 0.5 día | 5.2 |
| **5.4** | Corrección de bugs y optimizaciones | Dev 1 & Dev 2 | 1 día | 5.1‑5.3 |
| **6.1** | Configurar dominio y SSL en hosting (Netlify/Vercel) | Dev 1 | 0.5 día | 5.4 |
| **6.2** | Deploy a **staging** y revisión final con stakeholder | Todo | 0.5 día | 6.1 |
| **6.3** | Deploy a **producción** (push a master) | Dev 1 | 0.5 día | 6.2 |
| **7.1** | Monitorear métricas (visitas, conversiones) 24 h | C | 1 día | 6.3 |
| **7.2** | Resolución de incidencias “hyper‑care” (max 2 días) | Dev 1 & Dev 2 | 2 días | 7.1 |
| **7.3** | Reporte de lanzamiento y lecciones aprendidas | PM + C | 0.5 día | 7.2 |

---

## 3. Timeline visual (Calendario de 4 semanas)

> **Formato:** Cada bloque representa un día laborable. Los **límites de fase** están marcados con una barra vertical.  

| Semana | Lunes | Martes | Miércoles | Jueves | Viernes | Sábado | Domingo |
|--------|------|--------|-----------|--------|---------|--------|----------|
| **1** (D‑28 → D‑22) | 0.1‑0.2 (Kick‑off) | 1.1‑1.2 | 1.3 | 2.1 | 2.1 | **Buffer** | **Buffer** |
| **2** (D‑21 → D‑15) | 2.2‑2.3 | 2.4 | 3.1 | 3.1 | 3.1 | **Buffer** | **Buffer** |
| **3** (D‑14 → D‑8) | 3.2‑3.3 | 4.1‑4.2 | 4.2‑4.3 | 4.3‑4.4 | 4.5 | **Buffer** | **Buffer** |
| **4** (D‑7 → D‑1) | 5.1‑5.2 | 5.3‑5.4 | 6.1‑6.3 | 7.1 | 7.2‑7.3 | **Go‑Live** (Viernes tarde) | **Post‑launch** (monitor) |

> **Notas:**  
> - *Buffer* (2 días/semana) cubre imprevistos, revisiones de stakeholder y tiempo de descanso del equipo.  
> - Si el **video hero** se subcontrata, su entrega puede alinearse con la tarea 2.3 y el buffer permite tiempo de edición.

---

## 4. Herramientas recomendadas

| Área | Herramienta | Uso |
|------|-------------|-----|
| Gestión del proyecto | **Asana / Trello / ClickUp** | Backlog, sprints de 1 semana, asignación de tareas, dependencias |
| Comunicación | **Slack** (canal #landing‑launch) + **Google Meet** (dailies) |
| Diseño | **Figma** (mockups + prototipo) |
| Desarrollo | **VS Code**, **GitHub**, **GitHub Actions** (CI) |
| Hosting | **Netlify** o **Vercel** (deploy rápido, preview URLs) |
| Formularios & CRM | **HubSpot**, **Zapier** (para conectar con la base de datos) |
| Analítica | **Google Analytics 4**, **Facebook Pixel**, **Hotjar** |
| QA & Performance | **Chrome DevTools**, **Lighthouse**, **BrowserStack** (cross‑browser) |

---

## 5. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Retraso en la producción del video hero | Media | Alto (pierde impacto visual) | Definir guion y entregables antes de la semana 2; usar **stock video** como backup. |
| Cambios de último minuto en el copy | Media | Medio | Establecer **freeze** de copy al final de la semana 2; revisar con stakeholder antes del freeze. |
| Problemas de compatibilidad en navegadores antiguos | Baja | Medio | Testear en Chrome, Firefox, Safari y Edge desde la fase 5; usar polyfills si es necesario. |
| Formulario no captura leads correctamente | Baja | Alto | Configurar pruebas de envío en staging y validar webhook antes del go‑live. |
| Sobre‑carga de tráfico al día del lanzamiento | Media | Medio | Configurar CDN (Netlify/Vercel) y habilitar **autoscaling**; monitorizar logs durante las primeras 2 h. |

---

## 6. KPIs de lanzamiento (a monitorizar los primeros 30 días)

| Métrica | Objetivo inicial | Herramienta |
|---------|-----------------|------------|
| **Visitas a la landing** | 2 000 (primeras 2 sem.) | GA4 |
| **Tasa de conversión (lead)** | 4 % | HubSpot / GA4 |
| **Tiempo de carga (LCP)** | < 2.5 s | Lighthouse |
| **Bounce rate** | < 45 % | GA4 |
| **Interacciones con video** | ≥ 30 % de reproducciones completadas | Hotjar / YouTube API |
| **Coste por lead (CPL)** | ≤ $12 (si se usan campañas) | Ads Manager |

---

## 7. Resumen rápido (para presentar al equipo)

| Semana | Principales entregables | Owner(s) |
|-------|------------------------|----------|
| **1** | Brief, personas, arquitectura, borrador de copy | C, D |
| **2** | Copy final, assets visuales, mockup desktop + mobile | C, D |
| **3** | Código HTML/CSS/JS, formulario + tracking, pruebas QA | Dev 1, Dev 2 |
| **4** | Deploy a producción, monitorización, reporte de lanzamiento | Todo |

Con este plan, **todos saben qué hacer, cuándo y con quién**, y el proyecto tiene márgenes de tiempo y riesgos controlados para lanzar la landing page en **exactamente 4 semanas**. ¡Manos a la obra! 🚀