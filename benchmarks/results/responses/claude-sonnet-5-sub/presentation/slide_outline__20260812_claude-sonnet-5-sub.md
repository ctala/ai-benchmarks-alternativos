# Claude Sonnet 5 (suscripción) — presentation/slide_outline

- model_id: `claude-sonnet-5`
- success: True  | final: 7.76 | quality: 9.5
- latency_total: 63.872s | tokens_per_second: 78.4
- input_tokens: 2 | output_tokens: 5008
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un esquema detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board.


## Respuesta completa

# Outline: "Plataforma Digital 2.0" — Board de Directores

*Nota: incluí placeholders entre corchetes `[...]` donde necesitas tus cifras reales. Estructura pensada para 20-25 min de presentación + Q&A.*

---

### Slide 1 — Portada
**Bullets:**
- Plataforma Digital 2.0 — Actualización al Board
- [Fecha] | Presentado por [Nombre/Rol]
- Periodo cubierto: [Q1/mes de inicio] a la fecha

**Visual:** Imagen de marca / logo del proyecto, diseño minimalista
**Notas del presentador:** Abrir agradeciendo el tiempo del board y enmarcar el objetivo de la sesión: alinear estado real, riesgos y decisiones pendientes.

---

### Slide 2 — Resumen ejecutivo
**Bullets:**
- Estado general: [en curso / en riesgo / crítico] — semáforo 🟢🟡🔴
- Progreso vs plan: [X]% completado vs [Y]% esperado a la fecha
- Presupuesto: [X]% ejecutado vs [Y]% planeado
- Riesgo principal a vigilar: [una línea]
- Decisión que se pide hoy al board: [una línea]

**Visual:** Panel de 4 KPIs (scorecard) con semáforo
**Notas del presentador:** Este slide es el "si solo leen uno, que sea este" — dar el titular antes del detalle, el board valora esto más que el recorrido cronológico.

---

### Slide 3 — Objetivo y alcance del proyecto
**Bullets:**
- Problema de negocio que resuelve la plataforma
- Objetivo estratégico ligado a OKRs corporativos
- Alcance: qué incluye y qué explícitamente NO incluye esta fase
- Stakeholders clave / sponsors

**Visual:** Diagrama simple (caja de alcance / scope box)
**Notas del presentador:** Recordatorio breve para nivelar contexto, sobre todo si hay miembros del board que no siguieron el kickoff original.

---

### Slide 4 — Estado actual: overview
**Bullets:**
- Fase actual del proyecto (ej. desarrollo / piloto / rollout)
- % de avance global vs cronograma maestro
- Semáforo por workstream (producto / tecnología / operaciones / adopción)
- Comparación vs el corte anterior presentado al board

**Visual:** Tabla RAG (Red-Amber-Green) por workstream
**Notas del presentador:** Ser explícito sobre qué cambió desde la última reunión — el board recuerda el reporte anterior y busca la delta, no el estado absoluto.

---

### Slide 5 — Hitos completados
**Bullets:**
- [Hito 1] — completado [fecha]
- [Hito 2] — completado [fecha]
- [Hito 3] — completado [fecha]
- Lo que esto habilita para el negocio (impacto, no solo entrega técnica)

**Visual:** Timeline horizontal con hitos marcados
**Notas del presentador:** Conectar cada hito con valor de negocio, no solo "se entregó" — el board pregunta "¿y esto qué desbloquea?".

---

### Slide 6 — Métricas de progreso: adopción y uso
**Bullets:**
- Usuarios activos / adopción vs meta ([X] vs [Y])
- Tasa de conversión o uso del feature clave
- NPS / satisfacción de usuario (si aplica)
- Tendencia últimas 4-8 semanas

**Visual:** Gráfico de línea (tendencia temporal) + comparación vs meta
**Notas del presentador:** Priorizar la tendencia sobre el número puntual — un board quiere saber si vamos mejorando o empeorando, no solo dónde estamos hoy.

---

### Slide 7 — Métricas de progreso: calidad y performance técnico
**Bullets:**
- Uptime / disponibilidad ([X]% vs SLA objetivo)
- Incidentes críticos en el periodo ([N])
- Tiempo de respuesta / performance clave
- Deuda técnica o bloqueos relevantes

**Visual:** Gráfico de barras o dashboard de métricas técnicas
**Notas del presentador:** Traducir a impacto de negocio (ej. "cada minuto de downtime = $X en riesgo") — evitar jerga puramente técnica frente al board.

---

### Slide 8 — Presupuesto: ejecutado vs planeado (resumen)
**Bullets:**
- Presupuesto total aprobado: $[X]
- Ejecutado a la fecha: $[Y] ([Z]%)
- Proyección de cierre: on-budget / sobre-costo / bajo-costo
- Principal driver de la variación (si existe)

