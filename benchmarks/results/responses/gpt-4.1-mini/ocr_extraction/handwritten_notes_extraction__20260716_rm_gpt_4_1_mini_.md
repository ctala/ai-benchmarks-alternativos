# GPT-4.1 Mini — ocr_extraction/handwritten_notes_extraction

- model_id: `gpt-4.1-mini`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 9.19s | tokens_per_second: 85.1
- input_tokens: 438 | output_tokens: 782
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad y utilidad práctica, y los datos extraídos son exactos.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (falto Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión del equipo de producción"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para que Seba arregle el bug del webhook"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo a las 10am"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella preparada por Cami"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nuevo lanzamiento v2.0 (pospuesto desde 28/04)"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Lunes para que JP haga JD (Job Descriptions)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28 de abril a 5 de mayo",
    "Seba se encargará de corregir el bug crítico en API webhooks",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes para los 3",
    "JP hará las descripciones de trabajo (JD) para el lunes siguiente",
    "Próxima reunión programada para el 21 de abril a las 10am"
  ]
}