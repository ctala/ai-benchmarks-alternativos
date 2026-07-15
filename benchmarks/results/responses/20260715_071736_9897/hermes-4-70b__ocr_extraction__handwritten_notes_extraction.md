# Hermes 4 70B — ocr_extraction/handwritten_notes_extraction

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 7.247s | tokens_per_second: 90.8
- input_tokens: 466 | output_tokens: 658
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falto Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunion: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualzar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "2026-04-16"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "2026-04-23"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn y GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "2026-04-28", "evento": "Lanzamiento v2.0 original"},
    {"fecha": "2026-05-05", "evento": "Lanzamiento v2.0 actualizado"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión"},
    {"fecha": "2026-04-16", "evento": "Fecha límite para arreglar bug de webhook"},
    {"fecha": "2026-04-23", "evento": "Presentación de demo para Falabella"}
  ],
  "decisiones": [
    "Mover lanzamiento de v2.0 del 28 de abril al 5 de mayo",
    "Contratar 2 desarrolladores senior y 1 tester QA",
    "Aprobar presupuesto de $8M CLP/mes para 3 personas"
  ]
}