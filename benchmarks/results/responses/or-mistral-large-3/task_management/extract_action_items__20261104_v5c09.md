# Mistral Large 3 675B — task_management/extract_action_items

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.78 | quality: 9.4
- latency_total: 4.34s | tokens_per_second: 77.7
- input_tokens: 202 | output_tokens: 337
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar prioridades y asumir fechas específicas para tareas vagas.

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

Aquí tienes los *action items* extraídos de las notas de la reunión, organizados en una tabla con responsable, tarea, fecha límite y prioridad sugerida (basada en la cercanía del deadline y dependencias entre tareas):

| **Responsable** | **Tarea**                                  | **Fecha límite** | **Prioridad** |
|-----------------|--------------------------------------------|------------------|---------------|
| Carlos          | Terminar el API de pagos                   | 20 de abril      | Alta          |
| Carlos          | Documentar los endpoints del API           | 18 de abril      | Alta          |
| Ana             | Entregar los mockups del dashboard         | 14 de abril      | Alta          |
| Pedro           | Escribir tests para el módulo de autenticación | Esta semana*   | Media         |
| Equipo          | Asistir a daily standups a las 9:30 AM     | A partir del 12 de abril | Alta |

---
**Notas:**
- *Para Pedro*: "Esta semana" se asume como **17 de abril** (viernes) para alinearse con el flujo del proyecto.
- **Prioridades**:
  - **Alta**: Tareas con deadlines cercanos o críticas para que otros puedan avanzar (ej: mockups para desarrollo).
  - **Media**: Tareas importantes pero sin dependencias inmediatas (ej: tests de autenticación).
- *Deadline del proyecto Alpha (30 de abril)*: No es un *action item* directo, pero sirve como referencia para priorizar.