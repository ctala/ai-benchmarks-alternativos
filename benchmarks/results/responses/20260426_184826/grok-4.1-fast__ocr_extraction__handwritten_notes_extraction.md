# Grok 4.1 Fast — ocr_extraction/handwritten_notes_extraction

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.35 | quality: 8.44
- latency_total: 15.846s | tokens_per_second: 164.1
- input_tokens: 581 | output_tokens: 2600
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBoard", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo producto"},
    {"fecha": "16/04", "evento": "Seba fija bug webhook (miércoles)"},
    {"fecha": "21/04", "evento": "Próxima reunión (lunes 10am); JP prepara JD"},
    {"fecha": "23/04", "evento": "Demo para cliente Falabella"},
    {"fecha": "28/04", "evento": "Lanzamiento v2.0 original (movido)"},
    {"fecha": "05/05", "evento": "Nuevo lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Seba toma bug crítico en API webhooks",
    "Presupuesto aprobado: $8M CLP/mes x 3 para contratar 2 devs sr + 1 QA",
    "Reportadas métricas Q1: MRR 52.1k (+15%), churn 3.1%, NPS 51"
  ]
}