# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.73 | quality: 8.44
- latency_total: 26.264s | tokens_per_second: 160.1
- input_tokens: 472 | output_tokens: 4205
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": ""
    },
    {
      "responsable": "JP",
      "tarea": "Hacer JD para lunes (descripción del puesto)",
      "fecha_limite": "21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para fix de bug webhook (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión a las 10am y fecha límite para JD de JP"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Contratar 2 desarrolladores senior y 1 QA.",
    "Presupuesto aprobado de $8M CLP/mes para 3 personas.",
    "JP preparará la descripción del puesto (JD) para el lunes 21/04.",
    "Próxima reunión el lunes 21/04 a las 10am."
  ]
}