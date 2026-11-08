# Claude Fable 5.1 — presentation/slide_outline

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.22 | quality: 9.22
- latency_total: 76.957s | tokens_per_second: 76.1
- input_tokens: 219 | output_tokens: 5854
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

# Plataforma Digital 2.0 — Status Report al Board de Directores

**Outline de presentación (15 slides)**

> Nota: los valores entre corchetes `[ ]` son placeholders para completar con datos reales del proyecto. La estructura sigue la lógica típica de un board: conclusión primero, evidencia después, decisiones al final.

---

### Slide 1 — Portada
**Contenido:**
- Plataforma Digital 2.0 — Reporte de Estado al Board
- Fecha de la sesión y período cubierto (ej. Q1 [año])
- Presentador(es) y área responsable (ej. PMO / CTO)
- Clasificación: Confidencial — uso interno del Board

**Visual:** Imagen de marca / key visual del proyecto con logo corporativo.

**Notas del presentador:** Agradecer el tiempo del Board y anunciar que la presentación durará ~20 minutos con 10 minutos reservados para decisiones. Anticipar que hay [N] asks concretos al final.

---

### Slide 2 — Agenda
**Contenido:**
- Resumen ejecutivo y semáforo general
- Estado actual y métricas de progreso
- Presupuesto: ejecutado vs. planeado
- Riesgos y mitigaciones
- Roadmap Q2–Q3 y decisiones requeridas del Board

**Visual:** Lista numerada con íconos; marcar en color la sección de "Decisiones requeridas".

**Notas del presentador:** Señalar que las primeras secciones son contexto y evidencia; el foco de la discusión debe estar en los riesgos y los asks.

---

### Slide 3 — Resumen Ejecutivo (BLUF)
**Contenido:**
- Estado global del proyecto: **[Verde / Ámbar / Rojo]** — [una frase de diagnóstico]
- Avance: [X]% completado vs. [Y]% planeado a la fecha
- Presupuesto: [X]% ejecutado vs. [Y]% planeado (desviación de [±Z]%)
- Riesgo principal: [nombre del riesgo] — requiere decisión del Board
- Fecha de go-live: [fecha] — [se mantiene / se desplaza N semanas]

**Visual:** Dashboard tipo semáforo con 4 indicadores (Alcance, Cronograma, Presupuesto, Riesgos).

**Notas del presentador:** Esta es la slide más importante: si el Board solo recuerda una, debe ser esta. Dar el mensaje de fondo en 30 segundos antes de entrar en detalle.

---

### Slide 4 — Contexto: Qué es Plataforma Digital 2.0 y por qué importa
**Contenido:**
- Objetivo estratégico: [ej. unificar canales digitales y reducir time-to-market de nuevos productos]
- Business case aprobado: inversión de [$X] con retorno esperado de [$Y] / ROI [Z]% a [N] años
- Alcance en 3 pilares: [ej. nueva arquitectura core, experiencia cliente omnicanal, datos y analítica]
- Duración total: [N] meses — iniciado en [mes/año], go-live previsto [mes/año]

**Visual:** Diagrama simple de 3 pilares o "casa" del proyecto con los beneficios esperados en la parte superior.

**Notas del presentador:** Recordatorio breve para miembros nuevos o que no vieron la aprobación original; no profundizar más de 1 minuto.

---

### Slide 5 — Estado Actual por Workstream
**Contenido:**
- Arquitectura e Infraestructura: [estado] — [% avance] — [hito clave logrado]
- Desarrollo de Producto / Front-end: [estado] — [% avance] — [comentario]
- Datos, Integraciones y Migración: [estado] — [% avance] — [comentario]
- Gestión del Cambio y Adopción: [estado] — [% avance] — [comentario]
- Seguridad y Cumplimiento: [estado] — [% avance] — [comentario]

**Visual:** Tabla con columnas: Workstream | Semáforo | % Avance | Hito reciente | Próximo hito | Owner.

**Notas del presentador:** Enfocarse en los workstreams en ámbar o rojo; explicar en una oración por qué están ahí y qué cambió desde el último reporte.

---

### Slide 6 — Hitos: Planeado vs. Real
**Contenido:**
- Hitos completados a tiempo: [N] de [M] planeados a la fecha
- Hitos completados con retraso: [lista breve con días de desviación]
- Hitos pendientes del período: [lista] — nueva fecha comprometida
- Hitos próximos (siguientes 90 días): [lista con fechas]

