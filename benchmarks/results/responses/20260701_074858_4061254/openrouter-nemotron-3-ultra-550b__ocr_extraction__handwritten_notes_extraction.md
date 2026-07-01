# Nemotron 3 Ultra 550B — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 6.91 | quality: 7.6
- latency_total: 30.326s | tokens_per_second: 138.3
- input_tokens: 479 | output_tokens: 4195

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/25\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2025-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug en API", "fecha_limite": "2025-04-16"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "2025-04-23"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn y GetOnBoard", "fecha_limite": "2025-04-21"}
  ],
  "fechas_clave": [
    {"fecha": "2025-04-14", "evento": "Reunión equipo producto"},
    {"fecha": "2025-04-16", "evento": "Deadline fix webhook bug (Seba)"},
    {"fecha": "2025-04-21", "evento": "Próxima reunión (lunes 10am) / Deadline JD (JP)"},
    {"fecha": "2025-04-23", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "2025-04-28", "evento": "Fecha original lanzamiento v2.0"},
    {"fecha": "2025-05-05", "evento": "Nueva fecha lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28/04 al 05/05",
    "Seba se hace cargo del bug crítico en API webhooks",
    "Aprobar presupuesto para contratar 2 devs senior + 1 QA: $8M CLP/mes x 3 personas",
    "JP preparará Job Descriptions para el lunes 21/04",
    "Próxima reunión agendada para lunes 21/04 a las 10am"
  ]
}