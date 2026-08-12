# Gemma 4 26B MoE (3.8B activos) — structured_output/json_nested_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 6.289s | tokens_per_second: 131.2
- input_tokens: 249 | output_tokens: 825

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
    {
      "name": "Elena García",
      "role": "Diseñador UI/UX",
      "allocation_pct": 100
    },
    {
      "name": "Carlos Ruiz",
      "role": "Frontend Developer",
      "allocation_pct": 100
    },
    {
      "name": "Ana Martínez",
      "role": "Backend Developer",
      "allocation_pct": 100
    },
    {
      "name": "Luis Torres",
      "role": "QA Engineer",
      "allocation_pct": 50
    }
  ],
  "phases": [
    {
      "name": "Planificación y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {
          "title": "Wireframes de baja fidelidad",
          "assignee": "Elena García",
          "hours": 40,
          "depends_on": null
        },
        {
          "title": "Prototipo de alta fidelidad",
          "assignee": "Elena García",
          "hours": 60,
          "depends_on": "Wireframes de baja fidelidad"
        }
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-20",
      "tasks": [
        {
          "title": "Configuración de arquitectura y API",
          "assignee": "Ana Martínez",
          "hours": 80,
          "depends_on": "Prototipo de alta fidelidad"
        },
        {
          "title": "Maquetación de interfaces",
          "assignee": "Carlos Ruiz",
          "hours": 120,
          "depends_on": "Prototipo de alta fidelidad"
        },
        {
          "title": "Integración de servicios",
          "assignee": "Ana Martínez",
          "hours": 60,
          "depends_on": "Configuración de arquitectura y API"
        }
      ]
    },
    {
      "name": "Testing y Lanzamiento",
      "start": "2026-06-21",
      "end": "2026-06-30",
      "tasks": [
        {
          "title": "Pruebas de regresión y QA",
          "assignee": "Luis Torres",
          "hours": 40,
          "depends_on": "Integración de servicios"
        },
        {
          "title": "Despliegue a producción",
          "assignee": "Carlos Ruiz",
          "hours": 10,
          "depends_on": "Pruebas de regresión y QA"
        }
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