# Qwen 2.5 72B — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 20.209s | tokens_per_second: 36.3
- input_tokens: 479 | output_tokens: 734
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2023\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2023",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04/2023"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "prep demo p/ cliente Falabella", "fecha_limite": "23/04/2023"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "28/04/2023", "evento": "Fecha original del lanzamiento v2.0"},
    {"fecha": "05/05/2023", "evento": "Nueva fecha del lanzamiento v2.0"},
    {"fecha": "16/04/2023", "evento": "Fecha límite para fix webhook bug"},
    {"fecha": "23/04/2023", "evento": "Demo para cliente Falabella"},
    {"fecha": "21/04/2023", "evento": "Próxima reunión"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Contratar 2 devs sr y 1 QA con un presupuesto de $8M CLP/mes",
    "JP hará los JDs para lunes",
    "Próxima reunión el lunes 21/04 a las 10am"
  ]
}
```