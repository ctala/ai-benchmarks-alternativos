# Fugu Max — presentation/slide_outline

- model_id: `sakana/fugu-max`
- success: True  | final: 8.05 | quality: 9.52
- latency_total: 19.7s | tokens_per_second: 221.4
- input_tokens: 257 | output_tokens: 4362
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

A continuación tienes el outline completo para una presentación de 15 slides dirigida al Board de Directores. Las cifras entre corchetes `[ ]` son placeholders que deben completarse con datos del PMO/Finanzas antes de la sesión.

---

## Slide 1 — Portada
- Título: “Plataforma Digital 2.0: Estado del Proyecto y Decisiones Requeridas”.
- Fecha, audiencia: Board de Directores.
- Responsables: Sponsor ejecutivo, Project Manager y líderes de workstream.

**Visual sugerido:** Imagen corporativa sobria + logo del proyecto.  
**Notas del presentador:** Presentar el objetivo de la sesión: informar con transparencia y obtener decisiones concretas del Board. Mantener tono ejecutivo y orientado a acción.

---

## Slide 2 — Resumen ejecutivo
- Estado general del proyecto: `[Verde / Ámbar / Rojo]` con justificación breve.
- Avance global: `[X%]` vs plan `[Y%]`; próximo hito crítico: `[hito y fecha]`.
- Presupuesto ejecutado: `[X%]` del total aprobado; forecast al cierre: `[Y%]`.
- Principales riesgos y decisiones requeridas hoy: `[3 decisiones clave]`.

**Visual sugerido:** Dashboard ejecutivo con 4 KPI cards y semáforo RAG.  
**Notas del presentador:** Esta slide debe dejar el mensaje central: el proyecto está en `[estado]`, requiere `[atención/decisión]` y hoy se solicitan `[X]` aprobaciones.

---

## Slide 3 — Estado actual del proyecto
- Fase actual: `[diseño / build / piloto / despliegue]`, con alcance entregado a la fecha: `[X]`.
- Módulos o capacidades ya operativas: `[listado breve]`.
- Bloqueos actuales: `[dependencia técnica / proveedor / negocio / talento]`.
- Calidad y estabilidad: `[disponibilidad, defectos críticos, deuda técnica relevante]`.

**Visual sugerido:** Semáforo RAG por dimensión: alcance, plazo, presupuesto, calidad y adopción.  
**Notas del presentador:** Explicar el estado real sin maquillaje: qué está bajo control y qué requiere intervención del Board o del comité ejecutivo.

---

## Slide 4 — Objetivos y alcance de la fase actual
- Objetivos prioritarios del periodo: `[3 objetivos medibles]`.
- Alcance comprometido: `[módulos/entregables incluidos]`.
- Fuera de alcance temporalmente: `[items diferidos]`.
- Criterios de éxito: `[KPI de negocio, técnicos y de adopción]`.

**Visual sugerido:** Diagrama de alcance “In / Out” o mapa de capacidades.  
**Notas del presentador:** Alinear expectativas del Board sobre qué se entregará en Q2-Q3 y qué queda explícitamente fuera de alcance para proteger foco y presupuesto.

---

## Slide 5 — Métricas de progreso
- Avance global ponderado: `[X%]` vs plan `[Y%]`; desviación: `[Z pp]`.
- Avance por workstream: `[Producto / Tecnología / Datos / Cambio / Operaciones]`.
- Indicadores de cronograma y costo: SPI `[X]`, CPI `[Y]`.
- Hitos cumplidos: `[X de Y]`; hitos en riesgo: `[listado breve]`.

**Visual sugerido:** Gráfico de barras “Plan vs Real” por workstream + indicadores SPI/CPI.  
**Notas del presentador:** Enfatizar tendencia, no solo foto puntual: si la desviación es recuperable o estructural. Señalar el workstream que más atención requiere.

---

## Slide 6 — Hitos completados y próximos hitos
- Hitos completados en el periodo: `[hito 1, hito 2, hito 3]`.
- Hitos en curso: `[hito]`, con fecha comprometida `[fecha]`.
- Próximos hitos críticos Q2-Q3: `[hito y fecha]`.
- Desviaciones y plan de recuperación: `[acción / responsable / fecha]`.

**Visual sugerido:** Timeline tipo Gantt con hitos clave y estado RAG.  
**Notas del presentador:** Mostrar que el plan tiene secuencia lógica y dependencias claras. Hacer foco en los hitos que habilitan valor de negocio o decisiones posteriores.

---

## Slide 7 — Indicadores de adopción, calidad y operación
- Adopción temprana: `[usuarios activos / % adopción / NPS]`.
- Calidad: `[defectos críticos abiertos / tiempo medio de resolución]`.
- Operación: `[disponibilidad / incidentes / performance]`.
- Feedback de negocio: `[satisfacción / principales hallazgos]`.

**Visual sugerido:** Tabla KPI con tendencia (↑↓→) + mini gráfico de evolución.  
**Notas del presentador:** Conectar métricas técnicas con impacto de negocio. Si la adopción es baja, explicar causa y plan de mitigación.

---

