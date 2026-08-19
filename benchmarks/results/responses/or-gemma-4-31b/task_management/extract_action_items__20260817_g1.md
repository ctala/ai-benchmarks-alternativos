# Gemma 4 31B — task_management/extract_action_items

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.82 | quality: 9.6
- latency_total: 5.556s | tokens_per_second: 32.8
- input_tokens: 210 | output_tokens: 182
- judge_score: 5 | justificación: La respuesta es precisa y relevante, extrae correctamente los action items de las notas de la reunión, y los organiza de manera clara y útil, añadiendo valor con la priorización y la estructura.

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

Aquí tienes los action items extraídos de la reunión:

### 📋 Lista de Tareas y Compromisos

| Responsable | Tarea | Fecha Límite | Prioridad Sugerida |
| :--- | :--- | :--- | :--- |
| **Ana** | Entrega de mockups del dashboard | 14 de abril | Alta |
| **Pedro** | Escribir tests para el módulo de autenticación | 15 de abril* | Alta |
| **Carlos** | Documentar los endpoints | 18 de abril | Media |
| **Carlos** | Finalizar API de pagos | 20 de abril | Crítica |
| **Equipo** | Iniciar daily standups (9:30 AM) | 12 de abril | Media |

*\*Fecha estimada basada en "esta semana".*