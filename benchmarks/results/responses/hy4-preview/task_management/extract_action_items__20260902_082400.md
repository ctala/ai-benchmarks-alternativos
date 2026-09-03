# Tencent Hy4 preview — task_management/extract_action_items

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 162.055s | tokens_per_second: 56.4
- input_tokens: 229 | output_tokens: 9141
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente que organiza notas de reunion.

**user:**

Aqui estan las notas de la reunion de hoy:

Reunion de equipo - 11 abril 2026
Asistentes: Maria (PM), Carlos (Dev), Ana (Diseno), Pedro (QA)

- Maria comento que el deadline del proyecto Alpha es el 30 de abril
- Carlos necesita terminar el API de pagos antes del 20 de abril
- Ana va a entregar los mockups del dashboard el lunes 14
- Pedro dijo que faltan escribir tests para el modulo de autenticacion, lo hara esta semana
- Maria pidio a Carlos que documente los endpoints antes del viernes 18
- Se acordo hacer daily standups a las 9:30 AM empezando manana

Extrae todos los action items con: responsable, tarea, fecha limite, y prioridad sugerida. Formatea como tabla.


## Respuesta completa

Aquí tienes los **action items** extraídos de las notas, organizados en una tabla:

| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|---|---|---|---|
| **Equipo / María (PM)** | Cumplir con el deadline general del proyecto Alpha (entrega final) | 30 de abril | Alta |
| **Carlos (Dev)** | Terminar el API de pagos | Antes del 20 de abril *(19/04 si se interpreta literalmente “antes del”)* | Alta |
| **Ana (Diseño)** | Entregar los mockups del dashboard | Lunes 14 de abril | Alta |
| **Pedro (QA)** | Escribir los tests del módulo de autenticación | Esta semana *(semana del 11 de abril; fecha exacta por confirmar)* | Alta |
| **Carlos (Dev)** | Documentar los endpoints (solicitado por María) | Antes del viernes 18 de abril *(17/04 si se interpreta literalmente “antes del”)* | Media |
| **Equipo (todos)** | Realizar daily standups a las 9:30 AM | A partir de mañana, 12 de abril *(recurrente, diario)* | Media |

### Notas sobre las fechas y prioridades
- **“Antes del X”**: se conserva la fecha mencionada en las notas. Si en tu equipo se interpreta de forma estricta, la entrega sería el día anterior (ej. antes del 20 = 19 de abril; antes del viernes 18 = 17 de abril).
- **“Esta semana” (Pedro)**: se refiere a la semana de la reunión (11 de abril). Se recomienda confirmar el último día hábil o si vence el fin de semana.
- **Prioridades**: se marcaron como **Alta** las tareas con fechas más cercanas, entregables críticos o deuda urgente de QA; **Media** para la documentación de endpoints y el acuerdo de daily standups (proceso recurrente).