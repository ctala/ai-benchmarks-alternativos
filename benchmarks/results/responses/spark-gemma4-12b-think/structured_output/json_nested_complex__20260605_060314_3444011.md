# Gemma 4 12B (Spark llama-server, reasoning) — structured_output/json_nested_complex

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.71 | quality: 8.86
- latency_total: 59.136s | tokens_per_second: 25.8
- input_tokens: 247 | output_tokens: 1527
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura JSON válida que proporciona detalles útiles para un emprendedor.

## Respuesta completa

{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {
      "name": "Ana García",
      "role": "Diseñadora UX/UI",
      "allocation_pct": 100
    },
    {
      "name": "Carlos Ruiz",
      "role": "Developer Frontend",
      "allocation_pct": 100
    },
    {
      "name": "Laura Méndez",
      "role": "Developer Backend",
      "allocation_pct": 100
    },
    {
      "name": "Pedro Soler",
      "role": "QA Engineer",
      "allocation_pct": 100
    }
  ],
  "phases": [
    {
      "name": "Investigación y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-20",
      "tasks": [
        {
          "title": "Wireframes de baja fidelidad",
          "assignee": "Ana García",
          "hours": 40,
          "depends_on": null
        },
        {
          "title": "Diseño de interfaz de alta fidelidad",
          "assignee": "Ana García",
          "hours": 80,
          "depends_on": "Wireframes de baja fidelidad"
        }
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-21",
      "end": "2026-06-15",
      "tasks": [
        {
          "title": "Configuración de Base de Datos y API",
          "assignee": "Laura Méndez",
          "hours": 100,
          "depends_on": null
        },
        {
          "title": "Desarrollo de componentes Frontend",
          "assignee": "Carlos Ruiz",
          "hours": 120,
          "depends_on": "Configuración de Base de Datos y API"
        },
        {
          "title": "Integración de servicios",
          "assignee": "Laura Méndez",
          "hours": 60,
          "depends_on": "Desarrollo de componentes Frontend"
        }
      ]
    },
    {
      "name": "QA y Lanzamiento",
      "start": "2026-06-16",
      "end": "2026-06-30",
      "tasks": [
        {
          "title": "Pruebas de regresión y errores",
          "assignee": "Pedro Soler",
          "hours": 40,
          "depends_on": "Integración de servicios"
        },
        {
          "title": "Corrección de bugs críticos",
          "assignee": "Carlos Ruiz",
          "hours": 30,
          "depends_on": "Pruebas de regresión y errores"
        },
        {
          "title": "Despliegue a producción",
          "assignee": "Laura Méndez",
          "hours": 10,
          "depends_on": "Corrección de bugs críticos"
        }
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 8000,
      "development": 14000,
      "testing": 3000
    }
  }
}