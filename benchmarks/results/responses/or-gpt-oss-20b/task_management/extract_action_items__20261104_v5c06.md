# GPT-OSS 20B — task_management/extract_action_items

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.59 | quality: 7.63
- latency_total: 8.097s | tokens_per_second: 92.5
- input_tokens: 243 | output_tokens: 749
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

| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|-------------|-------|--------------|-------------------|
| Carlos | Terminar el API de pagos | 20 de abril | Alta |
| Ana | Entregar los mockups del dashboard | 14 de abril | Media |
| Pedro | Escribir tests para el módulo de autenticación | 18 de abril | Alta |
| Carlos | Documentar los endpoints | 18 de abril | Media |