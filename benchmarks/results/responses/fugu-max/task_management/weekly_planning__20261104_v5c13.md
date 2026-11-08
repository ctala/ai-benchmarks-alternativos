# Fugu Max — task_management/weekly_planning

- model_id: `sakana/fugu-max`
- success: True  | final: 8.25 | quality: 9.8
- latency_total: 18.161s | tokens_per_second: 227.3
- input_tokens: 324 | output_tokens: 4128
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y altamente util, con una buena estructura y consideración de las restricciones y tareas, aunque la profundidad podría mejorarse con más insights sobre la gestión del tiempo.

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

Asumo una jornada de **9:00 a 17:00** con comida de **13:00 a 14:00** (el lunes la comida es con cliente). Si tu jornada es más larga, usa el final del día como buffer.

## Plan semanal

### Lunes
| Hora | Bloque |
|---|---|
| 9:00–11:00 | Reunión de directivos |
| 11:00–12:00 | Responder emails de stakeholders |
| 12:00–13:00 | Revisar PRDs pendientes — bloque 1/2 |
| 13:00–14:00 | Almuerzo con cliente |
| 14:00–15:00 | Revisar PRDs pendientes — bloque 2/2 |
| 15:00–17:00 | Escribir OKRs Q3 — bloque 1/2 |

### Martes — día de foco
| Hora | Bloque |
|---|---|
| 9:00–10:00 | Responder emails de stakeholders |
| 10:00–13:00 | Preparar presentación para la demo — 3 h |
| 13:00–14:00 | Comida |
| 14:00–16:00 | Escribir OKRs Q3 — bloque 2/2 |
| 16:00–17:00 | Revisar métricas del producto |

### Miércoles
| Hora | Bloque |
|---|---|
| 9:00–10:00 | Responder emails de stakeholders |
| 10:00–10:30 | One-on-one reporte 1 |
| 10:30–11:00 | One-on-one reporte 2 |
| 11:00–11:30 | One-on-one reporte 3 |
| 11:30–12:30 | Buffer / preparación logística de la demo |
| 13:00–14:00 | Comida |
| 14:00–15:00 | Ensayo final y ajustes de la demo |
| 15:00–16:00 | Demo de producto |
| 16:00–17:00 | Notas y follow-ups de la demo |

### Jueves
| Hora | Bloque |
|---|---|
| 9:00–10:00 | Responder emails de stakeholders |
| 10:00–13:00 | Entrevistas de hiring |
| 13:00–14:00 | Comida |
| 14:00–15:00 | Documentar feedback de entrevistas |
| 15:00–17:00 | Buffer / cierre de pendientes / imprevistos |

### Viernes
| Hora | Bloque |
|---|---|
| 9:00–10:00 | Responder emails de stakeholders |
| 10:00–11:00 | Revisión semanal y preparación de la retrospectiva |
| 11:00–13:00 | Buffer / cierre de pendientes |
| 13:00–14:00 | Comida |
| 14:00–15:00 | Planificación de la próxima semana |
| 15:00–16:00 | Buffer |
| 16:00–17:00 | Retrospectiva |

## Cobertura de tareas

| Tarea | Horas | Dónde queda |
|---|---:|---|
| Preparar presentación demo | 3 h | Martes 10:00–13:00 |
| Revisar PRDs pendientes | 2 h | Lunes 12:00–13:00 y 14:00–15:00 |
| Escribir OKRs Q3 | 4 h | Lunes 15:00–17:00 + martes 14:00–16:00 |
| Emails de stakeholders | 1 h/día | Lunes 11:00–12:00; martes a viernes 9:00–10:00 |
| Revisar métricas | 1 h | Martes 16:00–17:00 |
| One-on-ones | 1.5 h | Miércoles 10:00–11:30 |

**Claves del plan:** la demo queda preparada antes del miércoles, los OKRs se reparten en dos bloques de foco y los huecos del jueves/viernes actúan como colchón para imprevistos o seguimientos.