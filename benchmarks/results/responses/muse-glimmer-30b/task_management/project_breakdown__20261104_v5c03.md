# Muse Glimmer 30B — task_management/project_breakdown

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 14.098s | tokens_per_second: 132.8
- input_tokens: 118 | output_tokens: 1872
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Lanzamiento en 4 semanas es ajustado pero viable para una landing page de 1 página + waitlist. Con tu equipo de 1 Diseñador, 2 Developers y 1 Copywriter, el flujo crítico es: Brief -> Copy -> Diseño -> Dev -> QA.

### Estructura del equipo
* **Copywriter:** Mensaje, estructura de contenido y SEO copy
* **Diseñador:** IA, wireframes, UI y assets
* **Dev 1 - Frontend:** HTML/CSS/JS, integración con CMS
* **Dev 2 - Backend/Integrations:** Formulario, CRM, Analytics, Deploy

### Fases y Timeline Realista

#### SEMANA 1 - FUNDAMENTOS Y CONTENIDO
**Objetivo: Cerrar estrategia y tener copy listo para diseñar.**

**Día 1-2 | Kickoff y Brief**
* Tarea: Workshop de objetivos, buyer persona, propuesta de valor y KPI de lanzamiento. Definir secciones: Hero + CTA, Problema/Solución, Features clave, Demo, Social proof, Pricing/Waitlist, FAQ, Footer.
* Responsable: Copywriter + Diseñador + Tú como PM
* Entrega: Brief aprobado en Notion

**Día 2-3 | Arquitectura de Información y Wireframes**
* Tarea: Mapa de la página y wireframes de baja fidelidad.
* Responsable: Diseñador
* Dependencia: Brief aprobado
* Entrega: Wireframes en Figma

**Día 3-5 | Copy Strategy y Redacción V1**
* Tarea: Headline, subheadline, bullets de valor, CTA principal y secundario. Copy para Features y FAQ.
* Responsable: Copywriter
* Dependencia: Wireframes
* Entrega: Copy en documento compartido

#### SEMANA 2 - DISEÑO
**Objetivo: UI final aprobada para desarrollo.**

**Día 6-8 | Diseño UI High-Fidelity**
* Tarea: Diseño del hero, secciones y estados de formulario en Figma. Design system básico: tipografía, colores, componentes.
* Responsable: Diseñador
* Dependencia: Wireframes + Copy V1
* Entrega: Mockups finales

**Día 8-9 | Revisión y Ajustes Copy**
* Tarea: Revisión interna y ajustes de copy según diseño. Validación de mensajes con producto.
* Responsable: Copywriter + Diseñador
* Entrega: Copy V2 final + UI aprobada

**Día 9-10 | Handoff a Dev**
* Tarea: Especificaciones de assets, export de componentes, guía de handoff.
* Responsable: Diseñador -> Dev 1
* Entrega: Figma con Dev Mode listo

#### SEMANA 3 - DESARROLLO
**Objetivo: Landing funcional en staging.**

**Día 8-12 | Setup y Frontend**
* Tarea: Setup repo, estructura HTML/Tailwind, maquetación responsive de todas las secciones.
* Responsable: Dev 1
* Dependencia: UI aprobada
* Entrega: Staging con diseño pixel perfect

**Día 10-14 | Integraciones**
* Tarea: Formulario de waitlist / demo request conectado a CRM / HubSpot / Airtable. Configuración de Analytics: GA4 + Meta Pixel + Hotjar. SEO básico: meta tags, OG, schema.
* Responsable: Dev 2
* Dependencia: Frontend base
* Entrega: Formulario funcional y eventos de tracking

**Día 12-15 | Contenido final y assets**
* Tarea: Carga de copy final, imágenes, iconos, micro-interacciones.
* Responsable: Copywriter + Diseñador + Dev 1
* Entrega: Landing completa en staging

#### SEMANA 4 - QA Y LANZAMIENTO
**Objetivo: Producción y go-live.**

**Día 16-17 | QA y Pruebas**
* Tarea: Checklist de QA: responsive mobile/tablet, velocidad Lighthouse >90, formularios, links, tracking.
* Responsable: Dev 1 + Dev 2 + Copywriter
* Dependencia: Landing completa
* Entrega: Bug list cerrada

**Día 18-19 | Ajustes finales y Pre-launch**
* Tarea: Correcciones, optimización de imágenes, dominio y SSL.
* Responsable: Dev 2
* Entrega: Versión final en producción oculta

**Día 20 | Lanzamiento**
* Tarea: Deploy a producción, verificación de analytics, anuncio interno.
* Responsable: Dev 2 + Tú
* Entrega: Landing live + URL de seguimiento

### Dependencias críticas
1. Copy no puede finalizar sin wireframes.
2. Diseño UI no puede empezar sin copy outline.
3. Dev no puede empezar sin UI aprobada.
4. Integraciones de formulario dependen del frontend base.
5. QA depende de contenido final cargado.

### Recomendaciones para no perder tiempo
* **Bloquea 1 daily de 15 min** con todo el equipo.
* Usa Figma como única fuente de verdad para diseño.
* El copywriter escribe directamente en el Figma para evitar saltos de documento.
* Prioriza MVP: Demo video puede ser un placeholder en semana 3 si no está listo.
* Deploy en Vercel/Netlify para despliegues instantáneos.

¿Quieres que te lo convierta en un tablero de Trello/Notion con checklist por tarea?