**Visual:** Gráfico de barras comparativo (planeado vs ejecutado) o gauge chart
**Notas del presentador:** Ser directo sobre desviaciones — si hay sobre-costo, nombrarlo aquí explícitamente en vez de dejar que aparezca como sorpresa en el detalle.

---

### Slide 9 — Presupuesto: desglose por fase/categoría
**Bullets:**
- Desglose por categoría: personas / tecnología / terceros / contingencia
- Fase con mayor consumo de presupuesto
- Ahorros identificados o reasignaciones propuestas
- Proyección de necesidad adicional (si aplica)

**Visual:** Gráfico de torta o barras apiladas por categoría
**Notas del presentador:** Este slide sostiene cualquier ask de presupuesto adicional que venga en el slide 15 — la lógica debe quedar clara aquí antes de pedir ahí.

---

### Slide 10 — Riesgos: matriz principal
**Bullets:**
- Riesgo 1: [descripción] — probabilidad [alta/media/baja] × impacto [alto/medio/bajo]
- Riesgo 2: [descripción] — probabilidad × impacto
- Riesgo 3: [descripción] — probabilidad × impacto
- Riesgos nuevos vs la última presentación

**Visual:** Matriz 2x2 (probabilidad vs impacto), riesgos como puntos posicionados
**Notas del presentador:** Enfocar la conversación en los riesgos que están en el cuadrante alto-alto — el board necesita saber cuáles requieren su intervención directa.

---

### Slide 11 — Riesgos: plan de mitigación
**Bullets:**
- Riesgo 1 → acción de mitigación → dueño → fecha objetivo
- Riesgo 2 → acción de mitigación → dueño → fecha objetivo
- Riesgo 3 → acción de mitigación → dueño → fecha objetivo
- Riesgos que requieren decisión o apoyo del board para mitigarse

**Visual:** Tabla (riesgo | mitigación | dueño | fecha | estado)
**Notas del presentador:** Distinguir con claridad qué mitigaciones son responsabilidad del equipo ejecutivo y cuáles necesitan una decisión del board para avanzar.

---

### Slide 12 — Roadmap Q2: hitos y entregables
**Bullets:**
- Hito 1 — fecha objetivo — criterio de éxito
- Hito 2 — fecha objetivo — criterio de éxito
- Hito 3 — fecha objetivo — criterio de éxito
- Dependencias críticas para cumplir el trimestre

**Visual:** Gantt simplificado o timeline por hitos
**Notas del presentador:** Anclar cada hito a un criterio medible de éxito, para que la próxima presentación al board se pueda evaluar contra esto mismo.

---

### Slide 13 — Roadmap Q3: hitos y entregables
**Bullets:**
- Hito 1 — fecha objetivo — criterio de éxito
- Hito 2 — fecha objetivo — criterio de éxito
- Hito 3 — fecha objetivo — criterio de éxito
- Supuestos clave sobre los que se construye el plan de Q3

**Visual:** Gantt simplificado o timeline por hitos (continuación del slide 12)
**Notas del presentador:** Ser transparente sobre qué supuestos de Q3 dependen de que Q2 se cumpla como está planeado — evita comprometer fechas en falso.

---

### Slide 14 — Recursos y dependencias necesarias
**Bullets:**
- Recursos actuales del equipo (headcount, roles críticos)
- Gaps de recursos identificados para Q2-Q3
- Dependencias de otras áreas del negocio (legal, IT, compras, etc.)
- Riesgo de no cubrir estos gaps a tiempo

**Visual:** Tabla o diagrama de dependencias entre áreas
**Notas del presentador:** Este slide es el puente directo hacia el ask del siguiente slide — dejar clara la relación causa-efecto entre gap de recursos y riesgo al roadmap.

---

### Slide 15 — Asks al board / decisiones requeridas
**Bullets:**
- Ask 1: [aprobación de presupuesto adicional / decisión de alcance / etc.] — por qué es urgente
- Ask 2: [respaldo ejecutivo para desbloquear dependencia] — por qué es urgente
- Ask 3: [decisión sobre riesgo alto-alto del slide 10] — por qué es urgente
- Fecha límite para cada decisión y qué pasa si no se toma a tiempo

**Visual:** Tabla simple (ask | impacto si no se aprueba | fecha límite)
**Notas del presentador:** Cerrar con máxima claridad y sin ambigüedad — cada ask debe tener una respuesta binaria posible (sí/no/con condiciones) para que la reunión termine con decisiones tomadas, no con "lo vemos después".

---

**Nota de estructura:** los slides 2, 8-9 y 15 son los que más recuerda un board — resumen, dinero y decisiones. Si necesitas recortar a 10-12 slides para una versión ejecutiva más corta, esos tres bloques son los que NO se tocan; el resto (5-7, 12-14) se puede consolidar o mover a apéndice.

¿Quieres que desarrolle alguno de estos slides con el copy completo (no solo bullets) o que arme la versión apéndice con detalle técnico adicional?