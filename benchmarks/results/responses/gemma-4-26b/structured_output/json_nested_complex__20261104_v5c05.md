# Gemma 4 26B MoE (3.8B activos) — structured_output/json_nested_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 28.492s | tokens_per_second: 29.2
- input_tokens: 250 | output_tokens: 831

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
      "name": "Roberto Sanz",
      "role": "QA Engineer",
      "allocation_pct": 50
    }
  ],
  "phases": [
    {
      "name": "Diseño y Prototipado",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {
          "title": "Wireframes de baja fidelidad",
          "assignee": "Laura García",
          "hours": 40,
          "depends_on": null
        },
        {
          "title": "Prototipo interactivo de alta fidelidad",
          "assignee": "Laura García",
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
          "title": "Configuración de entorno y arquitectura",
          "assignee": "Ana Martínez",
          "hours": 30,
          "depends_on": null
        },
        {
          "title": "Maquetación de componentes UI",
          "assignee": "Carlos Ruiz",
          "hours": 80,
          "depends_on": "Prototipo interactivo de alta fidelidad"
        },
        {
          "title": "Integración de API y Base de Datos",
          "assignee": "Ana Martínez",
          "hours": 100,
          "depends_on": "Configuración de entorno y arquitectura"
        }
      ]
    },
    {
      "name": "Testing y Despliegue",
      "start": "2026-06-21",
      "end": "2026-06-30",
      "tasks": [
        {
          "title": "Pruebas de regresión y QA",
          "assignee": "Roberto Sanz",
          "hours": 40,
          "depends_on": "Maquetación de componentes UI"
        },
        {
          "title": "Puesta en producción",
          "assignee": "Ana Martínez",
          "hours": 10,
          "depends_on": "Pruebas de regresión y QA"
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