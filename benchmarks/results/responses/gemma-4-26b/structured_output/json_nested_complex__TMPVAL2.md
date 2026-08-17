# Gemma 4 26B MoE (3.8B activos) — structured_output/json_nested_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 34.544s | tokens_per_second: 22.1
- input_tokens: 250 | output_tokens: 765

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
      "name": "Laura García",
      "role": "Diseñador UI/UX",
      "allocation_pct": 100
    },
    {
      "name": "Carlos Ruiz",
      "role": "Developer Frontend",
      "allocation_pct": 100
    },
    {
      "name": "Ana Martínez",
      "role": "Developer Backend",
      "allocation_pct": 100
    },
    {
      "name": "David López",
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
          "title": "Wireframes y Prototipado",
          "assignee": "Laura García",
          "hours": 80,
          "depends_on": null
        },
        {
          "title": "Definición de Arquitectura",
          "assignee": "Ana Martínez",
          "hours": 20,
          "depends_on": null
        }
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-20",
      "tasks": [
        {
          "title": "Maquetación Frontend",
          "assignee": "Carlos Ruiz",
          "hours": 120,
          "depends_on": "Wireframes y Prototipado"
        },
        {
          "title": "Implementación de API",
          "assignee": "Ana Martínez",
          "hours": 100,
          "depends_on": "Definición de Arquitectura"
        }
      ]
    },
    {
      "name": "Testing y Lanzamiento",
      "start": "2026-06-21",
      "end": "2026-06-30",
      "tasks": [
        {
          "title": "Pruebas de Regresión y QA",
          "assignee": "David López",
          "hours": 40,
          "depends_on": "Maquetación Frontend"
        },
        {
          "title": "Despliegue en Producción",
          "assignee": "Carlos Ruiz",
          "hours": 10,
          "depends_on": "Pruebas de Regresión y QA"
        }
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 7000,
      "development": 15000,
      "testing": 3000
    }
  }
}