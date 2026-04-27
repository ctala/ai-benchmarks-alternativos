# Grok 4.20 — ocr_extraction/handwritten_notes_extraction

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.1 | quality: 8.44
- latency_total: 6.612s | tokens_per_second: 120.7
- input_tokens: 550 | output_tokens: 798
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": null
    },
    {
      "responsable": "JP",
      "tarea": "Hacer Job Descriptions (JDs)",
      "fecha_limite": "2026-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Seba debe entregar fix del bug de webhooks"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0 (pospuesta)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Se pospuso el lanzamiento de la v2.0 del 28 de abril al 5 de mayo",
    "Se aprobó presupuesto de $8M CLP/mes para contratar 2 devs senior + 1 QA",
    "JP se encargará de crear las Job Descriptions para el lunes",
    "Seba se asignó la corrección del bug crítico de la API de webhooks"
  ]
}
```