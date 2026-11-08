# Ling 3.0 Flash — task_management/extract_action_items

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.02 | quality: 8.56
- latency_total: 10.147s | tokens_per_second: 32.1
- input_tokens: 239 | output_tokens: 326
- judge_score: 4.4 | justificación: 

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

| Responsable | Tarea | Fecha Límite | Prioridad |
|-------------|-------|--------------|-----------|
| Carlos | Terminar el API de pagos | 20/04/2026 | Alta |
| Ana | Entregar los mockups del dashboard | 14/04/2026 | Alta |
| Carlos | Documentar los endpoints del API | 18/04/2026 | Media |
| Pedro | Escribir tests para el módulo de autenticación | Esta semana (≈17/04/2026) | Alta |
| Todo el equipo | Daily standups a las 9:30 AM | Inicio: 15/04/2026 (continuo) | Media |

**Notas:**
- La tarea de Ana tiene prioridad **Alta** por ser la fecha límite más cercana y bloquea el avance del equipo.
- Carlos tiene dos tareas asignadas: el API de pagos (alta prioridad, deadline más urgente) y documentación (prioridad media, pero depende del avance del API).
- Los tests de Pedro son de prioridad **Alta** ya que son necesarios para la validación del módulo de autenticación.
- El deadline general del proyecto Alpha (30/04/2026) es la fecha final del proyecto, no un action item individual.