**Visual:** Gantt simplificado o línea de tiempo con hitos planeados (gris) vs. reales (color), destacando desviaciones.

**Notas del presentador:** Ser transparente con los retrasos y conectarlos con las causas raíz que se verán en la sección de riesgos. Evitar justificaciones extensas aquí.

---

### Slide 7 — Métricas de Progreso (KPIs del Proyecto)
**Contenido:**
- Avance de alcance: [X] de [Y] funcionalidades entregadas ([Z]%)
- Velocidad del equipo: [X] story points/sprint vs. [Y] planeados (tendencia [↑/↓/=])
- Schedule Performance Index (SPI): [valor] (1.0 = en plan)
- Cost Performance Index (CPI): [valor]
- Defectos abiertos críticos/altos: [N] vs. umbral aceptable de [M]

**Visual:** Panel de 4–5 gráficos pequeños (sparklines o gauges) mostrando tendencia de cada KPI en los últimos 3–6 meses.

**Notas del presentador:** Explicar en lenguaje de negocio qué significan SPI y CPI ("por cada dólar/día planeado, estamos entregando X"). Resaltar la tendencia más que el valor puntual.

---

### Slide 8 — Métricas de Resultado y Adopción
**Contenido:**
- Usuarios en piloto/producción: [N] vs. meta [M]
- Indicadores de valor temprano: [ej. reducción de [X]% en tiempo de proceso, NPS piloto [Y]]
- Disponibilidad / performance de la plataforma: [X]% uptime, latencia [Y] ms
- Capacitación completada: [X]% del personal objetivo
- Benefit tracking: [$X] de beneficios ya materializados vs. [$Y] previstos a la fecha

**Visual:** Gráfico de barras comparando "Meta vs. Real" por métrica, más una curva de adopción acumulada.

**Notas del presentador:** Esta slide responde a "¿está generando valor?" — separar claramente lo que ya es evidencia real de lo que es proyección.

---

### Slide 9 — Presupuesto: Ejecutado vs. Planeado
**Contenido:**
- Presupuesto total aprobado: [$X] | Ejecutado a la fecha: [$Y] ([Z]%)
- Planeado a la fecha: [$W] → desviación de [±$] / [±%]
- Desglose por categoría: Personal interno [$], Proveedores/consultoría [$], Licencias y cloud [$], Contingencia [$]
- Contingencia utilizada: [X]% de [$Y] disponible
- Compromisos pendientes (commitments) no reflejados aún en ejecución: [$]

**Visual:** Gráfico de barras agrupadas (Planeado vs. Ejecutado por categoría) + curva S acumulada de gasto planeado vs. real.

**Notas del presentador:** Aclarar si la desviación es de timing (gasto desplazado) o estructural (costo real mayor). El Board querrá saber si el total final cambia.

---

### Slide 10 — Análisis de Desviaciones y Forecast al Cierre
**Contenido:**
- Principales causas de desviación: [ej. extensión de consultoría +$X, ahorro en licencias -$Y, retraso de migración +$Z]
- Estimate at Completion (EAC): [$X] vs. presupuesto aprobado [$Y] → [sobre/bajo] en [Z]%
- Acciones de contención ya implementadas: [lista breve]
- Escenarios: Base [$] | Optimista [$] | Pesimista [$] con supuestos clave

**Visual:** Gráfico tipo "waterfall" (cascada) desde presupuesto aprobado hasta EAC, mostrando cada ajuste.

**Notas del presentador:** Si el EAC supera el aprobado, este es el momento de prepararlo como ask formal (slide 14). Presentar los escenarios con honestidad sobre su probabilidad.

---

### Slide 11 — Riesgos Principales
**Contenido:**
- R1 — [ej. Dependencia de proveedor crítico en integración core]: Probabilidad [A/M/B], Impacto [A/M/B], Tendencia [↑/↓/=]
- R2 — [ej. Disponibilidad de talento clave / rotación]: Prob. [ ], Impacto [ ], Tendencia [ ]
- R3 — [ej. Calidad de datos para migración]: Prob. [ ], Impacto [ ], Tendencia [ ]
- R4 — [ej. Cambios regulatorios / cumplimiento]: Prob. [ ], Impacto [ ], Tendencia [ ]
- Issues ya materializados (no riesgos): [N] — [el más relevante]

**Visual:** Matriz de calor 3×3 (Probabilidad × Impacto) con los riesgos ubicados y flechas de tendencia.

