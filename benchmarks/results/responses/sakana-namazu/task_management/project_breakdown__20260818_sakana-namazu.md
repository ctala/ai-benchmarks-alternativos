# Sakana Namazu — task_management/project_breakdown

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.15 | quality: 9.24
- latency_total: 8.759s | tokens_per_second: 233.8
- input_tokens: 157 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

El usuario necesita un plan de proyecto para lanzar una landing page para un producto SaaS de gestión de inventario en 4 semanas. El equipo consiste en: 1 diseñador, 2 desarrolladores y 1 copywriter.

Necesito proporcionar:
1. Fases del proyecto
2. Tareas detalladas
3. Dependencias
4. Responsables
5. Timeline realista de 4 semanas

Estructura del plan:
- Semana 1: Estrategia, contenido y wireframes (Foundation)
- Semana 2: Diseño y preparación de desarrollo (Design & Handoff)
- Semana 3: Desarrollo (Development)
- Semana 4: QA, optimización, lanzamiento y seurimiento (Launch)

Voy a detallar cada semana con tareas específicas, responsables (Designer, Dev1, Dev2, Copywriter), dependencias y duración estimada.

Consideraciones importantes:
- Es una landing page, no toda la app. Enfocarse en: Hero, Features, How it works, Pricing, Testimonials/Social proof, FAQ, CTA, Footer.
- 4 semanas es ajustado pero realista para un equipo de 4 personas si se gestiona bien.
- Los 2 devs pueden dividir trabajo: uno frontend principal, otro frontend/secundario + animaciones/SEO/performance.
- El copywriter debe trabajar en paralelo lo máximo posible.
- Herramientas sugeridas: Figma (design), Next.js/Webflow/WordPress (dependiendo del stack, mejor sugerir algo moderno y rápido como Next.js o si necesitan velocidad Webflow, pero como no especifican stack, mantendré el plan agnóstico al stack pero con tareas claras).

Detalle por semana:

**Semana 1: Descubrimiento, Estrategia y Contenido**
- Día 1-2: Kickoff, definición de objetivos, análisis competencia, definición de buyer persona (Todo el equipo)
- Día 2-3: Arquitectura de la landing (secciones, navegación) (Designer lidera, Copywriter input)
- Día 3-5: Copywriting: Headlines, body copy, CTAs, microcopy (Copywriter)
- Día 4-5: Wireframes baja/mediana fidelidad (Designer)
- Dependencias: Arquitectura debe estar antes que wireframes y copy. Copy puede empezar con brief.

**Semana 2: Diseño Visual y Preparación**
- Día 6-8: Diseño UI de la landing (Designer) - basado en wireframes aprobados y copy casi final.
- Día 8-9: Sistema de diseño/componentes (Designer)
- Día 9-10: Revisión de diseño y ajustes (Todo el equipo)
- Día 10-11: Preparación de assets (iconos, imágenes, mockups de UI del producto) (Designer, puede apoyar Copywriter en selección de imágenes)
- Día 11-12: Handoff a desarrollo + preparación de repo/estructura (Designer + Devs)
- Día 12-14: Setup inicial de desarrollo (Devs): Repo, CI/CD, hosting, dominio, analíticas.
- Dependencias: Diseño debe estar avanzado para handoff. Setup puede empezar en paralelo.

**Semana 3: Desarrollo**
- Día 15-17: Desarrollo frontend secciones principales (Hero, Features, Social proof) (Dev1 y Dev2)
- Día 17-19: Desarrollo secciones secundarias (How it works, Pricing, FAQ, Footer, Formularios)
- Día 19-20: Responsive design, animaciones, interacciones
- Día 20-21: Integraciones (Analytics, CRM, Email capture, Chatbot si aplica)
- Dependencias: Necesitan assets estructurados y diseño final.

