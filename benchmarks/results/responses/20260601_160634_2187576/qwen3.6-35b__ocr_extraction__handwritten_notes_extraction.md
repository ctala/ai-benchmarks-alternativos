# Qwen 3.6 35B base (OpenRouter FP8) — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.38 | quality: 9.28
- latency_total: 23.982s | tokens_per_second: 227.2
- input_tokens: 480 | output_tokens: 5448
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y acciones específicas, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix bug crítico en API webhooks", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn + GetOnBoard", "fecha_limite": "14/04 (Lunes)"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión del equipo prod y entrega de JDs por JP"},
    {"fecha": "16/04/26", "evento": "Fix bug crítico en webhooks por Seba"},
    {"fecha": "21/04/26", "evento": "Próxima reunión (10:00 AM)"},
    {"fecha": "23/04/26", "evento": "Demo para cliente Falabella"},
    {"fecha": "28/04/26", "evento": "Fecha original de lanzamiento v2.0 (postergada)"},
    {"fecha": "05/05/26", "evento": "Lanzamiento v2.0 (nueva fecha)"}
  ],
  "decisiones": [
    "Postergar el lanzamiento de la versión v2.0 del 28/04 al 05/05.",
    "Aprobar presupuesto de contratación: $8M CLP/mes por 3 personas (2 devs sr + 1 QA).",
    "Agendar próxima reunión para el lunes 21/04 a las 10:00 AM."
  ]
}
```