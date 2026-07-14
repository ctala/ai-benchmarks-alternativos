# Qwen 3-Next 80B Instruct — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 4.067s | tokens_per_second: 206.6
- input_tokens: 479 | output_tokens: 840
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor.

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-16",
      "evento": "Corrección del bug de webhooks por Seba"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Entrega de JDs por JP (lunes)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Lanzamiento v2.0 (fecha original)"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de la v2.0 del 28 de abril al 5 de mayo",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes",
    "Seba asume la responsabilidad del bug crítico en API webhooks",
    "JP se encarga de crear y publicar los perfiles de los puestos"
  ]
}