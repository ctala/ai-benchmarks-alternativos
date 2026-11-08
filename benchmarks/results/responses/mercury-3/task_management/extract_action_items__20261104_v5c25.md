# Mercury 3 — task_management/extract_action_items

- model_id: `inception/mercury-3`
- success: True  | final: 8.45 | quality: 8.0
- latency_total: 0.648s | tokens_per_second: 353.4
- input_tokens: 213 | output_tokens: 229
- judge_score: 4.0 | justificación: 

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

Aquí tienes los action items extraídos de las notas de la reunión, formateados como tabla:

| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|---|---|---|---|
| Carlos | Terminar el API de pagos | 20 de abril | Alta |
| Ana | Entregar mockups del dashboard | 14 de abril (lunes) | Alta |
| Pedro | Escribir tests para el módulo de autenticación | Esta semana (antes del 18 de abril) | Media |
| Carlos | Documentar los endpoints | 18 de abril (viernes) | Media |
| Todo el equipo | Iniciar daily standups a las 9:30 AM | 12 de abril (mañana) | Alta |

**Notas adicionales:**
- El deadline del proyecto Alpha es el 30 de abril, por lo que las tareas con fecha límite anterior a esa fecha son críticas.
- Se sugiere priorizar las tareas de Carlos (API de pagos y documentación) ya que son dependencias para el avance del proyecto.