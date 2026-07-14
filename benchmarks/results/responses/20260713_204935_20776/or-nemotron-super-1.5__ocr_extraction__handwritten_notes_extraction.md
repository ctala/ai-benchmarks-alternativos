# Nemotron Super 49B v1.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 57.821s | tokens_per_second: 53.4
- input_tokens: 470 | output_tokens: 3089
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falto Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crít en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: corregir bug webhook p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "corregir bug webhook", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn y GetOnBoard", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo prod"},
    {"fecha": "16/04/26", "evento": "Seba corregir bug webhook"},
    {"fecha": "21/04/26", "evento": "Próxima reunión"},
    {"fecha": "23/04/26", "evento": "Cami preparar demo para cliente Falabella"},
    {"fecha": "05/05/26", "evento": "Lanzamiento v2.0"}
  ],
  "decisiones": [
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 devs sr y 1 QA",
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "JP encargado de crear y publicar JDs en LinkedIn y GetOnBoard",
    "MaJo actualizar roadmap en Notion",
    "Cami preparar demo para cliente Falabella el 23/04"
  ]
}
```