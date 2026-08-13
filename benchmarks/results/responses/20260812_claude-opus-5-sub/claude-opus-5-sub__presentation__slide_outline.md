# Claude Opus 5 (suscripción) — presentation/slide_outline

- model_id: `claude-opus-5`
- success: True  | final: 7.48 | quality: 9.42
- latency_total: 96.825s | tokens_per_second: 63.6
- input_tokens: 2 | output_tokens: 6162
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

Acá está el outline. Las cifras van como placeholders `[ ]` porque no tengo la data real del proyecto — reemplázalas antes de presentar.

**Principio de estructura:** un board no quiere el relato cronológico, quiere saber si el proyecto está sano, cuánto falta, qué puede matarlo y qué decisión le estás pidiendo. Por eso el ask aparece en el slide 2 y se repite en el 15.

---

## Slide 1 — Plataforma Digital 2.0: Revisión de Estado al [fecha]

- Nombre del proyecto, período cubierto y sponsor ejecutivo
- Semáforo global: **[Verde / Ámbar / Rojo]**
- Presentador, equipo y fecha de la sesión
- Referencia al último reporte al board ([fecha]) para continuidad

**Visual:** Portada limpia con el logo, el semáforo grande y una línea de tiempo mínima que marque "estamos aquí".

**Notas:** Abrir declarando el estado en una sola palabra antes de cualquier detalle. Si el semáforo es ámbar o rojo, decirlo en los primeros 15 segundos evita que el board lo descubra a mitad del deck.

---

## Slide 2 — Resumen ejecutivo: lo que necesitan saber

- Avance global: **[X]%** completado vs **[Y]%** planeado a la fecha
- Presupuesto ejecutado: **$[A]** de **$[B]** aprobado (**[Z]%**)
- Fecha de go-live proyectada: **[fecha]** (plan original: **[fecha]**)
- Riesgo principal: **[una línea]**
- **3 decisiones que pedimos hoy:** [ask 1], [ask 2], [ask 3]

**Visual:** Tablero de 4 KPIs con semáforo individual (alcance, tiempo, costo, calidad) + caja destacada con los asks.

**Notas:** Este es el único slide que todos van a recordar. Si alguien se va después de este slide, debe irse con el estado y el pedido completos.

---

## Slide 3 — Por qué existe este proyecto: caso de negocio vigente

- Problema original: [dolor de negocio que motivó la inversión]
- Beneficio esperado: **$[monto]** anual / **[X]%** de reducción en [métrica]
- Supuestos del caso de negocio que **siguen siendo válidos**: [lista corta]
- Supuestos que **cambiaron** desde la aprobación: [lista corta]
- ROI proyectado actualizado vs ROI aprobado: **[X]% vs [Y]%**

**Visual:** Tabla de dos columnas — "Lo que aprobamos" vs "Lo que sabemos hoy" — con las filas cambiadas resaltadas.

**Notas:** Reanclar al board en el objetivo evita que la conversación derive a features. Si algún supuesto cambió, nombrarlo acá y no esconderlo en riesgos.

---

## Slide 4 — Estado actual: dónde estamos contra el plan

- Fase actual: **[fase]** de **[total]** (inicio: [fecha], cierre previsto: [fecha])
- Hitos completados: **[N] de [M]**
- Hitos con retraso: **[N]**, con desviación promedio de **[X] semanas**
- Ruta crítica actual pasa por: **[componente/entregable]**
- Cambio material desde el último reporte: **[uno]**

**Visual:** Gantt simplificado (máximo 8 barras) con línea vertical de "hoy" y barras retrasadas en color de alerta.

**Notas:** Mostrar solo hitos de nivel board, no tareas de equipo. Un Gantt con 40 filas hace que el board deje de mirar la pantalla.

---

## Slide 5 — Logros del período: qué se entregó

- **[Entregable 1]** — en producción desde [fecha], usado por [N] usuarios
- **[Entregable 2]** — completado, pendiente de aceptación de [área]
- **[Entregable 3]** — integración con [sistema legacy] operativa
- Capacidad habilitada que antes no existía: **[una frase]**
- Reconocimiento del equipo: [mención breve si aplica]

**Visual:** Antes/después en dos paneles — captura del flujo viejo vs el nuevo — o iconografía de 3 hitos entregados.

**Notas:** Anclar cada entregable a un resultado observable, no a "se completó el sprint 14". El board compra evidencia de funcionamiento, no actividad.

---

## Slide 6 — Avance de entregables: plan vs real

