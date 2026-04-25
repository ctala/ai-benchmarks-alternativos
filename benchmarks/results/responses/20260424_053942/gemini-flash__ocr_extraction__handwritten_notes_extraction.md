# Gemini 2.5 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.41 | quality: 8.16
- latency_total: 4.988s | tokens_per_second: 188.0
- input_tokens: 460 | output_tokens: 938
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar el bug de los webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de puesto (JDs) en LinkedIn y GetOnBrd",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Fecha de la reunión"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión (10:00 AM)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para que Seba arregle el bug de webhook"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Fecha de la demo de Cami para cliente Falabella"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Fecha límite para que JP prepare las descripciones de puesto (JDs)"
    }
  ],
  "decisiones": [
    {
      "punto": "Lanzamiento v2.0",
      "decision": "Mover la fecha de lanzamiento de v2.0 del 28 de abril al 5 de mayo."
    },
    {
      "punto": "Contrataciones",
      "decision": "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA."
    }
  ]
}
```