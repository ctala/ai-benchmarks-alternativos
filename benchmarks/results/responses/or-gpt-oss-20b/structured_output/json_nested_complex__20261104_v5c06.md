# GPT-OSS 20B — structured_output/json_nested_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.31 | quality: 10.0
- latency_total: 11.24s | tokens_per_second: 143.9
- input_tokens: 261 | output_tokens: 1617

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

{"project":"Rediseño sitio web","start_date":"2026-05-01","end_date":"2026-06-30","team":[{"name":"Ana Martínez","role":"Diseñadora UI/UX","allocation_pct":25},{"name":"Luis Pérez","role":"Desarrollador Frontend","allocation_pct":35},{"name":"María Gómez","role":"Desarrollador Backend","allocation_pct":35},{"name":"Carlos Ruiz","role":"QA","allocation_pct":5}],"phases":[{"name":"Planificación","start":"2026-05-01","end":"2026-05-05","tasks":[{"title":"Reunión de kick-off","assignee":"Luis Pérez","hours":8,"depends_on":null},{"title":"Análisis de requisitos","assignee":"Ana Martínez","hours":12,"depends_on":"Reunión de kick-off"},{"title":"Documentación de requisitos","assignee":"Luis Pérez","hours":8,"depends_on":"Análisis de requisitos"}]},{"name":"Diseño","start":"2026-05-06","end":"2026-05-20","tasks":[{"title":"Wireframes","assignee":"Ana Martínez","hours":20,"depends_on":"Documentación de requisitos"},{"title":"Mockups de alta fidelidad","assignee":"Ana Martínez","hours":30,"depends_on":"Wireframes"},{"title":"Revisión de diseño con stakeholders","assignee":"Ana Martínez","hours":10,"depends_on":"Mockups de alta fidelidad"}]},{"name":"Desarrollo","start":"2026-05-21","end":"2026-06-15","tasks":[{"title":"Configuración del entorno","assignee":"Luis Pérez","hours":8,"depends_on":"Revisión de diseño con stakeholders"},{"title":"Implementación del frontend","assignee":"Luis Pérez","hours":80,"depends_on":"Configuración del entorno"},{"title":"Implementación del backend","assignee":"María Gómez","hours":80,"depends_on":"Configuración del entorno"},{"title":"Integración frontend-backend","assignee":"Luis Pérez","hours":20,"depends_on":"Implementación del backend"}]},{"name":"Pruebas","start":"2026-06-16","end":"2026-06-25","tasks":[{"title":"Pruebas unitarias","assignee":"Carlos Ruiz","hours":20,"depends_on":"Implementación del backend"},{"title":"Pruebas de integración","assignee":"Carlos Ruiz","hours":15,"depends_on":"Pruebas unitarias"},{"title":"Pruebas de aceptación","assignee":"Carlos Ruiz","hours":20,"depends_on":"Pruebas de integración"}]},{"name":"Lanzamiento","start":"2026-06-26","end":"2026-06-30","tasks":[{"title":"Implementación en entorno de producción","assignee":"Luis Pérez","hours":8,"depends_on":"Pruebas de aceptación"},{"title":"Monitoreo post-lanzamiento","assignee":"Carlos Ruiz","hours":12,"depends_on":"Implementación en entorno de producción"}]}],"budget":{"total":25000,"breakdown":{"design":7000,"development":12000,"testing":3000}}}