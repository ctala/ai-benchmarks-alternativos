# Mistral Small 4 — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.62 | quality: 7.93
- latency_total: 4.897s | tokens_per_second: 145.2
- input_tokens: 480 | output_tokens: 711
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 10am",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fixear bug de webhook", "fecha_limite": "2026-04-16"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "2026-04-23"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn y GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "2026-04-14", "evento": "Reunión equipo prod"},
    {"fecha": "2026-04-28", "evento": "Lanzamiento v2.0 original (reprogramado)"},
    {"fecha": "2026-05-05", "evento": "Lanzamiento v2.0 reprogramado"},
    {"fecha": "2026-04-16", "evento": "Fecha límite para fixear bug de webhook"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión del equipo"},
    {"fecha": "2026-04-23", "evento": "Demo para cliente Falabella"}
  ],
  "decisiones": [
    "Reprogramar lanzamiento v2.0 de abril 28 a mayo 5",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto de $8M CLP/mes por 3 personas",
    "Objetivo de churn para Q1 cumplido (3.1% vs 3.5% objetivo)"
  ]
}
```