# Nemotron Nano 9B v2 — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 39.494s | tokens_per_second: 37.5
- input_tokens: 475 | output_tokens: 1480
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y accionables, y los datos extraídos son exactos.

## Respuesta completa



{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (ausente: Nico)\n\n1) Lanzamiento v2.0 - mover de 28/abril a 5/mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (re buena!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hará JD para lunes\n\n4) Próxima reunión: lun 21/04 a las 10am\n\nAcciones:\n- Seba: corregir bug del webhook para 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "corregir bug del webhook", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn y GetOnBoard", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo producto"},
    {"fecha": "28/abril", "evento": "Lanzamiento v2.0 (fecha de cambio)"},
    {"fecha": "5/mayo", "evento": "Lanzamiento v2.0 (fecha de cambio)"},
    {"fecha": "21/04", "evento": "Próxima reunión"},
    {"fecha": "16/04", "evento": "Fecha límite para Seba"},
    {"fecha": "23/04", "evento": "Fecha límite para Cami"}
  ],
  "decisiones": [
    "Aprobación de contratación de 2 devs senior y 1 QA con presupuesto $8M CLP/mes"
  ]
}
