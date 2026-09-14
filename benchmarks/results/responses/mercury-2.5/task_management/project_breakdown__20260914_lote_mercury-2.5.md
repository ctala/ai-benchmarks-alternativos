# Mercury 2.5 — task_management/project_breakdown

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.2 | quality: 9.8
- latency_total: 7.472s | tokens_per_second: 259.5
- input_tokens: 62 | output_tokens: 1939
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa



Aquí tienes un plan de proyecto detallado para lanzar la landing page en 4 semanas, optimizado para el equipo actual (1 diseñador, 2 desarrolladores, 1 redactor).

### Fase 1: Estrategia y Contenido (Semana 1)
**Objetivo:** Definir la estructura y redactar los textos base.

| Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- |
| Definir arquitectura de la página (sitemap) | Todos | Inicio | Mapa de sitio aprobado |
| Redactar copy de secciones principales (Hero, Features, CTA) | Copywriter | Mapa de sitio | Borrador de texto |
| Crear wireframes de baja fidelidad | Diseñador | Copy (esbozos) | Wireframes |
| Configurar repositorio y entorno | Desarrolladores | Inicio | Proyecto listo |
| Definir stack técnico y herramientas (Analytics, CRM) | Desarrolladores | Inicio | Documentación técnica |

### Fase 2: Diseño Visual (Semana 2)
**Objetivo:** Finalizar la interfaz y asegurar la alineación visual.

| Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- |
| Diseñar UI de alta fidelidad (Desktop y Mobile) | Diseñador | Copy final | Maquetas en Figma |
| Crear assets gráficos e iconos | Diseñador | UI definida | Librería de activos |
| Revisión de diseño y ajustes | Todos | Maquetas | Diseño aprobado |
| Implementar estructura HTML/CSS base | Desarrolladores | Maquetas | Skeleton listo |
| Integrar sistema de diseño (design tokens) | Desarrolladores | UI aprobada | Componentes reutilizables |

### Fase 3: Desarrollo e Integración (Semana 3)
**Objetivo:** Construir la funcionalidad y conectar servicios externos.

| Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- |
| Maquetar secciones (Hero, Grid, Testimonios) | Desarrolladores | Skeleton listo | Página funcional interna |
| Configurar formulario y conexión con CRM/Email | Desarrolladores | Diseño aprobado | Sistema de captura activo |
| Adaptar a móviles y tabletas (Responsive) | Desarrolladores | Maquetas | Diseño responsive |
| Redacción final de textos y ajustes SEO | Copywriter | Maquetas finales | Textos en sitio |
| Asegurar accesibilidad (WCAG) | Diseñador/Dev | Desarrollo | Validación de contraste y navegación |

### Fase 4: Pruebas y Lanzamiento (Semana 4)
**Objetivo:** Validar calidad, optimizar y publicar.

| Tarea | Responsable | Dependencias | Entregable |
| :--- | :--- | :--- | :--- |
| QA funcional (test de formularios, enlaces) | Desarrolladores | Desarrollo final | Informe de bugs |
| Optimización de rendimiento (Core Web Vitals) | Desarrolladores | QA inicial | Score de velocidad |
| Auditoría final de contenidos y SEO on-page | Copywriter | QA inicial | Lista de verificación SEO |
| Configuración de dominio y DNS | Desarrolladores | QA final | Sitio accesible |
| Lanzamiento oficial y monitoreo | Todos | DNS configurado | Página en producción |

### Consideraciones Clave
*   **Cuello de botella:** El redactor debe entregar el copy base antes de que el diseñador inicie la UI final para evitar re-trabajos.
*   **Paralelismo:** Mientras el diseñador trabaja en la semana 2, un desarrollador puede comenzar con la estructura base y la configuración técnica.
*   **Riesgos:** Si los cambios en el copy son frecuentes en la semana 3, el equipo de diseño debe priorizar la estabilidad visual.
*   **Post-Lanzamiento:** Planificar una semana de monitoreo post-fecha de lanzamiento para ajustes rápidos de conversión.

Este cronograma es agresivo pero viable si se mantiene una comunicación diaria corta (stand-up) y se prioriza el MVP de la landing page.