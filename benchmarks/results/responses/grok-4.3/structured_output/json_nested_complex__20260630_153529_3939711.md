# Grok 4.3 — structured_output/json_nested_complex

- model_id: `x-ai/grok-4.3`
- success: True  | final: 6.24 | quality: 6.2
- latency_total: 8.113s | tokens_per_second: 113.3
- input_tokens: 334 | output_tokens: 919

## Respuesta completa

{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Alex Rivera", "role": "Designer", "allocation_pct": 100},
    {"name": "Jordan Lee", "role": "Developer", "allocation_pct": 100},
    {"name": "Sam Patel", "role": "Developer", "allocation_pct": 100},
    {"name": "Taylor Kim", "role": "QA", "allocation_pct": 80}
  ],
  "phases": [
    {
      "name": "Discovery y Diseno",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {"title": "Investigacion usuarios", "assignee": "Alex Rivera", "hours": 40, "depends_on": null},
        {"title": "Wireframes y mockups", "assignee": "Alex Rivera", "hours": 60, "depends_on": null}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-15",
      "tasks": [
        {"title": "Frontend responsive", "assignee": "Jordan Lee", "hours": 80, "depends_on": "Wireframes y mockups"},
        {"title": "Backend integracion", "assignee": "Sam Patel", "hours": 70, "depends_on": "Wireframes y mockups"}
      ]
    },
    {
      "name": "Pruebas y Lanzamiento",
      "start": "2026-06-16",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Testing QA", "assignee": "Taylor Kim", "hours": 50, "depends_on": "Frontend responsive"},
        {"title": "Deploy produccion", "assignee": "Jordan Lee", "hours": 20, "depends_on": "Testing QA"}
      ]
    }
  ],
  "budget": {"total": 25000, "breakdown": {"design": 5000, "development": 15000, "testing": 5000}}
}