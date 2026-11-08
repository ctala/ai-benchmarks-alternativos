# GPT-6 Luna Pro — task_management/project_breakdown

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.81 | quality: 9.8
- latency_total: 19.496s | tokens_per_second: 112.2
- input_tokens: 3730 | output_tokens: 2187
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## Plan de lanzamiento en 4 semanas

**Supuestos:** landing page de marketing (no incluye construir el producto), con formulario de captación o solicitud de demo, analítica básica y una ronda de revisión legal. Para llegar a tiempo, conviene acordar pronto el alcance y limitar cambios tardíos.

### Fases, tareas y responsables

| Fase | Tareas principales | Responsable(s) | Dependencias |
|---|---|---|---|
| **1. Alineación y alcance** | Definir audiencia, propuesta de valor, CTA, métricas de éxito, requisitos y contenido necesario. Acordar páginas y funcionalidades dentro del alcance. | Copywriter (líder), diseñador, Dev 1, stakeholder | Ninguna |
| **2. Estructura y contenido** | Crear sitemap o esquema de secciones, redactar titulares y textos, definir preguntas frecuentes, mensajes del formulario y metadatos SEO. | Copywriter; diseñador aporta estructura | Fase 1 |
| **3. Diseño** | Wireframes, diseño visual responsive, estados de formulario, componentes y entrega de especificaciones. | Diseñador; copywriter revisa contenido | Estructura y borrador de contenido |
| **4. Desarrollo** | Preparar repositorio y despliegues; implementar la landing responsive; integrar formulario, analítica, SEO técnico y eventos; conectar CRM o herramienta de correo si aplica. | Dev 1 (frontend); Dev 2 (integraciones, analítica y QA técnico) | Diseño aprobado y textos suficientemente estables |
| **5. QA y ajustes** | Probar navegadores, móvil, enlaces, formulario, accesibilidad básica, rendimiento, SEO, analítica y mensajes de confirmación. Corregir errores y pulir contenido. | Dev 2 (coordinación), ambos developers; diseñador y copywriter revisan | Versión funcional desplegada |
| **6. Lanzamiento** | Revisión final, aprobación de stakeholders, publicación, comprobación en producción y seguimiento de métricas. | Dev 1 (deploy); Dev 2 (validación); copywriter y diseñador (revisión) | QA aprobado y aprobaciones recibidas |

### Timeline semanal

#### Semana 1 — Definición y estructura
- **Lunes:** reunión inicial; cerrar audiencia, propuesta de valor, CTA, métricas y alcance.
- **Martes–miércoles:** copywriter redacta el primer borrador; diseñador prepara estructura y wireframe de baja fidelidad.
- **Jueves:** revisión conjunta de mensajes, secciones y requisitos técnicos.
- **Viernes:** aprobar estructura y contenido principal. Dev 1 prepara el proyecto y Dev 2 identifica integraciones y eventos de analítica.

**Hito:** alcance y estructura aprobados.

#### Semana 2 — Diseño y contenido final
- Diseñador crea el diseño visual desktop y móvil.
- Copywriter termina textos, FAQ, etiquetas del formulario y metadatos.
- Developers revisan viabilidad técnica e identifican riesgos.
- Al final de la semana, se aprueban diseño y textos para implementación.

**Hito:** diseño y contenido aprobados. Después de este punto, los cambios de alcance se evalúan por impacto en la fecha.

#### Semana 3 — Implementación
- **Dev 1:** construye secciones y estilos responsive.
- **Dev 2:** integra formulario, CRM o correo, analítica, eventos y configuración SEO técnica.
- Diseñador revisa la primera versión y entrega ajustes puntuales.
- Copywriter valida que el contenido esté integrado correctamente.

**Hito:** landing completa en entorno de staging.

#### Semana 4 — QA, correcciones y lanzamiento
- **Lunes–martes:** pruebas funcionales, responsive, accesibilidad básica, rendimiento, enlaces y analítica.
- **Miércoles:** correcciones prioritarias y revisión final de stakeholders.
- **Jueves:** deploy a producción y smoke test.
- **Viernes:** margen para resolver incidencias; seguimiento inicial de tráfico, conversiones y formularios.

**Hito:** landing publicada y medición funcionando.

### Reparto práctico del equipo
- **Diseñador:** estructura visual, diseño responsive, especificaciones y revisión de implementación.
- **Dev 1:** frontend, componentes, responsive y deploy.
- **Dev 2:** integraciones, formulario, analítica, SEO técnico, QA y soporte al deploy.
- **Copywriter:** posicionamiento, textos, CTA, FAQ, mensajes del formulario y revisión editorial.

### Dependencias y riesgos clave
- El **diseño depende de la estructura y el contenido**; la implementación depende de que ambos estén aprobados.
- Si se integra un CRM, herramienta de email o servicio externo, confirmar accesos y configuración en la **semana 1**.
- Definir quién da la aprobación final y reservar tiempo de revisión; aprobaciones lentas ponen en riesgo la fecha.
- Mantener un margen en la última semana: evitar añadir páginas, funcionalidades o cambios de mensaje sustanciales después de comenzar QA.
- Si la fecha es inamovible, priorizar una versión inicial sencilla: una landing, un CTA principal y un formulario probado; dejar mejoras secundarias para después del lanzamiento.