# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 6.66 | quality: 8.16
- latency_total: 19.669s | tokens_per_second: 195.8
- input_tokens: 472 | output_tokens: 3852
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/2026 Asistentes: JP, MaJo, Seba, Cami (faltó Nico) 1) Lanzamiento v2.0 - mover de abril 28 a mayo 5 - falta QA en módulo pagos - bug crítico en API webhooks (Seba lo toma) 2) Métricas Q1: - MRR 52.1k (+15% vs Q4) - churn bajó a 3.1% (objetivo era 3.5%) - NPS subió a 51 (muy bueno!!) 3) Contratar 2 devs senior + 1 QA - presupuesto aprobado: $8M CLP/mes x 3 pax - JP hace JD para lunes 4) Próxima reunión: lun 21/04 10am Action items: - Seba: fix webhook bug p/ mié 16/04 - MaJo: actualizar roadmap en Notion - Cami: preparar demo para cliente Falabella (23/04) - JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
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
      "tarea": "publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión del equipo"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Fecha límite para preparar demo para cliente Falabella"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA",
    "JP elaborar y publicar job descriptions para lunes"
  ]
}