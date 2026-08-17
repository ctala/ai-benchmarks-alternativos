# GPT-OSS 120B — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 31.036s | tokens_per_second: 42.3
- input_tokens: 498 | output_tokens: 1312
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión de equipo product"
    },
    {
      "fecha": "28/04/26",
      "evento": "Fecha original de lanzamiento v2.0 (reprogramada)"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nuevo lanzamiento v2.0"
    },
    {
      "fecha": "16/04/26",
      "evento": "Entrega de fix al bug de webhook"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo para cliente Falabella"
    }
  ],
  "decisiones": [
    "Reprogramar lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Asignar QA al módulo de pagos.",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes.",
    "JP redactará los JD para el lunes siguiente.",
    "Fijar próxima reunión para el 21/04 a las 10 am."
  ]
}
```