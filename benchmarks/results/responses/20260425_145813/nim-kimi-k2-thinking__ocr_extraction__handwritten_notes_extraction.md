# Kimi K2 Thinking (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 6.75 | quality: 8.44
- latency_total: 76.974s | tokens_per_second: 26.6
- input_tokens: 464 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

 ```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\n\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5 - falta QA en módulo pagos - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n- MRR 52.1k (+15% vs Q4)\n- churn bajó a 3.1% (obj era 3.5%)\n- NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA - presup aprob: $8M CLP/mes x 3 pax - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Límite fix webhook bug (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión 10am"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original lanzamiento v2.0 (MOVIDA)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al