# Muse Spark 1.3 — task_management/project_breakdown

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 21.421s | tokens_per_second: 117.9
- input_tokens: 70 | output_tokens: 2525
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Perfecto, con 4 semanas y ese equipo sí llegas, pero tienes que trabajar en paralelo y congelar decisiones a tiempo. Aquí tienes un plan realista para una landing SaaS de gestión de inventario.

**Supuesto:** Landing en Next.js / Webflow + Vercel, con formulario a HubSpot/Mailchimp, GA4 + Pixel, y secciones estándar SaaS.

### Estructura de la Landing (alcance MVP)
Hero + CTA Demo/Trial, logos/prueba social, dolores, features (stock tiempo real, multi-almacén, alertas, integraciones, reportes), cómo funciona, integraciones, pricing, testimonios, FAQ, CTA final + footer legal.

### Las 5 Fases

**FASE 0: Kickoff y Estrategia - Día 1-2**
Responsable principal: Todos. Lidera: Tú (Product Owner)
1. Definir buyer persona, propuesta de valor y 1 CTA principal. *Resp: Copy + Tú*
2. Definir sitemap, secciones y KPIs (ej: >3% conversión a demo). *Resp: Todos*
3. Setup: Figma, repo GitHub, hosting Vercel, Notion/Trello, dominio staging. *Resp: Dev1 + Dev2*
**Entregable M1:** Brief de 1 página aprobado. Sin esto no se avanza.

**FASE 1: Contenido y Estructura - Día 2-8**
La clave de todo. El copy bloquea al diseño.
1. Research keywords SEO + competencia (3 competidores). *Resp: Copy* - 2 días
2. Wireframe lo-fi en Figma (desktop/mobile). *Resp: Diseñador* - Depende de brief - 3 días
3. Copywriting v1 de todas las secciones + SEO titles/meta. *Resp: Copywriter* - 4 días
4. Validar wireframe + copy con 2-3 usuarios. *Resp: Diseñador + Copy*
**Entregable M2 - Día 8: COPY CONGELADO.** Regla de oro: después del día 8 no se reescribe, solo se pule.

**FASE 2: Diseño UI - Día 5-12**
Se solapa con Fase 1.
1. Design System: colores, tipografías, botones, iconos. *Resp: Diseñador* - Día 5-6
2. Diseño UI hi-fi desktop + mobile en Figma. *Resp: Diseñador* - Depende de Copy v1 y Wireframe - Día 7-11
3. Prototipo + assets para devs (ilustraciones, mockups del dashboard). *Resp: Diseñador* - Día 11-12
4. Revisión y aprobación final. *Resp: Tú*
**Entregable M3 - Día 12: DISEÑO CONGELADO.**

Mientras tanto los devs no están parados:
Dev1 + Dev2 (Día 3-9): Setup proyecto, componentes base, formulario + integración CRM, analytics GA4, entorno staging.

**FASE 3: Desarrollo - Día 10-18**
1. Maquetación Front: Hero, features, pricing, FAQ, footer. Responsive mobile-first. *Resp: Dev1* - Depende de Diseño UI
2. Backend / Integraciones: Formulario demo, validación, HubSpot, autoresponder email, cookies/GDPR. *Resp: Dev2* - Depende de Copy final
3. Animaciones, velocidad (<2s), schema SEO, Open Graph. *Resp: Dev1 + Dev2*
4. Carga de contenido real + conexión dominio. *Resp: Dev2 + Copy*
**Entregable M4 - Día 18: Beta en staging lista para QA.**

**FASE 4: QA y Pre-lanzamiento - Día 16-20**
Se solapa 2 días con dev para ganar tiempo.
1. QA funcional y visual (Chrome, Safari, móvil), test formularios. *Resp: Dev1 + Diseñador*
2. QA copy, links, ortografía, legal. *Resp: Copywriter*
3. Performance, accesibilidad, SEO técnico (Lighthouse >90). *Resp: Dev2*
4. Soft launch: pasar a 10 usuarios beta + Hotjar/Clarity. *Resp: Todos - Día 19*
**Entregable M5 - Día 20: GO-LIVE.**

### Timeline Visual 4 Semanas

**Semana 1 (Día 1-5): Pensar**
Lun-Mar: Kickoff + brief
Mié-Vie: Wireframe + Copy v1 + Setup dev
*Review Viernes: aprobar wireframe*

**Semana 2 (Día 6-10): Diseñar**
Lun-Mar: Copy v1 -> vFinal (CONGELAR día 8)
Mié-Vie: UI hi-fi + Dev empieza componentes
*Review Viernes: aprobar diseño*

**Semana 3 (Día 11-15): Construir**
Lun-Vie: Build completo front + integraciones. Copy solo hace ajustes menores.
*Review Viernes: demo interna en staging*

**Semana 4 (Día 16-20): Pulir y Lanzar**
Lun-Mar: Terminar dev + empezar QA
Mié-Jue: QA, SEO, velocidad, beta test
Vie Día 20: Lanzamiento + anuncio + monitoreo

Deja 2 días de colchón dentro de la semana 4. No agregues features nuevas después del día 12.

### Dependencias Críticas (Camino Crítico)
Brief > Copy v1 > Diseño UI > Desarrollo Front > QA > Launch

Si el copy se retrasa 2 días, todo se retrasa 2 días. Por eso el copywriter debe entregar por secciones (Hero primero el día 4) para que diseñador y devs no esperen.

### Cómo trabajar para no quemarse
1. Daily de 15 min: qué hice, qué me bloquea.
2. 2 responsables por tarea: 1 ejecuta, 1 revisa.
3. Viernes = día de decisión. Tú apruebas o se pospone a post-lanzamiento.
4. Backlog post-lanzamiento: A/B test hero, video demo, calculadora ROI, blog, multi-idioma. NO entra ahora.

### Checklist Día de Lanzamiento
[ ] Formulario envía y llega al CRM
[ ] GA4 + Search Console activos
[ ] Mobile perfecto + carga <2s
[ ] Meta títulos + imagen compartir LinkedIn
[ ] Política privacidad + cookies
[ ] Plan rollback + monitoreo 48h

¿Quieres que te lo convierta en un tablero de Notion/Trello con tareas día por día asignadas para tu equipo?