# Claude Sonnet 5.5 — presentation/slide_outline

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.93 | quality: 9.5
- latency_total: 30.474s | tokens_per_second: 144.7
- input_tokens: 219 | output_tokens: 4409
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un esquema detallado y estructurado que cubre todos los aspectos solicitados, con insights útiles para una presentación ejecutiva.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Outline: Estado del Proyecto "Plataforma Digital 2.0"
**Audiencia:** Board de Directores | **Duración sugerida:** 25-30 min + Q&A

> Los valores entre corchetes [X] son placeholders. Reemplázalos con los datos reales antes de presentar.

---

## Slide 1: Portada
**Bullets:**
- Plataforma Digital 2.0: Estado del Proyecto y Próximos Pasos
- Presentado por: [Nombre, cargo]
- Fecha: [Mes/Año] | Período de reporte: [Q1 / hasta fecha]
- Confidencial: solo para uso del Board

**Visual:** Imagen de marca con logo y fondo limpio relacionado con el producto o la plataforma.

**Notas del presentador:** Agradece el tiempo y anticipa la estructura: estado, números, riesgos, finanzas, roadmap y decisiones que necesitamos hoy.

---

## Slide 2: Resumen ejecutivo
**Bullets:**
- Estado general: **[Verde/Amarillo/Rojo]**, con [X%] de avance vs. [Y%] planeado
- Presupuesto: [X%] ejecutado vs. [Y%] planeado (variación de [±Z%])
- Principales logros: [hito 1] y [hito 2]
- Principales riesgos: [riesgo 1] y [riesgo 2]
- Decisiones requeridas hoy: [N asks]

**Visual:** Tablero de una sola página con 4 tarjetas KPI (estado, avance, presupuesto, riesgos) y semáforos.

**Notas del presentador:** Esta slide debe funcionar sola: si el board solo leyera una, que sea esta. Menciona desde el inicio que hay asks al final.

---

## Slide 3: Contexto y objetivos del proyecto
**Bullets:**
- Problema que resuelve: [limitaciones de la plataforma actual]
- Objetivos estratégicos: [crecimiento, eficiencia, experiencia de cliente]
- Resultados esperados: [KPIs objetivo, ej. +X% conversión, -Y% costo operativo]
- Alcance aprobado y fecha de lanzamiento: [fecha]

**Visual:** Diagrama simple que conecte objetivos de negocio, capacidades de la plataforma y KPIs.

**Notas del presentador:** Recuerda brevemente el "por qué" para reconectar al board con la tesis de inversión original. No te extiendas más de 1 minuto.

---

## Slide 4: Estado actual del proyecto
**Bullets:**
- Estado por frente de trabajo: Producto, Tecnología, Datos, Operaciones, Change Management
- Fase actual: [Desarrollo / Piloto / Rollout]
- Avance global: [X%] vs. plan [Y%]
- Cambios de alcance desde el último reporte: [Ninguno / detalle]

**Visual:** Tabla con semáforos (RAG) por frente de trabajo, con una línea de comentario por fila.

**Notas del presentador:** Explica qué significa cada color y por qué cada frente tiene su estado. Si hay amarillos o rojos, adelanta que se tratan en la sección de riesgos.

---

## Slide 5: Hitos completados
**Bullets:**
- [Hito 1]: completado [fecha], [impacto]
- [Hito 2]: completado [fecha], [impacto]
- [Hito 3]: completado [fecha], [impacto]
- Cumplimiento de hitos: [X de Y] a tiempo

**Visual:** Línea de tiempo horizontal con hitos marcados (completados, en curso, pendientes).

**Notas del presentador:** Destaca los logros que reducen riesgo o desbloquean valor de negocio, no solo actividad técnica. Reconoce al equipo brevemente.

---

## Slide 6: Métricas de progreso de entrega
**Bullets:**
- Avance de alcance: [X%] de funcionalidades completadas
- Velocidad del equipo: [tendencia de los últimos N sprints]
- Cumplimiento de cronograma: [X días de desviación]
- Backlog: [N] ítems pendientes, [N] críticos

**Visual:** Gráfico de burn-up (planeado vs. real) junto con un gráfico de barras de velocity por sprint.

**Notas del presentador:** Enfócate en la tendencia, no en un punto aislado. Si hay desviación, explica la causa y el plan de recuperación.

---

## Slide 7: Métricas de negocio y adopción
**Bullets:**
- Usuarios activos en piloto/producción: [N] vs. objetivo [M]
- Adopción por segmento: [segmento A: X%, segmento B: Y%]
- KPIs de negocio: [conversión, NPS, tiempo de proceso, etc.]
- Retorno temprano: [ahorros o ingresos incrementales a la fecha]

**Visual:** Gráfico de líneas (tendencia de adopción) con una tabla de KPIs actual vs. objetivo.

**Notas del presentador:** Este es el puente entre el avance técnico y el valor de negocio. Si los números son tempranos, aclara qué es evidencia y qué es proyección.

---

## Slide 8: Calidad y desempeño técnico
**Bullets:**
- Disponibilidad: [99.X%] vs. SLA [99.Y%]
- Performance: tiempo de carga/respuesta [X ms] vs. objetivo
- Calidad: defectos críticos abiertos [N], cobertura de pruebas [X%]
- Seguridad: [resultado de pentest/auditoría], hallazgos abiertos [N]