## Slide 8 — Riesgos principales y mitigaciones
- Riesgo 1: `[descripción]` — impacto `[Alto/Medio]`, probabilidad `[Alta/Media]`, mitigación `[acción]`.
- Riesgo 2: `[descripción]` — impacto/probabilidad y mitigación.
- Riesgo 3: `[descripción]` — impacto/probabilidad y mitigación.
- Gobernanza de riesgos: revisión quincenal, owners asignados y escalamiento definido.

**Visual sugerido:** Tabla de registro de riesgos con impacto, probabilidad, owner y mitigación.  
**Notas del presentador:** Priorizar los riesgos que requieren decisión o apoyo del Board, no listar todos los riesgos operativos. Explicar qué se está haciendo y qué se necesita.

---

## Slide 9 — Mapa de exposición de riesgos
- Distribución de riesgos por severidad: `[X altos, Y medios, Z bajos]`.
- Exposición concentrada en: `[proveedor / dependencia técnica / talento / regulatorio]`.
- Riesgos aceptados explícitamente: `[listado breve]`.
- Acciones de contención con fecha y responsable.

**Visual sugerido:** Heatmap probabilidad vs impacto.  
**Notas del presentador:** Usar el heatmap para mostrar dónde se concentra la exposición y qué riesgos justifican contingencia presupuestal o patrocinio ejecutivo.

---

## Slide 10 — Presupuesto ejecutado vs planeado
- Presupuesto total aprobado: `[$X]`.
- Ejecutado a la fecha: `[$Y]` (`[Z%]`), vs planeado `[$W]` (`[V%]`).
- Forecast al cierre: `[$X]` con desviación estimada `[+/- %]`.
- Principales drivers de desviación: `[proveedor, alcance, talento, licencias]`.

**Visual sugerido:** Gráfico de barras “Presupuesto planeado vs ejecutado” por trimestre + línea de forecast.  
**Notas del presentador:** Ser claro sobre la salud financiera: si la desviación es temporal o estructural. Explicar qué parte está bajo control del proyecto y qué requiere aprobación del Board.

---

## Slide 11 — Desviaciones presupuestales y eficiencias
- Desviación acumulada: `[$X]` (`[%]`), explicada por `[causa principal]`.
- Contingencia disponible: `[$X]`; contingencia consumida: `[Y%]`.
- Eficiencias o reasignaciones propuestas: `[$X]`.
- Necesidad de aprobación: `[reasignación / contingencia / presupuesto adicional]`.

**Visual sugerido:** Waterfall de desviación presupuestal desde plan hasta forecast.  
**Notas del presentador:** Mostrar el “puente” entre lo planeado y el forecast actual. Hacer explícita la decisión financiera que se solicita, si aplica.

---

## Slide 12 — Roadmap Q2-Q3
- Q2: foco en `[entregables principales]`, hitos `[fechas]`.
- Q3: foco en `[entregables principales]`, hitos `[fechas]`.
- Dependencias críticas: `[proveedores / áreas / infraestructura / datos]`.
- Gates de decisión: `[gate 1]`, `[gate 2]`; criterios de go/no-go.

**Visual sugerido:** Roadmap tipo timeline con swimlanes por workstream y gates.  
**Notas del presentador:** Presentar una secuencia realista y defendible, con gates que permitan al Board evaluar avance antes de comprometer más recursos.

---

## Slide 13 — Dependencias y recursos críticos
- Dependencias interáreas: `[Legal, Finanzas, Operaciones, TI, Negocio]`.
- Dependencias externas: `[proveedor / integrador / licencias]`.
- Capacidad y talento: `[roles críticos / brechas / plan de contratación]`.
- Riesgo de capacidad: `[sobrecarga / rotación / expertise único]`.

**Visual sugerido:** Diagrama de dependencias o tabla RACI resumida.  
**Notas del presentador:** Explicar qué dependencias pueden retrasar el roadmap si no se resuelven. Solicitar patrocinio ejecutivo para destrabar las más críticas.

---

## Slide 14 — Asks al Board
- Ask 1 — Alcance/prioridades: aprobar `[decisión]` para proteger entregables críticos.
- Ask 2 — Presupuesto: aprobar `[reasignación / contingencia / monto]` por `[$X]`.
- Ask 3 — Gobernanza: respaldar `[escalamiento / comité / sponsor]` para resolver dependencias.
- Ask 4 — Plazo/decisión: fechas límite `[fecha]` e impacto de no decidir.

**Visual sugerido:** Tabla de decisiones: Ask, decisión requerida, impacto, deadline y responsable.  
**Notas del presentador:** Formular cada ask de manera binaria y accionable. Cerrar esta slide con la pregunta explícita: “¿El Board aprueba estas `[X]` decisiones?”

---

## Slide 15 — Próximos pasos y cierre
- Decisiones solicitadas hoy: `[resumen de 3-4 decisiones]`.
- Plan 30-60-90 días: `[acciones inmediatas]`.
- Cadencia de reporte al Board: `[mensual / quincenal]` con KPI acordados.
- Mensaje de cierre: proyecto `[viable / requiere apoyo]` para capturar `[beneficio esperado]`.

**Visual sugerido:** Timeline 30-60-90 + recuadro de “Decisiones de hoy”.  
**Notas del presentador:** Cerrar con claridad sobre lo que se necesita del Board y el compromiso del equipo. Dejar una idea final: el proyecto protege `[valor estratégico]` si se resuelven las decisiones clave.