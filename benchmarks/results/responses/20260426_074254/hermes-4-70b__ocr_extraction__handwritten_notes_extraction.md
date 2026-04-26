# Hermes 4 70B — ocr_extraction/handwritten_notes_extraction

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 7.3 | quality: 8.44
- latency_total: 8.598s | tokens_per_second: 75.6
- input_tokens: 466 | output_tokens: 650
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunion: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualzar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "28/04", "evento": "Fecha original de lanzamiento v2.0"},
    {"fecha": "05/05", "evento": "Nueva fecha de lanzamiento v2.0"},
    {"fecha": "16/04", "evento": "Fecha límite para fix webhook bug"},
    {"fecha": "23/04", "evento": "Fecha de demo para cliente Falabella"},
    {"fecha": "21/04", "evento": "Próxima reunión del equipo"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Aprobar presupuesto de $8M CLP/mes para 3 pax",
    "JP creará los JDs para el lunes"
  ]
}