# Qwen3-Coder-Next (OpenRouter FP8) — structured_output/json_nested_complex

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 21.706s | tokens_per_second: 58.8
- input_tokens: 227 | output_tokens: 1277

## Entrada exacta (lo que recibió el modelo)

**system:**

Responde SOLO con JSON valido. Sin markdown code blocks, sin explicaciones.

**user:**

Genera un JSON con la estructura de un plan de proyecto:

{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [{"name": "", "role": "", "allocation_pct": 0}],
  "phases": [
    {
      "name": "",
      "start": "",
      "end": "",
      "tasks": [{"title": "", "assignee": "", "hours": 0, "depends_on": null}]
    }
  ],
  "budget": {"total": 0, "breakdown": {"design": 0, "development": 0, "testing": 0}}
}

Llena con datos realistas. El equipo tiene 1 disenador, 2 developers, 1 QA. Presupuesto $25,000.


## Respuesta completa

{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Ana López", "role": "Diseñador UX/UI", "allocation_pct": 100},
    {"name": "Carlos Ruiz", "role": "Desarrollador Frontend", "allocation_pct": 100},
    {"name": "María González", "role": "Desarrollador Backend", "allocation_pct": 100},
    {"name": "Jorge Pérez", "role": "QA Engineer", "allocation_pct": 100}
  ],
  "phases": [
    {
      "name": "Análisis y Requerimientos",
      "start": "2026-05-01",
      "end": "2026-05-07",
      "tasks": [
        {"title": "Reunión de inicio y recopilación de requerimientos", "assignee": "Ana López", "hours": 8, "depends_on": null},
        {"title": "Análisis de competencia y benchmark", "assignee": "Ana López", "hours": 12, "depends_on": "Reunión de inicio y recopilación de requerimientos"},
        {"title": "Documentación de especificaciones funcionales", "assignee": "Carlos Ruiz", "hours": 10, "depends_on": "Análisis de competencia y benchmark"}
      ]
    },
    {
      "name": "Diseño",
      "start": "2026-05-08",
      "end": "2026-05-19",
      "tasks": [
        {"title": "Bocetos y wireframes de baja fidelidad", "assignee": "Ana López", "hours": 16, "depends_on": "Documentación de especificaciones funcionales"},
        {"title": "Diseño de alta fidelidad (mockups)", "assignee": "Ana López", "hours": 24, "depends_on": "Bocetos y wireframes de baja fidelidad"},
        {"title": "Prototipo interactivo funcional", "assignee": "Ana López", "hours": 20, "depends_on": "Diseño de alta fidelidad (mockups)"}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-20",
      "end": "2026-06-10",
      "tasks": [
        {"title": "Configuración de entorno y setup técnico", "assignee": "Carlos Ruiz", "hours": 6, "depends_on": null},
        {"title": "Implementación del frontend (HTML/CSS/JS)", "assignee": "Carlos Ruiz", "hours": 48, "depends_on": "Prototipo interactivo funcional"},
        {"title": "Implementación del backend (API REST)", "assignee": "María González", "hours": 56, "depends_on": "Prototipo interactivo funcional"},
        {"title": "Integración frontend-backend", "assignee": "Carlos Ruiz", "hours": 20, "depends_on": ["Implementación del frontend (HTML/CSS/JS)", "Implementación del backend (API REST)"]}
      ]
    },
    {
      "name": "Pruebas",
      "start": "2026-06-11",
      "end": "2026-06-24",
      "tasks": [
        {"title": "Planificación de casos de prueba", "assignee": "Jorge Pérez", "hours": 8, "depends_on": null},
        {"title": "Pruebas funcionales y de integración", "assignee": "Jorge Pérez", "hours": 32, "depends_on": "Integración frontend-backend"},
        {"title": "Pruebas de usabilidad y UX", "assignee": "Ana López", "hours": 16, "depends_on": "Pruebas funcionales y de integración"},
        {"title": "Corrección de bugs y validación final", "assignee": "Carlos Ruiz", "hours": 24, "depends_on": "Pruebas de usabilidad y UX"}
      ]
    },
    {
      "name": "Lanzamiento y Cierre",
      "start": "2026-06-25",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Preparación de despliegue en producción", "assignee": "María González", "hours": 12, "depends_on": "Corrección de bugs y validación final"},
        {"title": "Lanzamiento y monitoreo inicial", "assignee": "Carlos Ruiz", "hours": 8, "depends_on": "Preparación de despliegue en producción"},
        {"title": "Documentación técnica y manuales", "assignee": "Jorge Pérez", "hours": 10, "depends_on": "Lanzamiento y monitoreo inicial"},
        {"title": "Revisión final y cierre del proyecto", "assignee": "Ana López", "hours": 6, "depends_on": "Documentación técnica y manuales"}
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 6000,
      "development": 13000,
      "testing": 6000
    }
  }
}