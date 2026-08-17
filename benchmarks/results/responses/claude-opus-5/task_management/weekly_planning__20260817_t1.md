# Claude Opus 5 — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 56.219s | tokens_per_second: 80.8
- input_tokens: 320 | output_tokens: 4542
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un plan semanal estructurado que incorpora todas las restricciones y tareas con una lógica bien pensada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Soy product manager. Mi semana tiene estas restricciones:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Necesito meter estas tareas en la semana:
1. Preparar presentacion para la demo (3 horas)
2. Revisar PRDs pendientes (2 horas)
3. Escribir OKRs Q3 (4 horas)
4. Responder emails de stakeholders (1 hora diaria)
5. Revisar metricas del producto (1 hora)
6. One-on-one con 3 reportes directos (30 min cada uno)

Crea un plan semanal detallado con bloques de tiempo especificos.


## Respuesta completa

# Plan Semanal — Product Manager

**Supuestos** (ajústalos si no aplican): jornada 9:00–18:00, almuerzo 12:00–13:00 (excepto lunes), semana de 45h con ~8h ya comprometidas en reuniones fijas.

**Lógica del plan:**
- La prep de la demo termina **el martes**, no el miércoles a las 2 PM. Cero riesgo de llegar sin material.
- Los OKRs (4h, la tarea de mayor carga cognitiva) van el **martes**, tu único día sin interrupciones.
- **Métricas el lunes**: alimentan tanto los OKRs del martes como la narrativa de la demo.
- Emails en bloque fijo diario, nunca en modo reactivo.
- ~20% de la semana queda como buffer (viernes), porque algo se va a mover.

---

## LUNES — Día de contexto y datos

| Hora | Bloque |
|---|---|
| 9:00–11:00 | 🔒 Reunión de directivos |
| 11:00–11:15 | Notas y action items de la reunión (mientras está fresco) |
| 11:15–12:15 | **Emails stakeholders** (1h) |
| 12:15–13:00 | Prep del almuerzo: objetivos y preguntas para el cliente |
| 13:00–14:00 | 🔒 Almuerzo con cliente |
| 14:00–14:15 | Notas del cliente → backlog / insights |
| 14:15–15:45 | **Prep demo — Bloque 1** (1.5h): estructura, guion, flujo |
| 15:45–16:00 | Break |
| 16:00–17:00 | **Revisar métricas del producto** (1h) |
| 17:00–17:30 | **1:1 — Reporte #1** |
| 17:30–18:00 | Cierre + prep del día de deep work |

---

## MARTES — Deep work (día protegido)

> Bloquea el calendario como "Focus — no disponible". Slack en no molestar.

| Hora | Bloque |
|---|---|
| 9:00–10:00 | **Emails stakeholders** (1h) |
| 10:00–12:00 | **OKRs Q3 — Bloque 1** (2h): objetivos + key results borrador |
| 12:00–13:00 | Almuerzo (fuera del escritorio) |
| 13:00–15:00 | **OKRs Q3 — Bloque 2** (2h): métricas, targets, redacción final ✅ *tarea completa* |
| 15:00–15:15 | Break |
| 15:15–16:45 | **Prep demo — Bloque 2** (1.5h): slides, datos del lunes, cierre ✅ *tarea completa* |
| 16:45–17:15 | **1:1 — Reporte #2** |
| 17:15–18:00 | Buffer / revisión ligera de PRDs (adelanto) |

---

## MIÉRCOLES — Día de demo

| Hora | Bloque |
|---|---|
| 9:00–10:00 | **Emails stakeholders** (1h) |
| 10:00–12:00 | **Revisar PRDs pendientes** (2h) ✅ *tarea completa* |
| 12:00–13:00 | Almuerzo |
| 13:00–14:00 | **Ensayo de la demo en voz alta** (buffer, no tarea nueva) |
| 14:00–14:45 | Ajustes finales + prep de preguntas difíciles |
| 14:45–15:00 | Setup técnico (audio, pantalla, entorno de la demo) |
| 15:00–16:00 | 🔒 **Demo de producto** |
| 16:00–16:30 | Debrief: feedback, objeciones, follow-ups |
| 16:30–17:00 | **1:1 — Reporte #3** ✅ *tarea completa* |
| 17:00–18:00 | Envío de follow-ups post-demo |

---

## JUEVES — Día de hiring

| Hora | Bloque |
|---|---|
| 9:00–9:45 | Prep entrevistas: CVs, preguntas, rúbrica |
| 9:45–10:00 | Buffer |
| 10:00–13:00 | 🔒 Entrevistas de hiring |
| 13:00–14:00 | Almuerzo (necesario después de 3h de entrevistas) |
| 14:00–15:00 | **Emails stakeholders** (1h) |
| 15:00–16:00 | Scorecards y feedback de candidatos (mismo día = mejor calidad) |
| 16:00–17:00 | Overflow: lo que se atrasó de lunes–miércoles |
| 17:00–18:00 | Trabajo de producto ligero: grooming de backlog, respuestas a diseño/eng |

---

## VIERNES — Cierre, buffer y retro

| Hora | Bloque |
|---|---|
| 9:00–10:00 | **Emails stakeholders** (1h) ✅ *tarea completa* |
| 10:00–10:30 | 1:1 de reserva / seguimiento si alguno se canceló |
| 10:30–12:00 | **BUFFER PRINCIPAL**: cualquier tarea que se haya corrido |
| 12:00–13:00 | Almuerzo |
| 13:00–14:30 | Socializar OKRs Q3: compartir con directivos, recoger feedback |
| 14:30–15:30 | Planificación de la próxima semana + revisión de prioridades |
| 15:30–16:00 | Prep retro: datos, temas, tono |
| 16:00–17:00 | 🔒 Retrospectiva |
| 17:00–17:30 | Action items de la retro + cierre de semana |

---

## Verificación de carga

| Tarea | Horas | Cuándo | Estado |
|---|---|---|---|
| Prep demo | 3h | Lun 14:15 + Mar 15:15 | Lista 24h antes ✅ |
| Revisar PRDs | 2h | Mié 10:00 | ✅ |
| OKRs Q3 | 4h | Mar 10:00 + 13:00 | ✅ |
| Emails | 5h (1h/día) | Bloque fijo diario | ✅ |
| Métricas | 1h | Lun 16:00 | ✅ |
| 1:1s (3×30min) | 1.5h | Lun / Mar / Mié | ✅ |
| **Total tareas** | **16.5h** | | |
| Reuniones fijas | 8h | | |
| **Comprometido** | **24.5h de 45h** | | 45% libre para imprevistos |

---

## Reglas para que el plan sobreviva

1. **Martes es intocable.** Si alguien pide reunión, ofrece jueves 16:00–18:00. Es el único día donde 4h de OKRs son posibles.
2. **Regla de la demo:** si el miércoles a las 13:00 la presentación no está lista, el problema fue el lunes/martes. El bloque de ensayo no es para producir contenido.
3. **Si se cae algo**, el orden de sacrificio es: métricas → 1:1 (reagendar, no cancelar) → PRDs → emails a 30 min → **nunca OKRs ni demo**.
4. **1:1s temprano en la semana** para que tus reportes tengan la semana entera para actuar sobre lo que salga.

**Punto de fricción a vigilar:** lunes tiene reunión de directivos + almuerzo con cliente + 4h de trabajo. Es el día más denso. Si el lunes suele descarrilarse en tu experiencia, mueve las métricas al martes 9:00 y los emails del lunes a 30 min.

¿Quieres que ajuste horarios de jornada, o que reorganice asumiendo que tu energía cognitiva es mejor por la tarde?