**Notas del presentador:** Diferenciar explícitamente riesgos (pueden ocurrir) de issues (ya ocurrieron). Dedicar el tiempo a los 2 riesgos que el Board puede ayudar a mitigar.

---

### Slide 12 — Plan de Mitigación y Owners
**Contenido:**
- R1 → Mitigación: [acción] | Owner: [nombre] | Fecha: [ ] | Estado: [ ]
- R2 → Mitigación: [acción] | Owner: [ ] | Fecha: [ ] | Estado: [ ]
- R3 → Mitigación: [acción] | Owner: [ ] | Fecha: [ ] | Estado: [ ]
- R4 → Mitigación: [acción] | Owner: [ ] | Fecha: [ ] | Estado: [ ]
- Riesgos que requieren intervención del Board: [identificar cuáles y por qué]

**Visual:** Tabla de mitigación (Riesgo | Acción | Owner | Fecha | Estado | Requiere Board: Sí/No).

**Notas del presentador:** Mostrar que cada riesgo tiene dueño y plan activo; marcar claramente cuáles no pueden resolverse sin apoyo o decisión del Board.

---

### Slide 13 — Roadmap Q2–Q3
**Contenido:**
- **Q2:** [ej. cierre de migración de datos fase 1, piloto extendido a [N] usuarios, certificación de seguridad]
- **Q3:** [ej. go-live de módulo [X], desmantelamiento de sistema legado, inicio de fase 2]
- Hitos de decisión (gates): [fecha] Go/No-Go piloto | [fecha] Go/No-Go go-live
- Dependencias críticas externas: [proveedor/área/regulador]
- Capacidad requerida: [N] FTEs adicionales en [período] / [recursos clave]

**Visual:** Roadmap horizontal por trimestre con swimlanes por workstream y gates de decisión marcados con rombos.

**Notas del presentador:** Enfatizar los gates donde el Board será consultado nuevamente y las dependencias que están fuera del control del equipo.

---

### Slide 14 — Decisiones Requeridas del Board (Asks)
**Contenido:**
- **Ask 1 — Presupuesto:** Aprobar [ampliación de $X / reasignación de contingencia] para [propósito]. Impacto si no se aprueba: [consecuencia]
- **Ask 2 — Alcance/Cronograma:** Aprobar [ajuste de fecha de go-live a [fecha] / descope de funcionalidad [X] a fase 2]
- **Ask 3 — Recursos/Sponsorship:** [ej. asignación de ejecutivo sponsor para área [X] / priorización sobre proyecto [Y]]
- **Ask 4 — Proveedores:** [ej. autorización para renegociar/sustituir contrato con [proveedor]]
- Para cada ask: fecha límite de decisión y qué pasa si se posterga

**Visual:** Tabla de decisiones (Ask | Justificación | Opciones evaluadas | Recomendación | Fecha límite) con la opción recomendada resaltada.

**Notas del presentador:** Presentar cada ask con la recomendación del equipo y las alternativas consideradas; pedir la decisión explícita en la sesión o fijar fecha de resolución.

---

### Slide 15 — Próximos Pasos y Cierre
**Contenido:**
- Acciones inmediatas (próximos 30 días): [3 acciones con owner]
- Próximo reporte al Board: [fecha] — incluirá [resultado del gate / piloto / etc.]
- Canal de seguimiento intermedio: [dashboard / comité de steering mensual]
- Mensaje de cierre: [una frase de confianza basada en evidencia, no en optimismo]
- Espacio para preguntas y discusión

**Visual:** Lista limpia de acciones + imagen de cierre con los datos de contacto del equipo del proyecto.

**Notas del presentador:** Resumir en 20 segundos las decisiones tomadas en la sesión y confirmar los compromisos de seguimiento. Abrir a preguntas.

---

### Anexo sugerido (backup slides, no contar en las 15)
- Detalle de presupuesto línea por línea
- Registro completo de riesgos
- Métricas técnicas (arquitectura, deuda técnica, cobertura de pruebas)
- Resultados detallados del piloto / encuestas de usuarios
- Comparativa con benchmarks de proyectos similares

### Tips rápidos para la sesión
- **Regla 1-3-1:** 1 mensaje central, 3 evidencias de soporte, 1 decisión clara por tema.
- Usar siempre el mismo código de colores (verde/ámbar/rojo) en todas las slides.
- Si el proyecto está en ámbar/rojo, decirlo en la slide 3, no en la 11: el Board valora la transparencia temprana.