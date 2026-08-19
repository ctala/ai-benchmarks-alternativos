# Gemma 4 26B MoE (3.8B activos) — structured_output/json_nested_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 35.698s | tokens_per_second: 21.9
- input_tokens: 250 | output_tokens: 781

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
      "name": "Roberto Gómez",
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
          "title": "Implementación de maquetas Frontend",
          "assignee": "Carlos Ruiz",
          "hours": 120,
          "depends_on": "Prototipo interactivo de alta fidelidad"
        },
        {
          "title": "Configuración de API y Base de Datos",
          "assignee": "Ana Martínez",
          "hours": 100,
          "depends_on": null
        }
      ]
    },
    {
      "name": "Pruebas y Lanzamiento",
      "start": "2026-06-21",
      "end": "2026-06-30",
      "tasks": [
        {
          "title": "Pruebas de regresión y QA",
          "assignee": "Roberto Gómez",
          "hours": 40,
          "depends_on": "Implementación de maquetas Frontend"
        },
        {
          "title": "Despliegue en producción",
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