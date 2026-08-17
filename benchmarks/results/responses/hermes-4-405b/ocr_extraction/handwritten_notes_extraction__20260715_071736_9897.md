# Hermes 4 405B — ocr_extraction/handwritten_notes_extraction

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 21.867s | tokens_per_second: 31.2
- input_tokens: 466 | output_tokens: 683
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena estructura y utilidad práctica, proporcionando detalles útiles y organizados para un emprendedor.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajo a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "prep demo p/ cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "28/04/26", "evento": "Fecha original lanzamiento v2.0"},
    {"fecha": "05/05/26", "evento": "Nueva fecha lanzamiento v2.0"},
    {"fecha": "16/04/26", "evento": "Deadline fix webhook bug"},
    {"fecha": "23/04/26", "evento": "Demo cliente Falabella"},
    {"fecha": "21/04/26", "evento": "Próxima reunión"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Seba se hará cargo de fixear bug en API webhooks",
    "Contratar 2 devs sr y 1 QA con presupuesto aprobado de $8M CLP/mes por 3 pax",
    "JP creará JDs para lunes",
    "Próxima reunión el lunes 21/04 a las 10am"
  ]
}