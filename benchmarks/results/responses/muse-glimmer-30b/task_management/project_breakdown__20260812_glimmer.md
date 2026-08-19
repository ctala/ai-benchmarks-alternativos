# Muse Glimmer 30B — task_management/project_breakdown

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.48 | quality: 9.72
- latency_total: 29.964s | tokens_per_second: 62.1
- input_tokens: 118 | output_tokens: 1860
- judge_score: 4.8 | justificación: 

## Respuesta completa

Lanzar una landing en 4 semanas es ajustado pero viable si el scope es claro: Hero + propuesta de valor, 3-4 beneficios, demo/mockup, formulario de waitlist/CTA, pricing simple, FAQ y footer. Aquí tienes el plan realista.

### Equipo
* **Copywriter:** Mensajes y contenidos
* **Diseñador:** UX/UI y handoff
* **Dev 1:** Front-end
* **Dev 2:** Back-end / integraciones + QA

### Fases y Timeline

**SEMANA 1 - Fundación y Contenido**
*Día 1-2: Kickoff y Brief*
* **Tarea:** Kickoff, objetivos de lanzamiento, KPIs, buyer persona y propuesta de valor
* **Responsable:** Tú + Copywriter + Diseñador
* **Entrega:** Brief aprobado

*Día 2-5: Arquitectura y Wireframes*
* **Tarea:** Mapa de secciones y wireframes baja fidelidad
* **Responsable:** Diseñador
* **Dependencia:** Brief aprobado
* **Entrega:** Wireframes en Figma

*Día 3-5: Copy base*
* **Tarea:** Headline, subheadline, bullets de valor, CTA y FAQ
* **Responsable:** Copywriter
* **Dependencia:** Brief
* **Entrega:** Primer borrador de copy

**SEMANA 2 - Diseño y Preparación Técnica**
*Día 6-8: Diseño UI High-Fidelity*
* **Tarea:** Diseño de Hero, Features, Demo, Pricing, Footer. Sistema de diseño básico
* **Responsable:** Diseñador
* **Dependencia:** Wireframes + copy base
* **Entrega:** Mockups finales

*Día 6-7: Setup técnico*
* **Tarea:** Repo Git, entorno Vercel/Netlify, dominio, Google Analytics + Tag Manager
* **Responsable:** Dev 1 + Dev 2
* **Entrega:** Entorno listo

*Día 8-10: Revisión y Handoff*
* **Tarea:** Revisión interna de diseño + copy final
* **Responsable:** Copywriter + Diseñador
* **Dependencia:** Diseño UI
* **Entrega:** Copy final aprobado y Figma con specs para dev

**SEMANA 3 - Desarrollo**
*Día 11-15: Desarrollo Front-end*
* **Tarea:** Maquetado responsive con Next.js/Tailwind o similar. Integración de copy y assets
* **Responsable:** Dev 1
* **Dependencia:** Handoff aprobado
* **Entrega:** Landing funcional en staging

*Día 12-14: Integraciones*
* **Tarea:** Formulario waitlist a Mailchimp/Hubspot/Sheet, tracking de eventos, SEO básico meta tags y OG
* **Responsable:** Dev 2
* **Dependencia:** Front-end base
* **Entrega:** Formulario funcional y analytics OK

*Día 14-15: Copy final en vivo*
* **Tarea:** Ajustes finales de microcopy según maquetación
* **Responsable:** Copywriter
* **Dependencia:** Staging disponible

**SEMANA 4 - QA y Lanzamiento**
*Día 16-18: QA y Optimización*
* **Tarea:** Test responsive, velocidad, accesibilidad, links, formulario. Optimización imágenes
* **Responsable:** Dev 1 + Dev 2 + Diseñador
* **Dependencia:** Integraciones terminadas
* **Entrega:** Lista de bugs cerrada

*Día 19: Pre-lanzamiento*
* **Tarea:** Revisión final con todo el equipo, checklist SEO, 404, favicon
* **Responsable:** Todos
* **Entrega:** Aprobación Go/No Go

*Día 20: Lanzamiento*
* **Tarea:** Deploy a producción, DNS, verificación de formulario y analytics en vivo
* **Responsable:** Dev 2
* **Entrega:** Landing en producción

### Dependencias críticas
1. Brief -> Wireframes -> Diseño -> Handoff -> Desarrollo
2. Copy base -> Diseño -> Copy final -> Desarrollo
3. Diseño final es bloqueo para empezar desarrollo serio
4. Formulario y Analytics dependen de front-end base

### Recomendaciones para que encaje en 4 semanas
* Congela el scope el Día 2. No añadir secciones nuevas después de Semana 2.
* Diseñador y Copywriter trabajan en paralelo en Semana 1.
* Usa un template de landing probado para acelerar diseño y dev.
* Daily standup de 15 min y demo de staging los viernes.
* Prioriza móvil first.

¿Quieres que te lo convierta en un Gantt editable con las tareas asignadas a cada persona?