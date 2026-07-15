# Gemini 2.5 Pro — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 30.776s | tokens_per_second: 130.9
- input_tokens: 458 | output_tokens: 4030
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo de producto - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos.\n   - Bug crítico en API de webhooks (Seba lo toma).\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4).\n   - Churn bajó a 3.1% (objetivo era 3.5%).\n   - NPS subió a 51 (muy bueno).\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8.000.000 CLP/mes por 3 personas.\n   - JP hace las descripciones de cargo (Job Descriptions) para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10am.\n\nAction items:\n- Seba: Corregir bug de webhooks para el miércoles 16/04.\n- MaJo: Actualizar roadmap en Notion.\n- Cami: Preparar demo para cliente Falabella (para el 23/04).\n- JP: Publicar las descripciones de cargo en LinkedIn y GetOnBoard.",
  "fecha_reunion": "2026-04-14",
  "asistentes": [
    "JP",
    "MaJo",
    "Seba",
    "Cami"
  ],
  "ausentes": [
    "Nico"
  ],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug crítico en la API de webhooks.",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap del producto en Notion.",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar la demo para el cliente Falabella.",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Preparar las descripciones de cargo (Job Descriptions).",
      "fecha_limite": "2026-04-17"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de cargo en LinkedIn y GetOnBoard.",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto."
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para corregir bug de webhooks (Seba)."
    },
    {
      "fecha": "2026-04-17",
      "evento": "Fecha límite para preparar descripciones de cargo (JP)."
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 am)."
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para el cliente Falabella."
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original (cancelada) del lanzamiento v2.0."
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha para el lanzamiento de la v2.0."
    }
  ],
  "decisiones": [
    "Retrasar el lanzamiento de la v2.0 del 28 de abril al 5 de mayo debido a issues pendientes.",
    "Aprobar la contratación de 2 desarrolladores senior y 1 QA.",
    "Asignar un presupuesto de $8.000.000 CLP mensuales para las 3 nuevas contrataciones."
  ]
}
```