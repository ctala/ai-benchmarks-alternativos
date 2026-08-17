# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.44 | quality: 9.28
- latency_total: 8.267s | tokens_per_second: 95.7
- input_tokens: 472 | output_tokens: 791
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al estructurar la información y extraer detalles clave, como las tareas y fechas importantes.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fix webhook bug por Seba"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Lanzamiento v2.0 se mueve del 28 de abril al 5 de mayo",
    "Se contrata 2 devs senior + 1 QA con presupuesto de $8M CLP/mes total",
    "JP se encarga de hacer el JD para el lunes"
  ]
}
```