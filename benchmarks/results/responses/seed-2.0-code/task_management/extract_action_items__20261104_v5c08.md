# Seed 2.0 Code — task_management/extract_action_items

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.61 | quality: 7.8
- latency_total: 3.624s | tokens_per_second: 60.2
- input_tokens: 236 | output_tokens: 218
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena claridad y utilidad práctica, aunque la profundidad podría mejorarse con más contexto o insights.

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

| Responsable | Tarea | Fecha Límite | Prioridad Sugerida |
|-------------|-------|--------------|--------------------|
| Carlos | Terminar el API de pagos | 20 de abril 2026 | Alta |
| Ana | Entregar los mockups del dashboard | 14 de abril 2026 | Alta |
| Pedro | Escribir tests para el módulo de autenticación | 18 de abril 2026 (fin de semana) | Media-Alta |
| Carlos | Documentar los endpoints del API | 18 de abril 2026 (viernes) | Alta |
| Todo el equipo | Asistir a daily standups a las 9:30 AM | A partir del 12 de abril 2026 (mañana) | Media |
| Todo el equipo | Cumplir con el deadline general del Proyecto Alpha | 30 de abril 2026 | Máxima |