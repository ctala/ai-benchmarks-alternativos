# Claude Haiku 5.5 — task_management/project_breakdown

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.81 | quality: 9.8
- latency_total: 14.465s | tokens_per_second: 202.2
- input_tokens: 117 | output_tokens: 2925
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan de proyecto para la landing page de tu SaaS de gestión de inventario, con 4 semanas de duración y el equipo que describes (1 diseñador, 2 developers, 1 copywriter).

## Supuestos previos

- La landing es una página única (o con pocas secciones) con formulario de captura o botón de prueba gratuita.
- Se usará un stack web estándar (p. ej. Next.js, Webflow o similar) y un proveedor de analítica.
- Ya existe una marca mínima (logo, colores, tipografía). Si no, el diseñador debe definirla en la Fase 1.
- Si hay que construir también el backend de registro/onboarding, eso queda fuera de este plan y conviene tratarlo como proyecto aparte.

## Fases, tareas, responsables y dependencias

### Fase 0 — Preparación (Días 1–2)
| Tarea | Responsable | Dependencias |
|---|---|---|
| Definir objetivo principal de la landing (leads, pruebas, pre-registro) | Producto / líder del proyecto | Ninguna |
| Definir propuesta de valor, público objetivo y 3–5 beneficios clave | Copywriter + producto | Objetivo definido |
| Inventario de activos existentes (logo, capturas, testimonios, datos) | Diseñador | Ninguna |
| Definir stack técnico y herramientas de analítica/formularios | Developer senior | Ninguna |

### Fase 1 — Estrategia y diseño (Semana 1)
| Tarea | Responsable | Dependencias |
|---|---|---|
| Esquema de contenido (wireframe de secciones: hero, problema, solución, features, prueba social, pricing/CTA, FAQ) | Copywriter + diseñador | Propuesta de valor |
| Redacción de copy por sección (titulares, subtítulos, CTAs, microcopy) | Copywriter | Esquema de contenido |
| Wireframes de baja fidelidad (desktop y móvil) | Diseñador | Esquema de contenido |
| Diseño visual de alta fidelidad (desktop y móvil) | Diseñador | Wireframes aprobados |
| Sistema de componentes básicos (botones, tipografía, espaciados) | Diseñador + developer | Diseño de alta fidelidad |
| Configuración del repositorio, entorno de desarrollo y despliegue en staging | Developer 1 | Stack definido |

**Hito 1 (fin de semana 1):** copy y diseño aprobados por el equipo y el stakeholder.

### Fase 2 — Desarrollo (Semana 2)
| Tarea | Responsable | Dependencias |
|---|---|---|
| Maquetado de secciones en código (estructura y estilos) | Developer 1 | Diseño aprobado |
| Responsive (móvil, tablet) | Developer 1 | Maquetado |
| Formulario de captura, validaciones y conexión con CRM/email marketing | Developer 2 | Definición de campos y proveedor |
| Integración de analítica (GA4/eventos de conversión) y píxeles | Developer 2 | Proveedor de analítica elegido |
| Implementación de SEO técnico (meta tags, Open Graph, sitemap, datos estructurados, velocidad) | Developer 2 | Copy final de metadatos |
| Carga e integración de copy final | Developer 1 + copywriter | Copy aprobado |
| Preparar assets optimizados (imágenes, vídeo, iconos) | Diseñador | Diseño aprobado |

**Hito 2 (fin de semana 2):** landing funcional en staging, sin revisión de detalles finos.

### Fase 3 — QA, pruebas y optimización (Semana 3)
| Tarea | Responsable | Dependencias |
|---|---|---|
| Pruebas funcionales (formularios, enlaces, CTAs, envíos) | Developer 2 | Hito 2 |
| Pruebas cross-browser y de dispositivos | Developer 1 | Hito 2 |
| Revisión visual y de consistencia de marca | Diseñador | Hito 2 |
| Revisión de copy, ortografía y tono | Copywriter | Hito 2 |
| Pruebas de rendimiento (Lighthouse, Core Web Vitals) y accesibilidad (WCAG básico) | Developer 1 | Hito 2 |
| Prueba de flujo de conversión completo y verificación de eventos de analítica | Developer 2 | Integraciones terminadas |
| Preparar página de gracias / confirmación y emails automáticos | Copywriter + Developer 2 | Formulario funcionando |
| Ronda de feedback de stakeholders y correcciones | Todo el equipo | Pruebas internas |

**Hito 3 (fin de semana 3):** landing lista para producción, con feedback incorporado y QA aprobado.

### Fase 4 — Lanzamiento y post-lanzamiento (Semana 4)
| Tarea | Responsable | Dependencias |
|---|---|---|
| Configuración de dominio, DNS, SSL y redirecciones | Developer 1 | QA aprobado |
| Despliegue a producción y verificación post-deploy | Developer 1 | Dominio listo |
| Verificación de analítica y formularios en producción | Developer 2 | Despliegue |
| Preparar materiales de difusión (anuncios, email, redes) con las piezas de copy | Copywriter + diseñador | Copy final |
| Configurar pruebas A/B o plan de medición de conversión | Developer 2 + producto | Analítica activa |
| Monitoreo de las primeras 48 h (errores, conversión, tiempos de carga) | Developer 1 | Lanzamiento |
| Retrospectiva y lista de mejoras para iteraciones | Todo el equipo | Lanzamiento |

**Hito 4 (día 28):** landing publicada, medición activa y primeros datos revisados.

## Timeline resumido

- **Semana 1:** estrategia, copy, diseño. Hito: diseño aprobado.
- **Semana 2:** desarrollo e integraciones. Hito: staging funcional.
- **Semana 3:** QA, correcciones, optimización. Hito: listo para producción.
- **Semana 4:** lanzamiento, medición y difusión. Hito: publicada y monitorizada.

## Ruta crítica y riesgos

- **Ruta crítica:** aprobación de copy y diseño (Semana 1) → maquetado → integraciones → QA. Un retraso en la aprobación desplaza todo el proyecto, por eso conviene fijar una fecha límite de aprobación y un único decisor.
- **Riesgos principales:**
  - Cambios de alcance durante el diseño. Mitigación: congelar el alcance al final de la Fase 1.
  - Dependencia de proveedores externos (CRM, email, analítica). Mitigación: configurarlos en la Fase 0.
  - Falta de testimonios o datos reales para prueba social. Mitigación: el copywriter identifica pronto qué pruebas existen y, si no hay, usa lenguaje de beneficios sin cifras inventadas.
  - Carga de trabajo del diseñador concentrada en Semanas 1 y 2. Mitigación: que los developers preparen la estructura base mientras se diseña.
- **Holgura:** el plan no tiene margen. Si quieres más seguridad, reserva 2–3 días al final de la Semana 3 como colchón.

## Reparto de carga por persona

- **Diseñador:** intensivo en Semana 1, moderado en Semana 2 (assets), revisión en Semana 3, apoyo en difusión en Semana 4.
- **Developer 1:** configuración y maquetado (Semanas 1–2), QA de rendimiento y cross-browser (Semana 3), despliegue (Semana 4).
- **Developer 2:** integraciones y SEO (Semana 2), QA funcional y analítica (Semana 3), verificación en producción (Semana 4).
- **Copywriter:** intensivo en Semana 1, soporte en integración de textos (Semana 2), revisión (Semana 3), piezas de difusión (Semana 4).

Si me dices el stack exacto, el proveedor de CRM/email y si ya tienes marca definida, puedo ajustar las tareas técnicas y el timeline con más detalle.