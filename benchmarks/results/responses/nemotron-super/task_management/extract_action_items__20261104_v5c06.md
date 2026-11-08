# Nemotron 3 Super — task_management/extract_action_items

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.84 | quality: 8.2
- latency_total: 6.521s | tokens_per_second: 32.5
- input_tokens: 213 | output_tokens: 212
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y organizada, aunque la profundidad es solo aceptable sin insights adicionales.

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

Aquí tienes los action items extraídos de las notas de la reunión:

| Responsable | Tarea | Fecha Límite | Prioridad Sugerida |
| :--- | :--- | :--- | :--- |
| **Carlos** | Terminar el API de pagos | 20 de abril | Alta |
| **Ana** | Entregar mockups del dashboard | 14 de abril (lunes) | Alta |
| **Carlos** | Documentar los endpoints | 18 de abril (viernes) | Media |
| **Pedro** | Escribir tests para el módulo de autenticación | Fin de esta semana (20 de abril) | Media |
| **Todo el equipo** | Asistir a daily standups a las 9:30 AM | A partir de mañana (12 de abril) | Media |

**Notas adicionales:**
*   El deadline general del proyecto Alpha es el **30 de abril** (responsable general: Maria/PM).