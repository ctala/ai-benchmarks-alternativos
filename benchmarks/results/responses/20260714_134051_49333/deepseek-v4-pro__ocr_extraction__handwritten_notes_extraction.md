# DeepSeek V4 Pro — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 161.945s | tokens_per_second: 48.9
- input_tokens: 551 | output_tokens: 7923
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad en la interpretación de las notas manuscritas, y los datos extraídos son exactos.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/2025\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - falta QA en módulo de pagos\n   - bug crítico en API de webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP prepara JDs para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: arreglar bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBoard",
  "fecha_reunion": "2025-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar bug de webhook",
      "fecha_limite": "2025-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2025-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2025-04-14",
      "evento": "Reunión de equipo prod"
    },
    {
      "fecha": "2025-04-16",
      "evento": "Fecha límite para Seba: arreglar bug de webhook"
    },
    {
      "fecha": "2025-04-21",
      "evento": "Próxima reunión de equipo (10am) / JP prepara JDs para este día"
    },
    {
      "fecha": "2025-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "2025-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2025-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28 de abril al 5 de mayo debido a falta de QA en módulo de pagos y bug crítico en API de webhooks.",
    "Seba se encargará del bug crítico en API de webhooks.",
    "Contratar 2 desarrolladores senior y 1 QA, con presupuesto aprobado de $8M CLP/mes por persona.",
    "JP preparará las descripciones de puesto (JDs) para el lunes (posiblemente 21/04).",
    "Próxima reunión el lunes 21 de abril a las 10:00 am."
  ]
}