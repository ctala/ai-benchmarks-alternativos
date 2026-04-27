# Nemotron 3 Nano 30B — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.55 | quality: 8.44
- latency_total: 32.616s | tokens_per_second: 99.2
- input_tokens: 479 | output_tokens: 3236
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miercoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "prep demo p/ cliente Falabella",
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
      "fecha": "14/04/2026",
      "evento": "Reunión inicial"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 (fecha original)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión a las 10am"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite de Seba (fix webhook bug)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Fecha límite de Cami (prep demo cliente Falabella)"
    }
  ],
  "decisiones": [
    "Mover Lanzamiento v2.0 de 28/04 a 05/05",
    "Churn bajó a 3.1% (objetivo 3.5% cumplido)",
    "NPS subió a 51 (re buena)",
    "Presupuesto aprobado: $8M CLP/mes por cada uno de los 3 puestos",
    "Contratar 2 desarrolladores senior y 1 QA"
  ]
}