- Módulos completados: **[N]/[M]** (**[X]%**)
- Velocidad del equipo: **[X]** puntos/sprint promedio, tendencia **[estable/a la baja/al alza]**
- Alcance agregado post-aprobación: **[N]** solicitudes de cambio, **[X]%** de esfuerzo adicional
- Proyección de cierre con la velocidad actual: **[fecha]**
- Brecha vs plan: **[X] semanas**

**Visual:** Gráfico burn-up (no burn-down) con dos líneas: alcance total y trabajo completado. El burn-up muestra el scope creep, que es exactamente lo que un board debe ver.

**Notas:** Si la línea de alcance sube, explicar quién aprobó cada cambio. El scope creep no discutido es la causa más común de que un board se sienta engañado al final.

---

## Slide 7 — Adopción y uso: la plataforma en manos reales

- Usuarios activos: **[N]** de **[M]** objetivo (**[X]%** de penetración)
- Transacciones procesadas: **[N]** en el período, crecimiento **[X]%** vs anterior
- Tasa de adopción por unidad de negocio: mejor **[área, X%]** / peor **[área, Y%]**
- Satisfacción de usuario (CSAT/NPS): **[valor]** vs objetivo **[valor]**
- Migración desde el sistema legacy: **[X]%** completada

**Visual:** Gráfico de barras por unidad de negocio con línea horizontal de meta, o cohortes de adopción mes a mes.

**Notas:** La adopción baja en un área específica suele ser un problema de gestión del cambio, no de producto. Tener lista la causa raíz por si preguntan por el área rezagada.

---

## Slide 8 — Salud técnica: lo que sostiene la plataforma

- Disponibilidad del período: **[XX,X]%** vs SLA comprometido **[XX,X]%**
- Incidentes críticos (P1): **[N]**, tiempo medio de resolución **[X] horas**
- Deuda técnica acumulada: **[X]%** del backlog, tendencia **[dirección]**
- Cobertura de pruebas automatizadas: **[X]%**
- Hallazgos de seguridad abiertos: **[N] críticos / [N] altos**

**Visual:** Tabla semáforo de 5 filas (métrica / actual / objetivo / tendencia), con flechas de dirección.

**Notas:** Traducir cada métrica técnica a consecuencia de negocio: "99,2% de disponibilidad significa [X] horas de operación caída al mes". Sin esa traducción el board no puede evaluar el riesgo.

---

## Slide 9 — Presupuesto: ejecutado vs planeado

- Presupuesto aprobado total: **$[B]**
- Ejecutado a la fecha: **$[A]** (**[X]%**)
- Planeado a la fecha: **$[C]** (**[Y]%**)
- Desviación: **$[D]** (**[Z]%** [sobre/bajo] lo planeado)
- Composición del gasto: **[X]%** personal, **[Y]%** licencias, **[Z]%** infraestructura, **[W]%** terceros

**Visual:** Gráfico de líneas acumulado con tres curvas — presupuesto planeado, ejecutado real y proyección — más una dona pequeña con la composición del gasto.

**Notas:** Si hay subejecución, aclarar si es ahorro o retraso disfrazado; casi siempre es lo segundo. Un board experimentado va a hacer esa pregunta antes de que termines el slide.

---

## Slide 10 — Proyección a cierre y desviación esperada

- Costo estimado a completar (EAC): **$[E]**
- Desviación proyectada vs aprobado: **$[F]** (**[X]%**)
- Índice de desempeño de costo (CPI): **[valor]** | de cronograma (SPI): **[valor]**
- Contingencia disponible: **$[G]** de **$[H]** original (**[X]%** consumida)
- Escenarios: **base $[E]** / **optimista $[E1]** / **pesimista $[E2]**

**Visual:** Gráfico de tres escenarios (cascada o barras comparativas) mostrando aprobado, EAC base y rango pesimista-optimista.

**Notas:** Presentar el rango, no solo el número base — un board que recibe un único número y ve otro al final pierde la confianza. Indicar qué gatilla el escenario pesimista.

---

## Slide 11 — Mapa de riesgos: los 5 que importan

- **R1 — [nombre]:** probabilidad [alta/media/baja], impacto **$[monto]** / **[X] semanas**
- **R2 — [nombre]:** [probabilidad], impacto [magnitud]
- **R3 — [nombre]:** [probabilidad], impacto [magnitud]
- **R4 — [nombre]:** [probabilidad], impacto [magnitud]
- **R5 — [nombre]:** [probabilidad], impacto [magnitud]
- Riesgos cerrados desde el último reporte: **[N]**

**Visual:** Matriz de calor 3×3 (probabilidad × impacto) con los 5 riesgos posicionados como puntos numerados, y flechas indicando si se movieron desde el último reporte.

