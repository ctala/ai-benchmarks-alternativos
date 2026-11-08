# Fugu Max — task_management/project_breakdown

- model_id: `sakana/fugu-max`
- success: True  | final: 8.29 | quality: 9.8
- latency_total: 18.396s | tokens_per_second: 86.9
- input_tokens: 164 | output_tokens: 1598
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## Plan de lanzamiento en 4 semanas

**Objetivo:** publicar una landing clara, responsive y medible para el SaaS de gestión de inventario, con una propuesta de valor validada, formulario funcional y contenido aprobado.

**Supuestos:** ya existe una marca básica y alguien del equipo puede tomar decisiones de producto y aprobar textos/diseño en un máximo de 24 horas. Si no hay identidad visual, integraciones o proceso de aprobación definidos, habrá que reducir alcance o aceptar más riesgo.

### Roles

- **Diseñador/a:** UX, estructura visual, diseño responsive y recursos gráficos.
- **Developer 1 (D1):** estructura del sitio, componentes y desarrollo frontend.
- **Developer 2 (D2):** formularios e integraciones, analítica, despliegue y QA técnico.
- **Copywriter:** investigación, mensajes, textos y metadatos.
- **Responsable de producto/negocio (si está disponible):** define oferta, valida afirmaciones y aprueba entregables. No está incluido en el equipo indicado; es una dependencia clave.

## Fases, tareas y responsables

| Fase / tareas | Responsable principal | Apoyos | Dependencias |
|---|---|---|---|
| **1. Alineación y alcance**: definir audiencia, problema, propuesta de valor, CTA, oferta de lanzamiento, métricas y alcance de la página | Responsable de producto/negocio | Copywriter, diseñador/a, D1, D2 | Ninguna |
| **2. Contenido y estructura**: inventariar mensajes, definir secciones, redactar titulares, beneficios, funcionalidades, objeciones, FAQ y CTA | Copywriter | Producto, diseñador/a | Alineación y acceso a información del producto |
| **3. UX y diseño**: crear wireframe, revisar jerarquía, diseñar desktop/móvil y entregar especificaciones y recursos | Diseñador/a | Copywriter, D1 | Estructura y mensajes iniciales |
| **4. Desarrollo**: implementar página responsive, componentes, estados de formulario, metadatos y accesibilidad básica | D1 | Diseñador/a, copywriter | Diseño aprobado y textos suficientemente estables |
| **5. Integraciones y medición**: conectar formulario con CRM/email, configurar eventos y analítica, dominio y entorno de producción | D2 | D1, responsable de marketing/producto | Herramientas, accesos y campos del formulario definidos |
| **6. QA y preparación del lanzamiento**: revisar contenido, dispositivos, enlaces, formularios, rendimiento, SEO básico y analítica; resolver errores | D1 y D2 | Diseñador/a, copywriter, producto | Versión candidata desplegada |
| **7. Publicación y seguimiento**: desplegar, verificar en producción y monitorizar conversiones y errores | D2 | D1, producto | Aprobación final y checklist completada |

## Timeline realista

### Semana 1 — Decisiones y estructura
- **Día 1:** kickoff de 60–90 minutos. Acordar audiencia principal, problema, diferenciadores, objetivo de conversión y quién aprueba.
- **Días 1–2:** recopilar materiales existentes: logo, capturas del producto, testimonios, precios, políticas y datos para respaldar afirmaciones.
- **Días 2–3:** copywriter prepara mensajes clave y esquema de secciones; producto valida la precisión.
- **Días 3–5:** diseñador/a crea wireframe; se revisa en una sesión breve y se aprueba.
- **Paralelo:** D2 confirma hosting, dominio, formulario/CRM y analítica; D1 prepara repositorio y estructura técnica.

**Hito:** alcance y wireframe aprobados al final de la semana.  
**Riesgo a resolver:** decisiones lentas sobre propuesta de valor o CTA retrasan diseño y desarrollo.

### Semana 2 — Texto y diseño final
- **Días 1–2:** copywriter entrega primera versión completa de textos; producto revisa beneficios, funcionalidades y afirmaciones.
- **Días 1–3:** diseñador/a desarrolla el diseño visual responsive a partir del wireframe y textos preliminares.
- **Días 3–4:** revisión conjunta; cerrar una ronda de cambios priorizados.
- **Día 5:** aprobar diseño y contenido casi final; documentar estados, tamaños, assets y comportamiento móvil.
- **Paralelo:** D2 deja lista la integración de formulario y medición; D1 prepara componentes reutilizables, sin adelantar decisiones visuales inciertas.

**Hito:** diseño aprobado y contenido suficientemente estable para construir.

### Semana 3 — Construcción e integración
- **Días 1–4:** D1 implementa la landing; diseñador/a revisa la fidelidad visual; copywriter termina ajustes y metadatos.
- **Días 2–4:** D2 integra formulario, destino de leads, eventos de conversión, analítica y configuración del entorno.
- **Día 5:** primera versión completa en entorno de prueba; revisión interna de contenido y experiencia en móvil.

**Hito:** versión candidata funcional al final de la semana.  
**Importante:** reservar al menos un día de margen para resolver problemas de integración o diferencias entre diseño y código.

### Semana 4 — QA, correcciones y lanzamiento
- **Días 1–2:** QA funcional y visual: móvil/desktop, navegadores principales, validaciones y confirmación del formulario, enlaces y estados de error/éxito.
- **Día 2:** verificar eventos de analítica y que los leads lleguen correctamente al destino.
- **Días 2–3:** corregir errores y validar accesibilidad básica, rendimiento, SEO técnico y textos finales.
- **Día 4:** aprobación final y checklist de publicación.
- **Día 5:** publicar, probar en producción y monitorizar durante las primeras horas.

**Hito:** lanzamiento al final de la semana 4, con el último día como margen; no conviene programar el estreno antes de confirmar formulario y medición.

## Checklist mínimo de lanzamiento

- Propuesta de valor, CTA y textos aprobados.
- Página usable en móvil y escritorio.
- Formulario probado de principio a fin, incluido el destino de los datos y el mensaje de confirmación.
- Analítica y evento de conversión verificados.
- Dominio, HTTPS, favicon, título y descripción SEO configurados.
- Enlaces, imágenes y navegación revisados.
- Aviso de privacidad y consentimiento incluidos cuando corresponda.
- Procedimiento acordado para revisar leads y errores después de publicar.

## Para proteger el plazo

Mantendría el alcance en **una landing de una sola página**, con formulario y analítica básica. Dejaría para después cualquier calculadora interactiva, animaciones complejas, múltiples variantes de página o integraciones no imprescindibles. Limitar las revisiones a una ronda de wireframe, una de diseño y una de corrección reduce el riesgo de que el calendario se desplace.