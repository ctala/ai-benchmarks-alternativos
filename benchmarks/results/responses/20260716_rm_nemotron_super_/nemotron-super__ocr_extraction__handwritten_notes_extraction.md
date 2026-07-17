# Nemotron 3 Super — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.03 | quality: 10.0
- latency_total: 12.392s | tokens_per_second: 64.8
- input_tokens: 463 | output_tokens: 803
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor.

## Respuesta completa



{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
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
      "tarea": "fix webhook bug",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "21/04/2026 10:00",
      "evento": "Próxima reunión (lunes 21/04 10am)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Deadline para fix de bug webhook (Seba)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Deadline para demo cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Aprobar presupuesto de $8M CLP/mes x 3 pax para contratación de 2 devs senior y 1 QA",
    "Asignar a Seba la corrección del bug crítico en API webhooks",
    "Encargar a JP la elaboración de las JDs para el lunes"
  ]
}