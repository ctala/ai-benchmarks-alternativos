# Tencent Hy4 preview — structured_output/json_nested_complex

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 10.14s | tokens_per_second: 79.6
- input_tokens: 238 | output_tokens: 807

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
    {"name": "Ana Martínez", "role": "Diseñadora UX/UI", "allocation_pct": 100},
    {"name": "Carlos Ruiz", "role": "Desarrollador Frontend", "allocation_pct": 100},
    {"name": "Laura Gómez", "role": "Desarrolladora Backend", "allocation_pct": 100},
    {"name": "Diego Torres", "role": "QA Engineer", "allocation_pct": 50}
  ],
  "phases": [
    {
      "name": "Descubrimiento y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {"title": "Investigación de usuarios y benchmarks", "assignee": "Ana Martínez", "hours": 40, "depends_on": null},
        {"title": "Wireframes de baja fidelidad", "assignee": "Ana Martínez", "hours": 30, "depends_on": "Investigación de usuarios y benchmarks"},
        {"title": "Prototipo interactivo y diseño visual", "assignee": "Ana Martínez", "hours": 50, "depends_on": "Wireframes de baja fidelidad"}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-15",
      "tasks": [
        {"title": "Maquetación frontend (HTML/CSS/JS)", "assignee": "Carlos Ruiz", "hours": 120, "depends_on": "Prototipo interactivo y diseño visual"},
        {"title": "Integración con CMS y backend", "assignee": "Laura Gómez", "hours": 100, "depends_on": "Prototipo interactivo y diseño visual"},
        {"title": "Implementación de formularios y APIs", "assignee": "Laura Gómez", "hours": 60, "depends_on": "Integración con CMS y backend"}
      ]
    },
    {
      "name": "Pruebas y Lanzamiento",
      "start": "2026-06-16",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Pruebas funcionales y de regresión", "assignee": "Diego Torres", "hours": 40, "depends_on": "Maquetación frontend (HTML/CSS/JS)"},
        {"title": "Pruebas de rendimiento y responsive", "assignee": "Diego Torres", "hours": 24, "depends_on": "Pruebas funcionales y de regresión"},
        {"title": "Corrección de bugs y ajustes finales", "assignee": "Carlos Ruiz", "hours": 30, "depends_on": "Pruebas de rendimiento y responsive"},
        {"title": "Despliegue a producción", "assignee": "Laura Gómez", "hours": 16, "depends_on": "Corrección de bugs y ajustes finales"}
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 6000,
      "development": 15000,
      "testing": 4000
    }
  }
}