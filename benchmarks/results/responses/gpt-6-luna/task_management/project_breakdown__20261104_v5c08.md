# GPT-6 Luna — task_management/project_breakdown

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.86 | quality: 9.8
- latency_total: 11.011s | tokens_per_second: 94.5
- input_tokens: 69 | output_tokens: 1041
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## Plan de lanzamiento en 4 semanas

**Supuestos:** la landing presenta un producto SaaS ya definido y estará en español. El plan cubre contenido, diseño, desarrollo, QA y publicación; no incluye cambios importantes en el producto ni una campaña de marketing extensa. Con este equipo, conviene fijar el alcance y evitar nuevas funcionalidades durante la última semana.

### Fases y tareas

| Fase | Tareas principales | Responsable(s) | Dependencias |
|---|---|---|---|
| **1. Alineación y alcance** | Definir audiencia, propuesta de valor, objetivo de conversión, CTA, funcionalidades a destacar, requisitos legales y métricas. Confirmar dominio, analítica y materiales disponibles. | Copywriter (facilita); diseñador y developers aportan | Ninguna |
| **2. Estructura y contenido** | Preparar sitemap y wireframe de contenido: hero, beneficios, funcionalidades, prueba social, FAQ y CTA. Redactar y revisar textos. Solicitar testimonios, logos o datos de producto. | Copywriter; diseñador revisa jerarquía | Fase 1 |
| **3. Diseño** | Crear wireframes y diseño visual responsive. Definir componentes, estados de CTA, formularios y comportamiento móvil. Revisión y aprobación del equipo. | Diseñador; copywriter valida contenido; developers asesoran factibilidad | Borrador de estructura y textos |
| **4. Desarrollo** | Configurar proyecto y entorno; construir la página responsive; integrar textos, imágenes, formulario o registro, analítica, SEO técnico y eventos de conversión. | Developer 1: estructura e interfaz; Developer 2: formulario, integraciones y analítica; colaboración entre ambos | Diseño aprobado, contenido suficientemente final y accesos a servicios |
| **5. QA y ajustes** | Probar en móvil y escritorio, navegadores principales, enlaces, formulario, analítica, accesibilidad básica, rendimiento y metadatos. Corregir errores y validar textos. | Developers; diseñador revisa visual; copywriter revisa contenido | Versión implementada |
| **6. Lanzamiento** | Publicar, verificar dominio y HTTPS, probar conversiones en producción y monitorizar errores. Preparar plan de reversión si algo falla. | Developers; revisión final del equipo | QA aprobado y materiales finales |

### Timeline

| Semana | Trabajo y resultado esperado |
|---|---|
| **1 — Definición** | Reunión de inicio; acordar audiencia, mensaje, CTA, alcance y métricas. Copywriter entrega estructura y primer borrador de textos. Diseñador define dirección visual y wireframe inicial. **Hito:** alcance y estructura aprobados al final de la semana. |
| **2 — Contenido y diseño** | Completar textos y diseñar la página responsive. Developers preparan el proyecto, identifican integraciones y resuelven dudas técnicas. Revisión conjunta y aprobación del diseño. **Hito:** diseño aprobado y contenido casi final al cierre de la semana. |
| **3 — Implementación** | Desarrollar la página, conectar formulario/registro y analítica, cargar contenido y hacer una primera revisión visual. Copywriter cierra textos; diseñador responde dudas y valida componentes. **Hito:** versión funcional en staging al final de la semana. |
| **4 — QA y publicación** | Probar y corregir; verificar tracking, SEO técnico, rendimiento y formularios. Congelar contenido y diseño a mitad de semana. Publicar hacia el final, dejando tiempo para resolver incidencias. **Hito:** lanzamiento y comprobación en producción. |

### Orden de dependencias clave

**Alcance y mensaje → estructura y textos → diseño aprobado → desarrollo → QA → publicación.**

Para reducir bloqueos, puede arrancar en paralelo el trabajo técnico que no dependa del diseño final —por ejemplo, preparar el entorno y verificar integraciones—, pero la construcción visual debe esperar a que el diseño esté aprobado.

### Reparto recomendado

- **Diseñador:** arquitectura visual, wireframes, diseño responsive y revisión visual de QA.
- **Developer 1:** estructura de la página, componentes y adaptación responsive.
- **Developer 2:** formulario o flujo de registro, integraciones, analítica y soporte de despliegue.
- **Copywriter:** propuesta de valor, estructura narrativa, textos, CTA, FAQ y revisión editorial.
- **Decisiones compartidas:** alcance, aprobación final, métricas y prioridad de correcciones.

### Para que el plazo sea realista

- Nombrar a una persona que apruebe y responda dudas rápidamente; idealmente, en **un día laborable**.
- Limitar la primera versión a una landing y un flujo principal de conversión.
- Tener listos cuanto antes logos, capturas del producto, testimonios, precios y requisitos legales.
- No introducir funcionalidades ni cambios grandes de mensaje durante la última semana.
- Reservar al menos **2–3 días de QA y correcciones** antes de publicar.