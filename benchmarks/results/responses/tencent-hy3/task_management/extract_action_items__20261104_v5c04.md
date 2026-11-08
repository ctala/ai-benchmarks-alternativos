# Tencent Hy3 — task_management/extract_action_items

- model_id: `tencent/hy3`
- success: True  | final: 8.82 | quality: 9.6
- latency_total: 5.673s | tokens_per_second: 44.8
- input_tokens: 231 | output_tokens: 254
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una buena estructura y sugerencias de prioridad.

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

| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|-------------|-------|--------------|--------------------|
| Carlos (Dev) | Terminar el API de pagos | 20 de abril de 2026 | Alta |
| Ana (Diseño) | Entregar los mockups del dashboard | 14 de abril de 2026 (lunes) | Alta |
| Pedro (QA) | Escribir tests para el módulo de autenticación | Esta semana (antes del 17 de abril) | Alta |
| Carlos (Dev) | Documentar los endpoints del API | 18 de abril de 2026 (viernes) | Media |
| Todos (Equipo) | Asistir a daily standups a las 9:30 AM | Desde el 12 de abril de 2026 (diario) | Media |

**Notas:**
- El *deadline* general del proyecto Alpha es el 30 de abril (comunicado por Maria, no es un action item individual).
- La prioridad se sugiere según cercanía de la fecha y dependencias del proyecto.