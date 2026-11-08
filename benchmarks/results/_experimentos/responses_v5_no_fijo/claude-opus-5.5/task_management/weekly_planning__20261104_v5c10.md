# Claude Opus 5.5 — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.84 | quality: 9.52
- latency_total: 34.751s | tokens_per_second: 110.0
- input_tokens: 322 | output_tokens: 3823
- judge_score: 4.8 | justificación: 

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

# Plan semanal: Product Manager

**Supuestos:** jornada de 9:00 a 18:00, almuerzo de 13:00 a 14:00 (salvo el lunes, que ya lo tienes con el cliente). Los emails se dividen en dos bloques de 30 min para no dejar respuestas acumuladas todo el día.

**Lógica del plan:**
- La **preparación de la demo** se reparte entre lunes y miércoles para terminar antes de las 3 PM del miércoles, con un ensayo final justo antes.
- Las **métricas** se revisan el lunes porque alimentan la demo.
- Los **OKRs** (4 h) van el martes por la mañana, el único día sin interrupciones y con mejor energía para trabajo profundo.
- Las **one-on-ones** se distribuyen lunes, martes y miércoles, y quedan fuera del jueves, que es el día de entrevistas.

---

## 🟦 LUNES

| Horario | Actividad |
|---|---|
| 9:00 – 11:00 | 🔒 Reunión de directivos |
| 11:00 – 11:30 | 📧 Emails (bloque 1) |
| 11:30 – 12:30 | 📊 **Revisar métricas del producto** (con el contexto fresco de directivos) |
| 12:30 – 13:00 | Buffer / traslado al almuerzo |
| 13:00 – 14:00 | 🔒 Almuerzo con cliente |
| 14:00 – 15:00 | 🎤 **Demo – Parte 1 (1 h):** estructura, narrativa y mensajes clave, incorporando métricas y feedback del cliente |
| 15:00 – 15:30 | 👥 **One-on-one #1** |
| 15:30 – 16:00 | 📧 Emails (bloque 2) |
| 16:00 – 17:00 | 📄 **Revisar PRDs – Parte 1 (1 h)** |
| 17:00 – 18:00 | Buffer: follow-up del cliente, pendientes de directivos |

## 🟩 MARTES (día de trabajo profundo)

| Horario | Actividad |
|---|---|
| 9:00 – 9:30 | 📧 Emails (bloque 1) |
| 9:30 – 11:30 | 🎯 **OKRs Q3 – Parte 1 (2 h):** objetivos y alineación con la estrategia |
| 11:30 – 11:45 | Pausa |
| 11:45 – 13:45 | 🎯 **OKRs Q3 – Parte 2 (2 h):** key results, métricas y borrador final |
| 13:45 – 14:30 | Almuerzo |
| 14:30 – 16:00 | 🎤 **Demo – Parte 2 (1.5 h):** slides, flujo de la demo y datos de respaldo |
| 16:00 – 16:30 | 👥 **One-on-one #2** |
| 16:30 – 17:00 | 📧 Emails (bloque 2) |
| 17:00 – 18:00 | Buffer libre |

💡 Durante el bloque de OKRs, silencia Slack y las notificaciones y pon tu estado como "No molestar".

## 🟨 MIÉRCOLES (día de demo)

| Horario | Actividad |
|---|---|
| 9:00 – 9:30 | 📧 Emails (bloque 1) |
| 9:30 – 10:30 | 📄 **Revisar PRDs – Parte 2 (1 h)** ✅ |
| 10:30 – 11:00 | 👥 **One-on-one #3** ✅ |
| 11:00 – 13:00 | Bloque flexible (sugerencia: releer los OKRs con mente fresca) |
| 13:00 – 14:00 | Almuerzo |
| 14:00 – 14:30 | 🎤 **Demo – Parte 3 (30 min):** ensayo final ✅ |
| 14:30 – 15:00 | Setup técnico y verificación del entorno de la demo |
| 15:00 – 16:00 | 🔒 Demo de producto |
| 16:00 – 16:30 | Notas post-demo y feedback recibido |
| 16:30 – 17:00 | 📧 Emails (bloque 2) |
| 17:00 – 18:00 | Buffer libre |

## 🟧 JUEVES (día de hiring)

| Horario | Actividad |
|---|---|
| 9:00 – 9:30 | 📧 Emails (bloque 1) |
| 9:30 – 10:00 | Repasar CVs y preguntas de las entrevistas |
| 10:00 – 13:00 | 🔒 Entrevistas de hiring |
| 13:00 – 14:00 | Almuerzo |
| 14:00 – 14:30 | Completar scorecards mientras tienes las entrevistas frescas |
| 14:30 – 15:00 | 📧 Emails (bloque 2) |
| 15:00 – 18:00 | Bloque libre (ideal para seguir los acuerdos de la demo o compartir el borrador de OKRs) |

## 🟥 VIERNES

| Horario | Actividad |
|---|---|
| 9:00 – 9:30 | 📧 Emails (bloque 1) |
| 9:30 – 13:00 | Bloque libre / pendientes que surjan en la semana |
| 13:00 – 14:00 | Almuerzo |
| 14:00 – 15:00 | Preparar puntos para la retro |
| 15:00 – 15:30 | 📧 Emails (bloque 2) |
| 15:30 – 16:00 | Buffer |
| 16:00 – 17:00 | 🔒 Retrospectiva |
| 17:00 – 17:30 | Planificar la próxima semana |

---

## ✅ Verificación de tareas

| Tarea | Requerido | Asignado | Cuándo |
|---|---|---|---|
| Presentación demo | 3 h | 3 h | Lun 1 h + Mar 1.5 h + Mié 0.5 h |
| Revisar PRDs | 2 h | 2 h | Lun 1 h + Mié 1 h |
| OKRs Q3 | 4 h | 4 h | Martes por la mañana |
| Emails | 1 h/día | 5 h | 2 × 30 min diarios |
| Métricas | 1 h | 1 h | Lunes |
| One-on-ones | 3 × 30 min | 1.5 h | Lun, Mar, Mié |

Te quedan unas **9 horas libres** repartidas entre el miércoles por la mañana, el jueves por la tarde y el viernes por la mañana. Puedes usarlas para imprevistos sin descuadrar el plan.

¿Quieres que lo ajuste a otro horario o lo convierta en un formato para importar a Google Calendar u Outlook?