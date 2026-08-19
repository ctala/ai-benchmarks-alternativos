# Muse Glimmer 30B — ocr_extraction/handwritten_notes_extraction

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 37.548s | tokens_per_second: 65.0
- input_tokens: 452 | output_tokens: 2439
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad en los insights proporcionados.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falto Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunion: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "28/04",
      "evento": "Lanzamiento v2.0 originalmente programado - postergado"
    },
    {
      "fecha": "05/05",
      "evento": "Lanzamiento v2.0 reprogramado"
    },
    {
      "fecha": "16/04",
      "evento": "Deadline fix webhook bug por Seba"
    },
    {
      "fecha": "21/04 10am",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04",
      "evento": "Demo para cliente Falabella por Cami"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28 de abril a 5 de mayo",
    "Falta QA en módulo pagos para lanzamiento v2.0",
    "Seba toma bug crítico en API webhooks",
    "Aprobar presupuesto de $8M CLP/mes x 3 personas para contratar 2 devs sr + 1 QA",
    "JP elabora JD para el lunes"
  ]
}