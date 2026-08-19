# Hermes 4 405B — ocr_extraction/handwritten_notes_extraction

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 7.05 | quality: 8.44
- latency_total: 24.693s | tokens_per_second: 30.0
- input_tokens: 466 | output_tokens: 740
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajo a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha": "28/04",
      "evento": "Fecha original lanzamiento v2.0"
    },
    {
      "fecha": "05/05",
      "evento": "Nueva fecha lanzamiento v2.0"
    },
    {
      "fecha": "16/04",
      "evento": "Fix webhook bug (Seba)"
    },
    {
      "fecha": "18/04",
      "evento": "JP hace JD"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión 10am"
    },
    {
      "fecha": "23/04",
      "evento": "Demo cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Seba toma bug crítico en API webhooks",
    "Contratar 2 devs sr + 1 QA con presupuesto aprobado de $8M CLP/mes por persona",
    "JP hará JD para lunes",
    "Próxima reunión el lunes 21/04 a las 10am"
  ]
}