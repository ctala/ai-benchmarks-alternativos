# GPT-OSS 20B — structured_output/json_nested_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 9.946s | tokens_per_second: 133.6
- input_tokens: 274 | output_tokens: 1329

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

{"project":"Rediseño sitio web","start_date":"2026-05-01","end_date":"2026-06-30","team":[{"name":"Ana Pérez","role":"Designer","allocation_pct":100},{"name":"Carlos García","role":"Developer","allocation_pct":100},{"name":"María López","role":"Developer","allocation_pct":100},{"name":"Luis Martínez","role":"QA Engineer","allocation_pct":100}],"phases":[{"name":"Analysis","start":"2026-05-01","end":"2026-05-07","tasks":[{"title":"Stakeholder interviews","assignee":"Ana Pérez","hours":20,"depends_on":null},{"title":"Documentation","assignee":"Carlos García","hours":20,"depends_on":"Stakeholder interviews"}]},{"name":"Design","start":"2026-05-08","end":"2026-05-21","tasks":[{"title":"Wireframing","assignee":"Ana Pérez","hours":20,"depends_on":null},{"title":"UI Design","assignee":"Ana Pérez","hours":40,"depends_on":"Wireframing"},{"title":"Design Review","assignee":"Luis Martínez","hours":20,"depends_on":"UI Design"}]},{"name":"Development","start":"2026-05-22","end":"2026-06-13","tasks":[{"title":"Frontend Implementation","assignee":"Carlos García","hours":70,"depends_on":null},{"title":"Backend Implementation","assignee":"María López","hours":70,"depends_on":"Frontend Implementation"},{"title":"API Integration","assignee":"Carlos García","hours":30,"depends_on":"Backend Implementation"},{"title":"Code Review","assignee":"María López","hours":20,"depends_on":"API Integration"},{"title":"Merge and Deploy","assignee":"Luis Martínez","hours":10,"depends_on":"Code Review"}]},{"name":"Testing","start":"2026-06-14","end":"2026-06-20","tasks":[{"title":"Unit Testing","assignee":"Luis Martínez","hours":30,"depends_on":null},{"title":"Integration Testing","assignee":"Luis Martínez","hours":30,"depends_on":"Unit Testing"},{"title":"Bug Fix","assignee":"Carlos García","hours":20,"depends_on":"Integration Testing"}]},{"name":"Deployment","start":"2026-06-21","end":"2026-06-30","tasks":[{"title":"Production Deployment","assignee":"Luis Martínez","hours":20,"depends_on":null}]}],"budget":{"total":25000,"breakdown":{"design":8000,"development":15000,"testing":4000}}}