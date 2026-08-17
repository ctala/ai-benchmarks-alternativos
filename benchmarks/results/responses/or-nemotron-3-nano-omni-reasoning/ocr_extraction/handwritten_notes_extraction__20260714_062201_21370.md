# Nemotron 3 Nano Omni 30B-A3B Reasoning — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 21.952s | tokens_per_second: 151.2
- input_tokens: 479 | output_tokens: 3320
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprob: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para mié 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión del equipo"
    },
    {
      "fecha": "5/05/26",
      "evento": "Lanzamiento v2.0 (reprogramado)"
    },
    {
      "fecha": "16/04/26",
      "evento": "Fecha límite para fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04/26",
      "evento": "Fecha límite demo cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 5/05",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA",
    "Contratar 2 devs senior + 1 QA"
  ]
}