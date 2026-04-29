# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — ocr_extraction/handwritten_notes_extraction

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 6.47 | quality: 7.9
- latency_total: 70.042s | tokens_per_second: 65.1
- input_tokens: 480 | output_tokens: 4563
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsist: JP, Majo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: arreglar bug webhook para el miércoles 16/04\n- Majo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "Majo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "arreglar bug webhook",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "Majo",
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
      "tarea": "publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "19/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 originalmente programado"
    },
    {
      "fecha": "5/05/2026",
      "evento": "Lanzamiento v2.0 reprogramado"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para que Seba arregle el bug de webhook"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión (lunes 21/04 10am)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Fecha límite para Cami preparar demo para Falabella"
    },
    {
      "fecha": "19/04/2026",
      "evento": "Fecha límite para JP publicar JDs en LinkedIn y GetOnBoard"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 devs senior y 1 QA",
    "Contratar 2 devs senior + 1 QA"
  ]
}