**Visual:** Panel con 4 indicadores tipo "gauge" o velocímetro y tendencia mensual.

**Notas del presentador:** Traduce lo técnico a impacto: qué significa esto para cliente, operación y reputación. Evita jerga innecesaria.

---

## Slide 9: Presupuesto ejecutado vs. planeado
**Bullets:**
- Presupuesto total aprobado: [$X]
- Ejecutado a la fecha: [$Y] ([Z%]) vs. planeado [$W] ([V%])
- Variación: [±$ / ±%] y sus causas principales
- Desglose: personal, proveedores, infraestructura/licencias, contingencia

**Visual:** Gráfico de barras agrupadas (planeado vs. real por categoría) más una línea acumulada en el tiempo.

**Notas del presentador:** Explica la variación con claridad: ¿es timing, ahorro o sobrecosto real? El board buscará entender si es estructural o temporal.

---

## Slide 10: Forecast financiero y proyección al cierre
**Bullets:**
- Estimación al cierre (EAC): [$X] vs. presupuesto [$Y]
- Escenarios: base, optimista, pesimista
- Uso de contingencia: [$ usado] de [$ disponible]
- Impacto en el caso de negocio: ROI/payback [actualizado vs. original]

**Visual:** Gráfico de cascada (waterfall) del presupuesto original al forecast, más una tabla de escenarios.

**Notas del presentador:** Sé transparente sobre la incertidumbre y los supuestos clave. Conecta con los asks si hay necesidad de fondos adicionales.

---

## Slide 11: Principales riesgos
**Bullets:**
- Riesgo 1: [descripción], probabilidad [A/M/B], impacto [A/M/B]
- Riesgo 2: [ej. dependencia de proveedor crítico]
- Riesgo 3: [ej. capacidad del equipo o rotación]
- Riesgo 4: [ej. adopción interna / change management]
- Cambios desde el último reporte: [nuevos / cerrados / escalados]

**Visual:** Matriz de calor (probabilidad × impacto) con los riesgos ubicados y numerados.

**Notas del presentador:** Prioriza 3-4 riesgos que realmente importan al board. Señala cuáles requieren su atención o decisión.

---

## Slide 12: Plan de mitigación y dependencias
**Bullets:**
- Acción de mitigación por riesgo: responsable y fecha
- Dependencias críticas: [proveedores, otras áreas, regulatorio]
- Indicadores de alerta temprana (triggers) y plan de contingencia
- Riesgos que requieren apoyo del board: [lista]

**Visual:** Tabla con columnas: riesgo, mitigación, responsable, fecha, estado.

**Notas del presentador:** Demuestra que cada riesgo tiene dueño y plan. Conecta explícitamente con los asks cuando aplique.

---

## Slide 13: Roadmap Q2-Q3
**Bullets:**
- Q2: [entregables clave, ej. cierre de piloto, módulo X en producción]
- Q3: [entregables clave, ej. rollout masivo, integración Y]
- Hitos de decisión (go/no-go): [fechas y criterios]
- Dependencias críticas y ruta crítica

**Visual:** Diagrama tipo Gantt simplificado o roadmap por trimestres con hitos y puntos de decisión destacados.

**Notas del presentador:** Resalta qué valor de negocio se desbloquea en cada trimestre. Indica claramente los puntos donde volveremos al board.

---

## Slide 14: Asks al board
**Bullets:**
- **Ask 1 (decisión):** [ej. aprobar presupuesto adicional de $X para Q2-Q3]
- **Ask 2 (apoyo):** [ej. patrocinio ejecutivo para resolver dependencia con área/proveedor]
- **Ask 3 (alineación):** [ej. validar criterios de go/no-go del rollout]
- Fecha límite de cada decisión y consecuencia de no decidir

**Visual:** Tabla de 3 filas: ask, justificación, impacto si no se aprueba, fecha requerida.

**Notas del presentador:** Sé directo: plantea cada ask, su razón y qué pasa si se retrasa. Pide decisión explícita antes de pasar a preguntas.

---

## Slide 15: Próximos pasos y cierre
**Bullets:**
- Acciones inmediatas (próximos 30 días): [3 acciones con responsable]
- Cadencia de reporte al board: [mensual/trimestral]
- Resumen de decisiones tomadas hoy
- Preguntas y discusión

**Visual:** Lista de acciones con responsables y fechas, con un cierre visual limpio y datos de contacto.

**Notas del presentador:** Resume en 30 segundos los tres mensajes clave: dónde estamos, qué riesgos vigilamos y qué necesitamos del board. Abre espacio para preguntas.

---

## Apéndice sugerido (fuera de los 15 slides)
- Detalle financiero por partida
- Registro completo de riesgos
- Detalle técnico de arquitectura
- Glosario de términos y KPIs

**Consejo de entrega:** Dedica ~40% del tiempo a las slides 9-14 (finanzas, riesgos, roadmap, asks), porque son las que más influyen en las decisiones del board.

Si me compartes los datos reales (avance, presupuesto, riesgos), puedo convertir este outline en contenido final listo para cada slide.