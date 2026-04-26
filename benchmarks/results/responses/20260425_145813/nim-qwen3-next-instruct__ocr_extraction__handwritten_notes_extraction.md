# Qwen 3-Next 80B Instruct (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.05 | quality: 8.44
- latency_total: 27.344s | tokens_per_second: 28.4
- input_tokens: 459 | output_tokens: 777
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5 - falta QA en módulo pagos - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n- MRR: 52.1k (+15% vs Q4)\n- Churn bajó a 3.1% (obj era 3.5%)\n- NPS subió a 51 (¡muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA - presupuesto aprobado: $8M CLP/mes x 3 pax - JP hace JDs para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
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
      "tarea": "publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": "2026-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fix bug webhooks (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de v2.0 del 28/04 al 05/05",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes",
    "JP se encargará de crear los perfiles de trabajo (JDs) para el lunes 21/04"
  ]
}