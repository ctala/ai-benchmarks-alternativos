# Llama 4 Maverick — structured_output/json_nested_complex

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 6.516s | tokens_per_second: 78.4
- input_tokens: 215 | output_tokens: 511

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
    {"name": "Ana Gomez", "role": "Disenador", "allocation_pct": 80},
    {"name": "Juan Perez", "role": "Desarrollador", "allocation_pct": 100},
    {"name": "Luis Sanchez", "role": "Desarrollador", "allocation_pct": 90},
    {"name": "Maria Rodriguez", "role": "QA", "allocation_pct": 70}
  ],
  "phases": [
    {
      "name": "Diseno",
      "start": "2026-05-01",
      "end": "2026-05-14",
      "tasks": [
        {"title": "Creacion de wireframes", "assignee": "Ana Gomez", "hours": 40, "depends_on": null},
        {"title": "Revision de wireframes", "assignee": "Juan Perez", "hours": 8, "depends_on": "Creacion de wireframes"}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-15",
      "end": "2026-06-18",
      "tasks": [
        {"title": "Implementacion de diseno", "assignee": "Juan Perez", "hours": 80, "depends_on": "Revision de wireframes"},
        {"title": "Desarrollo de funcionalidades", "assignee": "Luis Sanchez", "hours": 120, "depends_on": "Implementacion de diseno"}
      ]
    },
    {
      "name": "Pruebas",
      "start": "2026-06-19",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Pruebas funcionales", "assignee": "Maria Rodriguez", "hours": 40, "depends_on": "Desarrollo de funcionalidades"},
        {"title": "Revision final", "assignee": "Ana Gomez", "hours": 8, "depends_on": "Pruebas funcionales"}
      ]
    }
  ],
  "budget": {"total": 25000, "breakdown": {"design": 5000, "development": 15000, "testing": 5000}}
}