# MiniMax M3 — task_management/weekly_planning

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.88 | quality: 9.8
- latency_total: 7.622s | tokens_per_second: 155.2
- input_tokens: 354 | output_tokens: 1183
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una buena estructura y consideración de las restricciones y tareas, aunque la profundidad podría mejorarse con más insights sobre la gestión del tiempo.

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

## Plan semanal

**Supuestos**
- La jornada laboral es **9:00 AM–6:00 PM**, de lunes a viernes.
- Los correos se concentran en una hora diaria, sin reuniones encima.
- Las tareas se programan en bloques completos cuando es posible.
- Los tres 1:1 quedan separados para proteger el seguimiento individual.

| Día | Horario | Actividad |
|---|---:|---|
| **Lunes** | 9:00–11:00 | Reunión de directivos |
| | 11:00–12:00 | Responder emails de stakeholders |
| | 12:00–1:00 | **Preparar presentación para la demo — bloque 1 de 2 h** |
| | 1:00–2:00 | Almuerzo con cliente |
| | 2:00–4:00 | **Preparar presentación para la demo — bloque 2 de 2 h** |
| | 4:00–5:00 | Revisar métricas del producto |
| | 5:00–6:00 | Revisar PRDs pendientes — bloque 1 de 2 h |
| **Martes** | 9:00–10:00 | Responder emails de stakeholders |
| | 10:00–12:00 | **Escribir OKRs Q3 — bloque 1 de 2 h** |
| | 12:00–1:00 | Almuerzo |
| | 1:00–3:00 | **Escribir OKRs Q3 — bloque 2 de 2 h** |
| | 3:00–4:00 | Revisar PRDs pendientes — bloque 2 de 1 h |
| | 4:00–4:30 | 1:1 con reporte directo 1 |
| | 4:30–5:00 | 1:1 con reporte directo 2 |
| | 5:00–5:30 | 1:1 con reporte directo 3 |
| | 5:30–6:00 | Buffer: seguimiento de pendientes y preparación de la demo |
| **Miércoles** | 9:00–10:00 | Responder emails de stakeholders |
| | 10:00–12:00 | Continuar y finalizar **OKRs Q3 — 2 h** |
| | 12:00–1:00 | Almuerzo |
| | 1:00–2:00 | Preparación final y rehearsal de la demo |
| | 2:00–2:30 | Buffer / ajustes de la demo |
| | 2:30–3:00 | Repaso de notas para la demo |
| | 3:00–4:00 | **Demo de producto** |
| | 4:00–4:30 | Registrar feedback y próximos pasos |
| | 4:30–5:30 | Continuar **OKRs Q3 — 1 h** |
| | 5:30–6:00 | Revisión del día y plan de seguimiento |
| **Jueves** | 9:00–10:00 | Preparación final de la demo / ajustes menores |
| | 10:00–1:00 | Entrevistas de hiring |
| | 1:00–2:00 | Almuerzo |
| | 2:00–3:00 | **Escribir OKRs Q3 — bloque final de 1 h** |
| | 3:00–4:00 | Revisar métricas del producto |
| | 4:00–5:00 | Revisar PRDs pendientes — bloque final de 1 h |
| | 5:00–6:00 | Revisión de OKRs, PRDs y próximos pasos |
| **Viernes** | 9:00–10:00 | Responder emails de stakeholders |
| | 10:00–11:00 | Preparar la retrospectiva: tópicos y métricas |
| | 11:00–12:00 | Revisar pendientes del equipo y bloqueos |
| | 12:00–1:00 | Almuerzo |
| | 1:00–2:30 | Trabajo de seguimiento: OKRs, PRDs o demo, según prioridad |
| | 2:30–3:30 | Revisar y cerrar los OKRs Q3 |
| | 3:30–4:00 | Buffer / actualización de notas |
| | 4:00–5:00 | **Retrospectiva** |
| | 5:00–6:00 | Acciones de la retrospectiva y cierre de la semana |

### Distribución de la carga principal

- **Preparar presentación para la demo:** 4 h el lunes + 2 h el martes + 1 h el miércoles.
- **Revisar PRDs pendientes:** 3 h el lunes + 1 h el martes + 1 h el jueves.
- **Escribir OKRs Q3:** 4 h el martes + 3 h el miércoles + 1 h el jueves.
- **Responder emails:** 1 h diaria, de 9:00–10:00, excepto lunes, que se hace de 11:00–12:00.
- **Revisar métricas:** lunes 4:00–5:00 y jueves 3:00–4:00.
- **1:1 con reportes directos:** martes de 4:00–5:30, 30 minutos por persona.

**Nota:** Si la demo del miércoles requiere una preparación más intensa, conviene convertir el bloque de seguimiento del viernes en preparación adicional. También es recomendable dejar el buffer del martes y la revisión final del miércoles como margen para imprevistos.