# Nemotron 3.5 Lightning — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 10.715s | tokens_per_second: 751.4
- input_tokens: 479 | output_tokens: 8052
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunion equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de 28/04 a 05/05\n   - falta QA en modulo de pagos\n   - bug critico en API webhooks (Seba lo toma)\n\n2) Metricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajo a 3.1% (objetivo era 3.5%)\n   - NPS subio a 51 (Buen!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprob: $8M CLP/mes x 3 puestos\n   - JP elabora JD para el lunes\n\n4) Proxima reunion: lun 21/04 10am\n\nAction items:\n- Seba: corregir bug de webhooks para el miercoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Corregir bug de webhooks en API", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn y GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunion actual"},
    {"fecha": "28/04/26", "evento": "Lanzamiento v2.0 (original)"},
    {"fecha": "05/05/26", "evento": "Lanzamiento v2.0 (reprogramado)"},
    {"fecha": "16/04/26", "evento": "Seba: corregir bug webhook"},
    {"fecha": "21/04/26", "evento": "Proxima reunion a las 10am"},
    {"fecha": "23/04/26", "evento": "Cami: demo para cliente Falabella"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Metricas Q1: MRR 52.1k (+15% vs Q4), churn bajo a 3.1% (objetivo 3.5%), NPS subió a 51 (Buen!!)",
    "Aprobar contratacion de 2 devs senior + 1 QA con presupuesto $8M CLP/mes x 3 puestos",
    "JP responsable de elaborar y publicar JDs en LinkedIn + GetOnBrd",
    "Seba a cargo del bug critico en API webhooks",
    "Próxima reunion programada para el lunes 21/04 a las 10am"
  ]
}