# Kimi K2 — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 18.815s | tokens_per_second: 40.5
- input_tokens: 486 | output_tokens: 762
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y accionables, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix bug crítico en API webhooks", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn y GetOnBrd", "fecha_limite": "21/04/26"},
    {"responsable": "JP", "tarea": "Crear job descriptions", "fecha_limite": "21/04/26"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión de equipo producto"},
    {"fecha": "16/04/26", "evento": "Deadline fix webhook (Seba)"},
    {"fecha": "21/04/26", "evento": "Próxima reunión de equipo + deadline JDs (JP)"},
    {"fecha": "23/04/26", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "05/05/26", "evento": "Nueva fecha lanzamiento v2.0 (postergado desde 28/04)"}
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28/04 al 5/05",
    "Seba asume el bug crítico en API webhooks",
    "Aprobado presupuesto de $8M CLP/mes para contratar 3 personas (2 devs senior + 1 QA)",
    "NPS 51 considerado resultado muy bueno"
  ]
}
```