# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — ocr_extraction/handwritten_notes_extraction

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.45 | quality: 8.44
- latency_total: 203.961s | tokens_per_second: 18.5
- input_tokens: 479 | output_tokens: 3769
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Metricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Prox reunion: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha": "14/04",
      "evento": "Reunión equipo producto"
    },
    {
      "fecha": "16/04",
      "evento": "Seba debe fijar bug de webhook"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión (lunes 10am)"
    },
    {
      "fecha": "23/04",
      "evento": "Cami prepara demo para cliente Falabella"
    },
    {
      "fecha": "28/04",
      "evento": "Lanzamiento v2.0 (fecha original)"
    },
    {
      "fecha": "05/05",
      "evento": "Nuevo lanzamiento v2.0 (fecha movida)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Aprobar contratación de 2 devs senior y 1 QA con presupuesto de $8M CLP/mes por cada uno",
    "JP preparará las descripciones de puesto (JD) para el lunes"
  ]
}