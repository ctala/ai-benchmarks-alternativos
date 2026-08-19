# GPT-5.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `gpt-5.5`
- success: True  | final: 6.56 | quality: 8.16
- latency_total: 14.849s | tokens_per_second: 91.4
- input_tokens: 437 | output_tokens: 1357
- judge_score: 4.2 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo producto - 14/04/25\nAsistentes: JP, MaJo, Seba, Cami. Ausente: Nico.\n\n1) Lanzamiento v2.0: mover de 28/04 a 05/05.\n   - Falta QA en módulo de pagos.\n   - Bug crítico en API webhooks. Seba lo toma.\n\n2) Métricas Q1:\n   - MRR: 52.1k (+15% vs Q4).\n   - Churn bajó a 3.1% (objetivo era 3.5%).\n   - NPS subió a 51. Muy bueno.\n\n3) Contratar 2 desarrolladores senior + 1 QA.\n   - Presupuesto aprobado: $8M CLP/mes para 3 personas.\n   - JP hace las descripciones de cargo para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10:00.\n\nAction items:\n- Seba: corregir bug de webhooks para el miércoles 16/04.\n- MaJo: actualizar roadmap en Notion.\n- Cami: preparar demo para cliente Falabella el 23/04.\n- JP: publicar JDs en LinkedIn y GetOnBrd.",
  "fecha_reunion": "2025-04-14",
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
      "tarea": "Corregir bug crítico en la API de webhooks",
      "fecha_limite": "2025-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2025-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": null
    },
    {
      "responsable": "JP",
      "tarea": "Preparar descripciones de cargo para las nuevas contrataciones",
      "fecha_limite": "2025-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2025-04-14",
      "evento": "Reunión de equipo producto"
    },
    {
      "fecha": "2025-04-16",
      "evento": "Fecha límite para corregir bug crítico de webhooks"
    },
    {
      "fecha": "2025-04-21",
      "evento": "Próxima reunión a las 10:00 y fecha límite para que JP prepare las descripciones de cargo"
    },
    {
      "fecha": "2025-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2025-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2025-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28/04 al 05/05.",
    "Seba tomará el bug crítico en la API de webhooks.",
    "Contratar 2 desarrolladores senior y 1 QA.",
    "Presupuesto aprobado de $8M CLP mensuales para 3 personas."
  ]
}