**Semana 4: QA, Optimización y Lanzamiento**
- Día 22-23: QA testing: Funcional, cross-browser, responsive, performance (Devs + Designer valida pixel perfect)
- Día 23-24: Corrección de bugs y ajustes finos (Devs)
- Día 24-25: Optimización SEO técnica, meta tags, velocidad, accesibilidad (Dev1/SEO + Copywriter metas)
- Día 25-26: Deploy en staging, revisión final con stakeholders (Todo el equipo)
- Día 26-27: Lanzamiento a producción (Devs)
- Día 27-28: Monitoreo post-lanzamiento, hotfixes, configuración de campañas (Devs + Copywriter para ajustes de copy si es necesario)

Roles:
- **Diseñador (D)**: UX research, wireframes, UI design, design system, handoff, revisiones visuales QA.
- **Copywriter (C)**: Estrategia de contenido, copy, microcopy, metadatos SEO, mensajes de error/success.
- **Dev 1 (Frontend Lead)**: Arquitectura frontend, componentes complejos, integraciones, performance, deploy.
- **Dev 2 (Frontend Support)**: Componentes secundarios, responsive, animaciones, testing.

Ajustes para hacerlo más realista:
- Dividiré en 4 fases exactas por semana.
- Destacar que ciertas tareas pueden solaparse (ej. setup dev mientras se finaliza diseño).
- Añadiré un diagrama de Gantt simplificado o una tabla clara.
- Incluiré riesgos y mitigaciones para que sea un plan completo.

Voy a estructurar la respuesta en español como se solicitó.

Estructura final:
1. Resumen del proyecto y stack sugerido (rápido)
2. Tabla/Matriz de fases, tareas, responsables, dependencias y duración.
3. Timeline semanal detallado (por días o rango de días)
4. Flujo de dependencias visual (descripción textual)
5. Reuniones clave y checkpoints
6. Riesgos y mitigaciones

Voy a asegurarme de usar términos claros y accionables. El usuario es de latinoamérica o España (usó "desglose", "diseñador"), así que español neutro.

Refinando tareas específicas:

Fase 1: Estrategia y Contenido (Semana 1)
- T1.1 Kickoff y definición de metas (Objetivo: leads, demos, waitlist?). Responsable: PM/Team Lead (asumiremos que el usuario es el lead o el team se auto-gestiona; si no hay PM, digo "Todo el equipo/Lead").
- T1.2 Benchmark de competidores y referencias visuales. D + C.
- T1.3 Definición de secciones y flujo de usuario. D + C.
- T1.4 Redacción de copy principal (value prop, headlines, descripciones). C. Depende de T1.1, T1.3.
- T1.5 Wireframes baja/mediana fidelidad en Figma. D. Depende de T1.3.
- T1.6 Keyword research básico para SEO. C.
- Entregable: Documento de brief + Wireframes + Copy v1.

Fase 2: Diseño UI y Handoff (Semana 2)
- T2.1 Diseño visual de alta fidelidad (Desktop). D. Depende de T1.4, T1.5.
- T2.2 Diseño responsive (Tablet/Mobile). D. Depende de T2.1.
- T2.3 Sistema de diseño (colores, tipografía, componentes base). D. Paralelo a T2.1.
- T2.4 Selección/edición de assets gráficos (mockups, imágenes, ilustraciones). D. Depende de T2.1.
- T2.5 Revisión de diseño con el equipo. Todo.
- T2.6 Preparación de handoff (exportación, especificaciones). D.
- T2.7 Setup inicial del proyecto (repo, hosting, dominio, analytics). Dev1 + Dev2. Puede empezar en paralelo al final de semana 1 o inicio 2.

Fase 3: Desarrollo (Semana 3)
- T3.1 Configuración de componentes base y tokens de diseño. Dev1.
- T3.2 Desarrollo Hero y navegación. Dev1.
- T3.3 Desarrollo Features/Benefits y Social Proof. Dev2.
- T3.4 Desarrollo How it works, Pricing, FAQ. Dev2.
- T3.5 Formularios (captación leads/demo request) + validaciones. Dev