# DeepSeek V3.2 — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 19.552s | tokens_per_second: 34.7
- input_tokens: 471 | output_tokens: 678
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04/2026"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "prep demo para cliente Falabella", "fecha_limite": "23/04/2026"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "28/04/2026", "evento": "Fecha original lanzamiento v2.0"},
    {"fecha": "05/05/2026", "evento": "Nueva fecha lanzamiento v2.0"},
    {"fecha": "16/04/2026", "evento": "Deadline fix bug webhooks"},
    {"fecha": "21/04/2026", "evento": "Próxima reunión equipo"},
    {"fecha": "23/04/2026", "evento": "Demo para cliente Falabella"}
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 al 5 de mayo",
    "Aprobar presupuesto de $8M CLP/mes para contratación de 2 devs senior + 1 QA"
  ]
}
```