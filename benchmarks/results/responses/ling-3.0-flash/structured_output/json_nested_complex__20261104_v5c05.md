# Ling 3.0 Flash — structured_output/json_nested_complex

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 19.056s | tokens_per_second: 56.7
- input_tokens: 269 | output_tokens: 1080

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
  "project": "Rediseño sitio web corporativo",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Laura Méndez", "role": "Diseñador UX/UI", "allocation_pct": 100},
    {"name": "Carlos Ruiz", "role": "Desarrollador Frontend", "allocation_pct": 100},
    {"name": "Ana Jiménez", "role": "Desarrollador Backend", "allocation_pct": 100},
    {"name": "Pedro Vargas", "role": "QA Engineer", "allocation_pct": 80}
  ],
  "phases": [
    {
      "name": "Análisis y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {"title": "Reuniones de levantamiento de requerimientos", "assignee": "Laura Méndez", "hours": 16, "depends_on": null},
        {"title": "Creación de wireframes de alta fidelidad", "assignee": "Laura Méndez", "hours": 24, "depends_on": null},
        {"title": "Diseño de sistema de bases de datos", "assignee": "Ana Jiménez", "hours": 12, "depends_on": null},
        {"title": "Revisión y aprobación de diseño", "assignee": "Laura Méndez", "hours": 8, "depends_on": "Creación de wireframes de alta fidelidad"}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-15",
      "tasks": [
        {"title": "Configuración de entorno y repositorios", "assignee": "Carlos Ruiz", "hours": 8, "depends_on": null},
        {"title": "Desarrollo de frontend (React)", "assignee": "Carlos Ruiz", "hours": 60, "depends_on": "Configuración de entorno y repositorios"},
        {"title": "Desarrollo de backend (API REST)", "assignee": "Ana Jiménez", "hours": 60, "depends_on": "Diseño de sistema de bases de datos"},
        {"title": "Integración frontend-backend", "assignee": "Carlos Ruiz", "hours": 16, "depends_on": "Desarrollo de frontend (React)"},
        {"title": "Integración frontend-backend", "assignee": "Ana Jiménez", "hours": 16, "depends_on": "Desarrollo de backend (API REST)"}
      ]
    },
    {
      "name": "Pruebas y Lanzamiento",
      "start": "2026-06-16",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Pruebas funcionales", "assignee": "Pedro Vargas", "hours": 24, "depends_on": "Integración frontend-backend"},
        {"title": "Pruebas de rendimiento y seguridad", "assignee": "Pedro Vargas", "hours": 16, "depends_on": "Pruebas funcionales"},
        {"title": "Corrección de bugs", "assignee": "Carlos Ruiz", "hours": 16, "depends_on": "Pruebas funcionales"},
        {"title": "Corrección de bugs", "assignee": "Ana Jiménez", "hours": 16, "depends_on": "Pruebas funcionales"},
        {"title": "Despliegue a producción", "assignee": "Carlos Ruiz", "hours": 8, "depends_on": "Corrección de bugs"},
        {"title": "Documentación final y entrega", "assignee": "Laura Méndez", "hours": 8, "depends_on": "Despliegue a producción"}
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 7500,
      "development": 12500,
      "testing": 5000
    }
  }
}