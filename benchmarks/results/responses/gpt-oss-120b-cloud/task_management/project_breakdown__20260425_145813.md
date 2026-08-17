# GPT-OSS 120B (Ollama Cloud) — task_management/project_breakdown

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.98 | quality: 9.24
- latency_total: 33.641s | tokens_per_second: 60.9
- input_tokens: 130 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

## 🚀 Plan de lanzamiento de la Landing Page  
**Producto:** SaaS de gestión de inventario  
**Plazo total:** 4 semanas (28 días)  
**Equipo:**  

| Rol | Nombre (ejemplo) | Horas disponibles por semana* |
|-----|------------------|------------------------------|
| Diseñador UI/UX | **Ana** | 30 h |
| Developer 1 (Front) | **Luis** | 30 h |
| Developer 2 (Back/Integraciones) | **María** | 30 h |
| Copywriter | **Javier** | 20 h |

\*Se asume 40 h/semana de jornada completa, pero cada recurso dedica solo el tiempo indicado al proyecto para que puedan atender otras tareas del negocio.

---

## 1️⃣ Fases, tareas y dependencias  

| Fase | Tarea | Descripción breve | Responsable | Duración estimada | Dependencia |
|------|-------|-------------------|-------------|-------------------|-------------|
| **0. Kick‑off & planificación** | 0.1 Reunión de arranque | Alineación de objetivos, público, KPIs, tono de marca y entregables | PM + todo | 2 h (día 1) | — |
| | 0.2 Definir brief creativo y técnico | Docs con wireframes de referencia, tech‑stack, formularios, tracking | PM + Diseñador + Devs | 2 h (día 1) | 0.1 |
| **1. Investigación & estrategia de contenido** | 1.1 Análisis de competencia y benchmark | Recopilar 5‑7 landing pages del segmento, identificar buenas prácticas | Copywriter | 4 h (día 2) | 0.2 |
| | 1.2 Definir estructura de la página (sitemap) | Home → Hero → Problema → Solución → Features → Testimonios → CTA → FAQ → Footer | Copy + Diseñador | 4 h (día 2‑3) | 1.1 |
| | 1.3 Redacción del copy principal (hero, value‑prop, CTA) | Texto persuasivo, foco en beneficios y “pain points” | Copywriter | 8 h (día 3‑4) | 1.2 |
| | 1.4 Redacción de micro‑copy (labels, tooltips, formularios) | Texto UI, mensajes de error, agradecimiento | Copywriter | 4 h (día 5) | 1.2 |
| **2. Diseño UI/UX** | 2.1 Wireframes de baja fidelidad | Sketch rápido de cada sección (incluye formulario) | Diseñador | 6 h (día 6) | 1.2 |
| | 2.2 Revisión interna + feedback | PM y devs revisan wireframes | Todo | 2 h (día 6) | 2.1 |
| | 2.3 UI mockup de alta fidelidad (desktop) | Aplicar brand‑guide, tipografía, colores, iconografía | Diseñador | 12 h (día 7‑8) | 2.2 |
| | 2.4 Adaptación a mobile (responsive) | Breakpoints, reorganización de bloques | Diseñador | 6 h (día 9) | 2.3 |
| | 2.5 Entrega de assets (SVG, imágenes optimizadas, style guide) | Exportar y subir a repo/Drive | Diseñador | 2 h (día 9) | 2.4 |
| **3. Desarrollo Front‑End** | 3.1 Setup del proyecto (repo, build, CI) | Next.js / React (u otro stack acordado) + Tailwind/SCSS | Dev 1 | 4 h (día 10) | 2.5 |
| | 3.2 Implementar layout desktop + mobile | HTML/JSX, CSS, componentes reutilizables | Dev 1 | 12 h (día 11‑12) | 2.5 |
| | 3.3 Integrar copy (i18n opcional) | Inserción de textos, placeholders | Dev 1 | 4 h (día 12) | 3.2 |
| | 3.4 Implementar formulario de captura (Mailchimp/HubSpot API) | Validación, envío, mensaje de éxito | Dev 2 | 6 h (día 13) | 3.2 |
| | 3.5 Implementar tracking (Google Tag Manager, GA4, Hotjar) | Eventos de click, scroll depth, envío formulario | Dev 2 | 4 h (día 13) | 3.4 |
| **4. QA y pruebas** | 4.1 Revisión de UI vs. mockup | Checklist de pixel‑perfect, tipografía, colores | Diseñador + Dev 1 | 3 h (día 14) | 3.3‑3.5 |
| | 4.2 Testing funcional (form, enlaces, responsividad) | Chrome, Firefox, Safari, mobile (iOS/Android) | Dev 2 | 4 h (día 14‑15) | 4.1 |
| | 4.3 Test de velocidad y SEO básico (Lighthouse) | Score > 90 % en Performance, Accessibility, SEO | Dev 1 | 3 h (día 15) | 4.2 |
| | 4.4 Corrección de bugs críticos | Ajustes rápidos | Dev 1/Dev 2 | 6 h (día 16) | 4.3 |
| **5. Preparación del lanzamiento** | 5.1 Configuración de dominio y certificado SSL | DNS, Cloudflare (si procede) | Dev 2 | 2 h (día 17) | 4.4 |
| | 5.2 Configuración de backups y monitoring (UptimeRobot) | Alertas de caída, logs | Dev 2 | 2 h (día 17) | 5.1 |
| | 5.3 Revisión final con stakeholder (demo) | Aprobación del copy, UI y funcionalidad | PM + todo | 2 h (día 18) | 5.2 |
| **6. Go‑Live** | 6.1 Deploy a producción (CI/CD) | Push a master → Vercel/Netlify | Dev 1 | 1 h (día 19) | 5.3 |
| | 6.2 Test post‑deploy (formulario, tracking) | Verificar que todo funciona en live | Todo | 2 h (día 19) | 6.1 |
| | 6.3 Anuncio interno y envío a lista de espera | Email a leads, publicación en redes internas | PM + Copywriter | 2 h (día 20) | 6.2 |
| **7. Post‑launch (primeras 2 sem.)** | 7.1 Monitoreo de métricas (visitas, conversiones) | GA4, Hotjar, funnel de captura | PM | 2 h/sem (día 21‑28) | 6.3 |
| | 7.2 Correcciones menores / A/B test de CTA | Pequeños tweaks basados en datos | Dev 1 + Copywriter | 4 h/sem (día 22‑27) | 7.1 |
| | 7.3 Reporte de resultados y lecciones aprendidas | Dashboard + presentación | PM | 4 h (día 28) | 7.2 |

> **Nota:** Los días están contados a partir del **lunes de la semana 1**. Los fines de semana se consideran libres, pero pueden usarse para tareas de bajo impacto (p.ej. revisión de copy) si el equipo lo desea.

---

## 2️⃣ Cronograma visual (Gantt simplificado)

```
Semana 1 (Días 1‑7)   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|
 0.1‑0.2              |██|
 1.1‑1.4              |██████|
 2.1‑2.2              |████|
 2.3‑2.5              |██████|
 3.1‑3.2              |██|
-----------------------------------------------
Semana 2 (Días 8‑14)  |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|
 2.4‑2.5              |██|
 3.3‑3.5              |██████|
 4.1‑4.4              |██████|
-----------------------------------------------
Semana 3 (Días 15‑21) |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■