**Notas:** Mostrar el movimiento respecto al reporte anterior demuestra que el registro de riesgos está vivo y no se copió del trimestre pasado. Los riesgos cerrados dan credibilidad a los abiertos.

---

## Slide 12 — Riesgo crítico: [nombre del riesgo #1]

- Descripción en una frase: **[qué puede fallar y por qué]**
- Impacto si se materializa: **$[monto]**, **[X] semanas** de retraso, **[efecto en el negocio]**
- Señal temprana que estamos monitoreando: **[indicador concreto]**
- Plan de mitigación en curso: **[acción]**, responsable **[nombre]**, fecha **[fecha]**
- Plan B si la mitigación falla: **[alternativa]** con costo de **$[monto]**
- **Qué necesitamos del board:** [decisión o recurso específico, si aplica]

**Visual:** Diagrama de árbol de decisión — riesgo → mitigación → dos ramas (funciona / no funciona) → consecuencia y plan B.

**Notas:** Este slide existe para que el board no se entere del problema cuando ya es irreversible. Terminar con la fecha límite en la que la decisión deja de estar disponible.

---

## Slide 13 — Roadmap Q2: compromisos del trimestre

- **[Mes 1]:** [hito], criterio de éxito **[medible]**
- **[Mes 2]:** [hito], criterio de éxito **[medible]**
- **[Mes 3]:** [hito], criterio de éxito **[medible]**
- Dependencias externas críticas: **[área/proveedor]** debe entregar **[qué]** antes de **[fecha]**
- Punto de decisión (gate) al cierre de Q2: **[qué se evalúa y con qué criterio]**

**Visual:** Timeline horizontal de 3 meses con hitos como marcadores, dependencias externas en una banda inferior de otro color.

**Notas:** Marcar explícitamente las dependencias que no controla el equipo del proyecto. Son las que el board sí puede desbloquear con una llamada.

---

## Slide 14 — Roadmap Q3 y visión a cierre

- **[Mes 4-6]:** [hitos principales del trimestre]
- Go-live completo proyectado: **[fecha]**
- Apagado del sistema legacy: **[fecha]**, ahorro recurrente de **$[monto]/mes**
- Capacidades que quedan fuera del alcance actual (fase 3): **[lista corta]**
- Transición a operación: modelo de soporte **[descripción]** desde **[fecha]**

**Visual:** Timeline extendido Q2-Q3 con el hito de go-live destacado, más una franja que muestre el traslape entre plataforma nueva y legacy.

**Notas:** Nombrar explícitamente lo que queda fuera del alcance evita que el board asuma que está incluido. El costo de operar dos sistemas en paralelo suele ser la sorpresa más cara del proyecto.

---

## Slide 15 — Asks al board

- **Ask 1 — [Decisión]:** aprobar [qué], por **$[monto]**. Necesario antes de **[fecha]** porque **[consecuencia del retraso]**
- **Ask 2 — [Recurso]:** asignar [qué o quién] desde [área]. Bloqueante para **[hito]**
- **Ask 3 — [Desbloqueo]:** intervención con **[stakeholder externo]** para destrabar **[dependencia]**
- Qué NO estamos pidiendo hoy: **[aclaración que evita discusiones fuera de alcance]**
- Próximo reporte al board: **[fecha]**

**Visual:** Tres tarjetas verticales, una por ask, cada una con decisión, monto, fecha límite y consecuencia de no decidir. Sin gráficos: acá el visual es la claridad.

**Notas:** Cada ask debe poder responderse con sí o no en la misma reunión; si requiere análisis posterior, no es un ask, es un preaviso. Cerrar leyendo las tres decisiones en voz alta y pidiendo confirmación una por una.

---

## Anexos sugeridos (no se presentan, se tienen listos)

- Registro completo de riesgos (todos, no solo el top 5)
- Detalle de presupuesto por línea y proveedor
- Log de solicitudes de cambio con aprobador y fecha
- Arquitectura técnica de la plataforma
- Métricas de adopción desagregadas por área

---

**Dos notas de ejecución:**

1. **Regla del slide 2:** si el board interrumpe en el slide 4 con "¿cuánto nos va a costar al final?", el deck falló en el resumen ejecutivo. Prueba el slide 2 con alguien externo antes de la sesión.

2. **Cifras:** todo lo que está entre `[ ]` necesita una fuente verificable. Un número que no puedes defender cuando te preguntan de dónde salió cuesta más credibilidad que no ponerlo.

Si quieres, lo puedo convertir en un `.pptx` editable + PDF con el skill `deck-ctala` una vez que tengas las cifras reales.