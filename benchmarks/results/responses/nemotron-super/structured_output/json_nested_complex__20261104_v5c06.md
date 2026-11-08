# Nemotron 3 Super — structured_output/json_nested_complex

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 3.9 | quality: 2.0
- latency_total: 2.31s | tokens_per_second: 286.6
- input_tokens: 241 | output_tokens: 662

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

{"project": "Rediseño sitio web", "start_date": "2026-05-01", "end_date": "2026-06-30", "team": [{"name": "Ana García", "role": "Diseñador UX/UI", "allocation_pct": 80}, {"name": "Carlos Ruiz", "role": "Desarrollador Frontend", "allocation_pct": 100}, {"name": "Lucía Méndez", "role": "Desarrollador Backend", "allocation_pct": 60}, {"name": "Pedro Sánchez", "role": "QA Engineer", "allocation_pct": 50}], "phases": [{"name": "Investigación y Diseño", "start": "2026-05-01", "end": "2026-05-15", "tasks": [{"title": "Análisis de requerimientos", "assignee": "Ana García", "hours": 20, "depends_on": null}, {"title": "Wireframes y prototipos", "assignee": "Ana García", "hours": 40, "depends_on": "Análisis de requerimientos"}, {"title": "Diseño visual final", "assignee": "Ana García", "hours": 30, "depends_on": "Wireframes y prototipos"}]}, {"name": "Desarrollo", "start": "2026-05-16", "end": "2026-06-15", "tasks": [{"title": "Desarrollo Frontend", "assignee": "Carlos Ruiz", "hours": 100, "depends_on": "Diseño visual final"}, {"title": "Desarrollo Backend y API", "assignee": "Lucía Méndez", "hours": 80, "depends_on": "Diseño visual final"}]}, {"name": "Pruebas y Lanzamiento", "start": "2026-06-16", "end": "2026-06-30", "tasks": [{"title": "Pruebas funcionales y QA", "assignee": "Pedro Sánchez", "hours": 40, "depends_on": "Desarrollo Frontend"}, {"title": "Corrección de bugs", "assignee": "Carlos Ruiz", "hours": 20, "depends_on": "Pruebas funcionales y QA"}, {"title": "Despliegue a producción", "assignee": "Lucía Méndez", "hours": 10, "depends_on": "Corrección de bugs"}]}, "budget": {"total": 25000, "breakdown": {"design": 7000, "development": 14000, "testing": 4000}}}