# Tencent Hy4 preview — task_management/extract_action_items

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.52 | quality: 9.6
- latency_total: 7.48s | tokens_per_second: 42.9
- input_tokens: 232 | output_tokens: 321
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al sugerir prioridades basadas en la urgencia y las dependencias.

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

Aquí tienes los action items extraídos de las notas de la reunión, organizados en una tabla. 

Para la **prioridad sugerida**, he evaluado la urgencia de las fechas y las dependencias entre tareas (por ejemplo, los mockups de Ana son urgentes para que el equipo pueda avanzar esta misma semana).

| Responsable | Tarea | Fecha Límite | Prioridad Sugerida |
| :--- | :--- | :--- | :--- |
| **Carlos** | Terminar el API de pagos | 20 de abril | Alta |
| **Carlos** | Documentar los endpoints de la API | 18 de abril (viernes) | Alta |
| **Ana** | Entregar los mockups del dashboard | 14 de abril (lunes) | Alta |
| **Pedro** | Escribir tests para el módulo de autenticación | Esta semana (hasta el 17/18 de abril) | Media |
| **Todos** | Asistir y participar en los daily standups | 12 de abril (empieza mañana a las 9:30 AM) | Media |

*Nota: Aunque la fecha "30 de abril" (Deadline del proyecto Alpha) mencionada por María es crucial, se ha dejado fuera de la tabla ya que funciona como un hito general del proyecto y no como un action item individual.*