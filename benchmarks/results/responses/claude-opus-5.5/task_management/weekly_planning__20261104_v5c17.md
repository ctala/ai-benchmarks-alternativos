# Claude Opus 5.5 — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.99 | quality: 9.72
- latency_total: 32.19s | tokens_per_second: 110.3
- input_tokens: 322 | output_tokens: 3550
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

**Supuestos:** jornada de 9:00 AM a 6:00 PM, con 1 hora de almuerzo. Si tu horario es distinto, ajusta los bloques manteniendo el orden de prioridades.

## Lógica del plan

- **La demo es lo más urgente:** la preparación termina el martes, con margen antes del miércoles a las 3 PM.
- **Las métricas van primero:** alimentan tanto la demo como los OKRs.
- **El martes es para trabajo profundo:** es tu único día libre, así que ahí van los OKRs.
- **Los OKRs se cierran después de la demo:** así incorporas el feedback recibido.
- **Los one-on-ones van al inicio de la semana:** para desbloquear a tu equipo temprano.

## 🗓️ Lunes: Contexto y arranque

| Hora | Actividad |
|------|-----------|
| 9:00 – 11:00 | 🔒 Reunión de directivos |
| 11:00 – 11:30 | Procesar notas y acciones de la reunión |
| 11:30 – 12:30 | 📧 Emails de stakeholders |
| 12:30 – 1:00 | Preparar el almuerzo con el cliente |
| 1:00 – 2:00 | 🔒 Almuerzo con cliente |
| 2:00 – 3:00 | 📊 **Revisar métricas del producto** (1h ✅) |
| 3:00 – 5:00 | 🎯 **Preparar demo, parte 1:** estructura y contenido (2h) |
| 5:00 – 5:30 | 👤 **One-on-one #1** |
| 5:30 – 6:00 | Buffer y cierre del día |

## 🗓️ Martes: Trabajo profundo

| Hora | Actividad |
|------|-----------|
| 9:00 – 11:00 | 🧠 **OKRs Q3, bloque 1:** objetivos y borrador de key results (2h) |
| 11:00 – 11:15 | Pausa |
| 11:15 – 12:15 | 🎯 **Preparar demo, parte 2:** pulir y hacer un ensayo (1h, total 3h ✅) |
| 12:15 – 1:15 | Almuerzo |
| 1:15 – 2:15 | 📧 Emails de stakeholders |
| 2:15 – 3:15 | 🧠 **OKRs Q3, bloque 2:** métricas y metas (1h, total 3h) |
| 3:15 – 4:30 | Buffer y trabajo flexible |
| 4:30 – 5:00 | 👤 **One-on-one #2** |
| 5:00 – 6:00 | Buffer |

> 💡 Bloquea el martes en tu calendario como "Focus time" para que nadie lo ocupe.

## 🗓️ Miércoles: Día de demo

| Hora | Actividad |
|------|-----------|
| 9:00 – 10:00 | 📧 Emails de stakeholders |
| 10:00 – 12:00 | 📄 **Revisar PRDs pendientes** (2h ✅) |
| 12:00 – 1:00 | Almuerzo |
| 1:00 – 1:30 | 👤 **One-on-one #3** (3/3 ✅) |
| 1:30 – 2:30 | Buffer |
| 2:30 – 3:00 | Repaso rápido y setup técnico de la demo |
| 3:00 – 4:00 | 🔒 **Demo de producto** |
| 4:00 – 4:30 | Documentar el feedback de la demo |
| 4:30 – 6:00 | Seguimiento de PRDs y comentarios a los autores |

## 🗓️ Jueves: Hiring y cierre de OKRs

| Hora | Actividad |
|------|-----------|
| 9:00 – 10:00 | Revisar CVs y preparar preguntas de entrevista |
| 10:00 – 1:00 | 🔒 Entrevistas de hiring |
| 1:00 – 2:00 | Almuerzo |
| 2:00 – 2:30 | Completar scorecards de candidatos (mientras está fresco) |
| 2:30 – 3:30 | 📧 Emails de stakeholders |
| 3:30 – 4:30 | 🧠 **OKRs Q3, bloque final:** incorporar el feedback de la demo (1h, total 4h ✅) |
| 4:30 – 6:00 | Buffer |

## 🗓️ Viernes: Cierre de semana

| Hora | Actividad |
|------|-----------|
| 9:00 – 10:00 | 📧 Emails de stakeholders |
| 10:00 – 12:00 | Bloque flexible para pendientes de la semana |
| 12:00 – 1:00 | Almuerzo |
| 1:00 – 2:00 | Compartir el borrador de OKRs con tu manager o equipo |
| 2:00 – 3:30 | Buffer |
| 3:30 – 4:00 | Preparar puntos para la retrospectiva |
| 4:00 – 5:00 | 🔒 Retrospectiva |
| 5:00 – 5:30 | Planificar la próxima semana |

## ✅ Resumen de cobertura

| Tarea | Requerido | Asignado | Cuándo |
|-------|-----------|----------|--------|
| Preparar demo | 3h | 3h | Lun + Mar |
| Revisar PRDs | 2h | 2h | Mié |
| OKRs Q3 | 4h | 4h | Mar (3h) + Jue (1h) |
| Emails | 1h/día | 5h | Todos los días |
| Métricas | 1h | 1h | Lun |
| One-on-ones | 3 × 30 min | 1.5h | Lun, Mar, Mié |

**Buffer total disponible: unas 9 horas** para imprevistos, Slack o tareas que se extiendan.

## 💡 Recomendaciones

1. **Protege el martes:** es tu día más valioso. Si alguien pide reunión, ofrécele el jueves o viernes por la tarde.
2. **Si la demo se complica,** usa el buffer del miércoles de 1:30 a 2:30.
3. **Los emails tienen hora fija:** revísalos solo en sus bloques y no estés pendiente todo el día.
4. **Los one-on-ones pueden reordenarse,** pero mantenlos antes del jueves para resolver bloqueos de tu equipo a tiempo.

¿Quieres que ajuste el plan a otro horario o que agregue más tiempo de ensayo para la demo?