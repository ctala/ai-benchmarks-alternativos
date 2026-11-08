# Seed 2.0 Code — structured_output/json_nested_complex

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 12.678s | tokens_per_second: 75.6
- input_tokens: 270 | output_tokens: 959

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
  "project": "Rediseño sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "María González", "role": "Diseñador UI/UX", "allocation_pct": 100},
    {"name": "Carlos Rodríguez", "role": "Desarrollador Frontend", "allocation_pct": 100},
    {"name": "Ana Martínez", "role": "Desarrolladora Backend", "allocation_pct": 100},
    {"name": "Roberto López", "role": "QA Tester", "allocation_pct": 100}
  ],
  "phases": [
    {
      "name": "Investigación y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {"title": "Análisis de requerimientos y benchmark", "assignee": "María González", "hours": 24, "depends_on": null},
        {"title": "Creación de wireframes y prototipos", "assignee": "María González", "hours": 40, "depends_on": "Análisis de requerimientos y benchmark"},
        {"title": "Validación de diseño con stakeholders", "assignee": "María González", "hours": 16, "depends_on": "Creación de wireframes y prototipos"}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-20",
      "tasks": [
        {"title": "Configuración de entorno y arquitectura", "assignee": "Carlos Rodríguez", "hours": 16, "depends_on": null},
        {"title": "Maquetación de páginas responsive", "assignee": "Carlos Rodríguez", "hours": 60, "depends_on": "Configuración de entorno y arquitectura"},
        {"title": "Desarrollo de APIs y endpoints", "assignee": "Ana Martínez", "hours": 48, "depends_on": "Configuración de entorno y arquitectura"},
        {"title": "Integración frontend-backend", "assignee": "Carlos Rodríguez, Ana Martínez", "hours": 32, "depends_on": "Maquetación de páginas responsive,Desarrollo de APIs y endpoints"},
        {"title": "Implementación de CMS y panel admin", "assignee": "Ana Martínez", "hours": 24, "depends_on": "Desarrollo de APIs y endpoints"}
      ]
    },
    {
      "name": "Pruebas y Lanzamiento",
      "start": "2026-06-21",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Pruebas funcionales y de usabilidad", "assignee": "Roberto López", "hours": 32, "depends_on": null},
        {"title": "Corrección de bugs y ajustes finales", "assignee": "Carlos Rodríguez, Ana Martínez", "hours": 24, "depends_on": "Pruebas funcionales y de usabilidad"},
        {"title": "Pruebas de rendimiento y seguridad", "assignee": "Roberto López", "hours": 16, "depends_on": "Corrección de bugs y ajustes finales"},
        {"title": "Deploy y lanzamiento", "assignee": "Ana Martínez", "hours": 8, "depends_on": "Pruebas de rendimiento y seguridad"}
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